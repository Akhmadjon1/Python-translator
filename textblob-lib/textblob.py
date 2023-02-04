from textblob import TextBlob

add_blob = TextBlob('Easy way to translatea text in python')
print(add_blob.translate(to = 'fr'))