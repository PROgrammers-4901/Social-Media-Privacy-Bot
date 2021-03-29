import nltk
import regex

nltk.download('stopwords')

def remove_urls(text):
    urls = regex.compile(r'https?://\S+')
    return urls.findall(r'',text[3])

def main