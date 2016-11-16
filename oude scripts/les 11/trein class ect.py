__author__ = 'alexander'
import datetime

class Train():

    unique_nummer=0

    def __init__(self, kleur, nummer, snelheid, passagiers, bouwjaar=2010):
        self.kleur          = kleur
        self.nummer         = Train.unique_nummer
        self.snelheid       = snelheid
        self.passagiers     = passagiers
        self.bouwjaar       = bouwjaar
        Train.unique_nummer += 1
    def