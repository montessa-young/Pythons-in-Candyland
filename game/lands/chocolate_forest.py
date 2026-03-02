import random


def enter(player):
    """Explore Chocolate Forest with a random challenge."""
    print("\nThe Chocolate Forest looms ahead, full of cocoa trees and fog.")
    # choose a scenario
    scenario = random.choice([_scenario_cocoa_path, _scenario_cookie_clear])
    scenario(player)


def _scenario_cocoa_path(player):
    print("A narrow path of cocoa beans stretches before you.")
    print("1. Follow the path into the darkness.")
    print("2. Turn back toward the gingerbread gate.")
    print("3. Climb a nearby tree to get your bearings.")
    choice = input("> ")
    if choice == "1":
        loss = random.randint(1, 4)
        print(f"The beans were slippery! You trip and drop {loss} coins.")
        player.money = max(0, player.money - loss)
    elif choice == "2":
        gain = random.randint(1, 3)
        print(f"A helpful squirrel rewards you with {gain} coins for being smart.")
        player.earn_money(gain)
        player.add_score(gain)
    elif choice == "3":
        loss = random.randint(2, 5)
        print(f"You slip out of the tree and lose {loss} coins in the leaves.")
        player.money = max(0, player.money - loss)
    else:
        print("Time wasted costs you. You lose a coin.")
        player.spend_money(1)


def _scenario_cookie_clear(player):
    print("You find a clearing with cookie crumbs everywhere.")
    print("1. Eat some crumbs. They look tasty.")
    print("2. Gather crumbs to sell later.")
    print("3. Ignore them and continue on.")
    choice = input("> ")
    if choice == "1":
        loss = random.randint(1, 3)
        print(f"The crumbs were stale! You feel sick and pay {loss} coins at a candy clinic.")
        player.money = max(0, player.money - loss)
    elif choice == "2":
        gain = random.randint(2, 4)
        print(f"You collect {gain} coins worth of crumbs and add them to your pouch.")
        player.earn_money(gain)
        player.add_score(gain)
    elif choice == "3":
        loss = random.randint(1, 2)
        print(f"You wasted time and accidentally drop {loss} coins.")
        player.money = max(0, player.money - loss)
    else:
        print("Your hesitation costs a coin.")
        player.spend_money(1)
