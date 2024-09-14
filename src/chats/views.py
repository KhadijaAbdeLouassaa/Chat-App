from django.shortcuts import render,redirect

# Create your views here.


def index(request, *args, **kwargs):
    if not request.user.is_authenticated :
        
        return redirect("users:login")
    context = {}
    return render(request,'chats/index.html', context)
    
    
