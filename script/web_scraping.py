import requests
from bs4 import BeautifulSoup
import pandas as pd

# Inicializando o DataFrame geral
df_geral = pd.DataFrame()

for page in range(1, 11):
    url = f'https://kingsleague.pro/en/world-cup/11-12-13-players?page={page}'
    req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    pagina = req.text
    soup = BeautifulSoup(pagina, 'html.parser')

    players_name = []
    players_role = []
    players_team = []
    players_appearances = []
    players_goals = []
    players_assists = []
    players_yellow_cards = []
    players_red_cards = []
    players_mvps = []
    players_goals_con = []
    players_ratio = []

    for line in soup.findAll(class_='player-card-content'):
        name = line.find('h5', attrs={'class': 'player-name'}).text.strip()
        players_name.append(name)

        role = line.find('p', attrs={'class': 'player-role'}).text.strip()
        players_role.append(role)

        team = line.find('img', class_='team-logo-container')
        if team and 'alt' in team.attrs:
            team_name = team['alt']
            players_team.append(team_name)


        stat_containers = line.findAll('div', class_='stats-data-container')
        appearances = None
        for container in stat_containers:
            description = container.find('p', class_='stat-description').text.strip()
            if description == 'Appearances':
                appearances = container.find('p', class_='stat-value').text.strip()
                break
        players_appearances.append(appearances)

        goals = None
        for container in stat_containers:
            description = container.find('p', class_='stat-description').text.strip()
            if description == 'Goals':
                goals = container.find('p', class_='stat-value').text.strip()
                break
        players_goals.append(goals)

        assists = None
        for container in stat_containers:
            description = container.find('p', class_='stat-description').text.strip()
            if description == 'Assists':
                assists = container.find('p', class_='stat-value').text.strip()
                break
        players_assists.append(assists)

        yellow = None
        for container in stat_containers:
            description = container.find('p', class_='stat-description').text.strip()
            if description == 'Yellow cards':
                yellow = container.find('p', class_='stat-value').text.strip()
                break
        players_yellow_cards.append(yellow)

        red = None
        for container in stat_containers:
            description = container.find('p', class_='stat-description').text.strip()
            if description == 'Red cards':
                red = container.find('p', class_='stat-value').text.strip()
                break
        players_red_cards.append(red)

        goals_con = None
        for container in stat_containers:
            description = container.find('p', class_='stat-description').text.strip()
            if description == 'Goals con.':
                goals_con = container.find('p', class_='stat-value').text.strip()
                break
        players_goals_con.append(goals_con)

        ratio = None
        for container in stat_containers:
            description = container.find('p', class_='stat-description').text.strip()
            if description == 'Ratio':
                ratio = container.find('p', class_='stat-value').text.strip()
                break
        players_ratio.append(ratio)

        mvp_container = line.find('div', class_='stats-data-container-mvp')
        if mvp_container:
            mvp_value = mvp_container.find('span', class_='font-bold').text.strip()
            players_mvps.append(mvp_value)
        else:
            players_mvps.append(0)

    # Selecionar apenas o primeiro valor de cada array se for a página 10
    if page == 10:
        players_name = players_name[:1]
        players_role = players_role[:1]
        players_team = players_team[:1]
        players_appearances = players_appearances[:1]
        players_goals = players_goals[:1]
        players_assists = players_assists[:1]
        players_yellow_cards = players_yellow_cards[:1]
        players_red_cards = players_red_cards[:1]
        players_mvps = players_mvps[:1]
        players_goals_con = players_goals_con[:1]
        players_ratio = players_ratio[:1]


    # Criar DataFrame temporário
    df_temp = pd.DataFrame({'name': players_name,
                            'role': players_role,
                            'team': players_team,
                            'appearances': players_appearances,
                            'goals': players_goals,
                            'assists': players_assists,
                            'yellow_cards': players_yellow_cards,
                            'red_cards': players_red_cards,
                            'mvps': players_mvps,
                            'goals_con': players_goals_con,
                            'ratio': players_ratio
                           })

    # Concatenar com o DataFrame geral
    df_geral = pd.concat([df_geral, df_temp], ignore_index=True)
    df_geral.fillna(0, inplace=True)


def get_stat_value(containers, description):
    for container in containers:
        if container.find('p', class_='stat-description').text.strip() == description:
            return container.find('p', class_='stat-value').text.strip()
    return None

def scrape_page(page_number):
    url = f'https://kingsleague.pro/en/world-cup/draft-players?page={page_number}'
    req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(req.text, 'html.parser')
    
    players_data = []
    
    for line in soup.findAll(class_='player-card-content'):
        name = line.find('h2', attrs={'class': 'player-name'}).text.strip()
        
        role = line.find('p', attrs={'class': 'player-role'}).text.strip()
        
        team_img = line.find('img', class_='team-logo-container')
        team = team_img['alt'].strip() if team_img and 'alt' in team_img.attrs else None

        stat_containers = line.findAll('div', class_='stats-data-container')
        appearances = get_stat_value(stat_containers, 'Appearances')
        goals = get_stat_value(stat_containers, 'Goals')
        assists = get_stat_value(stat_containers, 'Assists')
        yellow_cards = get_stat_value(stat_containers, 'Yellow cards')
        red_cards = get_stat_value(stat_containers, 'Red cards')
        goals_con = get_stat_value(stat_containers, 'Goals con.')
        ratio = get_stat_value(stat_containers, 'Ratio')
        
        mvp_container = line.find('div', class_='stats-data-container-mvp')
        mvps = mvp_container.find('span', class_='font-bold').text.strip() if mvp_container else '0'
        
        players_data.append({
            'name': name,
            'role': role,
            'team': team,
            'appearances': appearances,
            'goals': goals,
            'assists': assists,
            'yellow_cards': yellow_cards,
            'red_cards': red_cards,
            'mvps': mvps,
            'goals_con': goals_con,
            'ratio': ratio
        })
    
    return players_data

# Inicializando o DataFrame geral
df_draft = pd.DataFrame()

for page in range (1, 38):
  players_data = scrape_page(page)
  df_temp2 = pd.DataFrame(players_data)
  df_draft = pd.concat([df_draft, df_temp2], ignore_index=True)

df_draft.fillna(0, inplace=True)

df_players = pd.concat([df_geral, df_draft], ignore_index=True)

df_players.to_csv('players.csv', index=False)