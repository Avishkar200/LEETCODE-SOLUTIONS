/* Write your PL/SQL query statement below */
SELECT MAX(SALARY) AS SecondHighestSalary FROM Employee
WHERE SALARY<(
    SELECT MAX(SALARY) FROM EMPLOYEE
)
