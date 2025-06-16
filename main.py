import csv

def load_reachable_symbols(filepath):
    with open(filepath) as f:
        return set(line.strip() for line in f if line.strip())

def prune_cves(cve_csv_path, reachable_symbols_path, output_path):
    reachable = load_reachable_symbols(reachable_symbols_path)
    pruned = []

    with open(cve_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            affected_symbol = row['Affected_Symbol']
            if affected_symbol in reachable:
                pruned.append(row)

    # Write the pruned list
    with open(output_path, 'w', newline='') as csvfile:
        fieldnames = ['CVE_ID', 'Affected_File', 'Affected_Symbol']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(pruned)

    print(f"Pruned list saved to {output_path}, {len(pruned)} CVEs matched reachability.")

# Usage
prune_cves("cve_list.csv", "reachable_symbols.txt", "pruned_cves.csv")
