from models.baseline_model import predict

sample = [2,5,7,8]

results = []

for x in sample:
    results.append(predict(x))

print(results)
