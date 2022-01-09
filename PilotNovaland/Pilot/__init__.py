from otree.api import *
import random

from otree.models import player


class C(BaseConstants):
    NAME_IN_URL = 'Novaland'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number = models.IntegerField()
    showTreatmentgroup = models.StringField()
    name = models.StringField(label="Wie lautet ihr Name?", )
    age = models.IntegerField(label='Wie alt sind sie?', min=13, max=125)
    gender = models.StringField(
        choices=[['Männlich', 'Männlich'], ['Weiblich', 'Weiblich'], ['Diverse', 'Diverse'],
                 ['Keine Angabe', 'Keine Angabe'],
                 ],
        label='Welchem Geschlecht fühlen sie sich zugehörig?',
        widget=widgets.RadioSelect,
    )
    is_student = models.StringField(
        choices=[['Ja', 'Ja'], ['Nein', 'Nein']],
        label='Studieren Sie?',
        widget=widgets.RadioSelect,
    )
    SurveyFrage1 = models.IntegerField(
        label="SurveyFrage1"
    )
    SurveyFrage2 = models.IntegerField(
        label="SurveyFrage2"
    )
    SurveyFrage3 = models.IntegerField(
        label="SurveyFrage3"
    )

    SurveyFrage4 = models.IntegerField(
        label="SurveyFrage4"
    )
    SurveyFrage5 = models.IntegerField(
        label="SurveyFrage5"
    )
    SurveyFrage6 = models.IntegerField(
        label="SurveyFrage6"
    )


# FUNCTIONS
# PAGES
class Start(Page):
    pass


class UserDaten(Page):
    form_model = 'player'
    form_fields = ['name', 'age', 'gender', 'is_student']


class SurveyFragen(Page):
    player.number = random.randint(1, 3)
    form_model = 'player'
    if player.number == 1:
        form_fields = ['SurveyFrage1', 'SurveyFrage2', 'SurveyFrage3']
    elif player.number >= 2:
        form_fields = ['SurveyFrage4', 'SurveyFrage5', 'SurveyFrage6']


class TreatmentGruppe(Page):
    TreatmentGruppe1 = "Deutschland"
    TreatmentGruppe2 = "Österreicht"
    TreatmentGruppe3 = "Dänemark"
    Display_TreatmentGruppe1 = False
    Display_TreatmentGruppe2 = False
    Display_TreatmentGruppe3 = False
    player.number = random.randint(0, 3)

    def TreatmentgruppeAuswahl(self):
        if self.number == 1 and self.Display_TreatmentGruppe1 == False:
            return player.number == 4
            return self.Display_TreatmentGruppe1 == True
        elif self.number == 2 and self.Display_TreatmentGruppe1 == False:
            return self.Display_TreatmentGruppe2 == True
            return player.number == 5
            return player.number
        elif self.number == 3 and self.Display_TreatmentGruppe1 == False:
            return self.Display_TreatmentGruppe3 == True
            return number == 6
            return player.number
        else:
            number = random.randint(0, 3)

    def Show_TreatmentGruppe(self):
        if self.number == 4 and self.Display_TreatmentGruppe1 == True:
            return player.showTreatmentgroup == self.TreatmentGruppe1
            return player.treatmentGroup == self.TreatmentGruppe1
        if self.number == 5 and self.Display_TreatmentGruppe2 == True:
            return player.showTreatmentgroup == self.TreatmentGruppe2
            return player.treatmentGroup == self.TreatmentGruppe2
        if self.number == 6 and self.Display_TreatmentGruppe3 == True:
            return player.showTreatmentgroup == self.TreatmentGruppe3
            return player.treatmentGroup == self.TreatmentGruppe3

    def show_player_treatmentgruppe(self):
        if self.number == 4 and self.Display_TreatmentGruppe1 == True:
            return player.showTreatmentgroup == self.TreatmentGruppe1
        if self.number == 5 and self.Display_TreatmentGruppe2 == True:
            return player.showTreatmentgroup == self.TreatmentGruppe2
        if self.number == 6 and self.Display_TreatmentGruppe3 == True:
            return player.showTreatmentgroup == self.TreatmentGruppe3


class EndSeite(Page):
    pass


page_sequence = [Start, SurveyFragen, UserDaten, TreatmentGruppe, EndSeite]
