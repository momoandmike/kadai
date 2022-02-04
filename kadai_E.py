import requests
import time


def requests_top():
    top_url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
    response = requests.get(top_url)
    dic = response.json()


def main():
    requests_top()


if __name__ == '__main__':
    main()
