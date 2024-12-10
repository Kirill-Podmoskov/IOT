def translit_to_eng(s):
    translit_dict = {
        "а": "a", "б": "b", "в": "v", "г": "g", "д": "d",
        "е": "e", "ё": "e", "ж": "zh", "з": "z", "и": "i",
        "й": "y", "к": "k", "л": "l", "м": "m", "н": "n",
        "о": "o", "п": "p", "р": "r", "с": "s", "т": "t",
        "у": "u", "ф": "f", "х": "kh", "ц": "ts", "ч": "ch",
        "ш": "sh", "щ": "shch", "ы": "y", "э": "e", "ю": "yu",
        "я": "ya", "ь": "", "ъ": "", " ": "-"
    }
    result = "".join(translit_dict.get(char, char) for char in s.lower())
    return result

while True:
    name = input("Введите имя и фамилию (или оставьте строку пустой для выхода): ")
    if not name:
        break
    slug = translit_to_eng(name)
    print(f"Slug: {slug}")

class CommonUtils:
    @staticmethod
    def translit_to_eng(s):
        translit_dict = {
            "а": "a", "б": "b", "в": "v", "г": "g", "д": "d",
            "е": "e", "ё": "e", "ж": "zh", "з": "z", "и": "i",
            "й": "y", "к": "k", "л": "l", "м": "m", "н": "n",
            "о": "o", "п": "p", "р": "r", "с": "s", "т": "t",
            "у": "u", "ф": "f", "х": "kh", "ц": "ts", "ч": "ch",
            "ш": "sh", "щ": "shch", "ы": "y", "э": "e", "ю": "yu",
            "я": "ya", "ь": "", "ъ": "", " ": "-"
        }
        result = "".join(translit_dict.get(char, char) for char in s.lower())
        return result

    @staticmethod
    def save_to_file(file_name, slug_list):
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("\n".join(slug_list))

from commonUtils import CommonUtils

class SlugConverter:
    def __init__(self):
        self.__file_name = input("Введите название файла для сохранения: ")
        print(f"Данные будут сохранены в файл: {self.__file_name}")
        self.__slug_list = []
        self.run()

    def run(self):
        while True:
            name = input("Введите имя и фамилию известного человека (или оставьте строку пустой для выхода): ")
            if not name:
                break
            slug = CommonUtils.translit_to_eng(name)
            self.__slug_list.append(slug)
            print(f"Slug: {slug}")
        CommonUtils.save_to_file(self.__file_name, self.__slug_list)

from slugConverter import SlugConverter

if __name__ == "__main__":
    SlugConverter()

class SlugConverter:
    def __init__(self):
        self.__file_name = input("Введите название файла для сохранения: ")
        print(f"Данные будут сохранены в файл: {self.__file_name}")
        self.__slug_list = []
        self.run()

    def run(self):
        while True:
            name = input("Введите имя и фамилию известного человека (или оставьте строку пустой для выхода): ")
            if not name:
                break
            slug = CommonUtils.translit_to_eng(name)
            self.__slug_list.append(slug)
            print(f"Slug: {slug}")
        CommonUtils.save_to_file(self.__file_name, self.__slug_list)

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def slug_list(self):
        return self.__slug_list

    @slug_list.setter
    def slug_list(self, value):
        self.__slug_list = value