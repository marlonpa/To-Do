from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
import json
from django.http import Http404, HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView
from modulos.todo.forms import TaskForm, UtaskForm, AsitaskForm
from modulos.todo.models import Task


#listar tareas
class Ltd(ListView):
    template_name = 'todo/lis.html'
    model = Task
    paginate_by = 30

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_admin:
            qs = Task.objects.all().order_by('id')
        else:
            qs = Task.objects.filter(userid=self.request.user).order_by('id')

        task = self.request.GET.get('nom', None)

        if task:
            qs = qs.filter(task_name__icontains=task)
        return qs

    def get_context_data(self, **kwargs):
        context = super(Ltd, self).get_context_data(**kwargs)
        tot = len(self.get_queryset())
        context["tot"] = tot
        context['tit_cont'] = 'Lista'
        context['sub_tit_cont'] = ' de tareas'
        task = self.request.GET.get('task', None)

        if task:
            context["task"] = task
        return context


#registrar tareas
class Rtd(CreateView):
    template_name = 'form.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        messages.success(self.request, "Se registro tarea exitosamente")
        return reverse_lazy('todo:ltd')

    def get_context_data(self, **kwargs):

        context = super(Rtd, self).get_context_data(**kwargs)
        context['tit_cont'] = 'Registrar'
        context['sub_tit_cont'] = ' Tarea'
        return context

    def form_valid(self, form):
        form.instance.task_name = form.instance.task_name.capitalize()
        form.instance.userid = self.request.user

        return super(Rtd, self).form_valid(form)


class Utask(UpdateView):
    template_name = 'form.html'
    form_class = UtaskForm
    model = Task

    def get_object(self, queryset=None):

        qs = Task.objects.get(pk=self.kwargs['pk'])
        return qs

    def get_success_url(self):
        messages.success(self.request, "Se ha actualizado el estado de la tarea")
        return reverse_lazy('todo:ltd')

    def get_context_data(self, **kwargs):

        context = super(Utask, self).get_context_data(**kwargs)
        context['tit_cont'] = 'Actualizar'
        context['sub_tit_cont'] = ' tarea'
        return context

    def form_valid(self, form):

        form.instance.task_name = form.instance.task_name.capitalize()
        return super(Utask, self).form_valid(form)


#cambiar de la tarea
@csrf_exempt
def jsonCambiarEstado(request):

    if request.method == 'POST' and request.is_ajax():

        estado = request.POST.get('estado', None)
        print(estado)
        id = request.POST.get('pk', None)
        print(id)

        if Task.objects.filter(pk=id).exists():
            qs = Task.objects.get(pk=id)
            qs.estado = estado
            qs.save()
            data = {'pk': qs.pk}
            return HttpResponse(json.dumps(data), content_type="application/json")


#asignar tarea
class AsignarTask(UpdateView):
    template_name = 'form.html'
    form_class = AsitaskForm
    model = Task

    def get_object(self, queryset=None):

        qs = Task.objects.get(pk=self.kwargs['pk'])
        return qs

    def get_success_url(self):
        messages.success(self.request, "Se ha actualizado el estado de la tarea")
        return reverse_lazy('todo:ltd')

    def get_context_data(self, **kwargs):

        context = super(AsignarTask, self).get_context_data(**kwargs)
        context['tit_cont'] = 'Actualizar'
        context['sub_tit_cont'] = ' Asignado'
        return context



