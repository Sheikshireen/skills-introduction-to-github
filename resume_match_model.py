from sentence_transformers import SentenceTransformer, util

# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example job description
job_description = "We are hiring a Python backend developer with FastAPI experience."

def predict_resume_score(resume_text):
    # Embed both job description and resume
    job_embed = model.encode(job_description, convert_to_tensor=True)
    resume_embed = model.encode(resume_text, convert_to_tensor=True)
    
    # Compute cosine similarity
    score = util.cos_sim(job_embed, resume_embed)
    return float(score[0][0]) * 100  # return percentage match
