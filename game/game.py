import random
from .characters import AVAILABLE_CHARACTERS
from .ascii_art import SNAKE_ART, CANDY_ART


class Player:
    def __init__(self, name: str, character):
        self.name = name
        self.character = character
        self.money = 10
        self.score = 0
        self.candy = 0

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
    while True:
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


def travel(player: Player) -> None:
    print("\nYou slither forward through the sugar-coated trail...")
    event = random.choice(["coin", "pit", "candy", "nothing"])
    if event == "coin":
        amt = random.randint(1, 5)
        print(f"You found {amt} coins in a gummy patch!")
        player.earn_money(amt)
        player.add_score(amt)
    elif event == "pit":
        loss = random.randint(1, player.character.speed)
        print(f"Oh no! You fell into a sticky pit and lost {loss} coins.")
        player.money = max(0, player.money - loss)
    elif event == "candy":
        amt = random.randint(1, 3)
        print(f"Congratulations! You discovered {amt} pieces of candy.")
        player.candy += amt
        player.add_score(amt * 2)
    else:
        print("The trail is quiet... for now.")


def rest(player: Player) -> None:
    print("\nYou curl up for a nap under a licorice tree.")
    if random.random() < 0.3:
        print("A friendly candy fairy drops a sweet treat in your paws!")
        player.candy += 1
        player.add_score(1)


def print_stats(player: Player) -> None:
    print("\n===== STATUS =====")
    print(f"Name:   {player.name}")
    print(f"Snake:  {player.character.name}")
    print(f"Money:  {player.money}")
    print(f"Score:  {player.score}")
    print(f"Candy:  {player.candy}")
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
