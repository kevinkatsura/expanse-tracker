#!/usr/bin/env python

import mysql.connector
from mysql.connector import Error
import os
import time
import datetime
from decimal import Decimal

MYSQL_HOST = os.environ.get("MYSQL_HOST", "mysql")
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD", "rootpass")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "employee")

# --- Connect to MySQL ---
def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        return conn
    except Error as e:
        print("Error connecting to MySQL:", e)
        return None


# 1. Tambahkan satu personal dalam table dengan nama employee Albert dengan posisi enginner, 
# join date 24 Januari 2024, dengan Year of experience 2.5 year. 
# With salary $50.def test_insert_engineer():
def test_insert_engineer():
    expected = ('Albert', 'Engineer', datetime.date(2024, 1, 24), 3, Decimal('50.00'))
    conn = connect_to_mysql()
    if not conn:
        return "INSERT ENGINEER TEST FAILED: Connection error"

    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO employees (name, position, join_date, years_of_experience, salary)
        VALUES ('Albert', 'Engineer', '2024-01-24', 2.5, 50.00)
        """)
        conn.commit()

        cursor.execute("""
        SELECT name, position, join_date, years_of_experience, salary
        FROM employees
        WHERE name = 'Albert' AND position = 'Engineer'
        """)
        row = cursor.fetchone()
        return "INSERT ENGINEER TEST ====> PASSED" if row == expected else f"INSERT ENGINEER TEST FAILED: {row}"

    except Error as e:
        return f"INSERT ENGINEER TEST FAILED: {e}"

    finally:
        cursor.close()
        conn.close()

# 2. Update table dengan posisi enginner with salaray $85
def test_update_engineer_salary():
    conn = connect_to_mysql()
    if not conn:
        return "UPDATE ENGINEER SALARY TEST FAILED: Connection error"

    try:
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE employees
        SET salary = 85.00
        WHERE position = 'Engineer'
        """)
        conn.commit()

        cursor.execute("""
        SELECT COUNT(*) FROM employees
        WHERE position = 'Engineer' AND salary = 85.00
        """)
        count_correct = cursor.fetchone()[0]

        cursor.execute("""
        SELECT COUNT(*) FROM employees WHERE position = 'Engineer'
        """)
        total_engineers = cursor.fetchone()[0]

        if count_correct == total_engineers:
            return "UPDATE ENGINEER SALARY TEST ====> PASSED"
        else:
            return f"UPDATE ENGINEER SALARY TEST FAILED: {count_correct}/{total_engineers} engineers updated"

    except Error as e:
        return f"UPDATE ENGINEER SALARY TEST FAILED: {e}"

    finally:
        cursor.close()
        conn.close()

# 3.Hitung total pengeluaran salary saat tahun 2021.
def test_total_salary_2021():
    conn = connect_to_mysql()
    if not conn:
        return "TOTAL SALARY 2021 TEST FAILED: Connection error"

    try:
        cursor = conn.cursor()
        cursor.execute("""
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
        """)
        total_salary = cursor.fetchone()[0]

        expected_total_salary = 7205.00

        return "TOTAL SALARY 2021 TEST ====> PASSED" if total_salary == expected_total_salary else \
               f"TOTAL SALARY 2021 TEST FAILED: {total_salary} != {expected_total_salary}"

    except Error as e:
        return f"TOTAL SALARY 2021 TEST FAILED: {e}"

    finally:
        cursor.close()
        conn.close()

# 4. Sorting menampilkan 3 employee paling banyak yang memiliki Years of Experience
def test_top3_employees():
    conn = connect_to_mysql()
    if not conn:
        return "TOP 3 EMPLOYEES TEST FAILED: Connection error"

    try:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT name, position, years_of_experience, salary
        FROM employees
        ORDER BY years_of_experience DESC, salary DESC
        LIMIT 3;
        """)
        rows = cursor.fetchall()

        # Expected based on seed data
        expected = [
            ('Alano', 'Manager', 14, 175.00), 
            ('John', 'Assistant Manager', 12, 155.00),
            ('Jacky', 'Solution Architect', 8, 150.00)]

        return "TOP 3 EMPLOYEES TEST ====> PASSED" if rows == expected else \
               f"TOP 3 EMPLOYEES TEST FAILED: {rows} != {expected}"

    except Error as e:
        return f"TOP 3 EMPLOYEES TEST FAILED: {e}"

    finally:
        cursor.close()
        conn.close()

# 5. Tuliskan subquery untuk employee dengan posisi engginer yang memiliki exeperience kurang dari sama dengan 3 tahun
def test_engineers_experience_le3():
    conn = connect_to_mysql()
    if not conn:
        return "ENGINEERS <=3 YEARS TEST FAILED: Connection error"

    try:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT name FROM employees
        WHERE position = 'Engineer' AND years_of_experience <= 3;
        """)
        rows = cursor.fetchall()

        # Expected based on seed data
        # Example: Albert has 2.5 years
        expected = [('Aaron',), ('Albert',)]

        return "ENGINEERS <=3 YEARS TEST ====> PASSED" if rows == expected else \
               f"ENGINEERS <=3 YEARS TEST FAILED: {rows} != {expected}"

    except Error as e:
        return f"ENGINEERS <=3 YEARS TEST FAILED: {e}"

    finally:
        cursor.close()
        conn.close()

def main():
    test_results = [
        test_insert_engineer(),
        test_update_engineer_salary(),
        test_total_salary_2021(),
        test_top3_employees(),
        test_engineers_experience_le3()
    ]

    for result in test_results:
        print(result)

if __name__ == "__main__":
    main()
