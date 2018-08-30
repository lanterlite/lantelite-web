from flask import Flask, render_template
# from flask_bootstrap import Bootstrap
from flask import request
from application.settings import DEBUG

app = Flask(__name__)
app.debug = DEBUG
# Bootstrap(app)
app.static_folder = 'static'
	
@app.route('/')
def index():
    return render_template('index.html')
    # return render_template('bootstrap_index.html')
	
# if __name__ == '__main__':
	# app.run(debug=True)
	
import os
# def dated_url_for(endpoint, **values):
    # if endpoint == 'static':
        # filename = values.get('filename', None)
        # if filename:
            # file_path = os.path.join(app.root_path,
                                     # app.static_path, filename)
            # values['q'] = int(os.stat(file_path).st_mtime)
    # return url_for(endpoint, **values)
	
	
@app.url_defaults
def hashed_static_file(endpoint, values):
    if 'static' == endpoint or endpoint.endswith('.static'):
        filename = values.get('filename')
        if filename:
            blueprint = request.blueprint
            if '.' in endpoint:  # blueprint
                blueprint = endpoint.rsplit('.', 1)[0]

            static_folder = app.static_folder
           # use blueprint, but dont set `static_folder` option
            if blueprint and app.blueprints[blueprint].static_folder:
                static_folder = app.blueprints[blueprint].static_folder

            fp = os.path.join(static_folder, filename)
            if os.path.exists(fp):
                values['_'] = int(os.stat(fp).st_mtime)
				
				
	