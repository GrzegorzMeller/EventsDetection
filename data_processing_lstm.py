

def create_words_txt(file_path, new_name):
    '''input file should be in bio format'''
    sentence = ""
    doc = open(file_path, "r", encoding="utf8")
    f = open("D:\\projects\\inf_retrieval\\datasets\\bio_class\\" + new_name + ".words.txt", "w+", encoding="utf-8")
    iterator = 1
    for line in doc:
        if line.strip():
            words = line.split()
            t = (words[0])
            sentence = sentence+t+" "
        else:
            f.write(sentence+'\n')
            sentence = ""
        iterator += 1


def create_tags_txt(file_path, new_name):
    '''input file should be in bio format'''
    sentence = ""
    doc = open(file_path, "r", encoding="utf8")
    f = open("D:\\projects\\inf_retrieval\\datasets\\bio_class\\" + new_name + ".tags.txt", "w+", encoding="utf-8")
    for line in doc:
        if line.strip():
            words = line.split()
            t = (words[5])
            sentence = sentence+t+" "
        else:
            f.write(sentence+'\n')
            sentence = ""


if __name__ == "__main__":
    #create_words_txt("D:\\projects\\inf_retrieval\\datasets\\bio_class\\train.txt", "train")
    #create_words_txt("D:\\projects\\inf_retrieval\\datasets\\bio_class\\test.txt", "test")

    create_tags_txt("D:\\projects\\inf_retrieval\\datasets\\bio_class\\train.txt", "train")
    create_tags_txt("D:\\projects\\inf_retrieval\\datasets\\bio_class\\test.txt", "test")

