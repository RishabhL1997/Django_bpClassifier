
import pickle

def calculatebp(s,d):
    a,b=int(s),int(d)

    xy = [[a, b]]

    randomforest = pickle.load(open('BPmodel.sav', 'rb'))
    predictions = randomforest.predict(xy)

    bpi = predictions[0]
    bplist = ["-", "Hypertension-stage4", "Hypertension-stage3",
              "Hypertension-stage2", "Hypertension-stage1",
              "Pre-Hypertension", "High Normal",
              "Normal", "Low Normal", "Moderate Hypotension",
              "Sever Hypotension", "Extrem Hypotension"]
    return str(bplist[bpi])

print(calculatebp('120','80'))