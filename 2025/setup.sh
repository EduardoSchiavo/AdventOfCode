#!/usr/bin/env bash

set -e

# ---- config ----
YEAR=2025
SESSION_FILE="session.txt"
INPUTS_DIR="inputs"
EXAMPLES_DIR="examples"

# ---- argument check ----
if [ $# -ne 1 ]; then
    echo "Usage: $0 <day (1-25)>"
    exit 1
fi

DAY="$1"

if ! [[ "$DAY" =~ ^[0-9]+$ ]] || [ "$DAY" -lt 1 ] || [ "$DAY" -gt 25 ]; then
    echo "Error: day must be an integer between 1 and 25"
    exit 1
fi

for FILE in "$INPUT_FILE" "$EXAMPLE_FILE" "$PY_FILE"; do
    if [ -e "$FILE" ]; then
        echo "Error: $FILE already exists. Aborting."
        exit 1
    fi
done

# ---- read session ----
if [ ! -f "$SESSION_FILE" ]; then
    echo "Error: $SESSION_FILE not found"
    exit 1
fi

SESSION="$(cat "$SESSION_FILE" | tr -d '\n')"

# ---- create input file ----
INPUT_FILE="$INPUTS_DIR/input${DAY}.txt"

curl -s "https://adventofcode.com/${YEAR}/day/${DAY}/input" \
    -H "Cookie: session=${SESSION}" \
    -o "$INPUT_FILE"

echo "Created $INPUT_FILE"

# ---- create example file ----
EXAMPLE_FILE="$EXAMPLES_DIR/example${DAY}.txt"
touch "$EXAMPLE_FILE"
echo "Created $EXAMPLE_FILE"

# ---- create python file ----
PY_FILE="day${DAY}.py"

cat > "$PY_FILE" << EOF
with open("examples/example${DAY}.txt") as ifile:
    inp = ifile.read().splitlines()

print(inp)


def p1():
    pass


def p2():
    pass
EOF

echo "Created $PY_FILE"

