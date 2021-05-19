
import requests
import json
import time
from flask import Flask,jsonify,render_template

app = Flask(__name__)
# Fetching Data through API
api = "https://disease.sh/v3/covid-19/all"
json_data = requests.get(api).json()
#newDict = json.dumps(json_data,indent = 2 ,sort_keys=True)

# Storing specific data inside specific variable 
totalDeaths = str(json_data['deaths'])
totalinfected =str(time.strftime("%I:%M:%S",time.gmtime(json_data['updated']- 21600)))
casesToday = str(json_data['todayCases'])
deathToday = str(json_data['todayDeaths'])
totalrecovered = str(json_data['recovered'])
recoveredToday = str(json_data['todayRecovered'])
activeCases = str(json_data['active'])
criticalCases = str(json_data['critical'])

# creating route for the app
@app.route('/')
def index():
    # Sending API data to template
    return render_template("index.html",content=totalDeaths,totalinfected=totalinfected,casesToday = casesToday,deathToday = deathToday,totalrecovered = totalrecovered, recoveredToday = recoveredToday,activeCases = activeCases  )
if __name__ == "__main__":
    app.run()


  