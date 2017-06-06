from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_big_experiment'
    players_per_group = None
    num_rounds = 12
    income_adj = [-100, 100]
    income_adj_weights = [0.5, 0.5]
    base_stab_income = 1000
    base_decr_income = 2100
    income_change_rate = 100
    conv_multiplier = 500
    conv_power_multiplier = -0.02
    r = 0.2


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.calc_income()
            p.calc_savings()
            p.calc_disposable_income()
        return


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    grow_then_fall = models.BooleanField()
    income = models.IntegerField()
    consumption = models.PositiveIntegerField()
    savings = models.IntegerField()
    disposable_income = models.IntegerField()
    paying_period = models.IntegerField()

    name = models.CharField()
    age = models.IntegerField()
    sex = models.IntegerField(choices=[[1, 'Мужчина'], [2, 'Женщина']],
                              widget=widgets.RadioSelectHorizontal(),
                              verbose_name="")
    budget = models.PositiveIntegerField(initial=0)

    #
    # Calculating income
    def calc_income(self):
        time_elapsed = self.round_number % 6
        if time_elapsed == 1:
            self.income = Constants.base_stab_income
        else:
            self.income = (Constants.base_stab_income + random.choices(Constants.income_adj, weights=0.5, k=1)[0])
        return

    def calc_savings(self):
        if self.round_number == 1:
            self.savings = 0
        return

    def calc_starting_savings_for_next_round(self):
        if self.round_number < Constants.num_rounds:
            if self.round_number % 6 == 0:
                self.in_round(self.round_number + 1).savings = 0
            else:
                self.in_round(self.round_number + 1).savings = self.savings
        return

    def calc_DI_for_next_round(self):
        if self.round_number < Constants.num_rounds:
            self.in_round(self.round_number + 1).disposable_income = (
                self.in_round(self.round_number + 1).income +
                self.in_round(self.round_number + 1).savings)
        return

    def calc_disposable_income(self):
        if self.round_number == 1:
            self.disposable_income = self.income + self.savings
        return


