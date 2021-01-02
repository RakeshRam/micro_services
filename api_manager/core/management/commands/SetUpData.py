from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

import os
import json
import pprint
import random

from core.models import Creator, Ability, Character

# python manage.py SetUpData
class Command(BaseCommand):
    help = 'Creates Data in DB'

    def add_arguments(self, parser):
        # Optional argument
        parser.add_argument('-su', '--superuser', type=str, help='Create super user[y/n]', )

    def handle(self, *args, **kwargs):
        if kwargs.get('superuser') != "n":
            self.stdout.write("Creating SuperUser")
            user = User.objects.create_user('admin', password='admin')
            user.is_superuser=True
            user.is_staff=True
            user.save()
            self.stdout.write("Done - Creating SuperUser")

        # https://akabab.github.io/superhero-api/api/
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "all.json")
        
        # Creator
        creator_list = list(Creator.objects.all())
        print(creator_list)
        if not creator_list:
            self.stdout.write("Creating Creators")
            for c in ["Joe Simon", "Jack Kirby", "Stan Lee"]:
                creator = Creator(**{"name": c, "country": "US","is_retired": False})
                creator.save()
                creator_list.append(creator)
            self.stdout.write("Done - Creating Creators")

        with open(file_path) as dataFile:
            datas = json.load(dataFile)[:10]
            
            self.stdout.write("Creating Characters")
            for data in datas:
                character, _ = Character.objects.get_or_create(
                    name = data["name"], 
                    first_name = data["biography"]['fullName'],
                    last_name = "-",
                    series = data["biography"]['publisher'],
                    team = data["connections"]['groupAffiliation'][:50],
                    origin = data["biography"]['placeOfBirth'],
                    creator = random.choice(creator_list)
                    )
                character.save()
                for pw in data['powerstats']:
                    ability, _ = Ability.objects.get_or_create(ability=pw, level=10)
                    character.ability.add(ability)
                character.save()
            self.stdout.write("Done - Creating Characters")
                