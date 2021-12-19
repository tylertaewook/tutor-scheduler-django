from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from scheduler.models import Session
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# TODO: setup o_auth to login with google feature
# REF: https://www.section.io/engineering-education/django-google-oauth/


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created! You can now login"
            )
            return redirect("login")
    else:  # displays empty form initially
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    student = request.user
    context = {
        "user_sessions": Session.objects.filter(student=student),
        "teacher_sessions": Session.objects.all(),
    }
    return render(request, "users/profile.html", context)


class SessionEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Session
    fields = ["date", "timeblock", "helptype"]

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        session = self.get_object()
        if self.request.user == session.student:
            return True
        return False


class SessionCancelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Session
    success_url = "/"

    def test_func(self):
        session = self.get_object()
        if self.request.user == session.student:
            return True
        return False


@login_required
def editprofile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated.")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "users/editprofile.html", context)

