# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['UPLOADED_PATH'] = os.path.join(app.root_path, 'upload')

def dirCheck(dirPath):
    if not os.path.isdir(dirPath):
        try:
            os.mkdir(dirPath)
        except FileExistsError:
                pass

dirCheck(app.config['UPLOADED_PATH'])

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        for f in request.files.getlist('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('index.html')

if __name__ == '__main__':
    if len(os.sys.argv) > 1:
        if os.sys.argv[1] == 'debug':
            app.debug = True
    app.run('0.0.0.0', port=5000, threaded=True)
