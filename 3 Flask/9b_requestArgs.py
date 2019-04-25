from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome!'

# shopee.co.id/search?keyword=tamiya&location=jakarta
@app.route('/search')
def search():
    print(request.args)
    print(request.args['keyword'])
    print(request.args['location'])
    return 'Hai'

if __name__ == '__main__':
    app.run(debug=True)

# try to GET:
# localhost:5000/search?keyword=tamiya&location=jakarta
# localhost:5000/search?keyword=drone&location=bandung