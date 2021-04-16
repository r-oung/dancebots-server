# -*- coding: utf-8 -*-
import os
import socket
import audio_metadata

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
    """Convert seconds to minutes.
    
    """
    min_val = int(sec // 60)
    sec_val = int(sec % 60)
    str_val = "{:02}:{:02}".format(min_val, sec_val)

    return str_val


def get_files(path):
    """Get files from a specified path.
    
    """
    # Get all files in the path
    filelist = os.listdir(path)

    # Filter file types
    filelist = [ file for file in filelist if file.endswith( ('.mp3', '.wav', '.ogg') ) ]

    # Create files object
    files = []
    for filename in filelist:
        metadata = audio_metadata.load(os.path.join(path, filename))
        files.append(
            {
                "name": filename,
                "size": "{:02}".format(round(metadata.filesize / 1048576, 2)),
                "duration": sec2min(metadata.streaminfo.duration),
                "metadata": metadata,
            }
        )

    return files


if __name__ == "__main__":
    """Tests"""
    print(get_ip())

    print(sec2min(1))
    print(sec2min(10))
    print(sec2min(100))
    print(sec2min(1000))

    print(get_files("data"))

