def data_reverse(data):
    ch=8
    rd=[data[i:i+ch] for i in range (0,len(data), ch)][::-1]
    fd=[item for sublist in rd for item in sublist]
    return fd