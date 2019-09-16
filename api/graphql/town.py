import django_filters
import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from api.models import Town
from .province import ProvinceNode


class TownNode(DjangoObjectType):
    class Meta:
        model = Town
        interfaces = (relay.Node,)


class TownFilter(django_filters.FilterSet):
    class Meta:
        model = Town
        fields = ["id"]


class TownQuery(graphene.ObjectType):
    town = relay.Node.Field(TownNode)
    towns = DjangoFilterConnectionField(TownNode, filterset_class=TownFilter)


class CreateTown(relay.ClientIDMutation):
    town = graphene.Field(TownNode)

    class Input:
        name = graphene.String(required=True)
        province = graphene.ID(requiered=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        province = relay.Node.get_node_from_global_id(
            info, input.get("province"), ProvinceNode
        )
        print(province)
        town = Town(name=input.get("name"), province=province)
        town.save()
        return CreateTown(town=town)


class TownMutation(graphene.ObjectType):
    create_town = CreateTown.Field()
