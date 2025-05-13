from WalkIMUDataSet import WalkIMUDataSet
import matplotlib.pyplot as plt
import pandas as pd

def analyze_walk(walkIMUDataSet: WalkIMUDataSet):
    time_series, knee_angle = get_knee_angle(walkIMUDataSet)
    starts, ends = detect_cycles(time_series, knee_angle)
    avg_period_time = (time_series[starts[-1]] - time_series[starts[0]]) / (len(starts)-1)
    period_time_series, periods = get_gait_cycle_periods(time_series, knee_angle, starts, avg_period_time)
    plot_knee_angle(time_series, knee_angle)
    plot_walk_periods(period_time_series, periods)

def get_gait_cycle_periods(time_series: pd.Series, knee_angle: pd.Series, starts: list[int], avg_period_time: float):
    periods: list[pd.Series] = []
    period_time_series = get_time_series(time_series, starts[0], avg_period_time) - time_series[starts[0]]
    for i in range(len(starts)):
        period_time_series = get_time_series(time_series, starts[i], avg_period_time)
        period = knee_angle[period_time_series]
        # period.set_index(period_time_series, inplace=True)
        periods.append(period)
    return period_time_series, periods

def get_time_series(time_series, start: int, length: float):
    end = time_series.searchsorted(time_series[start] + length)
    return time_series[start:end]

def get_knee_angle(data: WalkIMUDataSet):
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

    return time_series, angle_difference

def detect_cycles(time_series: pd.Series, knee_angle: pd.Series):
    #This is where the knee is fully extended, and the heel touches the ground a�er the swing phase. A good signal to detect this is the angular velocity signal from the lower leg, but you may use another suitable signal. The graph below shows both the heel strike and the toe off events, only the heel strike event is required. 
    threshold = 20 #degrees
    #find indexes where the knee angle is above the threshold but previous isnt
    threshold_passes = []
    for i in range(1, len(time_series)):
        if knee_angle[time_series[i]] > threshold and knee_angle[time_series[i-1]] < threshold:
            threshold_passes.append(i)
    
    # find low turning point before the threshold
    starts = []
    for i in threshold_passes:
        for j in range(i, 0, -1):
            if knee_angle[time_series[j]] < knee_angle[time_series[j-1]] and knee_angle[time_series[j]] < knee_angle[time_series[j+1]]:
                starts.append(j)
                break
    
    ends = []
    for i in threshold_passes:
        for j in range(i, len(knee_angle)):
            if knee_angle[time_series[j]] < knee_angle[time_series[j-1]] and knee_angle[time_series[j]] < knee_angle[time_series[j+1]]:
                ends.append(j)
                break
    
    return starts, ends

def plot_knee_angle(time_series, knee_angle):
    #plot the data
    plt.figure(figsize=(12, 8))
    plt.plot(time_series, knee_angle, color='blue', alpha=0.5)
    plt.title("Knee Angle")
    plt.xlabel("Time (s)")
    plt.ylabel("Angle (degrees)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_walk_periods(time_series, periods):
    average_period = []
    for i in time_series:
        average_period.append(sum([period[i] for period in periods]) / len(periods))
    plt.figure(figsize=(12, 8))
    for period in periods:
        plt.plot(time_series, period, color='blue', alpha=0.5)
    plt.plot(time_series, average_period, color='red', label='Average Period', linewidth=2)
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
    analyze_walk(walkIMUDataSet)
