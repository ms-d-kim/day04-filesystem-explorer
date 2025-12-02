# day04-filesystem-explorer

A small CLI tool that recursively explores a directory and prints a tree view with:

- file / directory names
- POSIX-style permissions (e.g. `drwxr-xr-x`)
- inode numbers
- sizes (bytes or human-readable)

## Usage

Create and activate a virtualenv, then run:

```bash
python -m cli