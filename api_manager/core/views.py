from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CreatorrSerializer, AbilitySerializer, CharacterSerializer
from .models import Creator, Ability, Character

from pprint import pprint

class CreatorViewSet(viewsets.ModelViewSet):
    queryset = Creator.objects.all().order_by('name')
    serializer_class = CreatorrSerializer
    http_method_names = ['get']

class AbilityViewSet(viewsets.ModelViewSet):
    queryset = Ability.objects.all().order_by('ability')
    serializer_class = AbilitySerializer
    http_method_names = ['get']

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().order_by('name')
    serializer_class = CharacterSerializer
    http_method_names = ['get', 'put', 'post', 'delete']

    # CREATE NEW Character VIA API - POST
    def create(self, request, *args, **kwargs):
        """
        Ex POST:{
            "name": "MySuperHero",
            "series": "DC",
            "team": "JL",
            "origin": "India",
            "ability": ["strength", "Good"],
            "creator": "Stan Lee"
        }
        """
        character = request.data

        if "ability" in character:
            ability_list = []
            for ab in character.pop('ability'):
                ability, _ = Ability.objects.get_or_create(ability=ab, level=10)
                ability_list.append(ability)

        if "creator" in character:
            creator, _ = Creator.objects.get_or_create(name=character['creator'])
            character['creator'] = creator

        new_character = Character.objects.create(**character)
        for ab in ability_list:
            new_character.ability.add(ab)
        new_character.save()        

        serializer = CharacterSerializer(new_character)
        return Response(serializer.data)