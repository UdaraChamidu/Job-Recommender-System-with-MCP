from mcp.server.fastmcp import FastMCP
from src.job_api import fetch_linkedin_jobs, fetch_nakuri_jobs

# initialize the mcp
mcp = FastMCP("Job Recommender")

# convert it as a tool
@mcp.tool()
async def fetch_linkedin_jobs_tool(listofkey):
    return fetch_linkedin_jobs(listofkey)

@mcp.tool()
async def fetch_nakuri_jobs_tool(listofkey):
    return fetch_nakuri_jobs(listofkey)

# initialize the server
if __name__ == "__main__":
    mcp.run(transport="stdio")  # You can also use "http" for HTTP transport
    