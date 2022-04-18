from flask import Blueprint, render_template, request, flash
from algorithms import Path
from graph import Graphs

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("base.html")

@views.route("/navigate",methods=["GET","POST"])
def navigate():

    if request.method == "POST":
        if request.form.get("path-submit"):
            qr_url = request.form.get("qr-URL")
            if qr_url != None:
                try:
                    from base64 import b64decode

                    data_uri = qr_url
                    header, encoded = data_uri.split(",", 1)
                    data = b64decode(encoded)
                    with open("qrCode.png", "wb") as f:
                        f.write(data)

                    
                except Exception as e:
                    print(e)

            home_node = request.form.get("home")
            destn_node = request.form.get("destination")
            print(f"home : {home_node} | destination : {destn_node}")

            if len(home_node) != 0 and len(destn_node) != 0:

                G = Graphs()
                Graphs.graphDB = G.undirectgraph(Graphs.graphDB)
                P = Path(Graphs.graphDB)
                route_result = P.BFS_SP(G.graphDB,home_node,destn_node)

                return render_template("navigate.html",route=route_result)

            else:
                return render_template("navigate.html")


    return render_template("navigate.html")

@views.route("/maps")
def maps():
    return "Look at all the user generated maps"

@views.route("/create")
def create():
    return "This is where you create a new graph"

@views.route("/code")
def code():
    return "GitHub link"

@views.route("/login")
def login():
    return "Login Page"

@views.route("/docs")
def docs():
    return "Documentation"

@views.route("/camera")
def camera():
    import camera
    codeRead = camera.decodeAndCaptureQR()