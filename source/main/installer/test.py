import requests
import os

def downloadFile(url, fileName, downloadDirectory):
    os.makedirs(downloadDirectory, exist_ok=True)
    filePath = os.path.join(downloadDirectory, fileName)
    response = requests.get(url)
    if response.status_code == 200:
        with open(filePath, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download file from {url}. Status code: {response.status_code}")

downloadFile(
    "https://raw.githubusercontent.com/JK00011GaMiNgG/InfinityCalculator/main/source/main/python/calculator.py", 
    "calculator.py", 
    "C:/Users/Administrator/OneDrive/Desktop/InfinityCalculator/source/main/installer"
)
