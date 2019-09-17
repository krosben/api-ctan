from graphene import relay
from graphene.test import Client
from api_ctan.schema import schema


client = Client(schema=schema)


def test_query_provinces(snapshot):
    query = """
    {
        provinces {
            edges {
                node {
                    id
                    name
                }
            }
        }
    }
    """
    snapshot.assert_match(client.execute(query))


def test_query_province(snapshot):
    query = """
    {
        province($id: ID!) {
            id
            name
        }
    }
    """
    snapshot.assert_match(
        client.execute(
            query, variables={"id": relay.Node.to_global_id("ProvinceNode", 2)}
        )
    )


def test_query_towns_of_province(snapshot):
    query = """
    {
        province($id: ID!) {
            id
            name
            towns {
                edges {
                    node {
                        id
                        name
                    }
                }
            }
        }
    }
    """
    snapshot.assert_match(
        client.execute(
            query, variables={"id": relay.Node.to_global_id("ProvinceNode", 2)}
        )
    )
