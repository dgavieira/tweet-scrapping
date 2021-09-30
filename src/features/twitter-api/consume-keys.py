# Essa função tem por objetivo consumir as Consumer e User Keys do usuário genérico

def key_handler():
    api_key = input("Forneça a API KEY")
    api_key_secret = input("Forneça o API KEY SECRET")
    access_token = input("Forneça o ACCESS TOKEN")
    access_token_secret = input("Forneça o ACCESS TOKEN SECRET")

    return api_key, api_key_secret, access_token, access_token_secret