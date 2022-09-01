from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # define a class method which queries and returns all dojos in the database
    @classmethod
    def get_all(cls):
        # store the query string in a variable
        query = "SELECT * FROM dojos"
        # query the database using the variable we just made, and store the results within the 'results' variable
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # we will use this empty list to store each dojo in our database
        dojos = []
        # iterate over the results from our query, and append them to the dojos list
        for dojo in results:
            dojos.append(cls(dojo))
        # after we are done iterating over the query resu   lts, return the list of dojos
        return dojos

    @classmethod
    def get_one(cls, data):
        print("getting one dojo...")
        query = '''
        SELECT * FROM dojos
        WHERE id = %(id)s
        '''
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return cls(result[0])
        

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO dojos (name, created_at, updated_at) 
        VALUES (%(dojo_name)s, NOW(), NOW() );
        """
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)
    

