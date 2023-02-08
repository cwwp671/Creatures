"""
 * Author: Connor Pandolph
 * Project: World of Warcraft Creature Database
 * API: REST
 * Framework: Django
 * Container: Docker
 * Date: 2022
"""

from django.db import models

#Creature Model Path
def model_image_path(instance, filename):
    path, ext = filename[-5:].split('.', 1)
    return f"images/creatures/{instance.name}.{ext}"

#Ability Icon Image Path
def ability_icon_image_path(instance, filename):
    path, ext = filename[-5:].split('.', 1)
    return f"images/creatures/{instance.name}.{ext}"

#NPC Class Model (Warrior, Mage etc.)
class Class(models.Model):
    name = models.CharField(max_length=128)
    base_health = models.SmallIntegerField()
    base_mana = models.SmallIntegerField()
    base_armor = models.SmallIntegerField()
    base_melee_min = models.SmallIntegerField()
    base_melee_max = models.SmallIntegerField()
    base_money = models.FloatField(default=1.0)
    base_experience = models.FloatField(default=1.0)
    base_reputation = models.FloatField(default=1.0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'class'
        verbose_name_plural = 'classes'

#NPC Type Model (Normal, Elite, Boss, etc.)
class Classification(models.Model):
    name = models.CharField(max_length=128)
    base_health_multiplier = models.FloatField()
    base_mana_multiplier = models.FloatField()
    base_armor_multiplier = models.FloatField()
    base_melee_min_multiplier = models.FloatField()
    base_melee_max_multiplier = models.FloatField()
    base_money_multiplier = models.FloatField()
    base_experience_multiplier = models.FloatField()
    base_reputation_multiplier = models.FloatField()

    def __str__(self):
        return self.name

#NPC Expansion Origin Model
class Expansion(models.Model):
    name = models.CharField(max_length=128)
    base_health_multiplier = models.FloatField()
    base_mana_multiplier = models.FloatField()
    base_armor_multiplier = models.FloatField()
    base_melee_min_multiplier = models.FloatField()
    base_melee_max_multiplier = models.FloatField()
    base_money_multiplier = models.FloatField()
    base_experience_multiplier = models.FloatField()
    base_reputation_multiplier = models.FloatField(default=1.0)

    def __str__(self):
        return self.name

#NPC Experience Level Model
class Level(models.Model):
    number = models.SmallIntegerField()
    base_health_multiplier = models.FloatField()
    base_mana_multiplier = models.FloatField()
    base_armor_multiplier = models.FloatField()
    base_melee_min_multiplier = models.FloatField()
    base_melee_max_multiplier = models.FloatField()
    base_money_multiplier = models.FloatField()
    base_experience_multiplier = models.FloatField()
    base_reputation_multiplier = models.FloatField(default=1.0)

    def __str__(self):
        return str(self.number)

#NPC Faction Alignment Model
class Faction(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

#Ability School of Magic Model (Fire, Frost, etc.)
class School(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

#Ability Dispel Type Model (Magic, Curse, Poison, etc.)
class DispelType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

#NPC Abilities Model (Fireball, Shadow Bolt, etc.)
class Ability(models.Model):
    ability_id = models.IntegerField()
    name = models.CharField(max_length=128)
    icon_image = models.ImageField(upload_to=ability_icon_image_path)
    tooltip = models.TextField()
    cost = models.IntegerField()
    range = models.IntegerField()
    cast_time = models.FloatField()
    gcd = models.FloatField()
    school = models.ForeignKey('School', related_name='abilities', on_delete=models.CASCADE)
    cooldown = models.FloatField()
    value = models.FloatField()
    duration = models.FloatField()
    dispel_type = models.ForeignKey('DispelType', related_name='dispel_types', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ability'
        verbose_name_plural = 'abilities'

#NPC Model
class Creature(models.Model):
    name = models.CharField(max_length=128)
    model_image = models.ImageField(upload_to=model_image_path)
    classification = models.ForeignKey('Classification', related_name='creatures', on_delete=models.CASCADE)
    type = models.CharField(max_length=128)
    level = models.ForeignKey('Level', related_name='creatures', on_delete=models.CASCADE)
    faction = models.ForeignKey('Faction', related_name='creatures', on_delete=models.CASCADE)
    creature_class = models.ForeignKey('Class', related_name='creatures', on_delete=models.CASCADE)
    expansion = models.ForeignKey('Expansion', related_name='creatures', on_delete=models.CASCADE, null=True)
    abilities = models.ManyToManyField(Ability, blank=True)
    health = models.FloatField(default=0.0)
    mana = models.FloatField(default=0.0)
    armor = models.FloatField(default=0.0)
    melee_min = models.FloatField(default=0.0)
    melee_max = models.FloatField(default=0.0)
    money = models.FloatField(default=0.0)
    experience = models.FloatField(default=0.0)
    reputation = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        self.health = self.calculate_health()
        self.mana = self.calculate_mana()
        self.armor = self.calculate_armor()
        self.melee_min = self.calculate_melee_min()
        self.melee_max = self.calculate_melee_max()
        self.money = self.calculate_money()
        self.experience = self.calculate_experience()
        self.reputation = self.calculate_reputation()
        super(Creature, self).save(*args, **kwargs)

    #Automatic stat calculations based on linked models

    def calculate_health(self):
        if self.creature_class.base_health != 0:
            return self.creature_class.base_health * self.classification.base_health_multiplier * self.level.base_health_multiplier * self.expansion.base_health_multiplier
        else:
            return 0

    def calculate_mana(self):
        if self.creature_class.base_mana != 0:
            return self.creature_class.base_mana * self.classification.base_mana_multiplier * self.level.base_mana_multiplier * self.expansion.base_mana_multiplier
        else:
            return 0

    def calculate_armor(self):
        if self.creature_class.base_armor != 0:
            return self.creature_class.base_armor * self.classification.base_armor_multiplier * self.level.base_armor_multiplier * self.expansion.base_armor_multiplier
        else:
            return 0

    def calculate_melee_min(self):
        if self.creature_class.base_melee_min != 0:
            return self.creature_class.base_melee_min * self.classification.base_melee_min_multiplier * self.level.base_melee_min_multiplier * self.expansion.base_melee_min_multiplier
        else:
            return 0

    def calculate_melee_max(self):
        if self.creature_class.base_melee_max != 0:
            return self.creature_class.base_melee_max * self.classification.base_melee_max_multiplier * self.level.base_melee_max_multiplier * self.expansion.base_melee_max_multiplier
        else:
            return 0

    def calculate_money(self):
        if self.creature_class.base_money != 0:
            return self.creature_class.base_money * self.classification.base_money_multiplier * self.level.base_money_multiplier * self.expansion.base_money_multiplier
        else:
            return 0

    def calculate_experience(self):
        if self.creature_class.base_experience != 0:
            return self.creature_class.base_experience * self.classification.base_experience_multiplier * self.level.base_experience_multiplier * self.expansion.base_experience_multiplier
        else:
            return 0

    def calculate_reputation(self):
        if self.creature_class.base_reputation != 0:
            return self.creature_class.base_reputation * self.classification.base_reputation_multiplier * self.level.base_reputation_multiplier * self.expansion.base_reputation_multiplier
        else:
            return 0