import api

def get_response(message: str) -> str:
    processedMessage = message.lower()

    if processedMessage == '/chucknorrisjoke':
        joke = Api.get_joke()
        return joke
    else:
        return