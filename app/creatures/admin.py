from django.contrib import admin
from creatures.models import Class
from creatures.models import Classification
from creatures.models import Expansion
from creatures.models import Level
from creatures.models import Faction
from creatures.models import School
from creatures.models import DispelType
from creatures.models import Ability
from creatures.models import Creature
# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_health', 'base_mana', 'base_armor', 'base_melee_min', 'base_melee_max', 'base_money', 'base_experience', 'base_reputation')

class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_health_multiplier', 'base_mana_multiplier', 'base_armor_multiplier', 'base_melee_min_multiplier', 'base_melee_max_multiplier', 'base_money_multiplier', 'base_experience_multiplier', 'base_reputation_multiplier')

class ExpansionAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_health_multiplier', 'base_mana_multiplier', 'base_armor_multiplier', 'base_melee_min_multiplier', 'base_melee_max_multiplier', 'base_money_multiplier', 'base_experience_multiplier', 'base_reputation_multiplier')

class LevelAdmin(admin.ModelAdmin):
    list_display = ('number', 'base_health_multiplier', 'base_mana_multiplier', 'base_armor_multiplier', 'base_melee_min_multiplier', 'base_melee_max_multiplier', 'base_money_multiplier', 'base_experience_multiplier', 'base_reputation_multiplier')

class FactionAdmin(admin.ModelAdmin):
    list_display = ('name',)

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DispelTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class AbilityAdmin(admin.ModelAdmin):
    list_display = ('ability_id', 'icon_image', 'name', 'tooltip', 'cost', 'range', 'cast_time', 'gcd', 'school', 'cooldown', 'value', 'duration', 'dispel_type')

class CreatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'model_image', 'classification', 'type', 'level', 'faction', 'creature_class', 'expansion')
    readonly_fields=('health', 'mana', 'armor', 'melee_min', 'melee_max', 'money', 'experience', 'reputation')

admin.site.register(Class, ClassAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Expansion, ExpansionAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Faction, FactionAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(DispelType, DispelTypeAdmin)
admin.site.register(Ability, AbilityAdmin)
admin.site.register(Creature, CreatureAdmin)
