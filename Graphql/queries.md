# Queries
+ Graphql queries allow retrieval of data from an API. 
+ Queries are REST alternatives for retrieving data from an API.
+ They contain a type graphene.List or graphene.Field which  
references a defined schema.
+ They must have  a resolve method which is a class method and  
has implementation for querying the db for the needed data.  
+ Before creating a graphql query,we must first define models  
and schemas.
The code snippet below shows a graphql query that queries data from a table User.

`


    class QueryUsers(graphene.ObjectType:
        users = graphene.List(UserSChema)


        def resolve_users(self,info):
            users = db_session.query(User.all())
            return users
 

`
