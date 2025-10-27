# Automation Testing
<details>
<summary>Task Description</summary>
Buatlah skrip otomatis cron tab/cron job untuk collect data dari resource tertentu dengan
collect data 3 kali dalam sehari, setiap pukul 08.00 WIB, 12.00 WIB dan 15.00 WIB
dan simpan collect data tersebut dalam path /home/cron, dengan format data
“cron_{date}_{hours}”, sebagai contoh file adalah cron_12192024_15.00, dan .csv file
akan collect setiap 3 jam.
Data Cleansing : Buatlah skrip otomatis yang berbeda untuk menghapus file setelah
sebulan dalam path tersebut secara otomatis.
</details>

## Overview

This submodule implements automated data collection and data cleansing using Docker.  

**Main functionalities:**  

1. **Data Collection:** Collect data from specified resources **three times daily** at 08:00, 12:00, and 15:00 WIB.  
2. **Data Storage:** Save collected data as CSV files in `/home/cron` inside the container (host-mounted directory: `./output/home/cron`) with timestamped filenames: `cron_{date}_{hours}.csv`.  
3. **Data Cleansing:** Automatically remove files older than 30 days.  
4. **Containerization:** Fully Dockerized, requiring only Docker and internet access on the host.  

This ensures reliable automation, accurate data collection, and seamless maintenance.

---

## Features

- Automated data collection three times daily  
- Timestamped CSV file generation  
- Automated removal of files older than 30 days  
- Fully Dockerized for easy deployment  
- Simple `run.sh` and `stop.sh` scripts to manage the container  

---

## Prerequisites

- Docker >= 24.0 (latest stable version recommended)  
- Internet connection for building Docker images and accessing external data  

No additional tools or dependencies are required on the host system.

---

## Installation & Setup

```bash
git clone https://github.com/username/huawei-technical-test-I.git
cd huawei-technical-test-I/automation-testing
mkdir -p ./output/home/cron
chmod +x run.sh && ./run.sh
chmod +x stop.sh && ./stop.sh (stop the docker container and delete image after testing)
```
