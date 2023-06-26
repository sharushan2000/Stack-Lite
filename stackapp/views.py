from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TicketForm,CommentForm
from django.views.generic.list import ListView
from .models import Ticket,Comment
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

@login_required
def discussion(request, id):
    obj = Ticket.objects.get(pk=id)
    comments = Comment.objects.filter(solution_for_id=id)
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.solution_for = obj
            comment.user = request.user
            comment.save()
            return redirect("stackapp:discussion", id=id)

    else:
        form = CommentForm()
    
    context = {
        "object": obj,
        "form": form,
        "comments": comments
    }
    return render(request, 'stackapp/discussion.html', context)



@login_required
def solution(request,id):
    cmt = Comment.objects.get(pk=id)
    context = {'comment':cmt}
    return render(request,'stackapp/solution.html',context)

