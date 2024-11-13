# Найдёт везде
class WordsFinder:
    punkt = [',', '.', '=', '!', '?', ';', ':', ' - ']

    def __init__(self, *file_name):
        self.file_names = []
        for i in range(len(file_name)):
            self.file_names.append(file_name[i])

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            key_ = file_name
            with open(file_name, encoding='utf-8') as file:
                value_ = []
                for line in file:
                    line = line.lower()
                    for c in self.punkt:
                        line = line.replace(c, '')
                    words = line.split()
                    for word_ in words:
                        value_.append(word_)
            all_words[key_] = value_
        return all_words

    def find(self, word):
        find_result = {}
        for name, words in self.get_all_words().items():
            n = 0
            for word_ in words:
                n += 1
                if word_ == word.lower():
                    find_result[name] = n
                    break
        return find_result

    def count(self, word):
        count_result = {}
        for name, words in self.get_all_words().items():
            n = 0
            for word_ in words:
                if word_ == word.lower():
                    n += 1
            count_result[name] = n
        return count_result


if __name__ == '__main__':
    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))
    print()

    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
