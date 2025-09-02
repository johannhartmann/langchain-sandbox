#!/usr/bin/env python3
"""Test local JS implementation with matplotlib"""

import asyncio
import sys
from pathlib import Path


# Add the local package to path
sys.path.insert(0, str(Path(__file__).parent / "libs" / "sandbox-py"))

from langchain_sandbox import PyodideSandbox


async def test():
    """Test matplotlib with local JS implementation"""
    print("Testing local JS implementation...")
    print(f"Using JS from: {PyodideSandbox.__module__}")

    sandbox = PyodideSandbox(allow_net=True)

    code = """
import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Create plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave')
plt.grid(True)
plt.legend()

print("Plot created successfully!")
print(f"matplotlib version: {plt.matplotlib.__version__}")
"""

    result = await sandbox.execute(code)
    print(f"\nStatus: {result.status}")
    if result.stdout:
        print(f"Output:\n{result.stdout}")
    if result.stderr:
        print(f"Error:\n{result.stderr}")
    if result.result:
        print(f"Result: {result.result}")


if __name__ == "__main__":
    asyncio.run(test())
