# chart.py

A CLI tool that renders Unicode tree diagrams from line-by-line input.

## Usage

```
python3 chart.py
```

Enter nodes one per line. Prefix a line with `sub` to make it a child, `sub sub` for a grandchild, and so on. Type `go` to render the tree.

## Input format

| Input | Meaning |
|-------|---------|
| `Text` | Root-level node |
| `sub Text` | Depth 1 child |
| `sub sub Text` | Depth 2 child |
| `go` | Render the tree |
| `q` / `quit` / `exit` | Quit |

## Example

```
> Animals
| sub Dogs
| sub sub Poodle
| sub Cats
| go

Animals
├── Dogs
│   └── Poodle
└── Cats
```

## Multiple roots

Entering more than one root-level line produces a forest — each root is rendered as its own tree.

```
> Fruits
| sub Apple
| sub Banana
| Vegetables
| sub Carrot
| go

Fruits
├── Apple
└── Banana
Vegetables
└── Carrot
```
