import json
import os
import requests
from zipfile import ZipFile

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]


def main() -> None:
    # creeate the directory downloads if it doesn't exist
    if not os.path.exists(f"{os.getcwd()}/downloads"):
        os.makedirs(f"{os.getcwd()}/downloads")

    os.chdir('downloads/')

    # download the files one by one
    for uri in download_uris:
        file_name = uri.split("/")[-1]
        with requests.get(uri, allow_redirects = True) as r:
            if r.status_code == 404:
                print(f'File "{file_name}" not found!')
                continue
            elif r.status_code == 200:
                open(uri.split("/")[-1], 'wb').write(r.content)
                print(f'File "{file_name}" has been downloaded!')

    # each file is a zip, extract the csv from the zip and delete the zip file
    for file in os.listdir():
        if file.endswith(".zip"):
            with ZipFile(file, "r") as archive:
                file_names = archive.namelist()

                for file_name in file_names:
                    print(file_name)
                    if file_name.endswith(".csv"):
                        archive.extract(file_name)
                        print(f'File "{file_name}" has been extracted.')

        os.remove(file)
        print(f"Archive {file} has been removed!")


if __name__ == '__main__':
    main()