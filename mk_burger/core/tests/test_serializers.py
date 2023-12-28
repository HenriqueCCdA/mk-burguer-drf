from mk_burger.core.serializers import (
    BreadSerializer,
    IngredientSerializer,
    MeatSerializer,
    OptionalSerializer,
    StatusSerializer,
)


def test_serializer_breads(bread_list):
    serializer = BreadSerializer(instance=bread_list, many=True)

    for d, e in zip(bread_list, serializer.data):
        assert e["id"] == d.id
        assert e["tipo"] == d.tipo


def test_serializer_meats(meat_list):
    serializer = MeatSerializer(instance=meat_list, many=True)

    for d, e in zip(meat_list, serializer.data):
        assert e["id"] == d.id
        assert e["tipo"] == d.tipo


def test_serializer_optionais(optionais):
    serializer = OptionalSerializer(instance=optionais, many=True)

    for d, e in zip(optionais, serializer.data):
        assert e["id"] == d.id
        assert e["tipo"] == d.tipo


def test_serializer_status(status_list):
    serializer = StatusSerializer(instance=status_list, many=True)

    for d, e in zip(status_list, serializer.data):
        assert e["id"] == d.id
        assert e["tipo"] == d.tipo


def test_serializer_igredientes(bread_list, meat_list, optionais):
    serializer = IngredientSerializer({"paes": bread_list, "carnes": meat_list, "opcionais": optionais})

    assert len(serializer.data["paes"]) == len(bread_list)
    assert len(serializer.data["carnes"]) == len(meat_list)
    assert len(serializer.data["opcionais"]) == len(optionais)
