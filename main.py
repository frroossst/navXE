from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from website import create_app
from datetime import datetime
from algorithms import Path
from graph import Graphs
import psycopg2
import secrets
import pytz
import ast
import os



app = create_app()
api = Api(app)

db = SQLAlchemy()
db.init_app(app=app)



class route(Resource):

    def get(self,graph,home,destn,orientation):

        DATABASE_URL = os.environ.get("DATABASE_URL")

        conn = psycopg2.connect(
            DATABASE_URL,sslmode="require"
        )

        curr = conn.cursor()

        empty_dict = str({})

        query = f"select graphdata from map where graphname = '{graph}';"
        print(query)

        curr.execute(query)

        result = curr.fetchall()

        conn.close()

        graphObj = ast.literal_eval(result[0][0])
        print(graphObj,type(graphObj))

        G = Graphs()
        Graphs.graphDB = G.undirectGraph(graphObj)
        P = Path(Graphs.graphDB)
        print(f"[LOG] BFS from {home} to {destn}")
        print(f"[LOG] graph : {graph} | orientation : {orientation}")
        route_result = P.BFS_SP(G.graphDB,home,destn)
        print(f"[LOG] BFS route = {route_result}")

        return {"home" : home, "destination" : destn, "route" : route_result}                


class token(Resource):

    def get(self,base):

        response_json = {"tokenID" : "None"}

        if len(base) < 9:
            return response_json
        
        else:
            tokenGen = base + secrets.token_hex(16)
            response_json["tokenID"] = tokenGen
            return response_json
        

class create_database(Resource):

    """
    func args : CRUD
        create : add a row into the database
        read : fetch a graph from the database
        update : update a row in the database
        delete : remove a row from the database
    """

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

        if name == "*":
            query = "select graphname from map;" 
        else:
            query = f"select graphdata from map where graphname = '{str(name)}';"

        curr.execute(query)

        result = curr.fetchall()

        conn.close()

        return {"result" : result}

class update_database(Resource):

    def post(self,type,tok,name,new_graph):

        DATABASE_URL = os.environ.get("DATABASE_URL")

        conn = psycopg2.connect(
            DATABASE_URL,sslmode="require"
        )

        curr = conn.cursor()

        if type == "graphdata":

            update_query = f"update map set graphdata = '{str(new_graph)}' where token = '{tok}' and graphname = '{name}';"

            curr.execute(update_query)

            conn.commit()
    
            conn.close()
    
            return {"message" : "updated record"}

        elif type == "chardata":

            update_query = f"update map set chardata = '{str(new_graph)}' where token = '{tok}' and graphname = '{name}';"

            curr.execute(update_query)

            conn.commit()
    
            conn.close()
    
            return {"message" : "updated record"}

        elif type == "undirdata":

            update_query = f"update map set undirdata = '{str(new_graph)}' where token = '{tok}' and graphname = '{name}';"

            curr.execute(update_query)

            conn.commit()
    
            conn.close()
    
            return {"message" : "updated record"}
        
        else:

            return {"message" : "unable to complete database operation"}


class delete_database(Resource):

    def post(self,tok,graph_name):

        DATABASE_URL = os.environ.get("DATABASE_URL")

        conn = psycopg2.connect(
            DATABASE_URL,sslmode="require"
        )

        curr = conn.cursor()

        del_query = f"delete from map where token = '{tok}' and graphname = '{graph_name}';"

        curr.execute(del_query)

        conn.commit()

        conn.close()

        return {"message" : "deleted record"}



class appUpdate(Resource):

    def get(self,dev_tok):

        DATABASE_URL = os.environ.get("DATABASE_URL")

        conn = psycopg2.connect(
            DATABASE_URL,sslmode="require"
        )

        curr = conn.cursor()

        query = "select version from updates;"

        curr.execute(query)

        result = curr.fetchall()

        conn.close()

        return {"version" : str(result[0][0])}

    def post(self,dev_tok):

        DATABASE_URL = os.environ.get("DATABASE_URL")

        conn = psycopg2.connect(
            DATABASE_URL,sslmode="require"
        )

        curr = conn.cursor()

        reginaSK = pytz.timezone("America/Regina")
        now = datetime.now(reginaSK)
        dateStr = now.strftime("%-d.%-m.%y.%-H.%-M")

        query = f"update updates set version = '{dateStr}' where dev_token = '{dev_tok}';"

        curr.execute(query)

        conn.commit()

        conn.close()

        return {"newVersion" : dateStr}


class fetchImage(Resource):

    def get(self,header,graph):

        DATABASE_URL = os.environ.get("DATABASE_URL")

        conn = psycopg2.connect(
            DATABASE_URL,sslmode="require"
        )

        curr = conn.cursor()

        query = f"select uri from images where header = '{header}' and graph = '{graph}';"

        curr.execute(query)

        result = curr.fetchall()

        conn.close()

        try:
            url_return = result[0][0]
            url_return = url_return.replace("-",".")
            url_return = url_return.replace("+","/")
            return {"URI" : str(url_return)}
        except IndexError:
            return {"error" : "unable to unpack values", "code" : 54}

    def post(self,header,graph):
        print("POST does not exist for this call")


class AddImage(Resource):

    def get(self,header,uri,graph):
        print("GET does not exist for this call")

    def post(self,header,uri,graph,tok):
        """
            A POST header is passed separated by an underscore (_), the first part is the header while the second part is the GitHub URL
            fmt => header<br>url<br>graph
            eg : placeA<br>https://www.images.com/placeAimg<br>testDB
        """
        print("[LOG] POSTED header")
        
        #sep_li = header.split("_%_")

        DATABASE_URL = os.environ.get("DATABASE_URL")

        conn = psycopg2.connect(
            DATABASE_URL,sslmode="require"
        )

        curr = conn.cursor()

        #head = sep_li[0]
        #uri = sep_li[1]
        #graph = sep_li[2]

        validated = False

        q = f"select token from map;"
        curr.execute(q)
        r = curr.fetchall()
        for i in r:
            for j in i:
                if j == tok:
                    validated = True

        print(f"validation status : {validated}")

        if validated:
            query = f"insert into images (header, uri, graph) values ('{header}','{uri}','{graph}');"
    
            curr.execute(query)
    
            conn.commit()
    
            conn.close()
    
            return {"message" : "added image", "data" : {"header" : header, "URI" : uri, "graph" : graph}}

        else:
            return {"error" : "validation failed"}





api.add_resource(route,"/api/route/<string:graph>/<string:home>/<string:destn>/<string:orientation>")
api.add_resource(token,"/api/token/<string:base>")
api.add_resource(create_database,"/api/database/create/<string:name>/<string:tok>/<string:data>")
api.add_resource(read_database,"/api/database/read/<string:name>")
api.add_resource(update_database,"/api/database/update/<string:type>/<string:tok>/<string:name>/<string:new_graph>")
api.add_resource(delete_database,"/api/database/delete/<string:tok>/<string:graph_name>")
api.add_resource(appUpdate,"/api/update/<string:dev_tok>")
api.add_resource(fetchImage,"/api/image/<string:header>/<string:graph>")
api.add_resource(AddImage,"/api/image/add/<string:header>/<string:uri>/<string:graph>/<string:tok>")



if __name__ == "__main__":
    print("[LOG] App __init__")
    app.run()