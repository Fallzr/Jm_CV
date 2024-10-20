from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from forms import LoginForm, SignupForm  # Import the LoginForm and SignupForm classes

views = Blueprint(__name__, "views", template_folder='website/templates')  # Specify the templates folder for this blueprint

# Simulated user data for demonstration
users = {
    "user": "123"  # Replace this with your user data
}

@views.route("/")
def home():
    form = LoginForm()  # Create an instance of the LoginForm
    return render_template("login_page.html", form=form)  # Pass the form to the template

@views.route("/signup", methods=["GET", "POST"])  # Combined signup route
def signup():
    form = SignupForm()  # Create an instance of the SignupForm
    if request.method == "POST":
        # Process the signup data here
        first_name = form.first_name.data
        last_name = form.last_name.data
        sex = form.sex.data
        email = form.email.data
        password = form.password.data
        # Add logic to save the user information here
        flash("Signup successful!")  # You can adjust this based on your logic
        return redirect(url_for("views.home"))  # Redirect to home or login page
    
    return render_template("signup_page.html", form=form)  # Pass the form to the template

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
    form = LoginForm()  # Create a new instance of the form
    if form.validate_on_submit():  # Validate the form
        username = form.username.data
        password = form.password.data

        # Check if the username and password match
        if username in users and users[username] == password:
            return redirect(url_for("views.profile"))
        
        flash("Invalid credentials!")  # Show an error message
        return redirect(url_for("views.home"))  # Redirect back to home on failure
    
    flash("Please fill out the form correctly!")  # Handle form validation error
    return redirect(url_for("views.home"))  # Redirect back to home on failure
