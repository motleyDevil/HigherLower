import art
import game_data
import random

# get user input to pick A or B
# compare follower count
# if user was right, use the correct guess and grab a new entry, increment score
# repeat

def get_object_one():
    random_item_one = random.choice(game_data.data)
    name_one = random_item_one["name"]
    description_one = random_item_one["description"]
    country_one = random_item_one["country"]
    followers_one = random_item_one["follower_count"]
    print(f"Compare A: {name_one}, a {description_one} from {country_one}")
    return followers_one

def get_object_two():
    random_item_two = random.choice(game_data.data)
    name_two = random_item_two["name"]
    description_two = random_item_two["description"]
    country_two = random_item_two["country"]
    followers_two = random_item_two["follower_count"]
    print(f"Compare A: {name_two}, a {description_two} from {country_two}")
    return followers_two

def game_loop():
        get_object_one()
        get_object_two()

game_loop()