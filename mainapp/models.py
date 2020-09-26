from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()     # Maciek N. 2020-09-19 AnonymusUser


class MyModel(models.Model):
    class PetGender(models.TextChoices):
        MALE = 'Male', "Samiec"
        FEMLAE = 'Female', "Samica"
        UNN = 'Unknown', "Nie Wybrano"

    class UserGender(models.TextChoices):
        BOY = 'Man', "Mężczyzna"
        GRL = "Woman", "Kobieta"
        UNN = 'Unknown', "Nie Wybrano"

    class Weight(models.TextChoices):
        UNW = 0, "Nie Wybrano"
        kg1 = 1, '1 kg'
        kg2 = 2, '2 kg'
        kg3 = 3, '3 kg'
        kg4 = 4, '4 kg'
        kg5 = 5, '5 kg'
        kg6 = 6, '6 kg'
        kg7 = 7, '7 kg'
        kg8 = 8, '8 kg'
        kg9 = 9, '9 kg'
        kg10 = 10, '10 kg'
        kg11 = 11, '11 kg'
        kg12 = 12, '12 kg'
        kg13 = 13, '13 kg'
        kg14 = 14, '14 kg'
        kg15 = 15, '15 kg'
        kg16 = 16, '16 kg'
        kg17 = 17, '17 kg'
        kg18 = 18, '18 kg'
        kg19 = 19, '19 kg'
        kg20 = 20, '20 kg'
        kg21 = 21, '21 kg'
        kg22 = 22, '22 kg'
        kg23 = 23, '23 kg'
        kg24 = 24, '24 kg'
        kg25 = 25, '25 kg'
        kg26 = 26, '26 kg'
        kg27 = 27, '27 kg'
        kg28 = 28, '28 kg'
        kg29 = 29, '29 kg'
        kg30 = 30, '30 kg'
        kg31 = 31, '31 kg'
        kg32 = 32, '32 kg'
        kg33 = 33, '33 kg'
        kg34 = 34, '34 kg'
        kg35 = 35, '35 kg'
        kg36 = 36, '36 kg'
        kg37 = 37, '37 kg'
        kg38 = 38, '38 kg'
        kg39 = 39, '39 kg'
        kg40 = 40, '40 kg'
        kg41 = 41, '41 kg'
        kg42 = 42, '42 kg'
        kg43 = 43, '43 kg'
        kg44 = 44, '44 kg'
        kg45 = 45, '45 kg'
        kg46 = 46, '46 kg'
        kg47 = 47, '47 kg'
        kg48 = 48, '48 kg'
        kg49 = 49, '49 kg'
        kg50 = 50, '50 kg'
        kg51 = 51, '51 kg'
        kg52 = 52, '52 kg'
        kg53 = 53, '53 kg'
        kg54 = 54, '54 kg'
        kg55 = 55, '55 kg'
        kg56 = 56, '56 kg'
        kg57 = 57, '57 kg'
        kg58 = 58, '58 kg'
        kg59 = 59, '59 kg'
        kg60 = 60, '60 kg'
        kg61 = 61, '61 kg'
        kg62 = 62, '62 kg'
        kg63 = 63, '63 kg'
        kg64 = 64, '64 kg'
        kg65 = 65, '65 kg'
        kg66 = 66, '66 kg'
        kg67 = 67, '67 kg'
        kg68 = 68, '68 kg'
        kg69 = 69, '69 kg'
        kg70 = 70, '70 kg'
        kg71 = 71, '71 kg'
        kg72 = 72, '72 kg'
        kg73 = 73, '73 kg'
        kg74 = 74, '74 kg'
        kg75 = 75, '75 kg'
        kg76 = 76, '76 kg'
        kg77 = 77, '77 kg'
        kg78 = 78, '78 kg'
        kg79 = 79, '79 kg'
        kg80 = 80, '80 kg'
        kg81 = 81, '81 kg'
        kg82 = 82, '82 kg'
        kg83 = 83, '83 kg'
        kg84 = 84, '84 kg'
        kg85 = 85, '85 kg'
        kg86 = 86, '86 kg'
        kg87 = 87, '87 kg'
        kg88 = 88, '88 kg'
        kg89 = 89, '89 kg'
        kg90 = 90, '90 kg'
        kg91 = 91, '91 kg'
        kg92 = 92, '92 kg'
        kg93 = 93, '93 kg'
        kg94 = 94, '94 kg'
        kg95 = 95, '95 kg'
        kg96 = 96, '96 kg'
        kg97 = 97, '97 kg'
        kg98 = 98, '98 kg'
        kg99 = 99, '99 kg'

    class PetSpecies(models.TextChoices):
        DOG = "Pies", 'Dog'
        CAT = "Kot", 'Cat'
        MOU = "Mysz", 'Mouse'
        UNN = "Nie Wybrano", 'Unknown'


class PetOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)     # Foreign_Key do usera
    PetOwner_name = models.CharField(max_length=64)
    PetOwner_birth = models.DateField()
    PetOwner_gender = models.CharField(max_length=11, choices=MyModel.UserGender.choices,
                                       default=MyModel.UserGender.UNN)
    photo = models.ImageField(upload_to="pictures", null=True, blank=True)
    premium_account = models.BooleanField(default=False)

    def __str__(self):
        return self.PetOwner_name


class Pet(models.Model):
    pet_owner = models.ForeignKey(PetOwner, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=64)
    pet_birth = models.DateField()
    pet_gender = models.CharField(max_length=24, choices=MyModel.PetGender.choices, default=MyModel.PetGender.UNN)
    pet_weight = models.CharField(max_length=24, choices=MyModel.Weight.choices, default=MyModel.Weight.UNW)
    photo = models.ImageField(upload_to="pictures", null=True, blank=True)
    pet_species = models.CharField(max_length=24, choices=MyModel.PetSpecies.choices, default=MyModel.PetSpecies.UNN)

    def __str__(self):
        return self.pet_name


class VetVisit(models.Model):
    visit_owner = models.ForeignKey(Pet, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField()
    address = models.TextField(max_length=128)
    telephone = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    vetname = models.CharField(max_length=64, null=True, blank=True)
    comments = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f" {self.visit_owner } {self.date} ma wizytę: {self.address}"


class TestClass(models.Model):
    text = models.TextField(max_length=128)