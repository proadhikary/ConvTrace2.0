from flask import Flask, render_template, request, session
import json

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def fetch(file_id):
    with open('static/data/data.json') as f:
        obj = json.load(f)

    sess = obj[str(file_id)]
    url = sess['youtube_url']
    text = [{x['speaker']: x['text']} for x in sess['transcript']]

    return file_id, url, text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_input = request.form.get('search', '0')
        session['file_id'], session['url'], session['chat'] = fetch(search_input)
        return render_template('index.html', file_id=session['file_id'], url=session['url'], chat=session['chat'])
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
