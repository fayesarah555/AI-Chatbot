
import openai
import time

# Set your OpenAI API key here
openai.api_key = "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"

def chat_with_bot(prompt):
    try:
        response = openai.Completion.create(
            engine="davinci",  # You can choose different engines like "davinci", "curie", etc.
            prompt=prompt,
            max_tokens=50  # You can adjust this value to control the response length
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Chatbot: Hello! I'm your AI chatbot. How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        prompt = f"You: {user_input}\nChatbot:"
        bot_response = chat_with_bot(prompt)
        
        print("Chatbot:", bot_response)
        
        # Introduce a delay of 1 second between responses
        time.sleep(1)

if __name__ == "__main__":
    main()
