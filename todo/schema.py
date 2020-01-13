import graphene
from graphene_django import DjangoObjectType
from .models import TodoList
from graphql import GraphQLError


class TodoListType(DjangoObjectType):
    class Meta:
        model = TodoList


class CreateList(graphene.Mutation):
    list = graphene.Field(TodoListType)

    class Arguments:
        task = graphene.String(required=True)

    def mutate(self, info, content):
        list = TodoList.objects.get(pk=id)
        list.content = content
        list.save()

        return CreateList(list=list)


class UpdateList(graphene.Mutation):
    list = graphene.Field(TodoListType)

    class Arguments:
        task = graphene.Int(required=True)
        updated_task = graphene.String(required=True)

    def mutate(self, info, content):
        list = TodoList.objects.get(pk=id)

        if list is None:
            raise GraphQLError("Empty Task can  not be added!")
        list.content = content
        list.save()

        return UpdateList(list=list)


class DeleteList(graphene.Mutation):
    list = graphene.Field(TodoListType)

    class Arguments:
        task = graphene.Int(required=True)
        delete_task = graphene.String(required=True)

    def mutate(self, info, content):
        list = TodoList.objects.get(pk=id)

        if list is None:
            raise GraphQLError("Task can  not be found!")
        list.content = content
        list.save()

        return DeleteList(list=list)


class Mutation(graphene.ObjectType):
    create_list = CreateList.Field()
    update_list = UpdateList.Field()
    delete_list = DeleteList.Field()


class Query(graphene.ObjectType):
    todolist = graphene.List(TodoListType)

























