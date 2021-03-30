import nltk
import os
import regex
import gspread
#nltk.download('stopwords')

#Cleaning Data functions

#Returns a URLS list from text and removes them from the list
def remove_urls(tweet_list):

    tweet_links = []
    urls = regex.compile(r'https?://\S+')
    for temp in range(1,len(tweet_list)):
        tweet_links.append(regex.findall(r'https?://\S+',tweet_list[temp][3]))

        tweet_list[temp][3] = (urls.sub(r'',tweet_list[temp][3]))
    
    return tweet_list,tweet_links

#Returns a emojis list from text and removes them from the list
def remove_emojis(tweet_list):

    tweet_emojis = []

    emojis = regex.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=regex.UNICODE)
    for temp in range(1,len(tweet_list)):
        if emojis.search(tweet_list[temp][3]) == None:
            tweet_emojis.append(False)
        else:
            tweet_emojis.append(True)
        tweet_list[temp][3] = emojis.sub(r'',tweet_list[temp][3])
    return tweet_list,tweet_emojis

def main():

    #Currently only works on Alek's computer, will add dynamic credentials finding later
    to_path = os.path.join( os.getcwd(), '.vscode\social-media-privacy-bot-sheet-40065e2a0d5b.json')
   
    gc = gspread.service_account(filename=to_path)
    tweet_sheet = gc.open("tweet_data")
    
    ham_tweet_sheet = tweet_sheet.get_worksheet(0)
    spam_tweet_sheet = tweet_sheet.get_worksheet(2)

    ham_tweet_list = ham_tweet_sheet.get_all_values()
    spam_tweet_list = spam_tweet_sheet.get_all_values()
    
    ham_tweet_list,ham_tweet_links = remove_urls(ham_tweet_list)
    ham_tweet_list,ham_emojis = remove_emojis(ham_tweet_list)

    spam_tweet_list,spam_tweet_links = remove_urls(spam_tweet_list)
    spam_tweet_list,spam_emojis = remove_emojis(spam_tweet_list)

if __name__ == "__main__":
    main()