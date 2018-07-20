from common.tools import train_code_file, sum_of_word


class Counts:
    def __init__(self, types):
        self.types = types

    def one_file(self, file_name, word_list):
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    word_list += sum_of_word(line.strip())
        except Exception as e:
            print(e)

    def all_file(self, file_path):
        word_list = list()
        all_file = train_code_file(file_path, self.types)
        for file in all_file:
            self.one_file(file, word_list)

        word_dict = dict()
        for w in word_list:
            word_dict[w] = word_dict.setdefault(w, 0) + 1
        # print(word_dict)
        # for i in word_dict.items():
        #     print(i)
        result = sorted(word_dict.items(), key=lambda x: x[1])
        for i in result:
            print(i)


if __name__ == '__main__':
    Counts('python').all_file(r'C:\E_HDFS\vmhdfs\zhaopin')
