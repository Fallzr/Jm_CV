from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash

views = Blueprint(__name__, "views")

# Simulated user data for demonstration
users = {
    "user": "123"  # Replace this with your user data
}

@views.route("/")
def home():
    return render_template("index.html", name="Jm")

@views.route("/profile")
def profile():
    return render_template("profile.html")

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))

@views.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    # Check if the email and password match
    if email in users and users[email] == password:
        return redirect(url_for("views.profile"))
    
    flash("Invalid credentials!")  # Show an error message
    return redirect(url_for("views.home"))  # Redirect back to home on failure
