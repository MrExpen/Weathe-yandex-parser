import requests
from bs4 import BeautifulSoup
import openpyxl

URL = 'https://yandex.ru/pogoda/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.104 (Edition Yx 05)'}


# URL += input('county: ')


def get_html():
    '''
    api = requests.get(URL, headers=HEADERS)
    if api.status_code == 200:
        return api.text
    print("error ocorupted")
    quit()
    '''
    with open('index.html', 'r', encoding='utf-8') as file:
        return file.read()


def parse_html():
    html = get_html()
    soup = BeautifulSoup(html, 'html.parser')
    days = []
    for item in soup.find_all('div', class_='forecast-briefly__day'):
        day = {}
        day['time'] = item.find('time').get_text(strip=True)
        tmp = item.find_all('span', class_='temp__value')
        day['day_temp'] = tmp[0].get_text(strip=True)
        day['night_temp'] = tmp[1].get_text(strip=True)
        del tmp
        day['rainfall'] = item.find('div', class_='forecast-briefly__condition').get_text(strip=True)
        days.append(day)
        del day
    return days

def save_to_xls(data, file_name='weather.xlsx'):
    pass


def main():
    days = parse_html()
    


if __name__ == '__main__':
    main()
