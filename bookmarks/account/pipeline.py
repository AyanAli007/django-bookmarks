from .models import Profile


def create_user_profile(backend, user, response, *args, **kwargs):
    """
    Create a Profile for users that register via social authentication.
    """
    if backend.name == 'google-oauth2':
        Profile.objects.get_or_create(user=user)
