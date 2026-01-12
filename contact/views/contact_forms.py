from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact
from django.http import Http404


def create (request):
    context = {

    }
    return render(
        request,
        'contact/create.html',
        context
    )