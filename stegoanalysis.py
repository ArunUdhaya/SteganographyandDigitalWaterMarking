import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the cover and stego images
cover_image = np.load("cover_image.npy")
stego_image = np.load("stego_image.npy")

# Extract the features from the cover and stego images
cover_features = extract_features(cover_image)
stego_features = extract_features(stego_image)

# Label the samples as cover (0) or stego (1)
X = np.vstack((cover_features, stego_features))
y = np.hstack((np.zeros(len(cover_features)), np.ones(len(stego_features))))

# Train a logistic regression classifier on the labeled samples
classifier = LogisticRegression()
classifier.fit(X, y)

# Evaluate the classifier's performance on a test set
test_cover_image = np.load("test_cover_image.npy")
test_stego_image = np.load("test_stego_image.npy")
test_cover_features = extract_features(test_cover_image)
test_stego_features = extract_features(test_stego_image)
test_X = np.vstack((test_cover_features, test_stego_features))
test_y = np.hstack((np.zeros(len(test_cover_features)), np.ones(len(test_stego_features))))
predictions = classifier.predict(test_X)
accuracy = accuracy_score(test_y, predictions)
print("Accuracy: ", accuracy)