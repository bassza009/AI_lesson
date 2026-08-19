ground_truth = input().split(" ")

prediction = input().split(" ")

def true_positive(ground_truth, prediction):
    tp = 0
    for gt,pred in zip(ground_truth, prediction):
        if gt == "1" and pred =="1":
            tp += 1
    return tp

def true_negative(ground_truth, prediction):
    tn = 0
    for gt,pred in zip(ground_truth, prediction):
        if gt == "0" and pred == "0":
            tn += 1
    return tn

def false_positive(ground_truth, prediction):
    fp = 0
    for gt,pred in zip(ground_truth, prediction):
        if gt == "0" and pred == "1":
            fp += 1
    return fp

def false_negative(ground_truth, prediction):
    fn = 0
    for gt,pred in zip(ground_truth, prediction):
        if gt == "1" and pred == "0":
            fn += 1
    return fn

def accuracy(tp,tn,fp,fn):
    return (tp+tn)/(tp+tn+fp+fn)

def precision(tp,fp):
    return tp/(tp+fp)

def recall(tp,fn):
    return tp/(tp+fn)

def f1_score(prec,rec):
    return 2*(prec*rec)/(prec+rec)
def main():
    tp = true_positive(ground_truth, prediction)
    tn = true_negative(ground_truth, prediction)
    fp = false_positive(ground_truth, prediction)
    fn = false_negative(ground_truth, prediction)

    acc = accuracy(tp,tn,fp,fn)
    prec = precision(tp,fp)
    rec = recall(tp,fn)
    f1 = f1_score(prec,rec)

    print(f"Accuracy: {acc:.2f}")
    print(f"Precision: {prec:.2f}")
    print(f"Recall: {rec:.2f}")
    print(f"F1 Score: {f1:.2f}")

if __name__ == "__main__":
    main()