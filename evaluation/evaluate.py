def accuracy(pred,true):

    correct=0

    for p,t in zip(pred,true):
        if p==t:
            correct+=1

    return correct/len(true)
