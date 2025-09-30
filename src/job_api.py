from apify_client import ApifyClient
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

apify_client = ApifyClient(os.getenv("APIFY_API_KEY"))  # create apify client



# search for linkedin jobs
def fetch_linkedin_jobs(search_query, location="sri lanka", rows=60):

    # Prepare the Actor input (we can add more like remote or not, location...)
    # these parts can be found in apify site
    run_input = {
        # "keyword": search_query,
        # "maxJobs": 60,
        # "freshness": "all",
        # "sortBy": "relevance",
        # "experience": "all",
        # "fullTime": False,
        # "partTime": False,
        # "contract": False,
        # "temporary": False,
        # "internship": False,
        "location": location,
        "rows": rows,
        "title": search_query,
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"],
        }   
    }

    # Run the Actor and wait for it to finish
    run = apify_client.actor("RIGGeqD6RqKmlVoQU").call(run_input=run_input)

    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs






# search for nakuri jobs
def fetch_nakuri_jobs(search_query, location="sri lanka", rows=60):  # rows = maximum job units
    run_input = {
        "keyword": search_query,
        "maxJobs": 60,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
        # "location": location,
        # "rows": rows,
        # "title": search_query,
        # "proxy": {
        #     "useApifyProxy": True,
        #     "apifyProxyGroups": ["RESIDENTIAL"],
        # } 
    }
    
    # do not forget to pass the actor id from that sdk code
    run = apify_client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)

    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs

