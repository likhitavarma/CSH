# mental_health_chatbot.py
import random
import json

import torch
import nltk

nltk.download('punkt')
from mental_health_model import MentalHealthModel
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('mental_health_intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "mental_health_data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = MentalHealthModel(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "MentalHealthBot"


def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                # Check if there's a context and append it to the response if present
                context = intent.get('context', '')
                return response + ' ' + context if context else response

    return "I'm sorry, I couldn't understand that. If you need help, please reach out to a mental health professional."


if __name__ == "__main__":
    print("MentalHealthBot: How can I assist you today? (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input == "quit":
            break

        response = get_response(user_input)
        print(f"{bot_name}: {response}")
