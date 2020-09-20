from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import PetOwner, Pet, VetVisit
from .forms import PetOwnerForm, PetForm, VetVisitForm, UserForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def main(request):
    return render(request, "main.html")


def registration(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        send_mail(
            'Aktywacja Aplikacji PetNote',
            'To działa',
            'pythonpetnote@gmail.com',
            [form.cleaned_data['email']],
            fail_silently=False,
        )
        new_user = form.save()
        print(new_user)
        # created_user = User.objects.all()
        created_user2 = User.objects.get(email=new_user.email)
        created_user = created_user2.id
        return redirect('new-account', created_user)

    return render(request, "registration.html", {'form': form})


def google_account(request):
    if PetOwner.objects.filter(user__id__exact=request.user.id):
        users = PetOwner.objects.all()
        return render(request, "main.html", {'users': users})
    else:
        form = PetOwnerForm(request.POST or None)
        print(request.user)
        if form.is_valid():
            petowner = form.save(commit=False)  # zmienna tymczasowa
            petowner.user = request.user  # podpina user pod PetOwner
            petowner.save()
            return redirect('main')

        return render(request, 'new-account.html', {'form': form})


def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name="register-login/login.html",
                  context={"form": form})


"""Account C.R.U.D."""


def new_account(request, created_user):
    if PetOwner.objects.filter(user__id__exact=request.user.id):
        users = PetOwner.objects.all()
        return render(request, "main.html", {'users': users})
    else:
        print(created_user)
        new_user = User.objects.get(id=created_user)
        form = PetOwnerForm(request.POST or None)

        if form.is_valid():
            petowner = form.save(commit=False)      # zmienna tymczasowa
            petowner.user = new_user            # podpina user pod PetOwner
            petowner.save()
            return redirect('main')

        return render(request, 'new-account.html', {'form': form})


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


"""Pet C.R.U.D"""


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


"""Visit C.R.U.D."""


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