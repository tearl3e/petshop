from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .forms import SearchForm


def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def petmart(request):
    categories = Category.objects.all()
    pro = Product.objects.all()
    return render(request, 'petmart.html', {'pro': pro, 'categories': categories})


def all(request):
    categories = Category.objects.all()
    pro = Product.objects.all()
    return render(request, 'all.html', {'pro': pro, 'categories': categories})


def search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Product.objects.filter(name__startswith=query)
    return render(request, 'search.html', {'form': form, 'query': query, 'results': results})


def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})
