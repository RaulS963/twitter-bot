# twitter-bot
Simple twitter bot using tweepy

```
$ pip install -r requirements.txt
```

Authenticate to Twitter:
```python
import tweepy

auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
api = tweepy.API(auth)
```

Check if authentication is a success:
```python
try:
    api.verify_credentials()
    print("authentication success!")
except:
    print("error in authentication")
```

Upload a status or Tweet your message:
```python
api.update_status("Hello Twitter #tweepy")
```

Twitter Account Used: [@ScarletDemonic](https://twitter.com/ScarletDemonic) 
