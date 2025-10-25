from newspaper import Article

# --- Your existing functions are here ---


def extract_article_text(url: str) -> dict:
    # (no changes to this function)
    try:
        article = Article(url)
        article.download()
        article.parse()
        return {
            "title": article.title,
            "text": article.text,
            "authors": article.authors,
            "publish_date": (
                article.publish_date.isoformat() if article.publish_date else None
            ),
        }
    except Exception as e:
        return {"error": str(e)}


def extract_from_urls(urls: list[str]) -> list[dict]:
    # (no changes to this function)
    return [extract_article_text(url) for url in urls]


# --- Add this new part to the end of your script ---
if __name__ == "__main__":
    # 1. Create a list of websites for Derek to crawl
    ai_research_sites = [
        "https://arxiv.org/list/cs.AI/recent",  # For latest AI research papers
        "https://www.technologyreview.com/artificial-intelligence/",
        "https://blog.google/technology/ai/",
        "https://openai.com/blog",
        "https://quantum.country",
        "https://ocw.mit.edu/courses/physics",
        "https://www.w3schools.com",
        "https://www.freecodecamp.org",
        "https://qiskit.org",
    ]

    print("Starting article extraction...")
    # 2. Call your function with the list of URLs
    extracted_data = extract_from_urls(ai_research_sites)

    # 3. Print the results to see what was gathered
    for i, data in enumerate(extracted_data):
        print(f"--- Result from URL {i+1} ---")
        if "error" in data:
            print(f"Error: {data['error']}")
        else:
            print(f"Title: {data['title']}")
            print(f"Publish Date: {data['publish_date']}")
            # Print the first 200 characters of the text as a preview
            print(f"Text Preview: {data['text'][:200]}...")
        print("\n")

# ==============================================================================
# © 2025 Everett Nathaniel Christman & Misty Gail Christman
# The Christman AI Project — Luma Cognify AI
# All rights reserved. Unauthorized use, replication, or derivative training 
# of this material is prohibited.
# Core Directive: "How can I help you love yourself more?" 
# Autonomy & Alignment Protocol v3.0
# ==============================================================================
