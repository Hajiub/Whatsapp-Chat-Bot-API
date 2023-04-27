# Whatsapp Chat Bot API
This API provides a Whatsapp chat bot that answers questions based on OpenAI's GPT-3 engine.

## Getting Started
To use this API, you need to have a Twilio account set up and a WhatsApp Sandbox Channel configured. You also need to set up an OpenAI account and obtain an API key.

## Clone this repository and install the required dependencies by running:


``` bash 
pip install -r requirements.txt
```
## Create a .env file with your Twilio and OpenAI credentials:



```bash
OPENAI_API_KEY=your_api_key
```
## Start the server:

```bash
python main.py
```
## Usage
Send a POST request to the root endpoint / with the question in the request body in the following format:

```json
{
    "question": "What is the capital of France?"
}
```
The API will respond with a Twilio MessagingResponse object containing the answer:

```xml
<Response>
    <Message>Paris</Message>
</Response>
```
## Acknowledgements
This API was built using FastAPI, Pydantic, Twilio and OpenAI.

## License
This project is licensed under the MIT License - see the LICENSE file for details.