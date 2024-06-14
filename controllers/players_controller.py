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
    
    def get_player_by_id(self, id):
        db = connect_db()
        cursor = db.cursor()
        sql = "SELECT * FROM PLAYERS WHERE id = ?"
        cursor.execute(sql, [id])
        
        colunas = [desc[0] for desc in cursor.description]
        player = [dict(zip(colunas, row)) for row in cursor.fetchall()]
        return player
    
    def create_player(name, role, team, appearances, goals, yellow_cards, red_cards, mvps, goals_con, ratio):
        db = connect_db()
        cursor = db.cursor()
        sql = "INSERT INTO PLAYERS(name, role, team, appearances, goals, yellow_cards, red_cards, mvps, goals_con, ratio) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, [name, role, team, appearances, goals, yellow_cards, red_cards, mvps, goals_con, ratio])
        player_id = cursor.lastrowid  # Recupera o ID gerado para o novo jogador
        db.commit()
        db.close()
        
        return {
            "message": "Player created successfully",
            "player": {
                "id": player_id,
                "name": name,
                "role": role,
                "team": team,
                "appearances": appearances,
                "goals": goals,
                "yellow_cards": yellow_cards,
                "red_cards": red_cards,
                "mvps": mvps,
                "goals_conceded": goals_con,
                "ratio": ratio
            }
        }
    
    def update_player(id, name, role, team, appearances, goals, yellow_cards, red_cards, mvps, goals_con, ratio):
        db = connect_db()
        cursor = db.cursor()
        sql = "UPDATE PLAYERS SET name = ?, role = ?, team = ?, appearances = ?, goals = ?, yellow_cards = ?, red_cards = ? , mvps = ?, goals_con = ?, ratio = ?  WHERE id = ?"
        cursor.execute(sql, [name, role, team, appearances, goals, yellow_cards, red_cards, mvps, goals_con, ratio, id])
        db.commit()
        db.close()
        return {
            "message": "Player updated successfully",
            "player": {
                "id": id,
                "name": name,
                "role": role,
                "team": team,
                "appearances": appearances,
                "goals": goals,
                "yellow_cards": yellow_cards,
                "red_cards": red_cards,
                "mvps": mvps,
                "goals_conceded": goals_con,
                "ratio": ratio
            }
        }
    
    def delete_player(id):
        db = connect_db()
        cursor = db.cursor()
        player = players().get_player_by_id(id)  # Instanciando a classe para usar o método get_player_by_id
        
        sql = "DELETE FROM PLAYERS WHERE id = ?"
        cursor.execute(sql, [id])
        db.commit()
        db.close()
        
        if player:
            return {
                "message": f"Player id: {id} deleted successfully",
                "deleted_player": {
                    "id": player[0]['id'],
                    "name": player[0]['name'],
                    "role": player[0]['role'],
                    "team": player[0]['team'],
                    "appearances": player[0]['appearances'],
                    "goals": player[0]['goals'],
                    "yellow_cards": player[0]['yellow_cards'],
                    "red_cards": player[0]['red_cards'],
                    "mvps": player[0]['mvps'],
                    "goals_conceded": player[0]['goals_con'],
                    "ratio": player[0]['ratio']
                }
            }
        else:
            return {
                "message": f"Player id: {id} not found or already deleted",
                "deleted_player": None
            }