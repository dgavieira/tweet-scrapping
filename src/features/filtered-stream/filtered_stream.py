import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAAjMUAEAAAAA2IWgeYyQiRquudLkflANYmEIpZc%3DsxgYF5XckTGklaXBuuPbS8V3liLqnlpd6Lt5J8dS5JyAeSuXXt'


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r


def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(delete):
    # You can adjust the rules if needed
    sample_rules = [
        {"value": "COVID lang:pt", "tag": "Covid rule"},
        {"value": "Saúde lang:pt", "tag": "Health rule"},
        {"value": "Vacina lang:pt", "tag": "Vaccine rule"}
    ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(set):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    counter = 0
    lista = []
    textfile = open("tweets.json", "w")
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            #json_object = json.dumps(json_response, indent=4, sort_keys=True)
        if counter <= 2000:
            #print(counter)
            json_object = json.dumps(json_response, indent=4, sort_keys=True)
            print(counter)
            lista.append(str(json_object))
            counter = counter + 1
        else:
            for elemento in lista:
                textfile.write(elemento + "\n")
            textfile.close()
            break

        '''
        with open("tweets.json", "w") as outfile:
            outfile.write(json_object)
        # print(json.dumps(json_response, indent=4, sort_keys=True))
        counter = counter + 1
        if counter <= 10:
            print(counter)
        else:
            outfile.close()
            print("acabou")
            break
        '''

def main():
    rules = get_rules()
    delete = delete_all_rules(rules)
    set = set_rules(delete)
    get_stream(set)


if __name__ == "__main__":
    main()