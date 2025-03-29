# import pickle

# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import numpy as np


# data_dict = pickle.load(open('./data.pickle', 'rb'))

# data = np.asarray(data_dict['data'])
# labels = np.asarray(data_dict['labels'])

# x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# model = RandomForestClassifier()

# model.fit(x_train, y_train)

# y_predict = model.predict(x_test)

# score = accuracy_score(y_predict, y_test)

# print('{}% of samples were classified correctly !'.format(score * 100))

# f = open('model.p', 'wb')
# pickle.dump({'model': model}, f)
# f.close()




import pickle
import numpy as np

with open('data.pickle', 'rb') as f:
    data_dict = pickle.load(f)

data = data_dict['data']
labels = data_dict['labels']

# Debugging output
print(f"Type of data: {type(data)}")
print(f"Length of data: {len(data)}")

# Check individual sample sizes
for i, sample in enumerate(data):
    print(f"Sample {i} shape: {np.shape(sample)}")

# Convert to NumPy array (only if all shapes match)
try:
    data = np.asarray(data, dtype=np.float32)
except ValueError as e:
    print("Error converting data to NumPy array:", e)

labels = np.asarray(labels)

print(f"Final data shape: {data.shape if isinstance(data, np.ndarray) else 'Inconsistent shapes detected!'}")
