#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """


from urllib.request import urlopen

if __name__ == '__main__':
    with urlopen('https://intranet.hbtn.io/status') as response:
        data = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(data)))
        print('\t- content: {}'.format(data))
        print('\t- utf8 content: {}'.format(data.decode('utf-8')))
