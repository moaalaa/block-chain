from flask import Flask, redirect, render_template, request

from block import *

app = Flask(__name__, static_url_path='/assets', static_folder='web/assets', template_folder='web/views')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/add-to-list', methods=['POST'])
def add_to_list():

    anime_name = request.form.get('anime_name')
    anime_category = request.form.get('anime_category')
    watched_before = request.form.get('watched_before')
    
    create_block(anime_name=anime_name, anime_category=anime_category, watched_before=watched_before)
    
    return redirect('/')

@app.route('/check-list-integrity', methods=['GET'])
def check_list_integrity():
    blocks = check_integrity()

    return render_template('index.html', blocks=blocks)

if __name__ == "__main__":
    app.run(debug=True)
