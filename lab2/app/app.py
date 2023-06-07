from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    url = request.url
    return render_template('index.html')

@app.route('/headers')
def headers():
    return render_template('headers.html')


@app.route('/args')
def args():
    return render_template('args.html')
# pip install python-dotenv
@app.route('/cookies')
def cookies():
    response = make_response(render_template('cookies.html'))
    if 'name' in request.cookies:
        response.delete_cookie('name')
    else:
        response.set_cookie('name', 'value')
    return response
    
@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
