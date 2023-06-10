
# Knee Osteoarthritis Predictor - Model Deployment

This directory contains the code and resources for deploying the knee osteoarthritis predictor as an interactive web tool.

## Interactive Tool

The web application is developed using the Flask framework in Python and serves as an interactive tool for knee osteoarthritis prediction. It allows users to upload knee images and receive predictions regarding the severity of osteoarthritis.

## Usage

To use the interactive tool for knee osteoarthritis prediction, follow these steps:

1. Make sure you have Python 3 installed on your machine.

2. Clone the repository to your local machine:
   ```
   git clone https://github.com/jithendra-varma/Knee_Osteoarthritis_Predictor.git
   ```

3. Navigate to the `Model_Deployment` directory:
   ```
   cd Knee_Osteoarthritis_Predictor/Model_Deployment
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Make sure the trained model file (`knee.h5`) is present in the `model` directory.

6. Start the web application by running the following command:
   ```
   python app.py
   ```

7. Open a web browser and go to `http://localhost:5000` to access the interactive tool.

8. The main page will be displayed, providing an introduction to knee osteoarthritis and an option to proceed to the login page.

9. Click on the "Login" button to navigate to the login page.

10. On the login page, enter your username and password for accessing the knee osteoarthritis predictor.

11. Once logged in, you will be redirected to the upload page.

12. On the upload page, choose an image file (in JPEG or PNG format) containing a knee X-ray and upload it using the provided interface.

13. The web application will process the uploaded image and display the predicted severity of osteoarthritis on the results page.

14. If you want to upload another image, you can go back to the upload page and repeat the process.

## HTML Pages

The web interface of the interactive tool is built using HTML pages. The `templates` directory contains the following HTML files:

- [first_1.html](templates/first_1.html): The main page that provides an introduction to knee osteoarthritis and an option to proceed to the login page.
- [login_2.html](templates/login_2.html): The login page where users can enter their credentials for accessing the knee osteoarthritis predictor.
- [upload_3.html](templates/upload_3.html): The upload page where users can choose and upload an image file containing a knee X-ray.
- [result_4.html](templates/result_4.html): The results page that displays the predicted severity of osteoarthritis based on the uploaded image.
- [chart_6.html](templates/chart_6.html): The chart page that provides information about the performance and charts related to the knee osteoarthritis prediction model.
- [performance_5.html](templates/performance_5.html): The performance page that offers additional information about the performance of the knee osteoarthritis prediction model.

You can modify these HTML files to customize the appearance and layout of the web pages according to your preferences.

## Additional Resources

For more details on the project, including model training and evaluation, refer to the [main repository](https://github.com/jithendra-varma/Knee_Osteoarthritis_Predictor).
