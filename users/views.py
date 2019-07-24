"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView,FormView,UpdateView
from django.contrib.auth import views as auth_views
# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

# Forms
from users.forms import SignupForm


#login_required hereda de esta clase y hereda de LoginRequiredMixin 
class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    #traemos el contexto del user
    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs) #hace el query del object segun los valores que le pasemos
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class SignupView(FormView):
    """Users sign up view"""
    template_name='users/signup.html'
    form_class=SignupForm
    success_url= reverse_lazy('users:login')
    #cada vez que hacemos un FormView hacemos un form_valid
    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form) #que haga la redireccion

@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )

#usamos esta clase para actualizar un perfil
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    #retorna el perfil presente
    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username #object es el profile
        return reverse('users:detail', kwargs={'username': username})

class LoginView(auth_views.LoginView):
    """LoginView"""
    template_name='users/login.html'

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout View"""
    template_name='users/logeed_out.html'

