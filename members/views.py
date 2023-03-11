from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import EditProfileForm, PasswordChangingForm
from .forms import SignUpForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView
from blog.models import Profile
# Create your views here.

#registration form 

class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name =  'registration/register.html'
    success_url = reverse_lazy('login')

class UserChangeView(generic.UpdateView):
    form_class = EditProfileForm
    template_name =  'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    

    def get_object(self):
        return self.request.user
    
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm #this I created
    #form_class = PasswordChangeForm that is from django
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class ShowProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs): 
        # users_profile =  Profile.objects.all()
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)

        # to get data from profile related to specific user 
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user

        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')
    fields = [ 'bio', 'profie_pic', 'facebook_url', 'linkedIn_url', 'instagram_url']


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'
    # fields = '__all__'

    #this function is needed if the user who create a profile is a right one
    #making user available for a profile
    #when we save the form is saved in right user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

