from flask import Flask, render_template, render_template_string, request, jsonify
from extractor import get_article

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template_string("<h1>Hello</h1>")

@app.route('/extract>', methods=['GET', 'POST'])
def extract():
    if request.method == 'POST':
        url = request.form['article_url']
        data = {
            'text': get_article(url=str(url))
            }
        response = jsonify(data)
        response.status_code = 200
        return response


if __name__ == '__main__':
    app.run(debug=True)