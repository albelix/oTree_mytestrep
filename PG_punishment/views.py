from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Contribution(Page):
    form_model = models.Player
    form_fields = ['contribution']
    def vars_for_template(self):
        return {
           'current_round': self.subsession.round_number
        }

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

#    wait_for_all_groups=True

class Results0(Page):
    wait_for_all_players=True
    def vars_for_template(self):
        self.player.my_method()

class PunPage(Page):
    form_model = models.Player
    form_fields = ['pun_{}'.format(i) for i in range(1, 6)]
    def vars_for_template(self):
        self.player.my_method() # group.set_payoffs() # my_method()
        return {
            'my_payoff': sum([p.payoff for p in self.player.in_all_rounds()]),
            'me_in_all_rounds_1': self.group.get_player_by_id(1).my_payoff,
            'me_in_all_rounds_2': self.group.get_player_by_id(2).my_payoff,
            'me_in_all_rounds_3': self.group.get_player_by_id(3).my_payoff,
            'me_in_all_rounds_4': self.group.get_player_by_id(4).my_payoff,
            'me_in_all_rounds_5': self.group.get_player_by_id(5).my_payoff,
            'p1_contr': self.group.get_player_by_id(1).contribution,
            'p2_contr': self.group.get_player_by_id(2).contribution,
            'p3_contr': self.group.get_player_by_id(3).contribution,
            'p4_contr': self.group.get_player_by_id(4).contribution,
            'p5_contr': self.group.get_player_by_id(5).contribution,
            'current_round': self.subsession.round_number
        }

# class ResultsWaitPage1(WaitPage):
#     def after_all_players_arrive(self):
#         self.group.set_punpay()

class Results1(Page):
    wait_for_all_players=True
    def vars_for_template(self):
        self.player.my_method()


class Results(Page):
    def vars_for_template(self):
        self.player.my_method()
        return {
            'my_profit': sum([p.my_payoff for p in self.player.in_all_rounds()]),
            'my_in_all_rounds_1': self.group.get_player_by_id(1).my_payoff,
            'my_in_all_rounds_2': self.group.get_player_by_id(2).my_payoff,
            'my_in_all_rounds_3': self.group.get_player_by_id(3).my_payoff,
            'my_in_all_rounds_4': self.group.get_player_by_id(4).my_payoff,
            'my_in_all_rounds_5': self.group.get_player_by_id(5).my_payoff,
            'p1_sumcontr': self.group.get_player_by_id(1).contribution,
            'p2_sumcontr': self.group.get_player_by_id(2).contribution,
            'p3_sumcontr': self.group.get_player_by_id(3).contribution,
            'p4_sumcontr': self.group.get_player_by_id(4).contribution,
            'p5_sumcontr': self.group.get_player_by_id(5).contribution,
            'current_round': self.subsession.round_number
        }


page_sequence = [
    Contribution,
    ResultsWaitPage,
    Results0,
    PunPage,
#    ResultsWaitPage1,
    Results1,
    Results
]
