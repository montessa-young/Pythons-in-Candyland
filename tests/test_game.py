import pytest
import sys, os

# make the top‐level workspace directory importable so the `game` package can be
# found when running `pytest` directly from the repository root.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.characters import AVAILABLE_CHARACTERS
from game.game import Player


def test_player_initialization():
    char = AVAILABLE_CHARACTERS[0]
    p = Player("Tester", char)
    assert p.name == "Tester"
    assert p.character is char
    assert p.money == 10
    assert p.score == 0
    assert p.candy == 0


def test_earn_and_spend_money():
    p = Player("X", AVAILABLE_CHARACTERS[1])
    p.earn_money(5)
    assert p.money == 15
    ok = p.spend_money(4)
    assert ok is True
    assert p.money == 11
    # spending more than you have should fail
    ok = p.spend_money(100)
    assert ok is False
    assert p.money == 11


def test_add_score():
    p = Player("Y", AVAILABLE_CHARACTERS[2])
    p.add_score(7)
    assert p.score == 7


def test_lollipop_land_gain(monkeypatch):
    """Choosing the helpful peppermint tree should award coins and score."""
    from game.lands import lollipop_land
    p = Player("Tester", AVAILABLE_CHARACTERS[0])
    # force first scenario and ``choice 2``
    monkeypatch.setattr("random.choice", lambda seq: seq[0])
    monkeypatch.setattr("builtins.input", lambda prompt="": "2")
    monkeypatch.setattr("random.randint", lambda a, b: 3)
    lollipop_land.enter(p)
    assert p.money == 13
    assert p.score == 3


def test_lollipop_land_loss(monkeypatch):
    """Taking the syrup swamp path costs coins."""
    from game.lands import lollipop_land
    p = Player("Tester", AVAILABLE_CHARACTERS[0])
    monkeypatch.setattr("random.choice", lambda seq: seq[0])
    monkeypatch.setattr("builtins.input", lambda prompt="": "1")
    monkeypatch.setattr("random.randint", lambda a, b: 2)
    lollipop_land.enter(p)
    assert p.money == 8


def test_travel_selects_land(monkeypatch):
    """The travel function should pick a land and apply its effects."""
    p = Player("Tester", AVAILABLE_CHARACTERS[0])
    # control random.choice for both land selection and scenario
    monkeypatch.setattr("random.choice", lambda seq: seq[0])
    monkeypatch.setattr("builtins.input", lambda prompt="": "2")
    monkeypatch.setattr("random.randint", lambda a, b: 2)
    from game.game import travel
    travel(p)
    assert p.money == 12
    assert p.score == 2
