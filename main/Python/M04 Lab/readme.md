# Bookstore Database Web Application


This repository contains the source code for a simple web-based bookstore database application built using Flask and SQLAlchemy. The application allows you to perform CRUD (Create, Read, Update, Delete) operations on books in the database.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Contributing](#contributing)

## Detailed Explanation

- [About the HTML used](documentation/about-html.md): Explanation of the HTML templates used in the application.
- [About Python used](documentation/about-script.md): Detailed explanation of the main python code.
- [About the Javascript used](documentation/about-java.md): Detailed explanation of the Javascript used.
- [About the JSON](documentation/about-json.md): Detailed explanation of how JSON was implemented.

## Prerequisites

Before running this application, make sure you have the following prerequisites installed on your system:

- Python 3.x
- Pip (Python package manager)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd bookstore-database
   ```

3. Install the required Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application by running the following command:

   ```bash
   python app.py
   ```

2. The application will start running, and you will see the server information in the terminal.

3. Open a web browser and go to `http://localhost:5000` to access the bookstore database web application.

## Endpoints

The following endpoints are available in the application:

- `GET /`: Displays the list of books in the database.
- `GET /edit/<int:book_id>`: Displays an edit form for a specific book.
- `POST /edit/<int:book_id>`: Updates the details of a book.
- `POST /books`: Adds a new book to the database (JSON input).
- `GET /books`: Retrieves the list of books in the database (JSON output).
- `GET /books/<int:book_id>`: Retrieves the details of a specific book (JSON output).
- `PUT /books/<int:book_id>`: Updates the details of a specific book (JSON input).
- `DELETE /books/<int:book_id>`: Deletes a specific book from the database.

## Contributing

Contributions to this project are welcome. You can contribute by:

- Reporting issues
- Providing enhancements or new features
- Improving documentation

Please open a pull request with your contributions.

```   d8b  .d888         d8b 888    888                              .d888 888      
```   Y8P d88P"          Y8P 888    888                             d88P"  888      
```       888                888    888                             888    888      
```  8888 888888 888d888 888 888888 888888 .d8888b          8888b.  888888 888  888 
``` "888 888    888P"   888 888    888    88K                 "88b 888    888 .88P 
```   888 888    888     888 888    888    "Y8888b. 888888 .d888888 888    888888K  
```   888 888    888     888 Y88b.  Y88b.       X88        888  888 888    888 "88b 
```   888 888    888     888  "Y888  "Y888  88888P'        "Y888888 888    888  888 
```   888                                                                           
```  d88P                                                                           
```888P"                    