from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.user_search),
    path('login', views.login),
    path('login_process', views.login_process),
    path('signup', views.signup),
    path('signup_process', views.signup_process),
    path('admin/dashboard', views.admin_dashboard),
    path('admin/add_flight', views.admin_add_flight),
    path('admin/new_flight', views.new_flight),
    path('admin/edit_flight/<int:id>', views.admin_edit_flight),
    path('admin/update_flight/<int:id>', views.admin_update_flight),
    path('admin/delete_flight/<int:id>', views.admin_delete_flight),
    # path('search_results', views.search_results),
    path('dashboard', views.user_dashboard),
    path('book_flight/select_departure', views.book_flight_depart),
    # path('book_flight/select_return', views.book_flight_return),
    # path('book_flight/passengers', views.book_flight_passenger),
    path('payment/<int:id>', views.payment),
    path('book_flight/<int:id>', views.book_flight),
    path("logout", views.logout),
]