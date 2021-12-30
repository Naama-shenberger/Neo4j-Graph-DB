# Connection to neo4j driver connection
from driver_connection import graphdb


class Apartment:
    """class Apartment"""

    def __init__(self, number, key=-1):
        """A constructor that gets a number and key unique to each object (Initialized with zero)"""
        self.key = key
        self.number = number


def createApartmentNode(a):
    """A function that accepts a Apartment-type object and builds a node with properties"""
    if type(a) == Apartment:
        number = a.number
        key = a.key
        session = graphdb.session()
        session.run("CREATE (N:Apartment {number:$number,key:$key})", number=number, key=key)
    else:
        print("The parameter you submitted is not Apartment-type object")
