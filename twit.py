import json
import twitter

# python-twitter API documentation: https://python-twitter.readthedocs.io/en/latest/twitter.html

# method from Pauleuh on github

api = twitter.Api(consumer_key='put your key here',
                  consumer_secret='put your key here',
                  access_token_key='put your key here',
                  access_token_secret='put your key here',
                  sleep_on_rate_limit=True,
                  tweet_mode='extended')

def get_all_tweets_from_user(api, user_name, min_id=None):
    all_tweets = []
    if not min_id:
        first_tweets = api.GetUserTimeline(screen_name=user_name)
    else:
        first_tweets = api.GetUserTimeline(screen_name=user_name, since_id=min_id)
    if not len(first_tweets):
        return all_tweets
    all_tweets += [tweet.AsDict() for tweet in first_tweets]

    max_id = all_tweets[-1]['id']
    not_done = True
    while not_done:
        if not min_id:
            tweets = api.GetUserTimeline(screen_name=user_name, max_id=max_id)
        else:
            tweets = api.GetUserTimeline(screen_name=user_name, max_id=max_id, since_id=min_id)

        if len(tweets) > 1:

            for tweet in tweets:
                all_tweets.append(tweet.AsDict())
            max_id = str(int(all_tweets[-1]['id']) - 1)

        else:
            not_done = False
    return all_tweets


#print(api.VerifyCredentials())
#user = api.VerifyCredentials()
#print(type(user))
#print(type(user._json))
#print(json.dumps(user._json, indent=1))

#userid = 17760642
username = 'npqg_inc'
#print('UserName' + ' = ' + username)

#users = api.GetFriends(username)
#print([u.name for u in users])


for tweet in get_all_tweets_from_user(api, username, None):
    print(tweet['full_text'] + '\n--------------------------')

#statuses = api.GetUserTimeline(userid)
#for s in statuses:
#    print(s.text + '\n')

#status = api.PostUpdate('I love python-twitter!')
#print(status.text)

exit(0)
