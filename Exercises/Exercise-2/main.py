import requests
# import pandas

URL = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
TIMESTAMP = '2022-02-07 14:03'

def main(URL):
    r = requests.get(URL)
    print(r.status_code)
    print(r.encoding)
    return r.text
    


if __name__ == '__main__':
    # m = main(URL)
    # with open('data.txt', 'w') as f:
    #     f.write(m)

    file = open('data.txt', 'r')
    
    for line in file:
        # print(line)
        # print(type(line))
        if TIMESTAMP in line:
            print(line)
            break
        continue

    file.close()
    # print(type(m))