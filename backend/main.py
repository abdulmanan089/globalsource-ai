from fastapi import FastAPI
from scraper import search_alibaba
from ai_filter import filter_suppliers

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GlobalSource AI is running"}

@app.get("/search")
def search(product: str):

    raw_data = search_alibaba(product)

    results = filter_suppliers(raw_data)

    return results