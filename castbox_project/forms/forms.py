from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class SelectPlaylistForm(LoginRequiredMixin, forms.Form):
    playlist = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(SelectPlaylistForm, self).__init__(*args, **kwargs)
        self.fields['playlist'].choices = [
            (playlist.id, playlist.title) for playlist in user.playlists.all()]


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )
