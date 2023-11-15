from yt_dlp import YoutubeDL
import json


def fetch_info(url: str):
    ydl_opts = {}
    with YoutubeDL(ydl_opts) as ydl:
        metadata = ydl.sanitize_info(ydl.extract_info(url, download = False))
        video_format = metadata.get("formats", [])
        # video_res = video_format[0].get("resolution", [])

        # video_res = [res.get("format", []) for res in video_format]
        # video_res = [res.get("resolution", []) for res in video_format]
        video_id = metadata.get("id", None)
        video_title = metadata.get("title", None)


        custom_metadata = [{ "resolution": res.get("resolution", None),
                            "format_note": res.get("format_note", None),
                             "extension": res.get("ext", None),
                              "fps": res.get("fps", None),
                               "file_size": res.get("filesize", None) } for res in video_format if res.get("acodec") is not None and res.get("format_note") != "storyboard"]

        return {
            "title": video_title,
            "ID": video_id,
            "metadata" : custom_metadata,
                            }
    

output = fetch_info("https://youtu.be/9Gv2TGDnHJg?si=andrmbVu9unj3wiu")

print(output)