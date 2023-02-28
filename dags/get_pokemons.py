from tasks.get_pokemons_urls import get_pokemons_urls
from tasks.get_pokemons_details import get_pokemons_details

from airflow import DAG
import datetime

with DAG(
    dag_id="pokemons",
    start_date=datetime.datetime(2023, 2, 2),
    schedule_interval="@once",
    catchup=False,
) as dag:
    pokemons_url = get_pokemons_urls()
    pokemons_details = get_pokemons_details.expand(pokemon_url=pokemons_url)

    pokemons_url >> pokemons_details
