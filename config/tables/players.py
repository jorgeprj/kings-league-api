players = [
        """CREATE TABLE IF NOT EXISTS PLAYERS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            role TEXT NOT NULL,
            team TEXT NOT NULL,
            appearances INTEGER NULL,
            goals INTEGER NOT NULL,
            assists INTEGER NULL,
            yellow_cards INTEGER NULL,
            red_cards INTEGER NULL,
            mvps INTEGER NULL,
            goals_con INTEGER NULL,
            ratio INTEGER NULL
        )"""
]