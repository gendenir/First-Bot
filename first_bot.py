# Python 3
import requests
token = '561799639:AAFY_F5Z5KyFTsxHVrb4NLgUIiesDelKxS0'
URL = 'https://api.telegram.org/bot' + token + '/'


def get_updates():
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    text_message = data['result'][-1]['message']['text']
    chat_id = data['result'][-1]['message']['chat']['id']

    message = {'chat_id': chat_id,
               'text': text_message}

    return message


def send_message(chat_id, text='Wait a second, please...'):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():

    answer = get_message()

    chat_id = answer['chat_id']
    text_message = answer['text']
    send_message(chat_id, text_message)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

