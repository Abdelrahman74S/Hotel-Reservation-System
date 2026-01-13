from django.shortcuts import render , redirect
from .forms import UserForm , UserRegisterForm
from .models import User
from django.contrib.auth.views import LoginView 
from django.views.generic  import CreateView, DetailView ,UpdateView
from django.contrib.auth import  login , logout 
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

@login_required
def LogoutView(request):
    logout(request)
    return redirect('login')


class UserProfileView(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return self.request.user

class UserProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UserForm
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


def home_view(request):
    context = {
        'name': 'World',
        'items': ['apple', 'banana', 'cherry']
    }
    # The render() function loads the template and passes the context
    return render(request, 'home.html', context)