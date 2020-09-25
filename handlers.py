import requests
from bs4 import BeautifulSoup


def get_quontation():
    url = 'https://www.kse.kg/ru/Quotes'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    line = soup.find('table', class_='class1').find_all('tr', class_='parse')

    quontation = []

    for tr in line:
        td = tr.find_all('td')
        name = td[2].text
        qty_sell = td[3].text
        sell = td[4].text
        qty_buy = td[5].text
        buy = td[6].text

        if not sell:
            text = "\U0001F9F0 *Наименование* : \n\n _" + name + '_\n\n\u2757\uFE0F *Покупка*' + '\n Цена: ' + buy + \
                    '\n Количество:  ' + qty_buy
            quontation.append(text)

        if not buy:
            text = "\U0001F9F0 *Наименование* : \n\n_" + name + '_\n\n\u2757\uFE0F *Продажа*' + '\n Цена: ' + sell + \
                   '\n Количество: ' + qty_sell
            quontation.append(text)

    return quontation


def get_index():
    url = 'https://www.kse.kg/ru/IndexAndCapitalization'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    tr = soup.find('tr', 'index')
    td = tr.find_all('td')
    value = td[1].text
    index = "Индекс: " + value

    tr = soup.find('tr', 'capitalization')
    td = tr.find_all('td')
    value = td[1].text
    capitalization = "Капитализация (млн.сом): " + value

    date_cap = soup.find('th', 'date_cap').text

    return '\U0001F4C5 ' + date_cap + '\n' + index + "\n" + capitalization


def get_trade_results():
    url = 'https://www.kse.kg/ru/TradeResults'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('table', class_='class1')
    tr = table.find_all('tr', 'tradeResult')
    result = ""
    date_trade = soup.find('h3', 'tradeResult_date').text

    for line in tr:
        td = line.find_all('td')
        name = td[0].text
        money = td[1].text

        result += name + ' : ' + money + ' млн.сом ' + "\n"
    return '\U0001F4C5 ' + date_trade+'\n'+result


def get_company_trade_results():
    url = 'https://www.kse.kg/ru/TradeResults'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('table', class_='class5')
    tr = table.find_all('tr', class_='company_trade')
    result = ""

    for line in tr:
        td = line.find_all('td')
        name = td[0].text
        max_price = td[3].text
        min_price = td[4].text
        value = td[5].text
        result += '\U0001F9F0' + name + '\nMax цена: ' + max_price + '\nMin цена: ' + min_price + \
                  '\nОбъем торгов (тыс.сом): ' + value + '\n'

    return result
