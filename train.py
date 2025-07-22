import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical


IMG_SIZE = 128
DATASET_PATH = "dataset/"

# Check if dataset exists, else try to use leaf_dataset/Leaves as fallback
if not os.path.exists(DATASET_PATH) or len(os.listdir(DATASET_PATH)) == 0:
    fallback_path = "leaf_dataset/Leaves/"
    if os.path.exists(fallback_path):
        DATASET_PATH = fallback_path
    else:
        raise FileNotFoundError(f"No dataset found in '{DATASET_PATH}' or '{fallback_path}'. Please add your data.")


# Only include folders that contain at least one image file
def has_images(folder_path):
    for file in os.listdir(folder_path):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            return True
    return False

classes = [d for d in os.listdir(DATASET_PATH)
           if os.path.isdir(os.path.join(DATASET_PATH, d))
           and has_images(os.path.join(DATASET_PATH, d))]
if not classes:
    raise FileNotFoundError(f"No class folders with images found in '{DATASET_PATH}'. Please organize your data as dataset/class_name/image.jpg")
label_map = {name: idx for idx, name in enumerate(classes)}

X, y = [], []
for folder in classes:
    folder_path = os.path.join(DATASET_PATH, folder)
    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)
        if not (file.lower().endswith('.jpg') or file.lower().endswith('.png') or file.lower().endswith('.jpeg')):
            continue
        img = cv2.imread(path)
        if img is None:
            print(f"Warning: Unable to read image {path}, skipping.")
            continue
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        X.append(img)
        y.append(label_map[folder])

X = np.array(X) / 255.0
y = to_categorical(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(len(classes), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

if not os.path.exists('model'):
    os.mkdir('model')
model.save("model/leaf_model.h5")

print("Model training complete and saved!")
