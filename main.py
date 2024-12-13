from random import randint
from time import sleep

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
    return randint(1, die_type)


def get_multiplier():
    # Multiplier will be between 0.5 and 100, of different rarities
    Chance_num = randint(1,10000)

    if Chance_num <= 25:
        multiplier = 0.5
    elif Chance_num <= 100:
        multiplier = 0.75
    elif Chance_num <= 500:
        multiplier = 1
    elif Chance_num <= 1500:
        multiplier = 1.5
    elif Chance_num <= 3000:
        multiplier = 2
    elif Chance_num <= 5000:
        multiplier = 3
    elif Chance_num <= 6500:
        multiplier = 5
    elif Chance_num <= 7250:
        multiplier = 7.5
    elif Chance_num <= 8000:
        multiplier = 10
    elif Chance_num <= 8750:
        multiplier = 15
    elif Chance_num <= 9250:
        multiplier = 20
    elif Chance_num <= 9500:
        multiplier = 25
    elif Chance_num <= 9750:
        multiplier = 45
    elif Chance_num <= 9875:
        multiplier = 50
    elif Chance_num <= 9950:
        multiplier = 65
    elif Chance_num <= 9975:
        multiplier = 75
    elif Chance_num <= 9990:
        multiplier = 85
    elif Chance_num <= 9999:
        multiplier = 95
    else:
        multiplier = 100

    return multiplier


def is_between(compared_num, lower, upper):
    if compared_num >= lower and compared_num <= upper:
        return True
    else:
        return False


def search_duplicate_die(die_array, new_dice):
    count = 0

    for i in range(len(die_array)):
        if die_array[i] == new_dice:
            count += 1

    return count


def search_die(die_array, searched_dice):
    # Sets up variables used for counting searched_due
    num_of_searched_die = 0
    locations_of_searched_die = []

    for i in range(len(die_array)):
        if die_array[i] == searched_dice:
            locations_of_searched_die.append(i)
            num_of_searched_die += 1

    return num_of_searched_die, locations_of_searched_die


def decisions_with_ones(number_of_ones):
    # Setting up variables for this sub-program
    num_of_multipliers = 0
    num_of_new_die = 0
    num_of_staying = 0

    for i in range(number_of_ones):
        valid_input = False
        while not valid_input:
            user_input = str(input(f"What would you like to do with your {i+1} dice?:\n - Multiply your score (Multiply)\n - Replace it (replace)\n - Keep it (Stay)\n")).lower()
            
            if user_input == "multiply" or user_input == "replace" or user_input == "stay":
                valid_input = True
            else:
                print(f"Your input of {user_input} was invalid, please try again.")
        
        if user_input == "multiply": 
            num_of_multipliers += 1

        elif user_input == "replace":
            num_of_new_die += 1

        else:
            num_of_staying += 1

        return num_of_multipliers, num_of_new_die, num_of_staying

            


def score_counter(die_array, score):
    for i in range(len(die_array)):
        score += die_array[i]
    return score


def main_game():
    # Set variables for the game
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

            # Search for 1
            numb_of_ones, locations_of_ones = search_die(die_array, 1)



            score = score_counter(die_array, score)
            print(f"Your final hand is: {die_array}\nYour final hand is: {score}")
            round_cont = False
            game_cont = False


## Main ##

die_type = 20
#rules()
#main_game()
decisions_with_ones(2)