from django.db import models

VEGAN_LEVEL = (
    (3, "Vegan"),
    (2, "Vegetarian"),
    (1, "Veggie Friendly"),
)


def menu_path(instance):
    """Return menu path.

    'menues/id of particular restaurant'
    """
    return "menus/{}".format(instance.id)


class Restaurants(models.Model):
    """Restaurant Model."""

    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250, unique=True)
    location = models.PointField(max_length=40, null=True)
    hours = models.CharField(max_length=250)
    how_vegan = models.CharField(max_length=250, choices=VEGAN_LEVEL)
    website = models.CharField(max_length=250)
    summary = models.CharField(max_length=250, null=True, blank=True)
    menu = models.FileField(upload_to=menu_path, null=True, blank=True)

    objects = models.Manager()
