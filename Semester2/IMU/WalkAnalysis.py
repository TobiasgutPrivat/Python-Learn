from WalkIMUDataSet import WalkIMUDataSet
import matplotlib.pyplot as plt

#TODO: functionality to analyze the Walk data
def analyze(data: WalkIMUDataSet):
    # plot each angle for each sensor
    sensors = ["FemurAnterior", "TibiaAnterior"]#, "FemurLateral", "TibiaLateral"
    columns = ["GYRO X (deg/s)"]#"GYRO X (deg/s)", , "GYRO Z (deg/s)"
    plt.figure(figsize=(12, 8))
    for sensor in sensors:
        sensor_data = getattr(data, sensor)
        for column in columns:
            plt.plot(sensor_data.index, sensor_data[column], label=f"{sensor} {column}")
    plt.title("Walk Data Analysis")
    plt.xlabel("Time (s)")
    plt.ylabel("Sensor Readings")
    plt.legend(loc='upper right', fontsize='small')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    pass

if __name__ == "__main__":
    path = "GangLisa Konf 1.csv"
    walkIMUDataSet = WalkIMUDataSet(path)
    analyze(walkIMUDataSet)
