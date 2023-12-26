from typing import cast  # type: ignore

from django.apps import apps as app  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework.views import APIView  # type: ignore
from src.apps import SrcConfig  # type: ignore
from src.interfaces import IService  # type: ignore
from utils.di_container import inject  # type: ignore

app_config: SrcConfig = cast(SrcConfig, app.get_containing_app_config("src"))
di_container = app_config.di_container


class ItemView(APIView):
    @inject(di_container)
    def get(self, request, service: IService):
        print(service.say_hello())
        return Response("hello")
