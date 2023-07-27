# Streamlit Pubs Finder App

The Streamlit Pubs Finder App is a web application that allows users to find nearby pubs and bars based on their location. This app utilizes the Streamlit framework to create an interactive and user-friendly interface, making it easy for users to explore and discover local pubs in their area.

## Prerequisites

Before running the application, make sure you have the following installed:

1. Python 3.6 or higher
2. pip (Python package manager)

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/streamlit-pubs-finder.git
cd streamlit-pubs-finder
```

2. Create a virtual environment (optional, but recommended):

```bash
python -m venv venv
```

3. Activate the virtual environment (optional, but recommended):

On Windows:

```bash
venv\Scripts\activate
```

On macOS and Linux:

```bash
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the App

To run the Streamlit Pubs Finder App, use the following command:

```bash
streamlit run app.py
```

This command will start the development server, and you should see a local URL in your terminal. Typically, it will be `http://localhost:8501`. Open this URL in your web browser to access the application.

## Usage

1. **Home Page**: Upon opening the application, you will see the home page. Here, you can enter your current location (latitude and longitude) or use the "Use My Location" button to automatically detect your location.

2. **Map View**: After providing your location, the application will display a map view with markers representing nearby pubs and bars. Clicking on a marker will show additional information about the selected pub.

3. **Filtering**: You can use the filter options on the sidebar to narrow down the search based on specific criteria such as distance, ratings, or opening hours.

4. **List View**: The app also provides a list view of the nearby pubs, which can be accessed by clicking the "List View" option on the sidebar. This view displays basic information about each pub in a tabular format.

## Contributing

Contributions to the Streamlit Pubs Finder App project are welcome. If you find any issues or want to add new features, please follow these steps:

1. Fork the repository on GitHub.

2. Create a new branch from the `main` branch.

3. Make your changes and improvements.

4. Test the application to ensure everything works as expected.

5. Commit your changes and push them to your forked repository.

6. Create a pull request to the original repository's `main` branch.

7. Please provide a clear description of the changes you made and why they are beneficial.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This project was inspired by the love for pubs and bars all around the world!
- Thanks to the Streamlit team for creating such a fantastic framework.

## Contact

If you have any questions, suggestions, or feedback, feel free to reach out to us at [vsrivarshith@gmail.com] We'd love to hear from you!

---

This README provides a general outline for your Streamlit Pubs Finder App project. Feel free to customize it further based on the specifics of your project. Make sure to update the contact email, acknowledgments, and other relevant information to reflect the actual contributors and resources used in your app.
