import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/tipsters/api/sportscore1'

mcp = FastMCP('sportscore1')

@mcp.tool()
def teams_by_sport_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of teams belonging to a specified sport. Returns a list of teams'''
    url = 'https://sportscore1.p.rapidapi.com/sports/1/teams'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def events_by_sport_id_and_date(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of events belonging to a specified sport and date. Returns a list of events. Use `Meta/List of event status` to translate'''
    url = 'https://sportscore1.p.rapidapi.com/sports/1/events/date/2020-06-07'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def managers_by_sport_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of managers belonging to a specified sport. Returns a list of managers'''
    url = 'https://sportscore1.p.rapidapi.com/sports/1/managers'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def sport_data(id: Annotated[Union[int, float], Field(description='Sport ID Default: 1')]) -> dict: 
    '''Returns sport data'''
    url = 'https://sportscore1.p.rapidapi.com/sports/1'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def sport_list() -> dict: 
    '''Returns a list of sports. This is the main way to get the IDs of the available sports for future inquiries.'''
    url = 'https://sportscore1.p.rapidapi.com/sports'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def sections_by_sport_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of sections belonging to a specified sport. Returns a list of sections'''
    url = 'https://sportscore1.p.rapidapi.com/sports/1/sections'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def leagues_by_sport_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of leagues belonging to a specified sport. Returns a list of leagues'''
    url = 'https://sportscore1.p.rapidapi.com/sports/1/leagues'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def challenges_by_sport_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of challenges belonging to a specified sport. Returns a list of challenges'''
    url = 'https://sportscore1.p.rapidapi.com/sports/1/challenges'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def players_by_sport_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of players belonging to a specified sport. Returns a list of players'''
    url = 'https://sportscore1.p.rapidapi.com/sports/1/players'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def events_live_by_sport_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a live list of events belonging to a specified sport. Returns a list of live events'''
    url = 'https://sportscore1.p.rapidapi.com/sports/1/events/live'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def events_by_sport_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of events belonging to a specified sport. Returns a list of events'''
    url = 'https://sportscore1.p.rapidapi.com/sports/1/events'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def seasons_by_sport_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of seasons belonging to a specified sport. Returns a list of seasons'''
    url = 'https://sportscore1.p.rapidapi.com/sports/1/seasons'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def events_by_section_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of events belonging to a specified section. Returns a list of events'''
    url = 'https://sportscore1.p.rapidapi.com/sections/1/events'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def challenges_by_section_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of challenges belonging to a specified section. Returns a list of challenges'''
    url = 'https://sportscore1.p.rapidapi.com/sections/1/challenges'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def section_list(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Returns a list of section'''
    url = 'https://sportscore1.p.rapidapi.com/sections'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_sections(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get a list of sections by filter. Returns a list of sections'''
    url = 'https://sportscore1.p.rapidapi.com/sections/search'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def leagues_by_section_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of leagues belonging to a specified section. Returns a list of leagues'''
    url = 'https://sportscore1.p.rapidapi.com/sections/1/leagues'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def section_data(id: Annotated[Union[int, float], Field(description='Section ID Default: 1')]) -> dict: 
    '''Returns section data'''
    url = 'https://sportscore1.p.rapidapi.com/sections/1'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_data(id: Annotated[Union[int, float], Field(description='League ID Default: 1')]) -> dict: 
    '''Returns league data'''
    url = 'https://sportscore1.p.rapidapi.com/leagues/1'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def events_by_league_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of events belonging to a specified league. Returns a list of events'''
    url = 'https://sportscore1.p.rapidapi.com/leagues/1/events'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def league_list(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Returns a list of league'''
    url = 'https://sportscore1.p.rapidapi.com/leagues'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def challenges_by_league_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of challenges belonging to a specified league. Returns a list of challenges'''
    url = 'https://sportscore1.p.rapidapi.com/leagues/1/challenges'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_leagues(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get a list of leagues by filter. Returns a list of leagues'''
    url = 'https://sportscore1.p.rapidapi.com/leagues/search'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def seasons_by_league_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of seasons belonging to a specified league. Returns a list of seasons'''
    url = 'https://sportscore1.p.rapidapi.com/leagues/1/seasons'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def challenges_list(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Returns a list of challenges'''
    url = 'https://sportscore1.p.rapidapi.com/challenges'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def challenges_data(id: Annotated[Union[int, float], Field(description='Challenge ID Default: 1')]) -> dict: 
    '''Returns challenge data'''
    url = 'https://sportscore1.p.rapidapi.com/challenges/1'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def season_data(id: Annotated[Union[int, float], Field(description='Season ID Default: 1')]) -> dict: 
    '''Returns season data'''
    url = 'https://sportscore1.p.rapidapi.com/seasons/1'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def standings_tables_by_season_id(id: Annotated[Union[int, float], Field(description='Season ID Default: 1')]) -> dict: 
    '''Get a list of standing-tables belonging to a specified season. Returns a list of standing-tables'''
    url = 'https://sportscore1.p.rapidapi.com/seasons/1/standings-tables'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def season_list(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Returns a list of seasons'''
    url = 'https://sportscore1.p.rapidapi.com/seasons'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def events_by_season_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of events belonging to a specified season. Returns a list of events'''
    url = 'https://sportscore1.p.rapidapi.com/seasons/1/events'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def сup_trees_by_season_id(id: Annotated[Union[int, float], Field(description='Season ID Default: 1')]) -> dict: 
    '''Get a list of cup-trees belonging to a specified season. Returns a list of cup-trees'''
    url = 'https://sportscore1.p.rapidapi.com/seasons/1/cup-trees'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams_by_season_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of teams belonging to a specified season. Returns a list of teams'''
    url = 'https://sportscore1.p.rapidapi.com/seasons/1/teams'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_seasons(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get a list of seasons by filter. Returns a list of seasons'''
    url = 'https://sportscore1.p.rapidapi.com/seasons/search'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def lineups_by_team_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of lineups belonging to a specified team. Returns a list of lineup'''
    url = 'https://sportscore1.p.rapidapi.com/teams/1/lineups'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def team_list(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Returns a list of team'''
    url = 'https://sportscore1.p.rapidapi.com/teams'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def players_by_team_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of players belonging to a specified team. Returns a list of players'''
    url = 'https://sportscore1.p.rapidapi.com/teams/1/players'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_teams(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get a list of teams by a filter data. Returns a list of teams'''
    url = 'https://sportscore1.p.rapidapi.com/teams/search'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def h2_hevents_by_team_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of events belonging to a specified team. Returns a list of events'''
    url = 'https://sportscore1.p.rapidapi.com/teams/1/h2h-events/1'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def sub_teams_by_team_id(id: Annotated[Union[int, float], Field(description='Team ID Default: 25502')]) -> dict: 
    '''Returns a list of sub-teams'''
    url = 'https://sportscore1.p.rapidapi.com/teams/25502/sub-teams'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def team_data(id: Annotated[Union[int, float], Field(description='Team ID Default: 1')]) -> dict: 
    '''Returns team data'''
    url = 'https://sportscore1.p.rapidapi.com/teams/1'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def seasons_by_team_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of seasons belonging to a specified team. Returns a list of seasons'''
    url = 'https://sportscore1.p.rapidapi.com/teams/1/seasons'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def metrika_by_team_id(id: Annotated[Union[int, float], Field(description='Team ID Default: 1')]) -> dict: 
    '''Get team metrika and statistics. Returns metrika data.'''
    url = 'https://sportscore1.p.rapidapi.com/teams/1/metrika'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def events_by_team_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of events belonging to a specified team. Returns a list of events'''
    url = 'https://sportscore1.p.rapidapi.com/teams/1/events'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_events(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get a list of events by filter. Simple pagination is used'''
    url = 'https://sportscore1.p.rapidapi.com/events/search'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def lineups_by_event_id(id: Annotated[Union[int, float], Field(description='Event ID Default: 561559')]) -> dict: 
    '''Get a list of lineups belonging to a specified event. Returns a list of lineups. Use `Meta/Player positions list` to translate'''
    url = 'https://sportscore1.p.rapidapi.com/events/561559/lineups'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def medias_by_event_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of media belonging to a specified event. Returns a list of media.'''
    url = 'https://sportscore1.p.rapidapi.com/events/230732/medias'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def event_list(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Returns a list of events. Simple pagination is used'''
    url = 'https://sportscore1.p.rapidapi.com/events'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def series_by_event_id(id: Annotated[Union[int, float], Field(description='Event ID Default: 371908')]) -> dict: 
    '''Get a list of series belonging to a specified event. Returns a list of series.'''
    url = 'https://sportscore1.p.rapidapi.com/events/371908/series'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def event_data(id: Annotated[Union[int, float], Field(description='Event ID Default: 1')]) -> dict: 
    '''Returns event data by event ID'''
    url = 'https://sportscore1.p.rapidapi.com/events/1'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def event_live_list(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of live events. Returns list of events'''
    url = 'https://sportscore1.p.rapidapi.com/events/live'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def markets_by_event_id(id: Annotated[Union[int, float], Field(description='Event ID Default: 54225')]) -> dict: 
    '''Returns a list of markets belonging to a specified event'''
    url = 'https://sportscore1.p.rapidapi.com/events/54225/markets'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tennis_points_by_event_id(id: Annotated[Union[int, float], Field(description='Event ID Default: 546599')]) -> dict: 
    '''Sports: tennis. Get a list of points by points belonging to a specified event. Returns a list of points.'''
    url = 'https://sportscore1.p.rapidapi.com/events/546599/points'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def statistics_by_event_id(id: Annotated[Union[int, float], Field(description='Event ID Default: 132371')]) -> dict: 
    '''Get a list of statistics belonging to a specified event. Returns a list of statistics.'''
    url = 'https://sportscore1.p.rapidapi.com/events/132371/statistics'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_events_by_similar_name(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get a list of eventsby similar name. Calculates the degree of similarity of two strings using the algorithm described in Programming Classics.'''
    url = 'https://sportscore1.p.rapidapi.com/events/search-similar-name'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def event_list_by_date(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Returns a list of events by date. Use your own filters to filter the resulting list more accurately.'''
    url = 'https://sportscore1.p.rapidapi.com/events/date/2020-05-23'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def incidents_by_event_id(id: Annotated[Union[int, float], Field(description='Event ID Default: 132371')]) -> dict: 
    '''Get a list of incidents belonging to a specified event. Sort in order. Returns a list of incidents.'''
    url = 'https://sportscore1.p.rapidapi.com/events/132371/incidents'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def medias_by_player_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of media belonging to a specified player'''
    url = 'https://sportscore1.p.rapidapi.com/players/1/medias'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def transfers_by_player_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of transfer histories belonging to a specified player. Returns a list of transfer histories'''
    url = 'https://sportscore1.p.rapidapi.com/players/1/transfers'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def player_list(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Returns a list of players'''
    url = 'https://sportscore1.p.rapidapi.com/players'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def statistics_by_player_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get player statistics list by player ID. Season statistics. Returns a list of statistics'''
    url = 'https://sportscore1.p.rapidapi.com/players/1/statistics'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams_by_player_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of teams belonging to a specified player. Returns a list of teams'''
    url = 'https://sportscore1.p.rapidapi.com/players/1/teams'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def player_data(id: Annotated[Union[int, float], Field(description='Player ID Default: 1')]) -> dict: 
    '''Get player data by player ID. Returns player data'''
    url = 'https://sportscore1.p.rapidapi.com/players/1'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_players(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get a list of players by filter. Returns a list of players.'''
    url = 'https://sportscore1.p.rapidapi.com/players/search'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def lineup_to_player_by_player_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of lineup-to-players belonging to a specified player'''
    url = 'https://sportscore1.p.rapidapi.com/players/1/lineup-to-players'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def seasons_by_player_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of seasons belonging to a specified player. Returns a list of seasons'''
    url = 'https://sportscore1.p.rapidapi.com/players/1/seasons'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def referee_list(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Returns a list of referees'''
    url = 'https://sportscore1.p.rapidapi.com/referees'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_referees(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get a list of referees by filter. Returns a list of referees'''
    url = 'https://sportscore1.p.rapidapi.com/referees/search'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def referee_data(id: Annotated[Union[int, float], Field(description='Referee ID Default: 1')]) -> dict: 
    '''Returns referee data'''
    url = 'https://sportscore1.p.rapidapi.com/referees/1'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def events_by_referee_id(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Get a list of events belonging to a specified referee. Returns a list of events'''
    url = 'https://sportscore1.p.rapidapi.com/referees/1/events'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def manager_data(id: Annotated[Union[int, float], Field(description='Manager ID Default: 1')]) -> dict: 
    '''Returns manager data'''
    url = 'https://sportscore1.p.rapidapi.com/managers/1'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def manager_transfers(id: Annotated[Union[int, float], Field(description='Manager ID Default: 1')]) -> dict: 
    '''Returns a manager transfers'''
    url = 'https://sportscore1.p.rapidapi.com/managers/1/transfers'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def manager_list(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Returns a list of managers'''
    url = 'https://sportscore1.p.rapidapi.com/managers'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_managers(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get a list of managers by filter. Returns a list of manager.'''
    url = 'https://sportscore1.p.rapidapi.com/managers/search'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def media_list(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Returns a list of medias. Simple pagination is used'''
    url = 'https://sportscore1.p.rapidapi.com/medias'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def media_data(id: Annotated[Union[int, float], Field(description='Media ID Default: 1')]) -> dict: 
    '''Returns media data'''
    url = 'https://sportscore1.p.rapidapi.com/medias/1'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tennis_rankings_wta_list(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Returns a list of tennis rankings WTA'''
    url = 'https://sportscore1.p.rapidapi.com/tennis-rankings/wta'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tennis_rankings_atp_list(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Returns a list of tennis rankings ATP'''
    url = 'https://sportscore1.p.rapidapi.com/tennis-rankings/atp'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_of_common_translations() -> dict: 
    '''Returns a list of translation'''
    url = 'https://sportscore1.p.rapidapi.com/meta/line'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_of_event_status() -> dict: 
    '''Returns events status'''
    url = 'https://sportscore1.p.rapidapi.com/meta/event-status'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def player_positions_list() -> dict: 
    '''Returns a list of player positions'''
    url = 'https://sportscore1.p.rapidapi.com/meta/player-positions'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def venues_list(page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''Returns a list of venues'''
    url = 'https://sportscore1.p.rapidapi.com/venues'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def venue_data(id: Annotated[Union[int, float], Field(description='Challenge ID Default: 1')]) -> dict: 
    '''Returns venue data'''
    url = 'https://sportscore1.p.rapidapi.com/venues/1'
    headers = {'x-rapidapi-host': 'sportscore1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
