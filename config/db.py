import sqlite3
import csv
from config.tables.players import players

DATABASE = "players.db"

def connect_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def generate_tables():
    all_tables = [players]
    db = connect_db()
    cursor = db.cursor()

    try:
        for table in all_tables:
            for query in table:
                cursor.execute(query)

        def nome_existe(nome):
            cursor.execute("SELECT 1 FROM players WHERE name = ?", (nome,))
            return cursor.fetchone() is not None

        # Ler os dados do arquivo CSV e inserir na tabela
        with open('./data/players.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not nome_existe(row['name']):
                    cursor.execute('''
                        INSERT INTO players (name, role, team, appearances, goals, assists, yellow_cards, red_cards, mvps, goals_con, ratio)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (row['name'], row['role'], row['team'], row['appearances'], row['goals'], row['assists'], row['yellow_cards'], row['red_cards'], row['mvps'], row['goals_con'], row['ratio']))

        db.commit()

    except sqlite3.Error as e:
        print(f"Erro SQLite: {e}")

    finally:
        db.close()

# Testar a geração de tabelas e inserção de dados
if __name__ == "__main__":
    generate_tables()
