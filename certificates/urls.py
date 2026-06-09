from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'add/',
        views.add_certificate,
        name='add_certificate'
    ),

    path(
        'list/',
        views.certificate_list,
        name='certificate_list'
    ),

    path(
        'view/<int:id>/',
        views.certificate_view,
        name='certificate_view'
    ),

    path(
        'edit/<int:id>/',
        views.edit_certificate,
        name='edit_certificate'
    ),

    path(
        'delete/<int:id>/',
        views.delete_certificate,
        name='delete_certificate'
    ),
]