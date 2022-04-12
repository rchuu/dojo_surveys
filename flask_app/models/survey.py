from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Survey:
    db = 'dojo_survey_schema'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_survey(cls):
        query = """SELECT * FROM dojos
        ORDER BY dojos.id 
        DESC LIMIT 1;"""
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        return Survey(results[0])  # why this?

    @staticmethod
    def is_valid(survey):
        is_valid = True  # we assume this is true
        if len(survey['name']) < 2:  # to make sure everything in the model is acceptable
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(survey['location']) < 1:
            flash("Must have location.")
            is_valid = False
        if len(survey['comment']) < 2:
            flash("Comment must be 2 characters or greater.")
            is_valid = False
        if len(survey['language']) < 1:
            flash("Must have fave language.")
            is_valid = False
        return is_valid
