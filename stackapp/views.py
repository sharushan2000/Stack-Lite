from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TicketForm
from django.views.generic.list import ListView
from .models import Ticket
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request ,"stackapp/index.html",{} )




@login_required
def create_ticket(request):
    form = TicketForm()

    if request.method =="POST":
        ticket_form = TicketForm(request.POST)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.maker = request.user
            print(request.user)
            ticket.save()

            return redirect("stackapp:list_questions")

    context = {
        "form":form,
        }
    return render(request,"stackapp/ask.html",context)



class QuestionList(ListView):
    model= Ticket
    paginate_by = 20
    template_name = "stackapp/queslistview.html"
    context_object_name = "questions"
    

class SearchQuestionList(ListView):
    model =Ticket
    paginate_by = 20
    template_name = "stackapp/queslistview.html"
    context_object_name = "questions"

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get("search")
        object_list = Ticket.objects.filter(
           Q(title__icontains=query) | Q(describe__icontains=query)
            )
        return object_list
