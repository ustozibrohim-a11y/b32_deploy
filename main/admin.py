from django.contrib import admin

import main.models as models


# Register your models here.

@admin.register(models.Faq)
class FaqAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    ...


@admin.register(models.TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    ...
