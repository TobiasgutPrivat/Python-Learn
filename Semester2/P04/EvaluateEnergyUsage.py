from GetEnergyUsage import getEnergyUsage, getEnergyUsageSource
import matplotlib.pyplot as plt

def evaluateList(data: list[dict[str,any]]):
    # create line chart
    quarts = []
    values = []
    title_values = "MWh/Quartal"
    title_quarts = "Quartal"
    for quart in data:
        quarts.append(quart["date"])
        values.append(quart["conso_total"])
    plt.plot(quarts, values)
    plt.title("Energy Consumption in Freibourgh")
    plt.xlabel(title_quarts)
    plt.ylabel(title_values)
    plt.show()

if __name__ == "__main__":
    source = getEnergyUsageSource()
    data = getEnergyUsage(source)
    evaluateList(data)
