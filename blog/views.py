from django.shortcuts import render, redirect, get_object_or_404
# get an object if it does not exits return 404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Create View
# from .forms import PostStructure
from .models import Fields, Add_comment
from .forms import FillInForms, EditForms, AddCommentForm

# Sign up view
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
# CreateView # bring it back the way it set to datatbase.
from django.urls import reverse_lazy


def home(request):
    field = Fields.objects.all().order_by('-updated_on')
    return render(request, 'index.html', {'field': field})


# ordering by id


# Id part for next page
def detail(request, title_id):
    # look up the code
    # Grabe th id from Fields look up the id of that blog
    # assign to stuffs that take total like and get calculate it
    # thing = get_object_or_404(Fields, pk=title_id)
    title = get_object_or_404(Fields, pk=title_id)
    total_like = title.total_likes()  # from model

    # request user id and pass unlike variable in context
    unlike = False
    if title.like.filter(id=request.user.id).exists():
        unlike = True
    context = {
        'title': title,
        'total_like': total_like,
        'unlike': unlike,

    }
    return render(request, 'detail.html', context)


# to make sure only logged-in can add a blog
@login_required
def fill_in_form(request):
    if request.method == "POST":
        form = FillInForms(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog:user_blog', title_id=post.pk,
                            author_name=post.user.username)  # redirect to a success page or the list of fields
    else:
        form = FillInForms()
    return render(request, 'form.html', {'form': form})


from django.contrib.auth.decorators import login_required


# To redirect to that specific page belong to that user with id/author name urls
@login_required
def user_blog(request, title_id, author_name):
    title = get_object_or_404(Fields,
                              pk=title_id)  # View logic: checking th author name from the urls mach the username of the associated user this will ensure only the rig user can access
    if title.user.username != author_name or title.user != request.user:  # with this changes, The URL for user blog will included both the 'title_id' and 'author_name'
        raise Http404("You don't have permission to view this post.")
    return render(request, 'user_blog.html', {'title': title})


# Signup View
def signup(request):
    if request.method == 'POST':
        form_signup = UserCreationForm(request.POST)
        if form_signup.is_valid():
            form_signup.save()
            return redirect('login')  # redirect to login after sign up
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form_signup': form_signup})


def user_logout(request):
    return LogoutView.as_view(next_page='blog:home')(request)


# Test Delete later
class Home(ListView):
    model = Fields
    template_name = 'post.html'


# Test Delete later
class Detaisl_View(DetailView):
    model = Fields
    template_name = 'post_create.html'


# class AddPost(CreateView):
#     model = Fields
#     template_name = 'form.html'
#     fields = '__all__'

# Build in class edit post
class EditPostView(UpdateView):
    model = Fields
    form_class = EditForms
    template_name = 'update_blog.html'

    # If you're using 'pk' or 'slug' in your URL patterns, you do not need to override get_object.
    # However, if you have a custom URL pattern, you would override it like so:
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')  # This should match the keyword used in your URL pattern
        return get_object_or_404(Fields, pk=pk)

    # Define this method if you want to customize the success URL.
    def get_success_url(self):
        # Make sure the keyword argument matches what's expected in your URL pattern
        return reverse('blog:detail', kwargs={'title_id': self.object.pk})

    #     # Assuming self.object is the post object and has an 'id' attribute


class DeletePostView(DeleteView):
    model = Fields
    # success_url = reverse_lazy('blog:home')
    template_name = 'delete_blog.html'

    def get_success_url(self):
        # You can include any logic you want here to determine the correct success URL.
        return reverse('blog:home')  #


def LikeView(request, pk):
    title = get_object_or_404(Fields, id=request.POST.get('title_id'))
    #     Whta ever title id is that looks up in that post and assign to post variable and save to the table
    #     We savinh a like from the user to see who like thi spost

    # pass in the request and request contain user id for login. If we login look up whether like has been like by user 1
    #     If clicked and if it except then we want to unlike the post and remove by user
    if title.like.filter(id=request.user.id).exists():
        title.like.remove(request.user)
    else:
        title.like.add(request.user)
    # if it doesn' alreay exit then we just add the like an dchenge like to True and add like as Fale
    # After unlike like will be false . after like it like will be true

    # title.like.add(request.user)
    # redirect to the same page, instaed of returning render request or return lazy. first import Http
    return HttpResponseRedirect(reverse('blog:detail', args=[str(pk)]))

# Add comment
class AddCommentpage(CreateView):
    model = Add_comment
    form_class = AddCommentForm
    template_name = 'post_comment.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.post_title_id = self.kwargs['pk']

        return super().form_valid(form)
    success_url = reverse_lazy('blog:home')
# In your AddCommentpage class view, you are setting form.instance.id = self.kwargs['pk'], but you should be setting the post_title_id since id would refer to the primary key of the Add_comment instance (which is auto-generated).