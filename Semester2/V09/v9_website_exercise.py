# -*- coding: utf-8 -*-
"""
v9
Lists all modules in the curriculum from our BSc study
"""

import inscriptis
import pandas as pd
import urllib.request
import sys

# Main execution
url = 'https://www.zhaw.ch/de/engineering/studium/bachelorstudium/medizininformatik/curriculum-studium-medizininformatik/'
# try with other BSc programs
# url = 'https://www.zhaw.ch/de/engineering/studium/bachelorstudium/systemtechnik/curriculum-lehrplan/'
# url = 'https://www.zhaw.ch/de/engineering/studium/bachelorstudium/data-science/curriculum-lehrplan/'


# load website
try:
    fweb = urllib.request.urlopen(url)
except Exception as e:
    print(f"Cannot load data! ({e})", file=sys.stderr)
    exit(-1)
else:
    data_html = fweb.read().decode()
    data_text = inscriptis.get_text(data_html)

# Split the text into lines
lines = data_text.strip().split('\n')

# Prepare a list to collect module data
VZ = None
modules_VZ = []
modules_TZ = []
current_semester = ""
module_name = ""

# Iterate over each line in the text
for i, line in enumerate(lines):
    if 'Vollzeitstudium' in line:
        VZ = True
    if 'Teilzeitstudium' in line:
        VZ = False
    if 'Semester,' in line: 
        current_semester = line.split(",")[0].strip()
    elif 'ECTS:' in line:
        # Extract ECTS value
        # "* ECTS: 4"
        ects = int(line.split(':')[1].strip())
        # Capture the module name from the previous lines
        module_name = lines[i - 2].strip()
        description = lines[i + 3].strip()
        if VZ:
            modules_VZ.append({"Semester": current_semester, "Module": module_name, "ECTS": ects, "Description": description})
        else:
            modules_TZ.append({"Semester": current_semester, "Module": module_name, "ECTS": ects, "Description": description})
    
# Create DataFrame from collected module data
df_VZ = pd.DataFrame(modules_VZ)
df_TZ = pd.DataFrame(modules_TZ)

print("VZ:")
print(df_VZ)
print("TZ:")
print(df_TZ)

# Extent this script
# 1. Make 2 DataFrames for the modules, one for VZ, one for TZ
# 2. Present the DFs sorted to number of credits
# 3. Add the details of the modules as column in the DF, note that for MI-TZ, maybe not all modules have details


"""
example of data_text
1. Semester, ECTS: 30, Semester Wochenlektionen: 30

                Communication Competence 1

                  Communication Competence 1

                    * ECTS: 2
                    * Details zu diesem Modul

                  Im Modul Co mmunication Competence 1 liegt der Schwerpunkt auf folgenden Aspekten des Kommunikationstrainings: Information im wissenschaftlichen Kontext recherchieren und verarbeiten // Auftritts- und Sprachkompetenz für Präsentationen weiterentwickeln // Im Team Kommunikation gestalten und Feedback geben // Unterrichtssprache: DE/EN

                Informatikprojekte

                  Informatikprojekte

                    * ECTS: 4
                    * Details zu diesem Modul

                  Informatik-Projekte sind das Haupt-Einsatzgebiet von Medzinal Informatik Ingenieuren. Angemessene Fertigkeiten der Studierenden in diesem Gebiet sind deshalb von grosser Bedeutung für die Ausbildung. In diesem ersten Projektmodul wird Fachwissen aus anderen Informatik Modulen angewandt und mit ersten Erfahrungen in Team-Projektarbeit angereichert. Dies beinhaltet Team- und Einzelarbeit bei Projektplanung, Erstellung von technischen Texten, Softwareentwurf und Codeverwaltung. // Unterrichtssprache: DE

                Informatik Programmieren 1

                  Informatik Programmieren 1

                    * ECTS: 4
                    * Details zu diesem Modul

                  Einführung in die Programmierung mit der Programmiersprache Python. // Unterrichtssprache: DE

                Datenbanken

                  Datenbanken

                    * ECTS: 4
                    * Details zu diesem Modul

                  Grundlagen der relationalen Datenbanken: relationale Algebra, Entity-Relationship-Design, SQL DDL/DML, effiziente und korrekte Datenbankabfragen in SQL, Indexe, Trigger, Transaktionen/ACID // Unterrichtssprache: DE
"""