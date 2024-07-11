import requests
from bs4 import BeautifulSoup
import os
import concurrent.futures 
from concurrent.futures import ThreadPoolExecutor

def find_webm_links(url):
    """Fetch all .webm file links from a given URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        if link['href'].endswith('.webm'):
            links.append(link['href'])
            
    links = [f"https:{link}" for link in links]
    return links

def find_png_links(url):
    """Fetch all .png file links from a given URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        if link['href'].endswith('.png'):
            links.append(link['href'])
            
    links = [f"https:{link}" for link in links]
    return links

def download_file(link, directory):
    """Download a file given by the link into the specified directory."""   
    filename = os.path.join(directory, link.split('/')[-1])
    response = requests.get(link, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    else:
        print(f"Failed to download {link}")

def main(url, target_dir):
    """Main function to download all .webm files from a webpage using threading."""
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    webm_links = find_webm_links(url)
    webm_links = set(webm_links)
    print(f"Webm files to download: {len(webm_links)}")
    
    png_links = find_png_links(url)
    png_links = set(png_links)
    print(f"Png files to download: {len(png_links)}")

    
    # Set up a ThreadPoolExecutor to download files concurrently
    with ThreadPoolExecutor(max_workers=15) as executor:
        futures = [executor.submit(download_file, link, target_dir) for link in webm_links]
        for future in concurrent.futures.as_completed(futures):
            future.result()  # This will raise exceptions if any occurred during thread execution
        futures = [executor.submit(download_file, link, target_dir) for link in png_links]
        for future in concurrent.futures.as_completed(futures):
            future.result()  # This will raise exceptions if any occurred during thread execution


    print(f"Download complete. Files are saved to {target_dir}")

if __name__ == '__main__':
    url = input("Input link below:\n")
    
    # Replace with your path - will create it if it doesn't exist already
    target_dir = 'test_folder'  
    main(url, target_dir)
