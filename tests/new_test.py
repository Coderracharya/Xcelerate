
import yt_dlp

url ='https://youtu.be/itKaYVbT0Ko'

ydl_opts = {
    'format': 'bestaudio',
    'quiet': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    meta = ydl.sanitize_info(ydl.extract_info(url, download=False))

#    print(json.dumps(meta))
    vid_info = meta.get("formats", [])
    custom_meta = [
            {
                "id": meta.get("id", None),
                "title": meta.get("title", None),
                "metadata": [
                    {
                        "resolution": res.get("resolution", None),
                        "raw_url": res.get("url", None),
                        "format_note": res.get("format_note", None),
                        } for res in vid_info if not res.get("url","").endswith(".m3u8")
                    ]
                }
            ]
    print(custom_meta)
