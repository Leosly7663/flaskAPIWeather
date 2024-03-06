# Flask REST API for Current Weather Data

This is a simple Flask REST API that retrieves current weather data for a given city.

## Endpoint

The API endpoint is `https://flask-apiw-eather.vercel.app//api/<cityName>` where `<cityName>` is the name of the city for which you want to retrieve weather data.

## Example

For example, if you want to get the weather data for Guelph, you would make a GET request to `https://flask-apiw-eather.vercel.app//api/Guelph`.

## Response

The API returns a JSON object containing the following weather data:

- `condition`: Description of the weather condition
- `dateQueried`: Date when the weather data was queried
- `dewPoint`: Dew point in Celsius
- `humidity`: Humidity level in percentage
- `observedLocation`: Location where the weather was observed
- `pressure`: Atmospheric pressure in kilopascals
- `temperature`: Current temperature in Celsius
- `tendency`: Description of the atmospheric pressure tendency
- `timeQueried`: Time when the weather data was queried
- `windDirection`: Wind direction
- `windSpeed`: Wind speed in kilometers per hour

  
### Example Response

```json
{
"condition":"Cloudy",
"dateQueried":"2024-03-06",
"dewPoint":4.6,
"humidity":84.0,
"observedLocation":"Guelph Turfgrass Institute 3:00 PM EST",
"pressure":101.7,
"temperature":7.0,
"tendency":"Falling",
"timeQueried":"15h22m",
"windDirection":"NNE",
"windSpeed":14
}
