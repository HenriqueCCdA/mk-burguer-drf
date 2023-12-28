from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from mk_burger.core.models import Bread, Meat, Optional, Status
from mk_burger.core.serializers import IngredientSerializer, StatusSerializer


class IngredientesList(APIView):
    @extend_schema(
        summary="Lista dos ingredientes",
        responses=IngredientSerializer,
    )
    def get(self, request):
        """Lista os igredientes disponiveis na plataforma"""

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


@extend_schema(summary="Lista o status", description="Lista os **status** disponiveis na plataforma")
class StatusList(ListAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


ingredientes_list = IngredientesList.as_view()
status_list = StatusList.as_view()
