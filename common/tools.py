import os

from config import config


# 遍历指定后缀的代码文件
def train_code_file(fold_path, file_type, all_file=list()):
    if os.path.isdir(fold_path):
        l = os.listdir(fold_path)
        for i in l:
            path = os.path.join(fold_path, i)
            if os.path.isdir(path):
                train_code_file(path, file_type)
            else:
                if path.endswith(config.file_type_dict[file_type]):
                    all_file.append(path)
        return all_file
    else:
        return [fold_path]


def remove_space(w):
    if w != '':
        return True
        # for i in w:
        #     if not ('a' <= i <= 'z') and not ('A' <= i <= 'Z'):
        #         return False
        # else:
        #     return True
    else:
        return False


# 统计python单词数目
def sum_of_word(words):
    for i in config.const_python_split:
        words = words.replace(i, ' ')
    return list(filter(remove_space, words.split(' ')))


# 遍历所有的文件
def train_all_file(fold_path, all_file=list()):
    if os.path.isdir(fold_path):
        try:
            l = os.listdir(fold_path)
            for i in l:
                path = os.path.join(fold_path, i)
                if os.path.isdir(path):
                    train_all_file(path)
                else:
                    all_file.append(path)
            return all_file
        except Exception as e:
            print(e)
    else:
        return [fold_path]


if __name__ == '__main__':
    sum_of_word('')
