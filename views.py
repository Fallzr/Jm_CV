from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash

views = Blueprint(__name__, "views", template_folder='templates')  # Specify the templates folder for this blueprint

# Simulated user data for demonstration
users = {
    "user": "123"  # Replace this with your user data
}

@views.route("/")
def home():
    return render_template("index.html", name="Jm")  # This will find index.html in the root directory

@views.route("/profile")
def profile():
    return render_template("profile.html")  # This will find profile.html in the templates directory

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))

@views.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")  # Use 'username' instead of 'email'
    password = request.form.get("password")

    # Check if the username and password match
    if username in users and users[username] == password:
        return redirect(url_for("views.profile"))
    
    flash("Invalid credentials!")  # Show an error message
    return redirect(url_for("views.home"))  # Redirect back to home on failure
