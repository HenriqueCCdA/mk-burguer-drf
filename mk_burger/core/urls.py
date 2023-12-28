from django.urls import path

from .views import RootView, ingredientes_list

app_name = "core"
urlpatterns = [
    path("", RootView.as_view(), name="root"),
    path("ingredientes/", ingredientes_list, name="ingredientes"),
]
