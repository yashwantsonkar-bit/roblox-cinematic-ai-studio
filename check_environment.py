#!/usr/bin/env python3
"""Read-only local tool and hardware check. Uses only Python standard library."""
import json, os, platform, shutil, subprocess, sys

def command_version(cmd, args):
    path = shutil.which(cmd)
    if not path:
        return {"found": False, "path": None}
    try:
        p = subprocess.run([path, *args], capture_output=True, text=True, timeout=8)
        out = (p.stdout or p.stderr).strip().splitlines()
        return {"found": True, "path": path, "version": out[0] if out else "version unavailable"}
    except Exception as e:
        return {"found": True, "path": path, "version_error": str(e)}

info = {
    "platform": platform.platform(),
    "python": sys.version.split()[0],
    "cpu_count": os.cpu_count(),
    "tools": {
        "blender": command_version("blender", ["--version"]),
        "ffmpeg": command_version("ffmpeg", ["-version"]),
        "git": command_version("git", ["--version"]),
        "uv": command_version("uv", ["--version"]),
        "claude": command_version("claude", ["--version"])
    },
    "notes": [
        "This script does not verify MCP authentication or connected application sessions.",
        "Open Roblox Studio and Blender and verify their MCP connections inside Claude Code."
    ]
}
print(json.dumps(info, indent=2))
