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
    name_in_url = 'test_1'
    players_per_group = 6
    num_rounds = 7

    region_coef_0 = 0.8
    region_coef_1 = 1
    region_coef_2 = 1.2



    compensation = [1,1.4,2,3,3.6,4]
    thresholds = [-1,20,40,60,80,100,1000]
    ecu_rate = c(3)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):

    in_coalition_out = models.CharField()
    # in_coalition_inner = models.CharField()
    in_coalition_counter = models.IntegerField()


    def is_in_coalition(self):

        self.in_coalition_out = ""
        # self.in_coalition_inner = []

        in_coalition_inner = []
        for plr in self.get_players():
            if plr.coalition_marker:
                self.in_coalition_out += str(plr.id_in_group)
                self.in_coalition_out += " и "
                # self.in_coalition_inner.append(plr.id_in_group)
                in_coalition_inner.append(plr.id_in_group)

        # if len(self.in_coalition_inner) > 1:
        if len(in_coalition_inner) > 1:
            self.in_coalition_out = self.in_coalition_out[:-3] + " в коалиции"
        else:
            # if len(self.in_coalition_inner) > 0:
            if len(in_coalition_inner) > 0:
                # self.get_player_by_id(int(self.in_coalition_inner[0])).coalition_marker = False
                self.get_player_by_id(int(in_coalition_inner[0])).coalition_marker = False
                self.in_coalition_out = "В коалиции никого нет"
            else:
                self.in_coalition_out = "В коалиции никого нет"

        self.in_coalition_counter = len(in_coalition_inner)



    slider_position_1 = models.PositiveIntegerField()
    slider_position_2 = models.PositiveIntegerField()
    slider_position_3 = models.PositiveIntegerField()
    slider_position_4 = models.PositiveIntegerField()
    slider_position_5 = models.PositiveIntegerField()
    slider_position_6 = models.PositiveIntegerField()
    slider_position_7 = models.PositiveIntegerField()
    slider_position_8 = models.PositiveIntegerField()
    slider_position_9 = models.PositiveIntegerField()
    slider_position_10 = models.PositiveIntegerField()
    slider_position_11 = models.PositiveIntegerField()
    slider_position_12 = models.PositiveIntegerField()
    slider_position_13 = models.PositiveIntegerField()
    slider_position_14 = models.PositiveIntegerField()
    slider_position_15 = models.PositiveIntegerField()
    slider_position_16 = models.PositiveIntegerField()
    slider_position_17 = models.PositiveIntegerField()
    slider_position_18 = models.PositiveIntegerField()
    slider_position_19 = models.PositiveIntegerField()
    slider_position_20 = models.PositiveIntegerField()
    slider_position_21 = models.PositiveIntegerField()
    slider_position_22 = models.PositiveIntegerField()
    slider_position_23 = models.PositiveIntegerField()
    slider_position_24 = models.PositiveIntegerField()
    slider_position_25 = models.PositiveIntegerField()
    slider_position_26 = models.PositiveIntegerField()
    slider_position_27 = models.PositiveIntegerField()
    slider_position_28 = models.PositiveIntegerField()
    slider_position_29 = models.PositiveIntegerField()
    slider_position_30 = models.PositiveIntegerField()

    def slider_randomisation(self):
            self.slider_position_1 = random.randint(1,100)
            self.slider_position_2 = random.randint(1,100)
            self.slider_position_3 = random.randint(1,100)
            self.slider_position_4 = random.randint(1,100)
            self.slider_position_5 = random.randint(1,100)
            self.slider_position_6 = random.randint(1,100)
            self.slider_position_7 = random.randint(1,100)
            self.slider_position_8 = random.randint(1,100)
            self.slider_position_9 = random.randint(1,100)
            self.slider_position_10 = random.randint(1,100)
            self.slider_position_11 = random.randint(1, 100)
            self.slider_position_12 = random.randint(1, 100)
            self.slider_position_13 = random.randint(1, 100)
            self.slider_position_14 = random.randint(1, 100)
            self.slider_position_15 = random.randint(1, 100)
            self.slider_position_16 = random.randint(1, 100)
            self.slider_position_17 = random.randint(1, 100)
            self.slider_position_18 = random.randint(1, 100)
            self.slider_position_19 = random.randint(1, 100)
            self.slider_position_20 = random.randint(1, 100)
            self.slider_position_21 = random.randint(1, 100)
            self.slider_position_22 = random.randint(1, 100)
            self.slider_position_23 = random.randint(1, 100)
            self.slider_position_24 = random.randint(1, 100)
            self.slider_position_25 = random.randint(1, 100)
            self.slider_position_26 = random.randint(1, 100)
            self.slider_position_27 = random.randint(1, 100)
            self.slider_position_28 = random.randint(1, 100)
            self.slider_position_29 = random.randint(1, 100)
            self.slider_position_30 = random.randint(1, 100)


    def set_sliders(self):
        for plr in self.get_players():
            plr.num_of_sliders = 0
            if plr.slider_1 == self.slider_position_1:
                plr.num_of_sliders += 1

            if plr.slider_2 == self.slider_position_2:
                plr.num_of_sliders += 1

            if plr.slider_3 == self.slider_position_3:
                plr.num_of_sliders += 1

            if plr.slider_4 == self.slider_position_4:
                plr.num_of_sliders += 1

            if plr.slider_5 == self.slider_position_5:
                plr.num_of_sliders += 1

            if plr.slider_6 == self.slider_position_6:
                plr.num_of_sliders += 1

            if plr.slider_7 == self.slider_position_7:
                plr.num_of_sliders += 1

            if plr.slider_8 == self.slider_position_8:
                plr.num_of_sliders += 1

            if plr.slider_9 == self.slider_position_9:
                plr.num_of_sliders += 1

            if plr.slider_10 == self.slider_position_10:
                plr.num_of_sliders += 1

            if plr.slider_11 == self.slider_position_11:
                plr.num_of_sliders += 1

            if plr.slider_12 == self.slider_position_12:
                plr.num_of_sliders += 1

            if plr.slider_13 == self.slider_position_13:
                plr.num_of_sliders += 1

            if plr.slider_14 == self.slider_position_14:
                plr.num_of_sliders += 1

            if plr.slider_15 == self.slider_position_15:
                plr.num_of_sliders += 1

            if plr.slider_16 == self.slider_position_16:
                plr.num_of_sliders += 1

            if plr.slider_17 == self.slider_position_17:
                plr.num_of_sliders += 1

            if plr.slider_18 == self.slider_position_18:
                plr.num_of_sliders += 1

            if plr.slider_19 == self.slider_position_19:
                plr.num_of_sliders += 1

            if plr.slider_20 == self.slider_position_20:
                plr.num_of_sliders += 1

            if plr.slider_21 == self.slider_position_21:
                plr.num_of_sliders += 1

            if plr.slider_22 == self.slider_position_22:
                plr.num_of_sliders += 1

            if plr.slider_23 == self.slider_position_23:
                plr.num_of_sliders += 1


            if plr.slider_24 == self.slider_position_24:
                plr.num_of_sliders += 1

            if plr.slider_25 == self.slider_position_25:
                plr.num_of_sliders += 1

            if plr.slider_26 == self.slider_position_26:
                plr.num_of_sliders += 1

            if plr.slider_27 == self.slider_position_27:
                plr.num_of_sliders += 1

            if plr.slider_28 == self.slider_position_28:
                plr.num_of_sliders += 1

            if plr.slider_29 == self.slider_position_29:
                plr.num_of_sliders += 1

            if plr.slider_30 == self.slider_position_30:
                plr.num_of_sliders += 1

    def performance(self):
        for plr in self.get_players():
            if plr.role() == "High region":
                plr.plr_perf = round(plr.num_of_sliders*Constants.region_coef_2,2)
            if plr.role() == "Low region":
                plr.plr_perf = round(plr.num_of_sliders * Constants.region_coef_0, 2)



    coal_payoff = models.FloatField()

    def payoff_for_coalition(self):

        coal_perf = 0
        counter = 0

        for plr in self.get_players():
            if plr.coalition_marker:
                counter += 1
                coal_perf += plr.plr_perf

        for i in range(len(Constants.compensation)):
            if (Constants.thresholds[i] < coal_perf and coal_perf <= Constants.thresholds[i+1]):
                self.coal_payoff = coal_perf*Constants.compensation[i]

        for plr in self.get_players():
            if plr.coalition_marker:
                plr.plr_payoff = round(self.coal_payoff/counter,2)

    def payoff_for_non_coalition(self):

        for plr in self.get_players():
            if plr.coalition_marker == False:
                for i in range(len(Constants.compensation)):
                    if (Constants.thresholds[i] < plr.plr_perf and plr.plr_perf <= Constants.thresholds[i + 1]):
                        plr.plr_payoff = round(plr.plr_perf * Constants.compensation[i],2)

    def payoff_for_0_round(self):
        for plr in self.get_players():
            for i in range(len(Constants.compensation)):
                if (Constants.thresholds[i] < plr.plr_perf and plr.plr_perf <= Constants.thresholds[i + 1]):
                    plr.plr_payoff = round(plr.plr_perf * Constants.compensation[i],2)

    plr_1_perf_round_0 = models.FloatField()
    plr_1_perf_round_1 = models.FloatField()
    plr_1_perf_round_2 = models.FloatField()
    plr_1_perf_round_3 = models.FloatField()
    plr_1_perf_round_4 = models.FloatField()
    plr_1_perf_round_5 = models.FloatField()
    plr_1_perf_round_6 = models.FloatField()

    plr_2_perf_round_0 = models.FloatField()
    plr_2_perf_round_1 = models.FloatField()
    plr_2_perf_round_2 = models.FloatField()
    plr_2_perf_round_3 = models.FloatField()
    plr_2_perf_round_4 = models.FloatField()
    plr_2_perf_round_5 = models.FloatField()
    plr_2_perf_round_6 = models.FloatField()

    plr_3_perf_round_0 = models.FloatField()
    plr_3_perf_round_1 = models.FloatField()
    plr_3_perf_round_2 = models.FloatField()
    plr_3_perf_round_3 = models.FloatField()
    plr_3_perf_round_4 = models.FloatField()
    plr_3_perf_round_5 = models.FloatField()
    plr_3_perf_round_6 = models.FloatField()

    plr_4_perf_round_0 = models.FloatField()
    plr_4_perf_round_1 = models.FloatField()
    plr_4_perf_round_2 = models.FloatField()
    plr_4_perf_round_3 = models.FloatField()
    plr_4_perf_round_4 = models.FloatField()
    plr_4_perf_round_5 = models.FloatField()
    plr_4_perf_round_6 = models.FloatField()

    plr_5_perf_round_0 = models.FloatField()
    plr_5_perf_round_1 = models.FloatField()
    plr_5_perf_round_2 = models.FloatField()
    plr_5_perf_round_3 = models.FloatField()
    plr_5_perf_round_4 = models.FloatField()
    plr_5_perf_round_5 = models.FloatField()
    plr_5_perf_round_6 = models.FloatField()

    plr_6_perf_round_0 = models.FloatField()
    plr_6_perf_round_1 = models.FloatField()
    plr_6_perf_round_2 = models.FloatField()
    plr_6_perf_round_3 = models.FloatField()
    plr_6_perf_round_4 = models.FloatField()
    plr_6_perf_round_5 = models.FloatField()
    plr_6_perf_round_6 = models.FloatField()

    def table_with_perf(self):

        self.plr_1_perf_round_0 = self.get_player_by_id(1).in_round(1).plr_perf

        self.plr_1_perf_round_1 = self.get_player_by_id(1).in_round(2).plr_perf
        if self.plr_1_perf_round_1 is None:
            self.plr_1_perf_round_1 = 0

        self.plr_1_perf_round_2 = self.get_player_by_id(1).in_round(3).plr_perf
        if self.plr_1_perf_round_2 is None:
            self.plr_1_perf_round_2 = 0

        self.plr_1_perf_round_3 = self.get_player_by_id(1).in_round(4).plr_perf
        if self.plr_1_perf_round_3 is None:
            self.plr_1_perf_round_3 = 0

        self.plr_1_perf_round_4 = self.get_player_by_id(1).in_round(5).plr_perf
        if self.plr_1_perf_round_4 is None:
            self.plr_1_perf_round_4 = 0

        self.plr_1_perf_round_5 = self.get_player_by_id(1).in_round(6).plr_perf
        if self.plr_1_perf_round_5 is None:
            self.plr_1_perf_round_5 = 0

        self.plr_1_perf_round_6 = self.get_player_by_id(1).in_round(7).plr_perf
        if self.plr_1_perf_round_6 is None:
            self.plr_1_perf_round_6 = 0

        self.plr_2_perf_round_0 = self.get_player_by_id(2).in_round(1).plr_perf

        self.plr_2_perf_round_1 = self.get_player_by_id(2).in_round(2).plr_perf
        if self.plr_2_perf_round_1 is None:
            self.plr_2_perf_round_1 = 0

        self.plr_2_perf_round_2 = self.get_player_by_id(2).in_round(3).plr_perf
        if self.plr_2_perf_round_2 is None:
            self.plr_2_perf_round_2 = 0

        self.plr_2_perf_round_3 = self.get_player_by_id(2).in_round(4).plr_perf
        if self.plr_2_perf_round_3 is None:
            self.plr_2_perf_round_3 = 0

        self.plr_2_perf_round_4 = self.get_player_by_id(2).in_round(5).plr_perf
        if self.plr_2_perf_round_4 is None:
            self.plr_2_perf_round_4 = 0

        self.plr_2_perf_round_5 = self.get_player_by_id(2).in_round(6).plr_perf
        if self.plr_2_perf_round_5 is None:
            self.plr_2_perf_round_5 = 0

        self.plr_2_perf_round_6 = self.get_player_by_id(2).in_round(7).plr_perf
        if self.plr_2_perf_round_6 is None:
            self.plr_2_perf_round_6 = 0

        self.plr_3_perf_round_0 = self.get_player_by_id(3).in_round(1).plr_perf

        self.plr_3_perf_round_1 = self.get_player_by_id(3).in_round(2).plr_perf
        if self.plr_3_perf_round_1 is None:
            self.plr_3_perf_round_1 = 0

        self.plr_3_perf_round_2 = self.get_player_by_id(3).in_round(3).plr_perf
        if self.plr_3_perf_round_2 is None:
            self.plr_3_perf_round_2 = 0

        self.plr_3_perf_round_3 = self.get_player_by_id(3).in_round(4).plr_perf
        if self.plr_3_perf_round_3 is None:
            self.plr_3_perf_round_3 = 0

        self.plr_3_perf_round_4 = self.get_player_by_id(3).in_round(5).plr_perf
        if self.plr_3_perf_round_4 is None:
            self.plr_3_perf_round_4 = 0

        self.plr_3_perf_round_5 = self.get_player_by_id(3).in_round(6).plr_perf
        if self.plr_3_perf_round_5 is None:
            self.plr_3_perf_round_5 = 0

        self.plr_3_perf_round_6 = self.get_player_by_id(3).in_round(7).plr_perf
        if self.plr_3_perf_round_6 is None:
            self.plr_3_perf_round_6 = 0

        self.plr_4_perf_round_0 = self.get_player_by_id(4).in_round(1).plr_perf

        self.plr_4_perf_round_1 = self.get_player_by_id(4).in_round(2).plr_perf
        if self.plr_4_perf_round_1 is None:
            self.plr_4_perf_round_1 = 0

        self.plr_4_perf_round_2 = self.get_player_by_id(4).in_round(3).plr_perf
        if self.plr_4_perf_round_2 is None:
            self.plr_4_perf_round_2 = 0

        self.plr_4_perf_round_3 = self.get_player_by_id(4).in_round(4).plr_perf
        if self.plr_4_perf_round_3 is None:
            self.plr_4_perf_round_3 = 0

        self.plr_4_perf_round_4 = self.get_player_by_id(4).in_round(5).plr_perf
        if self.plr_4_perf_round_4 is None:
            self.plr_4_perf_round_4 = 0

        self.plr_4_perf_round_5 = self.get_player_by_id(4).in_round(6).plr_perf
        if self.plr_4_perf_round_5 is None:
            self.plr_4_perf_round_5 = 0

        self.plr_4_perf_round_6 = self.get_player_by_id(4).in_round(7).plr_perf
        if self.plr_4_perf_round_6 is None:
            self.plr_4_perf_round_6 = 0

        self.plr_5_perf_round_0 = self.get_player_by_id(5).in_round(1).plr_perf

        self.plr_5_perf_round_1 = self.get_player_by_id(5).in_round(2).plr_perf
        if self.plr_5_perf_round_1 is None:
            self.plr_5_perf_round_1 = 0

        self.plr_5_perf_round_2 = self.get_player_by_id(5).in_round(3).plr_perf
        if self.plr_5_perf_round_2 is None:
            self.plr_5_perf_round_2 = 0

        self.plr_5_perf_round_3 = self.get_player_by_id(5).in_round(4).plr_perf
        if self.plr_5_perf_round_3 is None:
            self.plr_5_perf_round_3 = 0

        self.plr_5_perf_round_4 = self.get_player_by_id(5).in_round(5).plr_perf
        if self.plr_5_perf_round_4 is None:
            self.plr_5_perf_round_4 = 0

        self.plr_5_perf_round_5 = self.get_player_by_id(5).in_round(6).plr_perf
        if self.plr_5_perf_round_5 is None:
            self.plr_5_perf_round_5 = 0

        self.plr_5_perf_round_6 = self.get_player_by_id(5).in_round(7).plr_perf
        if self.plr_5_perf_round_6 is None:
            self.plr_5_perf_round_6 = 0

        self.plr_6_perf_round_0 = self.get_player_by_id(6).in_round(1).plr_perf

        self.plr_6_perf_round_1 = self.get_player_by_id(6).in_round(2).plr_perf
        if self.plr_6_perf_round_1 is None:
            self.plr_6_perf_round_1 = 0

        self.plr_6_perf_round_2 = self.get_player_by_id(6).in_round(3).plr_perf
        if self.plr_6_perf_round_2 is None:
            self.plr_6_perf_round_2 = 0

        self.plr_6_perf_round_3 = self.get_player_by_id(6).in_round(4).plr_perf
        if self.plr_6_perf_round_3 is None:
            self.plr_6_perf_round_3 = 0

        self.plr_6_perf_round_4 = self.get_player_by_id(6).in_round(5).plr_perf
        if self.plr_6_perf_round_4 is None:
            self.plr_6_perf_round_4 = 0

        self.plr_6_perf_round_5 = self.get_player_by_id(6).in_round(6).plr_perf
        if self.plr_6_perf_round_5 is None:
            self.plr_6_perf_round_5 = 0

        self.plr_6_perf_round_6 = self.get_player_by_id(6).in_round(7).plr_perf
        if self.plr_6_perf_round_6 is None:
            self.plr_6_perf_round_6 = 0


    plr_1_payoff_round_0 = models.FloatField()
    plr_1_payoff_round_1 = models.FloatField()
    plr_1_payoff_round_2 = models.FloatField()
    plr_1_payoff_round_3 = models.FloatField()
    plr_1_payoff_round_4 = models.FloatField()
    plr_1_payoff_round_5 = models.FloatField()
    plr_1_payoff_round_6 = models.FloatField()

    plr_2_payoff_round_0 = models.FloatField()
    plr_2_payoff_round_1 = models.FloatField()
    plr_2_payoff_round_2 = models.FloatField()
    plr_2_payoff_round_3 = models.FloatField()
    plr_2_payoff_round_4 = models.FloatField()
    plr_2_payoff_round_5 = models.FloatField()
    plr_2_payoff_round_6 = models.FloatField()

    plr_3_payoff_round_0 = models.FloatField()
    plr_3_payoff_round_1 = models.FloatField()
    plr_3_payoff_round_2 = models.FloatField()
    plr_3_payoff_round_3 = models.FloatField()
    plr_3_payoff_round_4 = models.FloatField()
    plr_3_payoff_round_5 = models.FloatField()
    plr_3_payoff_round_6 = models.FloatField()

    plr_4_payoff_round_0 = models.FloatField()
    plr_4_payoff_round_1 = models.FloatField()
    plr_4_payoff_round_2 = models.FloatField()
    plr_4_payoff_round_3 = models.FloatField()
    plr_4_payoff_round_4 = models.FloatField()
    plr_4_payoff_round_5 = models.FloatField()
    plr_4_payoff_round_6 = models.FloatField()

    plr_5_payoff_round_0 = models.FloatField()
    plr_5_payoff_round_1 = models.FloatField()
    plr_5_payoff_round_2 = models.FloatField()
    plr_5_payoff_round_3 = models.FloatField()
    plr_5_payoff_round_4 = models.FloatField()
    plr_5_payoff_round_5 = models.FloatField()
    plr_5_payoff_round_6 = models.FloatField()

    plr_6_payoff_round_0 = models.FloatField()
    plr_6_payoff_round_1 = models.FloatField()
    plr_6_payoff_round_2 = models.FloatField()
    plr_6_payoff_round_3 = models.FloatField()
    plr_6_payoff_round_4 = models.FloatField()
    plr_6_payoff_round_5 = models.FloatField()
    plr_6_payoff_round_6 = models.FloatField()

    def table_with_payoff(self):

        self.plr_1_payoff_round_0 = self.get_player_by_id(1).in_round(1).plr_payoff

        self.plr_1_payoff_round_1 = self.get_player_by_id(1).in_round(2).plr_payoff
        if self.plr_1_payoff_round_1 is None:
            self.plr_1_payoff_round_1 = 0

        self.plr_1_payoff_round_2 = self.get_player_by_id(1).in_round(3).plr_payoff
        if self.plr_1_payoff_round_2 is None:
            self.plr_1_payoff_round_2 = 0

        self.plr_1_payoff_round_3 = self.get_player_by_id(1).in_round(4).plr_payoff
        if self.plr_1_payoff_round_3 is None:
            self.plr_1_payoff_round_3 = 0

        self.plr_1_payoff_round_4 = self.get_player_by_id(1).in_round(5).plr_payoff
        if self.plr_1_payoff_round_4 is None:
            self.plr_1_payoff_round_4 = 0

        self.plr_1_payoff_round_5 = self.get_player_by_id(1).in_round(6).plr_payoff
        if self.plr_1_payoff_round_5 is None:
            self.plr_1_payoff_round_5 = 0

        self.plr_1_payoff_round_6 = self.get_player_by_id(1).in_round(7).plr_payoff
        if self.plr_1_payoff_round_6 is None:
            self.plr_1_payoff_round_6 = 0

        self.plr_2_payoff_round_0 = self.get_player_by_id(2).in_round(1).plr_payoff

        self.plr_2_payoff_round_1 = self.get_player_by_id(2).in_round(2).plr_payoff
        if self.plr_2_payoff_round_1 is None:
            self.plr_2_payoff_round_1 = 0

        self.plr_2_payoff_round_2 = self.get_player_by_id(2).in_round(3).plr_payoff
        if self.plr_2_payoff_round_2 is None:
            self.plr_2_payoff_round_2 = 0

        self.plr_2_payoff_round_3 = self.get_player_by_id(2).in_round(4).plr_payoff
        if self.plr_2_payoff_round_3 is None:
            self.plr_2_payoff_round_3 = 0

        self.plr_2_payoff_round_4 = self.get_player_by_id(2).in_round(5).plr_payoff
        if self.plr_2_payoff_round_4 is None:
            self.plr_2_payoff_round_4 = 0

        self.plr_2_payoff_round_5 = self.get_player_by_id(2).in_round(6).plr_payoff
        if self.plr_2_payoff_round_5 is None:
            self.plr_2_payoff_round_5 = 0

        self.plr_2_payoff_round_6 = self.get_player_by_id(2).in_round(7).plr_payoff
        if self.plr_2_payoff_round_6 is None:
            self.plr_2_payoff_round_6 = 0

        self.plr_3_payoff_round_0 = self.get_player_by_id(3).in_round(1).plr_payoff

        self.plr_3_payoff_round_1 = self.get_player_by_id(3).in_round(2).plr_payoff
        if self.plr_3_payoff_round_1 is None:
            self.plr_3_payoff_round_1 = 0

        self.plr_3_payoff_round_2 = self.get_player_by_id(3).in_round(3).plr_payoff
        if self.plr_3_payoff_round_2 is None:
            self.plr_3_payoff_round_2 = 0

        self.plr_3_payoff_round_3 = self.get_player_by_id(3).in_round(4).plr_payoff
        if self.plr_3_payoff_round_3 is None:
            self.plr_3_payoff_round_3 = 0

        self.plr_3_payoff_round_4 = self.get_player_by_id(3).in_round(5).plr_payoff
        if self.plr_3_payoff_round_4 is None:
            self.plr_3_payoff_round_4 = 0

        self.plr_3_payoff_round_5 = self.get_player_by_id(3).in_round(6).plr_payoff
        if self.plr_3_payoff_round_5 is None:
            self.plr_3_payoff_round_5 = 0

        self.plr_3_payoff_round_6 = self.get_player_by_id(3).in_round(7).plr_payoff
        if self.plr_3_payoff_round_6 is None:
            self.plr_3_payoff_round_6 = 0

        self.plr_4_payoff_round_0 = self.get_player_by_id(4).in_round(1).plr_payoff

        self.plr_4_payoff_round_1 = self.get_player_by_id(4).in_round(2).plr_payoff
        if self.plr_4_payoff_round_1 is None:
            self.plr_4_payoff_round_1 = 0

        self.plr_4_payoff_round_2 = self.get_player_by_id(4).in_round(3).plr_payoff
        if self.plr_4_payoff_round_2 is None:
            self.plr_4_payoff_round_2 = 0

        self.plr_4_payoff_round_3 = self.get_player_by_id(4).in_round(4).plr_payoff
        if self.plr_4_payoff_round_3 is None:
            self.plr_4_payoff_round_3 = 0

        self.plr_4_payoff_round_4 = self.get_player_by_id(4).in_round(5).plr_payoff
        if self.plr_4_payoff_round_4 is None:
            self.plr_4_payoff_round_4 = 0

        self.plr_4_payoff_round_5 = self.get_player_by_id(4).in_round(6).plr_payoff
        if self.plr_4_payoff_round_5 is None:
            self.plr_4_payoff_round_5 = 0

        self.plr_4_payoff_round_6 = self.get_player_by_id(4).in_round(7).plr_payoff
        if self.plr_4_payoff_round_6 is None:
            self.plr_4_payoff_round_6 = 0

        self.plr_5_payoff_round_0 = self.get_player_by_id(5).in_round(1).plr_payoff

        self.plr_5_payoff_round_1 = self.get_player_by_id(5).in_round(2).plr_payoff
        if self.plr_5_payoff_round_1 is None:
            self.plr_5_payoff_round_1 = 0

        self.plr_5_payoff_round_2 = self.get_player_by_id(5).in_round(3).plr_payoff
        if self.plr_5_payoff_round_2 is None:
            self.plr_5_payoff_round_2 = 0

        self.plr_5_payoff_round_3 = self.get_player_by_id(5).in_round(4).plr_payoff
        if self.plr_5_payoff_round_3 is None:
            self.plr_5_payoff_round_3 = 0

        self.plr_5_payoff_round_4 = self.get_player_by_id(5).in_round(5).plr_payoff
        if self.plr_5_payoff_round_4 is None:
            self.plr_5_payoff_round_4 = 0

        self.plr_5_payoff_round_5 = self.get_player_by_id(5).in_round(6).plr_payoff
        if self.plr_5_payoff_round_5 is None:
            self.plr_5_payoff_round_5 = 0

        self.plr_5_payoff_round_6 = self.get_player_by_id(5).in_round(7).plr_payoff
        if self.plr_5_payoff_round_6 is None:
            self.plr_5_payoff_round_6 = 0

        self.plr_6_payoff_round_0 = self.get_player_by_id(6).in_round(1).plr_payoff

        self.plr_6_payoff_round_1 = self.get_player_by_id(6).in_round(2).plr_payoff
        if self.plr_6_payoff_round_1 is None:
            self.plr_6_payoff_round_1 = 0

        self.plr_6_payoff_round_2 = self.get_player_by_id(6).in_round(3).plr_payoff
        if self.plr_6_payoff_round_2 is None:
            self.plr_6_payoff_round_2 = 0

        self.plr_6_payoff_round_3 = self.get_player_by_id(6).in_round(4).plr_payoff
        if self.plr_6_payoff_round_3 is None:
            self.plr_6_payoff_round_3 = 0

        self.plr_6_payoff_round_4 = self.get_player_by_id(6).in_round(5).plr_payoff
        if self.plr_6_payoff_round_4 is None:
            self.plr_6_payoff_round_4 = 0

        self.plr_6_payoff_round_5 = self.get_player_by_id(6).in_round(6).plr_payoff
        if self.plr_6_payoff_round_5 is None:
            self.plr_6_payoff_round_5 = 0

        self.plr_6_payoff_round_6 = self.get_player_by_id(6).in_round(7).plr_payoff
        if self.plr_6_payoff_round_6 is None:
            self.plr_6_payoff_round_6 = 0






class Player(BasePlayer):

    coalition_marker = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']])

    slider_1 = models.PositiveIntegerField(
        min = 1, max=100,
        widget = widgets.SliderInput(attrs={'step': '1'})
    )
    slider_2 = models.PositiveIntegerField(
        min = 1, max=100,
        widget = widgets.SliderInput(attrs={'step': '1'})
    )
    slider_3 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_4 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_5 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_6 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_7 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_8 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_9 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_10 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_11 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_12 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_13 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_14 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_15 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_16 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_17 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_18 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_19 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_20 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_21 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_22 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_23 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_24 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_25 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_26 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_27 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_28 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_29 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )
    slider_30 = models.PositiveIntegerField(
        min=1, max=100,
        widget=widgets.SliderInput(attrs={'step': '1'})
    )

    num_of_sliders = models.IntegerField()

    plr_perf = models.FloatField()
    plr_payoff = models.FloatField()

    def role(self):
        if self.id_in_group == 1:
            return 'High region'
        if self.id_in_group == 2:
            return 'High region'
        if self.id_in_group == 3:
            return 'High region'
        if self.id_in_group == 4:
            return 'Low region'
        if self.id_in_group == 5:
            return 'Low region'
        if self.id_in_group == 6:
            return 'Low region'
