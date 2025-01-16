from django.shortcuts import render


def blog_view(request):
    
    blogs = [
        {
            "title": "Blog 1",
            "desc": "Blog 1 Description",
        },
        {
            "title": "Blog 3",
            "desc": "Blog 3 Description",
        },
        {
            "title": "Blog 2",
            "desc": "Blog 2 Description",
        },
        {
            "title": "Blog 4",
            "desc": "Blog 4 Description",
        },
    ]
    
    
    context = {
        'blogs': blogs
    }
    
    return render(request, "blog/blog.html", context)