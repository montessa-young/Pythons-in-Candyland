import random


def enter(player):
    """Find a magical armory and test your word-shooting abilities."""
    print("\nYou discover a glittering Magical Armory hidden behind candy canes!")
    print("An old wizard appears: 'To claim treasure, you must activate my magical cannon!'")
    print("Type the correct word to fire the weapon and claim a prize.\n")
    
    # List of possible words to shoot
    words = ["CANDY", "SNAKE", "PYTHON", "SUGAR", "CHOCOLATE", "LICORICE"]
    secret_word = random.choice(words)
    
    print(f"The word has {len(secret_word)} letters.")
    print("Hint: It could be CANDY, SNAKE, PYTHON, SUGAR, CHOCOLATE, or LICORICE.\n")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        user_input = input("Type a word: ").upper()
        attempts += 1
        
        if user_input == secret_word:
            print(f"\n⚡ BOOM! The cannon fires with a brilliant flash!")
            print(f"You got it right! The word was {secret_word}!")
            _success_outcome(player)
            return
        else:
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Wrong! You have {remaining} attempts left.\n")
            else:
                print(f"\nThe cannon sputters and dies. The wizard sighs.")
                print(f"The secret word was: {secret_word}")
                _failure_outcome(player)
                return


def _success_outcome(player):
    """Player successfully guesses the word."""
    outcomes = [
        _outcome_gold_coins,
        _outcome_magic_crystal,
        _outcome_enchanted_shield
    ]
    random.choice(outcomes)(player)


def _failure_outcome(player):
    """Player fails to guess the word."""
    outcomes = [
        _outcome_cannon_backfire,
        _outcome_wizard_trick,
        _outcome_escape_penalty
    ]
    random.choice(outcomes)(player)


def _outcome_gold_coins(player):
    print("Gold coins rain down from the cannon!")
    gain = random.randint(5, 10)
    print(f"You collect {gain} coins!")
    player.earn_money(gain)
    player.add_score(10)


def _outcome_magic_crystal(player):
    print("A magical crystal emerges from the cannon.")
    print("You sell it to a traveling merchant for a nice profit!")
    gain = random.randint(4, 8)
    print(f"You earn {gain} coins!")
    player.earn_money(gain)
    player.add_score(8)


def _outcome_enchanted_shield(player):
    print("An enchanted shield materializes before you!")
    print("A collector buys it immediately for top coin.")
    gain = random.randint(6, 12)
    print(f"You gain {gain} coins!")
    player.earn_money(gain)
    player.add_score(12)


def _outcome_cannon_backfire(player):
    print("The cannon misfires! It shoots backwards!")
    loss = random.randint(2, 4)
    print(f"You get blasted and lose {loss} coins in medical bills.")
    player.money = max(0, player.money - loss)


def _outcome_wizard_trick(player):
    print("The wizard laughs mischievously.")
    print("It was all a trick! Nothing was ever real.")
    loss = random.randint(1, 3)
    print(f"You feel foolish and somehow lose {loss} coins.")
    player.money = max(0, player.money - loss)


def _outcome_escape_penalty(player):
    print("The cannon crackles with dangerous energy!")
    print("You run away in fear, dropping coins as you flee.")
    loss = random.randint(2, 5)
    print(f"You lost {loss} coins in your hasty escape.")
    player.money = max(0, player.money - loss)
