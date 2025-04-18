import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

# Function to get weather
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    api_key = 'ce86bdbfd1445eac2788f22acb7bf60b'  # Replace with your OpenWeatherMap API key
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'

    # Get current weather
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        rain = data.get('rain', {}).get('1h', 0)  # Rain data for the last hour (if available)
        sys = data['sys']

        # Extract data
        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description']
        wind_speed = wind['speed']
        wind_deg = wind['deg']
        sunrise = datetime.utcfromtimestamp(sys['sunrise']).strftime('%H:%M:%S')
        sunset = datetime.utcfromtimestamp(sys['sunset']).strftime('%H:%M:%S')

        # Check if it will rain
        rain_info = "No rain expected." if rain == 0 else f"Rain expected: {rain} mm in the last hour."

        # Display current weather info
        result_label.config(text=f"Temperature: {temperature}°C\n"
                                f"Humidity: {humidity}%\n"
                                f"Condition: {description.capitalize()}\n"
                                f"Wind Speed: {wind_speed} m/s\n"
                                f"Wind Direction: {wind_deg}°\n"
                                f"Sunrise: {sunrise}\nSunset: {sunset}\n"
                                f"{rain_info}")
        
        # Get 5-day forecast
        forecast_response = requests.get(forecast_url)
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()
            forecast_text = "5-day Forecast:\n"
            for i in range(0, len(forecast_data['list']), 8):  # Every 8th entry corresponds to the same time every day
                forecast = forecast_data['list'][i]
                date = forecast['dt_txt'].split()[0]
                temp = forecast['main']['temp']
                description = forecast['weather'][0]['description']
                rain = forecast.get('rain', {}).get('3h', 0)  # Check for rain in the forecast (3h data)
                rain_info_forecast = "No rain" if rain == 0 else f"Rain: {rain} mm"
                forecast_text += f"{date}: {temp}°C, {description.capitalize()}, {rain_info_forecast}\n"
            forecast_label.config(text=forecast_text)
        else:
            messagebox.showerror("Error", "Error fetching forecast data.")
    else:
        messagebox.showerror("Error", "City not found. Please try again.")

# Set up the GUI window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x500")

# Create input fields and labels
city_label = tk.Label(root, text="Enter city name:", font=("Arial", 12))
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12), bg="skyblue")
search_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

forecast_label = tk.Label(root, text="", font=("Arial", 12), justify="left", anchor="w")
forecast_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
