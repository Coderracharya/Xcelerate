from yt_dlp import YoutubeDL, utils

def fetch_info(url: str):
    ydl_opts = { 'quiet': True,
                'netrc': True,
                         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3' 
                         }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            metadata = ydl.sanitize_info(ydl.extract_info(url, download=False))
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
                    "file_size": res.get("filesize", None),
                    "video_codec": res.get("vcodec", None),
                    "audio_codec": res.get("acodec", None)
                      } for res in video_info if not res.get("acodec") == "none" 
                      and not res.get("url","").endswith(".m3u8") 
                      and not res.get("format_note", "") == "storyboard"
                ],
                "thumbnail": metadata.get("thumbnail", None)
            }]

            return custom_meta
    except utils.DownloadError as e:
        return [{
            "status": 0,
            "message": "no media streams found or something went wrong!"
        }]

