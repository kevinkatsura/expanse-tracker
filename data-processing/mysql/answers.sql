-- 1. Tambahkan satu personal dalam table dengan nama employee Albert dengan posisi enginner, 
    -- join date 24 Januari 2024, dengan Year of experience 2.5 year. With salary $50.
INSERT INTO employees (name, position, join_date, years_of_experience, salary) VALUES ('Albert', 'Engineer', '2024-01-24', 2.5, 50.00);

-- 2. Update table dengan posisi enginner with salaray $85
UPDATE employees SET salary = 85.00, WHERE position = 'Engineer';

-- 3.Hitung total pengeluaran salary saat tahun 2021.
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

-- 4. Sorting menampilkan 3 employee paling banyak yang memiliki Years of Experience
SELECT name, position, years_of_experience, salary FROM employees ORDER BY years_of_experience DESC, salary DESC LIMIT 3;

-- 5. Tuliskan subquery untuk employee dengan posisi engginer yang memiliki exeperience kurang dari sama dengan 3 tahun
SELECT * FROM employees WHERE position = 'Engineer' AND years_of_experience <= 3;
