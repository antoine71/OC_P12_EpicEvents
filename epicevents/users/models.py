from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Default user for epicevents."""

    pass

    # #: First and last name do not cover name patterns around the globe
    # name = CharField(_("Name of User"), blank=True, max_length=255)
    # first_name = None  # type: ignore
    # last_name = None  # type: ignore
