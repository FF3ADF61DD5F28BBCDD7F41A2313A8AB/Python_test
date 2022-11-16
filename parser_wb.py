import csv
import requests
import json

def get_product_info(result):
    list_computer_cases = result['data']['products']
    rez = {}
    for infocase in list_computer_cases:
        if infocase["name"] and infocase["brand"] and infocase["salePriceU"]:
            rez["name"] = infocase["name"]
            rez["brand"] = infocase["brand"]
            rez["price"] = int(int(infocase["salePriceU"]) / 100)
            with open("wb.csv", "a", newline="") as csvfile:
                csv.DictWriter(csvfile, fieldnames=["name", "brand", "price"],
                               dialect='excel').writerow(rez)


def main():
    url = "https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&couponsGeo=2,12,7,3,6,18,21&curr=rub&dest=-1075831,-77669,-1398615,12358317&emp=0&lang=ru&locale=ru&page=1&pricemarginCoeff=1.0&query=%D0%BA%D0%BE%D1%80%D0%BF%D1%83%D1%81%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%BE%D0%B2&reg=1&regions=80,64,83,4,38,33,70,82,69,68,86,30,40,48,1,22,66,31&resultset=catalog&sort=popular&spp=33&sppFixGeo=4&suppressSpellcheck=false"
    with open("wb.csv", "w", encoding="utf-8") as csvfile:
        csv.DictWriter(csvfile, fieldnames=["name", "brand", "price"], dialect='excel').writeheader()
    for page in range(1,8):

        response = requests.get(url=url[:167]+str(page)+url[168:])

        with open('wb.json', 'w', encoding='utf-8') as file:
            json.dump(response.json(), file, ensure_ascii=False)
        with open('wb.json', 'r', encoding='utf-8') as file:
            result = json.load(file)
            get_product_info(result)


if __name__ == "__main__":
    main()
