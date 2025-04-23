import requests
# Create a small Python application that downloads a daily wind measurements
# archive and calculates the average sunshine duration (minutes) for Bad Ragaz over
# the past 7 days.

#consts
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

def get_sunshine_duration_last_7_days():
    with open(filename, "r") as file:
        lines = file.readlines()

    sunshine_duration = 0
    for line in lines[1:]:  # Skip the header line
        parts = line.strip().split(";")
        if len(parts) > 7:
            sunshine_duration += int(parts[7])  # Assuming the sunshine duration is in the 8th column

    return sunshine_duration / len(lines[1:])  # Average over the number of days

if __name__ == "__main__":
    retrieve()
    avg_sunshine_duration = get_sunshine_duration_last_7_days()
    print(f"Average sunshine duration over the past 7 days: {avg_sunshine_duration} minutes")


