from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from mk_burger.core.models import Bread, Meat, Optional
from mk_burger.core.serializers import IngredientSerializer


class IngredientesList(APIView):
    @extend_schema(
        responses=IngredientSerializer,
    )
    def get(self, request):
        """Lista os igredientes"""

        bread_list = Bread.objects.all()
        meat_list = Meat.objects.all()
        optional_list = Optional.objects.all()

        serializer = IngredientSerializer(
            {
                "paes": bread_list,
                "carnes": meat_list,
                "opcionais": optional_list,
            }
        )
        return Response(serializer.data)


ingredientes_list = IngredientesList.as_view()
