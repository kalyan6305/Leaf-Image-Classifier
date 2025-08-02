## 🌿 Leaf Image Classifier using Deep Learning

This project is a deep learning–based web application that classifies **30 different tree species** using **leaf images**. It uses a Convolutional Neural Network (CNN) model built with TensorFlow and provides detailed tree specifications upon prediction.

---

### ✨ Features

* 🔍 Predicts tree species from uploaded leaf images
* 🌗 Dark & light theme switch for improved UI
* 🧠 CNN model trained on custom dataset of 30 species
* 📊 Shows confidence score for each prediction
* 🌳 Displays tree details: name, uses, growth time, lifespan, and benefits
* 📥 Downloadable prediction result for offline reference

---

### 🧰 Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/)
* **Modeling**: TensorFlow / Keras (CNN)
* **Image Processing**: OpenCV
* **Data Handling**: NumPy, scikit-learn

---

### 🚀 Getting Started

#### Clone and install dependencies:

```bash
git clone https://github.com/kalyan6305/Leaf-Image-Classifier.git
cd Leaf-Image-Classifier
pip install -r requirements.txt
```

#### Run the app:

```bash
streamlit run app.py
```

---

### 📁 Project Structure

```
├── app.py                  # Streamlit frontend
├── train.py                # Model training script
├── model/
│   ├── leaf_model.h5       # Saved Keras model
│   └── classes.json        # Class name mappings
├── leaf_dataset/Leaves/    # Dataset organized by class
├── requirements.txt
└── README.md
```

---

### 🌳 Tree Species Included (30)

Examples:

* Neem, Mango, Amla, Asopalav, Banyan, Babul, Bamboo, Sitafal, Gulmohor, Coconut, Sugarcane, etc.

---

### 📜 License

This project is licensed under the [MIT License](LICENSE).


