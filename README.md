# Deep Learning-Based Assessment of Parkinson’s Disease Severity - WebApp

This project provides a web application for assessing the severity of Parkinson’s disease using deep learning techniques. The model analyzes input data and predicts the severity of the disease.

## Features

- **Deep Learning Model Integration**: Uses a trained neural network for Parkinson’s disease assessment.
- **User-Friendly Interface**: Simple and interactive web app for predictions.
- **Flask Backend**: Serves the deep learning model and handles API requests.
- **Responsive Design**: Works across multiple devices.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Flask (Python)  
- **Machine Learning**: TensorFlow/Keras  
- **Deployment**: Flask Server  

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/prashanth370/Deep-Learning-based-assessment-of-Parkinson-s-disease-severity.git
   cd Deep-Learning-based-assessment-of-Parkinson-s-disease-severity/WebApp
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open your browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

## Usage

- Upload or input required data for Parkinson’s disease assessment.  
- Click on the **Predict** button to get the severity analysis.  

## Folder Structure

```
📂 WebApp
├── 📂 static        # Contains CSS, JS, and images
├── 📂 templates     # HTML templates for the frontend
├── app.py          # Flask application
├── model.pkl       # Trained deep learning model
├── requirements.txt # Dependencies
```

## Dependencies

Ensure you have the required Python libraries installed:

```bash
pip install Flask tensorflow numpy pandas scikit-learn
```

## License

This project is open-source and available under the MIT License.

---
