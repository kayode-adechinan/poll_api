from django.contrib import admin

# Register your models here.
from poll import models 

@admin.register(models.Poll)
class PollAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass    

@admin.register(models.Vote)
class VoteAdmin(admin.ModelAdmin):
    pass    


