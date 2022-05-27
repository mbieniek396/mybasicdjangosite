from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("<int:nr>", views.v1, name="v1"),
    path("klient/<int:idK>/", views.klientS, name='showKlient'),
    path("siema/", views.siema, name="Siema"),
    path("<str:value>/", views.name, name="Siema")
]
