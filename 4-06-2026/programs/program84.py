subjects=["I","You"]
verb =["Play", "Love"]
object=["Hockey","Football"]
sentences=[]
for s in subjects:
    for v in verb:
        for o in object:
            sentence=f"{s}{v}{o}"
            sentences.append(sentence)
for sentence in sentences:
   print(sentence)
