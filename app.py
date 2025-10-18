import os
import logging
from flask import Flask
from config import Config
from extensions import db
from models.uploaded_file import UploadedFile 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Logging configuration
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['LOG_FOLDER'], exist_ok=True)
    logging.basicConfig(
        filename=f"{app.config['LOG_FOLDER']}/app.log",
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s'
    )

    # Create database tables
    with app.app_context():
        db.create_all()

    # Register blueprints
    from controllers.file_controller import file_bp
    app.register_blueprint(file_bp)


    return app

app = create_app()

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True, use_reloader=False)

