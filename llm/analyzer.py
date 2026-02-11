import os

def analyze_job(job):
    """
    Analyse une offre avec LLM local (ou fallback simple)
    """

    # Fallback minimal si aucun LLM
    summary = f"{job['title']} chez {job['company']} ({job['location']})"

    return {
        "summary": summary,
        "relevant": "SOC" in job["title"] or "Security" in job["title"]
    }
