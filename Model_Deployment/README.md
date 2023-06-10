
# Knee Osteoarthritis Predictor - Model Deployment

This directory contains the code and resources for deploying the knee osteoarthritis predictor as an interactive web tool.

## Interactive Tool

The interactive tool allows users to upload knee images and obtain predictions for the severity of osteoarthritis. It provides a user-friendly interface where individuals can interact with the trained model without requiring any programming knowledge.

### Prerequisites

- Python 3: Ensure you have Python 3 installed on your machine.

### Installation

To set up and run the interactive tool locally, follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/jithendra-varma/Knee_Osteoarthritis_Predictor.git
   ```

2. Navigate to the `model_deployment` directory:
   ```
   cd Knee_Osteoarthritis_Predictor/model_deployment
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage

To use the interactive tool for knee osteoarthritis prediction, follow these steps:

1. Make sure the trained model file (`knee.h5`) is present in the `model` directory.

2. Start the web application by running the following command:
   ```
   python app.py
   ```

3. Open a web browser and go to `http://localhost:5000` to access the interactive tool.

4. Use the provided interface to upload knee images (in JPEG or PNG format) and click the "Predict" button.

5. The tool will process the image and display the predicted severity of osteoarthritis.

### HTML Pages

The web interface of the interactive tool is built using HTML pages. The `templates` directory contains the following HTML files:

- `index.html`: The main page of the interactive tool that allows users to upload knee images and view predictions.

- `result.html`: The page that displays the predicted severity of osteoarthritis after processing the uploaded image.

- `error.html`: The error page that is displayed when there are issues with image uploading or prediction.

You can modify these HTML files to customize the appearance and layout of the web pages according to your preferences.

### Demo

A live demo of the interactive tool is available [here](https://example.com) for you to explore and test without any setup.

## Additional Resources

For more details on the project, including model
