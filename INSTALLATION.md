# Installation Guide for Fixed LangChain Sandbox

This fork of langchain-sandbox includes critical fixes for matplotlib support in headless environments.

## Key Fixes
- ✅ Fixed matplotlib backend configuration for Pyodide environments
- ✅ Corrected import detection to properly handle submodule imports
- ✅ Ensured compatibility with all Pyodide-supported packages

## Installation Options

### Option 1: Install from GitHub (Recommended)
```bash
pip install git+https://github.com/johannhartmann/langchain-sandbox.git#subdirectory=libs/sandbox-py
```

### Option 2: Install from Local Build
If you have cloned the repository:
```bash
cd libs/sandbox-py
pip install -e .  # For development
# or
pip install .     # For production
```

### Option 3: Install Built Wheel
```bash
pip install dist/langchain_sandbox-0.0.7-py3-none-any.whl
```

## Verify Installation
```python
from langchain_sandbox.pyodide import PyodideSandbox

# Test matplotlib support
sandbox = PyodideSandbox()
result = await sandbox.execute("""
import matplotlib.pyplot as plt
print("matplotlib works!")
""")
print(result.stdout)  # Should print: matplotlib works!
```

## Important Notes
- This fork uses the local TypeScript implementation with matplotlib fixes
- The official PyPI package (0.0.6) does NOT include these fixes
- Ensure you're using version 0.0.7 or later from this fork

## Matplotlib Support
This version correctly configures matplotlib to use the 'Agg' backend for headless environments, fixing the common error:
- ❌ "Failed to install required Python packages: matplotlib.pyplot"
- ❌ "ImportError: cannot import name 'document' from 'js'"

Both errors are now resolved in this fork.