# Harmonica Chord-to-Tab

A Python CLI tool that converts chord names to harmonica tablature for a standard 10-hole diatonic harmonica in the key of C.

## Usage

```
python3 harmonica.py
```

Enter chords separated by spaces, across multiple lines. Type `go` to look them up.

```
> c g em
| am f
| go
  C major: +1 +2 +3 (blow holes 1, 2, 3)
  G major: -1 -2 -3 (draw holes 1, 2, 3)
  E minor: +2 -2 -3 (blow 2, draw 2, draw 3)
  A minor: -3 -4 +5 (draw 3, draw 4, blow 5)
  F major: -1 +2 -3 (draw 1, blow 2, draw 3)
```

## Commands

- `go` — process all entered chords
- `list` / `help` — show all available chords
- `q` / `quit` — exit

## Notation

- `+` = blow (exhale)
- `-` = draw (inhale)
- `''` = bend

## Available Chords

| Input | Chord | Tab |
|-------|-------|-----|
| c | C major | +1 +2 +3 |
| c2 | C major (high) | +4 +5 +6 |
| c3 | C major (highest) | +7 +8 +9 |
| g | G major | -1 -2 -3 |
| g2 | G major (high) | -4 -5 -6 |
| dm | D minor | -4 -5 -6 |
| em | E minor | +2 -2 -3 |
| am | A minor | -3 -4 +5 |
| f | F major | -1 +2 -3 |
| g7 | G7 | -2 -3 -4 -5 |
| c7 | C7 | +4 -4 +5 -5 |
| d7 | D7 | -1 -2 -3 -4 |
| d | D major | -1 -2'' -3 |
| a | A major | -3'' -4 +5 |
| e | E major | +2 -2 -3'' |
| bb | Bb major | -1 +2 -3'' |
