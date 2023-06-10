
# Model Training

This directory contains the code and resources for training the knee osteoarthritis predictor model.

## Prerequisites

- Python 3
- Google Colab
- Keras
- NumPy
- Pandas
- scikit-learn
- TensorFlow

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/jithendra-varma/Knee_Osteoarthritis_Predictor.git
   ```

2. Access the model training directory:

   ```bash
   cd Knee_Osteoarthritis_Predictor/Model_Training
   ```

3. Mount Google Drive to access the training data.

4. Set the paths for the training and testing directories in the code.

5. Define the model architecture by using the VGG16 pre-trained model.

6. Train the model using the training data.

7. Save the trained model as `knee.h5`.

8. Evaluate the model using the testing data.

9. Plot the confusion matrix and compute metrics, such as accuracy, precision, recall, and F-measure.

## Results

After training the model, the following results were obtained:

- Accuracy: 0.954
- Precision: 0.960
- Recall: 0.954
- F-Measure: 0.954

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](../LICENSE) file.
