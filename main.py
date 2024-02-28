import art
import game_data
import random

#### CAN YOU USE THE SAME OBJECT FOR BOTH, ASSIGN 1 TO BOTH A AND B AND COMPARE FROM THERE?


def get_object_one():
    random_item_one = random.choice(game_data.data)
    name_one = random_item_one["name"]
    description_one = random_item_one["description"]
    country_one = random_item_one["country"]
    followers_one = random_item_one["follower_count"]
    print(f"A: {name_one}, a {description_one} from {country_one}")
    return followers_one


def get_object_two():
    random_item_two = random.choice(game_data.data)
    name_two = random_item_two["name"]
    description_two = random_item_two["description"]
    country_two = random_item_two["country"]
    followers_two = random_item_two["follower_count"]
    print(f"B: {name_two}, a {description_two} from {country_two}")
    return followers_two


def get_new_object():
    random_item_new = random.choice(game_data.data)
    name_new = random_item_new["name"]
    description_new = random_item_new["description"]
    country_new = random_item_new["country"]
    followers_new = random_item_new["follower_count"]
    print(f"B: {name_new}, a {description_new} from {country_new}")
    return followers_new


def get_guess():
    guess = input("What is your guess? ").lower()
    return guess


def compare(followers_one, followers_two):
    if followers_one > followers_two:
        winner = "a"
    elif followers_one < followers_two:
        winner = "b"
    return winner


print(art.logo)


def game_loop(score):
    print("Who has the most Instagram followers?")
    guess = get_guess()
    if guess == winner:
        score += 1
        print(f"Congratulations!")
        if score == 1:
            print(f"You have {score} point so far!")
        else:
            print(f"You have {score} points so far!")
    else:
        print(f"Sorry. Game over. Your final score was {score}.")


score = 0
followers_one = get_new_object()
followers_two = get_new_object()

get_object_one()
print(art.vs)
get_object_two()

print(f'{followers_one}  {followers_two}')

# winner = compare(followers_one, followers_two)

# game_loop(winner, score)

