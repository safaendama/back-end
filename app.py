from fastapi import FastAPI
import uvicorn
import pickle
from fastapi.middleware.cors import CORSMiddleware
from models import Women

app=FastAPI()



origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



model=pickle.load(open("model.sav","rb"))
@app.get("/")
def greet():
    return {"Hello World!"}


@app.post("/predict")
def predict(req:Women):
    text=req.text
    predict=model.predict([text])
    if(predict==1):
        return {"resultat" : "this tweet is disaster"}
    else:
        return { "resultat" : "this tweet is not disaster"}

if __name__=="__main__":
    uvicorn.run(app)    