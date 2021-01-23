# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    
    if request.method == "POST":
        #zipcode is the input element name
        zipcode = request.POST['zipcode']

        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=5C9783CC-85F7-468D-86AE-35BFB1C62530")

        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api = "Error"
        
        
        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50): Enjoy your outdoor activities"
            category_colour = "good"

        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100): If you are unusually sensitive to particle pollution, consider reducing your activity level or shorten the amount of time you are active outdoors."
            category_colour = "Moderate"

        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101 - 150): Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_colour = "UnhealthyforSensitiveGroups"

        elif api[0]['Category']['Name'] == "Unhealthy": 
            category_description = "(151 - 200): Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_colour = "Unhealthy"

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300): Health alert: The risk of health effects is increased for everyone."
            category_colour = "VeryUnhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301 - 500): Health warning of emergency conditions: everyone is more likely to be affected."
            category_colour = "Hazardous"

        return render(request, 'home.html', {'api':api, 'category_description':category_description, 'category_colour' : category_colour})

    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=85201&distance=5&API_KEY=5C9783CC-85F7-468D-86AE-35BFB1C62530")

        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api = "Error"
        
        
        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50): Enjoy your outdoor activities"
            category_colour = "good"

        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100): If you are unusually sensitive to particle pollution, consider reducing your activity level or shorten the amount of time you are active outdoors."
            category_colour = "Moderate"

        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101 - 150): Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_colour = "UnhealthyforSensitiveGroups"

        elif api[0]['Category']['Name'] == "Unhealthy": 
            category_description = "(151 - 200): Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_colour = "Unhealthy"

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300): Health alert: The risk of health effects is increased for everyone."
            category_colour = "VeryUnhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301 - 500): Health warning of emergency conditions: everyone is more likely to be affected."
            category_colour = "Hazardous"

        return render(request, 'home.html', {'api':api, 'category_description':category_description, 'category_colour' : category_colour})


def about(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=5C9783CC-85F7-468D-86AE-35BFB1C62530")

    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error"

    return render(request, 'about.html', {'api':api})
