from django.contrib import admin

from .models import PetOwner, Pet, VetVisit


@admin.register(PetOwner)
class PetOwnerAdmin(admin.ModelAdmin):
    exclude = ["premium_account"]               # wszystkie pola oprócz: ""
    list_display = ["PetOwner_name", "photo"]   # pola do wyśiwetlenia na liście
    list_filter = ('PetOwner_gender',)          # filtrowanie po rpawej stronie
    search_fields = ('PetOwner_name',)          # wyszukiwanie po polu


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    exclude = [""]
    list_display = ["pet_name", "photo"]   # pola do wyśiwetlenia na liście
    list_filter = ('pet_gender',)          # filtrowanie po prawej stronie
    search_fields = ('pet_name',)


@admin.register(VetVisit)
class VetVisitAdmin(admin.ModelAdmin):
    exclude = [""]
    list_display = ["visit_owner", "date"]   # pola do wyśiwetlenia na liście
    list_filter = ("visit_owner",)          # filtrowanie po prawej stronie
    search_fields = ("visit_owner",)