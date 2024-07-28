import sqlite3
import matplotlib.pyplot as plt

# Function to make database and table
def create_database():
    conn = sqlite3.connect('population_TJ.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert data
def insert_initial_data():
    cities = [
        ("Miami", 455924),
        ("Orlando", 320742),
        ("Tampa", 403364),
        ("Jacksonville", 990931),
        ("Fort Lauderdale", 184255),
        ("St. Petersburg", 266417),
        ("Sarasota", 57602),
        ("Tallahassee", 392645),
        ("Naples", 19704),
        ("Palm Bay", 135566)
    ]

    conn = sqlite3.connect('population_TJ.db')
    c = conn.cursor()

    for city, population in cities:
        c.execute('''
            INSERT INTO population (city, year, population)
            VALUES (?, ?, ?)
        ''', (city, 2023, population))

    conn.commit()
    conn.close()


# Function to simulate growth
def simulate_population_growth():
    conn = sqlite3.connect('population_TJ.db')
    c = conn.cursor()

    growth_rate = 0.02
    c.execute('SELECT DISTINCT city FROM population')
    cities = [row[0] for row in c.fetchall()]

    for city in cities:
        c.execute('SELECT population FROM population WHERE city = ? AND year = 2023', (city,))
        initial_population = c.fetchone()[0]
        population = initial_population
        for year in range(2024, 2024 + 20):
            population = int(population * (1 + growth_rate))
            c.execute('''
                INSERT INTO population (city, year, population)
                VALUES (?, ?, ?)
            ''', (city, year, population))

    conn.commit()
    conn.close()


# Function to show growth
def visualize_population_growth(city):
    conn = sqlite3.connect('population_TJ.db')
    c = conn.cursor()
    c.execute('''
        SELECT year, population FROM population
        WHERE city = ?
    ''', (city,))
    data = c.fetchall()
    conn.close()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    plt.figure(figsize=(10, 5))
    plt.plot(years, populations, marker='o')
    plt.title(f'Population Growth for {city}')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.show()


# Main
def main():
    create_database()
    insert_initial_data()
    simulate_population_growth()

    cities = [
        "Miami", "Orlando", "Tampa", "Jacksonville", "Fort Lauderdale",
        "St. Petersburg", "Sarasota", "Tallahassee", "Naples", "Palm Bay"
    ]

    print("Available cities:")
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city}")

    choice = int(input("Choose a city by number: ")) - 1
    if 0 <= choice < len(cities):
        selected_city = cities[choice]
        visualize_population_growth(selected_city)
    else:
        print("Invalid choice. Please run the program again.")


if __name__ == "__main__":
    main()