import pyodbc

conx = pyodbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-LCQUT2B; Database=AdventureWorks; Trusted_Connection=yes;')
pyodbc.drivers()
conx_string = "driver={SQL Server}; server=DESKTOP-LCQUT2B; database=AdventureWorks; Trusted_Connection=yes;"
query = "SELECT Name, CreditRating FROM Purchasing.Vendor WHERE CreditRating < 3"
conx = pyodbc.connect(conx_string);
cursor = conx.cursor();
cursor.execute(query);
data = cursor.fetchall();
print(data[:5])
conx.close()

