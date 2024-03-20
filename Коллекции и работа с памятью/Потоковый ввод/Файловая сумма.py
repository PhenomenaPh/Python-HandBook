with open('numbers.num', 'rb') as f:
    values = []
    while True:
        bytes_chunk = f.read(2)
        
        if not bytes_chunk:
            break
            
        values.append(int.from_bytes(bytes_chunk, 'big'))
    result = sum(values) % 65536
    print(result)
            