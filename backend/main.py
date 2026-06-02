from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database

app = FastAPI(
    title = "Alpha.AI Financial Terminal Backend",
    version = "1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# Initialize the SQLite tables upon application launch
@app.on_event("startup")
def startup_event():
    database.initialize_database()

@app.get("/")
def read_root():
    return {"status": "ONLINE", "system": "Alpha.AI Sentiment Engine Core"}

@app.get("/api/sentiment/{ticker}")
def get_ticker_sentiment(ticker: str):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT headline, source, sentiment_score, justification, timestamp FROM article_sentiment WHERE ticker = ? ORDER BY timestamp DESC LIMIT 10",
        (ticker.upper(),)
    )
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]
