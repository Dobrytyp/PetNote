from django.urls import path, include


from mainapp.views import mypage, logout, all_pets, main, logged_new_pet, logged_edit_pet, logged_delete_pet, logged_new_visit, logged_delete_visit, logged_edit_visit, google_account, registration, new_account, all_accounts,edit_account, delete_account, new_pet, edit_pet, delete_pet, new_visit, all_visits, edit_visit, delete_visit


urlpatterns = [
    # login and registration
    path('main/', main, name='main'),
    path('', include('django.contrib.auth.urls')),
    path('registration/', registration),
    path('mylogout/', logout),
    # Logged user
    path('mypage/', mypage, name='mypage'),
    path('logged-new-pet/', logged_new_pet),
    path('logged-new-pet/<int:id>/', logged_edit_pet),
    path('logged-delete-pet/<int:id>/', logged_delete_pet),
    path('logged-new-visit/', logged_new_visit),
    path('logged-new-visit/<int:id>/', logged_new_visit),
    path('logged-edit-visit/<int:id>/', logged_edit_visit),
    path('logged-delete-visit/<int:id>/', logged_delete_visit),
    # admin Crud
    path('new-account/', google_account, name='google-account'),
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

]