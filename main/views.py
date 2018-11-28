from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from api.serializers import PersonModelSerializer
from main.models import Person, Category, Achievements
from main.forms import PersonListForm
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.generic.edit import FormMixin
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden

app_name = 'main'

def index(request):
    persons_list = Person.objects.all()
    if request.method == 'POST':
        form = PersonListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PersonListForm()
    context = {
		'persons_list': persons_list,
		'form': form
	}
    return render(request, 'main/index.html', context)

"""def persons_list(request, pk):
	try:
		task_list = Person.objects.get(id=task_list_id)
	except Task_List.DoesNotExist:
		raise Http404("Task List not found")
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/todos/'+str(task_list_id)+'/')
	else:
		form = TaskForm()
	context = {
		'task_list': task_list,
		'tasks': task_list.tasks.all(),
		'form': form
	}
	return render(request, 'main/todo_list.html', context)"""

class IndexView(FormMixin, ListView):
    template_name = "main/home.html"
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PersonModelSerializer
    form_class = PersonListForm
    def get_success_url(self):
        return redirect('/'+str(self.object.pk)+'/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['persons_list'] = Person.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super().form_valid(form)

    def get_queryset(self):
        return Person.objects.all().order_by('-date_created')

class DetailsView(FormMixin, DetailView):
    model = Person
    form_class = PersonListForm
    template_name = "main/details.html"
    serializer_class = PersonModelSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_success_url(self):
        return redirect('/'+str(self.object.pk)+'/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['person'] = Person.objects.get(pk=self.object.pk)
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super().form_valid(form)