"""
CAUTION: You may get a json.decoding error.
This works for some of us but fails for others.
"""

from datetime import UTC, datetime

import requests
from rich import box
from rich import console as rich_console
from rich import table as rich_table

LIMIT = 10
TODAY = datetime.now(tz=UTC)
API_URL = (
    "https://www.forbes.com/forbesapi/person/rtb/0/position/true.json"
    "?fields=personName,gender,source,countryOfCitizenship,birthDate,finalWorth"
    f"&limit={LIMIT}"
)


def years_old(unix_timestamp: float) -> str:
    """Calculates age from given unix time format.

    Returns:
        Age as string

    >>> from datetime import datetime, UTC
    >>> 2024 - int(years_old(946684800))
    2000
    >>> 2024 - int(years_old(-2145703316))
    1902
    >>> 2024 - int(years_old(2209202284))
    2040
    """
    birth_date = datetime.fromtimestamp(unix_timestamp, tz=UTC)

    # Calculate the age
    current_date = datetime.now(tz=UTC)
    age = (
        current_date.year
        - birth_date.year
        - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    )
    return str(age)


def get_forbes_real_time_billionaires() -> list[dict[str, int | str]]:
    """
    Get the top 10 real-time billionaires using Forbes API.

    Returns:
        List of top 10 realtime billionaires data.
    """
    response_json = requests.get(API_URL).json()
    return [
        {
            "Name": person["personName"],
            "Source": person["source"],
            "Country": person["countryOfCitizenship"],
            "Gender": person["gender"],
            "Worth ($)": f"{person['finalWorth'] / 1000:.1f} Billion",
            "Age": years_old(person["birthDate"]),
        }
        for person in response_json["personList"]["personsLists"]
    ]


def display_billionaires(forbes_billionaires: list[dict[str, int | str]]) -> None:
    """
    Display Forbes real-time billionaires in a rich table.

    Args:
        forbes_billionaires (list): Forbes top 10 real-time billionaires
    """

    table = rich_table.Table(
        title=f"Forbes Top {LIMIT} Real-Time Billionaires at {TODAY:%Y-%m-%d %H:%M}",
        style="green",
        highlight=True,
        box=box.SQUARE,
    )
    for key in forbes_billionaires[0]:
        table.add_column(key)

    for billionaire in forbes_billionaires:
        table.add_row(*billionaire.values())

    rich_console.Console().print(table)


if __name__ == "__main__":
    display_billionaires(get_forbes_real_time_billionaires())
