// Test JavaScript functionality
console.log("=== JavaScript Functionality Test ===");

// Test 1: Check if localStorage is available
function testLocalStorage() {
    try {
        localStorage.setItem('test', 'value');
        const retrieved = localStorage.getItem('test');
        localStorage.removeItem('test');
        return retrieved === 'value';
    } catch (e) {
        return false;
    }
}

// Test 2: Check if fetch API is available
function testFetchAPI() {
    return typeof fetch === 'function';
}

// Test 3: Check if the generateName function would work
function testGenerateFunction() {
    return typeof generateName === 'function';
}

// Run tests
console.log("Test 1 - localStorage available:", testLocalStorage() ? "✅ PASS" : "❌ FAIL");
console.log("Test 2 - fetch API available:", testFetchAPI() ? "✅ PASS" : "❌ FAIL");
console.log("Test 3 - generateName function exists:", testGenerateFunction() ? "✅ PASS" : "❌ FAIL");

// Test API call
async function testAPICall() {
    try {
        const response = await fetch('/api/generate');
        if (response.ok) {
            const data = await response.json();
            console.log("Test 4 - API call successful:", "✅ PASS - Name:", data.name);
            return true;
        } else {
            console.log("Test 4 - API call failed:", "❌ FAIL - Status:", response.status);
            return false;
        }
    } catch (error) {
        console.log("Test 4 - API call error:", "❌ FAIL - Error:", error.message);
        return false;
    }
}

// Run API test
testAPICall().then(success => {
    console.log("\n=== Test Summary ===");
    console.log("All core functionality tests completed.");
    console.log("The UI should work if all tests pass.");
});
