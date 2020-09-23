from django.forms import ModelForm
from .models import Pet, PetOwner, VetVisit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


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


class LoggedPetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['pet_name', 'pet_birth', 'pet_gender', 'pet_weight', 'photo', 'pet_species']
        labels = {
            'pet_name': 'Imie zwierzęcia',
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


class UserForm(UserCreationForm):
    username = forms.CharField(label="Nazwa Użytkownika", required=True)
    password1 = forms.CharField(label="Hasło", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Powtórz hasło", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

