from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

import math
import random


class IntroPage(Page):
    #
    # This page is for showing instructions
    # It is shown at the beginning of each part
    form_model = models.Player

    def is_displayed(self):
        return (self.round_number % 6) == 1

    def vars_for_template(self):
        description_text = ''
        if self.round_number == 1:
            description_text = 'Вы приступаете к Части 3, раздел 1'
        if self.round_number == 7:
            description_text = 'Вы приступаете к Части 3, раздел 2'
        return {'description_text': description_text}


class ChoicePage(Page):
    timeout_seconds = 180
    form_model = models.Player
    form_fields = ['consumption']

    def before_next_page(self):
        self.player.savings = (self.player.disposable_income -
                               self.player.consumption) * (1 + Constants.r)
        self.player.calc_starting_savings_for_next_round()
        self.player.calc_DI_for_next_round()
        if self.round_number == 12:
            self.player.paying_period = random.choice(
                range(1, Constants.num_rounds + 1))
            tokens = self.player.in_round(self.player.paying_period).consumption
            self.player.payoff = int(tokens/15)

        return

    def consumption_max(self):
        return self.player.income + self.player.savings

    def vars_for_template(self):
        return {
            'player_in_previous_rounds': self.player.in_previous_rounds(),
            'len_player_in_previous_rounds': len(self.player.in_previous_rounds())
        }


class Results(Page):
    form_model = models.Player

    def is_displayed(self):
        return (self.round_number % 6) == 0

    def vars_for_template(self):
        description_text = ''
        if self.round_number == 6:
            description_text = 'Вы закончили раздел 1'
        if self.round_number == 12:
            description_text = 'Вы закончили выполнять все разделы Части 3 эксперимента'
        return {'description_text': description_text}


class FinalResultsPage(Page):
    form_model = models.Player

    def vars_for_template(self):
        return {'random_consumption': self.player.in_round(self.player.paying_period).consumption,
                'risk': self.participant.vars.get('payoff_risk'),
                'df': self.participant.vars.get('payoff_df'),
                'risk_num': self.participant.vars.get('num_lottery'),
                'df_num': self.participant.vars.get('num_df'),
                'risk_sel': self.participant.vars.get('selected_lottery'),
                'df_sel': self.participant.vars.get('selected_df'),
                'risk_won': self.participant.vars.get('won_or_lost'),
                }

    def is_displayed(self):
        return self.round_number == 12


class Start(Page):
    form_model = models.Player
    form_fields = ['age', 'sex',
                   'city', 'yearsinmsc', 'univ', 'study', 'riskat', 'fin_income', 'satis' ]
    def is_displayed(self):
        return (self.round_number % 12) == 0

class ToThink(Page):
    def vars_for_template(self):
        return {'saved': self.player.savings,
                'consumed': self.player.consumption,
                'income_was': self.player.disposable_income,

                'payoff': int(self.player.consumption/15),
                'month': int(self.player.round_number - 6)
                }



page_sequence = [
    IntroPage,
    ChoicePage,
    ToThink,
    Results,
    FinalResultsPage,
    Start
]
