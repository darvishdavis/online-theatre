from django.http import HttpResponse
from . models import Movies
from django.shortcuts import render, redirect
from .forms import FilmForm


# Create your views here.
def default(request):
    movie = Movies.objects.all
    context = {'movie_dictionary': movie}
    return render(request, 'home.html', context)

def home(request):
    movie = Movies.objects.all
    context = {'movie_dictionary': movie}
    return render(request, 'home.html', context)

def movie(request, film_id):
    movie = Movies.objects.all
    context = {'movie_dictionary': movie, 'id': film_id}
    return render(request, 'details.html', context)


def add(request):
    if request.method == 'POST':
        m_title=request.POST.get('title')
        m_desc = request.POST.get('description')
        m_year=request.POST.get('year')
        m_image = request.FILES['image']
        adding= Movies(title=m_title, description=m_desc, year=m_year, image=m_image)
        adding.save()
        return redirect("/home")

    return render(request, 'add.html')

def edit(request,film_id):
    old_details = Movies.objects.get(id=film_id)
    new_details = FilmForm(request.POST or None, request.FILES, instance=old_details)
    if new_details.is_valid():
        new_details.save()
        return redirect("/home")
    return render(request, 'edit.html', {'old': old_details, 'new': new_details})

def delete(request, film_id):
    delete_details = Movies.objects.get(id=film_id)
    delete_details.delete()
    render(request, "delete.html")
    return redirect("/home")

