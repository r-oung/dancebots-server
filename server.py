#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""HTML file server

Starts a simple HTML server with its address generated as a QR-code.

Copyright (C) 2021 Raymond Oung

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
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

# Print license notice
print("""
dancebots-server  Copyright (C) 2021  Raymond Oung
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions. Refer to the license notice at the
top of the script.

""")

# Print server details
qrcode = pyqrcode.create(f"http://{get_ip()}:5000")
print(qrcode.terminal(quiet_zone=1))
print(f"Scan the QR code or go to the following address: http://{get_ip()}:5000")
print("Don't forget, your computer should be on the same network as your mobile device.")

# Make server available to other devices on the same network
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
app.run(debug=False, host="0.0.0.0")
