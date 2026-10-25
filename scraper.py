
import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TWITTERAPIS_KEY")
URL = "https://api.twitterapis.com/twitter/tweet/advanced_search"

# Batas keamanan: maksimal 100 panggilan API
MAX_CALLS = 100
MAX_PAGES_PER_QUERY = 25

QUERIES = [
    '"PPh Pasal 22"',
    '"pajak marketplace"',
    '"pajak seller"',
    '"pajak penjual online"',
]

if not API_KEY:
    raise ValueError(
        "API key tidak ditemukan. Periksa file .env"
    )

headers = {"Authorization": f"Bearer {API_KEY}"}

posts = []
seen_ids = set()
calls = 0

for query in QUERIES:
    cursor = None
    seen_cursors = set()

    print(f"\nMemulai pencarian: {query}")

    for page in range(MAX_PAGES_PER_QUERY):
        if calls >= MAX_CALLS:
            print("Batas panggilan API tercapai.")
            break

        params = {
            "query": query,
            "product": "Latest"
        }

        if cursor:
            params["cursor"] = cursor

        try:
            response = requests.get(
                URL,
                headers=headers,
                params=params,
                timeout=30
            )
            calls += 1

            if response.status_code != 200:
                print("API error:", response.status_code)
                print(response.text[:300])
                break

            result = response.json()
            tweets = result.get("tweets") or []

            if not tweets:
                print("Tidak ada post lagi.")
                break

            added = 0

            for tweet in tweets:
                tweet_id = (
                    tweet.get("id")
                    or tweet.get("rest_id")
                )

                if not tweet_id or tweet_id in seen_ids:
                    continue

                seen_ids.add(tweet_id)

                author = tweet.get("author") or {}

                posts.append({
                    "id": tweet_id,
                    "tanggal": (
                        tweet.get("created_at")
                        or tweet.get("createdAt")
                    ),
                    "username": author.get("username", ""),
                    "teks": tweet.get("text", ""),
                    "kata_kunci": query
                })

                added += 1

            print(
                f"API {calls}/{MAX_CALLS} | "
                f"Halaman {page + 1} | "
                f"Post: {len(tweets)} | "
                f"Data unik baru: {added}"
            )

            next_cursor = result.get("next_cursor")

            if not next_cursor:
                print("Halaman pencarian selesai.")
                break

            if next_cursor in seen_cursors:
                print("Cursor berulang, pencarian dihentikan.")
                break

            seen_cursors.add(next_cursor)
            cursor = next_cursor

            time.sleep(0.5)

        except requests.RequestException as error:
            print("Koneksi bermasalah:", error)
            break

    if calls >= MAX_CALLS:
        break

df = pd.DataFrame(
    posts,
    columns=[
        "id", "tanggal", "username",
        "teks", "kata_kunci"
    ]
)

if not df.empty:
    df = df.drop_duplicates(subset=["id"])
    df = df[df["teks"].fillna("").str.strip() != ""]

df.to_csv(
    "hasil_scraping.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\n=== HASIL SCRAPING ===")
print("Total panggilan API:", calls)
print("Total post unik:", len(df))
print("Perkiraan biaya API: $", f"{calls * 0.0008:.4f}")
print("File tersimpan: hasil_scraping.csv")
