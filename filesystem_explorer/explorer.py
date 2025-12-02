from __future__ import annotations

import os
import stat
from pathlib import Path
from typing import Optional


def format_permissions(mode: int) -> str:
    """Return a string like 'drwxr-xr-x'."""
    is_dir = "d" if stat.S_ISDIR(mode) else "-"
    perms = ""
    for who in ["USR", "GRP", "OTH"]:
        for what in ["R", "W", "X"]:
            flag = getattr(stat, f"S_I{what}{who}")
            perms += what.lower() if (mode & flag) else "-"
    return is_dir + perms


def format_size(size: int, human: bool) -> str:
    """Return size in bytes or human-readable string."""
    if not human:
        return f"{size}B"
    units = ["B", "KB", "MB", "GB", "TB"]
    value = float(size)
    idx = 0
    while value >= 1024.0 and idx < len(units) - 1:
        value /= 1024.0
        idx += 1
    return f"{value:.1f}{units[idx]}"


def walk(
    root: Path,
    max_depth: Optional[int] = None,
    show_hidden: bool = False,
    human_readable: bool = False,
) -> None:
    """
    Recursively walk the filesystem starting at root and print a tree.

    root: starting directory
    max_depth: if set, limits depth (1 = just root contents)
    show_hidden: include dotfiles if True
    human_readable: show sizes as e.g. 1.2MB instead of raw bytes
    """

    def _walk(path: Path, depth: int, prefix: str) -> None:
        if max_depth is not None and depth > max_depth:
            return

        try:
            entries = list(path.iterdir())
        except PermissionError:
            print(prefix + "[permission denied]")
            return
        except FileNotFoundError:
            print(prefix + "[not found]")
            return

        if not show_hidden:
            entries = [e for e in entries if not e.name.startswith(".")]

        # Directories first, then files; sorted by name
        entries.sort(key=lambda p: (not p.is_dir(), p.name.lower()))

        for i, entry in enumerate(entries):
            is_last = i == len(entries) - 1
            connector = "└── " if is_last else "├── "
            next_prefix = prefix + ("    " if is_last else "│   ")

            try:
                st = entry.stat()
            except PermissionError:
                print(prefix + connector + f"{entry.name}  [permission denied]")
                continue

            perms = format_permissions(st.st_mode)
            inode = st.st_ino
            size_str = format_size(st.st_size, human_readable)

            print(
                f"{prefix}{connector}{entry.name}  "
                f"[{perms}]  inode={inode}  size={size_str}"
            )

            if entry.is_dir():
                _walk(entry, depth + 1, next_prefix)

    root = root.resolve()
    print(root)
    _walk(root, depth=1, prefix="")


def explore(
    path: str = ".",
    max_depth: Optional[int] = None,
    show_hidden: bool = False,
    human_readable: bool = False,
) -> None:
    """Public entrypoint used by the CLI."""
    root = Path(path)
    if not root.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")
    walk(root, max_depth=max_depth, show_hidden=show_hidden, human_readable=human_readable)