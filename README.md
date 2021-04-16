# Dancebots Server
Runs a webserver on your machine so that you can play audio files from your smartphone web browser.


## Installation
```shell
git clone https://github.com/r-oung/dancebots-server.git
cd dancebot-server/
pip install -r requirements.txt
```

Alternatively, if you're using Linux or macOS, you can use the `setup.sh` script to create a virtual environment and install dependencies:
```shell
git clone https://github.com/r-oung/dancebots-server.git
cd dancebot-server/
./setup.sh
. venv/bin/activate
```


## Usage
```
python server.py /path/to/audio/files
```

Make sure you mobile device is on the same network as your computer. Scan the QR code with your mobile device (hint: iPhone's can do this using the default camera app) and select the link. Alternatively, point the browser on your mobile device to the provided HTML address.
