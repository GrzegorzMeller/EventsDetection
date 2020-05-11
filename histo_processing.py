import xml.dom.minidom

#to do: sliding window on text, and annotation on each window if it contatins event or not

def get_text():
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


if __name__ == "__main__":
    get_text()
