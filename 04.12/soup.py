# from bs4 import BeautifulSoup

# html = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#   <meta charset="UTF-8">
#   <title>First HTML Page</title>
# </head>
# <body>
#   <div id="first">
#     <h3 data-example="yes">hi</h3>
#     <p>more text.</p>
#   </div>
#   <ol>
#     <li class="special">This list item is special.</li>
#     <li class="special">This list item is also special.</li>
#     <li>This list item is not special.</li>
#   </ol>
#   <div data-example="yes">bye</div>
# </body>
# </html>
# """

# soup = BeautifulSoup(html, "html.parser")
# print(type(soup))
# print(soup.body)
# print(soup.body.div)

# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokas = soup.find('div', class_ = 'headline')
# print(blokas.prettify())

# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokas = soup.find('div', class_ = 'headline')

# kategorija = blokas.find('div', class_ = 'headline-category').text.strip()
# tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
# linkas = blokas.find('a', class_="CBarticleTitle")['href']

# print(kategorija)
# print(tekstas)
# print(linkas)

# import csv

# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai/samsung').text
# soup = BeautifulSoup(source, 'html.parser')

# blokai = soup.find_all('div', class_ = 'mobiles-product-card card card__product card--anim js-product-compare-product')

# with open("Telia Samsung telefonai.csv", "w", encoding="UTF-8", newline='') as failas:
#     csv_writer = csv.writer(failas)
#     csv_writer.writerow(['Modelis', 'Mėnesio kaina', 'Kaina'])

#     for blokas in blokai:
#         try:
#             pavadinimas = blokas.find('a', class_ = 'mobiles-product-card__title js-open-product').text.strip()
#             men_kaina = blokas.find('div', class_ = 'mobiles-product-card__price-marker').text.strip()
#             kaina = blokas.find_all('div', class_ = 'mobiles-product-card__price-marker')[1].text.strip()
#             print(pavadinimas, men_kaina, kaina)
#             csv_writer.writerow([pavadinimas, men_kaina, kaina])
#         except:
#             pass

import csv
from bs4 import BeautifulSoup
import requests

base_url = 'https://www.telia.lt/prekes/mobilieji-telefonai'
brand = 'samsung'

with open("Telia Samsung telefonai.csv", "w", encoding="UTF-8", newline='') as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow(['Modelis', 'Mėnesio kaina', 'Kaina'])

    page = 1
    while True:
        if page == 1:
            url = f"{base_url}/{brand}"
        else:
            url = f"{base_url}/{brand}?page={page}"
        
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'html.parser')
        blokai = soup.find_all('div', class_ = 'mobiles-product-card card card__product card--anim js-product-compare-product')
        
        for blokas in blokai:
            try:
                pavadinimas = blokas.find('a', class_ = 'mobiles-product-card__title js-open-product').text.strip()
                men_kaina = blokas.find('div', class_ = 'mobiles-product-card__price-marker').text.strip()
                kaina = blokas.find_all('div', class_ = 'mobiles-product-card__price-marker')[1].text.strip()
                print(pavadinimas, men_kaina, kaina)
                csv_writer.writerow([pavadinimas, men_kaina, kaina])
            except:
                pass

        next_page = soup.find('a', class_='pagination__link js-pagination-next')
        if not next_page or next_page.has_attr('disabled'):
            break
        
        page += 1







