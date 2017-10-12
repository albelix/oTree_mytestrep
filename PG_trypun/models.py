from mock.mock import self
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
# from tables import group

#import random

from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree.db import models
#from otree import widgets
from otree.common import Currency as c, currency_range, safe_json

author = 'Alexis Belianin'

doc = """
PG game with punishment 
"""


class Constants(BaseConstants):
    name_in_url = 'PG_trypun'
    players_per_group = 5
    num_rounds = 8
    endowment = c(100)
    lumpsum = c(160)
    efficiency_factor = 2
    contribution_limits = currency_range(0, endowment, 1) #define range of contribs


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    round_num=models.IntegerField()
    # p1 = models.IntegerField()
    # p2 = models.IntegerField()
    # p3 = models.IntegerField()
    # p1_payoff = models.CurrencyField()
    # p2_payoff = models.CurrencyField()
    # p3_payoff = models.CurrencyField()
    # glob_contribution=models.CurrencyField()
    # glob_cont=models.CurrencyField()

    # def __init__(self):
    #    self.group = None
    def round_number(self):
        return self.subsession.round_number

# before punishment
    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.efficiency_factor / Constants.players_per_group
        for p in self.get_players():
            p.payoff = Constants.endowment - p.contribution + self.individual_share

# after punishment
    def set_punpay(self):
        for p in self.get_players():
            p.profit = p.payoff - p.pun - p.puncost
            # p1 = self.get_player_by_id(1)
            # p2 = self.get_player_by_id(2)
            # p3 = self.get_player_by_id(3)
            # p1_payoff = sum([p.payoff for p in self.in_previous_rounds() if p.p1 == 1])
            # p2_payoff = sum([p.payoff for p in self.in_previous_rounds() if p.p2 == 2])
            # p3_payoff = sum([p.payoff for p in self.in_previous_rounds() if p.p3 == 3])  # in_all_rounds
            print('p.payoff_is', p.profit)

    # def globcont(self):
    #     self.glob_contribution = sum([p.total_contribution for p in self.in_all_rounds()])
    #     for p in self.in_all_rounds():
    #         p.glob_cont = self.glob_contribution
    #         print('*******my_payoff is', p.globcont)

    # def set_payoffs_all(self):
    #     p1 = self.get_player_by_id(1)
    #     p2 = self.get_player_by_id(2)
    #     p3 = self.get_player_by_id(3)
    #     print('*******p1 is', self.p1)
    #     print('*******p2 is', self.p2)
    #     print('*******p3 is', self.p3)
    #     # p4 = self.get_player_by_id(4)
    #     # p5 = self.get_player_by_id(5)
    #     p1_payoff = sum([p.payoff for p in self.in_previous_rounds() if self.p1 == 1])
    #     p2_payoff = sum([p.payoff for p in self.in_previous_rounds() if self.p2 == 2])
    #     p3_payoff = sum([p.payoff for p in self.in_previous_rounds() if self.p3 == 3]) # in_all_rounds
    #     print('*******p1_payoff is', self.p1_payoff)
    #     print('*******p2_payoff is', self.p2_payoff)
    #     print('*******p3_payoff is', self.p3_payoff)
        # p2.payoff = sum([p.payoff for p2 in self.in_all_rounds()])
        # p3.payoff = sum([p.payoff for p3 in self.in_all_rounds()])
        # p4.payoff = sum([p4.payoff for p4 in self.in_all_rounds()])
        # p5.payoff = sum([p5.payoff for p5 in self.in_all_rounds()])

    # def sum_in_previous_round(self):
    #     return sum(p.in_previous_rounds()[-1].payoff for p in self.get_players())

class Player(BasePlayer):
    contribution = models.CurrencyField(doc="""The amount contributed by the player""", min=0,max=100) # choices=Constants.contribution_limits) #add this to see schedule of contribs
    payoff = models.CurrencyField()
    total_contribution = models.CurrencyField()
    my_contribution = models.CurrencyField(doc="""The amount contributed by the player""", )
    summy_contribution = models.CurrencyField(doc="""Total amount contributed by the player""")
    my_payoff = models.CurrencyField()
    my_profit = models.CurrencyField()
    pun=models.CurrencyField()
    pun_1 = models.CurrencyField(min=0,max=4,initial=0)
    pun_2 = models.CurrencyField(min=0,max=4,initial=0)
    pun_3 = models.CurrencyField(min=0,max=4,initial=0)
    pun_4 = models.CurrencyField(min=0,max=4,initial=0)
    pun_5 = models.CurrencyField(min=0,max=4,initial=0)
    profit = models.CurrencyField()
    mean_contribution = models.CurrencyField()
    puncost = models.CurrencyField()

# before punishment
    def my_method(self):
        self.my_contribution = sum([p.contribution for p in self.in_round(self.round_number)])#sum([p.contribution for p in self.in_all_rounds()])
        self.my_payoff = sum([p.payoff for p in self.in_round(self.round_number)])
        self.mean_contribution=sum(p.my_contribution for p in self.group.get_players())/5

# after punishment
    def my_method1(self):
        self.summy_contribution = sum([p.contribution for p in self.in_all_rounds()])
        self.my_profit = sum([p.profit for p in self.in_all_rounds()])


        if self.id_in_group == 1:
            pun=sum([p.pun_1 for p in self.subsession.get_players() if p.id_in_group != 1])
        if self.id_in_group == 2:
            pun=sum([p.pun_2 for p in self.subsession.get_players() if p.id_in_group != 2])
        if self.id_in_group == 3:
            pun=sum([p.pun_3 for p in self.subsession.get_players() if p.id_in_group != 3])
        if self.id_in_group == 4:
            pun=sum([p.pun_4 for p in self.subsession.get_players() if p.id_in_group != 4])
        else:
            pun=sum([p.pun_5 for p in self.subsession.get_players() if p.id_in_group != 5])

        #self.puncost = sum([p.pun for p in self.subsession.get_players()])*0.2
        self.puncost = (self.pun_1 + self.pun_2 + self.pun_3 + self.pun_4 + self.pun_5)*0.2
        #        self.others_choice = self.get_others_in_group()[1].my_payoff
        # for p in self.in_all_rounds():
        #     p.prof = p.my_payoff
        #     print('*******my_payoff is', p.prof)
        #     p.contr = p.my_contribution
        #     print('*******my_payoff is', p.contr)


