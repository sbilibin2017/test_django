from django.db.models import Model, TextField


class DescriptionMixin(Model):
    description: TextField = TextField(
        max_length=255,
        null=True,
        blank=True,
        default="",
        verbose_name="desription",
    )

    class Meta:
        abstract = True
