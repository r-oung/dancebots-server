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
PARSER.add_argument("path", help="Path to audio folder")
ARGS = PARSER.parse_args()

# Start webapp
app = Flask(__name__)
app.config["AUDIO_FOLDER"] = ARGS.path
# app.config["AUDIO_FOLDER"] = "static"
# app.static_url_path = ARGS.path
# app.static_folder = app.root_path + app.static_url_path

print(app.static_url_path)
print(app.static_folder)


# Define routes
@app.route("/")
def audio_list():
    """Audio list route."""
    return render_template("audio_list.html", files=get_files(app.config["AUDIO_FOLDER"]))


@app.route("/<path:filename>", methods=["GET"])
def audio_file(filename):
    try:
        # return send_from_directory(app.config["AUDIO_FOLDER"], filename=filename, mimetype="audio/mpeg, audio/wav", as_attachment=True)
        return send_from_directory(app.config["AUDIO_FOLDER"], filename=filename, as_attachment=False)
    except FileNotFoundError:
        abort(404)


# Print server details
qrcode = pyqrcode.create(f"http://{get_ip()}:5000")
print(qrcode.terminal(quiet_zone=1))
print("Scan the QR code or go to the following address: http://{get_ip()}:5000")

# Make server publicly available
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
app.run(debug=True, host="0.0.0.0")
