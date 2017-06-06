from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):

        yield (views.IntroPage)
        yield (views.ChoicePage, {'consumption': 100})
        yield (views.ChoicePage, {'consumption': 110})
        yield (views.ChoicePage, {'consumption': 120})
        yield (views.ChoicePage, {'consumption': 130})
        yield (views.ChoicePage, {'consumption': 140})
        yield (views.ChoicePage, {'consumption': 150})
        yield (views.Results)

        yield (views.IntroPage)
        yield (views.ChoicePage, {'consumption': 160})
        yield (views.ChoicePage, {'consumption': 170})
        yield (views.ChoicePage, {'consumption': 180})
        yield (views.ChoicePage, {'consumption': 190})
        yield (views.ChoicePage, {'consumption': 200})
        yield (views.ChoicePage, {'consumption': 210})
        yield (views.Results)

        yield (views.FinalResultsPage)

