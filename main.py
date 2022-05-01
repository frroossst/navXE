from flask_restful import Api, Resource
from website import create_app
from algorithms import Path
from graph import Graphs

app = create_app()
api = Api(app)

class route(Resource):

    def get(self,home,destn):
        G = Graphs()
        Graphs.graphDB = G.undirectGraph(Graphs.graphDB)
        P = Path(Graphs.graphDB)
        print(f"[LOG] BFS from {home} to {destn}")
        route_result = P.BFS_SP(G.graphDB,home,destn)
        print(f"[LOG] BFS route = {route_result}")
        return {"home" : home, "destination" : destn, "route" : route_result}                

    def post(self):
        return {"message" : "POSTED to API"}


api.add_resource(route,"/route/<string:home>/<string:destn>")


if __name__ == "__main__":
    print("[LOG] App __init__")
    app.run()
