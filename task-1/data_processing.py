import csv

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_csv(filename, data, fieldnames):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data written to {filename}")

def filter_data(data, key, value):
    return [row for row in data if row.get(key) == value]

# Example Usage
if __name__ == "__main__":
    # Sample Data
    data = [
        {"name": "Aayush", "age": "25"},
        {"name": "Nitin", "age": "30"},
        {"name": "Atul", "age": "25"}
    ]
    write_csv("people.csv", data, fieldnames=["name", "age"])

    rows = read_csv("people.csv")
    filtered = filter_data(rows, "age", "25")

    print("Filtered Data:")
    for row in filtered:
        print(row)
