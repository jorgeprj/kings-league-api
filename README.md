<img src="./static/kings.svg" alt="Kings League Logo" width="50" height="50">

# Kings World Cup 2024 API
Welcome to the documentation for the Kings League World Cup API. This is a fan-made *Python* project with the purpose of promoting the competition. All data is sourced from the [official Kings League website](https://kingsleague.pro) via a web-scraping script.

Below are the available endpoints:

- [GET /players](#get-players): Retrieve all players.
- [GET /player/&lt;id&gt;](#get-player): Retrieve a player by ID.
- [POST /player](#create-player): Create a new player.
- [POST /player/&lt;id&gt;](#update-player): Update a player by ID.
- [DELETE /player/&lt;id&gt;](#delete-player): Delete a player by ID.

## Endpoints

### GET /players
Retrieve all players.

#### Request
```plaintext
GET /players
```

#### Response
```json
{
    "players": [
        {
            "id": 1,
            "name": "Player Name",
            "role": "Player Role",
            "team": "Player Team",
            "appearances": 10,
            "goals": 5,
            "yellow_cards": 2,
            "red_cards": 0,
            "mvps": 1,
            "goals_conceded": 10,
            "ratio": 0.5
        },
        {
            "id": 2,
            "name": "Another Player",
            "role": "Forward",
            "team": "Team B",
            "appearances": 15,
            "goals": 12,
            "yellow_cards": 1,
            "red_cards": 0,
            "mvps": 3,
            "goals_conceded": 20,
            "ratio": 0.6
        }
    ]
}
```

#### Example Usage
```
curl -X GET https://api.example.com/players
```
**Note:** Only goalkeepers have ratio and goals_conceded attributes.

### GET /player/<id>
Retrieve a player by ID.

#### Request
```plaintext
GET /player/1
```

#### Response
```json
{
    "players": [
        {
            "id": 1,
            "name": "Player Name",
            "role": "Player Role",
            "team": "Player Team",
            "appearances": 10,
            "goals": 5,
            "yellow_cards": 2,
            "red_cards": 0,
            "mvps": 1,
            "goals_conceded": 10,
            "ratio": 0.5
        }
    ]
}
```

#### Example Usage
```
curl -X GET https://api.example.com/player/&lt;id&gt;
```

### POST /player
Create a new player.

#### Request Body
```json
{
    "name": "New Player",
    "role": "Midfielder",
    "team": "Team A",
    "appearances": 5,
    "goals": 2,
    "yellow_cards": 1,
    "red_cards": 0,
    "mvps": 0,
    "goals_conceded": 0,
    "ratio": 0.4
}
```

#### Response
```json
{
    "message": "Player created successfully",
    "player": {
        "id": 3,
        "name": "New Player",
        "role": "Midfielder",
        "team": "Team A",
        "appearances": 5,
        "goals": 2,
        "yellow_cards": 1,
        "red_cards": 0,
        "mvps": 0,
        "goals_conceded": 0,
        "ratio": 0.4
    }
}
```

#### Example Usage
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "New Player", "role": "Midfielder", "team": "Team A", "appearances": 5, "goals": 2, "yellow_cards": 1, "red_cards": 0, "mvps": 0, "goals_conceded": 0, "ratio": 0.4}' https://api.example.com/player

```

### POST /player/<id>
Update a player by ID.

#### Request Body
```json
{
    "name": "Updated Player Name",
    "role": "Forward",
    "team": "Team B",
    "appearances": 20,
    "goals": 15,
    "yellow_cards": 2,
    "red_cards": 0,
    "mvps": 3,
    "goals_conceded": 10,
    "ratio": 0.75
}
```

#### Response
```json
{
    "message": "Player updated successfully",
    "player": {
        "id": 1,
        "name": "Updated Player Name",
        "role": "Forward",
        "team": "Team B",
        "appearances": 20,
        "goals": 15,
        "yellow_cards": 2,
        "red_cards": 0,
        "mvps": 3,
        "goals_conceded": 10,
        "ratio": 0.75
    }
}
```

#### Example Usage
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Updated Player Name", "role": "Forward", "team": "Team B", "appearances": 20, "goals": 15, "yellow_cards": 2, "red_cards": 0, "mvps": 3, "goals_conceded": 10, "ratio": 0.75}' https://api.example.com/player/1

```

### DELETE /player/<id>
Delete a player by ID.

#### Request
```plaintext
DELETE /player/1
```

#### Response
```json
{
    "message": "Player deleted successfully",
    "deleted_player": {
        "id": 1,
        "name": "Updated Player Name",
        "role": "Forward",
        "team": "Team B",
        "appearances": 20,
        "goals": 15,
        "yellow_cards": 2,
        "red_cards": 0,
        "mvps": 3,
        "goals_conceded": 10,
        "ratio": 0.75
    }
}
```

#### Example Usage
```bash
curl -X DELETE https://api.example.com/player/1
```

## License

© 2024 Kings League. All rights reserved.
- Official Website: [https://kingsleague.pro](https://kingsleague.pro)