from config.settings import settings

from .mixins import (DatetimeMixin, DescriptionMixin, FloatMixin, IdMixin,
                     NameMixin,)

TABLE_NAME: str = "tax"
TABLE_NAME_CAPIRALIZED: str = TABLE_NAME.capitalize()


class Tax(IdMixin, NameMixin, DatetimeMixin, DescriptionMixin, FloatMixin):
    def __str__(self):
        return str(self.name)

    class Meta:  # type: ignore
        db_table = '{schema}"."{table_name}'.format(
            schema=settings.db.schema, table_name=TABLE_NAME
        )
        verbose_name = TABLE_NAME_CAPIRALIZED
        verbose_name_plural = TABLE_NAME_CAPIRALIZED + "s"
