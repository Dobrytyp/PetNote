from django.urls import path, include


from mainapp.views import all_pets, main, google_registration, registration, new_account, all_accounts,edit_account, delete_account, new_pet, edit_pet, delete_pet, new_visit, all_visits, edit_visit, delete_visit


urlpatterns = [
    path('main/', main, name='main'),
    # user Crud
    path('new-account/', google_registration, name='google-account-'),
    path('new-account/<int:created_user>', new_account, name='new-account'),
    path('all-accounts/', all_accounts),
    path('edit-account/<int:id>/', edit_account),
    path('delete-account/<int:id>/', delete_account),
    # pet crud
    path('new-pet/', new_pet),
    path('all-pets/', all_pets, name='test'),
    path('edit-pet/<int:id>/', edit_pet),
    path('delete-pet/<int:id>/', delete_pet),
    # vet visit crud
    path('new-visit/', new_visit),
    path('all-visits/', all_visits),
    path('edit-visit/<int:id>/', edit_visit),
    path('delete-visit/<int:id>/', delete_visit),
    path('registration/', registration)
]