"""
 * Author: Connor Pandolph
 * Project: Creatures
 * API: REST
 * Framework: Django
 * Container: Docker
 * Date: 2022
"""

from rest_framework.serializers import ModelSerializer
from creatures.models import Class, Classification, Expansion, Level, Faction, School, DispelType, Ability, Creature

#Serialization of models
class ClassSerializer(ModelSerializer):

    class Meta:
        model = Class
        fields = [
            'name',
            'base_health',
            'base_mana',
            'base_armor',
            'base_melee_min',
            'base_melee_max',
            'base_money',
            'base_experience',
            'base_reputation',
    ]


class ClassificationSerializer(ModelSerializer):

    class Meta:
        model = Classification
        fields = [
            'name',
            'base_health_multiplier',
            'base_mana_multiplier',
            'base_armor_multiplier',
            'base_melee_min_multiplier',
            'base_melee_max_multiplier',
            'base_money_multiplier',
            'base_experience_multiplier',
            'base_reputation_multiplier',
    ]


class ExpansionSerializer(ModelSerializer):

    class Meta:
        model = Expansion
        fields = [
            'name',
            'base_health_multiplier',
            'base_mana_multiplier',
            'base_armor_multiplier',
            'base_melee_min_multiplier',
            'base_melee_max_multiplier',
            'base_money_multiplier',
            'base_experience_multiplier',
            'base_reputation_multiplier',
    ]


class LevelSerializer(ModelSerializer):

    class Meta:
        model = Level
        fields = [
            'number',
            'base_health_multiplier',
            'base_mana_multiplier',
            'base_armor_multiplier',
            'base_melee_min_multiplier',
            'base_melee_max_multiplier',
            'base_money_multiplier',
            'base_experience_multiplier',
            'base_reputation_multiplier',
    ]


class FactionSerializer(ModelSerializer):

    class Meta:
        model = Faction
        fields = [
            'name',
    ]


class SchoolSerializer(ModelSerializer):

    class Meta:
        model = School
        fields = [
            'name',
    ]


class DispelTypeSerializer(ModelSerializer):

    class Meta:
        model = DispelType
        fields = [
            'name',
    ]


class AbilitySerializer(ModelSerializer):

    class Meta:
        model = Ability
        fields = [
            'ability_id',
            'icon_image',
            'name',
            'tooltip',
            'cost',
            'range',
            'cast_time',
            'gcd',
            'school',
            'cooldown',
            'value',
            'duration',
            'dispel_type',
    ]


class CreatureSerializer(ModelSerializer):

    classification = ClassificationSerializer()
    level = LevelSerializer()
    faction = FactionSerializer()
    creature_class = ClassSerializer()
    expansion = ExpansionSerializer()
    abilities = AbilitySerializer(many=True)

    class Meta:
        model = Creature
        fields = [
            'name',
            'model_image',
            'classification',
            'type',
            'level',
            'faction',
            'creature_class',
            'expansion',
            'abilities',
        ]

        read_only_fields = [
            'health',
            'mana',
            'armor',
            'melee_min',
            'melee_max',
            'money',
            'experience',
            'reputation',
        ]