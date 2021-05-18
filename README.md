# Dancebots Server
Runs a web-server on your machine so that you can play audio files from your smartphone's web browser.

## Setup
Clone the repository and install dependencies:
```shell
git clone https://github.com/r-oung/dancebots-server.git
cd dancebot-server/
pip install -r requirements.txt
```

## Usage
Connect your mobile device to the same Wi-Fi network as your machine. Then run:
```shell
python server.py /path/to/audio/files
```

Scan the QR code with your mobile device (hint: iPhone's can do this using the default camera app) and select the link. Alternatively, point the browser on your mobile device to the provided HTML address.
