from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database
import pipeline  # ◄ Import your pipeline module here

app = FastAPI(
    title="Alpha.AI Financial Terminal Backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    database.initialize_database()

@app.get("/")
def read_root():
    return {"status": "ONLINE", "system": "Alpha.AI Sentiment Engine Core"}

# UPGRADED: Trigger pipeline on-demand when a user requests data
@app.get("/api/sentiment/{ticker}")
def get_ticker_sentiment(ticker: str):
    ticker_upper = ticker.upper()
    
    try:
        # 1. Dynamically sweep the web for fresh news and cache it
        raw_news = pipeline.fetch_live_financial_news(ticker_upper)
        pipeline.mock_ai_sentiment_processor(raw_news)
    except Exception as e:
        print(f"⚠️ Pipeline execution warning: {e}")
        # Proceeding anyway so we can fall back to whatever is cached in the DB

    # 2. Fetch records out of the database to send to your React app
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT headline, source, sentiment_score, justification, timestamp 
           FROM article_sentiment 
           WHERE ticker = ? 
           ORDER BY timestamp DESC LIMIT 10""",
        (ticker_upper,)
    )
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]