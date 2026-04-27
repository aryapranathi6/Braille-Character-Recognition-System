# Braille Character Recognition System using CNN

## Project Overview

This project is a Braille Character Recognition System developed using Convolutional Neural Networks (CNN) and Streamlit.

The system helps recognize Braille characters (A, B, C, D, E) from images and converts them into readable text for normal users, improving accessibility and inclusive communication.

---

## Problem Statement

Many people cannot understand Braille symbols used by visually impaired individuals in public places like elevators, hospitals, railway stations, and educational environments.

This project helps bridge that gap by recognizing Braille characters and converting them into understandable text.

---

## Technologies Used

* Python
* TensorFlow / Keras
* OpenCV
* NumPy
* Matplotlib
* Streamlit
* Scikit-learn

---

## Dataset Used

Braille Alphabet Image Dataset (A–Z)

For this prototype, 5 classes were used:

* A
* B
* C
* D
* E

Each class contains 100 images.

---

## Model Architecture

* Conv2D
* MaxPooling2D
* Conv2D
* MaxPooling2D
* Flatten
* Dense Layer
* Softmax Output Layer

---

## Results

* Accuracy: 100%
* Precision: 1.00
* Recall: 1.00
* F1-score: 1.00

The model successfully predicts Braille characters using the Streamlit interface.

---

## Streamlit Interface

Users can upload a Braille image and the system predicts the corresponding character with confidence score.

Example:

Predicted Character: A
Confidence: 99.98%

---

## Future Scope

* Expand from 5 classes to full Braille alphabet (A–Z)
* Add emergency words like Help, Exit, Lift, Up, Down
* Add voice output using Text-to-Speech
* Mobile/Web deployment
* Real-time camera-based Braille detection

---

## Conclusion

This project demonstrates how AI can be used to improve accessibility and inclusive communication through Braille recognition.

It serves as a strong prototype for future expansion into a complete Braille-to-English translation assistant.
