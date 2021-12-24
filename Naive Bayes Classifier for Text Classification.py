
file_name = "traindata.txt"

def read_file():
    with open(file_name) as f:
        lines = [line.rstrip("\n") for line in f]
    return lines[1:]

print(read_file())

def dict_sentence_class():
    sentence_list = []
    class_list =[]
    for i in range(len(read_file())):
        sentence_list.append(read_file()[i].split(", ")[1])
        class_list.append(read_file()[i].split(", ")[0])
    return dict(zip(sentence_list,class_list))

print(dict_sentence_class())

def get_all_words_uniquely_and_all_words():
    lis = []
    list_all_words = []
    for k in dict_sentence_class().keys():
        lis.append(k)
    unique_list = []
    for i in lis:
        unique_list += i.lower().split(" ")
    return sorted(list(set(unique_list))),unique_list


def count_exist_word_from_string(str, word):
    # x = 'This is my book is'
    # print(x.split(" ").count("is"))
    return str.split(" ").count(word)

def count_exist_word_from_list(list,word):
    return list.count(word)

def get_all_classes():
    return list(set(dict_sentence_class().values()))
print(get_all_classes())

def prob_each_class():
    class_prob_list = []
    lx = [0] * len(get_all_classes())
    for key, value in dict_sentence_class().items():
        for j in range(len(get_all_classes())):
            if value == get_all_classes()[j]:
                lx[j] += 1
    for i in lx:
        class_prob_list.append(i/sum(lx))
    return class_prob_list

def dict_prob_class():
    return dict(zip(get_all_classes(),prob_each_class()))

print(dict_prob_class())

# def freq_of_original_word():



def smoothing(w_freq_in_class,freq_class,num_uniq):

    return (w_freq_in_class+1)/(freq_class+num_uniq)

def prob_each_word():
    uniq, all_w = get_all_words_uniquely_and_all_words()
    dict_x = {}
    for w in all_w:
        if w in dict_x:
            dict_x[w] += 1
        else:
            dict_x[w] = 1
    total = sum(dict_x.values())

    for k,v in dict_x.items():
        dict_x[k] = v/total

    return dict_x

print(prob_each_word())


