from flask import Blueprint, render_template, request, flash
from algorithms import Path
from graph import Graphs

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("base.html")

@views.route("/navigate",methods=["GET","POST"])
def navigate():
    print("[LOG] redirect to /navigate")
    print(request.form)

    if request.method == "POST":
        print("[LOG] POST method on /navigate")

        if request.form.get("path-submit"):
            qr_url = request.form.get("qr-URL")
            print(f"[LOG] qr_url : {qr_url}")

            if qr_url != None or qr_url != "None":

                try:
                    from base64 import b64decode

                    data_uri = qr_url
                    _, encoded = data_uri.split(",", 1)
                    data = b64decode(encoded)

                    with open("qrCode.png", "wb") as f:
                        f.write(data)
                        print("[LOG] writing qr code to PNG")
                    
                except Exception as e:
                    print(f"[ERROR] {e}")

            home_node = request.form.get("home")
            print(f"[LOG] {home_node}, {type(home_node)}")
            destn_node = request.form.get("destination")

            if home_node == "" or home_node is None or  home_node == "None" or len(home_node) == 0:
                print("[LOG] reading QR code to home_node")
                import camera
                home_node = camera.decodeAndCaptureQR()

            print(f"home : {home_node} | destination : {destn_node}")

            if len(destn_node) != 0:

                G = Graphs()
                Graphs.graphDB = G.undirectGraph(Graphs.graphDB)
                P = Path(Graphs.graphDB)
                route_result = P.BFS_SP(G.graphDB,home_node,destn_node) 

                return render_template("navigate.html",route=route_result)

            else:
                return render_template("navigate.html",route="Missing home or destination location")


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