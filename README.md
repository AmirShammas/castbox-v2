# Castbox-Project

This app creates a website about the podcasts using Django templates and sqlite database.

## Installation

This app is developed using python 3.11.

After making venv, install the necessary packages using the command below:

```
pip install -r requirements.txt
```

Copy `sample_settings.py` file and rename it to `local_settings.py`.

To generate the secret key, run the command below:

```
py -c "import secrets; print(secrets.token_urlsafe())"
```

Copy and paste this new value into the `local_settings.py` under the variable `SECRET_KEY`.

Run migrations:

```
py manage.py makemigrations

py manage.py migrate
```

Run the server:

```
py manage.py runserver
```

## Permissions

You have not access to any endpoint without authentication.

After sign-up as a regular-user, you have limited access to endpoints.

Only the super-user has access to `log` endpoint.

## Usage

The user can watch channels list and each channel's details, follow or unfollow a channel and receive a mention message when a new episode is created in this channel, create or update or delete a comment for a channel, watch the episodes list and an episode's details, add or remove an episode in default-playlist, create a new playlist and add or remove the episodes for it, create a new channel and update or delete this channel, watch the number of followers for this channel, create a new episode for this new channel, watch the number of likes for this episode, update or delete this new episode.

When the user wathes a channel's detail page or plays an episode, a log message will be automatically created. The super-user can watch these logs via a link in the header of his home page.

## TODO

- [x] make the project modular
- [ ] complete admin panel
- [ ] upload audio file in episode
- [ ] upload user photo in profile
- [ ] change or reset password in profile
- [ ] change email or username in profile
- [ ] delete account in profile
- [ ] email must be unique in customuser table
- [ ] remove title from comment model
- [ ] change null=True and blank=True in models
- [ ] user can not delete his default-playlist
- [ ] user can not follow his own channel
- [ ] user can not like his own episode
- [ ] user sends a ticket to super-user and receives the answer
