import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://user1:1234@localhost:5432/user1')
connection = engine.connect()

sel = connection.execute("""select name, year_of_issue from album
    where year_of_issue in (2018)
    ;""").fetchall()
print(sel)

sel = connection.execute("""select name, duration from track
    order by duration desc
    ;""").fetchone()
print(sel)

sel = connection.execute("""select name from track
    where duration > 3.50
    ;""").fetchall()
print(sel)

sel = connection.execute("""select name from compilation
    where year_of_issue between 2018 and 2020
    ;""").fetchall()
print(sel)

sel = connection.execute("""select name from musician
    where length(trim(both from name))-length(replace(name,' ','')) < 1
    ;""").fetchall()
print(sel)

sel = connection.execute("""select name from track
    where name ilike '%%my%%'
    ;""").fetchall()
print(sel)

