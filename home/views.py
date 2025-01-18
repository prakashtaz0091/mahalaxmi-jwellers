from django.shortcuts import render, redirect
import re
from django.contrib import messages
from .forms import EmailForm

def is_valid(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

# def home_view(request):
    
#     # print(request.GET)
#     if request.method == "POST":
#         email = request.POST.get("email")
        
#         if not is_valid(email): #if email is not valid
#             messages.error(request, "Please enter a valid email address.")
#             return redirect("home")
        
#         # send email or do necessary operations
#         print(email)
#         messages.success(request, "Thank your for reaching out. We will get back to you soon.")      
#         return redirect("home")
    
#     return render(request, "home/home.html")


def home_view(request):
    
    # print(request.GET)
    if request.method == "POST":
        emailForm = EmailForm(request.POST, request.FILES)
        
        if not emailForm.is_valid():
            context = {
                'form': emailForm
            }
            return render(request, "home/home.html", context)
        
        # email = emailForm.cleaned_data.get('email')
        # print("Yes the email is valid", email)
        print(emailForm.cleaned_data)
        
        return redirect("home")
    
    
    emailForm = EmailForm()
    
    context = {
        'form':emailForm
    }
    
    return render(request, "home/home.html", context)
