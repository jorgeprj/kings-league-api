players = [
        """CREATE TABLE IF NOT EXISTS PLAYERS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL,
            goals INTEGER NOT NULL,
            team TEXT NOT NULL UNIQUE
        )"""
]