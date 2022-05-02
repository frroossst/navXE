from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from website import create_app
from algorithms import Path
from graph import Graphs
import secrets
import os


app = create_app()
api = Api(app)


db = SQLAlchemy()
db.init_app(app=app)

class Map(db.Model):

    name = db.Column(db.String(), primary_key=True, nullable=False)
    token = db.Column(db.String(), unique=True, nullable=False)
    graphData = db.Column(db.String())

    def __init__(self,graphName,token,graphData):

        self.graphName = graphName 
        self.token = token 
        self.graphData = graphData

    def __repr__(self):
        return "<__repr__ response not ready yet>"



class route(Resource):

    def get(self,graph,home,destn,orientation):

        G = Graphs()
        Graphs.graphDB = G.undirectGraph(Graphs.graphDB)
        P = Path(Graphs.graphDB)
        print(f"[LOG] BFS from {home} to {destn}")
        print(f"[LOG] graph : {graph} | orientation : {orientation}")
        route_result = P.BFS_SP(G.graphDB,home,destn)
        print(f"[LOG] BFS route = {route_result}")
        return {"home" : home, "destination" : destn, "route" : route_result}                

    def post(self):
        return {"message" : "POSTED to API"}

class token(Resource):

    def get(self,base):

        response_json = {"tokenID" : "None"}

        if len(base) < 9:
            return response_json
        
        else:
            tokenGen = secrets.token_hex(8) + base + secrets.token_hex(16)
            response_json["tokenID"] = tokenGen
            return response_json
        

    def post(self,base):
        return {"message" : "this API endpoint does not support POST request"}

class database(Resource):

    def get(self,name):
        return {"err" : name}

    def post(self,name,tok,data):

        data = Map(name=name,token=tok,graphData=data)

        db.session.add(data)
        db.session.commit()

        return {"graph name" : name, "token" : tok, "data" : data}



api.add_resource(route,"/api/route/<string:graph>/<string:home>/<string:destn>/<string:orientation>")
api.add_resource(token,"/api/token/<string:base>")
api.add_resource(database,"/api/database/<string:name>/<string:tok>/<string:data>")



if __name__ == "__main__":
    print("[LOG] App __init__")
    app.run()
