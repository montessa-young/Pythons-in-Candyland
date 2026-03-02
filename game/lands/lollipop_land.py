import random


def enter(player):
    """Explore Lollipop Land with random scenario and choices."""
    print("\nYou wander into Lollipop Land, where everything is sweet and sticky.")
    # pick one of the scenarios to play
    scenario = random.choice([_scenario_fork, _scenario_river])
    scenario(player)


def _scenario_fork(player):
    print("You come upon a fork in the candy road.")
    print("1. Go left towards the syrup swamp.")
    print("2. Take the right path through peppermint trees.")
    print("3. Climb the candy cane hill.")
    choice = input("> ")
    if choice == "1":
        loss = random.randint(1, 3)
        print(f"You got stuck in syrup and lost {loss} coins getting free.")
        player.money = max(0, player.money - loss)
    elif choice == "2":
        gain = random.randint(1, 4)
        print(f"The peppermint trees gave you {gain} coins!")
        player.earn_money(gain)
        player.add_score(gain)
    elif choice == "3":
        loss = random.randint(2, 5)
        print(f"A candy cane fell and you lost {loss} coins.")
        player.money = max(0, player.money - loss)
    else:
        print("Indecision costs you a coin as time passes.")
        player.spend_money(1)


def _scenario_river(player):
    print("You arrive at a river of chocolate.")
    print("1. Swim across.")
    print("2. Build a bridge.")
    print("3. Follow the river.")
    choice = input("> ")
    if choice == "1":
        loss = random.randint(1, 4)
        print(f"You slip and lose {loss} coins in the mud.")
        player.money = max(0, player.money - loss)
    elif choice == "2":
        gain = random.randint(2, 5)
        print(f"You sell bridge materials and earn {gain} coins!")
        player.earn_money(gain)
        player.add_score(gain)
    elif choice == "3":
        loss = random.randint(1, 3)
        print(f"You get lost and drop {loss} coins.")
        player.money = max(0, player.money - loss)
    else:
        print("You wander aimlessly and coins fall out.")
        player.spend_money(1)
