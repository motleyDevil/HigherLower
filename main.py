import art
import game_data
import random

object_new = {}
object_a = {}
object_b = {}

def get_object_new():
    random_item_one = random.choice(game_data.data)
    object_new["name"] = random_item_one["name"]
    object_new["description"] = random_item_one["description"]
    object_new["country"] = random_item_one["country"]
    object_new["followers"] = random_item_one["follower_count"]


print(get_object_new)

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


def game_start():
    get_object_new()
    assign_object_a()
    get_object_new()
    assign_object_b()
    print(object_a["followers"])
    print(object_b["followers"])


game_start()

# print(art.logo)
