from flask import Flask, jsonify



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)

    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index():
        return jsonify([
            {
                "status": 1,
                "message": "server is active!"
            }
        ]), 200
    
    from api_core.routes import api
    from api_core.routes.downloader import video_extractor

    api.register_blueprint(video_extractor)

    app.register_blueprint(api)
    
    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify([{
            "status": 0,
            "message": "page not found!"
        }]), 404
    

    return app
