"""
Template loader module for Leprechaun Name Generator
Pre-loads PDF templates at startup for improved performance
"""

import os

class TemplateLoader:
    """
    Pre-loads and caches PDF templates
    """

    def __init__(self, template_dir='pdf-templates'):
        """
        Initialize template loader

        Args:
            template_dir: Directory containing PDF templates
        """
        self.template_dir = template_dir
        self.templates = {}
        self._load_all_templates()

    def _load_all_templates(self):
        """Load all templates from template directory"""
        template_files = {
            'classic-emerald': 'classic-emerald-template.html',
            'pot-of-gold': 'pot-of-gold-template.html',
            'rainbow-magic': 'rainbow-magic-template.html'
        }

        for template_name, filename in template_files.items():
            filepath = os.path.join(self.template_dir, filename)
            try:
                with open(filepath, 'r') as f:
                    self.templates[template_name] = f.read()
                print(f"Loaded template: {template_name} from {filename}")
            except Exception as e:
                print(f"Error loading template {template_name} from {filepath}: {e}")
                self.templates[template_name] = ''

        print(f"Loaded {len(self.templates)} templates")

    def get_template(self, template_name):
        """
        Get a template by name

        Args:
            template_name: Name of the template

        Returns:
            Template content as string, or empty string if not found
        """
        return self.templates.get(template_name, '')

    def get_all_templates(self):
        """Get all loaded templates"""
        return self.templates.copy()

    def reload(self):
        """Reload all templates from disk"""
        self.templates.clear()
        self._load_all_templates()
        return len(self.templates)

# Global template loader instance
_template_loader = None

def init_template_loader(template_dir='pdf-templates'):
    """Initialize the global template loader"""
    global _template_loader
    if _template_loader is None:
        _template_loader = TemplateLoader(template_dir)
    return _template_loader

def get_template_loader():
    """Get the global template loader instance"""
    global _template_loader
    if _template_loader is None:
        raise RuntimeError("Template loader not initialized. Call init_template_loader() first.")
    return _template_loader
