import random

# Setting Global Variables
die_type = 0


class Item:
    def __init__(self, name, rarity, description, effect, weighting):
        self.name = name
        self.rarity = rarity
        self.description = description
        self.effect = effect
        self.weighting = weighting


def rules():
    print(
        f"||Dice Game||\n   - To play this game you will roll 9 consecutive D{die_type},\n   - By default, when you receive a duplicate of a die you have rolled preciously, you can chose to re-roll the die, or keep it.\n   - If you have 3 of the same die, by default you must re-roll the die.\n   - At the end of a round of rolling die, any Nat 1s can be spent on either:\n      - Multiplying the value of your score.\n      - Getting a new die of any value you chose.\n      - Staying the same.\n   - By beating a round you will earn money based on your final score in that game, this can be used in a shop you can enter every 5 rounds.\n   - Items bought in the shop will change how the game works, giving bonuses, or other boosts.\n   - Rounds will get progressively harder until you lose, There is no 'winning'."
    )


def roll_die():
    return random.randint(1, die_type)


def search_duplicate_die(die_array, new_dice):
    count = 0

    for i in range(len(die_array)):
        if die_array[i] == new_dice:
            count += 1

    return count


def search_die(die_array, searched_dice):
    for i in range(len(die_array)):
        if die_array[i] == searched_dice:
            return i
    return -1


def score_counter(die_array, score):
    for i in range(len(die_array)):
        score += die_array[i]
    return score


def main_game():
    round_num = 0
    game_cont = True
    die_count = 9

    while game_cont:
        round_cont = True
        round_num += 1

        while round_cont:
            die_array = []
            score = 0

            for i in range(die_count):

                new_dice = roll_die()
                print(f"Your current hand is: {die_array}\nYou rolled a {new_dice}")
                numb_of_die = search_duplicate_die(die_array, new_dice)
                if numb_of_die > 3:
                    print(
                        f"You currently have {numb_of_die} of this number in your hand currently, You must re-roll."
                    )
                    i -= 1
                else:
                    die_array.append(new_dice)

            search_for_one = True
            while search_for_one:
                location_one_found = search_die(die_array, 1)

            score = score_counter(die_array, score)
            print(f"Your final hand is: {die_array}\nYour final hand is: {score}")
            round_cont = False
            game_cont = False


## Main ##

die_type = 20
rules()
main_game()
