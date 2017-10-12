from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Alexis Belianin'

doc = """
PG game for CUSb, 2nd less than min stage
"""


class Constants(BaseConstants):
    name_in_url = 'my_PGmin'
    players_per_group = 5
    num_rounds = 12
    endowment=c(100)
    efficiency_factor=2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    mean_contribution = models.CurrencyField()

    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.efficiency_factor / Constants.players_per_group
        self.mean_contribution = self.total_contribution /  Constants.players_per_group
        for p in self.get_players():
            p.payoff = Constants.endowment - p.contribution + self.individual_share
            print('*******p.payoff is', p.payoff)
        self.subsession_get_players = [
            p for p in self.subsession.get_players() if self.contribution < self.mean_contributon == 11]

class Player(BasePlayer):
    contribution = models.CurrencyField(min=0, max=Constants.endowment)
    pass
