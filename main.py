from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes.proccess_img import proccess

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "https://creditoya.vercel.app",
    "https://creditoya-git-master-credito-yas-projects.vercel.app/",
    "https://creditoya-lnyhrc0d5-credito-yas-projects.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "CreditoYa"}


app.include_router(proccess, prefix="/processing")

load_dotenv()
