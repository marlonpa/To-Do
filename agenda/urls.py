from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('modulos.users.urls', 'modulos.users'), namespace='users')),
    path('', include(('modulos.todo.urls', 'modulos.todo'), namespace='todo')),

]

