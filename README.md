# Image Recognition System

## Description
A web application allowing users to upload images and have them classified into predefined categories (e.g., animals, vehicles, landscapes). The system leverages Python with TensorFlow's pre-trained ResNet50 model for classification, alongside a Node.js frontend to handle uploads and present results. The entire solution is containerized with Docker for ease of deployment and scalability.

## Installation Instructions

### Prerequisites
Docker and Docker Compose installed on your machine.

### Steps
1. Clone this repository:  
    `git clone <your-repository-url>`  
    `cd <project-folder>`  
2. Build and run the application using Docker Compose:  
    `docker compose build`  
    `docker compose up`  
3. Access the web interface:
- Node.js Web Server: http://localhost:3000

## Usage
- Open your browser to http://localhost:3000.
- Click the upload button to select an image file.
- Submit the form and wait briefly for the classification results.
- The predicted categories and confidence levels will display on the screen.

## Features
- Image classification into predefined categories using ResNet50.
- Web-based interface for ease of use.
- Docker containerization for consistent deployment.
- FastAPI for efficient API handling.
- Node.js backend for file handling and user interaction.

## Current Limitations
I chose to use ResNet50 as the data model based on its reputation of performing exceptionally well on common object classes. Limitations quickly revealed themselves when I ran my profile image through it.  
| Photo                                     | Results                                    |
|-------------------------------------------|--------------------------------------------|
| <img src="/images/photo.jpeg width="300"> | <img src="/images/results.png width="300"> |


### Common limitations of ResNet50:
1. Fixed Input Size and Color Channels:
- Expects images of exactly 224x224 pixels and exactly 3 RGB channels.
- Requires additional preprocessing to handle different sizes or transparency (alpha channel).
2. Predefined Categories (ImageNet Classes):
- The model classifies images into 1000 categories defined by ImageNet.
- If your images fall outside these categories or you require custom categories, the model won't provide meaningful results without additional training.
3. Limited Generalization:
- While ResNet50 performs exceptionally well on many common object classes, it may struggle with highly specialized, abstract, or unusual imagery.
4. Computational Resources:
- Relatively resource-intensive, requiring decent CPU/GPU memory and processing power.

### Alternatives and Enhancements:
#### 🚀 Alternative Models:
- EfficientNet: Great for resource-limited environments, offers excellent accuracy and efficiency.
- MobileNet V2 or V3: Ideal for mobile or web-based apps needing low-latency predictions.
- InceptionV3/V4: Excellent balance of accuracy and performance, handles diverse image types well.
- Vision Transformer (ViT): Strong at generalization, especially with fine-tuning.

#### 🔄 Fine-tuning and Custom Training:
To overcome ResNet50’s limitations, you could fine-tune the model with a custom dataset:
- Label your own data to match specific categories.
- Train (fine-tune) ResNet50 on this data using transfer learning.
- Deploy a model customized precisely for the current use case.

#### 📦 Using Cloud-based APIs (Optional):
Cloud models would offer broader recognition and fewer limitations, but at an increased cost:
- Google Vision AI
- AWS Rekognition
- Azure Cognitive Services

## Contributing
This is a learning project for me. While I am not looking for contributions, feedback is welcome!

Feel free to open issues for bugs or feature requests.

## License
MIT License

## Contact Info or Support
Visit [My Portfolio Page](https://davenull311.github.io/) for contact info. 

## Acknowledgments
Thanks for all who have given feedback! 