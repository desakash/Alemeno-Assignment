# Urine Strip Color Analyzer

The Urine Strip Color Analyzer is a web application that allows users to upload an image of a urine strip and identify the colors on the strip. Each strip typically has 10 colors, and the application analyzes the image using OpenCV to extract the RGB values of each color.

## Features

- **Upload Image**: Users can upload an image of a urine strip through the web interface.
- **Color Identification**: The application analyzes the uploaded image and identifies the RGB values of each color on the strip.
- **JSON Output**: The color values are returned as a JSON object, making it easy to integrate with other applications or systems.

## Getting Started

### Prerequisites

- Python (3.6 or higher)
- Django (version 3.2 or higher)
- OpenCV (version 4.5.3 or higher)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/urine-strip-color-analyzer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd urine-strip-color-analyzer
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

2. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Usage

1. Upload an image of a urine strip using the provided form.
2. Submit the form to analyze the colors on the strip.
3. The application will display the RGB values of each color identified on the strip.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the need for a simple tool to analyze urine strip colors ans as a Assignment from Alemeno.
- Special thanks to the contributors who helped improve this project.
