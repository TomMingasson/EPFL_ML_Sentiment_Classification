def read_vocab(filename):
    
    dict_ = {}
    with open(filename, 'r', encoding='utf-8-sig') as datafile:
        for line in datafile:
            occurence = line.strip().split(' ')[0]
            word = line.strip().split(' ')[1]
            dict_[word] = int(occurence)
    return dict_