import argparse

from filesystem_explorer.explorer import explore


def main() -> None:
    parser = argparse.ArgumentParser(description="Filesystem explorer CLI")
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to explore (default: current directory)",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=None,
        help="Maximum recursion depth (1 = just children of root)",
    )
    parser.add_argument(
        "--show-hidden",
        action="store_true",
        help="Include hidden files/directories (starting with '.')",
    )
    parser.add_argument(
        "--human-readable",
        action="store_true",
        help="Show human-readable sizes like 1.2MB instead of raw bytes",
    )

    args = parser.parse_args()

    explore(
        path=args.path,
        max_depth=args.max_depth,
        show_hidden=args.show_hidden,
        human_readable=args.human_readable,
    )


if __name__ == "__main__":
    main()