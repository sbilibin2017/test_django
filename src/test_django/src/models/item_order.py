from config.settings import settings
from django.db.models import CASCADE, ForeignKey

from .mixins import DatetimeMixin, IdMixin

TABLE_NAME: str = "item_order"
TABLE_NAME_CAPIRALIZED: str = TABLE_NAME.capitalize()


class ItemOrder(IdMixin, DatetimeMixin):
    item_id: ForeignKey = ForeignKey(
        "Item",
        on_delete=CASCADE,
        db_column="item_id",
    )
    order_id: ForeignKey = ForeignKey(
        "Order",
        on_delete=CASCADE,
        db_column="order_id",
    )

    def __str__(self):
        return "iteam_id-order_id: {item_id}-{order_id}".format(
            item_id=str(self.item_id), order_id=str(self.order_id)
        )

    class Meta:  # type: ignore
        db_table = '{schema}"."{table_name}'.format(
            schema=settings.db.schema, table_name=TABLE_NAME
        )
        verbose_name = TABLE_NAME_CAPIRALIZED
        verbose_name_plural = TABLE_NAME_CAPIRALIZED + "s"
