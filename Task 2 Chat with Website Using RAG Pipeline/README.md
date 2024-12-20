## Chat with Website using RAG Pipeline

## Project Overview
This project implements a Retrieval-Augmented Generation (RAG) pipeline enabling conversational AI using data extracted from websites. The system processes semi-structured web data, embeds relevant content, and generates responses using a large language model (LLM).
## Watch below video for more guidance
## https://youtu.be/Y5uIMEmIQJU

## Features
- **Web Scraping:** Extracts data from specified URLs.
- **Data Processing:** Segments and cleans text data.
- **Embedding Generation:** Creates embeddings using SentenceTransformers.
- **Vector Search:** Utilizes FAISS for similarity search.
- **Response Generation:** Uses OpenAI’s API for dynamic responses.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/Chat-with-Website-RAG
   ```
2. Navigate to the project directory:
   ```bash
   cd Chat-with-Website-RAG
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
- Update the `config.py` file with:
  - API keys for OpenAI
  - Relevant paths and parameters

## Usage
1. Run the main application:
   ```bash
   python main.py
   ```
2. Enter the target URLs for crawling.
3. Ask questions based on the extracted content.

## Project Structure
```
📂 Chat-with-Website-RAG
 ├── data_ingestion
 │   ├── scraper.py
 ├── embeddings
 │   ├── embedding_model.py
 │   ├── vector_database.py
 ├── response_generation
 │   ├── llm_integration.py
 ├── main.py
 ├── requirements.txt
 └── README.md
```

## Technologies Used
- **Python Libraries:** BeautifulSoup, SentenceTransformers, FAISS, OpenAI API
- **Environment:** Python 3.9+

## Contribution
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgements
- OpenAI for API support
- Hugging Face for embedding models
- FAISS for vector search functionality

---
Feel free to reach out for questions or contributions!

