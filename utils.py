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
    """Convert seconds to minutes."""
    min_val = int(sec // 60)
    sec_val = int(sec % 60)
    str_val = "{:02}:{:02}".format(min_val, sec_val)

    return str_val


def get_files(directory):
    """Get files."""
    # Get all files in the directory
    filelist = os.listdir(directory)

    # Filter file types
    filelist = [ file for file in filelist if file.endswith( ('.wav', '.mp3') ) ]
    print(filelist)

    # Create files object
    files = []
    for filename in filelist:
        metadata = audio_metadata.load(os.path.join(directory, filename))
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
    get_files("audio")
