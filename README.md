# Knee Osteoarthritis Predictor

Knee Osteoarthritis Predictor is a deep learning-based project that aims to predict knee osteoarthritis using the Kellgren-Lawrence system of classification. The project consists of two main components: model training and model deployment. The model training phase involves training a VGG-16 convolutional neural network (CNN) model on a dataset of knee X-ray images. The trained model is then deployed in a web application, allowing users to upload their knee X-ray images and obtain predictions regarding the severity of osteoarthritis.

## Repository Structure

The repository is organized into the following directories:

- **model-training**: Contains code and resources related to the model training phase.
- **model-deployment**: Includes code and files necessary for deploying the trained model and developing the web application.

For a detailed overview of the repository structure, refer to the [Repository Structure](./repository-structure.md) documentation.

## Usage

To use the Knee Osteoarthritis Predictor, follow these steps:

1. **Model Training**: Navigate to the `model-training` directory to access the code and resources related to the model training phase. Refer to the [Model Training Guide](./model-training/README.md) for detailed instructions.

2. **Model Deployment**: Proceed to the `model-deployment` directory to find the code and files for model deployment and web application development. Consult the [Model Deployment Guide](./model-deployment/README.md) for step-by-step instructions.

## Results

After training the model and deploying it as a web application, the Knee Osteoarthritis Predictor provides users with predictions regarding the severity of knee osteoarthritis based on uploaded X-ray images. The web application offers a user-friendly interface, enabling easy and efficient utilization of the predictor.

## Contributing

Contributions to the Knee Osteoarthritis Predictor project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to submit an issue or a pull request.

## License

This project is licensed under the [MIT License](./LICENSE).

## Acknowledgements

- [Kellgren-Lawrence Classification System](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4715541/)
- [VGG-16 Model](https://arxiv.org/abs/1409.1556)

