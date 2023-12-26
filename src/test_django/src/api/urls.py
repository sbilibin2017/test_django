from django.urls import include, path  # type: ignore

urlpatterns = [
    path("v1/", include("src.api.v1.urls")),
]
