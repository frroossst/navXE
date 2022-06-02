from flask import Blueprint, render_template, request, redirect, url_for
from flask_cors import cross_origin
from algorithms import Path
from graph import Graphs
from methods import method

views = Blueprint('views',__name__)

# Checking for https
def check_https():
    print(f"[LOG] {request.url}")
    if request.url[0:8:1] != "https://":
        print("[LOG] insecure connection redirecting")
        url_new = request.url.replace("http://","https://",1)
        code = 301
        return(redirect(url_new,code=code))

@views.route('/')
def home():
    check_https()
    return render_template("deprecated.html")

@views.route("/navigate",methods=["GET","POST"])
def navigate():

    return render_template("deprecated.html")

    print("[LOG] redirect to /navigate")
    print(request.form)

    if request.method == "POST":
        print("[LOG] POST method on /navigate")

        if request.form.get("path-submit"):
            print(request.form.get("path-submit"))
            qr_url = request.form.get("qr-URL")
            print(f"[LOG] qr_url : {qr_url}")

            home_node = request.form.get("home")
            destn_node = request.form.get("destination")
            home_orientation = request.form.get("qr-orientation")
            home_graph = request.form.get("qr-graph")

            print(f"home : {home_node} | destination : {destn_node}")
            print(f"orientatiopn : {home_orientation} | graph : {home_graph}")

            if len(home_node) == 0:
                return render_template("navigate.html",route="Missing home node, scan a QR code or enter value")

            if len(destn_node) != 0:

                G = Graphs()
                Graphs.graphDB = G.undirectGraph(Graphs.graphDB)
                P = Path(Graphs.graphDB)
                print(f"[LOG] BFS from {home_node} to {destn_node}")
                route_result = P.BFS_SP(G.graphDB,home_node,destn_node) 
                print(f"[LOG] BFS route = {route_result}")
                return render_template("navigate.html",route=route_result,qrDecoded="")

            else:
                return render_template("navigate.html",route="Missing destination location")

        elif request.form.get("scanQR-submit"):
            return redirect(url_for("views.qr_scan"))

@views.route("/graphs")
def graphs():
    return render_template("deprecated.html")
    return "Look at all the user generated maps"

@views.route("/create")
def create():
    return render_template("deprecated.html")
    return "This is where you create a new graph"

@views.route("/code")
def code():
    return render_template("deprecated.html")
    return "<a href='https://github.com/frroossst/navXE'>GitHub Link</a>"

@views.route("/login")
def login():
    return render_template("deprecated.html")
    return "Login Page"

@views.route("/docs")
def docs():
    return render_template("deprecated.html")
    return "Documentation"

@views.route("/reports")
def reports():
    return render_template("deprecated.html")
    return "Cannot submit reports as of now!"

@views.route("/share")
def share():
    return render_template("deprecated.html")
    return render_template("share.html")

@views.route("/settings")
def settings():
    return render_template("deprecated.html")
    return "Configure your settings"

@views.route("/qr",methods=["GET","POST"])
def qr_scan():

    return render_template("deprecated.html")
    if request.method == "POST":
        scanned_value = request.form.get("qr-scan-value")
        print(f"[LOG] qr read as {scanned_value}")
        return redirect(url_for("views.navigate"))

    else:
        return render_template("qr_front.html")

@views.route("/api",methods=["GET","POST"])
@cross_origin()
def API():
    return {"message" : "Hello World! from the API"}
