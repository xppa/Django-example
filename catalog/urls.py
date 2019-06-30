from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.ClientListView.as_view(), name='clients'),
    path('client/<int:pk>', views.ClientDetailView.as_view(), name='client-detail'),
    path('doctors/', views.DoctorListView.as_view(), name='doctors'),
    path('doctor/<int:pk>',
         views.DoctorDetailView.as_view(), name='doctor-detail'),
]


urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),  # Added for challenge
]


# Add URLConf for librarian to renew a book.
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]


# Add URLConf to create, update, and delete authors
urlpatterns += [
    path('doctor/create/', views.DoctorCreate.as_view(), name='doctor_create'),
    path('doctor/<int:pk>/update/', views.DoctorUpdate.as_view(), name='doctor_update'),
    path('doctor/<int:pk>/delete/', views.DoctorDelete.as_view(), name='doctor_delete'),
]

# Add URLConf to create, update, and delete books
urlpatterns += [
    path('client/create/', views.ClientCreate.as_view(), name='client_create'),
    path('client/<int:pk>/update/', views.ClientUpdate.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', views.ClientDelete.as_view(), name='client_delete'),
]
