from yt_dlp import YoutubeDL, utils


def fetch_info(url: str):
    ydl_opts = { 'quiet': True }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            metadata = ydl.sanitize_info(ydl.extract_info(url, download= False))
            video_info = metadata.get("formats", [])

            custom_meta = [{
                "status": 1,
                "id": metadata.get("id", None),
                "title": metadata.get("title", None),
                "metadata": [
                    { "resolution": res.get("resolution", None),
                    "format_note": res.get("format_note", None),
                    "raw_url": res.get("url", None),
                    "ext": res.get("ext", None),
                    "fps": res.get("fps", None),
                    "file_size": res.get("filesize", None)
                      } for res in video_info if res.get("acodec") is not None and res.get("format_note") != "storyboard"
                ]
            }]

            return custom_meta
    except utils.DownloadError as e:
        return [{
            "status": 0,
            "message": "no media streams found or something went wrong!"
        }]