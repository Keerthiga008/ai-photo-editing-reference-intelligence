from __future__ import annotations

class FaissIndex:
    """Vector index stub for reference matching and similarity search."""

    def __init__(self, dimension: int = 512):
        self.dimension = dimension
        self.items: list[tuple[str, list[float]]] = []

    def add_reference(self, reference_id: str, embedding: list[float]) -> None:
        if len(embedding) != self.dimension:
            raise ValueError(f"Embedding dimension mismatch: expected {self.dimension}, got {len(embedding)}")
        self.items.append((reference_id, embedding))

    def search(self, query_embedding: list[float], limit: int = 5):
        if len(query_embedding) != self.dimension:
            raise ValueError(f"Query dimension mismatch: expected {self.dimension}, got {len(query_embedding)}")

        results = []
        for reference_id, embedding in self.items:
            score = sum(a * b for a, b in zip(query_embedding, embedding))
            results.append((reference_id, score))

        return sorted(results, key=lambda item: item[1], reverse=True)[:limit]
