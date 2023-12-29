from django.urls import path

from mk_burger.core.views import burger_lc, burger_rud, ingredientes_list, status_list

app_name = "core"
urlpatterns = [
    path("ingredientes/", ingredientes_list, name="ingredientes"),
    path("status/", status_list, name="status"),
    path("burgers/", burger_lc, name="burger-list-create"),
    path("burgers/<int:pk>/", burger_rud, name="burger-retrieve-update-destroy"),
]
