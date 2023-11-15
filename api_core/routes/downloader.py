from flask import (
    Blueprint, request, jsonify
)
from api_core.models.url_form import URLForm
from api_core.services.extractor import fetch_info


video_extractor = Blueprint('extractor', __name__, url_prefix='/extract')

44444
@video_extractor.post('/')
def extract_info():
    form = URLForm(request.form)
    if request.method == "POST" and form.validate():
        validated_url = form.url.data
        video_metadata = fetch_info(validated_url)
        if video_metadata[0].get("status", None) == 1:
            return jsonify(video_metadata), 200
        else:
            return jsonify(video_metadata), 404