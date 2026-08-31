/* Write your PL/SQL query statement below 
SELECT FIRSTNAME,LASTNAME,CITY,state
from person
INNER JOIN ADDRESS ON PERSON.PERSONID=ADDRESS.PERSONID*/
SELECT p.FirstName,
       p.LastName,
       a.City,
       a.State
FROM Person p
LEFT JOIN Address a
ON p.PersonId = a.PersonId;