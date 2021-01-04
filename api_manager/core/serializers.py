from django.shortcuts import get_object_or_404

from rest_framework import serializers

from .models import Creator, Ability, Character

class CreatorrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = "__all__"
        depth = 1

class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = "__all__"

class CharacterSerializer(serializers.ModelSerializer):
    ability = AbilitySerializer(many=True)
    creator = CreatorrSerializer(many=False)
    class Meta:
        model = Character
        fields = "__all__"
        depth = 2

    def update(self, instance, validated_data):
        """
        EX PUT:{
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
        instance.name = validated_data.get('name', instance.name)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.series = validated_data.get('series', instance.series)
        instance.team = validated_data.get('team', instance.team)
        instance.origin = validated_data.get('origin', instance.origin)
        instance.is_villan = validated_data.get('is_villan', instance.is_villan)

        # Nested Objects
        if "creator" in validated_data:
            creator = get_object_or_404(
                Creator, 
                name=validated_data['creator']['name'], 
                country=validated_data['creator']['country']
                )
            instance.creator = creator

        if "ability" in validated_data:
            for ability in validated_data.pop('ability'):
                ability = get_object_or_404(Ability, ability=ability['ability'], level=10)
                instance.ability.add(ability)        

        instance.save()

        return instance