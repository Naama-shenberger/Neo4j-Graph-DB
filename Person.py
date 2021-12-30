# Connection to neo4j driver connection
from driver_connection import graphdb


class Person:
    """class person"""

    def __init__(self, name, last_name, age, gender, key=-1):
        """A constructor that gets a name,last name,age, gender, and key unique to each object (Initialized with zero)"""
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.key = key


def createPersonNode(p):
    '''A function that accepts a person-type object and builds a node with properties'''
    if type(p) == Person:
        name = p.name
        last_name = p.last_name
        age = p.age
        gender = p.gender
        key = p.key
        session = graphdb.session()
        session.run("CREATE (N:person {name:$name, last_name:$last_name, age:$age, gender:$gender, key:$key})",
                    name=name, last_name=last_name, age=age, gender=gender, key=key)
    else:
        print("The parameter you submitted is not person-type object")
