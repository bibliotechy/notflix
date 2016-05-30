import pycorpora
import random
import json
from sys import modules


def build_a_sentence():
    return a_netflix_category() + " with " + a_character() + " Who " + an_action()


def a_netflix_category():
    return random.choice(netflix_categories()['categories'])['name']


def netflix_categories():
    return json.loads(open("netflix-categories.json").read())


def a_character():
    # Pick a function to generate the featured charater of this category
    pick = random.choice(["a_qualified_character_type", "an_animal"])
    return getattr(_this_module(), pick)()


def a_qualified_character_type():
    rct = a_character_type()
    quality = rct.get("quality", " ")
    ctype = rct['name']
    return a_or_an((quality + " " + ctype).strip().title())


def a_character_type():
    # Returns a json object of a character type with name, qualities, synonyms, etc.
    return random.choice(pycorpora.archetypes['character']['characters'])


def an_animal():
    return a_or_an(random.choice(pycorpora.animals["common"]["animals"]).title())



def an_action():
    pick = random.choice(["eat", "resume"])
    if pick is "eat":
        action = "Eats " + a_food()
    elif pick is "resume":
        action = a_resume_action_word() + " " + a_noun()
    else:
        action = ""
    return action


def a_food():
    pick = random.choice(["a_bread_or_pastry", "an_apple_type"])
    return getattr(_this_module(), pick)()


def a_bread_or_pastry():
    borp = random.choice(["breads", "pastries"])
    return a_or_an(random.choice(pycorpora.foods["breads_and_pastries"][borp]).title())


def an_apple_type():
    return a_or_an(random.choice(pycorpora.foods['apple_cultivars']['cultivars']).title())


def a_noun():
    return a_or_an(random.choice(pycorpora.words['nouns']['nouns']).title())


def a_resume_action_word():
    return random.choice(pycorpora.words["resume_action_words"]["resume_action_words"]).title()


def a_or_an(word):
    vowels = ["a", "e", "i", "o" "u"]
    if word.lower()[0] in vowels:
        article = "an "
    else:
        article = "a "
    return article + word


def _this_module():
    return modules[__name__]


if __name__ == '__main__':
    print build_a_sentence()
