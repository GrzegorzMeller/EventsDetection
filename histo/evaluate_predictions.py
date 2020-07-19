from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import  recall_score

def take_predictions(file_path):
    '''input file should be in bio format'''
    original_list = []
    pred_list = []
    doc = open(file_path, "r", encoding="utf8")
    for line in doc:
        if line.strip():
            words = line.split()
            original_list.append(words[1])
            pred_list.append(words[2])
    return original_list, pred_list




if __name__ == "__main__":
    original, predictions = take_predictions("D:\\projects\\inf_retrieval\\datasets\\predictions\\mention\\dev.preds.txt")
    print(predictions)
    print(original)
    f1 = f1_score(original, predictions, average='weighted')
    prec = precision_score(original, predictions, average='weighted')
    rec = recall_score(original, predictions, average='weighted')
    print(f1, prec, rec)



