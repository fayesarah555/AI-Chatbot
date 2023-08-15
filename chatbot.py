
import openai
import time


openai.api_key = "****"

def chat_with_bot(prompt):
    try:
        response = openai.Completion.create(
            engine="davinci",  
            prompt=prompt,
            max_tokens=50  
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Chatbot: Bonjour ! Je suis votre chatbot IA. Comment puis-je vous aider aujourd'hui ?")
    
    while True:
        user_input = input("Vous : ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Au revoir !")
            break
        
        prompt = f"Vous : {user_input}\nChatbot:"
        bot_response = chat_with_bot(prompt)
        
        print("Chatbot :", bot_response)
        
        time.sleep(1)

if __name__ == "__main__":
    main()
