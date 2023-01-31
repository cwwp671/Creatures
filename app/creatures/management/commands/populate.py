import os
from django.core.files import File
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from creatures.models import Class, Classification, Expansion, Level, Faction, School, DispelType, Ability, Creature

#Populates database with default data if there is no database
class Command(BaseCommand):

    def handle(self, *args, **options):

        Creature.objects.all().delete()
        Class.objects.all().delete()
        Classification.objects.all().delete()
        Expansion.objects.all().delete()
        Level.objects.all().delete()
        Faction.objects.all().delete()
        School.objects.all().delete()
        DispelType.objects.all().delete()
        Ability.objects.all().delete()

        if Creature.objects.count() == 0:

            print('Populating Database')

            self.populate_database()

        user, created = User.objects.get_or_create(
            first_name="Default",
            last_name="User",
            username="Default_User",
            email="default@default.com",
            is_active=True,
            is_staff=False)
        if created:
            user.set_password('default1234')
            user.save()

    def populate_abilities(self, ability_data):

        current_dir = os.path.dirname(os.path.realpath(__file__))
        image_dir = os.path.join(current_dir, './images/')

        try:
            ability = Ability.objects.get(ability_id=ability_data.get('ability_id'))
            return ability

        except Ability.DoesNotExist:
            ability = Ability()

            ability.ability_id = ability_data.get('ability_id')
            ability.name = ability_data.get('name')
            file_path = os.path.abspath(os.path.join(image_dir, ability_data.get('icon_image')))
            f = open(file_path, 'rb')
            ability.icon_image = File(f)

            ability.tooltip = ability_data.get('tooltip')
            ability.cost = ability_data.get('cost')
            ability.range = ability_data.get('range')
            ability.cast_time = ability_data.get('cast_time')
            ability.gcd = ability_data.get('gcd')

            school, created = School.objects.get_or_create(ability_data.get('school'))
            ability.school = school

            ability.cooldown = ability_data.get('cooldown')
            ability.value = ability_data.get('value')
            ability.duration = ability_data.get('duration')

            dispel_type, created = DispelType.objects.get_or_create(ability_data.get('dispel_type'))
            ability.dispel_type = dispel_type

            ability.save()
            return ability

    def populate_database(self):

        current_dir = os.path.dirname(os.path.realpath(__file__))
        image_dir = os.path.join(current_dir, './images/')

        classes = [
            {
                'name': 'Default Class',
                'base_health': 1,
                'base_mana': 1,
                'base_armor': 1,
                'base_melee_min': 1,
                'base_melee_max': 1,
            },
        ]

        classifications = [
            {
                'name': 'Default Classification',
                'base_health_multiplier': 1,
                'base_mana_multiplier': 1,
                'base_armor_multiplier': 1,
                'base_melee_min_multiplier': 1,
                'base_melee_max_multiplier': 1,
                'base_money_multiplier': 1,
                'base_experience_multiplier': 1,
                'base_reputation_multiplier': 1,
            },
            {
                'name': 'Default Classification 2',
                'base_health_multiplier': 1,
                'base_mana_multiplier': 1,
                'base_armor_multiplier': 1,
                'base_melee_min_multiplier': 1,
                'base_melee_max_multiplier': 1,
                'base_money_multiplier': 1,
                'base_experience_multiplier': 1,
                'base_reputation_multiplier': 1,
            },
        ]

        expansions = [
            {
                'name': 'Default Expansion',
                'base_health_multiplier': 1,
                'base_mana_multiplier': 1,
                'base_armor_multiplier': 1,
                'base_melee_min_multiplier': 1,
                'base_melee_max_multiplier': 1,
                'base_money_multiplier': 1,
                'base_experience_multiplier': 1,
            },
        ]

        levels = [
            {
                'number': 1,
                'base_health_multiplier': 1,
                'base_mana_multiplier': 1,
                'base_armor_multiplier': 1,
                'base_melee_min_multiplier': 1,
                'base_melee_max_multiplier': 1,
                'base_money_multiplier': 1,
                'base_experience_multiplier': 1,
            },
        ]

        factions = [
            {
                'name': 'Default Faction',
            },
        ]

        schools = [
            {
                'name': 'Default School',
            },
        ]

        dispeltypes = [
            {
                'name': 'Default Dispel Type',
            },
        ]

        abilities = [
            {
                'ability_id': 1,
                'icon_image': 'default_ability.jpg',
                'name': 'Default Ability',
                'tooltip': 'Default Tooltip',
                'cost': 1,
                'range': 1,
                'cast_time': 1,
                'gcd': 1,
                'school': schools[0],
                'cooldown': 1,
                'value': 1,
                'duration': 1,
                'dispel_type': dispeltypes[0],
            },
        ]

        creatures = [
            {
                'name': 'Default Creature',
                'model_image': 'default_creature.png',
                'classification': classifications[0],
                'type': 'Default Type',
                'level': levels[0],
                'faction': factions[0],
                'creature_class': classes[0],
                'expansion': expansions[0],
                'abilities': [abilities[0]],
            },
            {
                'name': 'Default Creature 2',
                'model_image': 'default_creature.png',
                'classification': classifications[1],
                'type': 'Default Type',
                'level': levels[0],
                'faction': factions[0],
                'creature_class': classes[0],
                'expansion': expansions[0],
                'abilities': [abilities[0]],
            },
        ]

        for creature_data in creatures:

            creature = Creature()

            creature.name = creature_data.get('name')

            file_path = os.path.abspath(os.path.join(image_dir, creature_data.get('model_image')))
            f = open(file_path, 'rb')
            creature.model_image = File(f)

            classification, created = Classification.objects.get_or_create(creature_data.get('classification'))
            creature.classification = classification

            creature.type = creature_data.get('type')

            level, created = Level.objects.get_or_create(creature_data.get('level'))
            creature.level = level

            faction, created = Faction.objects.get_or_create(creature_data.get('faction'))
            creature.faction = faction

            creature_class, created = Class.objects.get_or_create(creature_data.get('creature_class'))
            creature.creature_class = creature_class

            expansion, created = Expansion.objects.get_or_create(creature_data.get('expansion'))
            creature.expansion = expansion

            abilities_list = []

            for creature_ability in creature_data.get('abilities'):
                abilities_list.append(self.populate_abilities(creature_ability))

            creature.save()
            creature.abilities.set(abilities_list)