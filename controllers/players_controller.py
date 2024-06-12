from config.db import connect_db

class players:
    def get_players():
        db = connect_db()
        cursor = db.cursor()
        sql = "SELECT * FROM PLAYERS"
        cursor.execute(sql)
        
        colunas = [desc[0] for desc in cursor.description]
        result = [dict(zip(colunas, row)) for row in cursor.fetchall()]
        return result
    
    def get_player_by_id(id):
        db = connect_db()
        cursor = db.cursor()
        sql = "SELECT * FROM PLAYERS WHERE id = ?"
        cursor.execute(sql, [id])
        
        colunas = [desc[0] for desc in cursor.description]
        player = [dict(zip(colunas, row)) for row in cursor.fetchall()]
        return player
    
    def create_player(name, age, goals, team):
        db = connect_db()
        cursor = db.cursor()
        sql = "INSERT INTO PLAYERS(name, age, goals, team) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, [name, age, goals, team])
        db.commit()
        return "New player registered successfully"
    
    def update_player(id, name, age, goals, team):
        db = connect_db()
        cursor = db.cursor()
        sql = "UPDATE PLAYERS SET name = ?, age = ?, goals = ?, team = ? WHERE id = ?"
        cursor.execute(sql, [name, age, goals, team])
        db.commit()
        return "Player " + name + " was successfully updated"
    
    def delete_player(id):
        db = connect_db()
        cursor = db.cursor()
        sql = "DELETE FROM PLAYERS WHERE id = ?"
        cursor.execute(sql, [id])
        db.commit()
        return "Player id: " + id + " deleted successfully"