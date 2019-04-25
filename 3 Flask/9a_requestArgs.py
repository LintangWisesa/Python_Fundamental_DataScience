from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome!'

# shopee.co.id/search?keyword=tamiya
@app.route('/search')
def search():
    print(request.args)
    print(request.args['keyword'])
    return 'Hai'

if __name__ == '__main__':
    app.run(debug=True)

# try to GET:
# localhost:5000/search?keyword=tamiya
# localhost:5000/search?keyword=drone