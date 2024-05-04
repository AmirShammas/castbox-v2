def create_episode_mention(sender, instance, created, **kwargs):
    from mention.models import Mention
    from profilee.models import Profile
    if created:
        for follow in instance.channel.follows.all():
            new_mention = Mention.objects.create(
                user=follow.user, message=f"A new episode '{instance.title}' created in channel '{instance.channel.title}' !!", channel=instance.channel, episode=instance)
            profile = Profile.objects.get(owner=follow.user)
            profile.mention.add(new_mention)


def create_user_profile(sender, instance, created, **kwargs):
    from profilee.models import Profile
    if created:
        Profile.objects.create(owner=instance)


def create_default_playlist(sender, instance, created, **kwargs):
    from playlist.models import Playlist
    from profilee.models import Profile
    if created:
        new_playlist = Playlist.objects.create(
            user=instance, title="default-playlist")
        profile = Profile.objects.get(owner=instance)
        profile.playlist.add(new_playlist)
