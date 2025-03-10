def perceptron_train(data, labels, learning_rate=0.1, epochs=100):
    weights = [0.0] * (len(data[0]) + 1)
    for _ in range(epochs):
        for i in range(len(data)):
            inputs = [1] + data[i]
            prediction = predict(inputs, weights)
            error = labels[i] - prediction
            for j in range(len(weights)):
                weights[j] += learning_rate * error * inputs[j]
    return weights

def predict(inputs, weights):
    activation = sum(x * w for x, w in zip(inputs, weights))
    return 1 if activation >= 0 else 0

def classify(height, weight, weights):
    inputs = [1, height, weight]
    prediction = predict(inputs, weights)
    return "Male" if prediction == 1 else "Female"

data = [[5.9, 75], [5.8, 86], [5.2, 50], [5.4, 55], [6.1, 85], [5.5, 62]]
labels = [1, 1, 0, 0, 1, 0]

trained_weights = perceptron_train(data, labels)

print(classify(6, 82, trained_weights))
print(classify(5.3, 52, trained_weights))