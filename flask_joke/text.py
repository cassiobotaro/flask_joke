import json

from markdown import markdown
from pkg_resources import resource_filename


def joke():
    return markdown(
        "Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... "
        "**Beiherhund** das Oder die Flipperwaldt gersput."
    )


def joke_from_json() -> str:
    filepath = resource_filename(__name__, "data/joke.json")
    with open(filepath) as file:
        data = json.load(file)
        return markdown(data["joke"])
