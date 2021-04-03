import requests
from src.shopscraper.devices.Phone import Phone
from bs4 import BeautifulSoup

def mediamarkt_scrap():
    result = []
    page_number = 1
    done = False
    while not done:
        print('Scraping page ' + str(page_number))
        page = requests.get("https://www.mediamarkt.es/es/category/_smartphones-701189.html?page=" + str(page_number))
        page_number += 1
        soup = BeautifulSoup(page.content, features="lxml")
        divs = soup.find_all('div')
        page_count = 0
        for div in divs:

            if div.get('class') and 'ProductFlexBox__StyledListItem-sc-1xuegr7-0' in div.get('class') and 'cBIIIT' in div.get('class'):
                # Info que se pueda extraer del nombre
                texts = div.find_all('p')
                device = None
                for text in texts:
                    if text.get('class') and 'Typostyled__StyledInfoTypo-sc-1jga2g7-0' in text.get('class') and 'ioNsGp' in text.get('class'):
                        full_name = text.get_text()
                        parts = full_name.split(' - ')
                        if len(parts) == 1:
                            parts = parts[0].split(', ')
                        else:
                            parts = parts[1].split(', ')
                        device = name_parser(parts)

                if device is not None:
                    inner_divs = div.find_all('div')
                    order = 0
                    for cpu_div in inner_divs:
                        if cpu_div.get('class'):
                            # Info de cpu y sistema operativo
                            if 'Typostyled__StyledInfoTypo-sc-1jga2g7-0' in cpu_div.get('class') and 'jWLrAW' in cpu_div.get('class'):
                                if order == 1:
                                    device.os = cpu_div.get_text()
                                elif order == 2:
                                    device.cpu = cpu_div.get_text()
                                elif order == 3:
                                    device.cpu_speed = cpu_div.get_text()
                                order += 1
                            # Info de precios
                            elif 'UnbrandedPricestyled__Wrapper-jah2p3-6' in cpu_div.get('class') and 'ecqQxw' in cpu_div.get('class'):
                                price_spans = cpu_div.find_all('span')
                                for price_span in price_spans:
                                    if price_span.get('class'):
                                        # Se obtienen los precios, con prioridad para el precio en oferta
                                        if 'Typostyled__StyledInfoTypo-sc-1jga2g7-0' in price_span.get('class') and \
                                            'StrikeThrough__StyledStrikePriceTypo-sc-1uy074f-0' in price_span.get('class') and \
                                            (
                                                'djQnbI' in price_span.get('class') and
                                                'gaisZZ' in price_span.get('class')
                                            ) or (
                                                not device.price and
                                                'byeGwd' in price_span.get('class') and
                                                'hvGcLR' in price_span.get('class')
                                            ) or (
                                                not device.price and
                                                'bshHmK' in price_span.get('class') and
                                                'dgJmxy' in price_span.get('class')):
                                            # Transformacion del precio a flotante, evitando los finales en ".-"
                                            device.price = float(price_span.get_text().split('.–')[0])

                    result.append(device)
                    page_count += 1
        print('Devices identified: ' + str(page_count))
        if page_count == 0:
            done = True
    return result

def name_parser(name):
    phone = Phone(name[0])
    for value in name:
        if value != phone.name:
            if value in ['Negro', 'Blanco', 'Naranja', 'Verde', 'Azul', 'Rojo', 'Gris', 'Violeta', 'Blanco Glaciar', 'Malva', 'Plata', 'Grafito', 'Oro', 'Lavanda', 'Neon', 'Amarillo', 'Azul pacífico', 'Stream White', 'Verde noche']:
                phone.color = value
            elif 'GB RAM' in value:
                phone.memory = value
            elif 'GB' in value:
                phone.storage = value
            elif '"' in value:
                phone.screen = value
            elif 'mAh' in value:
                phone.battery = value
    return phone
