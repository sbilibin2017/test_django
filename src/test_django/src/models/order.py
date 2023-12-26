from config.settings import settings
from django.db.models import ManyToManyField

from .mixins import DatetimeMixin, IdMixin

TABLE_NAME: str = "order"
TABLE_NAME_CAPIRALIZED: str = TABLE_NAME.capitalize()


class Order(IdMixin, DatetimeMixin):
    items: ManyToManyField = ManyToManyField("Item", through="ItemOrder")

    def __str__(self):
        return str(self.id)

    class Meta:  # type: ignore
        db_table = '{schema}"."{table_name}'.format(
            schema=settings.db.schema, table_name=TABLE_NAME
        )
        verbose_name = TABLE_NAME_CAPIRALIZED
        verbose_name_plural = TABLE_NAME_CAPIRALIZED + "s"
