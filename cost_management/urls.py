from django.urls import path, re_path
from . import views

# Create url
urlpatterns = [
    path('list/', views.my_expense, name='cost-list'),
    path('add/', views.add_expense, name='add-expense'),
    re_path(r'^edit/(?P<expense_id>[0-9]+)/$', views.edit_expense, name='edit-expense'),
    re_path(r'^delete/(?P<expense_id>[0-9]+)/$', views.delete_expense, name='delete-expense'),

]
