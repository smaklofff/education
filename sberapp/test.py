import requests


def download_new_schedule(link, path):
    try:
        page = requests.get(link)
        with open(path, mode='wb') as output_file:
            output_file.write(page.content)
    except Exception as exp:
        print('Не получилось скачать расписание:' + str(exp))


if __name__ == '__main__':
    download_new_schedule('https://rasp.dmami.ru/semester.json', 'data/data.json')