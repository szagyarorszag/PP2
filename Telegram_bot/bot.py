import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import openai

import requests 
from pprint import pprint
city ='Almaty'
open_weather_token ='<Your Open-Weather API'
def get_weather(city, open_weather_token):
    try: 
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
        data = r.json() 

        city = data["name"]
        current_temp = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        max_temp = data["main"]["temp_max"]
        min_temp = data["main"]["temp_min"]
        wind = data["wind"]["speed"]
        weather_data = ( f'Weather in {city}:\n' 
            f'Current temperature feels like: {current_temp}°C\n'
            f'Humidity: {humidity}%\n'
            f'Pressure: {pressure}hPa\n'
            f'Highest temperature: {max_temp}°C\n'
            f'Lowest temperature: {min_temp}°C\n' 
            f'Speed of the wind: {wind}m/s')
        print(weather_data)
        return weather_data

    except Exception as ex:
        print(ex)
def main(): 
    get_weather(city, open_weather_token)


logging.basicConfig(level=logging.INFO)

openai.api_key = "Your Openai API"
bot = Bot(token="Your Tg bot Api")

dp = Dispatcher(bot)
if not os.path.exists("users"):
    os.mkdir("users")

@dp.message_handler(content_types=types.ContentType.TEXT)

async def process_message(message: types.Message):

    if f"{message.chat.id}.txt" not in os.listdir("users"):

        with open(f"users/{message.chat.id}.txt", "x") as f:
            f.write("")

    with open(f"users/{message.chat.id}.txt", "r", encoding="utf-8") as file:
        oldmes = file.read()

    if message.text == "/clear":

        with open(f"users/{message.chat.id}.txt", "w", encoding="utf-8") as file:
            file.write("")

        return await bot.send_message(chat_id=message.chat.id, text="История очищена!")
    
    try:
        if "/" not in message.text:
            send_message = await bot.send_message(chat_id=message.chat.id, text="Please wait;)")
            completion = openai.Completion.create(
                model="text-davinci-003",
            prompt=message.text,
            temperature=0.9,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["You:"]
            )
            await bot.edit_message_text(
                text=completion.choices[0].text,
                chat_id=message.chat.id,
                message_id=send_message.message_id,
            )

            with open(f"users/{message.chat.id}.txt", "a+", encoding="utf-8") as file:
                file.write(
                    message.text.replace("\n", " ")
                    + "\n"
                    + completion.choices[0].text.replace("\n", " ")
                    + "\n"
                    )
                
            with open(f"users/{message.chat.id}.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
        elif message.text == "/clear":

            with open(f"users/{message.chat.id}.txt", "w", encoding="utf-8") as file:
                file.write("")

            return await bot.send_message(chat_id=message.chat.id, text="История очищена!")
        elif message.text == "/reliable_clothes":  
            send_message = await bot.send_message(chat_id=message.chat.id, text="Please wait;)")
            completion = openai.Completion.create(
                model="text-davinci-003",
            prompt=f"what kind of clothes should i wear according to this data ?: {get_weather(city,open_weather_token)}",
            temperature=0.9,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["You:"]
            )
            await bot.edit_message_text(
                text=completion.choices[0].text,
                chat_id=message.chat.id,
                message_id=send_message.message_id,
            )

            with open(f"users/{message.chat.id}.txt", "a+", encoding="utf-8") as file:
                file.write(
                    message.text.replace("\n", " ")
                    + "\n"
                    + completion.choices[0].text.replace("\n", " ")
                    + "\n"
                    )
                
            with open(f"users/{message.chat.id}.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()

    except Exception as e:
        await bot.send_message(chat_id=message.chat.id, text=str(e))

if __name__ == "__main__":
    main()
    executor.start_polling(dp, skip_updates=True)