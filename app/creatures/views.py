from rest_framework import viewsets
from creatures.models import Creature, Class, Classification, Expansion, Level, Faction, School, DispelType, Ability
from creatures.serializers import CreatureSerializer, ClassSerializer, ClassificationSerializer, ExpansionSerializer, LevelSerializer, FactionSerializer, SchoolSerializer, DispelTypeSerializer, AbilitySerializer

class ClassViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Class instances.
    """
    serializer_class = ClassSerializer
    queryset = Class.objects.all()
    lookup_field = 'id'
    pagination_class = None


class CreatureViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing creature instances.
    """
    serializer_class = CreatureSerializer
    queryset = Creature.objects.all()
    lookup_field = 'id'
    pagination_class = None
