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
# day04-filesystem-explorer

A small CLI tool that recursively explores a directory and prints a tree-style view with:

- file / directory names  
- POSIX-style permissions (e.g. `drwxr-xr-x`)  
- inode numbers  
- sizes (bytes or human-readable)  

This project is part of my 90-day systems & infra sprint, building foundational intuition about how filesystems, permissions, and directories work — skills that matter for later projects on storage engines, ETL pipelines, and distributed filesystems.

## Features

- Recursive directory traversal  
- Tree-style ASCII output (`├──`, `└──`)  
- Permission formatting (`rwx`)  
- Support for hidden files  
- Human-readable file sizes  
- Configurable max recursion depth  

## Installation

Activate a virtual environment (optional, but recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Then run the CLI:

```bash
python -m cli
```

## Usage Examples

Explore the current directory:

```bash
python -m cli .
```

Limit recursion depth:

```bash
python -m cli . --max-depth 2
```

Show hidden files:

```bash
python -m cli . --show-hidden
```

Human-readable sizes:

```bash
python -m cli . --human-readable
```

Combine flags:

```bash
python -m cli /tmp --max-depth 3 --human-readable --show-hidden
```

## Example Output

```
/Users/minseok/day04-filesystem-explorer
├── filesystem_explorer  [drwxr-xr-x]  inode=12345  size=64B
│   ├── __init__.py      [-rw-r--r--]  inode=12346  size=0B
│   └── explorer.py      [-rw-r--r--]  inode=12347  size=2.3KB
├── cli.py               [-rw-r--r--]  inode=12348  size=1.0KB
└── README.md            [-rw-r--r--]  inode=12349  size=0.7KB
```

## Why this project matters (roadmap context)

This daily project increases my intuition for:

- How filesystems represent paths, inodes, and permissions  
- How tools like `ls`, `tree`, `find`, and file explorers work  
- How to traverse directory structures safely (permissions, errors)  
- How metadata is organized — crucial for:
  - building ETL pipelines  
  - writing custom storage layers  
  - understanding partitioning and table layouts in data warehouses  
  - later capstone work on distributed file storage  

It builds the foundation for storage, metadata, and distributed system intuition needed in later weeks of the 90-day sprint.

## Status

Completed as part of Day 04 of my 90-day Systems & Infra Sprint.