import requests
from bs4 import BeautifulSoup as BS4


URL = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"

RUS_ALPHABET = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
                    'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

def parser(start_url: str) -> list:

    def write_into_file(array: list) -> None:
        with open("animals_names.txt", 'a+', encoding='utf-8') as file:
            i = 0
            while i < len(array):
                if list(array[i])[0] not in RUS_ALPHABET:
                    break
                if i == len(array) - 1:
                    file.write(array[i])
                else:    
                    file.write(array[i] + "\n")
                i+=1

    def animals_request(request_url: str) -> list:
        req = requests.get(request_url)
        html = req.text
        parser = BS4(html, "html.parser")
        elements = parser.select("ul")
        list_animals = elements[2].text.split('\n')
        if 'ЖивотныеОрганизмы по алфавиту' != elements[3].text:
            return list_animals + elements[3].text.split('\n')
        return list_animals[:-1]
        
    animals = animals_request(start_url)
    write_into_file(animals)
    
    while list(animals[-1])[0] in RUS_ALPHABET:
        result = '+'.join(animals[-1].split())
        next_url = f"https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom={result}"
        arr = animals_request(next_url)
        write_into_file(arr)
        animals+=arr
    
    return animals

def counting_animals(animals_list: list) -> dict:
    count_dict = {}
    for key in RUS_ALPHABET:
        count_dict[key] = 0

    for animal in animals_list:
        for letter in RUS_ALPHABET:
            if list(animal)[0] == letter:
                count_dict[letter] += 1
    
    return count_dict

def main():
    animals = parser(URL)
    
    count_animals_dict = counting_animals(animals)
    with open("report.txt", 'w+', encoding='utf-8') as file:
        for letter in RUS_ALPHABET:
            file.write(f"{letter}: {count_animals_dict[letter]}\n")
            print(f"{letter}: {count_animals_dict[letter]}")

if __name__ == "__main__":
    main()