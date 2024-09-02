from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    
    #POST; through form
    if request.method == "POST":
        #zipcode we got from form input
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=20&API_KEY=E2DDB5EA-19AE-4607-92E1-0CA4F031EFE6")
        
        try:
            api = json.loads(api_request.content)        
        except Exception as e:
            api = "Error...."
        
        if api[0]['Category']['Name'] == "Good":
            category_description = "(0-50) Air quality is considered satisfactory and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51-100) Air quality is acceptable and moderate health concern for sensitive people."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101-150) General public is not likely to be affected, people with lung and heart diseases are at risk."
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151-200) Everyone may begin to experience health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201-300) Health Alert: Everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301-500) Health warnings of emergency conditions. The entire population is likely to be affected."
            category_color = "hazardous"
        
        return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})
    
    else:
        
        #GET - regular hardcoded
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=20&API_KEY=E2DDB5EA-19AE-4607-92E1-0CA4F031EFE6")
        
        try:
            api = json.loads(api_request.content)        
        except Exception as e:
            api = "Error...."
        
        if api[0]['Category']['Name'] == "Good":
            category_description = "(0-50) Air quality is considered satisfactory and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51-100) Air quality is acceptable and moderate health concern for sensitive people."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101-150) General public is not likely to be affected, people with lung and heart diseases are at risk."
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151-200) Everyone may begin to experience health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201-300) Health Alert: Everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301-500) Health warnings of emergency conditions. The entire population is likely to be affected."
            category_color = "hazardous"
        
        return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})

def about(request):
    return render(request, 'about.html', {})