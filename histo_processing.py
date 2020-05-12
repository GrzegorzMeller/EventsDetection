import sklearn_crfsuite
from sklearn_crfsuite import scorers
from sklearn_crfsuite import metrics

def create_tuple_list(file_path):
    '''input file should be in bio format'''
    tuple_list = []
    sentence = []
    doc = open(file_path, "r")
    for line in doc:
        if line.strip():
            words = line.split()
            t = (words[0], words[2], words[5])
            sentence.append(t)
        else:
            tuple_list.append(sentence)
            sentence = []
    return tuple_list


def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]

    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'postag': postag,
        'postag[:2]': postag[:2],
    }
    if i > 0:
        word1 = sent[i - 1][0]
        postag1 = sent[i - 1][1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            '-1:postag': postag1,
            '-1:postag[:2]': postag1[:2],
        })
    else:
        features['BOS'] = True

    if i < len(sent) - 1:
        word1 = sent[i + 1][0]
        postag1 = sent[i + 1][1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            '+1:postag': postag1,
            '+1:postag[:2]': postag1[:2],
        })
    else:
        features['EOS'] = True

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]


def sent2labels(sent):
    return [label for token, postag, label in sent]


def sent2tokens(sent):
    return [token for token, postag, label in sent]


if __name__ == "__main__":
    #get_text()]

    tuple_list_train = create_tuple_list("D:\\projects\\inf_retrieval\\datasets\\bio_mention\\train.txt")
    tuple_list_dev = create_tuple_list("D:\\projects\\inf_retrieval\\datasets\\bio_mention\\dev.txt")
    print(tuple_list_dev[1])
    print(sent2features(tuple_list_dev[1])[1])

    X_train = [sent2features(s) for s in tuple_list_train]
    y_train = [sent2labels(s) for s in tuple_list_train]

    X_test = [sent2features(s) for s in tuple_list_dev]
    y_test = [sent2labels(s) for s in tuple_list_dev]

    crf = sklearn_crfsuite.CRF(
        algorithm='lbfgs',
        c1=0.1,
        c2=0.1,
        max_iterations=100,
        all_possible_transitions=True
    )
    crf.fit(X_train, y_train)

    labels = ['B-EVENT_MENTION', 'I-EVENT_MENTION']
    y_pred = crf.predict(X_test)
    m = metrics.flat_f1_score(y_test, y_pred,
                          average='weighted', labels=labels)
    print(m)
