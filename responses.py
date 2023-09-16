import api

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '/chucknorrisjoke':
        joke = api.get_joke()
        return joke

    else:
        return ''
