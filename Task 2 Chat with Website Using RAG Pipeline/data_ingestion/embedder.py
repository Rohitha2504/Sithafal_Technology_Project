from transformers import BertTokenizer, BertModel
import torch

class Embedder:
    def __init__(self):
        # Load tokenizer and model for BERT (or any transformer model you're using)
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')

    def preprocess_input(self, text):
        """
        Preprocess the input text by tokenizing and truncating it to fit within BERT's max length of 512 tokens.
        
        Args:
        - text (str): The input text to preprocess.
        
        Returns:
        - dict: Tokenized and padded inputs ready to be passed to the model.
        """
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
        return inputs

    def embed_text(self, text):
        """
        Embeds the input text using BERT.
        
        Args:
        - text (str): The input text to embed.
        
        Returns:
        - torch.Tensor: The embeddings of the input text (averaged across all tokens).
        """
        # Preprocess the input text
        inputs = self.preprocess_input(text)
        
        # Run the model to get the embeddings
        with torch.no_grad():  # Disable gradient calculation during inference
            outputs = self.model(**inputs)
        
        # Extract the embeddings (using the last hidden state)
        embeddings = outputs.last_hidden_state.mean(dim=1)  # Averaging the token embeddings
        
        return embeddings


