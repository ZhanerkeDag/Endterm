from django import forms
from main.models import Person

app_name = 'main'

class PersonListForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ['id', 'name', 'surname', 'date_of_birth', 'email', 'number', 'gender', 'year_at_school', 'category', 'achievements', 'date_created']