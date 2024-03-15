import art
import game_data
import random

object_new = {}
object_a = {}
object_b = {}
guess = str()
higher = str()
current_score = 0


def get_object_new():
    random_item_one = random.choice(game_data.data)
    object_new["name"] = random_item_one["name"]
    object_new["description"] = random_item_one["description"]
    object_new["country"] = random_item_one["country"]
    object_new["followers"] = random_item_one["follower_count"]


def assign_object_a():
    object_a["name"] = object_new["name"]
    object_a["description"] = object_new["description"]
    object_a["country"] = object_new["country"]
    object_a["followers"] = object_new["followers"]


def assign_object_b():
    object_b["name"] = object_new["name"]
    object_b["country"] = object_new["country"]
    object_b["followers"] = object_new["followers"]
    object_b["description"] = object_new["description"]


def reassign_object_a():
    object_a["name"] = object_b["name"]
    object_a["description"] = object_b["description"]
    object_a["country"] = object_b["country"]
    object_a["followers"] = object_b["followers"]


def game_setup():
    get_object_new()
    assign_object_a()
    get_object_new()
    assign_object_b()


def game_start():
    print(f"Selection A: {object_a["name"]}, a {object_a["description"]} from {object_a['country']}")
    print(art.vs)
    print(f"Selection B: {object_b["name"]}, a {object_b["description"]} from {object_b['country']}\n")
    print(f'A = {object_a["followers"]} and B = {object_b["followers"]}')

    guess = input("Who has the most instagram followers? A or B: \n").lower
    return guess


def compare():
    higher = str()
    followers_a = object_a["followers"]
    followers_b = object_b["followers"]

    if followers_a > followers_b:
        higher = "a"
    elif followers_a < followers_b:
        higher = "b"

    if guess == higher:
        correct()
    elif guess != higher:
        end_game()



def correct(current_score):
    current_score += 1
    print("Correct!")
    print(f"Your score is {current_score}.")
    if higher == "b":
        reassign_object_a()
    continue_playing = 1
    return current_score


def end_game():
    print("Sorry, that's incorrect.")
    continue_playing = 2

#####

game_setup()
continue_playing = 1

while continue_playing == 1:
    current_score = int()
    game_start()
    compare()


# print(art.logo)