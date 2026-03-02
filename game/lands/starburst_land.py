import time
import random


def enter(player):
    """Starburst land: race to type 'STARBURST' quickly for better rewards."""
    print("\nYou step into a glowing field of Starbursts; the air tastes like rainbow!")
    print("A mystical gatekeeper challenges you: \"Type 'STARBURST' as fast as you can!\"")
    
    target = "STARBURST"
    input("Press Enter when you're ready...")
    start = time.perf_counter()
    typed = input("Type the word: ").strip().upper()
    end = time.perf_counter()
    elapsed = end - start
    
    if typed != target:
        print("Oh no! That wasn't the correct word.")
        loss = random.randint(1, 3)
        print(f"You fumble and drop {loss} coins in embarrassment.")
        player.money = max(0, player.money - loss)
        return
    
    # determine outcome by speed
    print(f"You typed it in {elapsed:.2f} seconds.")
    if elapsed < 2.0:
        gain = random.randint(8, 12)
        print("Incredible speed! The gatekeeper gifts you a trove of coins!")
        print(f"You earn {gain} coins!")
        player.earn_money(gain)
        player.add_score(10)
    elif elapsed < 4.0:
        gain = random.randint(4, 7)
        print("Nice work! The gatekeeper gives you some coins.")
        print(f"You earn {gain} coins!")
        player.earn_money(gain)
        player.add_score(5)
    else:
        loss = random.randint(1, 4)
        print("You were slow... the gatekeeper frowns and takes coins as a penalty.")
        print(f"You lose {loss} coins.")
        player.money = max(0, player.money - loss)
