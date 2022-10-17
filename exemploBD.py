import sqlite3 as dbapi

print(dbapi.apilevel)
print(dbapi.threadsafety)
print(dbapi.paramstyle)
try:
    bbdd = dbapi.connect('bbdd.dat')
except(dbapi.DatabaseError):
    print("Erro na BD")
else:
    print("Conectado á BD")
    print(bbdd)

try:
    c = bbdd.cursor()

    c.execute('''create table usuarios (dni text''')

except dbapi.DatabaseError as e:
    print("Erro na BD")