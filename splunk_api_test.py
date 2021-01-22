import splunklib.client as client
import splunklib.results as results

HOST = "localhost"
PORT = 8089
USERNAME = "admin"
PASSWORD = "changeme"

# Create a Service instance and log in 
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)



# Run a one-shot search and display the results using the results reader

# Set the parameters for the search:
# - Search everything in a 24-hour time range starting June 19, 12:00pm
# - Display the first 10 results
kwargs_oneshot = {"earliest_time": "2020-10-12T12:00:00.000-07:00",
                  "latest_time": "2020-10-13T12:00:00.000-07:00"}
searchquery_oneshot = "search index=notable | head 10"

oneshotsearch_results = service.jobs.oneshot(searchquery_oneshot, **kwargs_oneshot)

# Get the results and display them using the ResultsReader
reader = results.ResultsReader(oneshotsearch_results)
for item in reader:
    print("\n")
    print(item)