from flask import Flask, redirect, url_for
from flask_wtf import CSRFProtect  # Import CSRFProtect
from views import views

# Initialize the Flask app
app = Flask(__name__, template_folder='.')  # Keep the root folder for index.html

# Set the secret key for session management and CSRF protection
app.secret_key = 'Th1s1sak3y'  # Make sure to use a strong secret key

# Enable CSRF protection
csrf = CSRFProtect(app)  # CSRF protection is enabled here

# Register the blueprint
app.register_blueprint(views, url_prefix="/login_page")

# Add a route for the root URL
@app.route("/")
def login_page():
    return redirect(url_for("views.home"))  # Redirect root URL to /views/

if __name__ == '__main__':
    app.run(debug=True, port=8000)
