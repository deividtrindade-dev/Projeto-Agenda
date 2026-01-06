from django.shortcuts import get_list_or_404, get_object_or_404, render
from contact.models import Contact
from django.http import Http404
def index (request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[10:20]

    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact (request, contact_id):
    # single_contact = Contact.objects.filter(id=contact_id).last()
    single_contact = get_object_or_404(Contact, id=contact_id, show=True)

    context = {
        'contact': single_contact,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )

