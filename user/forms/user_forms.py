from django.forms import ModelForm, widgets
from user.models import User

class UserCreateForm(ModelForm):
    class Meta:
        model = User
        exlude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'})
        }