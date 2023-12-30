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

        bread_list = Bread.objects.filter(is_active=True)
        meat_list = Meat.objects.filter(is_active=True)
        optional_list = Optional.objects.filter(is_active=True)

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
    queryset = Status.objects.filter(is_active=True)

    @extend_schema(
        summary="Lista dos status",
    )
    def get(self, request, *args, **kwargs):
        """Retorna os status disponiveis na plataforma"""
        return super().get(request, *args, **kwargs)


class BurgerLC(ListCreateAPIView):
    serializer_class = BurgerSerializer
    queryset = Burger.objects.filter(is_active=True)

    @extend_schema(
        summary="Lista dos Hamburguers",
    )
    def get(self, request, *args, **kwargs):
        """Retorna a lista de pedidos de hamburgers"""
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Cria um Hamburguer",
    )
    def post(self, request, *args, **kwargs):
        """Cria de pedido de um hamburgers"""
        return super().post(request, *args, **kwargs)


class BurgerRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = BurgerSerializer
    queryset = Burger.objects.filter(is_active=True)

    @extend_schema(
        summary="Le um Hamburguers",
    )
    def get(self, request, *args, **kwargs):
        """Le um hamburger pelo id"""
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Autalização parcial de um Hamburguers",
    )
    def patch(self, request, *args, **kwargs):
        """Atualiza um hamburger pelo id"""
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        summary="Autalização de um Hamburguers",
    )
    def put(self, request, *args, **kwargs):
        """Atualiza um hamburger pelo id"""
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary="Deleta um Hamburguers",
    )
    def delete(self, request, *args, **kwargs):
        """Deleta um hamburger pelo id"""
        return super().delete(request, *args, **kwargs)


ingredientes_list = IngredientesList.as_view()
status_list = StatusList.as_view()
burger_lc = BurgerLC.as_view()
burger_rud = BurgerRUD.as_view()
