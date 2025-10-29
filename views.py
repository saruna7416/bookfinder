from django.shortcuts import render

# Create your views here.
import requests


def search_books(request):
    books = []
    if 'q' in request.GET:
        query = request.GET['q']
        url = f"https://openlibrary.org/search.json?title={query}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            books = data['docs']
    return render(request, 'books.html', {'books': books})
