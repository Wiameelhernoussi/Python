from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def score_cv(cv_text, job_offer_text):
    cv_embedding = model.encode(cv_text, convert_to_tensor=True)
    job_embedding = model.encode(job_offer_text, convert_to_tensor=True)
    score = util.pytorch_cos_sim(cv_embedding, job_embedding)
    return float(score[0][0])


