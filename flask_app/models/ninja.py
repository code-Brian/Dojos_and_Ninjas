from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Ninja():
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return results
    
    @classmethod
    def get_one(cls, data):
        print("getting one ninja...")
        query = '''
        SELECT * FROM ninjas
        WHERE id = %(id)s
        '''
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def show_dojo(cls, data):
        query = '''
        SELECT dojo.name FROM dojos
        WHERE ninja.id = %(id)s
        '''
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_dojo_ninjas(cls, data):
        query = '''SELECT * FROM ninjas
        WHERE dojo_id = (%(id)s);'''
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        print(results)
        dojo_ninjas = []
        for dojo_ninja in results:
            dojo_ninjas.append(cls(dojo_ninja))
        return results
    
    @classmethod
    def add_ninja(cls, data):
        query = '''
        INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
        VALUES (%(fname)s, %(lname)s, %(age)s, %(id)s, NOW(), NOW() );'''

        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def edit_ninja(cls, data):
        query = '''
        UPDATE ninjas SET 
        first_name=%(fname)s, 
        last_name=%(lname)s, 
        age=%(age)s, 
        updated_at=NOW(),
        dojo_id=%(dojo_id)s
        WHERE id = %(id)s;
        '''

        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = '''
        DELETE FROM ninjas WHERE id = %(id)s;'''

        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

'''
SELECT * FROM ninjas 
JOIN dojos ON ninjas.id
WHERE dojos.id = 4;
'''