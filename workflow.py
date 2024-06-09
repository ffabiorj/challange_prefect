import httpx
from prefect import flow, task
import random
import time

URL = "https://rickandmortyapi.com/api/"

@task(retries=2, retry_delay_seconds=1)
def get_character(name: str) -> dict:
    """Get info about a character"""
    url = f"{URL}character/?name={name}"
    # simulate a task that rondomly fails due to a timeout
    time_sleep = random.choice([1,3])
    if time_sleep > 2:
        raise Warning("Simulate task failure due to timeout")
    response = httpx.get(url)
    response.raise_for_status()
    character_info = response.json()
    return character_info


@task
def get_episodes(name: str) -> dict:
    """Get all episodies by name"""
    url = f"{URL}episode/?name={name}"
    response = httpx.get(url)
    response.raise_for_status()
    episodes_info = response.json()
    return episodes_info


@flow
def show_info(name: str) -> str:
    """show info about a character"""
    character = get_character(name)
    get_character_name = character["results"][0]["name"]
    get_first_name = get_character_name.split(" ")[0]
    episodes = get_episodes(get_first_name)
    episodes = episodes["info"]["count"]
    print(f"This character {get_character_name} has {episodes} episodes")


if __name__ == "__main__":
    show_info("rick")
