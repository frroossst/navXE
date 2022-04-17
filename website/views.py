from flask import Blueprint, render_template, request, flash

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("base.html")

@views.route("/navigate",methods=["GET","POST"])
def navigate():
    if request.method == "POST":
        home_node = request.form.get("home")
        destn_node = request.form.get("destination")
        print(f"home : {home_node} destination : {destn_node}")

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