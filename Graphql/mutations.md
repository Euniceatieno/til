# Mutations
+ Graphql mutations allow posting,editing and deleting data  
+ Graphql mutations are rest alternatives for putting,updating  
and deleting data in an API.
+ Graphql mutations take in class arguments and also contain  
a mutate method which is a class method.
+ Before creating a graphql mutation,we must first define models  
and schemas.
The code snippet below shows a graphql mutation that adds details to a table  
User in a datbase.  


`
class UserCreate(graphene.Mutation):
    class Arguemnts:
        name = graphene.String()

    user = graphene.Field(UserSchema) ## graphene.Field takes in a defined schema that attached to a model.

    def mutate(self,info,name):
        user = User(name = name) ## User here is the user model
        db_session.add(user)
        db.commit()
        return UserCreate(user = user)
 

`