from django.shortcuts import render, redirect
from product.models import Category,Drink  

def home(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'index.html', {'categories':categories})
    
    if request.method == 'POST':
        category = request.POST.get('coffee','')
        categories = Category.objects.all()
        if category == '':
            return render(request, 'index.html', {'categories':categories})
        category_get = Category.objects.get(name=category)
        drinks = Drink.objects.filter(category=category_get)
        return render(request, 'index.html', {'drinks': drinks, 'categories':categories})