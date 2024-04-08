import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.layout = QVBoxLayout()
        self.city_layout = QHBoxLayout()

        self.label_city = QLabel()
        self.label_weather = QLabel()
        self.label_temperature = QLabel()
        self.label_humidity = QLabel()
        self.label_wind_speed = QLabel()

        self.textbox = QLineEdit()
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.fetch_weather_data)

        self.city_layout.addWidget(QLabel("City: "))
        self.city_layout.addWidget(self.textbox)
        self.city_layout.addWidget(self.search_button)

        self.layout.addLayout(self.city_layout)
        self.layout.addWidget(self.label_city)
        self.layout.addWidget(self.label_weather)
        self.layout.addWidget(self.label_temperature)
        self.layout.addWidget(self.label_humidity)
        self.layout.addWidget(self.label_wind_speed)
        self.setLayout(self.layout)

    def fetch_weather_data(self):
        city = self.textbox.text().strip()
        if not city:
            print("Please enter a city name.")
            return

        api_key = "a3a8ee035471296c25c880d91c36cb22"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        print("API URL:", url)

        try:
            response = requests.get(url)
            print("Response status code:", response.status_code)
            if response.status_code == 200:
                data = response.json()
                self.update_weather_data(data)
            else:
                print("Error fetching weather data:", response.status_code)
                print("Response content:", response.content.decode())
        except Exception as e:
            print("Error fetching weather data:", e)

    def update_weather_data(self, data):
        if data:
            self.label_city.setText("City: " + data["name"])
            self.label_weather.setText("Weather: " + data["weather"][0]["description"])
            self.label_temperature.setText("Temperature (°C): " + str(data["main"]["temp"]))
            self.label_humidity.setText("Humidity: " + str(data["main"]["humidity"]))
            self.label_wind_speed.setText("Wind Speed (m/s): " + str(data["wind"]["speed"]))
        else:
            print("No weather data available.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
