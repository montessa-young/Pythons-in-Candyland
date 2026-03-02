import random
from ascii_art import PEPPERMINT_ART, BUTTERSCOTCH_ART, FRUIT_SNACKS_ART, STARBURST_ART, TOOTSIE_POP_ART, CAPRI_SUN_ART, SNAKE_DEATH_ART


def enter(player):
    """The final encounter with outcomes influenced by the player's stats.

    Luck makes the candy rewards more likely; speed likewise helps you escape
    snake death.  We still have the same six prize outcomes and ten death
    outcomes, but the odds are skewed by the character's attributes.
    """
    print("\nYou emerge into a mysterious clearing in Candyland...")
    print("Suddenly, a massive Python appears before you!\n")
    
    # separate lists for positive and negative results
    positive = [
        (_outcome_peppermint, "peppermint"),
        (_outcome_butterscotch, "butterscotch"),
        (_outcome_fruit_snacks, "fruit snacks"),
        (_outcome_starburst, "starburst"),
        (_outcome_tootsie_pop, "tootsie pop"),
        (_outcome_capri_sun, "capri sun"),
    ]
    negative = [
        (_outcome_constricted, None),
        (_outcome_venom, None),
        (_outcome_crushed, None),
        (_outcome_swallowed, None),
        (_outcome_fangs, None),
        (_outcome_coiled, None),
        (_outcome_strangled, None),
        (_outcome_bitten, None),
        (_outcome_dragged, None),
        (_outcome_devoured, None),
    ]

    # compute probability of a positive result based on stats
    # base chance roughly 6/16 (~0.37)
    base = len(positive) / (len(positive) + len(negative))
    # add modifiers: each point of luck contributes 0.05, each point of speed 0.03
    # character stats are stored on the nested character object
    prob_positive = (
        base
        + player.character.luck * 0.05
        + player.character.speed * 0.03
    )
    prob_positive = min(max(prob_positive, 0.0), 1.0)

    # debug: you could print probability for testing
    # print(f"[DEBUG] positive chance: {prob_positive:.2f}")

    if random.random() < prob_positive:
        func, candy = random.choice(positive)
    else:
        func, candy = random.choice(negative)
    func(player, candy)


def _outcome_peppermint(player, candy_type):
    print(PEPPERMINT_ART)
    print("The Python sneezes from the spicy candy around you!")
    print("You quickly slip away and grab a delicious peppermint.")
    player.candy += 1
    player.add_score(5)
    print("You obtained: peppermint! 🍭")


def _outcome_butterscotch(player, candy_type):
    print(BUTTERSCOTCH_ART)
    print("The Python is mesmerized by shiny butterscotch in your paws!")
    print("You toss it aside and escape with your own butterscotch reward.")
    player.candy += 1
    player.add_score(5)
    print("You obtained: butterscotch! 🍬")


def _outcome_fruit_snacks(player, candy_type):
    print(FRUIT_SNACKS_ART)
    print("A magical gust of wind confuses the Python!")
    print("In the chaos, you grab a handful of fruit snacks.")
    player.candy += 1
    player.add_score(5)
    print("You obtained: fruit snacks! 🍓")


def _outcome_starburst(player, candy_type):
    print(STARBURST_ART)
    print("The Python is distracted by a rainbow appearing in the sky!")
    print("You seize the moment and claim a Starburst prize.")
    player.candy += 1
    player.add_score(5)
    print("You obtained: Starburst! 🌈")


def _outcome_tootsie_pop(player, candy_type):
    print(TOOTSIE_POP_ART)
    print("A mysterious Candyland guardian spirit appears!")
    print("It grants you a legendary Tootsie Pop and whisks away the Python.")
    player.candy += 1
    player.add_score(5)
    print("You obtained: Tootsie Pop! ⭐")


def _outcome_capri_sun(player, candy_type):
    print(CAPRI_SUN_ART)
    print("The Python is suddenly very thirsty!")
    print("While it searches for water, you grab a refreshing Capri Sun and escape.")
    player.candy += 1
    player.add_score(5)
    print("You obtained: Capri Sun! 💧")


def _outcome_constricted(player, candy):
    print(SNAKE_DEATH_ART)
    print("The Python coils around you tightly...")
    print("Your vision fades as you feel the crushing squeeze.")
    print("☠️ You have been constricted by the Python. GAME OVER.")
    player.alive = False


def _outcome_venom(player, candy):
    print(SNAKE_DEATH_ART)
    print("The Python strikes with lightning speed!")
    print("Its venomous fangs pierce through your scales...")
    print("The world goes numb as the toxin spreads through your body.")
    print("☠️ You have been poisoned by the Python. GAME OVER.")
    player.alive = False


def _outcome_crushed(player, candy):
    print(SNAKE_DEATH_ART)
    print("The Python wraps around you with incredible force!")
    print("Your bones crack and crumble under the immense pressure.")
    print("☠️ You have been crushed by the Python. GAME OVER.")
    player.alive = False


def _outcome_swallowed(player, candy):
    print(SNAKE_DEATH_ART)
    print("The Python opens its enormous jaws wider and wider...")
    print("You slip down its throat into the darkness.")
    print("☠️ You have been swallowed by the Python. GAME OVER.")
    player.alive = False


def _outcome_fangs(player, candy):
    print(SNAKE_DEATH_ART)
    print("The Python's lethal fangs glisten in the candyland light...")
    print("You try to escape, but you're too slow.")
    print("The fangs pierce deep as everything goes black.")
    print("☠️ You have been destroyed by the Python's fangs. GAME OVER.")
    player.alive = False


def _outcome_coiled(player, candy):
    print(SNAKE_DEATH_ART)
    print("The Python coils around you in a deathly spiral!")
    print("You struggle, but with each breath, the coils tighten more.")
    print("Your last thought is of all the candy you'll never taste.")
    print("☠️ You have been coiled to death by the Python. GAME OVER.")
    player.alive = False


def _outcome_strangled(player, candy):
    print(SNAKE_DEATH_ART)
    print("The Python's body wraps around your neck!")
    print("You gasp for air that never comes.")
    print("☠️ You have been strangled by the Python. GAME OVER.")
    player.alive = False


def _outcome_bitten(player, candy):
    print(SNAKE_DEATH_ART)
    print("The Python lunges with teeth bared!")
    print("Sharp fangs sink deep into your body.")
    print("You collapse as darkness overtakes you.")
    print("☠️ You have been bitten by the Python. GAME OVER.")
    player.alive = False


def _outcome_dragged(player, candy):
    print(SNAKE_DEATH_ART)
    print("The Python grabs you with its powerful jaws!")
    print("You're dragged deeper and deeper into the forest.")
    print("Your screams echo through Candyland, then fall silent.")
    print("☠️ You have been dragged away by the Python. GAME OVER.")
    player.alive = False


def _outcome_devoured(player, candy):
    print(SNAKE_DEATH_ART)
    print("The hungry Python sees you as nothing but a meal...")
    print("In one swift motion, you're engulfed completely.")
    print("Candyland will never see you again.")
    print("☠️ You have been devoured by the Python. GAME OVER.")
    player.alive = False
