file1, file2 = input(), input()

with open(file1, 'r') as f1, open(file2, 'w') as f2:
    for line in f1:
        line = line.strip()
        if line:
            words = line.strip().replace('\t', '').split()
            f2.write(' '.join(words) + '\n')
