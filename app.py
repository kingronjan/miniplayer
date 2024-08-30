import os
from datetime import datetime
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    base_dir = Path(__file__).parent.absolute() / 'static/videos'
    files = []

    with os.scandir(base_dir) as entries:
        for entry in entries:
            modify_time = datetime.fromtimestamp(entry.stat().st_mtime)
            modify_time = modify_time.strftime('%Y-%m-%d %H:%M')
            files.append((entry.path.split('videos', maxsplit=1)[-1], entry.name, modify_time))

    return render_template('index.html', files=files)


@app.route('/video/<string:filename>')
def video(filename):
    return render_template('video.html', filename=filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
