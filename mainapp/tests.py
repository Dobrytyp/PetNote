from django.test import TestCase
from .models import User, PetOwner, Pet, VetVisit


class PetOwnerTests(TestCase):

    def setUp(self):
        self.test_PetOwner_user = 1
        self.test_PetOwner_name = 'Wiesław'
        self.test_PetOwner_birth = '2020-03-12'
        self.test_PetOwner_gender = 'Man'
        self.test_PetOwner_premium_account = False
        return super().setUp()

    def test_PetOwner_creation(self):
        myuser = User.objects.create(id=1)
        petowner = PetOwner.objects.create(user=myuser,
                                           PetOwner_name='Wiesław',
                                           PetOwner_birth='2020-03-12',
                                           PetOwner_gender='Man',
                                           premium_account=False)
        self.assertEqual(petowner.id, 1)
        self.assertEqual(petowner.PetOwner_name, self.test_PetOwner_name)
        self.assertEqual(petowner.PetOwner_birth, self.test_PetOwner_birth)
        self.assertEqual(petowner.PetOwner_gender, self.test_PetOwner_gender)
        self.assertEqual(petowner.premium_account, self.test_PetOwner_premium_account)


class PetTests(TestCase):

    def setUp(self):
        self.test_pet_owner = 1
        self.test_pet_name = 'Rex'
        self.test_pet_birth = '2020-02-12'
        self.test_pet_gender = 'Male'
        self.test_pet_weight = '4'
        self.test_pet_species = 'Dog'

    def test_Pet_creation(self):
        myuser = User.objects.create(id=1)
        petowner = PetOwner.objects.create(user=myuser,
                                         PetOwner_birth='2020-03-12'
                                         )
        pet = Pet.objects.create(pet_owner=petowner,
                                 pet_name='Rex',
                                 pet_birth='2020-02-12',
                                 pet_gender='Male',
                                 pet_weight='4',
                                 pet_species='Dog')
        self.assertEqual(pet.id, 1)
        self.assertEqual(pet.pet_name, self.test_pet_name)
        self.assertEqual(pet.pet_birth, self.test_pet_birth)
        self.assertEqual(pet.pet_gender, self.test_pet_gender)
        self.assertEqual(pet.pet_weight, self.test_pet_weight)
        self.assertEqual(pet.pet_species, self.test_pet_species)


class VisitTests(TestCase):

    def setUp(self):
        self.test_visit_owner = 1
        self.test_date = '2020-09-30 11:30:00'
        self.test_address = 'ul. Polnej Róży'
        self.test_telephone = 505012333
        self.test_email = 'brak@brak.pl'
        self.test_vetname = 'Marek'
        self.test_comments = 'Parter, pokój nr 2'

    def test_Visit_creation(self):
        myuser = User.objects.create(id=1)
        petowner = PetOwner.objects.create(user=myuser,
                                           PetOwner_birth='2020-03-12'
                                           )
        pet = Pet.objects.create(pet_owner=petowner,
                                 pet_name='Rex',
                                 pet_birth='2020-02-12',
                                 pet_gender='Male',
                                 pet_weight='4',
                                 pet_species='Dog')

        visit = VetVisit.objects.create(visit_owner=pet,
                                        date='2020-09-30 11:30:00',
                                        address='ul. Polnej Róży',
                                        telephone=505012333,
                                        email='brak@brak.pl',
                                        vetname='Marek',
                                        comments='Parter, pokój nr 2')
        self.assertEqual(visit.id, 1)
        self.assertEqual(visit.date, self.test_date)
        self.assertEqual(visit.address, self.test_address)
        self.assertEqual(visit.telephone, self.test_telephone)
        self.assertEqual(visit.email, self.test_email)
        self.assertEqual(visit.vetname, self.test_vetname)
        self.assertEqual(visit.comments, self.test_comments)