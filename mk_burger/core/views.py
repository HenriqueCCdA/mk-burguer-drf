from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from mk_burger.core.models import Bread, Burger, Meat, Optional, Status
from mk_burger.core.serializers import BurgerSerializer, IngredientSerializer, StatusSerializer


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


class StatusList(ListAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class BurgerLC(ListCreateAPIView):
    serializer_class = BurgerSerializer
    queryset = Burger.objects.all()


class BurgerRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = BurgerSerializer
    queryset = Burger.objects.all()


ingredientes_list = IngredientesList.as_view()
status_list = StatusList.as_view()
burger_lc = BurgerLC.as_view()
burger_rud = BurgerRUD.as_view()
