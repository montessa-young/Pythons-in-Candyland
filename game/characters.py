class Character:
    def __init__(self, name: str, speed: int, luck: int):
        self.name = name
        self.speed = speed
        self.luck = luck

    def __repr__(self):
        return f"Character(name={self.name!r}, speed={self.speed}, luck={self.luck})"


# a small roster of snakes the player can choose from
AVAILABLE_CHARACTERS = [
    Character("Gummy Python", speed=5, luck=3),
    Character("Peppermint Boa", speed=3, luck=5),
    Character("Chocolate Cobra", speed=4, luck=4),
]
