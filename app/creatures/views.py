"""
 * Author: Connor Pandolph
 * Project: Creatures
 * API: REST
 * Framework: Django
 * Container: Docker
 * Date: 2022
"""

from rest_framework import viewsets
from creatures.models import Class, Classification, Expansion, Level, Faction, School, DispelType, Ability, Creature
from creatures.serializers import ClassSerializer, ClassificationSerializer, ExpansionSerializer, LevelSerializer, FactionSerializer, SchoolSerializer, DispelTypeSerializer, AbilitySerializer, CreatureSerializer

#Viewsets for viewing and editing Class instances
class ClassViewSet(viewsets.ModelViewSet):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()
    lookup_field = 'name'
    pagination_class = None

class ClassificationViewSet(viewsets.ModelViewSet):
    serializer_class = ClassificationSerializer
    queryset = Classification.objects.all()
    lookup_field = 'name'
    pagination_class = None

class ExpansionViewSet(viewsets.ModelViewSet):
    serializer_class = ExpansionSerializer
    queryset = Expansion.objects.all()
    lookup_field = 'name'
    pagination_class = None

class LevelViewSet(viewsets.ModelViewSet):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()
    lookup_field = 'number'
    pagination_class = None

class FactionViewSet(viewsets.ModelViewSet):
    serializer_class = FactionSerializer
    queryset = Faction.objects.all()
    lookup_field = 'name'
    pagination_class = None

class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    lookup_field = 'name'
    pagination_class = None

class DispelTypeViewSet(viewsets.ModelViewSet):
    serializer_class = DispelTypeSerializer
    queryset = DispelType.objects.all()
    lookup_field = 'name'
    pagination_class = None

class AbilityViewSet(viewsets.ModelViewSet):
    serializer_class = AbilitySerializer
    queryset = Ability.objects.all()
    lookup_field = 'ability_id'
    pagination_class = None

class CreatureViewSet(viewsets.ModelViewSet):
    serializer_class = CreatureSerializer
    queryset = Creature.objects.all()
    lookup_field = 'name'
    pagination_class = None