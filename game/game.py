import random
from characters import AVAILABLE_CHARACTERS
from ascii_art import SNAKE_ART, CANDY_ART


class Player:
    def __init__(self, name: str, character):
        self.name = name
        self.character = character
        self.money = 10
        self.score = 0
        self.candy = 0
        self.alive = True
        # track whether certain special lands have been visited
        self.visited_starburst = False

    def add_score(self, amount: int) -> None:
        self.score += amount

    def earn_money(self, amount: int) -> None:
        self.money += amount

    def spend_money(self, amount: int) -> bool:
        if amount > self.money:
            return False
        self.money -= amount
        return True


def select_character():
    print("\nChoose your snake: ")
    for idx, char in enumerate(AVAILABLE_CHARACTERS, start=1):
        print(f"{idx}. {char.name} (speed {char.speed}, luck {char.luck})")
    choice = 0
    while choice not in range(1, len(AVAILABLE_CHARACTERS) + 1):
        try:
            choice = int(input("> "))
        except ValueError:
            pass
    return AVAILABLE_CHARACTERS[choice - 1]


def show_ascii():
    print(SNAKE_ART)


def game_loop(player: Player):
    print(f"\nWelcome, {player.name} the {player.character.name}!")
    while player.alive:
        print("\nWhat would you like to do?")
        print("1. Travel")
        print("2. Rest")
        print("3. Check Stats")
        print("4. Quit")
        choice = input("> ")
        if choice == "1":
            travel(player)
        elif choice == "2":
            rest(player)
        elif choice == "3":
            print_stats(player)
        elif choice == "4":
            print("Thanks for playing! Come back when you want more candy adventures.")
            break
        else:
            print("Invalid choice.")


from lands.lollipop_land import enter as enter_lollipop_land
from lands.chocolate_forest import enter as enter_chocolate_forest
from lands.magic_armory import enter as enter_magic_armory
from lands.licorice_shop import enter as enter_licorice_shop
from lands.starburst_land import enter as enter_starburst_land
from lands.ending_encounter import enter as enter_ending_encounter

LANDS = [
    enter_lollipop_land,
    enter_chocolate_forest,
    enter_magic_armory,
    enter_licorice_shop,
    enter_starburst_land,
    enter_ending_encounter,
]

def travel(player: Player) -> None:
    """Pick a random land and let the player explore a story situation there.

    The special Starburst land is only available once per playthrough; after
    the player visits it we mark it and exclude it from subsequent rolls.
    """
    print("\nYou slither forward through the sugar-coated trail...")
    # compute available lands, skipping starburst if already seen
    available = list(LANDS)
    if player.visited_starburst:
        from lands.starburst_land import enter as _enter_starburst
        available = [l for l in available if l is not _enter_starburst]

    # select a land at random and enter it
    land_func = random.choice(available)
    land_func(player)
    # if we just landed in starburst, flip the flag so it won't repeat
    from lands.starburst_land import enter as _enter_starburst
    if land_func is _enter_starburst:
        player.visited_starburst = True


def rest(player: Player) -> None:
    """Resting yields random flavor text and sometimes coins/candy."""
    scenes = [
        "You curl up for a nap under a licorice tree.",
        "You find a soft patch of marshmallow and doze off.",
        "A gentle rain of powdered sugar lulls you to sleep."
    ]
    print(f"\n{random.choice(scenes)}")
    # small chance to earn coins or candy during rest
    roll = random.random()
    if roll < 0.2:
        coins = random.randint(1, 3)
        print(f"You wake up refreshed and find {coins} coins by your side!")
        player.earn_money(coins)
        player.add_score(coins)
    elif roll < 0.35:
        print("A friendly candy fairy drops a sweet treat in your paws!")
        player.candy += 1
        player.add_score(1)


def print_stats(player: Player) -> None:
    # in this version of the game we treat everything as coins; score and
    # candy are internal details that get converted into a single total.
    total_coins = player.money + player.score + player.candy
    print("\n===== STATUS =====")
    print(f"Name:   {player.name}")
    print(f"Snake:  {player.character.name}")
    print(f"Coins:  {total_coins}")
    print("==================\n")


def main() -> None:
    print("=== Welcome to Pythons in Candyland ===")
    show_ascii()
    name = input("What is your name, brave snake? ")
    character = select_character()
    player = Player(name, character)
    game_loop(player)


if __name__ == "__main__":
    main()
