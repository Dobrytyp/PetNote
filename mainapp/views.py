from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import PetOwner, Pet, VetVisit
from .forms import PetOwnerForm, PetForm, VetVisitForm, UserForm, LoggedPetForm, LoggedVetVisitForm


"""Core"""


def main(request):  # Strona Główna
    return render(request, "main.html")


def mypage(request):  # Główny widok użytkownika po zalogowaniu
    user_id = request.user.id
    print(user_id)
    pet_owner = PetOwner.objects.filter(user_id=user_id).values()
    user_pets = Pet.objects.filter(pet_owner_id=pet_owner[0]['id'])

    user_pets_id = user_pets.filter().values_list('id', flat=True)              # przeszukujemy po id zwierzęcia
    print(user_pets_id)
    user_pets_id_list = []                                                      # tworzymy listę
    for elem in user_pets_id:
        user_pets_id_list.append(elem)

    pet_visit = VetVisit.objects.filter(visit_owner_id__in=user_pets_id_list)   # filtrujemy id wizyty po liście z id zwierzęcia

    args = {'user_id': user_id, 'user_pets': user_pets, 'pet_visit': pet_visit}
    return render(request, "mypage.html", args)


def logout(request):  # wylogowanie
    return render(request, "mylogout.html")


"""Rejestracja i logowanie"""


def registration(request):  # rejestracja usera
    form = UserForm(request.POST or None)

    if request.method == 'POST':

        temp_email = request.POST.get('email')
        temp_db_user = User.objects.filter(email=temp_email).first()

        if temp_db_user:  # sprawdzenie czy email istnieje w DB
            return redirect('/mainapp/login/')  # jeśli tak, przekierowani do strony logowania
        if form.is_valid():  # sprawdzenie czy forma jest poprawna
            send_mail(  # wysyłka email
                'Aktywacja Aplikacji PetNote',
                'To działa',
                'pythonpetnote@gmail.com',
                [form.cleaned_data['email']],
                fail_silently=False,
            )

            new_user = form.save()
            get_user_by_email = User.objects.get(email=new_user.email)  # wyciągnięcie usera po emailu
            created_user = get_user_by_email.id  # wyciągnięcie jego id

            return redirect('new-account', created_user)
        else:
            return render(request, "registration.html", {'form': form})

    else:
        return render(request, "registration.html", {'form': form})


def google_account(request):  # rejestracja PetOwner dla Usera przez Google
    if PetOwner.objects.filter(user__id__exact=request.user.id):
        users = PetOwner.objects.all()
        # return render(request, "mypage.html", {'users': users})
        return redirect('mypage')
    else:
        form = PetOwnerForm(request.POST or None)
        print(request.user)
        if form.is_valid():
            petowner = form.save(commit=False)  # zmienna tymczasowa
            petowner.user = request.user  # podpina user pod PetOwner
            petowner.save()
            return redirect('mypage')  # rejestracja przez google nie wymaga juŻ logowania

        return render(request, 'new-account.html', {'form': form})


def new_account(request, created_user):  # rejestracja PetOwner dla Usera
    if PetOwner.objects.filter(user__id__exact=request.user.id):
        users = PetOwner.objects.all()
        return render(request, "main.html", {'users': users})
    else:
        new_user = User.objects.get(id=created_user)
        form = PetOwnerForm(request.POST or None)

        if form.is_valid():
            petowner = form.save(commit=False)  # zmienna tymczasowa
            petowner.user = new_user  # podpina user pod PetOwner
            petowner.save()
            return redirect('/mainapp/login/')  # przekierowanie do logowanie

        return render(request, 'new-account.html', {'form': form})


def login_request(request):  # logowanie
    form = AuthenticationForm()
    return render(request=request,
                  template_name="registration/login.html",
                  context={"form": form})


"""Logged User Pet C.R.U.D."""


def user_settings(request, id):
    edit = get_object_or_404(User, pk=id)

    return render(request, 'user-settings.html', {'id': id})



def user_delete(request, id):
    delete = get_object_or_404(User, pk=id)

    if request.method == "POST":
        delete.delete()
        return redirect('main')

    return render(request, 'user-delete.html', {'id': id, 'delete': delete})


def logged_new_pet(request):
    form = LoggedPetForm(request.POST or None)

    if form.is_valid():
        pet = form.save(commit=False)
        temp = PetOwner.objects.get(user_id=request.user.id)
        pet.pet_owner = temp
        pet.save()
        return redirect('mypage')

    return render(request, 'logged-new-pet.html', {'form': form})


def logged_edit_pet(request, id):
    edit = get_object_or_404(Pet, pk=id)
    form = LoggedPetForm(request.POST or None, instance=edit)

    if form.is_valid():
        form.save()
        redirect(main)
        return redirect('mypage')

    return render(request, 'logged-new-pet.html', {'id': id, 'form': form})


def logged_delete_pet(request, id):
    delete = get_object_or_404(Pet, pk=id)

    if request.method == "POST":
        delete.delete()
        return redirect('mypage')

    return render(request, 'logged-delete-pet.html', {'id': id, 'delete': delete})


"""Logged User Pet C.R.U.D."""


def logged_new_visit(request, id):
    form = LoggedVetVisitForm(request.POST or None)
    if form.is_valid():
        print(id)
        visit = form.save(commit=False)
        temp = Pet.objects.get(id=id)
        print(temp)
        visit.visit_owner = temp
        visit.save()
        return redirect('mypage')
    return render(request, 'logged-new-visit.html', {'form': form})


def logged_edit_visit(request, id):
    edit = get_object_or_404(VetVisit, pk=id)
    form = LoggedVetVisitForm(request.POST or None, instance=edit)
    if form.is_valid():
        form.save()
        redirect(main)
        return redirect('mypage')

    return render(request, 'logged-edit-visit.html', {'form': form})


def logged_delete_visit(request, id):
    delete = get_object_or_404(VetVisit, pk=id)

    if request.method == "POST":
        delete.delete()
        return redirect('mypage')

    return render(request, 'logged-delete-visit.html', {'id': id, 'delete': delete})


"""""""""""""""""""""""""""Admin C.R.U.D."""""""""""""""""""""""""""""""""

"""Admin C.R.U.D."""


def all_accounts(request):
    users = PetOwner.objects.all()
    return render(request, "all-accounts.html", {'users': users})


def edit_account(request, id):
    edit = get_object_or_404(PetOwner, pk=id)
    form = PetOwnerForm(request.POST or None, instance=edit)

    if form.is_valid():
        form.save()
        redirect(main)
        return redirect('main')

    return render(request, 'new-account.html', {'form': form})


def delete_account(request, id):
    delete = get_object_or_404(PetOwner, pk=id)

    if request.method == "POST":
        delete.delete()
        return redirect('main')

    return render(request, 'delete-account.html', {'delete': delete})


"""Admin Pet C.R.U.D"""


def new_pet(request):
    form = PetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('main')

    return render(request, 'new-pet.html', {'form': form})


def all_pets(request):
    test = Pet.objects.all()
    return render(request, "all-pets.html", {'test': test})


def edit_pet(request, id):
    edit = get_object_or_404(Pet, pk=id)
    form = PetForm(request.POST or None, instance=edit)

    if form.is_valid():
        form.save()
        redirect(main)
        return redirect('main')

    return render(request, 'new-pet.html', {'form': form})


def delete_pet(request, id):
    delete = get_object_or_404(Pet, pk=id)

    if request.method == "POST":
        delete.delete()
        return redirect('main')

    return render(request, 'delete-pet.html', {'delete': delete})


"""Admin Visit C.R.U.D."""


def new_visit(request):
    form = VetVisitForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('main')

    return render(request, 'new-visit.html', {'form': form})


def all_visits(request):
    visits = VetVisit.objects.all()
    return render(request, "all-visits.html", {'visits': visits})


def edit_visit(request, id):
    edit = get_object_or_404(VetVisit, pk=id)
    form = VetVisitForm(request.POST or None, instance=edit)

    if form.is_valid():
        form.save()
        redirect(main)
        return redirect('main')

    return render(request, 'new-visit.html', {'form': form})


def delete_visit(request, id):
    delete = get_object_or_404(VetVisit, pk=id)

    if request.method == "POST":
        delete.delete()
        return redirect('main')

    return render(request, 'delete-visit.html', {'delete': delete})
