import os
import sys
import json
import tweepy
import requests
from dotenv import load_dotenv

load_dotenv()

def post_x(text: str) -> dict:
    client = tweepy.Client(
        consumer_key=os.environ["X_API_KEY"],
        consumer_secret=os.environ["X_API_SECRET"],
        access_token=os.environ["X_ACCESS_TOKEN"],
        access_token_secret=os.environ["X_ACCESS_SECRET"],
    )
    resp = client.create_tweet(text=text)
    data = resp.data or {}
    return data


def post_linkedin(text: str) -> dict:
    access_token = os.environ["LINKEDIN_ACCESS_TOKEN"]
    person_urn = os.environ.get("LINKEDIN_PERSON_URN")

    if not person_urn:
        me_resp = requests.get(
            "https://api.linkedin.com/v2/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        me_resp.raise_for_status()
        person_urn = me_resp.json().get("id")

    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json",
    }
    body = {
        "author": f"urn:li:person:{person_urn}",
        "lifecycleState": "PUBLISHED",
        "visibility": "PUBLIC",
        "commentary": text,
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": [],
        },
    }
    resp = requests.post(
        "https://api.linkedin.com/rest/posts",
        headers=headers,
        json=body,
    )
    resp.raise_for_status()
    return {"status": "ok"}


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python social_poster.py <platform> <text>")
        print("platform: 'x' or 'linkedin' or 'both'")
        sys.exit(1)

    platform = sys.argv[1]
    text = sys.argv[2]

    results = {}
    if platform in ("x", "both"):
        results["x"] = post_x(text)
        print(f"X: posted -> {results['x']}")
    if platform in ("linkedin", "both"):
        results["linkedin"] = post_linkedin(text)
        print("LinkedIn: posted")

    print(json.dumps(results))
