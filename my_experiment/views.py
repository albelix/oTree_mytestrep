from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

# Extra imports
import random


def calc_return_a(decision, prob):
    nature_outcome = random.choices(['W', 'L'], weights = [prob, 1-prob])[0]
    if nature_outcome == 'W':
        if decision == 'A':
            nature_pay = Constants.win_pay_A_a
        else:
            nature_pay = Constants.win_pay_B_a
    else:
        if decision == 'A':
            nature_pay = Constants.lose_pay_A_a
        else:
            nature_pay = Constants.lose_pay_B_a
    return nature_pay, nature_outcome

def calc_return_b(decision, prob):
    nature_outcome = random.choices(['W', 'L'], weights = [prob, 1-prob])[0]
    if nature_outcome == 'W':
        if decision == 'A':
            nature_pay = Constants.win_pay_A_b
        else:
            nature_pay = Constants.win_pay_B_b
    else:
        if decision == 'A':
            nature_pay = Constants.lose_pay_A_b
        else:
            nature_pay = Constants.lose_pay_B_b
    return nature_pay, nature_outcome


def calc_offer(periods_count, annual_rate):
    monthly_rate = (annual_rate / 12)
    return_sum = (Constants.base_sum * 
            ((1 + monthly_rate) ** periods_count))
    return return_sum


def df_payment(decision, period, rate_id):
    if decision == 'A':
        nature_pay = Constants.base_sum
    else:
        nature_pay = calc_offer(period, Constants.interest_rates[rate_id])
    return nature_pay



class Lottery_risk_P1(Page):
    form_model = models.Player
    form_fields = ['risk01', 'risk02', 'risk03', 'risk04', 'risk05',
            'risk06', 'risk07', 'risk08', 'risk09', 'risk10', 'risk11', 'risk12', 'risk13', 'risk14', 'risk15',
            'risk16', 'risk17', 'risk18', 'risk19', 'risk20']
    def vars_for_template(self):
        win_p01 = Constants.win_probabilities[0]
        win_p02 = Constants.win_probabilities[1]
        win_p03 = Constants.win_probabilities[2]
        win_p04 = Constants.win_probabilities[3]
        win_p05 = Constants.win_probabilities[4]
        win_p06 = Constants.win_probabilities[5]
        win_p07 = Constants.win_probabilities[6]
        win_p08 = Constants.win_probabilities[7]
        win_p09 = Constants.win_probabilities[8]
        win_p10 = Constants.win_probabilities[9]
        win_p11 = Constants.win_probabilities[10]
        win_p12 = Constants.win_probabilities[11]
        win_p13 = Constants.win_probabilities[12]
        win_p14 = Constants.win_probabilities[13]
        win_p15 = Constants.win_probabilities[14]
        win_p16 = Constants.win_probabilities[15]
        win_p17 = Constants.win_probabilities[16]
        win_p18 = Constants.win_probabilities[17]
        win_p19 = Constants.win_probabilities[18]
        win_p20 = Constants.win_probabilities[19]
        lose_p01 = 1 - win_p01
        lose_p02 = 1 - win_p02
        lose_p03 = 1 - win_p03
        lose_p04 = 1 - win_p04
        lose_p05 = 1 - win_p05
        lose_p06 = 1 - win_p06
        lose_p07 = 1 - win_p07
        lose_p08 = 1 - win_p08
        lose_p09 = 1 - win_p09
        lose_p10 = 1 - win_p10
        lose_p11 = 1 - win_p11
        lose_p12 = 1 - win_p12
        lose_p13 = 1 - win_p13
        lose_p14 = 1 - win_p14
        lose_p15 = 1 - win_p15
        lose_p16 = 1 - win_p16
        lose_p17 = 1 - win_p17
        lose_p18 = 1 - win_p18
        lose_p19 = 1 - win_p19
        lose_p20 = 1 - win_p20

        return {'win_p01':win_p01, 'win_p02':win_p02, 'win_p03':win_p03,
                'win_p04':win_p04, 'win_p05':win_p05,
                'win_p06':win_p06, 'win_p07':win_p07, 'win_p08':win_p08, 'win_p09':win_p09, 'win_p10':win_p10,
                'win_p11':win_p11, 'win_p12':win_p12, 'win_p13':win_p13, 'win_p14':win_p14, 'win_p15':win_p15, 
                'win_p16':win_p16, 'win_p17':win_p17, 'win_p18':win_p18, 'win_p19':win_p19, 'win_p20':win_p20,
                'lose_p01':lose_p01, 'lose_p02':lose_p02, 'lose_p03':lose_p03, 'lose_p04':lose_p04, 'lose_p05':lose_p05,
                'lose_p06':lose_p06, 'lose_p07':lose_p07, 'lose_p08':lose_p08, 'lose_p09':lose_p09, 'lose_p10':lose_p10,
                'lose_p11': lose_p11, 'lose_p12': lose_p12, 'lose_p13': lose_p13, 'lose_p14': lose_p14, 'lose_p15': lose_p15,
                'lose_p16': lose_p16, 'lose_p17': lose_p17, 'lose_p18': lose_p18, 'lose_p19': lose_p19, 'lose_p20': lose_p20}

    def before_next_page(self):
        self.player.risk01_pay, self.player.risk01_res = calc_return_a(
                self.player.risk01, Constants.win_probabilities[0])
        self.player.risk02_pay, self.player.risk02_res = calc_return_a(
                self.player.risk02, Constants.win_probabilities[1])
        self.player.risk03_pay, self.player.risk03_res = calc_return_a(
                self.player.risk03, Constants.win_probabilities[2])
        self.player.risk04_pay, self.player.risk04_res = calc_return_a(
                self.player.risk04, Constants.win_probabilities[3])
        self.player.risk05_pay, self.player.risk05_res = calc_return_a(
                self.player.risk05, Constants.win_probabilities[4])
        self.player.risk06_pay, self.player.risk06_res = calc_return_a(
                self.player.risk06, Constants.win_probabilities[5])
        self.player.risk07_pay, self.player.risk07_res = calc_return_a(
                self.player.risk07, Constants.win_probabilities[6])
        self.player.risk08_pay, self.player.risk08_res = calc_return_a(
                self.player.risk08, Constants.win_probabilities[7])
        self.player.risk09_pay, self.player.risk09_res = calc_return_a(
                self.player.risk09, Constants.win_probabilities[8])
        self.player.risk10_pay, self.player.risk10_res = calc_return_a(
                self.player.risk10, Constants.win_probabilities[9])
        self.player.risk11_pay, self.player.risk11_res = calc_return_a(
                self.player.risk11, Constants.win_probabilities[10])
        self.player.risk12_pay, self.player.risk12_res = calc_return_a(
            self.player.risk12, Constants.win_probabilities[11])
        self.player.risk13_pay, self.player.risk13_res = calc_return_a(
            self.player.risk13, Constants.win_probabilities[12])
        self.player.risk14_pay, self.player.risk14_res = calc_return_a(
            self.player.risk14, Constants.win_probabilities[13])
        self.player.risk15_pay, self.player.risk15_res = calc_return_a(
            self.player.risk15, Constants.win_probabilities[14])
        self.player.risk16_pay, self.player.risk16_res = calc_return_a(
            self.player.risk16, Constants.win_probabilities[15])
        self.player.risk17_pay, self.player.risk17_res = calc_return_a(
            self.player.risk17, Constants.win_probabilities[16])
        self.player.risk18_pay, self.player.risk18_res = calc_return_a(
            self.player.risk18, Constants.win_probabilities[17])
        self.player.risk19_pay, self.player.risk19_res = calc_return_a(
            self.player.risk19, Constants.win_probabilities[18])
        self.player.risk20_pay, self.player.risk20_res = calc_return_a(
            self.player.risk20, Constants.win_probabilities[19])

        payoffs_dict = {
            1: [self.player.risk01, self.player.risk01_res,
                self.player.risk01_pay],
            2: [self.player.risk02, self.player.risk02_res,
                self.player.risk02_pay],
            3: [self.player.risk03, self.player.risk03_res,
                self.player.risk03_pay],
            4: [self.player.risk04, self.player.risk04_res,
                self.player.risk04_pay],
            5: [self.player.risk05, self.player.risk05_res,
                self.player.risk05_pay],
            6: [self.player.risk06, self.player.risk06_res,
                self.player.risk06_pay],
            7: [self.player.risk07, self.player.risk07_res,
                self.player.risk07_pay],
            8: [self.player.risk08, self.player.risk08_res,
                self.player.risk08_pay],
            9: [self.player.risk09, self.player.risk09_res,
                self.player.risk09_pay],
            10: [self.player.risk10, self.player.risk10_res,
                 self.player.risk10_pay],
            11: [self.player.risk11, self.player.risk11_res,
                 self.player.risk11_pay],
            12: [self.player.risk12, self.player.risk12_res,
                 self.player.risk12_pay],
            13: [self.player.risk13, self.player.risk13_res,
                 self.player.risk13_pay],
            14: [self.player.risk14, self.player.risk14_res,
                 self.player.risk14_pay],
            15: [self.player.risk15, self.player.risk15_res,
                 self.player.risk15_pay],
            16: [self.player.risk16, self.player.risk16_res,
                 self.player.risk16_pay],
            17: [self.player.risk17, self.player.risk17_res,
                 self.player.risk17_pay],
            18: [self.player.risk18, self.player.risk18_res,
                 self.player.risk18_pay],
            19: [self.player.risk19, self.player.risk19_res,
                 self.player.risk19_pay],
            20: [self.player.risk20, self.player.risk20_res,
                 self.player.risk20_pay]}
        # range from a to (b less 1)
        selected_key = random.choice(range(1, 21))
        self.player.risk_P1_nat = selected_key
        self.player.risk_P1_sel = payoffs_dict[selected_key][0]
        self.player.risk_P1_res = payoffs_dict[selected_key][1]
        self.player.risk_P1_pay = payoffs_dict[selected_key][2]


        return


class Lottery_risk_P1_res(Page):
    form_model = models.Player
    pass


class Discount_M2(Page):
    form_model = models.Player
    form_fields = ['df2c01', 'df2c02', 'df2c03', 'df2c04',
            'df2c05', 'df2c06', 'df2c07', 'df2c08', 'df2c09', 'df2c10'] 
    def vars_for_template(self):
        offer_1 = calc_offer(1, Constants.interest_rates[0])
        offer_2 = calc_offer(1, Constants.interest_rates[1])
        offer_3 = calc_offer(1, Constants.interest_rates[2])
        offer_4 = calc_offer(1, Constants.interest_rates[3])
        offer_5 = calc_offer(1, Constants.interest_rates[4])
        offer_6 = calc_offer(1, Constants.interest_rates[5])
        offer_7 = calc_offer(1, Constants.interest_rates[6])
        offer_8 = calc_offer(1, Constants.interest_rates[7])
        offer_9 = calc_offer(1, Constants.interest_rates[8])
        offer_10 = calc_offer(1, Constants.interest_rates[9])
        json_construct = {
                'offer_1':offer_1,
                'offer_2':offer_2,
                'offer_3':offer_3,
                'offer_4':offer_4,
                'offer_5':offer_5,
                'offer_6':offer_6,
                'offer_7':offer_7,
                'offer_8':offer_8,
                'offer_9':offer_9,
                'offer_10':offer_10,
                'rate_01':'{:.2}'.format(Constants.interest_rates[0]),
                'rate_02':'{:.2}'.format(Constants.interest_rates[1]),
                'rate_03':'{:.2}'.format(Constants.interest_rates[2]),
                'rate_04':'{:.2}'.format(Constants.interest_rates[3]),
                'rate_05':'{:.2}'.format(Constants.interest_rates[4]),
                'rate_06':'{:.2}'.format(Constants.interest_rates[5]),
                'rate_07':'{:.2}'.format(Constants.interest_rates[6]),
                'rate_08':'{:.2}'.format(Constants.interest_rates[7]),
                'rate_09':'{:.2}'.format(Constants.interest_rates[8]),
                'rate_10':'{:.2}'.format(Constants.interest_rates[9]),
                'months_short':1,
                'months_long':2}
        return json_construct
    
    def before_next_page(self):
        self.player.df2c01_pay = df_payment(self.player.df2c01, 1, 0)
        self.player.df2c02_pay = df_payment(self.player.df2c02, 1, 1)
        self.player.df2c03_pay = df_payment(self.player.df2c03, 1, 2)
        self.player.df2c04_pay = df_payment(self.player.df2c04, 1, 3)
        self.player.df2c05_pay = df_payment(self.player.df2c05, 1, 4)
        self.player.df2c06_pay = df_payment(self.player.df2c06, 1, 5)
        self.player.df2c07_pay = df_payment(self.player.df2c07, 1, 6)
        self.player.df2c08_pay = df_payment(self.player.df2c08, 1, 7)
        self.player.df2c09_pay = df_payment(self.player.df2c09, 1, 8)
        self.player.df2c10_pay = df_payment(self.player.df2c10, 1, 9)
        return 
    
class Discount_M3(Page):
    form_model = models.Player
    form_fields = ['df3c01', 'df3c02', 'df3c03', 'df3c04',
            'df3c05', 'df3c06', 'df3c07', 'df3c08', 'df3c09', 'df3c10'] 
    def vars_for_template(self):
        offer_11 = calc_offer(2, Constants.interest_rates[0])
        offer_12 = calc_offer(2, Constants.interest_rates[1])
        offer_13 = calc_offer(2, Constants.interest_rates[2])
        offer_14 = calc_offer(2, Constants.interest_rates[3])
        offer_15 = calc_offer(2, Constants.interest_rates[4])
        offer_16 = calc_offer(2, Constants.interest_rates[5])
        offer_17 = calc_offer(2, Constants.interest_rates[6])
        offer_18 = calc_offer(2, Constants.interest_rates[7])
        offer_19 = calc_offer(2, Constants.interest_rates[8])
        offer_20 = calc_offer(2, Constants.interest_rates[9])
        json_construct = {
                'offer_11':offer_11,
                'offer_12':offer_12,
                'offer_13':offer_13,
                'offer_14':offer_14,
                'offer_15':offer_15,
                'offer_16':offer_16,
                'offer_17':offer_17,
                'offer_18':offer_18,
                'offer_19':offer_19,
                'offer_20':offer_20,
                'rate_01':'{:.2}'.format(Constants.interest_rates[0]),
                'rate_02':'{:.2}'.format(Constants.interest_rates[1]),
                'rate_03':'{:.2}'.format(Constants.interest_rates[2]),
                'rate_04':'{:.2}'.format(Constants.interest_rates[3]),
                'rate_05':'{:.2}'.format(Constants.interest_rates[4]),
                'rate_06':'{:.2}'.format(Constants.interest_rates[5]),
                'rate_07':'{:.2}'.format(Constants.interest_rates[6]),
                'rate_08':'{:.2}'.format(Constants.interest_rates[7]),
                'rate_09':'{:.2}'.format(Constants.interest_rates[8]),
                'rate_10':'{:.2}'.format(Constants.interest_rates[9]),
                'months_short':1,
                'months_long':3}
        return json_construct
    
    def before_next_page(self):
        self.player.df3c01_pay = df_payment(self.player.df3c01, 2, 0)
        self.player.df3c02_pay = df_payment(self.player.df3c02, 2, 1)
        self.player.df3c03_pay = df_payment(self.player.df3c03, 2, 2)
        self.player.df3c04_pay = df_payment(self.player.df3c04, 2, 3)
        self.player.df3c05_pay = df_payment(self.player.df3c05, 2, 4)
        self.player.df3c06_pay = df_payment(self.player.df3c06, 2, 5)
        self.player.df3c07_pay = df_payment(self.player.df3c07, 2, 6)
        self.player.df3c08_pay = df_payment(self.player.df3c08, 2, 7)
        self.player.df3c09_pay = df_payment(self.player.df3c09, 2, 8)
        self.player.df3c10_pay = df_payment(self.player.df3c10, 2, 9)
        return 
    
class Discount_M4(Page):
    form_model = models.Player
    form_fields = ['df4c01', 'df4c02', 'df4c03', 'df4c04',
            'df4c05', 'df4c06', 'df4c07', 'df4c08', 'df4c09', 'df4c10'] 
    def vars_for_template(self):
        offer_21 = calc_offer(3, Constants.interest_rates[0])
        offer_22 = calc_offer(3, Constants.interest_rates[1])
        offer_23 = calc_offer(3, Constants.interest_rates[2])
        offer_24 = calc_offer(3, Constants.interest_rates[3])
        offer_25 = calc_offer(3, Constants.interest_rates[4])
        offer_26 = calc_offer(3, Constants.interest_rates[5])
        offer_27 = calc_offer(3, Constants.interest_rates[6])
        offer_28 = calc_offer(3, Constants.interest_rates[7])
        offer_29 = calc_offer(3, Constants.interest_rates[8])
        offer_30 = calc_offer(3, Constants.interest_rates[9])
        json_construct = {
                'offer_21':offer_21,
                'offer_22':offer_22,
                'offer_23':offer_23,
                'offer_24':offer_24,
                'offer_25':offer_25,
                'offer_26':offer_26,
                'offer_27':offer_27,
                'offer_28':offer_28,
                'offer_29':offer_29,
                'offer_30':offer_30,
                'rate_01':'{:.2}'.format(Constants.interest_rates[0]),
                'rate_02':'{:.2}'.format(Constants.interest_rates[1]),
                'rate_03':'{:.2}'.format(Constants.interest_rates[2]),
                'rate_04':'{:.2}'.format(Constants.interest_rates[3]),
                'rate_05':'{:.2}'.format(Constants.interest_rates[4]),
                'rate_06':'{:.2}'.format(Constants.interest_rates[5]),
                'rate_07':'{:.2}'.format(Constants.interest_rates[6]),
                'rate_08':'{:.2}'.format(Constants.interest_rates[7]),
                'rate_09':'{:.2}'.format(Constants.interest_rates[8]),
                'rate_10':'{:.2}'.format(Constants.interest_rates[9]),
                'months_short':1,
                'months_long':4}
        return json_construct

    def before_next_page(self):
        self.player.df4c01_pay = df_payment(self.player.df4c01, 3, 0)
        self.player.df4c02_pay = df_payment(self.player.df4c02, 3, 1)
        self.player.df4c03_pay = df_payment(self.player.df4c03, 3, 2)
        self.player.df4c04_pay = df_payment(self.player.df4c04, 3, 3)
        self.player.df4c05_pay = df_payment(self.player.df4c05, 3, 4)
        self.player.df4c06_pay = df_payment(self.player.df4c06, 3, 5)
        self.player.df4c07_pay = df_payment(self.player.df4c07, 3, 6)
        self.player.df4c08_pay = df_payment(self.player.df4c08, 3, 7)
        self.player.df4c09_pay = df_payment(self.player.df4c09, 3, 8)
        self.player.df4c10_pay = df_payment(self.player.df4c10, 3, 9)
        return


class Discount_M5(Page):
    form_model = models.Player
    form_fields = ['df5c01', 'df5c02', 'df5c03', 'df5c04',
                   'df5c05', 'df5c06', 'df5c07', 'df5c08', 'df5c09', 'df5c10']

    def vars_for_template(self):
        offer_31 = calc_offer(4, Constants.interest_rates[0])
        offer_32 = calc_offer(4, Constants.interest_rates[1])
        offer_33 = calc_offer(4, Constants.interest_rates[2])
        offer_34 = calc_offer(4, Constants.interest_rates[3])
        offer_35 = calc_offer(4, Constants.interest_rates[4])
        offer_36 = calc_offer(4, Constants.interest_rates[5])
        offer_37 = calc_offer(4, Constants.interest_rates[6])
        offer_38 = calc_offer(4, Constants.interest_rates[7])
        offer_39 = calc_offer(4, Constants.interest_rates[8])
        offer_40 = calc_offer(4, Constants.interest_rates[9])
        json_construct = {
            'offer_31': offer_31,
            'offer_32': offer_32,
            'offer_33': offer_33,
            'offer_34': offer_34,
            'offer_35': offer_35,
            'offer_36': offer_36,
            'offer_37': offer_37,
            'offer_38': offer_38,
            'offer_39': offer_39,
            'offer_40': offer_40,
            'rate_01': '{:.2}'.format(Constants.interest_rates[0]),
            'rate_02': '{:.2}'.format(Constants.interest_rates[1]),
            'rate_03': '{:.2}'.format(Constants.interest_rates[2]),
            'rate_04': '{:.2}'.format(Constants.interest_rates[3]),
            'rate_05': '{:.2}'.format(Constants.interest_rates[4]),
            'rate_06': '{:.2}'.format(Constants.interest_rates[5]),
            'rate_07': '{:.2}'.format(Constants.interest_rates[6]),
            'rate_08': '{:.2}'.format(Constants.interest_rates[7]),
            'rate_09': '{:.2}'.format(Constants.interest_rates[8]),
            'rate_10': '{:.2}'.format(Constants.interest_rates[9]),
            'months_short': 1,
            'months_long': 5}
        return json_construct

    def before_next_page(self):
        self.player.df5c01_pay = df_payment(self.player.df5c01, 4, 0)
        self.player.df5c02_pay = df_payment(self.player.df5c02, 4, 1)
        self.player.df5c03_pay = df_payment(self.player.df5c03, 4, 2)
        self.player.df5c04_pay = df_payment(self.player.df5c04, 4, 3)
        self.player.df5c05_pay = df_payment(self.player.df5c05, 4, 4)
        self.player.df5c06_pay = df_payment(self.player.df5c06, 4, 5)
        self.player.df5c07_pay = df_payment(self.player.df5c07, 4, 6)
        self.player.df5c08_pay = df_payment(self.player.df5c08, 4, 7)
        self.player.df5c09_pay = df_payment(self.player.df5c09, 4, 8)
        self.player.df5c10_pay = df_payment(self.player.df5c10, 4, 9)
        return

class Discount_M6(Page):
    form_model = models.Player
    form_fields = ['df6c01', 'df6c02', 'df6c03', 'df6c04',
                   'df6c05', 'df6c06', 'df6c07', 'df6c08', 'df6c09', 'df6c10']

    def vars_for_template(self):
        offer_41 = calc_offer(5, Constants.interest_rates[0])
        offer_42 = calc_offer(5, Constants.interest_rates[1])
        offer_43 = calc_offer(5, Constants.interest_rates[2])
        offer_44 = calc_offer(5, Constants.interest_rates[3])
        offer_45 = calc_offer(5, Constants.interest_rates[4])
        offer_46 = calc_offer(5, Constants.interest_rates[5])
        offer_47 = calc_offer(5, Constants.interest_rates[6])
        offer_48 = calc_offer(5, Constants.interest_rates[7])
        offer_49 = calc_offer(5, Constants.interest_rates[8])
        offer_50 = calc_offer(5, Constants.interest_rates[9])
        json_construct = {
            'offer_41': offer_41,
            'offer_42': offer_42,
            'offer_43': offer_43,
            'offer_44': offer_44,
            'offer_45': offer_45,
            'offer_46': offer_46,
            'offer_47': offer_47,
            'offer_48': offer_48,
            'offer_49': offer_49,
            'offer_50': offer_50,
            'rate_01': '{:.2}'.format(Constants.interest_rates[0]),
            'rate_02': '{:.2}'.format(Constants.interest_rates[1]),
            'rate_03': '{:.2}'.format(Constants.interest_rates[2]),
            'rate_04': '{:.2}'.format(Constants.interest_rates[3]),
            'rate_05': '{:.2}'.format(Constants.interest_rates[4]),
            'rate_06': '{:.2}'.format(Constants.interest_rates[5]),
            'rate_07': '{:.2}'.format(Constants.interest_rates[6]),
            'rate_08': '{:.2}'.format(Constants.interest_rates[7]),
            'rate_09': '{:.2}'.format(Constants.interest_rates[8]),
            'rate_10': '{:.2}'.format(Constants.interest_rates[9]),
            'months_short': 1,
            'months_long': 6}

        return json_construct

    def before_next_page(self):

        offer_01 = df_payment(self.player.df2c01, 1, 0)
        offer_02 = df_payment(self.player.df2c02, 1, 1)
        offer_03 = df_payment(self.player.df2c03, 1, 2)
        offer_04 = df_payment(self.player.df2c04, 1, 3)
        offer_05 = df_payment(self.player.df2c05, 1, 4)
        offer_06 = df_payment(self.player.df2c06, 1, 5)
        offer_07 = df_payment(self.player.df2c07, 1, 6)
        offer_08 = df_payment(self.player.df2c08, 1, 7)
        offer_09 = df_payment(self.player.df2c09, 1, 8)
        offer_10 = df_payment(self.player.df2c10, 1, 9)
        offer_11 = df_payment(self.player.df3c01, 2, 0)
        offer_12 = df_payment(self.player.df3c02, 2, 1)
        offer_13 = df_payment(self.player.df3c03, 2, 2)
        offer_14 = df_payment(self.player.df3c04, 2, 3)
        offer_15 = df_payment(self.player.df3c05, 2, 4)
        offer_16 = df_payment(self.player.df3c06, 2, 5)
        offer_17 = df_payment(self.player.df3c07, 2, 6)
        offer_18 = df_payment(self.player.df3c08, 2, 7)
        offer_19 = df_payment(self.player.df3c09, 2, 8)
        offer_20 = df_payment(self.player.df3c10, 2, 9)
        offer_21 = df_payment(self.player.df4c01, 3, 0)
        offer_22 = df_payment(self.player.df4c02, 3, 1)
        offer_23 = df_payment(self.player.df4c03, 3, 2)
        offer_24 = df_payment(self.player.df4c04, 3, 3)
        offer_25 = df_payment(self.player.df4c05, 3, 4)
        offer_26 = df_payment(self.player.df4c06, 3, 5)
        offer_27 = df_payment(self.player.df4c07, 3, 6)
        offer_28 = df_payment(self.player.df4c08, 3, 7)
        offer_29 = df_payment(self.player.df4c09, 3, 8)
        offer_30 = df_payment(self.player.df4c10, 3, 9)
        offer_31 = df_payment(self.player.df5c01, 4, 0)
        offer_32 = df_payment(self.player.df5c02, 4, 1)
        offer_33 = df_payment(self.player.df5c03, 4, 2)
        offer_34 = df_payment(self.player.df5c04, 4, 3)
        offer_35 = df_payment(self.player.df5c05, 4, 4)
        offer_36 = df_payment(self.player.df5c06, 4, 5)
        offer_37 = df_payment(self.player.df5c07, 4, 6)
        offer_38 = df_payment(self.player.df5c08, 4, 7)
        offer_39 = df_payment(self.player.df5c09, 4, 8)
        offer_40 = df_payment(self.player.df5c10, 4, 9)
        offer_41 = df_payment(self.player.df6c01, 5, 0)
        offer_42 = df_payment(self.player.df6c02, 5, 1)
        offer_43 = df_payment(self.player.df6c03, 5, 2)
        offer_44 = df_payment(self.player.df6c04, 5, 3)
        offer_45 = df_payment(self.player.df6c05, 5, 4)
        offer_46 = df_payment(self.player.df6c06, 5, 5)
        offer_47 = df_payment(self.player.df6c07, 5, 6)
        offer_48 = df_payment(self.player.df6c08, 5, 7)
        offer_49 = df_payment(self.player.df6c09, 5, 8)
        offer_50 = df_payment(self.player.df6c10, 5, 9)
        df_payoffs_dict = {
            1: [self.player.df2c01, offer_01],
            2: [self.player.df2c02, offer_02],
            3: [self.player.df2c03, offer_03],
            4: [self.player.df2c04, offer_04],
            5: [self.player.df2c05, offer_05],
            6: [self.player.df2c06, offer_06],
            7: [self.player.df2c07, offer_07],
            8: [self.player.df2c08, offer_08],
            9: [self.player.df2c09, offer_09],
            10: [self.player.df3c10, offer_10],
            11: [self.player.df3c01, offer_11],
            12: [self.player.df3c02, offer_12],
            13: [self.player.df3c03, offer_13],
            14: [self.player.df3c04, offer_14],
            15: [self.player.df3c05, offer_15],
            16: [self.player.df3c06, offer_16],
            17: [self.player.df3c07, offer_17],
            18: [self.player.df3c08, offer_18],
            19: [self.player.df3c09, offer_19],
            20: [self.player.df3c10, offer_20],
            21: [self.player.df4c01, offer_21],
            22: [self.player.df4c02, offer_22],
            23: [self.player.df4c03, offer_23],
            24: [self.player.df4c04, offer_24],
            25: [self.player.df4c05, offer_25],
            26: [self.player.df4c06, offer_26],
            27: [self.player.df4c07, offer_27],
            28: [self.player.df4c08, offer_28],
            29: [self.player.df4c09, offer_29],
            30: [self.player.df4c10, offer_30],
            31: [self.player.df5c01, offer_31],
            32: [self.player.df5c02, offer_32],
            33: [self.player.df5c03, offer_33],
            34: [self.player.df5c04, offer_34],
            35: [self.player.df5c05, offer_35],
            36: [self.player.df5c06, offer_36],
            37: [self.player.df5c07, offer_37],
            38: [self.player.df5c08, offer_38],
            39: [self.player.df5c09, offer_39],
            40: [self.player.df5c10, offer_40],
            41: [self.player.df6c01, offer_41],
            42: [self.player.df6c02, offer_42],
            43: [self.player.df6c03, offer_43],
            44: [self.player.df6c04, offer_44],
            45: [self.player.df6c05, offer_45],
            46: [self.player.df6c06, offer_46],
            47: [self.player.df6c07, offer_47],
            48: [self.player.df6c08, offer_48],
            49: [self.player.df6c09, offer_49],
            50: [self.player.df6c10, offer_50]}
        selected_key = random.choice(range(1, 51))
        self.player.df_nat = selected_key
        self.player.df_sel = df_payoffs_dict[selected_key][0]
        self.player.df_pay = df_payoffs_dict[selected_key][1]

        self.player.df6c01_pay = df_payment(self.player.df6c01, 5, 0)
        self.player.df6c02_pay = df_payment(self.player.df6c02, 5, 1)
        self.player.df6c03_pay = df_payment(self.player.df6c03, 5, 2)
        self.player.df6c04_pay = df_payment(self.player.df6c04, 5, 3)
        self.player.df6c05_pay = df_payment(self.player.df6c05, 5, 4)
        self.player.df6c06_pay = df_payment(self.player.df6c06, 5, 5)
        self.player.df6c07_pay = df_payment(self.player.df6c07, 5, 6)
        self.player.df6c08_pay = df_payment(self.player.df6c08, 5, 7)
        self.player.df6c09_pay = df_payment(self.player.df6c09, 5, 8)
        self.player.df6c10_pay = df_payment(self.player.df6c10, 5, 9)

        self.player.payoff = self.player.df_pay + self.player.risk_P1_pay

        return


class Instructions_Lottery(Page):
    pass

class Instructions_DF(Page):
    pass

class ResultsWaitPage(WaitPage):

    def after_all_Players_arrive(self):
        for p in self.get_players():
            p.calc_payoff()
        return

class Results(Page):
    pass

class Wait_aft_S(WaitPage):
    wait_for_all_players = True
    title_text = "Спасибо за выполнение Части 1, ожидайте, пока остальные участники закончат"
    body_text = "После того, как все участники закончат задание, мы приступим к следующей части эксперимента"

class Instr_aft_S(Page):
    pass

class Wait_aft_P1_res(WaitPage):
    wait_for_all_players = True
    title_text = "Спасибо за выполнение Части 2, ожидайте, пока остальные участники закончат"
    body_text = "После того, как все участники закончат задание, мы приступим к следующей части эксперимента"

class Instr_aft_P1_res(Page):
    pass

class Wait_aft_Res(WaitPage):
    wait_for_all_players = True
    title_text = "Спасибо за выполнение Части 3, ожидайте, пока остальные участники закончат"
    body_text = "После того, как все участники закончат задание, мы приступим к следующей части эксперимента"

class Instr_aft_Res(Page):
    pass

page_sequence = [Instr_aft_S,
                 Lottery_risk_P1, Lottery_risk_P1_res, Wait_aft_P1_res, Instr_aft_P1_res,
                 Discount_M2, Discount_M3, Discount_M4, Discount_M5, Discount_M6,
                 Wait_aft_Res, Instr_aft_Res]
