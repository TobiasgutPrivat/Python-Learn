"""
Context:
Hospitals store large amounts of data keyed by patient ID. A hash map (dictionary)
allows quick lookups by ID.

Exercise:
1) Create a dictionary patient_records mapping IDs to short info strings.
2) Add a few records, retrieve one by its key, and demonstrate key checking.
"""


def demo_hash_map():
    patient_records = {}

    patient_records["1001"] = "Patient A: Diagnosed with flu"
    patient_records["1002"] = "Patient B: Chest X-Ray pending"
    patient_records["1003"] = "Patient C: Discharged"

    # Retrieving
    pid_to_lookup = "1002"
    if pid_to_lookup in patient_records:
        print(f"Record for {pid_to_lookup}:", patient_records[pid_to_lookup])
    else:
        print(f"No record found for {pid_to_lookup}")

    # Checking keys
    print("All patient IDs:", patient_records.keys())


if __name__ == "__main__":
    demo_hash_map()
