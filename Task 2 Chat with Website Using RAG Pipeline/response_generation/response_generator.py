class ResponseGenerator:
    def generate_response(self, query, context):
        return f"Query: {query}\nAnswer: Based on the data, the answer is {context}."

if __name__ == "__main__":
    generator = ResponseGenerator()
    query = "What is the capital of France?"
    context = "Paris"
    response = generator.generate_response(query, context)
    print(response)
