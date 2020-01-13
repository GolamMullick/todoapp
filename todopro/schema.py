import graphene
import todo.schema

import graphql_jwt


class Query(todo.schema.Query,graphene.ObjectType):
    pass


class Mutation(todo.schema.Mutation,
               graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)