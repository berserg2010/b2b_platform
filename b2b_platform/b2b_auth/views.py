from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


class SignUpFormView(FormView):

    form_class = UserCreationForm
    template_name = "b2b_auth/sign_up.html"
    success_url = '/private_side/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SignInFormView(FormView):

    form_class = AuthenticationForm
    template_name = 'b2b_auth/sign_in.html'
    success_url = '/private_side/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)


class SignOutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
