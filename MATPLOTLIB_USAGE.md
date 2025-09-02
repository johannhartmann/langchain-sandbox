# Matplotlib Usage in LangChain Sandbox

## Overview

Matplotlib works perfectly in the LangChain Sandbox! Since the sandbox runs in a headless backend environment (not in a browser), you need to use the **Agg backend** for matplotlib.

## Correct Usage

Always set the backend to 'Agg' before importing pyplot:

```python
import matplotlib
matplotlib.use('Agg')  # Must be before importing pyplot
import matplotlib.pyplot as plt
```

## Complete Example

```python
from langchain_sandbox import PyodideSandbox
import asyncio

async def create_plot():
    sandbox = PyodideSandbox(allow_net=True)
    
    code = """
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

# Create your plot
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave')
plt.grid(True)
plt.legend()

# Save to bytes buffer
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)

# Convert to base64 for transmission
img_base64 = base64.b64encode(buf.read()).decode('utf-8')
buf.close()

print(f"Plot created! Image size: {len(img_base64)} bytes")
# Return the base64 image data
img_base64
"""
    
    result = await sandbox.execute(code)
    if result.status == "success":
        # result.result contains the base64 image
        print("Plot generated successfully!")
        return result.result
    else:
        print(f"Error: {result.stderr}")
        return None

# Run the example
asyncio.run(create_plot())
```

## Common Issues and Solutions

### Issue: ImportError with 'document' from 'js'
**Cause**: Using the default interactive backend which expects a browser environment.
**Solution**: Always use `matplotlib.use('Agg')` before importing pyplot.

### Issue: plt.show() doesn't work
**Cause**: `plt.show()` requires an interactive backend with a display.
**Solution**: Use `plt.savefig()` to save to a buffer or file instead.

## Supported Operations

✅ **Supported:**
- All matplotlib plotting functions
- Saving plots to memory buffers or files
- Converting plots to base64 for data transmission
- All non-interactive matplotlib features

❌ **Not Supported:**
- `plt.show()` - requires interactive display
- Interactive widgets
- Animation with interactive controls
- Any feature requiring a browser DOM

## Best Practices

1. **Always set the backend first**: Call `matplotlib.use('Agg')` before any pyplot imports
2. **Use BytesIO buffers**: Save plots to memory instead of files for better performance
3. **Return base64 data**: Convert images to base64 for easy transmission
4. **Close resources**: Always close buffers after use to free memory

## Performance Notes

- First import may be slow due to font cache building
- Subsequent plots will be faster
- The sandbox caches installed packages between executions (when stateful=True)