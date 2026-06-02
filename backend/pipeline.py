import feedparser
import urllib.parse
import database

def fetch_live_financial_news(ticker: str):
    """
    Connects to the real-time financial RSS channel, extracts the 5 most
    recent breaking headlines for a specific asset ticker, and cleans the text strings.
    """
    print(f"📡 Initiating real-time news sweep for asset: {ticker.upper()}...")
    
    # 1. Format the search string cleanly to safely handle symbols like '$'
    query_string = urllib.parse.quote(f"{ticker} stock news")
    rss_url = f"https://news.google.com/rss/search?q={query_string}&hl=en-US&gl=US&ceid=US:en"
    
    # 2. Parse the remote data stream
    feed = feedparser.parse(rss_url)
    
    extracted_records = []
    
    # 3. Process only the top 5 freshest headlines to minimize API compute costs later
    for entry in feed.entries[:5]:
        record = {
            "ticker": ticker.upper(),
            "headline": entry.title,
            "source": getattr(entry, 'source', {}).get('text', 'Financial Network')
        }
        extracted_records.append(record)
        
    print(f"✅ Successfully ingested {len(extracted_records)} raw headlines for evaluation.")
    return extracted_records

def mock_ai_sentiment_processor(news_records):
    """
    Temporary Processing Module: Simulated AI scoring engine to verify data 
    routing paths before we bind our production LLM API keys.
    """
    conn = database.get_db_connection()
    cursor = conn.cursor()
    
    for record in news_records:
        # Check if we have already evaluated this specific headline to avoid duplicates
        cursor.execute("SELECT id FROM article_sentiment WHERE headline = ?", (record["headline"],))
        if cursor.fetchone():
            continue  # Skip processing if cached in our SQLite environment
            
        # Simulated Metrics (We will replace this with the LLM API next!)
        simulated_score = 0.5 if "up" in record["headline"].lower() or "profit" in record["headline"].lower() else -0.2
        simulated_justification = "Automated keyword scan detected structural market indicators within text string."
        
        # Save straight to our operational database
        cursor.execute('''
            INSERT INTO article_sentiment (ticker, headline, source, sentiment_score, justification)
            VALUES (?, ?, ?, ?, ?)
        ''', (record["ticker"], record["headline"], record["source"], simulated_score, simulated_justification))
        
    conn.commit()
    conn.close()
    print("💾 Analysis cache written to local SQLite database instance.")

if __name__ == "__main__":
    # Test execution path to verify everything routes cleanly
    raw_news = fetch_live_financial_news("NVDA")
    mock_ai_sentiment_processor(raw_news)