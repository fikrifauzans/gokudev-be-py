from django.db import models
from pygments.lexers import get_all_lexers  # type: ignore
from pygments.styles import get_all_styles  # type: ignore

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class ExampleModel(models.Model):

    string = models.CharField(null=True)
    integer = models.BigIntegerField(null=True)
    

    class Meta:
        ordering = ["created"]
