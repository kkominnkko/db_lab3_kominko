import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = 'Minnkko1'
database = 'dota'
host = 'localhost'
port = '5432'

query_1 = '''
CREATE VIEW HeroOfEachCategory AS 
SELECT category.hero_category, COUNT(heroes.category_id) FROM heroes
JOIN category ON category.category_id = heroes.category_id GROUP BY hero_category
'''

query_2 = '''
CREATE VIEW HeroOfEachRole AS 
SELECT roles.hero_role, COUNT(heroes.role_id) FROM heroes
JOIN roles ON roles.role_id = heroes.role_id GROUP BY hero_role
'''

query_3 = '''
CREATE VIEW StrengthHeroIntelligence AS 
SELECT hero_name, hero_intelligence FROM heroes
WHERE category_id = 1 ORDER BY hero_intelligence DESC
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
x = []
y = []


with conn:
    print("Database opened successfully")
    cur = conn.cursor()

    cur.execute('DROP VIEW if exists HeroOfEachCategory')
    cur.execute(query_1)
    cur.execute('SELECT * FROM HeroOfEachCategory')
    for row in cur:
        x.append(row[0])
        y.append(row[1])
    plt.bar(x, y, width=0.5, alpha=0.6, color='blue')
    plt.ylabel('Максимальна кількість персонажів в категорії')
    plt.title('Кількість персонажів кожної категорії')
    plt.show()

    x.clear()
    y.clear()

    cur.execute('DROP VIEW if exists HeroOfEachRole')

    cur.execute(query_2)
    cur.execute('SELECT * FROM HeroOfEachRole')
    for row in cur:
        x.append(row[0])
        y.append(row[1])
    plt.pie(y, labels=x, shadow=True, autopct='%1.1f%%', startangle=180)
    plt.title('Кількість персонажів кожної ролі (у відсотках)')
    plt.show()

    x.clear()
    y.clear()
    cur.execute('DROP VIEW if exists StrengthHeroIntelligence')

    cur.execute(query_3)
    cur.execute('SELECT * FROM StrengthHeroIntelligence')
    for row in cur:
        y.append(row[1])
        x.append(row[0])
    plt.plot(x, y, 'go-')
    plt.ylabel('Показники інтелекту')
    plt.title('Сильні персонажі')
    for x, y in zip(x, y):
        plt.annotate(y, xy=(x, y), xytext=(7, 2), textcoords='offset points')
    plt.show()