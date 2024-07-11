# Asynchronous Downloader
This repository contains a simple asynchronous downloader that can be used to download all `.webm` and `.png` files from a website concurrently. This enables the rapid download of large numbers of files which can be useful for scraping image boards, open directories, and similar websites.

## Installation
To install the downloader, clone the repository and install the requirements using conda / pip. 

As there are only a few requirements, I do not provide a `requirements.txt` file.

## Usage
To use the downloader, set your target directory in the script and then run the `asynchronous_downloader.py` file. You will be prompted to provide the URL of the website you want to download files from. 


## Limitations
The current implementation is limited to downloading files from websites with direct links in the HTML - image boards, open directories, and similar websites work well. 

It does not support downloading files from websites that require authentication or which load files dynamically using JavaScript or similar technologies.



