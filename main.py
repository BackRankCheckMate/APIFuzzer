import requests
import sys

def fuzz(ip):
    for word in sys.stdin:
        res = requests.get(url=f"http://{ip}/{word}")
        if res.status_code == 404:
            continue
        else:
            data = res.json()
            print(data)
            print(res.status_code)
            print(word)

def main():
    ip = input("Enter IP address:")
    fuzz(ip)

if __name__ == "__main__":
    main()