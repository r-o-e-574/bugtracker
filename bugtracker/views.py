from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from bugtracker import forms
from bugtracker import  models

# Create your views here.
@login_required
def index_view(request):
    tickets = models.Ticket.objects.all()
    new_tickets = tickets.filter(status_of_ticket='N')
    inprogress_tickets = tickets.filter(status_of_ticket='P')
    done_tickets = tickets.filter(status_of_ticket='D')
    invalid_tickets = tickets.filter(status_of_ticket='I')
    return render(request, "index.html",
                  {"Welcome": "Bugtracker",
                   "tickets": tickets,
                   "new_tickets": new_tickets,
                   "inprogress_tickets": inprogress_tickets,
                   "done_tickets": done_tickets,
                   "invalid_tickets": invalid_tickets,
                   })


@login_required
def ticket_detail(request, ticket_id):
    ticket = models.Ticket.objects.filter(id=ticket_id).first()
    return render(request, "ticket.html", {"ticket": ticket})


@login_required
def user_detail(request, user_id):
    selected_user = models.MyUser.objects.filter(id=user_id).first()
    ticket_list = models.Ticket.objects.filter(name_of_user=selected_user)
    new_tickets = ticket_list.filter(status_of_ticket='N')
    inprogress_tickets = ticket_list.filter(status_of_ticket='P')
    done_tickets = ticket_list.filter(status_of_ticket='D')
    invalid_tickets = ticket_list.filter(status_of_ticket='I')
    return render(request, "user_tickets.html",
                  {"selected_user": selected_user,
                   "new_tickets": new_tickets,
                   "inprogress_tickets": inprogress_tickets,
                   "done_tickets": done_tickets,
                   "invalid_tickets": invalid_tickets,
                   })



def add_ticket(request):
    if request.method == "POST":
        form = forms.AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            models.Ticket.objects.create(
                title = data.get("title"),
                description = data.get("description"),
                name_of_user = request.user
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = forms.AddTicketForm()
    return render(request, "generic_form.html", {"form": form})


@login_required
def edit_ticket(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    if request.method == "POST":
        form = forms.AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data["title"]
            ticket.description = data["description"]
            ticket.save()
        return HttpResponseRedirect(reverse("ticket_view", args=[ticket.id]))
    
    data = {
        "title": ticket.title,
        "description": ticket.description
    }
    form = forms.AddTicketForm(initial=data)
    return render(request, "generic_form.html", {"form": form})


@login_required
def ticket_inprogress(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    ticket.status_of_ticket = 'P'
    ticket.completed_by = None
    if request.method == "POST":
        form = forms.AssignTicket(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.user_assigned = data["user_assigned"]
            ticket.save()
        return HttpResponseRedirect(reverse("ticket_view", args=[ticket.id]))
    data = {
        "Assigned User": ticket.user_assigned
    }
    form = forms.AssignTicket(initial=data)
    return render(request, "generic_form.html", {"form": form})


def ticket_completed(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    ticket.status_of_ticket = 'D'
    ticket.completed_by = ticket.user_assigned
    ticket.user_assigned = None
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def ticket_invalid(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    ticket.status_of_ticket = 'I'
    ticket.user_assigned = None
    ticket.completed_by = None
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
            
    form = forms.LoginForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))