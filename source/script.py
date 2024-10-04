import os
import translators as ts
import re

current_directory = os.getcwd()
for filename in os.listdir(current_directory):
    file_path = os.path.join(current_directory, filename)
    if os.path.isfile(file_path) and filename.endswith('.srt'):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                
                a = 0
                threshold = 9000

                tmp = ''
                try:
                    for i in range(0, len(text), threshold):
                        counter = i + 9000 
                        while text[counter] != '\n' and text[counter+1] != '\n':
                            counter += 1
                        tmp += ts.translate_text(text[a:counter+1], translator='yandex', from_language='fr', to_language='en') + '\n\n'
                        a = counter + 1
                except IndexError:
                    tmp += ts.translate_text(text[a:], translator='yandex', from_language='en', to_language='ru')

                text = re.sub(r'(\d\d:)\s{0,1}(\d\d:)\s{0,1}(\d\d,)\s{0,1}(\d\d\d)\s{0,1}( --> )\s{0,1}(\d\d:)\s{0,1}(\d\d:)\s{0,1}(\d\d,)\s{0,1}(\d\d\d)', r'\1\2\3\4\5\6\7\8\9', tmp)

            with open(file_path[:-4] + '_русский' + '.srt', 'w', encoding='utf8') as file:
                file.write(text)
        except Exception as e:
            print(f"Ошибка при открытии файла {filename}: {e}")


# import os
# import translators as ts
# import re
# import tqdm
# from joblib import Parallel, delayed

# # current_directory = os.path.dirname(os.path.abspath(__file__))
# current_directory = os.getcwd()
# for filename in os.listdir(current_directory):
#     file_path = os.path.join(current_directory, filename)
#     if os.path.isfile(file_path) and filename.endswith('.srt'):
#         # try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             text = file.read()
#             # print(text)
#             a = 0
#             threshold = 9000
#             text_batch = []
#             # for i in range(0, len(text), len_part):
#             #     tmp += ts.translate_text(text[i:i+len_part], translator='yandex', from_language='en', to_language='ru')
#             tmp = ''

#             for x in re.finditer(r'\n\n', text):
#                 b = x.end()
#                 if b - 2 > threshold:
#                     b -= 2
#                     # if text[b+1] == '\n':
#                     #     b += 1
#                     # tmp += text[a:b] + '\naboba\n'
#                     tmp += ts.translate_text(text[a:b], translator='yandex', from_language='en', to_language='ru') + '\n\n'
#                     # text_batch += [text[a:b+1]]
#                     a = b+1
#                     threshold += 9000
#             if a < len(text):
#                 tmp += ts.translate_text(text[a:], translator='yandex', from_language='en', to_language='ru')
#                 # text_batch += [text[a:]]
#             # print(text)
#             # def translate(text):
#             #     return ts.translate_text(text[a:b+1], translator='yandex', from_language='en', to_language='ru')
            
#             # processed_texts = Parallel(n_jobs=-1)(delayed(translate)(t) for t in tqdm(text_batch))

#             # text = ''.join(processed_texts)
#             text = tmp
#             # text = re.sub(r'[^,\s](\d{3,3})', r'\n\n\1', tmp)
#             text = re.sub(r'(\d\d:)\s{0,1}(\d\d:)\s{0,1}(\d\d,)\s{0,1}(\d\d\d)\s{0,1}( --> )\s{0,1}(\d\d:)\s{0,1}(\d\d:)\s{0,1}(\d\d,)\s{0,1}(\d\d\d)', r'\1\2\3\4\5\6\7\8\9', tmp)
                
#             # print(text)
#         with open(file_path[:-4] + '_русский' + '.srt', 'w', encoding='utf8') as file:
#             file.write(text)
#                 # with open(file_path, 'w', encoding='utf8') as file:
#                 #     text = ''
#         # except Exception as e:
#         #     print(f"Ошибка при открытии файла {filename}: {e}")



# import os
# import translators as ts
# current_directory = os.path.dirname(os.path.abspath(__file__))

# file_path = r'subs.txt'

# if os.path.isfile('subs.txt'):
#     try:
#         with open(file_path, 'r', encoding='utf8') as file:
#             text = file.read().replace('\n\n', '\n')
#             print(len(text))
#             len_part = 9000
#             tmp = ''
#             for i in range(0, len(text), len_part):
#                 tmp += ts.translate_text(text[i:i+len_part], translator='yandex', from_language='en', to_language='ru')
#             text = tmp
#             print(text)
#         with open(file_path[:-4] + '.srt', 'w', encoding='utf8') as file:
#             file.write(text)
#         with open(file_path, 'w', encoding='utf8') as file:
#             text = ''
#     except Exception as e:
#         print(f"Ошибка при открытии файла {file_path}: {e}")



