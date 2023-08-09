import os


type_labels = ['Б', 'КБ', 'МБ', 'ГБ']
threshold = 1024
 
 
def get_size(file_name: str):
    
    file_size = os.stat(file_name).st_size
    label_index = 0
    
    while file_size >= threshold and label_index < len(type_labels) - 1:
        file_size /= threshold
        label_index += 1
    
    print(f'{int(-(- file_size // 1))}{type_labels[label_index]}')


file_name = input()

get_size(file_name)
