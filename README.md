# Real-Time-Vibration-Monitoring-and-Analysis-System-Using-ESP32-and-ADXL345
Project Summary

This project utilizes the ESP32 microcontroller and ADXL345 accelerometer sensor to collect vibration data, analyze it, and effectively visualize the results. The project integrates various software components and technologies to handle data processing and visualization.
1. Arduino Code

    Function: Collects data from the ADXL345 accelerometer sensor and transmits it to a server in JSON format.
    Libraries Used: WiFi.h, HTTPClient.h, SPI.h, Adafruit_Sensor.h, Adafruit_ADXL345_U.h.
    Process Steps:
        Establishes a Wi-Fi connection.
        Initializes the ADXL345 sensor.
        Processes X, Y, and Z-axis data and sends it via an HTTP POST request to the specified server.

2. Python Code
a. data_analysis.py

    Function: Analyzes and classifies data from the database.
    Process Steps:
        Retrieves data from the vibration_data table.
        Classifies data as 'Stable' or 'Vibrating' based on standard deviations of X, Y, and Z axes.
        Saves classified data to the classified_data table.

b. model_training.py

    Function: Trains a classification model.
    Process Steps:
        Extracts data from the classified_data table.
        Separates data into features and target variables.
        Trains a Random Forest classifier.
        Evaluates model performance and saves the model to a file.

c. predict_new_data.py

    Function: Makes predictions on new data.
    Process Steps:
        Retrieves new data from the vibration_data table.
        Loads the trained model and makes predictions.
        Saves prediction results to the classified_data table.

3. PHP Code
a. server.php

    Function: Receives data from Arduino and stores it in the MySQL database.
    Process Steps:
        Receives and parses JSON data.
        Inserts data into the vibration_data table.

b. get_data.php

    Function: Provides classified data in JSON format.
    Process Steps:
        Retrieves data from the classified_data table and returns it in JSON format.

4. HTML and JavaScript Code

    Function: Visualizes data.
    Process Steps:
        Fetches data via get_data.php.
        Creates a chart and table with the fetched data.
        The chart displays X, Y, and Z values over time.
        The table highlights data statuses and abnormal vibrations.
        The chart and table are updated every second.

Overall Flow

    Data Collection: The Arduino collects data from the ADXL345 sensor and transmits it to the server via an HTTP POST request.
    Data Storage and Analysis: PHP scripts store data in the MySQL database. Python scripts analyze and classify the data, with classified data stored back in the database.
    Model Training and Prediction: Python scripts train a classification model and make predictions on new data, storing the results in the database.
    Visualization: HTML and JavaScript are used to visualize the data in a chart and table, with continuous updates.

This system collects and analyzes sensor data in real-time and visualizes the results effectively, enabling users to monitor vibration data in detail.
