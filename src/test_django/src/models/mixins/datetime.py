from django.db.models import DateTimeField, Model


class DatetimeMixin(Model):
    created_at: DateTimeField = DateTimeField(
        auto_now_add=True, verbose_name="created_at"
    )
    updated_at: DateTimeField = DateTimeField(
        auto_now=True, null=True, verbose_name="updated_at"
    )

    class Meta:
        abstract = True
