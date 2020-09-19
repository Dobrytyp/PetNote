from django.forms import ModelForm
from .models import Pet, PetOwner, VetVisit
from django.contrib.auth.models import User

class PetOwnerForm(ModelForm):
    class Meta:
        model = PetOwner
        fields = ['PetOwner_name', 'PetOwner_birth', 'PetOwner_gender', 'photo']
        labels = {
            'PetOwner_name': 'Imię',
            'PetOwner_birth': 'Data Urodzenia',
            'PetOwner_gender': 'Płeć',
            'photo': 'Zdjęcie'
        }


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
            'pet_species': 'Gatunek',
        }


class VetVisitForm(ModelForm):
    class Meta:
        model = VetVisit
        fields = ['visit_owner', 'date', 'address', 'telephone', 'email', 'vetname', 'comments']
        labels = {
            'visit_owner': 'Wybierz zwierze',
            'date': 'Data wizyty',
            'address': 'Adres',
            'telephone': 'Telefon',
            'email': 'Email',
            'vetname': 'Weterynarz',
            'comments': 'Komentarz'
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        labels = {
            'username': "Podaj imię",
            'password': "Podaj hasło",
            'email': "email"
        }