from google_play_scraper import reviews, Sort
import pandas as pd
from datetime import datetime

def scrape_reviews(app_id, start_date, end_date, max_reviews=1000):
    all_reviews = []
    continuation_token = None

    while len(all_reviews) < max_reviews:
        result, continuation_token = reviews(
            app_id,
            lang="id",
            country="id",
            sort=Sort.NEWEST,
            count=200,
            continuation_token=continuation_token
        )

        if not result:
            break

        for r in result:
            review_date = r["at"].date()
            if start_date <= review_date <= end_date:
                all_reviews.append({
                    "Ulasan": r["content"],
                    "Tanggal": review_date
                })

        if continuation_token is None:
            break

    return pd.DataFrame(all_reviews)
