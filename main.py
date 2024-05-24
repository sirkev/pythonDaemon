import requests
import time
import os


def fetch_and_save_api_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def write_to_file(content):
    # Open the file in append mode and write to it
    with open("api_response.txt", "a") as file:
        file.write(content + "\n")


def run_as_daemon():
    api_url = "https://jsonplaceholder.typicode.com/posts/1"
    print('starting main process...')
    time.sleep(5)

    # Detach the process from the terminal
    pid = os.fork()
    if pid > 0:
        print('forked main process...')
        time.sleep(5)

        print('exiting main process...')
        return
    else:
        print('running daemon process successful...')
        while True:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            response_content = fetch_and_save_api_response(api_url)
            if response_content:
                write_to_file(current_time)
                write_to_file(response_content)
            time.sleep(5)


if __name__ == "__main__":
    run_as_daemon()
