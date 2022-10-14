from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


def profile_view(request):
    print('---', request.user)
    return render(request, 'account/profile.html')


class UpdateProfileView(generic.UpdateView):
    form_class = CustomUserChangeForm
    template_name = 'account/profile.html'
    model = get_user_model()

    def get_object(self, queryset=None):
        # return get_user_model().objects.get(pk=self.request.user.pk)
        return get_object_or_404(
            get_user_model(),
            pk=self.request.user.pk,
        )
