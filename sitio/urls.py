from django.urls import path

from sitio import views

urlpatterns = [
    path('', views.inicio, name='incio'),
    path('login/',views.login_view, name='login'),
    path('newalert/',views.newalert, name='newalert'),
    path('newalert/<int:pk>/', views.newalert, name='modificar_alerta'),
    path('newalert/eliminar/<int:pk>/', views.eliminar_alerta, name='eliminar_alerta'),
    path('contacto/',views.contacto, name='contacto'),
    path('servicios/',views.servicioalerta, name='servicioalerta'),
    path('nosotros/',views.nosotros, name='nosotros'),
    path('quienessomos/', views.quienessomos, name='quienessomos'),
    path('sismos/', views.sismos, name='sismos'),
    path('clima/', views.clima, name='clima'),
]