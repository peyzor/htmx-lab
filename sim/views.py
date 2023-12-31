from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from sim.forms import SampleForm, ContactForm
from sim.models import Person, Article


def sample_post(request, *args, **kwargs):
    form = SampleForm(request.POST or None)

    if form.is_valid():
        # form.cleaned_data now contains the validated data
        print(f'{ form.cleaned_data= }')
        return HttpResponse('<p class="success">Form submitted successfully! ✅</p>')
    else:
        # form.errors contains the form validation errors
        return HttpResponse(
            f'<p class="error">Your form submission was unsuccessful ❌. '
            f'Please would you correct the errors? The current errors: {form.errors}</p>')


def example(request):
    return render(request, 'example.html')


def search_view(request):
    all_people = Person.objects.all()
    context = {'count': all_people.count()}
    return render(request, 'search.html', context)


def search_results_view(request):
    query = request.GET.get('search', '')
    print(f'{query = }')

    all_people = Person.objects.all()
    if query:
        people = all_people.filter(name__icontains=query)
    else:
        people = []

    context = {'people': people, 'count': all_people.count()}
    return render(request, 'search_results.html', context)


def articles(request):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(Article.objects.all(), 10)
    page_obj = paginator.get_page(page_number)

    return render(request, 'articles.html', {'page_obj': page_obj})


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'htmx_contact_form_confirm.html')
    else:
        form = ContactForm()

    return render(request, 'htmx_contact_form.html', {'contact_form': form})
