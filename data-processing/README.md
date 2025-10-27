# Data Processing
query-related tasks, provide test_script.py to validate query execution results.

<details>
<summary>Task Description</summary>
Tugas:
Tuliskan script code SQL query dengan ketentuan berikut :
1. Tambahkan satu personal dalam table dengan nama employee Albert dengan posisi enginner, join date 24 Januari 2024, dengan Year of experience 2.5 year. With salary $50.
2. Update table dengan posisi enginner with salaray $85
3. Hitung total pengeluaran salary saat tahun 2021.
4. Sorting menampilkan 3 employee paling banyak yang memiliki Years of Experience
5. Tuliskan subquery untuk employee dengan posisi engginer yang memiliki exeperience kurang dari sama dengan 3 tahun
</details>

## Answer Summary (You can also access it in ./mysql/answers.sql)

<details>
<summary>1. Tambahkan satu personal dalam table dengan nama employee Albert dengan posisi enginner, join date 24 Januari 2024, dengan Year of experience 2.5 year. With salary $50.</summary>
```sql
INSERT INTO employees (name, position, join_date, years_of_experience, salary) VALUES ('Albert', 'Engineer', '2024-01-24', 2.5, 50.00);
```
</details>

<details>
<summary>2. Update table dengan posisi enginner with salaray $85</summary>
```sql
UPDATE employees SET salary = 85.00, WHERE position = 'Engineer';
```
</details>

<details>
<summary>3. Hitung total pengeluaran salary saat tahun 2021.</summary>
```sql
SELECT 
    SUM(
        salary * (
            CASE
                WHEN YEAR(join_date) < 2021 THEN 12
                WHEN YEAR(join_date) = 2021 THEN (12 - (MONTH(join_date) - 1))
                ELSE 0
            END
        )
    ) AS total_salary_2021
FROM employees;
```
</details>

<details>
<summary>4. Sorting menampilkan 3 employee paling banyak yang memiliki Years of Experience</summary>
```sql
SELECT name, position, years_of_experience, salary FROM employees ORDER BY years_of_experience DESC, salary DESC LIMIT 3;
```
</details>

<details>
<summary>5. Tuliskan subquery untuk employee dengan posisi engginer yang memiliki exeperience kurang dari sama dengan 3 tahun</summary>
```sql
SELECT * FROM employees WHERE position = 'Engineer' AND years_of_experience <= 3;
```
</details>


## Overview

**Main tasks include:**  

1. Insert a new employee record into the table  
2. Update salaries for employees with a specific position  
3. Calculate total salary expenditure for 2021  
4. Sort employees by years of experience  
5. Use a subquery to filter engineers with experience ≤ 3 years  

The project demonstrates SQL proficiency in **data insertion, updates, aggregation, sorting, and subqueries**.

---

## Features

- Insert employee data with specific attributes  
- Update salaries based on position  
- Aggregate total salary expenditure by year  
- Sort employees by years of experience  
- Subquery to filter employees based on criteria  
- Fully Dockerized setup for ease of deployment  

---

## Prerequisites

- Docker >= 24.0 (latest stable version recommended)  
- Internet connection (for downloading Docker images)  

No other tools or packages are required on the host system.

---

## Installation & Setup

```bash
1. git clone https://github.com/username/huawei-technical-test-I.git
2. cd huawei-technical-test-I/data-processing
3. chmod +x run-server.sh && ./run-server.sh
4. chmod +x test-queries.sh && ./test-queries.sh
5. chmod +x stop-server.sh && ./stop-server.sh (to stop docker running and delete the images)
```

### Error Guides
- You can ignore `ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock'` if it raises after the 3rd step (running run-server.sh)
- The `test_script.py` doesn't provide/handle repetitive test execution since it contains insertion query. Therefore, kindly re-execute by running `./stop-server.sh` and re-run the 3rd step (run-server.sh & test-queries.sh).


