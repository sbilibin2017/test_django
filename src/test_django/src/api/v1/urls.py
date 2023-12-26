from django.urls import path  # type: ignore

from .item import ItemView  # type: ignore

urlpatterns = [
    path("item/", ItemView.as_view()),
]
