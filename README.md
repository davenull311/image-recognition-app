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

## Contributing
This is a learning project for me. While I am not looking for contributions, feedback is welcome!

Feel free to open issues for bugs or feature requests.

## License
MIT License

## Contact Info or Support
Visit [My Portfolio Page](https://davenull311.github.io/) for contact info. 

## Acknowledgments
Thanks for all who have given feedback! 