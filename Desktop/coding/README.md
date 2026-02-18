# CLI Tools

A collection of small Python CLI utilities.

## Tools

### [harmonica](harmonica/) — Harmonica Chord-to-Tab

Converts chord names to tablature for a standard 10-hole diatonic harmonica in the key of C.

```
> c g em
| go
  C major: +1 +2 +3 (blow holes 1, 2, 3)
  G major: -1 -2 -3 (draw holes 1, 2, 3)
  E minor: +2 -2 -3 (blow 2, draw 2, draw 3)
```

```
python3 harmonica/harmonica.py
```

### [chart](chart/) — Tree Chart

Renders Unicode tree diagrams from line-by-line input. Depth is set by prefixing lines with `sub`.

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

```
python3 chart/chart.py
```

## Requirements

Python 3.8+, no external dependencies.
