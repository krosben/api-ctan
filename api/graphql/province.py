import django_filters
import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from api.models import Province


class ProvinceNode(DjangoObjectType):
    class Meta:
        model = Province
        interfaces = (relay.Node,)


class ProvinceFilter(django_filters.FilterSet):
    class Meta:
        model = Province
        fields = ["id"]


class ProvinceQuery(graphene.ObjectType):
    province = relay.Node.Field(ProvinceNode)
    provinces = DjangoFilterConnectionField(
        ProvinceNode, filterset_class=ProvinceFilter
    )


class CreateProvince(relay.ClientIDMutation):
    province = graphene.Field(ProvinceNode)

    class Input:
        name = graphene.String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        province = Province(name=input.get("name"))
        province.save()
        return CreateProvince(province=province)


class ProvinceMutation(graphene.ObjectType):
    create_province = CreateProvince.Field()
