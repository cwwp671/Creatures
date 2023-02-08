"""
 * Author: Connor Pandolph
 * Project: World of Warcraft Creature Database
 * API: REST
 * Framework: Django
 * Container: Docker
 * Date: 2022
"""

from django.test import TestCase
from creatures.models import Creature, Class, Classification, Expansion, Level, Faction, School, DispelType, Ability

#Model testing cases

class ClassTestCase(TestCase):
    def setUp(self):
        Class.objects.create(name="warrior", base_health=5, base_mana=1, base_armor=5, base_melee_min=5, base_melee_max=25)
        Class.objects.create(name="mage", base_health=1, base_mana=5, base_armor=1, base_melee_min=1, base_melee_max=5)

    def test_classes_exists(self):
        warrior = Class.objects.get(name="warrior")
        mage = Class.objects.get(name="mage")
        self.assertEqual(warrior.name, "warrior")
        self.assertEqual(mage.name, "mage")

class ClassificationTestCase(TestCase):
    def setUp(self):
        Classification.objects.create(name="normal", base_health_multiplier=1, base_mana_multiplier=1, base_armor_multiplier=1, base_melee_min_multiplier=1, base_melee_max_multiplier=1, base_money_multiplier=1, base_experience_multiplier=1, base_reputation_multiplier=1)
        Classification.objects.create(name="elite", base_health_multiplier=2, base_mana_multiplier=2, base_armor_multiplier=2, base_melee_min_multiplier=2, base_melee_max_multiplier=2, base_money_multiplier=2, base_experience_multiplier=2, base_reputation_multiplier=2)

    def test_classifications_exists(self):
        normal = Classification.objects.get(name="normal")
        elite = Classification.objects.get(name="elite")
        self.assertEqual(normal.name, "normal")
        self.assertEqual(elite.name, "elite")

class ExpansionTestCase(TestCase):
    def setUp(self):
        Expansion.objects.create(name="original", base_health_multiplier=1, base_mana_multiplier=1, base_armor_multiplier=1, base_melee_min_multiplier=1, base_melee_max_multiplier=1, base_money_multiplier=1, base_experience_multiplier=1)
        Expansion.objects.create(name="expansion 1", base_health_multiplier=2, base_mana_multiplier=2, base_armor_multiplier=2, base_melee_min_multiplier=2, base_melee_max_multiplier=2, base_money_multiplier=2, base_experience_multiplier=2)

    def test_expansions_exists(self):
        original = Expansion.objects.get(name="original")
        expansion_1 = Expansion.objects.get(name="expansion 1")
        self.assertEqual(original.name, "original")
        self.assertEqual(expansion_1.name, "expansion 1")

class LevelTestCase(TestCase):
    def setUp(self):
        Level.objects.create(number=1, base_health_multiplier=1, base_mana_multiplier=1, base_armor_multiplier=1, base_melee_min_multiplier=1, base_melee_max_multiplier=1, base_money_multiplier=1, base_experience_multiplier=1)
        Level.objects.create(number=2, base_health_multiplier=2, base_mana_multiplier=2, base_armor_multiplier=2, base_melee_min_multiplier=2, base_melee_max_multiplier=2, base_money_multiplier=2, base_experience_multiplier=2)

    def test_levels_exists(self):
        level_1 = Level.objects.get(number=1)
        level_2 = Level.objects.get(number=2)
        self.assertEqual(level_1.number, 1)
        self.assertEqual(level_2.number, 2)

class FactionTestCase(TestCase):
    def setUp(self):
        Faction.objects.create(name="faction 1")
        Faction.objects.create(name="faction 2")

    def test_factions_exists(self):
        faction_1 = Faction.objects.get(name="faction 1")
        faction_2 = Faction.objects.get(name="faction 2")
        self.assertEqual(faction_1.name, "faction 1")
        self.assertEqual(faction_2.name, "faction 2")

class SchoolTestCase(TestCase):
    def setUp(self):
        School.objects.create(name="fire magic")
        School.objects.create(name="shadow magic")

    def test_schools_exists(self):
        fire_school = School.objects.get(name="fire magic")
        shadow_school = School.objects.get(name="shadow magic")
        self.assertEqual(fire_school.name, "fire magic")
        self.assertEqual(shadow_school.name, "shadow magic")

class DispelTypeTestCase(TestCase):
    def setUp(self):
        DispelType.objects.create(name="magic")
        DispelType.objects.create(name="curse")

    def test_dispeltypes_exists(self):
        magic_type = DispelType.objects.get(name="magic")
        curse_type = DispelType.objects.get(name="curse")
        self.assertEqual(magic_type.name, "magic")
        self.assertEqual(curse_type.name, "curse")

class AbilityTestCase(TestCase):
    def setUp(self):
        fire_school = School.objects.create(name="fire magic")
        shadow_school = School.objects.create(name="shadow magic")
        magic_type = DispelType.objects.create(name="magic")
        curse_type = DispelType.objects.create(name="curse")
        test_image_filepath = f"media/images/creatures/Default_Ability.jpg"
        Ability.objects.create(ability_id=1, name="fireball", icon_image=test_image_filepath, tooltip="Shoots a Fireball and Burns target afterwards", cost=5, range=40, cast_time=4.0, gcd=1.5, school=fire_school, cooldown=0, value=15, duration=4, dispel_type=magic_type)
        Ability.objects.create(ability_id=1, name="shadowbolt", icon_image=test_image_filepath, tooltip="Shoots a Shadow Bolt and Haunts target afterwards", cost=10, range=30, cast_time=2.5, gcd=1.5, school=shadow_school, cooldown=0, value=5, duration=4, dispel_type=curse_type)

    def test_abilities_exists(self):
        fireball = Ability.objects.get(name="fireball")
        shadowbolt = Ability.objects.get(name="shadowbolt")
        self.assertEqual(fireball.name, "fireball")
        self.assertEqual(shadowbolt.name, "shadowbolt")

class CreatureTestCase(TestCase):
    def setUp(self):
        warrior = Class.objects.create(name="warrior", base_health=5, base_mana=1, base_armor=5, base_melee_min=5, base_melee_max=25)
        mage = Class.objects.create(name="mage", base_health=1, base_mana=5, base_armor=1, base_melee_min=1, base_melee_max=5)
        normal = Classification.objects.create(name="normal", base_health_multiplier=1, base_mana_multiplier=1, base_armor_multiplier=1, base_melee_min_multiplier=1, base_melee_max_multiplier=1, base_money_multiplier=1, base_experience_multiplier=1, base_reputation_multiplier=1)
        elite = Classification.objects.create(name="elite", base_health_multiplier=2, base_mana_multiplier=2, base_armor_multiplier=2, base_melee_min_multiplier=2, base_melee_max_multiplier=2, base_money_multiplier=2, base_experience_multiplier=2, base_reputation_multiplier=2)
        original = Expansion.objects.create(name="original", base_health_multiplier=1, base_mana_multiplier=1, base_armor_multiplier=1, base_melee_min_multiplier=1, base_melee_max_multiplier=1, base_money_multiplier=1, base_experience_multiplier=1)
        expansion_1 = Expansion.objects.create(name="expansion 1", base_health_multiplier=2, base_mana_multiplier=2, base_armor_multiplier=2, base_melee_min_multiplier=2, base_melee_max_multiplier=2, base_money_multiplier=2, base_experience_multiplier=2)
        level_1 = Level.objects.create(number=1, base_health_multiplier=1, base_mana_multiplier=1, base_armor_multiplier=1, base_melee_min_multiplier=1, base_melee_max_multiplier=1, base_money_multiplier=1, base_experience_multiplier=1)
        level_2 = Level.objects.create(number=2, base_health_multiplier=2, base_mana_multiplier=2, base_armor_multiplier=2, base_melee_min_multiplier=2, base_melee_max_multiplier=2, base_money_multiplier=2, base_experience_multiplier=2)
        faction_1 = Faction.objects.create(name="faction 1")
        faction_2 = Faction.objects.create(name="faction 2")
        fire_school = School.objects.create(name="fire magic")
        shadow_school = School.objects.create(name="shadow magic")
        magic_type = DispelType.objects.create(name="magic")
        curse_type = DispelType.objects.create(name="curse")
        test_ability_image_filepath = f"media/images/creatures/Default_Ability.jpg"
        test_creature_image_filepath = f"media/images/creatures/Default_Creature.png"
        fireball = Ability.objects.create(ability_id=1, name="fireball", icon_image=test_ability_image_filepath, tooltip="Shoots a Fireball and Burns target afterwards", cost=5, range=40, cast_time=4.0, gcd=1.5, school=fire_school, cooldown=0, value=15, duration=4, dispel_type=magic_type)
        shadowbolt = Ability.objects.create(ability_id=1, name="shadowbolt", icon_image=test_ability_image_filepath, tooltip="Shoots a Shadow Bolt and Haunts target afterwards", cost=10, range=30, cast_time=2.5, gcd=1.5, school=shadow_school, cooldown=0, value=5, duration=4, dispel_type=curse_type)
        dummy_fire_mage = Creature.objects.create(name="fire mage", model_image=test_creature_image_filepath, classification=normal, type="Humanoid", level=level_1, faction=faction_1, creature_class=mage, expansion=original, health=1, mana=5, armor=1, melee_min=1, melee_max=5, money=1, experience=1, reputation=1)
        dummy_shadow_knight = Creature.objects.create(name="shadow knight", model_image=test_creature_image_filepath, classification=elite, type="Humanoid", level=level_2, faction=faction_2, creature_class=warrior, expansion=expansion_1, health=5, mana=2, armor=5, melee_min=5, melee_max=20, money=2, experience=2, reputation=2)
        dummy_fire_mage.abilities.add(fireball)
        dummy_shadow_knight.abilities.add(shadowbolt)

    def test_creatures_exists(self):
        fire_mage = Creature.objects.get(name="fire mage")
        shadow_knight = Creature.objects.get(name="shadow knight")
        self.assertEqual(fire_mage.name, "fire mage")
        self.assertEqual(shadow_knight.name, "shadow knight")