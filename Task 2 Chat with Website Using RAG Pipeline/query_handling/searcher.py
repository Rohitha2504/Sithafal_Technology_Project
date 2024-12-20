import numpy as np  # Add this import

class Searcher:
    def __init__(self, vector_db):
        self.vector_db = vector_db  # Pass VectorDatabase object to Searcher

    def cosine_similarity(self, vec1, vec2):
        vec1 = vec1.flatten()  # Flatten the arrays to 1D
        vec2 = vec2.flatten()  # Flatten the arrays to 1D
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    def search(self, query_embedding):
        max_score = -1
        best_match_key = None
        embeddings = self.vector_db.get_embeddings()  # Get all embeddings from the vector database
        for key, embedding in embeddings.items():
            score = self.cosine_similarity(query_embedding, embedding)
            if score > max_score:
                max_score = score
                best_match_key = key
        return best_match_key
