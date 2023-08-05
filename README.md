# CSH (Compassionate Soul Harbinger)

This project implements a Mental Health chatbot using Flask web framework and PyTorch for intent classification. The chatbot is capable of understanding user queries and providing appropriate responses based on pre-defined intents.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Starting the Web Server](#starting-the-web-server)
  - [Interacting with the Chatbot](#interacting-with-the-chatbot)
- [Training the Model](#training-the-model)
- [Built With](#built-with)
- [License](#license)

## Getting Started

### Prerequisites

Before running the chatbot, ensure you have the following installed:

- Python 3.x
- Flask
- PyTorch
- NLTK (Natural Language Toolkit)

### Installation

1. Clone this repository to your local machine.
2. Install the required Python packages using the following command:

   ```
   pip install flask torch nltk
   ```

## Usage

### Starting the Web Server

To start the Flask web server, run the following command:

```
python app.py
```

The server should now be running at `http://localhost:5000/`.

### Interacting with the Chatbot

Once the web server is running, open your web browser and go to `http://localhost:5000/`. You will see a simple chat interface.

Type your message in the text box and press Enter or click the "Send" button to interact with the chatbot. The chatbot will process your query and provide a response based on the pre-trained model.

To exit the chat, type "quit" or close the browser tab.

## Training the Model

If you wish to train the model on a new set of intents or data, follow these steps:

1. Modify the `intents.json` file to include your new intents and corresponding patterns.
2. Run the training script `train.py`:

   ```
   python train.py
   ```

   This will train the model and save the trained model data to `data.pth`.

## Built With

- [Flask](https://flask.palletsprojects.com/) - Web framework for serving the chatbot.
- [PyTorch](https://pytorch.org/) - Deep learning framework for building and training the neural network.
- [NLTK](https://www.nltk.org/) - Natural Language Toolkit for tokenization and stemming.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---
