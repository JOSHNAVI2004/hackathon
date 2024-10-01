from flask import Flask, request
import pickle

# Load the model
with open('model.pkl', 'rb') as model:
    ai = pickle.load(model)

app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # Check if 'sensorvalue' is in request.args
    if 'sensorvalue' not in request.args:
        return "Error: 'sensorvalue' parameter is required.", 400

    try:
        # Get the sensor value from the query parameters
        sensorvalue = int(request.args.get('sensorvalue'))
        # Make a prediction
        result = ai.predict([[sensorvalue]])[0]
        return f"Prediction: {result}"
    except ValueError:
        return "Error: Invalid 'sensorvalue' format. Must be an integer.", 400
    except Exception as e:
        return f"Error: {str(e)}", 500  # Return any other errors

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000)
