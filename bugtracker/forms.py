from django import forms
from bugtracker.models import Ticket

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class AddTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description"]
        
        
class AssignTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["user_assigned"]