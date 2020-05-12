import xml.dom.minidom

#to do: sliding window on text, and annotation on each window if it contatins event or not


def get_text():
    '''input file should be in xml format'''
    doc = xml.dom.minidom.parse("D:\\projects\\inf_retrieval\\datasets\\news\\Anarchists_Demand_Strike_To_End_War.txt.xml")
    tokens = doc.getElementsByTagName("token")
    iterator = 0
    text = ""
    for t in tokens:
        token = doc.getElementsByTagName("token")[iterator]
        element = token.childNodes[0]
        text += element.nodeValue+" "
        iterator += 1
    print(text)


def create_tuple_list():
    '''input file should be in bio format'''
    tuple_list = []
    sentence = []
    doc = open(
        "D:\\projects\\inf_retrieval\\datasets\\bio_mention\\train.txt","r")
    for line in doc:
        if line.strip():
            words = line.split()
            t = (words[0], words[1], words[2], words[3], words[4], words[5])
            sentence.append(t)
        else:
            tuple_list.append(sentence)
            sentence = []
    return tuple_list


if __name__ == "__main__":
    #get_text()]

    tuple_list = create_tuple_list()
    print(tuple_list[0])
