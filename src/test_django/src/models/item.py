from config.settings import settings
from django.db.models import IntegerField

from .mixins import DatetimeMixin, DescriptionMixin, IdMixin, NameMixin

TABLE_NAME: str = "item"
TABLE_NAME_CAPIRALIZED: str = TABLE_NAME.capitalize()


class Item(IdMixin, NameMixin, DatetimeMixin, DescriptionMixin):
    price: IntegerField = IntegerField()

    def __str__(self):
        return str(self.name)

    class Meta:  # type: ignore
        db_table = '{schema}"."{table_name}'.format(
            schema=settings.db.schema, table_name=TABLE_NAME
        )
        verbose_name = TABLE_NAME_CAPIRALIZED
        verbose_name_plural = TABLE_NAME_CAPIRALIZED + "s"
