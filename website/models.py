from enum import unique
from . import db

class Map(db.Model):
    
    name = db.Column(db.String, primary_key=True, nullable=False)

    token = db.Column(db.String, unique=True, nullable=False)

    graphData = db.Column(db.String)

    charData = db.Column(db.String)

    undirData = db.Column(db.String)

    updated = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Map('{self.name}', '{self.token}', '{self.graphData}', '{self.charData}', '{self.undirData}', '{self.updated}')"