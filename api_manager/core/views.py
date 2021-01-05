from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import CreatorrSerializer, AbilitySerializer, CharacterSerializer
from .models import Creator, Ability, Character
from .producer import publish

from django.views.generic import ListView

class CharacterListView(ListView):
    model = Character
    template_name = 'index.html'
    context_object_name = 'characters'


class CreatorViewSet(viewsets.ModelViewSet):
    queryset = Creator.objects.all().order_by('name')
    serializer_class = CreatorrSerializer
    http_method_names = ['get']


class AbilityViewSet(viewsets.ModelViewSet):
    queryset = Ability.objects.all().order_by('ability')
    serializer_class = AbilitySerializer
    http_method_names = ['get']


class CharacterViewSet(viewsets.ViewSet):
    def list(self, request):
        characters = Character.objects.all().order_by('name')
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)

    # CREATE NEW Character VIA API - POST
    def create(self, request):
        """
        Ex POST:{
                "name": "MySuperHero5",
                "series": "DC",
                "team": "JL",
                "origin": "India",
                "ability": [
                    {
                        "ability": "speed"
                    }
                ],
                "creator": {
                    "name": "Jack Kirby", 
                    "country": "US"
                }
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
        
        publish('character_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        character = Character.objects.get(id=pk)
        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    def update(self, request, pk=None):
        character = Character.objects.get(id=pk)
        serializer = CharacterSerializer(instance=character, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('character_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # DELETE Character VIA API - DELETE
    def destroy(self, request, pk=None):
        character = Character.objects.get(id=pk)
        character.delete()
        publish('character_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)