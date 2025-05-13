from WalkIMUDataSet import WalkIMUDataSet
import matplotlib.pyplot as plt

#TODO: functionality to analyze the Walk data
def analyze(data: WalkIMUDataSet):
    #inital data
    time_series = data.FemurAnterior.index
    sample_frequency = len(time_series) / (time_series[-1] - time_series[0])
    raw_femur = data.FemurAnterior["GYRO X (deg/s)"]
    raw_tibia = data.TibiaAnterior["GYRO X (deg/s)"]

    #remove bias
    bias_femur = raw_femur.mean()
    bias_tibia = raw_tibia.mean()

    velocity_femur = raw_femur - bias_femur
    velocity_tibia = raw_tibia - bias_tibia

    #integrate to get angle
    angle_femur = velocity_femur.cumsum() / sample_frequency
    angle_tibia = velocity_tibia.cumsum() / sample_frequency

    #angle difference
    angle_difference = angle_femur - angle_tibia

    #plot the data
    plt.figure(figsize=(12, 8))
    plt.plot(time_series, angle_difference, label="Angle Difference", color='green')
    plt.title("Walk Analysis")
    plt.xlabel("Time (s)")
    plt.ylabel("Angle (degrees)")
    plt.legend(loc='upper right', fontsize='small')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    path = "GangLisa Konf 1.csv"
    walkIMUDataSet = WalkIMUDataSet(path)
    analyze(walkIMUDataSet)
