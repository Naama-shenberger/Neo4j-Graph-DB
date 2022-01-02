from neo4j import GraphDatabase

uri = "neo4j+s://1d0a616c.databases.neo4j.io"
graphdb = GraphDatabase.driver(uri, auth=("neo4j", "gmnnjaal3rzkRdOuAD8QHN1EAwwyzhNMiid85MTIN0c"))
