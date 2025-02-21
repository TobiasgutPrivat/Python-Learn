import pandas as pd
import matplotlib.pyplot as plt
# Load the CSV data
data = pd.read_csv('C:/Users/tobia/GitProjekte/Python Learn/DISP/SW1/healthcare_institution_electronic_system_data.csv', sep=';')
# Set the Institution Type column as the index and transpose the DataFrame
data = data.set_index('Institution Type').T
# Plot the data
plt.figure(figsize=(10, 6))
for column in data.columns:
    plt.plot(data.index, data[column], marker='o', label=column)

plt.title('Development of Electronic Systems for Medical Patient Data Management')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Institution Type')
plt.grid(True)
plt.tight_layout()
plt.show()
