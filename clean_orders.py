import csv


def clean_orders(input_file, output_file):
    with open(input_file) as source:
        reader = csv.DictReader(source)
        orders = []

        for row in reader:
            if row["email"]:
                row["email"] = row["email"].lower()
                orders.append(row)

    with open(output_file, "w") as target:
        writer = csv.DictWriter(target, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(orders)
