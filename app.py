from flask import Flask
from routes.upload_routes import upload_bp
from routes.analyse_routes import analyse_bp
from routes.user_routes import user_bp

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Enregistrement des routes
app.register_blueprint(upload_bp, url_prefix="/api")
app.register_blueprint(analyse_bp, url_prefix="/api")
app.register_blueprint(user_bp, url_prefix="/api")

if __name__ == '__main__':
    app.run(debug=True)
