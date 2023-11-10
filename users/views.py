from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfilePage, PageForm
from django.views.generic import DetailView, CreateView
from blog.models import Profile

# Create your views here.
class UserRegisterPageView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class UserEditPageView(generic.UpdateView):
    form_class = EditProfilePage
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('blog:home')

    def get_object(self):
        return self.request.user

# Create profile page
class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/profile_page.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        # page_user = get_object_or_404(Profile, id=self.kwargs['pk']) #geting part to url
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context

class EditProfilePage(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page_for_user.html'
    fields = ['bio','picture_profile','facebook_url',  'twitter_url', 'instagram_url']
    success_url = reverse_lazy('blog:home')

class CreateProfilePageForUser(CreateView):
    model = Profile
    form_class = PageForm #tell view that we are using that form
    template_name = "registration/create_profile_page_for_user.html"
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
#     there is a user fill out the form make it available for the form it self then save the form by return super and pass it form.
# make user id available so when we save the form it save under the right user take 7 put the form as user then set the form


