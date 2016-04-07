from django.db import models
import random
from django import forms


class Wallet():

    def __init__(self, request):
        self.total_gold = 0
        self.request = request
        if "total_gold" in request.session:
            self.total_gold = request.session['total_gold']

    def find_gold_in_farm(self):
        random_gold = random.randrange(10, 20)
        self.total_gold += random_gold
        self.save_in_session()

    def find_gold_in_cave(self):
        random_gold = random.randrange(5, 10)
        self.total_gold += random_gold
        self.save_in_session()

    def find_gold_in_house(self):
        random_gold = random.randrange(2, 5)
        self.total_gold += random_gold
        self.save_in_session()

    def find_gold_in_casino(self):
        random_gold = int(random.uniform(-50, 50))
        self.total_gold += random_gold
        self.save_in_session()

    def save_in_session(self):
        self.request.session['total_gold'] = self.total_gold

    def find_gold(self, location):
        if location == "farm":
            self.find_gold_in_farm()
        elif location == "cave":
            self.find_gold_in_cave()
        elif location == "house":
            self.find_gold_in_house()
        elif location == "casino":
            self.find_gold_in_casino() 


class Form(forms.Form):
    ninja = forms.CharField()
