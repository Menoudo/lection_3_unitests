import requests
import logging

logging.basicConfig(level=logging.INFO)

WEATHER_API_URL_TEMPLATE = (
    "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
    "&current=temperature_2m,rain,cloud_cover&forecast_days=1"
)


def request_forecast_with_retry(url: str, max_retry=3) -> requests.Response:
    for n in range(max_retry):
        response = requests.get(url)
        if response.status_code == 200:
            return response
        logging.info(logging.INFO, "request forecast retry: %d", n)
    return response


def json_to_weather_forecast_string(json_data) -> str:
    return "Temperature: {} °C, Clouds: {}%, Rain: {} mm".format(
        json_data["current"]["temperature_2m"], 0, 0
    )


def get_weather(lat=56.06, lon=60.44) -> str:
    url = WEATHER_API_URL_TEMPLATE.format(lat=lat, lon=lon)
    logging.log(logging.INFO, "url: %s" % (url,))
    r = request_forecast_with_retry(url)
    if r.status_code == 200:
        return json_to_weather_forecast_string(r.json())
    else:
        return "No weather available"


if __name__ == "__main__":
    print(get_weather(0, 0))
