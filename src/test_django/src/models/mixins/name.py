from django.db.models import CharField, Model


class NameMixin(Model):
    name: CharField = CharField(
        max_length=255, null=True, blank=True, default="", verbose_name="name"
    )

    class Meta:
        abstract = True
