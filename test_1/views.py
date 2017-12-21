from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

import random
from django.shortcuts import render_to_response

class Round_0(Page):
    def is_displayed(self):
        return self.round_number == 1

class Round_1(Page):
    def is_displayed(self):
        return self.round_number == 2

class Round_2(Page):
    def is_displayed(self):
        return self.round_number == 3

class Round_3(Page):
    def is_displayed(self):
        return self.round_number == 4

class Round_4(Page):
    def is_displayed(self):
        return self.round_number == 5

class Coalition_to_be_or_not_to_be(Page):
    form_model = models.Player
    form_fields = ['coalition_marker']

    def is_displayed(self):
        return self.round_number != 1

class WaitPage0(WaitPage):
    pass

class ResultsWaitPage1(WaitPage):
    def after_all_players_arrive(self):
        self.group.is_in_coalition()


class Coalition_results_if_coalition(Page):

    def is_displayed(self):
        return len(self.group.in_coalition_inner) > 1

    def is_displayed(self):
        return self.round_number != 1

    def is_displayed(self):
        return self.player.coalition_marker

class Coalition_results_if_no_coalition(Page):

    def is_displayed(self):
        return len(self.group.in_coalition_inner) <= 1

    def is_displayed(self):
        return self.round_number != 1



class ResultsWaitPage2(WaitPage):
   def after_all_players_arrive(self):
        self.group.slider_randomisation()

class slder_proba(Page):
    form_model = models.Player
    form_fields = ['slider_1', 'slider_2', 'slider_3', 'slider_4', 'slider_5', 'slider_6', 'slider_7', 'slider_8', 'slider_9', 'slider_10',
                   'slider_11', 'slider_12', 'slider_13', 'slider_14', 'slider_15', 'slider_16', 'slider_17', 'slider_18', 'slider_19', 'slider_20',
                   'slider_21', 'slider_22', 'slider_23', 'slider_24', 'slider_25', 'slider_26', 'slider_27', 'slider_28', 'slider_29', 'slider_30']

    timeout_seconds = 60

class ResultsWaitPage3(WaitPage):
    def after_all_players_arrive(self):
        if self.round_number != 1:
            self.group.set_sliders()
            self.group.performance()
            self.group.payoff_for_coalition()
            self.group.payoff_for_non_coalition()

        else:
            self.group.set_sliders()
            self.group.performance()
            self.group.payoff_for_0_round()






class Payoff_page_2(Page):

    def vars_for_template(self):
        dict_with_perf_payoffs = {}
        for p in range(2):
            total_perf = 0
            total_payoff = 0

            for i in range(5):
                key = 'plr_' + str(p+1) + '_perf_round_' + str(i)
                dict_with_perf_payoffs[key] = self.group.get_player_by_id(p+1).in_round(i+1).plr_perf
                key = 'plr_' + str(p+1) + '_payoff_round_' + str(i)
                dict_with_perf_payoffs[key] = self.group.get_player_by_id(p+1).in_round(i+1).plr_payoff

                if self.group.get_player_by_id(p+1).in_round(i+1).plr_perf is None:
                    total_perf += 0
                else:
                    total_perf += self.group.get_player_by_id(p + 1).in_round(i + 1).plr_perf

                if self.group.get_player_by_id(p+1).in_round(i+1).plr_payoff is None:
                    total_payoff += 0
                else:
                    total_payoff += self.group.get_player_by_id(p + 1).in_round(i + 1).plr_payoff

            key = 'plr_' + str(p + 1) + '_total_perf'
            dict_with_perf_payoffs[key] = round(total_perf, 2)
            key = 'plr_' + str(p + 1) + '_total_payoff'
            dict_with_perf_payoffs[key] = round(total_payoff, 2)

        return dict_with_perf_payoffs


page_sequence = [
    Round_0,
    Round_1,
    Round_2,
    Round_3,
    Round_4,
    WaitPage0,
    Coalition_to_be_or_not_to_be,
    ResultsWaitPage1,
    Coalition_results_if_coalition,
    Coalition_results_if_no_coalition,
    ResultsWaitPage2,
    slder_proba,
    ResultsWaitPage3,
    Payoff_page_2
]
