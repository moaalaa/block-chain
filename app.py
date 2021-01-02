from flask import Flask, redirect, render_template, request




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
if __name__ == "__main__":
    app.run(debug=True)
