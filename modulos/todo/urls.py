from django.urls import reverse_lazy, path
from django.contrib.auth.decorators import login_required

from modulos.todo.views import Ltd, Rtd, Utask, jsonCambiarEstado, AsignarTask
from modulos.users.views import Login, salir, Panel, Lus, Rus, Uus, CambiarEstado

urlpatterns = [

    path('lis/td/',
         login_required(Ltd.as_view(), login_url=reverse_lazy('users:login')),
         name='ltd'),
    path('reg/td/',
         login_required(Rtd.as_view(), login_url=reverse_lazy('users:login')),
         name='rtd'),
    path('upd/<int:pk>/task/',
         login_required(Utask.as_view(), login_url=reverse_lazy('users:login')),
         name='utask'),
    path('cam/est/', login_required(jsonCambiarEstado), name='cambiarEstado'),
    path('asi/<int:pk>/task/',
         login_required(AsignarTask.as_view(), login_url=reverse_lazy('users:login')),
         name='asitask'),

]
