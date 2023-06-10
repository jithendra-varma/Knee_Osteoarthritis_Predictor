
# Knee Osteoarthritis Predictor

This repository contains the code for training a knee osteoarthritis predictor using a Convolutional Neural Network (CNN) model. The model is trained on a dataset of knee images to classify the severity of osteoarthritis into five categories: Normal, Doubtful, Mild, Moderate, and Severe.

## Model Training

The model training is performed using the `Model_Training.ipynb` notebook. The notebook utilizes the data present in the `Data` folder. To access the notebook and the data, you can follow this [link](https://github.com/jithendra-varma/Knee_Osteoarthritis_Predictor/tree/main/Model_Training).

### Prerequisites

- Google Colab: The notebook is designed to run on Google Colab, which provides a cloud-based environment with necessary dependencies pre-installed.

### Steps to Run

1. Mount Google Drive: The first step in the notebook is to mount Google Drive. This allows access to the necessary files and datasets stored in Google Drive.

2. Set the Working Directory: The notebook sets the working directory to the location of the project files on Google Drive.

3. Import Libraries: The required libraries, including `numpy`, `pandas`, and `keras`, are imported for data processing and model building.

4. Load the Data: The training and testing data directories are specified, and the data is loaded using the `ImageDataGenerator` from Keras. The data is preprocessed by rescaling the pixel values between 0 and 1.

5. Define the Model Architecture: The model architecture is based on the VGG16 model pretrained on ImageNet. The VGG16 model is imported from `keras.applications.vgg16` and the top layer is removed. The base model is then followed by a flatten layer and a dense layer with softmax activation for classification.

6. Compile and Train the Model: The model is compiled with the Adam optimizer, categorical cross-entropy loss function, and accuracy metric. The model is trained using the `fit` function, specifying the training and validation data generators and the number of epochs.

7. Save the Model: After training, the model is saved as `knee.h5` for future use.

8. Evaluate the Model: The model is evaluated using the validation data generator. The accuracy, precision, recall, and F-measure scores are computed and printed.

9. Plot the Confusion Matrix: The confusion matrix is computed using the true labels and predictions. The matrix is then plotted using a custom function, showing the distribution of predicted and actual labels.

10. Test on New Images: A function `test_on_img` is defined to test the model on new images. The function takes an image as input, resizes it to 224x224 pixels, and predicts the severity of osteoarthritis. The image and the predicted class are returned.

11. Plot Training Loss and Accuracy: Finally, the training loss and accuracy curves are plotted using the history object obtained during training.

## Model Deployment

To deploy the knee osteoarthritis predictor as an interactive web tool, refer to the `Model_Deployment` directory in this repository. The web application is developed using the Flask framework in Python and allows users to upload knee images and receive predictions regarding the severity of osteoarthritis. For more details on the model deployment, refer to the [Model_Deployment](https://github.com/jithendra-varma/Knee_Osteoarthritis_Predictor/tree/main/Model_Deployment) directory.

## Additional Resources

For more details on the project, including model training and evaluation, refer to the [main repository](https://

github.com/jithendra-varma/Knee_Osteoarthritis_Predictor).

Feel free to explore and experiment with the code to enhance the knee osteoarthritis predictor!

For a more detailed understanding of the model training process, please refer to the `Model_Training.ipynb` notebook in this repository.
