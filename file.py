import pieces_copilot_sdk

def main():
    # Print "Hello World"
    print("Hello World")

    # Initialize the Pieces Copilot client
    client = pieces_copilot_sdk.client(api_key='your_api_key')

    # Define the question you want to ask
    question = "What is the capital of France?"

    # Use the Pieces Copilot client to ask the question
    response = client.askQuestion(question)

    # Print the response from the Pieces Copilot
    print("Question:", question)
    print("Response:", response)

if __name__ == "__main__":
    main()
