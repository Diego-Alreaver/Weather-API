# Alreavers Weather API

## Overview
This Weather API is a simple yet powerful web service that provides current weather data for any city. Built using Django Rest Framework, this API allows users to easily access and retrieve weather information with minimal effort. 

## Features
- **City Weather Retrieval**: Get current weather details by providing the city name (If no city is specified, it defaults to London).
- **Caching with Redis**: The API caches weather data for up to 12 hours, improving response times for repeat requests.
- **Rate Limiting**: To ensure fair use, the API implements rate limiting, allowing only a certain number of requests per minute from a single IP address.
- **Swagger Documentation**: The API includes interactive Swagger documentation for easy exploration of its endpoints.

## Technologies Used
- **Django Rest Framework**: A powerful toolkit for building Web APIs in Python.
- **Redis**: An in-memory data structure store, used here for caching API responses.
- **dotenv**: A library to manage environment variables, keeping sensitive information secure.
- **drf-yasg**: A great library for generating real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API.


![image](https://github.com/user-attachments/assets/c802bfe7-00be-4750-979a-2d6349a939e8)

## Cache response:
![image](https://github.com/user-attachments/assets/3541baec-cc65-49f4-bc6e-8f1489d82c07)

## Normal response:
![image](https://github.com/user-attachments/assets/acd9f837-b950-4560-ac5e-eeb982306788)


