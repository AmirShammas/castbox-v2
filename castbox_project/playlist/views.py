from django.utils.decorators import method_decorator
from forms.forms import SelectPlaylistForm
from permissions.permissions import channel_episode_required
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Playlist
from episode.models import Episode
from django.urls import reverse
from django.http import HttpResponseRedirect


@method_decorator(channel_episode_required, name='dispatch')
class EpisodeSelectPlaylistView(LoginRequiredMixin, FormView):
    template_name = 'episodes/episode_select_playlist.html'
    form_class = SelectPlaylistForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        playlist_id = form.cleaned_data['playlist']
        episode_id = self.kwargs['pk']
        playlist = Playlist.objects.get(pk=playlist_id)
        episode = Episode.objects.get(pk=episode_id)

        if episode in playlist.episode.all():
            return HttpResponseRedirect(reverse('episode_detail', kwargs={'channel_id': self.kwargs['channel_id'], 'pk': self.kwargs['pk']}))

        playlist.episode.add(episode)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('episode_detail', kwargs={'channel_id': self.kwargs['channel_id'], 'pk': self.kwargs['pk']})

