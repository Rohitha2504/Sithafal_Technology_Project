class VectorDatabase:
    def __init__(self):
        # Initialize an empty dictionary to store embeddings
        self.embeddings = {}

    def add_embedding(self, key, embedding):
        # Add a new embedding to the database
        self.embeddings[key] = embedding

    def get_embeddings(self):
        # Return all stored embeddings
        return self.embeddings

    def get_embedding(self, key):
        # Return a specific embedding by its key
        return self.embeddings.get(key, None)
