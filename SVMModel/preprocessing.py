import re
import nltk
import contractions
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

def remove_stopwords(text):
    new_list = []
    words = nltk.word_tokenize(text)
    stopwrds = set(stopwords.words('english')) - {'not'}
    stopwrds.update(['d', 'm', 's', 're', 've', 'll'])

    for word in words:
        if word not in stopwrds:
            new_list.append(word)
    return ' '.join(new_list)

def remove_emojis(text):
    emoj = re.compile("["
                      u"\U0001F600-\U0001F64F"  # emoticons
                      u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                      u"\U0001F680-\U0001F6FF"  # transport & map symbols
                      u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                      u"\U00002500-\U00002BEF"  # chinese char
                      u"\U00002702-\U000027B0"
                      u"\U00002702-\U000027B0"
                      u"\U000024C2-\U0001F251"
                      u"\U0001f926-\U0001f937"
                      u"\U00010000-\U0010ffff"
                      u"\u2640-\u2642"
                      u"\u2600-\u2B55"
                      u"\u200d"
                      u"\u23cf"
                      u"\u23e9"
                      u"\u231a"
                      u"\ufe0f"  # dingbats
                      u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', text)

abbr_dict = {
    "ain t": "am not",
    "can t": "can not",
    "cannot": "can not",
    "couldn t": "could not",
    "didn t": "did not",
    "gotta": "got to",
    "hadn t": "had not",
    "hasn t": "has not",
    "haven t": "have not",
    "imma": "i am going to",
    "isn t": "is not",
    "shouldn t": "should not",
    "smthg": "some thing",
    "wasn t": "was not",
    "weren t": "were not",
    "won t": "will not",
    "wouldn t": "would not",
    "wouldn t ve": "would not have",}

def misspelled_abbreviations(text):
    text = re.sub('’', '\'', text)

    for abbr, expanded_form in abbr_dict.items():
        text = text.replace(abbr, expanded_form)

    return text

def preprocess_text(text):
    text = re.sub(r'RT @\w+:\s*|RT@\w+\s*', '', text)  # Remove RT@
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\[|\]|\(|\)|\{|\}|\<|\>|_|-', '', text)  # Remove brackets
    text = re.sub(r'\w\d\w', '', text)  # Remove characters with digits
    text = re.sub(r'\b[mf](\d+)\b', '', text, flags=re.IGNORECASE)  # Remove male/female digits
    text = re.sub(r'\b(\d+)[mf]\b', '', text, flags=re.IGNORECASE)  # Remove male/female digits
    text = contractions.fix(text)  # Fix contractions
    text = misspelled_abbreviations(text)  # misspelled_abbreviations
    text = text.replace("'", "").replace('"', '')  # Remove quotes
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Remove URLs
    text = text.replace('\n', ' ').replace('\r', '')  # Remove newlines
    text = remove_emojis(text)  # remove_emojis
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    text = remove_stopwords(text)  # remove_stopwords
    text = re.sub(r'\d+', '', text)  # Remove digits
    text = re.sub(r' +', ' ', text)  # Remove whitespaces
    return text
#print(preprocess_text("Hello \///\\\//\\\//\/\ RT@omar https://twitter.com/sopehsalah57609 😀😀😀😀")) تجربة
