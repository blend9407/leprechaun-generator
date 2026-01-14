"""
Database caching module for Leprechaun Name Generator
Provides in-memory caching for names database with periodic persistence
"""

import os
import json
import threading
import time
from datetime import datetime

class NameDatabaseCache:
    """
    In-memory cache for names database with automatic persistence
    """

    def __init__(self, db_file='names.json', auto_save_interval=300):
        """
        Initialize the cache

        Args:
            db_file: Path to JSON database file
            auto_save_interval: Seconds between automatic saves (default: 5 minutes)
        """
        self.db_file = db_file
        self.auto_save_interval = auto_save_interval
        self.cache = []  # In-memory cache of names
        self.modified = False
        self.lock = threading.Lock()
        self.save_thread = None
        self.running = False

        # Load initial data
        self._load_from_disk()

        # Start auto-save thread
        self._start_auto_save()

    def _load_from_disk(self):
        """Load data from JSON file into cache"""
        try:
            if os.path.exists(self.db_file):
                with open(self.db_file, 'r') as f:
                    self.cache = json.load(f)
                print(f"Loaded {len(self.cache)} names from {self.db_file}")
            else:
                self.cache = []
                print(f"Database file {self.db_file} does not exist, starting with empty cache")
        except Exception as e:
            print(f"Error loading database: {e}")
            self.cache = []

    def _save_to_disk(self):
        """Save cache to JSON file"""
        try:
            with open(self.db_file, 'w') as f:
                json.dump(self.cache, f, indent=2)
            self.modified = False
            print(f"Saved {len(self.cache)} names to {self.db_file}")
            return True
        except Exception as e:
            print(f"Error saving database: {e}")
            return False

    def _auto_save_worker(self):
        """Background thread for periodic saving"""
        while self.running:
            time.sleep(self.auto_save_interval)
            with self.lock:
                if self.modified:
                    self._save_to_disk()

    def _start_auto_save(self):
        """Start the auto-save background thread"""
        self.running = True
        self.save_thread = threading.Thread(target=self._auto_save_worker, daemon=True)
        self.save_thread.start()
        print(f"Auto-save thread started (interval: {self.auto_save_interval}s)")

    def stop(self):
        """Stop the cache and save any pending changes"""
        self.running = False
        if self.save_thread:
            self.save_thread.join(timeout=5)
        if self.modified:
            self._save_to_disk()
        print("Cache stopped")

    def get_all(self):
        """Get all names from cache"""
        with self.lock:
            return self.cache.copy()

    def add(self, name_data):
        """Add a new name to cache"""
        with self.lock:
            # Add timestamp if not present
            if 'timestamp' not in name_data:
                name_data['timestamp'] = datetime.now().isoformat()

            self.cache.append(name_data)
            self.modified = True
            return len(self.cache) - 1  # Return index of added item

    def get_count(self):
        """Get count of names in cache"""
        with self.lock:
            return len(self.cache)

    def save_now(self):
        """Force immediate save to disk"""
        with self.lock:
            return self._save_to_disk()

    def clear(self):
        """Clear the cache (use with caution)"""
        with self.lock:
            self.cache = []
            self.modified = True
            self._save_to_disk()
            return True

# Global cache instance
_name_cache = None

def init_cache(db_file='names.json', auto_save_interval=300):
    """Initialize the global cache"""
    global _name_cache
    if _name_cache is None:
        _name_cache = NameDatabaseCache(db_file, auto_save_interval)
    return _name_cache

def get_cache():
    """Get the global cache instance"""
    global _name_cache
    if _name_cache is None:
        raise RuntimeError("Cache not initialized. Call init_cache() first.")
    return _name_cache

def stop_cache():
    """Stop the global cache"""
    global _name_cache
    if _name_cache:
        _name_cache.stop()
        _name_cache = None
