from sys import stdin
sentence = input().lower()

file_names = [i.strip() for i in stdin]


def find_file(files: list()):
    good_files = list()
    for file in files:
        with open(file, 'r') as f:
            if sentence in ' '.join(f.read().lower().split()):
                good_files.append(file)
    if good_files:
        print('\n'.join(good_files))
    else:
        print('404. Not Found')


find_file(file_names)