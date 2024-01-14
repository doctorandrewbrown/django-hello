from django.db import models


# Item class inherits from Model class in models module imported above.
class Item(models.Model):
    # blank=False stops blank fields submitting in web forms.
    # null=False prevents null values entering database
    # from other places like admin panel
    name = models.CharField(max_length=50, blank=False, null=False)
    done = models.BooleanField(default=False, blank=False, null=False)

    # String repr giving model name
    def __str__(self):
        return (self.name)
