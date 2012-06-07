# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *


class PaperAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'date_published', 'doi', 'pubmed_id', 'neurosynth_id')
    search_fields = ('title', 'abstract', 'authors', 'doi', 'pubmed_id')


class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('title', 'paper')
    raw_id_fields = ('paper',)
    search_fields = ('title',)

    
class LocationAdmin(admin.ModelAdmin):
    list_display = ('x', 'y', 'z', 'experiment')
    raw_id_fields = ('experiment',)

    
class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'parent')
    list_filter = ('type',)
    raw_id_fields = ('parent',)
    readonly_fields = ('parent',)
    search_fields = ('name',)
    

class TagAdmin(admin.ModelAdmin):
    list_display = ('label', 'experiment', 'level', 'num_likes', 'num_dislikes')
    raw_id_fields = ('experiment',)
    readonly_fields = ('level', 'num_likes', 'num_dislikes')
    

class TagInstanceAdmin(admin.ModelAdmin):
    pass
    
    
class RatingAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(Paper, PaperAdmin)
admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(TagInstance, TagInstanceAdmin)
admin.site.register(Rating, RatingAdmin)
