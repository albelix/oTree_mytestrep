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
    income_adj = [-600, 600]
    income_adj_weights = [0.5, 0.5]
    base_stab_income = 2000
    base_decr_income = 2100
    income_change_rate = 100
    conv_multiplier = 120
    conv_power_multiplier = -0.001
    r = 0.0083


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
            self.income = (Constants.base_stab_income +
                           random.choice(Constants.income_adj))
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

    city = models.PositiveIntegerField(
        verbose_name='''
    	    Сколько человек (приблизительно) проживало в том населенном пункте, где Вы жили в возрасте 16 лет.''',
        min=1, max=30000000,
        initial=None)

    yearsinmsc = models.PositiveIntegerField(
        verbose_name='''
    	    Укажите, сколько лет Вы живете в Москве. Впишите число, округленное до ближайшего целого числа лет.''',
        min=0, max=95,
        initial=None)


    univ = models.CharField(
        verbose_name='''Укажите ВУЗ, в котором учитесь(или который окончили).'''
    )

    study = models.CharField(
        verbose_name='''Укажите  направление подготовки, на котором Вы обучаетесь(или обучались).'''
    )
    riskat = models.PositiveIntegerField(
        verbose_name='''Вы любите риск или боитесь риска?''',
        choices=[
            [1, 'Очень люблю рисковать'],
            [2, 'Скорее люблю рисковать'],
            [3, 'Нейтрален к риску'],
            [4, 'Скорее боюсь рисковать'],
            [5, 'Очень боюсь рисковать'],
        ],
        widget=widgets.RadioSelect()
    )

    fin_income = models.PositiveIntegerField(
        verbose_name='''Какое высказывание наиболее точно описывает финансовое положение вашей семьи?''',
        choices=[
            [1, 'Едва сводим концы с концами, денег не хватает на выживание;'],
            [2, 'Живем от зарплаты до зарплаты, денег хватает только на неотложные нужды;'],
            [3, 'На ежедневные расходы хватает денег, но уже покупка одежды требует накоплений;'],
            [4,
             'Вполне хватает денег, даже имеются некоторые накопления, но крупные покупки требуется планировать заранее;'],
            [5, 'Можем позволить себе крупные траты при первой необходимости.'],
        ],
        widget=widgets.RadioSelect()
    )

    satis = models.PositiveIntegerField(
        verbose_name='''Учитывая все обстоятельства, насколько Вы удовлетворены вашей жизнью в целом в эти дни? (от 1 «полностью не удовлетворен» до 10 «полностью удовлетворен»)''',
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal()
    )

    mobile = models.IntegerField()