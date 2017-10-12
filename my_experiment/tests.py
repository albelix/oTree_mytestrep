from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (views.Start, {'name': 'Жора', 'age': 20, 'sex': 1, 'consumption': 500})
        yield (views.Instr_aft_S)
        yield (views.Lottery_risk_P1, {'risk01': 'A', 'risk02': 'A', 'risk03': 'A', 'risk04': 'A', 'risk05': 'A',
                                       'risk06': 'A', 'risk07': 'A', 'risk08': 'A', 'risk09': 'A', 'risk10': 'A',
                                       'risk11': 'A', 'risk12': 'A', 'risk13': 'A', 'risk14': 'A', 'risk15': 'A',
                                       'risk16': 'A', 'risk17': 'A', 'risk18': 'A', 'risk19': 'A', 'risk20': 'A'})
        yield (views.Lottery_risk_P1_res)
        yield (views.Instr_aft_P1_res)
        yield (views.Discount_M2, {'df2c01': 'A', 'df2c02': 'A', 'df2c03': 'A', 'df2c04': 'B', 'df2c05': 'B',
                                   'df2c06': 'B', 'df2c07': 'B', 'df2c08': 'B', 'df2c09': 'B', 'df2c10': 'B'})
        yield (views.Discount_M3, {'df3c01': 'A', 'df3c02': 'A', 'df3c03': 'A', 'df3c04': 'B', 'df3c05': 'B',
                                   'df3c06': 'B', 'df3c07': 'B', 'df3c08': 'B', 'df3c09': 'B', 'df3c10': 'B'})
        yield (views.Discount_M4, {'df4c01': 'A', 'df4c02': 'A', 'df4c03': 'A', 'df4c04': 'B', 'df4c05': 'B',
                                   'df4c06': 'B', 'df4c07': 'B', 'df4c08': 'B', 'df4c09': 'B', 'df4c10': 'B'})
        yield (views.Discount_M5, {'df5c01': 'A', 'df5c02': 'A', 'df5c03': 'A', 'df5c04': 'B', 'df5c05': 'B',
                                   'df5c06': 'B', 'df5c07': 'B', 'df5c08': 'B', 'df5c09': 'B', 'df5c10': 'B'})
        yield (views.Discount_M6, {'df6c01': 'A', 'df6c02': 'A', 'df6c03': 'A', 'df6c04': 'B', 'df6c05': 'B',
                                   'df6c06': 'B', 'df6c07': 'B', 'df6c08': 'B', 'df6c09': 'B', 'df6c10': 'B'})
        yield (views.Results)
        yield (views.Instr_aft_Res)


