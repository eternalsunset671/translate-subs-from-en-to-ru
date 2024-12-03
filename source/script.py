from os import listdir, getcwd
from os.path import isfile, join
from translators import translate_text
from re import sub
from tqdm import tqdm
from time import sleep


def translate(text):
    a = 0
    threshold = 9000

    tmp = ''
    try:
        for i in tqdm(range(0, len(text), threshold)):
            counter = i + 9000 
            while text[counter] != '\n' and text[counter+1] != '\n':
                counter += 1
            tmp += translate_text(text[a:counter+1], translator='yandex', from_language='en', to_language='ru') + '\n\n'
            a = counter + 1
    except IndexError:
        tmp += translate_text(text[a:], translator='yandex', from_language='en', to_language='ru')

    text = sub(r'(\d\d:)\s{0,1}(\d\d:)\s{0,1}(\d\d,)\s{0,1}(\d\d\d)\s{0,1}( --> )\s{0,1}(\d\d:)\s{0,1}(\d\d:)\s{0,1}(\d\d,)\s{0,1}(\d\d\d)', r'\1\2\3\4\5\6\7\8\9', tmp)
    return text


def main():
    current_directory = getcwd()
    for filename in listdir(current_directory):
        file_path = join(current_directory, filename)
        if isfile(file_path):
            if filename.endswith('.srt'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        text = file.read()

                    text = translate(text)
                    with open(file_path[:-4] + '_русский' + '.srt', 'w', encoding='utf8') as file:
                        file.write(text)
                except Exception as err:
                    print(f"Ошибка при открытии файла {filename}: {err}")
                    sleep(2)
            elif not filename.endswith('.exe') and not filename.endswith('.txt') and not filename.endswith('.md'):
                print(filename, 'Некорректное расширение файла (должно быть ____.srt)')
                sleep(2)

if __name__ == '__main__':
    main()