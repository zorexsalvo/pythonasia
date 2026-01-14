import json

import requests
from django.core.cache import cache

from config.environment import settings


class PretalxService:
    def __init__(self, base_url: str | None = None):
        self.base_url = base_url or settings.PRETALX.BASE_URL.rstrip("/")
        self.headers = {
            "Content-Type": "application/json",
        }

    def get_event(self, event_slug: str):
        url = f"{self.base_url}/api/events/{event_slug}/"
        response = requests.get(url, headers=self.headers)
        return response.json() if response.ok else response.raise_for_status()

    def get_submissions(self, event_slug: str):
        cache_key = f"pretalx_submissions_{event_slug}"
        cached = cache.get(cache_key)
        if cached:
            return cached
        url = f"{self.base_url}/api/events/{event_slug}/submissions/?page_size=999"
        response = requests.get(url, headers=self.headers)
        data = response.json() if response.ok else response.raise_for_status()
        cache.set(cache_key, data)
        return data

    def get_speakers(self, event_slug: str):
        try:
            cache_key = f"pretalx_speakers_{event_slug}"
            cached = cache.get(cache_key)
            if cached:
                return cached

            url = f"{self.base_url}/api/events/{event_slug}/speakers/?page_size=999"
            response = requests.get(url, headers=self.headers)
            data = response.json() if response.ok else response.raise_for_status()

            submissions = self.get_submissions(event_slug)
            confirmed_codes = {sub["code"] for sub in submissions.get("results", []) if sub.get("state") == "confirmed"}

            data["results"] = [
                speaker
                for speaker in data.get("results", [])
                if any(code in confirmed_codes for code in speaker.get("submissions", []))
            ]
            cache.set(cache_key, data)
            return data
        except requests.RequestException:
            return {"results": []}

    def get_talks(self, event_slug: str):
        url = f"{self.base_url}/api/events/{event_slug}/talks?limit=999&state=confirmed"
        response = requests.get(url, headers=self.headers)
        return response.json() if response.ok else response.raise_for_status()

    def update_submission(self, event_slug: str, submission_id: str, data: dict):
        url = f"{self.base_url}/api/events/{event_slug}/submissions/{submission_id}/"
        response = requests.patch(url, json=data, headers=self.headers)
        return response.json() if response.ok else response.raise_for_status()

    def send_feedback(self, event_slug: str, submission_id: str, feedback: dict):
        url = f"{self.base_url}/api/events/{event_slug}/submissions/{submission_id}/feedback/"
        response = requests.post(url, json=feedback, headers=self.headers)
        return response.json() if response.ok else response.raise_for_status()

    def get_sessions(self, event_slug: str):
        url = f"{self.base_url}/api/events/{event_slug}/sessions/"
        response = requests.get(url, headers=self.headers)
        return response.json() if response.ok else response.raise_for_status()
