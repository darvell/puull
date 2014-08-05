from flask import Flask, request
import os
import random
import string
import time

app = Flask(__name__)
app.config.from_pyfile('settings.cfg', silent=True)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # Stop jerks

@app.route('/api/up',methods=['POST'])
def upload():
    img  = request.files['f']
    secret_filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    file_extension = os.path.splitext(img.filename)[1]
    img.save(os.path.join(app.config['UPLOAD_FOLDER_REAL_LOCATION'],'{0}{1}'.format(secret_filename,file_extension)))
    res =  '0,{0},{1},0'.format('http://{0}/{1}/{2}{3}'.format(app.config['HOSTNAME'],app.config['UPLOAD_FOLDER'],secret_filename,file_extension),int(time.time()))
    print res
    return res

@app.route('/api/hist',methods=['POST'])
def history():
    return '0'

@app.route('/{0}/<path:path>'.format(app.config['UPLOAD_FOLDER']))
def serve_file(path):
    return app.send_static_file(os.path.join(app.config['UPLOAD_FOLDER_REAL_LOCATION'],path))


# For those using the OSX patch.
@app.route('/api/hist/',methods=['POST'])
def history_redir():
    return history()

@app.route('/api/up/',methods=['POST'])
def upload_redir():
    return upload()


@app.before_first_request
def init():
    app.config['UPLOAD_FOLDER_REAL_LOCATION'] = os.path.join(os.path.dirname(os.path.realpath(__file__)),app.config['UPLOAD_FOLDER'] + '/')
    if not os.path.exists(app.config['UPLOAD_FOLDER_REAL_LOCATION']):
        os.makedirs(app.config['UPLOAD_FOLDER_REAL_LOCATION'])



if __name__ == '__main__':
    app.run('0.0.0.0',80,debug=True)