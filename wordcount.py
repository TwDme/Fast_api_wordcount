import requests
from bs4 import BeautifulSoup


def get_html_from_url(url: str) -> str:
    source_code = requests.get(url).text
    bs = BeautifulSoup(source_code, 'html.parser')
    return bs.get_text()


def create_words_list(text: str) -> list:
    cleaned_list = list([val for val in text.lower().split() if val.isalpha()])
    return cleaned_list


def wordcount(cleaned_list: list) -> dict:
    word_count = {}

    for word in cleaned_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print(word_count)
    return word_count




