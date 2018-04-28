# Python 3
import requests
import my
import json
token = my.token
URL = 'https://api.telegram.org/bot' + token + '/'


def get_updates():
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    with open('updates.json', 'w') as file:
         json.dump(data, file, indent=2, ensure_ascii=False)

    message = {'chat_id': data['result'][-1]['message']['chat']['id'],
               'text': data['result'][-1]['message']['text']}
    return message


def send_message(chat_id, text='Wait a second, please...'):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    # d = getUpdates()

    answer = get_message()
    chat_id = answer['chat_id']
    text_message = answer['text']
    send_message(chat_id, text_message)


if __name__ == '__main__':
    try:
        main()
    finally:
        exit()


