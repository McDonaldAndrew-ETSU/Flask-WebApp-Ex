# Create Virtual Environment, then Install Flask
### Python 3.10.6
Flask uses Jinja as HTML templates as the HTML must be created as Flask is a lightweight web-development framework.

The import statement includes references to Flask, which is the core of any Flask application. We'll use render_template in a while, when we want to return our HTML.

# Add the Routes to app.py
For example:
**@app.route('/', methods=['GET'])**
**def index():**
    **return render_template('index.html')**

# Create a templates Directory
Inside the templates folder will contain created HTML files so that your app can render the linked HTML files

# Test the Application
Run the following command to set the Flask runtime to development, which means that the server will automatically reload with every change:
**set FLASK_ENV=development**
run the app:
**fask run**

