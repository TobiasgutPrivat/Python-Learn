# importIMUData.py
# This script reads an IMU data file and extracts sensor data into separate DataFrames.
#
# Expects CSV file with the following structure:
# 1. 3 irrelevant lines
skipLines = 3
# 2. list of sensornames in the 4th line with seperating commas indicating the number of values per sensor
# 3. some irrelevant lines
# 4. data (head indicated by having string "ACC X Time Series"), which can includes time series for each sensor. indicated by string "Time Series (s)"
firstValueHead = "ACC X Time Series"

import pandas as pd

def readIMUFile(fileName: str) -> tuple[str, pd.DataFrame]:
    with open(fileName, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        sensorLine = lines[skipLines].strip()  # Read the first line for the sensor tag

    # Finde startline
    for i, line in enumerate(lines):
        if firstValueHead in line:
            header_line_index = i
            break
    data = pd.read_csv(fileName, skiprows=header_line_index)
    # turn values into floats
    data = data.apply(pd.to_numeric, errors='coerce')
    data = data.dropna(how='all')
    
    return sensorLine, data

def GetIMUSensorData(fileName: str) -> dict[str,pd.DataFrame]:
    sensorLine, data = readIMUFile(fileName)
    data: pd.DataFrame
    sensorIndexes = {}
    for i, sensor in enumerate(sensorLine.split(",")):
        if not sensor.strip():
            continue

        #expected format: "Sensor Name (Sensor Number)"
        sensor = sensor.strip()
        # remove sensornumber from sensor name
        if "(" in sensor and ")" in sensor:
            sensor = sensor.split("(")[0].strip()

        if sensor not in sensorIndexes:
            sensorIndexes[sensor] = i

    # Split the data into multiple DataFrames
    dataframes = {}
    spacing = len(sensorLine.split(",")) // (len(sensorIndexes)-1) # -1 because the last sensor has no noted commas

    for sensor, index in sensorIndexes.items():
        # Extract the relevant columns for each sensor
        sensor_data = data.iloc[:, range(index, index + spacing)]
        sensor_data: pd.DataFrame
        sensor_data.columns = [col.split(".")[0].strip() for col in sensor_data.columns]

        #remove rdeundant time Series
        timeSeriesString = "Time Series (s)"
        intial_col = None
        for col in sensor_data.columns:
            if timeSeriesString in col:
                if intial_col == None:
                    intial_col = col
                else:
                    sensor_data.drop(columns=[col], inplace=True)

        sensor_data.set_index(intial_col, inplace=True)
        
        dataframes[sensor] = sensor_data

    return dataframes

if __name__ == "__main__":
    sensorData = GetIMUSensorData("GangLisa Konf 1.csv")
    for sensor, data in sensorData.items():
        print(f"Sensor: {sensor}")
        print(data.head())  # Print the first few rows of each DataFrame
        print()
