
 SELECT FirstName, LastName, MiddleName
 FROM Person.Person
 WHERE MiddleName IS NOT NULL
 ORDER BY FirstName DESC, LastName DESC;
 