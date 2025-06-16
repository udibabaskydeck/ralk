# RALK

This tool prunes a list of Linux kernel CVEs based on code reachability analysis. It identifies which CVEs are relevant to a given system or workload by checking if the affected symbols are reachable in your environment.

## 📌 Features

- Parses a CSV list of CVEs with affected file/function information
- Filters CVEs based on a list of reachable kernel symbols
- Outputs a reduced list of relevant CVEs

## 📂 Input Files

### 1. `cve_list.csv`
A CSV file containing CVEs and the corresponding file and symbol they affect.

**Example:**
```csv
CVE_ID,Affected_File,Affected_Symbol
CVE-2021-1234,net/core/dev.c,netif_rx
CVE-2022-2345,fs/ext4/super.c,ext4_fill_super
CVE-2023-3456,drivers/net/e1000e/netdev.c,e1000e_open
