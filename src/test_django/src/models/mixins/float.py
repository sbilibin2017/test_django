from django.db.models import FloatField, Model


class FloatMixin(Model):
    value: FloatField = FloatField(verbose_name="value")

    class Meta:
        abstract = True
