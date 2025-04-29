import requests
import pandas as pd

url = "https://data.geo.admin.ch/ch.meteoschweiz.klima/nbcn-tageswerte/nbcn-daily_RAG_current.csv"
filename = "BadRagaz.csv"
# format of the data:
# station/location;date;gre000d0;hto000d0;nto000d0;prestad0;rre150d0;sre000d0;tre200d0;tre200dn;tre200dx;ure200d0
# RAG;20250101;66;-;-;967.4;0;362;3.4;-1.2;8.3;56.6
# RAG;20250102;34;-;-;957.9;7.2;10;5.8;1;11;55.3
# RAG;20250103;41;-;-;962.6;0.1;66;0.4;-2.5;2.3;85.7
# RAG;20250104;65;-;-;960.5;0.6;363;-0.9;-3.1;5.3;69.9
 
def retrieve():
    response = requests.get(url)
    data = response.text
    with open(filename, "w") as file:
        file.write(data)
    print(f"Data saved to {filename}")

def evaluate():
    df = pd.read_csv("BadRagaz.csv", sep=';')
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
    df = df.sort_values('date', ascending=False).head(7) #Um die ersten 7 Zeilen zu holen
    sunshine = df['sre000d0']
    # correction -Tobias
    total_sunshine = sum(sunshine.values)
    sunshine_avg = total_sunshine / 7
    # sunshine_avg = sunshine / 7
    print(f"Average sunshine duration: {sunshine_avg} minutes.")


if __name__ == "__main__":
    retrieve()
    evaluate()

# was good, apart from average. -Tobias