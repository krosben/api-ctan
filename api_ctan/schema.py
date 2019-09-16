import graphene
from django.conf import settings
from graphene_django.debug import DjangoDebug

from api.graphql import ProvinceQuery, ProvinceMutation, TownQuery, TownMutation


class Query(ProvinceQuery, TownQuery):
    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(ProvinceMutation, TownMutation):
    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query, mutation=Mutation)
