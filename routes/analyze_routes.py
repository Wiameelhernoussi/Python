from flask import Blueprint, request, jsonify
from models.bert_engine import score_cv
from nlp.cleaner import clean_text
from detection.fraud_detector import detect_fraudulent_cv

analyse_bp = Blueprint('analyse_bp', __name__)

@analyse_bp.route('/score', methods=['POST'])
def analyse_cv():
    data = request.get_json()
    cv_text = clean_text(data['cv'])
    job_text = clean_text(data['job'])
    score = score_cv(cv_text, job_text)
    return jsonify({'score': round(score, 2)})

@analyse_bp.route('/fraud', methods=['POST'])
def detect_fraud():
    data = request.get_json()
    text = clean_text(data['cv'])
    is_fraud = detect_fraudulent_cv(text)
    return jsonify({'fraudulent': is_fraud})
