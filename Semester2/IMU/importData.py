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
    sonsorIndexes = {}
    for i, sensor in enumerate(sensorLine.split(",")):
        if not sensor.strip():
            continue

        sensor = sensor.strip()
        if sensor not in sonsorIndexes:
            sonsorIndexes[sensor] = i

    print(sonsorIndexes)  # Display the sensor indexes for verification

    # Assuming the data is structured in a way that allows for splitting into multiple DataFrames
    # Femur Anterior (75657), , , , , , , , , , , , Femur Lateral (75758), , , , , , , , , , , , Tibia Anterior (75557), , , , , , , , , , , , Tibia Lateral (75812) (sensorLine)
    # sensor mode: 609, , , , , , , , , , , , sensor mode: 609, , , , , , , , , , , , sensor mode: 609, , , , , , , , , , , , sensor mode: 609
    # ACC X Time Series (s), ACC X (G), ACC Y Time Series (s), ACC Y (G), ACC Z Time Series (s), ACC Z (G), GYRO X Time Series (s), GYRO X (deg/s), GYRO Y Time Series (s), GYRO Y (deg/s), GYRO Z Time Series (s), GYRO Z (deg/s), ACC X Time Series (s), ACC X (G), ACC Y Time Series (s), ACC Y (G), ACC Z Time Series (s), ACC Z (G), GYRO X Time Series (s), GYRO X (deg/s), GYRO Y Time Series (s), GYRO Y (deg/s), GYRO Z Time Series (s), GYRO Z (deg/s), ACC X Time Series (s), ACC X (G), ACC Y Time Series (s), ACC Y (G), ACC Z Time Series (s), ACC Z (G), GYRO X Time Series (s), GYRO X (deg/s), GYRO Y Time Series (s), GYRO Y (deg/s), GYRO Z Time Series (s), GYRO Z (deg/s), ACC X Time Series (s), ACC X (G), ACC Y Time Series (s), ACC Y (G), ACC Z Time Series (s), ACC Z (G), GYRO X Time Series (s), GYRO X (deg/s), GYRO Y Time Series (s), GYRO Y (deg/s), GYRO Z Time Series (s), GYRO Z (deg/s)

    # Split the data into multiple DataFrames

    pass

if __name__ == "__main__":
    GetSensorData()
