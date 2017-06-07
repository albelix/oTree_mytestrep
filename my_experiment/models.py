from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_experiment'
    players_per_group = None
    num_rounds = 1
    win_probabilities = [0.05,0.1, 0.15, 0.2, 0.25,  0.3, 0.35, 0.4, 0.45, 0.5,
                         0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
    win_pay_A_a = 2000
    lose_pay_A_a= 1600
    win_pay_B_a = 4000
    lose_pay_B_a = 100

    win_pay_A_b = 1000
    lose_pay_A_b = 500
    win_pay_B_b = 2000
    lose_pay_B_b = 250

    interest_rates = [0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55]
    interest_rates_eff = [0.104, 0.159, 0.216, 0.274, 0.335, 0.399, 0.464, 0.532, 0.602, 0.674]
    base_sum = 1500

    conv_power_multiplier = -0.001
    conv_multiplier = 120


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):

    risk01 = models.CharField(choices=['A', 'B',],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk02 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk03 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk04 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk05 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk06 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk07 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk08 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk09 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk10 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk11 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk12 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk13 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk14 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk15 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk16 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk17 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk18 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk19 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    risk20 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")


    df2c01 = models.CharField(
                choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df2c02 = models.CharField( choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df2c03 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df2c04 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df2c05 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df2c06 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df2c07 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df2c08 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df2c09 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df2c10 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")

    df3c01 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df3c02 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df3c03 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df3c04 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df3c05 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df3c06 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df3c07 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df3c08 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df3c09 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df3c10 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    
    df4c01 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df4c02 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df4c03 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df4c04 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df4c05 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df4c06 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df4c07 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df4c08 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df4c09 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df4c10 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    
    df5c01 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df5c02 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df5c03 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df5c04 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df5c05 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df5c06 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df5c07 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df5c08 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df5c09 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df5c10 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    
    df6c01 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df6c02 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df6c03 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df6c04 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df6c05 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df6c06 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df6c07 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df6c08 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df6c09 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")
    df6c10 = models.CharField(choices=['A', 'B'],
                widget=widgets.RadioSelectHorizontal(),
                verbose_name="")

    risk01_pay = models.IntegerField()
    risk02_pay = models.IntegerField()
    risk03_pay = models.IntegerField()
    risk04_pay = models.IntegerField()
    risk05_pay = models.IntegerField()
    risk06_pay = models.IntegerField()
    risk07_pay = models.IntegerField()
    risk08_pay = models.IntegerField()
    risk09_pay = models.IntegerField()
    risk10_pay = models.IntegerField()
    risk11_pay = models.IntegerField()
    risk12_pay = models.IntegerField()
    risk13_pay = models.IntegerField()
    risk14_pay = models.IntegerField()
    risk15_pay = models.IntegerField()
    risk16_pay = models.IntegerField()
    risk17_pay = models.IntegerField()
    risk18_pay = models.IntegerField()
    risk19_pay = models.IntegerField()
    risk20_pay = models.IntegerField()

    risk01_res = models.CharField()
    risk02_res = models.CharField()
    risk03_res = models.CharField()
    risk04_res = models.CharField()
    risk05_res = models.CharField()
    risk06_res = models.CharField()
    risk07_res = models.CharField()
    risk08_res = models.CharField()
    risk09_res = models.CharField()
    risk10_res = models.CharField()
    risk11_res = models.CharField()
    risk12_res = models.CharField()
    risk13_res = models.CharField()
    risk14_res = models.CharField()
    risk15_res = models.CharField()
    risk16_res = models.CharField()
    risk17_res = models.CharField()
    risk18_res = models.CharField()
    risk19_res = models.CharField()
    risk20_res = models.CharField()


    df2c01_pay = models.PositiveIntegerField()
    df2c02_pay = models.PositiveIntegerField()
    df2c03_pay = models.PositiveIntegerField()
    df2c04_pay = models.PositiveIntegerField()
    df2c05_pay = models.PositiveIntegerField()
    df2c06_pay = models.PositiveIntegerField()
    df2c07_pay = models.PositiveIntegerField()
    df2c08_pay = models.PositiveIntegerField()
    df2c09_pay = models.PositiveIntegerField()
    df2c10_pay = models.PositiveIntegerField()

    df3c01_pay = models.PositiveIntegerField()
    df3c02_pay = models.PositiveIntegerField()
    df3c03_pay = models.PositiveIntegerField()
    df3c04_pay = models.PositiveIntegerField()
    df3c05_pay = models.PositiveIntegerField()
    df3c06_pay = models.PositiveIntegerField()
    df3c07_pay = models.PositiveIntegerField()
    df3c08_pay = models.PositiveIntegerField()
    df3c09_pay = models.PositiveIntegerField()
    df3c10_pay = models.PositiveIntegerField()
    
    df4c01_pay = models.PositiveIntegerField()
    df4c02_pay = models.PositiveIntegerField()
    df4c03_pay = models.PositiveIntegerField()
    df4c04_pay = models.PositiveIntegerField()
    df4c05_pay = models.PositiveIntegerField()
    df4c06_pay = models.PositiveIntegerField()
    df4c07_pay = models.PositiveIntegerField()
    df4c08_pay = models.PositiveIntegerField()
    df4c09_pay = models.PositiveIntegerField()
    df4c10_pay = models.PositiveIntegerField()
    
    df5c01_pay = models.PositiveIntegerField()
    df5c02_pay = models.PositiveIntegerField()
    df5c03_pay = models.PositiveIntegerField()
    df5c04_pay = models.PositiveIntegerField()
    df5c05_pay = models.PositiveIntegerField()
    df5c06_pay = models.PositiveIntegerField()
    df5c07_pay = models.PositiveIntegerField()
    df5c08_pay = models.PositiveIntegerField()
    df5c09_pay = models.PositiveIntegerField()
    df5c10_pay = models.PositiveIntegerField()
    
    df6c01_pay = models.PositiveIntegerField()
    df6c02_pay = models.PositiveIntegerField()
    df6c03_pay = models.PositiveIntegerField()
    df6c04_pay = models.PositiveIntegerField()
    df6c05_pay = models.PositiveIntegerField()
    df6c06_pay = models.PositiveIntegerField()
    df6c07_pay = models.PositiveIntegerField()
    df6c08_pay = models.PositiveIntegerField()
    df6c09_pay = models.PositiveIntegerField()
    df6c10_pay = models.PositiveIntegerField()

    #
    risk_P1_nat = models.IntegerField() #number of random lottery
    risk_P1_sel = models.CharField() #player's selection
    risk_P1_pay = models.IntegerField() #payment of random lottery
    risk_P1_res = models.CharField() #won/lost
    risk_payoff = models.CurrencyField()

    df_nat = models.IntegerField() #number of df game
    df_sel = models.CharField() #player's selection option
    df_pay = models.IntegerField() #payment of this option
    df_payoff = models.CurrencyField()



    def calc_payoff(self):
        self.payoff = self.risk_payoff__add__(self.df_payoff)
        return

    def some_method(self):
        return

