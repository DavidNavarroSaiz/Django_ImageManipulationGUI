# Django Image Processor Demo

This Django application is a simple web app that allows users to apply basic image operations, particularly focusing on HSL color ranges and threshold ranges. It provides functionality to control these operations using two bars.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Features

- Convert the image to HSL color space.
- Convert the image to grayscale.
- Operate on specific image channels (R, G, B).
- Apply simple thresholding operations.
- Apply range-based operations on the image.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/django-image-processor-demo.git
   cd django-image-processor-demo

    ```

2. Create a virtual environment and activate it:

```
python3 -m venv env
source env/bin/activate
```
3.Install the dependencies:

```
pip install -r requirements.txt

```
## Usage

Run the Django development server:
```
python manage.py runserver

```
Open the application in your web browser: http://localhost:8000

Upload an image and use the provided controls to apply various image operations.