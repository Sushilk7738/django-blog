from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Blog, Category

def posts_by_category(request, category_id):
    #fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status = 'Published', category = category_id)

    #* use try/except when we want to do some custom actions if category not exist
    # try:
    #     category = Category.objects.get(pk = category_id)
    # except:
        # redirect the user to home page
        # return redirect('home')

    #* Use get_object_or_404 when you want to show 404 page
    category = get_object_or_404(Category, pk = category_id)
    
    context = {
        'posts' : posts,
        'category' :  category,
    }
    return render(request, 'posts_by_category.html', context)