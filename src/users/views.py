from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm,EditProfileForm
from .models import UserProfile
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

class SignupView(CreateView):
    form_class = UserForm
    template_name = "users/signup.html"
    success_url = "/"
    
@login_required    
def edit_profile(request):
    if request.method == "POST" :
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect("chats:index")
    else :
        form = EditProfileForm(instance=request.user.userprofile)
    return render(request, "users/profile.html", {'form':form})        