#!/usr/bin/env python3
"""Copy TypeScript file from source to package directory."""

import shutil
from pathlib import Path


def copy_typescript():
    """Copy the main.ts file to the package directory."""
    # Get paths
    root = Path(__file__).parent.parent.parent
    src_ts = root / "pyodide-sandbox-js" / "main.ts"
    dst_ts = root / "sandbox-py" / "langchain_sandbox" / "pyodide_sandbox.ts"

    # Check source exists
    if not src_ts.exists():
        raise FileNotFoundError(f"Source TypeScript file not found: {src_ts}")

    # Create destination directory if needed
    dst_ts.parent.mkdir(parents=True, exist_ok=True)

    # Copy file
    shutil.copy2(src_ts, dst_ts)
    print(f"✓ Copied {src_ts} -> {dst_ts}")

    # Verify copy
    if dst_ts.exists():
        src_size = src_ts.stat().st_size
        dst_size = dst_ts.stat().st_size
        if src_size == dst_size:
            print(f"✓ Verified: {dst_size:,} bytes copied successfully")
        else:
            raise ValueError(f"File size mismatch: src={src_size}, dst={dst_size}")
    else:
        raise FileNotFoundError(f"Failed to copy file to {dst_ts}")


if __name__ == "__main__":
    copy_typescript()
