import HTMLParser
html_parser = HTMLParser.HTMLParser()
origi_tweet = "I luv my &lt;3 iphone &amp; you’re awsm apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com"
tweet  = html_parser.unescape(origi_tweet)
#print(tweet)
