import pycorpora
import random
import json
from sys import modules


def build_a_sentence():
    pick = random.choice(["character", "place", "corporation"])
    if pick is "character":
        ending = " with " + a_character() + " Who " + an_action()
    elif pick is "place":
        ending = " set in " + a_place()
    elif pick is "corporation":
        ending = " with Product Placement for " + a_corporation() + " on " + an_object()
    return a_netflix_category() + ending


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
    pick = random.choice(["eat", "resume", "color"])
    if pick is "eat":
        action = "Eats " + a_food()
    elif pick is "resume":
        action = a_resume_action_word() + " " + an_object()
    elif pick is "color":
        action = a_color_interaction() + a_color()
    else:
        action = ""
    return action


def a_food():
    pick = random.choice(["a_bread_or_pastry", "a_condiment", "a_menu_item"])
    return getattr(_this_module(), pick)()


def a_bread_or_pastry():
    pick = random.choice(["breads", "pastries"])
    return random.choice(pycorpora.foods["breads_and_pastries"][pick]).title()


def a_condiment():
    return random.choice(pycorpora.foods['condiments']['condiments']).title()


def a_menu_item():
    return random.choice(pycorpora.foods['menuItems']['menuItems']).title()


def an_object():
    return a_or_an(random.choice(pycorpora.objects['objects']['objects']).title())


def a_resume_action_word():
    return random.choice(pycorpora.words["resume_action_words"]["resume_action_words"]).title()


def a_place():
    pick = random.choice(["a_room", "a_venue", "a_country", "a_us_city"])
    return getattr(_this_module(), pick)()


def a_venue():
    return a_or_an(random.choice(random.choice(pycorpora.geography["venues"]["categories"])["categories"])["name"].title())


def a_room():
    return a_or_an(random.choice(pycorpora.architecture['rooms']['rooms']).title())


def a_country():
    return random.choice(pycorpora.geography["countries"]["countries"]).title()


def a_us_city():
    city = random.choice(pycorpora.geography["us_cities"]["cities"])
    return ", ".join([city["city"], city["state"]]).title()


def a_color():
    return random.choice(pycorpora.colors["crayola"]["colors"])["color"].title()


def a_color_interaction():
    return random.choice(["only wears ", "is bathed in ", "is weakened by ", "hates "]).title()


def a_corporation():
    pick = random.choice(["a_djia", "a_fortune500", "a_nasdaq", "a_newspaper"])
    return getattr(_this_module(), pick)()


def a_djia():
    return random.choice(pycorpora.corporations["djia"]["corporations"])["name"].title()


def a_fortune500():
    return random.choice(pycorpora.corporations["fortune500"]["companies"]).title()


def a_nasdaq():
    return random.choice(pycorpora.corporations["nasdaq"]["corporations"])["name"].title()


def a_newspaper():
    return random.choice(pycorpora.corporations["newspapers"]["newspapers"]).title()


def a_or_an(word):
    vowels = ["a", "e", "i", "o" "u"]
    if word.lower()[0] in vowels:
        article = "an "
    else:
        article = "a "
    return article + word


def _this_module():
    # Using sys.modules to dynamically get this modules name so we can call functions using getattr
    return modules[__name__]


if __name__ == '__main__':
    print build_a_sentence()
