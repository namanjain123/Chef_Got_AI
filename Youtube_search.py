import requests
from bs4 import BeautifulSoup
import webbrowser

def search_on_youtube(query):
    base_url = "https://www.youtube.com/results?search_query="
    query = query.replace(" ", "+")
    search_url = base_url + query
    return search_url

def get_first_five_results(query):
    search_url = search_on_youtube(query)
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    video_links = soup.findAll('a', {'class': 'yt-uix-tile-link'})

    results = []
    for link in video_links[:5]:  # Getting the first 5 links
        video_title = link['title']
        video_url = 'https://www.youtube.com' + link['href']
        results.append((video_title, video_url))

    return results

def get_youtubelinks(Cooking_recipe):
    search_results = get_first_five_results(Cooking_recipe)
    for idx, result in enumerate(search_results, start=1):
        print(f"{idx}. Title: {result[0]}")
        print(f"   URL: {result[1]}")
        print()

    # Open the first search result in the web browser
    if search_results:
        webbrowser.open(search_results[0][1])
