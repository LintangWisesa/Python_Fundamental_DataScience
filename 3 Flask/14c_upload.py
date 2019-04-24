# upload image & render html with image uploaded

from flask import Flask, render_template, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# lokasi file usai upload ada di folder './file'
app.config['UPLOAD_FOLDER'] = './file'

@app.route('/')
def uploadpage():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploadfile():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return redirect('/sukses/' + filename)
		
# static file render route
@app.route('/file/<path:path>')
def staticfile(path):
    return send_from_directory('file', path)

# render html with file image uploaded
@app.route('/sukses/<path:path>')
def sukses(path):
    return render_template('sukses.html', data = "http://localhost:5000/file/"+path)

if __name__ == '__main__':
   app.run(debug = True)