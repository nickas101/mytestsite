from django.shortcuts import render
from django.views import generic

# Create your views here.

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # # Генерация "количеств" некоторых главных объектов
    # num_books=Book.objects.all().count()
    # num_instances=BookInstance.objects.all().count()
    # # Доступные книги (статус = 'a')
    # num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    # num_authors=Author.objects.count()  # Метод 'all()' применен по умолчанию.
    
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books':5,'num_instances':7,'num_instances_available':3,'num_authors':4},
    )

class BookListView(generic.ListView):
    pass
    # model = Book