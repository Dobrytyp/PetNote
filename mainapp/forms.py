from django.forms import ModelForm
from .models import Pet, PetOwner, VetVisit


class PetOwnerForm(ModelForm):
    class Meta:
        model = PetOwner
        fields = ['PetOwner_name', 'PetOwner_birth', 'PetOwner_gender', 'photo']


class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['pet_owner', 'pet_name', 'pet_birth', 'pet_gender', 'pet_weight', 'photo', 'pet_species']
        labels = {
            'pet_owner': 'Właściciel',
            'pet_name' : 'Imie zwierzęcia',
            'pet_birth': 'Data urodzenia',
            'pet_gender': 'Płeć',
            'pet_weight': 'Waga',
            'photo': 'Zdjęcie',
            'pet_species': 'gatunek',
        }


class VetVisitForm(ModelForm):
    class Meta:
        model = VetVisit
        fields = ['visit_owner', 'date', 'address', 'telephone', 'email', 'vetname', 'comments']
