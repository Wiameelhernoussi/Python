from flask import Blueprint, request, jsonify
import os
from ocr.extractor import extract_text_from_image, extract_text_from_pdf

upload_bp = Blueprint('upload_bp', __name__)

@upload_bp.route('/upload', methods=['POST'])
def upload_cv():
    file = request.files['file']
    path = os.path.join('static/uploads', file.filename)
    file.save(path)

    if file.filename.endswith('.pdf'):
        text = extract_text_from_pdf(path)
    else:
        text = extract_text_from_image(path)

    return jsonify({'text': text})
