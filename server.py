#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""File server.

Starts a simple HTML server.
"""
import argparse
import pyqrcode
from flask import Flask, render_template, url_for, send_from_directory, abort
from utils import get_ip, sec2min, get_files

# Parse command line arguments
PARSER = argparse.ArgumentParser(
    description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
)
PARSER.add_argument("path", help="Path to folder with audio files (.mp3, .wav, .ogg)")
ARGS = PARSER.parse_args()

# Start webapp
app = Flask(__name__)
app.config["AUDIO_FOLDER"] = ARGS.path

# Define routes
@app.route("/")
def audio_list():
    """Audio list route."""
    return render_template("audio_list.html", files=get_files(app.config["AUDIO_FOLDER"]))

@app.route("/<path:filename>", methods=["GET"])
def audio_file(filename):
    try:
        return send_from_directory(app.config["AUDIO_FOLDER"], filename=filename, as_attachment=False)
    except FileNotFoundError:
        abort(404)

# Print server details
qrcode = pyqrcode.create(f"http://{get_ip()}:5000")
print(qrcode.terminal(quiet_zone=1))
print(f"Scan the QR code or go to the following address: http://{get_ip()}:5000")
print("Don't forget, your computer should be on the same network as your mobile device.")

# Make server available to other devices on the same network
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
app.run(debug=False, host="0.0.0.0")
