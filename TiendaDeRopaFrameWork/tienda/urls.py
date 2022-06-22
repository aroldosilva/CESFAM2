from django.urls import path
from .views import home
from .views import galeria
from .views import producto
from .views import carro
from .views import contacto
from .views import listado
from .views import form_producto, form_mod_producto, form_del_producto

urlpatterns = [
    path('',home,name="home"),
    path('galeria/<id>',galeria,name="galeria"),
    path('producto/<id>',producto,name="producto"),
    path('carro/',carro,name="carro"),
    path('contacto/',contacto,name="contacto"),
    path('lista/',listado,name="lista"),
    path('form_producto/',form_producto,name="form_producto"),
    path('form_mod_producto/<id>',form_mod_producto,name="form_mod_producto"),
    path('form_del_producto/<id>',form_del_producto,name="form_del_producto"),
]