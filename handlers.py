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


def get_listing_result(query_text):
    if query_text == "KENB":
        return get_listing("ОАО Оптима Банк")
    elif query_text == "RSBK":
        return get_listing("ОАО \"РСК Банк\"")
    elif query_text == "MAIR":
        return get_listing("ОАО \"Международный аэропорт Манас\"")
    elif query_text == "AYLB":
        return get_listing("ОАО \"Айыл Банк\"")
    elif query_text == "FKDB":
        return get_listing("ОАО \"ФинансКредитБанк КАБ\"")
    elif query_text == "ELST":
        return get_listing("ОАО Электрические станции")
    elif query_text == "KELD":
        return  get_listing("ОАО Келдике")
    elif query_text == "SELK":
        return get_listing("ОАО Северэлектро")
    elif query_text == "UCHK":
        return get_listing("ОАО Учкун")
    elif query_text == "KTEL":
        return get_listing("ОАО Кыргызтелеком")
    elif query_text == "KTTS":
        return get_listing("ОАО Кыргыз Тоо-Таш")
    elif query_text == "BTST":
        return get_listing("ОАО Бишкектеплосеть")
    elif query_text == "CHGS":
        return get_listing("ОАО Чакан ГЭС")
    elif query_text == "EHSUb":
        return  get_listing("ОсОО \"ИХСАН-ОРИКС\"")
    elif query_text == "TEPL":
        return get_listing("ОАО Тепличный")
    elif query_text == "ZLKR":
        return get_listing("ОАО Керемет Банк")
    elif query_text == "AYUUb":
        return get_listing("ОсОО Аю")
    elif query_text == "PMTBb":
        return get_listing("ОсОО Первая Металлобаза")
    elif query_text == "KICBb":
        return get_listing("ЗАО Кыргызский Инвестиционно-Кредитный Банк")
    elif query_text == "KALT":
        return get_listing("ОАО Кыргызалтын")
    elif query_text == "SALFb":
        return get_listing("ОАО Микрофинансовая компания «Салым Финанс»")
    elif query_text == "MABNb":
        return get_listing("ОАО Микрофинансовая компания АБН")
    elif query_text == "KSDB":
        return get_listing("ОАО Кыргызсуудолбоор")
    elif query_text == "FRPR":
        return get_listing("ОАО Микрокредитная компания Фонд развития предпринимательства")
    elif query_text == "BMZD":
        return get_listing("ОАО Бишкекский машиностроительный завод")
    elif query_text == "MTURb":
        return get_listing("ОАО Торговый дом Мин Туркун")
    else:
        return "По данному запросу ничего не найдено. Убедитесь в правильности введенных данных!"



def get_listing(listening):
    url = 'https://www.kse.kg/ru/Listing'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('table', class_='class1')
    tr = table.find_all('tr', class_='listing_details')
    result_table = []
    for line in tr:
        td = line.find_all('td')
        name = td[0].text
        last_price = td[2].text

        result = name + '\nПоследняя цена (сом): ' + last_price + "\n"
        result_table.append(result)

    for res in result_table:
        if res.startswith(listening):
            return res
