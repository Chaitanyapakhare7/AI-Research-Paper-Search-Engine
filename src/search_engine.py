import random

class PaperSearchEngine:
    def __init__(self):
        self.mock_papers = [
            {
                "title": "Attention Is All You Need",
                "abstract": "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks...",
                "row_index": 0
            },
            {
                "title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
                "abstract": "We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers...",
                "row_index": 1
            },
            {
                "title": "Generative Adversarial Nets",
                "abstract": "We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models...",
                "row_index": 2
            }
        ]

    def search(self, query: str, k: int = 5):
        results = []
        for i in range(k):
            paper = self.mock_papers[i % len(self.mock_papers)]
            results.append({
                "rank": i + 1,
                "title": f"{paper['title']} (Match)",
                "abstract": paper["abstract"],
                "score": random.uniform(0.75, 0.98),
                "row_index": paper["row_index"]
            })
        return results

    def summarize(self, abstract: str) -> str:
        return f"This paper explores a novel approach optimizing deep network architectures, shortening training times significantly."

    def extract_keywords(self, abstract: str):
        return [("transformers", 0.92), ("neural networks", 0.88), ("deep learning", 0.81)]

    def recommend_papers(self, row_index: int, top_n: int = 3):
        recommendations = []
        for i in range(top_n):
            recommendations.append({
                "title": f"Related Discovery Paper {i+1} for Index {row_index}",
                "score": random.uniform(0.60, 0.85)
            })
        return recommendations
