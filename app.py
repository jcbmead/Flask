# This imports flask and the render template and bootstrap so that bootstrap templates can be used
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# This creates a new flask app and boostrap app within the flask app
app = Flask(__name__)
bootstrap = Bootstrap(app)

# This routes the user to the correct page
@app.route('/')
def index():
	return render_template('index.html')

# This is a custom error page for a 404 error
# This is shown when a page is not currently assoicated with that link
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# This tells the flask app to run when the code is run
# This also tells the app to have debugging on
# This also tells the app to run on 0.0.0.0 which is for unknown IPs which mean it can be accessed from any device
if __name__ == '__main__':
	app.config['DEBUG'] = True
	app.run(host='0.0.0.0')
