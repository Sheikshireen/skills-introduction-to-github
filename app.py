from fastapi import FastAPI, UploadFile, File
from backend import predict_resume_score

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Job Hunt Copilot!"}

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    score = predict_resume_score(content.decode("utf-8"))
    return {"resume_fit_score": score}
