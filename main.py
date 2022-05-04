from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from numpy import empty
from website import create_app
from algorithms import Path
from graph import Graphs
import psycopg2
import secrets
import os


app = create_app()
api = Api(app)


db = SQLAlchemy()
db.init_app(app=app)

class Map(db.Model):

    __tablename__ = "map"
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


class create_database(Resource):

    """
    func args : CRUD
        create : add a row into the database
        read : fetch a graph from the database
        update : update a row in the database
        delete : remove a row from the database
    """

    def get(self):
        pass

    def post(self,name, tok, data):

        DATABASE_URL = os.environ.get("DATABASE_URL")

        conn = psycopg2.connect(
            DATABASE_URL,sslmode="require"
        )

        curr = conn.cursor()

        empty_dict = str({})

        insert_query = f"INSERT INTO map(graphname,token,graphdata,chardata,undirdata) VALUES('{name}','{tok}','{data}','{empty_dict}','{empty_dict}');"

        curr.execute(insert_query)

        conn.commit()

        conn.close()

        return {"message" : "inserted record"}


class read_database(Resource):

    def get(self,name):

        DATABASE_URL = os.environ.get("DATABASE_URL")

        conn = psycopg2.connect(
            DATABASE_URL,sslmode="require"
        )

        curr = conn.cursor()

        print(f"[DEBUG] {name}")

        query = f"select graphdata from map where graphname = '{str(name)}';"

        curr.execute(query)

        result = curr.fetchall()

        conn.close()

        return {"result" : result}

class update_database(Resource):

    def post(self,tok,name,new_graph):

        DATABASE_URL = os.environ.get("DATABASE_URL")

        conn = psycopg2.connect(
            DATABASE_URL,sslmode="require"
        )

        curr = conn.cursor()

        update_query = f"update map set graphdata = '{str(new_graph)}' where token = '{tok}' and graphname = '{name}';"

        # ! Add a method to return invalid response for invalid operations

        curr.execute(update_query)

        conn.commit()

        conn.close()

        return {"message" : "updated record"}


class delete_database(Resource):

    def post(self):
        pass




api.add_resource(route,"/api/route/<string:graph>/<string:home>/<string:destn>/<string:orientation>")
api.add_resource(token,"/api/token/<string:base>")
api.add_resource(create_database,"/api/database/create/<string:name>/<string:tok>/<string:data>")
api.add_resource(read_database,"/api/database/read/<string:name>")
api.add_resource(update_database,"/api/database/update/<string:tok>/<string:name>/<string:new_graph>")
api.add_resource(delete_database,"/api/database/delete/<string:token>/<string:graph_name>")



if __name__ == "__main__":
    print("[LOG] App __init__")
    app.run()
