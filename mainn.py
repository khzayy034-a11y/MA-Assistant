import asyncio
from datetime import datetime

import jdatetime
import requests

from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest


api_id = 37869075
api_hash = "7925e30fa8bca59db30c0638e6dfd0a0af"


client = TelegramClient("my_session", api_id, api_hash)


def get_weather():

    try:

        url = "https://wttr.in/Hamadan?format=j1"

        data = requests.get(url, timeout=10).json()

        temp = data["current_condition"][0]["temp_C"]

        weather = data["current_condition"][0]["weatherDesc"][0]["value"]

        return temp, weather

    except:

        return "--", "Unknown"



def smart_bio():

    now = datetime.now()

    clock = now.strftime("%H:%M")

    date = jdatetime.datetime.now().strftime("%Y/%m/%d")

    temp, weather = get_weather()


    return (
        f"🕒 {clock} | 📅 {date} "
        f"📍 همدان 🌡 {temp}°C {weather}"
    )



async def auto_bio():

    await client.start()

    print("✅ Auto Bio فعال شد")


    while True:

        try:

            bio = smart_bio()


            await client(
                UpdateProfileRequest(
                    about=bio
                )
            )


            print("✅", bio)


        except Exception as e:

            print("❌", e)



        await asyncio.sleep(60)



with client:

    client.loop.run_until_complete(auto_bio())