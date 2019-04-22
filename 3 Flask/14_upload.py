from flask import Flask, render_template, request
from werkzeug import secure_filename
import os

app = Flask(__name__)

# lokasi file usai upload ada di folder './file'
app.config['UPLOAD_FOLDER'] = './file'

@app.route('/upload')
def uploadpage():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploadfile():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return 'File uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)