class StandardScaler:
    def __init__(self):
        self.mean = None
        self.std = None

    def fit(self, data):
        self.mean = sum(data) / len(data)
        self.std = (sum((x - self.mean) ** 2 for x in data) / len(data)) ** 0.5

    def transform(self, data):
        if self.mean is None or self.std is None:
            raise ValueError("Scaler has not been fitted yet.")
        
        return [(x - self.mean) / self.std if self.std != 0 else 0 for x in data]

    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)

data = [10, 20, 30, 40, 50]
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
print("Original Data:", data)
print("Standardized Data:", scaled_data)
