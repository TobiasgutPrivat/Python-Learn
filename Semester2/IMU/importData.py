import pandas as pd

def readFile():
    fileName = "GangLisa Konf 1.csv"

    with open(fileName, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        sensorLine = lines[3].strip()  # Read the first line for the sensor tag

    # Finde startline
    for i, line in enumerate(lines):
        if 'ACC X Time Series' in line:
            header_line_index = i
            break

    return sensorLine, pd.read_csv(fileName, skiprows=header_line_index)

def GetSensorData() -> dict[str,pd.DataFrame]:
    sensorLine, data = readFile()
    sensorIndexes = {}
    for i, sensor in enumerate(sensorLine.split(",")):
        if not sensor.strip():
            continue

        sensor = sensor.strip()
        if sensor not in sensorIndexes:
            sensorIndexes[sensor] = i

    # Split the data into multiple DataFrames
    dataframes = {}
    spacing = len(sensorLine.split(",")) // (len(sensorIndexes)-1) # -1 because the last sensor has no noted commas

    for sensor, index in sensorIndexes.items():
        # Extract the relevant columns for each sensor
        sensor_data = data.iloc[:, range(index, index + spacing)]
        sensor_data.columns = [col.split(".")[0] for col in sensor_data.columns]

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
    sensorData = GetSensorData()
    for sensor, data in sensorData.items():
        print(f"Sensor: {sensor}")
        print(data.head())  # Print the first few rows of each DataFrame
        print()
