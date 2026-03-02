# Pythons-in-Candyland

A simple text‑based demo game for high school Python students.  The theme is a mash‑up of the classic *Candyland* board game and an Oregon‑Trail style journey, but our main protagonists are Python snakes!

Players choose a candy‑themed snake, travel through a sugary landscape, earn money and score points, and collect candy prizes along the way. The project is intended as a starting point for lessons about:

- basic Python package structure
- classes and object state (`Player`, `Character`)
- user input and game loops
- simple scoring/money systems
- unit testing with `pytest`

## Getting started

```bash
# optional: create a virtual environment
python -m venv .venv
source .venv/bin/activate

# install the test dependency
pip install -r requirements.txt
```

Run the game:

```bash
python -m game.game
```

Run the unit tests:

```bash
pytest
```

## Project structure

```
Pythons-in-Candyland/
├── game/               # Python package containing game logic
│   ├── __init__.py
│   ├── ascii_art.py    # some ASCII images used in the demo
│   ├── characters.py   # character definitions
│   └── game.py         # main loop and gameplay functions
├── tests/              # simple unit tests for core classes
│   └── test_game.py
├── requirements.txt    # dependencies for running tests
└── README.md           # this documentation
```

Feel free to modify the characters, events, and scoring rules to make the game as rich as your classroom imagination allows.  Happy coding!  :snake: :candy:
