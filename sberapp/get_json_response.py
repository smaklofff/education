import os
import json
from argparse import ArgumentParser
import requests


# def cmd_args():
#     parser = ArgumentParser()
#     parser.add_argument('--group-number', dest='GROUP_NUMBER',
#                         help='\'report\' value from reports.json file',
#                         required=True)
#     return parser.parse_args()


def readJsonConfigFile(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(current_dir, filename), 'r', encoding='utf-8') as file:
            return json.loads(file.read())
    except FileNotFoundError as exc:
        print('Cant find json config file with name: ' +
              filename + ' Error: ' + str(exc))
        raise
    except Exception as exc:
        print('Cant find json config file with name: ' +
              filename + ' Error: ' + str(exc))
        raise


def checkArgValues(group, group_number):
    if group not in group_number:
        print('Invalid OUTPUT value: ' + group)
        return False
    return True


def download_new_schedule(link):
    page = requests.get(link)
    path = 'data/data.json'
    with open(path, mode='wb') as output_file:
        output_file.write(page.content)


def get_answer(group, file_json):
    return file_json['contents'][group]


def get_schedule_json(group):
    file_json = readJsonConfigFile('data/data.json')
    group_number = file_json['contents'].keys()
    # args = cmd_args()
    if checkArgValues(group, group_number):
        return get_answer(group, file_json)
    return "Error, the key doesn't exist. Check your number of group"


# if __name__ == '__main__':
#     get_schedule()
#     # download('https://rasp.dmami.ru/semester.json')

# py -3.8 test.py --group-number 201-363
