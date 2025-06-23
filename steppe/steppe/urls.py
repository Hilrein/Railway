from django.contrib import admin
from django.urls import path
from app import views
from app.views import LoginUser


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("about", views.about, name='about'),
    path("contacts", views.contacts, name='contacts'),
    path("registration", views.RegisterUser.as_view(), name='registration'),
    path("login", LoginUser.as_view(), name='login'),
    path('success_form/', views.success_form, name='success_form'),
    path('find_trains/', views.find_trains, name='find_trains'),
    path('buy_ticket/<int:train_id>/', views.buy_ticket, name='buy_ticket'),
    path('payment/test/', views.payment_test, name='payment_test'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('reviews/', views.reviews, name='reviews'),
    path('logout/', views.logout_user, name='logout'),
    path("create/", views.create, name='create'),
    path('delete/<int:rid>/', views.delete, name='delete'),
    path('select_wagon/', views.select_wagon, name='select_wagon'),
    path('question_save/', views.question_save, name='question_save'),
    path("bonuses", views.bonuses, name='bonuses'),
    path("promokod", views.promokod, name='promokod'),
    path("kuzhat", views.kuzhat, name='kuzhat'),
    path("myprofile", views.myprofile, name='myprofile'),
    path("bailanys", views.bailanys, name='bailanys'),
    path("sayahat", views.sayahat, name='sayahat'),
]
