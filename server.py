#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""File server.

Starts a simple HTML server.
"""
import os
import socket
import audio_metadata
import pyqrcode
from flask import Flask, render_template, url_for

# @TODO https://stackoverflow.com/questions/43346486/change-static-folder-from-config-in-flask
app = Flask(__name__)


def get_ip():
    """Get local IP address.

    https://stackoverflow.com/a/28950776
    """
    # pylint: disable=C0103, W0703
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


def sec2min(sec):
    """Convert seconds to minutes."""
    print(sec)
    min_val = int(sec // 60)
    sec_val = int(sec % 60)
    str_val = "{:02}:{:02}".format(min_val, sec_val)
    print(str_val)
    return str_val


def get_files(directory):
    """Get files."""
    filelist = os.listdir(directory)

    files = []
    for filename in filelist:
        metadata = audio_metadata.load(os.path.join(directory, filename))
        files.append(
            {
                "filename": filename,
                "url": url_for("static", filename=filename),
                "size": "{:02}".format(round(metadata.filesize / 1048576, 2)),
                "duration": sec2min(metadata.streaminfo.duration),
                # "album": metadata.tags.album[0],
                # "artist": metadata.tags.artist,
                "title": metadata.tags.title[0],
            }
        )

    return files


@app.route("/")
def home():
    """Home route."""
    return render_template("home.html", files=get_files("static"))


if __name__ == "__main__":
    print(f"\nRunning on http://{get_ip()}:5000")
    url = pyqrcode.create(f"http://{get_ip()}:5000")
    print(url.terminal(quiet_zone=1))

    # Make server publicly available
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
    app.run(debug=False, host="0.0.0.0")
