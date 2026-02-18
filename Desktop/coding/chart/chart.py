#!/usr/bin/env python3
"""Tree Chart CLI — enter nodes line by line, type 'go' to render a Unicode tree."""

from typing import TypedDict


class Node(TypedDict):
    label: str
    children: "list[Node]"


def parse_lines(lines: list[str]) -> list[Node]:
    """Parse buffered lines into a forest (list of root nodes)."""
    roots: list[Node] = []
    stack: list[Node] = []

    for line in lines:
        tokens = line.split()
        depth = 0
        while depth < len(tokens) and tokens[depth] == "sub":
            depth += 1
        label = " ".join(tokens[depth:])
        if not label:
            continue

        node: Node = {"label": label, "children": []}

        if depth == 0:
            roots.append(node)
            stack = [node]
        else:
            parent = stack[depth - 1]
            parent["children"].append(node)
            if depth < len(stack):
                stack[depth] = node
                del stack[depth + 1:]
            else:
                stack.append(node)

    return roots


def render(node: Node, prefix: str = "", is_last: bool = True) -> None:
    """Recursively render a node and its children with Unicode box-drawing chars."""
    connector = "└── " if is_last else "├── "
    print(prefix + connector + node["label"])
    child_prefix = prefix + ("    " if is_last else "│   ")
    children = node["children"]
    for i, child in enumerate(children):
        render(child, child_prefix, i == len(children) - 1)


def print_forest(roots: list[Node]) -> None:
    """Print each root and its subtree."""
    for root in roots:
        print(root["label"])
        children = root["children"]
        for i, child in enumerate(children):
            render(child, "", i == len(children) - 1)


def main() -> None:
    print("=== Tree Chart ===")
    print("Enter nodes: 'sub' prefix sets depth (e.g. 'sub sub Leaf').")
    print("Type 'go' to render the tree, or 'q' to quit.\n")

    buffer: list[str] = []

    while True:
        try:
            user_input = input("| " if buffer else "> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not user_input:
            continue

        cmd = user_input.lower()

        if cmd in ("q", "quit", "exit"):
            break

        if cmd == "go":
            if buffer:
                roots = parse_lines(buffer)
                if roots:
                    print()
                    print_forest(roots)
                    print()
                else:
                    print("  Nothing to render.\n")
                buffer = []
            else:
                print("  No input entered yet.\n")
            continue

        buffer.append(user_input)


if __name__ == "__main__":
    main()
