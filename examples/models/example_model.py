from django.db import models
from pygments.lexers import get_all_lexers  # type: ignore
from pygments.styles import get_all_styles  # type: ignore


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class ExampleModel(models.Model):

    id = models.AutoField(primary_key=True)
    string = models.CharField(null=True)
    text = models.TextField(null=True)
    smallint = models.SmallIntegerField(null=True)
    integer = models.IntegerField(null=True)
    biginteger = models.BigIntegerField(null=True)
    boolean = models.BooleanField(null=False, default=False)
    date = models.DateField(null=True)
    datetime = models.DateTimeField(null=True)
    time = models.TimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    created_by = models.BigIntegerField(null=True)
    updated_by = models.BigIntegerField(null=True)
    deleted_by = models.BigIntegerField(null=True)

    class Meta:
        db_table = 'examples_example_table'
        ordering = ["created_by"]
        verbose_name = "Example Model"
        verbose_name_plural = "Example Models"
