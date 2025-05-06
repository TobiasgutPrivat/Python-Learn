from ImportIMUData import GetIMUSensorData
import pandas as pd

class WalkIMUDataSet:
    FemurAnterior: pd.DataFrame
    FemurLateral: pd.DataFrame
    TibiaAnterior: pd.DataFrame
    TibiaLateral: pd.DataFrame

    def __init__(self, path):
        self.path = path

        SensorData = GetIMUSensorData(path)
        #expected data format: 
        # 1. Femur Anterior
        # 2. Femur Lateral
        # 3. Tibia Anterior
        # 4. Tibia Lateral
        self.FemurAnterior = SensorData["Femur Anterior"]
        self.FemurLateral = SensorData["Femur Lateral"]
        self.TibiaAnterior = SensorData["Tibia Anterior"]
        self.TibiaLateral = SensorData["Tibia Lateral"]

if __name__ == "__main__":
    path = "GangLisa Konf 1.csv"
    walkIMUDataSet = WalkIMUDataSet(path)
    print("Femur Anterior Data:")
    print(walkIMUDataSet.FemurAnterior.head())
    print("\nFemur Lateral Data:")
    print(walkIMUDataSet.FemurLateral.head())