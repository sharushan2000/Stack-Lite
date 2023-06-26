from django import forms
from .models import Ticket ,Comment



class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ("title", "describe", "code")
        # widgets = {
        #     "title": forms.TextInput(attrs={"class": "form-control"}),
        #     "describe": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        #     "code": forms.Textarea(attrs={"class": "form-control", "rows": 8}),
        # }



class CommentForm(forms.ModelForm):

    class Meta:
        model =Comment
        fields =("title","solution","code")
        # widgets = {
        #     "title": forms.TextInput(attrs={"class": "form-control"}),
        #     "solution": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        #     "code": forms.Textarea(attrs={"class": "form-control", "rows": 8}),
        # }


