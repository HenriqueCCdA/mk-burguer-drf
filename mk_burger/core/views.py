from rest_framework.response import Response
from rest_framework.views import APIView

from mk_burger.core.models import Bread, Meat, Optional


class RootView(APIView):
    def get(self, request):
        return Response("Ok")


class IngredientesList(APIView):
    def get(self, request):
        bread_list = Bread.objects.all()
        meat_list = Meat.objects.all()
        optional_list = Optional.objects.all()

        dict_ = {
            "paes": [{"id": item.id, "tipo": item.tipo} for item in bread_list],
            "carnes": [{"id": item.id, "tipo": item.tipo} for item in meat_list],
            "opcionais": [{"id": item.id, "tipo": item.tipo} for item in optional_list],
        }

        return Response(dict_)


ingredientes_list = IngredientesList.as_view()
