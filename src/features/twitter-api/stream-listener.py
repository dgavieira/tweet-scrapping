import tweepy as tw

class MinhaStreamListener(tw.StreamListener):
    def on_status(self, status):
        print(status.user.screen_name)
        print(status.text)
        print('-------')
        print('\n')


if __name__ == '__main__':
    auth = tw.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tw.API(auth)
    rules = [
        {"value": "COVID lang:pt", "tag": "Covid rule"},
        {"value": "Saúde lang:pt", "tag": "Health rule"},
        {"value": "Vacina lang:pt", "tag": "Vaccine rule"}
    ]

        
