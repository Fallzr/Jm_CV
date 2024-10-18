from flask import Flask, redirect, url_for
from views import views

app = Flask(__name__, template_folder='.')  # Keep the root folder for index.html
app.secret_key = 'Th1s1sak3y'  # Set your secret key here
app.register_blueprint(views, url_prefix="/login_page")

# Add a route for the root URL
@app.route("/")
def index():
    return redirect(url_for("views.home"))  # Redirect root URL to /views/

if __name__ == '__main__':
    app.run(debug=True, port=8000)
