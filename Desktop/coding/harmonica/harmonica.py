#!/usr/bin/env python3
"""Harmonica Chord-to-Tab CLI for a standard 10-hole diatonic in key of C."""

CHORDS = {
    "c":    ("C major",  "+1 +2 +3",       "blow holes 1, 2, 3"),
    "c2":   ("C major (high)",  "+4 +5 +6", "blow holes 4, 5, 6"),
    "c3":   ("C major (highest)", "+7 +8 +9", "blow holes 7, 8, 9"),
    "g":    ("G major",  "-1 -2 -3",        "draw holes 1, 2, 3"),
    "g2":   ("G major (high)", "-4 -5 -6",  "draw holes 4, 5, 6"),
    "dm":   ("D minor",  "-4 -5 -6",        "draw holes 4, 5, 6"),
    "em":   ("E minor",  "+2 -2 -3",        "blow 2, draw 2, draw 3"),
    "am":   ("A minor",  "-3 -4 +5",        "draw 3, draw 4, blow 5"),
    "f":    ("F major",  "-1 +2 -3",        "draw 1, blow 2, draw 3"),
    "g7":   ("G7",       "-2 -3 -4 -5",     "draw holes 2, 3, 4, 5"),
    "c7":   ("C7",       "+4 -4 +5 -5",     "blow 4, draw 4, blow 5, draw 5"),
    "d7":   ("D7",       "-1 -2 -3 -4",     "draw holes 1, 2, 3, 4"),
    "d":    ("D major",  "-1 -2'' -3",      "draw 1, draw 2'' bend, draw 3"),
    "a":    ("A major",  "-3'' -4 +5",      "draw 3'' bend, draw 4, blow 5"),
    "e":    ("E major",  "+2 -2 -3''",      "blow 2, draw 2, draw 3'' bend"),
    "bb":   ("Bb major", "-1 +2 -3''",      "draw 1, blow 2, draw 3'' bend"),
}


def process_chords(chords):
    """Look up a list of chord names and print their tabs."""
    for chord in chords:
        entry = CHORDS.get(chord.lower())
        if entry:
            name, tab, description = entry
            print(f"  {name}: {tab} ({description})")
        else:
            print(f"  Unknown chord '{chord}'. Type 'list' to see available chords.")
    print()


def main():
    print("=== Harmonica Chord-to-Tab (Key of C) ===")
    print("Enter chords separated by spaces, across multiple lines.")
    print("Type 'go' to look them up, 'list' for all chords, or 'q' to quit.\n")

    buffer = []

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

        if cmd in ("list", "help"):
            print("\nAvailable chords:")
            for key, (name, tab, _) in sorted(CHORDS.items()):
                print(f"  {key:<6} -> {name:<20} {tab}")
            print()
            continue

        if cmd == "go":
            if buffer:
                process_chords(buffer)
                buffer = []
            else:
                print("  No chords entered yet.\n")
            continue

        buffer.extend(user_input.split())


if __name__ == "__main__":
    main()
