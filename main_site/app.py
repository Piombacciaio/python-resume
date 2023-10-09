import oyaml as yaml, os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['UPLOAD_FOLDER'] = 'cv'

@app.route('/')
def index():
    website_data = yaml.safe_load(open('main_site/_config.yaml'))

    return render_template('index.html', data=website_data)

@app.route('/cv-IT')
def downloadIT():
    path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(path, "cv - IT.pdf")

@app.route('/cv-EN')
def downloadEN():
    path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(path, "cv - EN.pdf")

if __name__ == '__main__':
    app.run(debug=False, port=5000)
