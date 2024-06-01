from django.shortcuts import render
from .models import Genre, Book
# Create your views here.



def home(request):
    books = Book.objects.all()
    context = {
        "BOOKS": books
    }
    return render(request, "imaginary/book.html", context)

