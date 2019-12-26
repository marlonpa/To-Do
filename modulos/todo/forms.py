from crispy_forms.layout import Submit, Button, Layout, Field, HTML, Row, Div
from django import forms
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group, Permission
from django.urls import reverse_lazy

from modulos.todo.models import Task
from modulos.users.models import Users

url_tyc = reverse_lazy('users:ter_and_con')
url_reg_gru = reverse_lazy('users:reg_gru')
url_reg_tip_usu = reverse_lazy('users:reg_tip_usr')


#Form tarea
class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['task_name', ]

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['task_name'].required = True
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_group_wrapper_class = 'row clearfix'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-10 col-md-10 col-sm-8 form-control-label'
        self.helper.field_class = 'col-lg-10 col-md-10 col-sm-8'
        self.helper.add_input(Submit('submit', 'Enviar'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-default'))
        self.helper.layout = Layout(
            'task_name'
        )


#Form actualizar tarea
class UtaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['task_name', ]

    def __init__(self, *args, **kwargs):
        super(UtaskForm, self).__init__(*args, **kwargs)
        self.fields['task_name'].required = False
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_group_wrapper_class = 'row clearfix'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-10 col-md-10 col-sm-8 form-control-label'
        self.helper.field_class = 'col-lg-10 col-md-10 col-sm-8'
        self.helper.add_input(Submit('submit', 'Enviar'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-default'))
        self.helper.layout = Layout(
            'task_name'
        )


#form asignar tarea
class AsitaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['userid', ]

    def __init__(self, *args, **kwargs):
        super(AsitaskForm, self).__init__(*args, **kwargs)
        self.fields['userid'].label = 'Asignar a'
        self.fields['userid'].query = Users.objects.filter(is_active__exact=True)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_group_wrapper_class = 'row clearfix'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-10 col-md-10 col-sm-8 form-control-label'
        self.helper.field_class = 'col-lg-10 col-md-10 col-sm-8'
        self.helper.add_input(Submit('submit', 'Enviar'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn-default'))
        self.helper.layout = Layout(
            'userid'
        )