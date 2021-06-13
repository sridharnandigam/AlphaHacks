from transformers import pipeline
import json

classifier = pipeline('sentiment-analysis')
print("loaded classifier")

article_data = None
with open("metadata.json", "r") as f:
    article_data = json.loads(f.read());
print("loaded article_data")
descriptions = list(map(lambda x: x["data"]["description"], article_data))
print("getting classifications")
classifications = []
for i in range(len(descriptions)):
    print(i,end=",")
    classification = classifier(descriptions[i])
    classifications.append(classification)
    print(classification)

print("received classifications")

def numerical(classification):
    classification = classification[0]
    choice = classification["label"]
    confidence = classification["score"]
    if choice == "POSITIVE":
        return confidence
    else:
        return 1-confidence

print("mapping classifications")
classifications = list(map(numerical, classifications))

print("labeling articles with sentiment")
for i in range(len(article_data)):
    article_data[i]["sentiment"] = classifications[i]

print("saving to new json")
with open("sentiment.json", "w") as f:
    json.dump(article_data, f)
