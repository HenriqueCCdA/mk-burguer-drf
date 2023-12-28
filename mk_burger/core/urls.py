from django.urls import path

from mk_burger.core.views import ingredientes_list

app_name = "core"
urlpatterns = [
    path("ingredientes/", ingredientes_list, name="ingredientes"),
]
