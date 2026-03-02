import random


def enter(player):
    """A mysterious licorice shop where you can buy items that affect your journey."""
    print("\nYou find yourself at the Licorice Shop, a cozy store filled with magical potions and items.")
    print("The shopkeeper greets you warmly.\n")
    
    print("===== LICORICE SHOP =====")
    print("Available Items:")
    print("1. Speed Potion - 2 coins (Makes you faster, easier to escape danger)")
    print("2. Lucky Charm - 3 coins (Increases your luck)")
    print("3. Protective Amulet - 4 coins (Protects you from losing too much money)")
    print("4. All-Purpose Elixir - 6 coins (Combines all benefits!)")
    print("5. Leave the shop")
    print("========================\n")
    print(f"You have {player.money} coins\n")
    
    choice = input("What would you like to buy? (1-5): ")
    
    if choice == "1":
        _buy_speed_potion(player)
    elif choice == "2":
        _buy_lucky_charm(player)
    elif choice == "3":
        _buy_protective_amulet(player)
    elif choice == "4":
        _buy_all_purpose_elixir(player)
    elif choice == "5":
        print("The shopkeeper waves goodbye.")
    else:
        print("The shopkeeper looks confused at your choice.")


def _buy_speed_potion(player):
    cost = 2
    if player.spend_money(cost):
        print("\nYou drink the Speed Potion! You feel incredibly fast!")
        print("In your newfound speed, you outrun danger...")
        gain = random.randint(3, 6)
        print(f"You discover hidden shortcuts worth {gain} coins!")
        player.earn_money(gain)
        player.add_score(3)
    else:
        print(f"\nYou don't have enough coins! (Need {cost}, Have {player.money})")


def _buy_lucky_charm(player):
    cost = 3
    if player.spend_money(cost):
        print("\nThe Lucky Charm begins to glow in your hands!")
        if random.random() < 0.6:  # 60% chance of good luck
            print("Your luck increases! You find a stash of candy coins!")
            gain = random.randint(4, 8)
            print(f"You gain {gain} coins!")
            player.earn_money(gain)
            player.add_score(5)
        else:
            print("Hmm, the luck doesn't seem to be working perfectly...")
            print("But at least you have a nice charm!")
            player.add_score(1)
    else:
        print(f"\nYou don't have enough coins! (Need {cost}, Have {player.money})")


def _buy_protective_amulet(player):
    cost = 4
    if player.spend_money(cost):
        print("\nYou wear the Protective Amulet around your neck.")
        print("You feel safer already!")
        print("Later in your journey, the amulet shields you from a financial disaster!")
        protected_loss = random.randint(4, 7)
        actual_loss = random.randint(1, 2)
        print(f"You avoided losing {protected_loss} coins, only losing {actual_loss}!")
        player.money = max(0, player.money - actual_loss)
        player.add_score(7)
    else:
        print(f"\nYou don't have enough coins! (Need {cost}, Have {player.money})")


def _buy_all_purpose_elixir(player):
    cost = 6
    if player.spend_money(cost):
        print("\nYou drink the legendary All-Purpose Elixir!")
        print("Power surges through your entire body!")
        print("You feel faster, luckier, and more protected all at once!\n")
        
        # Combination of all benefits
        print("You move with incredible speed and grace...")
        gain1 = random.randint(3, 5)
        print(f"Hidden shortcuts reward you with {gain1} coins!")
        
        print("Your newfound luck kicks in at just the right moment...")
        if random.random() < 0.7:
            gain2 = random.randint(2, 4)
            print(f"A lucky find gives you {gain2} more coins!")
        else:
            gain2 = 0
        
        print("Your protective aura deflects harm...")
        protected_loss = random.randint(2, 4)
        print(f"You avoid losing {protected_loss} coins!")
        
        total_gain = gain1 + gain2
        player.earn_money(total_gain)
        player.add_score(15)
    else:
        print(f"\nYou don't have enough coins! (Need {cost}, Have {player.money})")
