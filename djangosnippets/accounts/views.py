from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.
class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = '/'

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"]
        )
        login(self.request, user)
        return to_return
