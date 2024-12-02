import toml

def read_config(file_path):
    try:
        with open(file_path, 'r') as file:
            config = toml.load(file)
            return config
    except Exception as e:
        print(f"An error occured while reading the config file: {e}")
        return None
        

def main():
    config = read_config('config.toml')

    if config:
        print("Title:", config.get('title', 'No title found'))

        owner = config.get('owner', {})
        print(f"Owner: {owner.get('name', 'Unknown')} ({owner.get('email', 'No email')})")

        database = config.get('database', {})
        print(f"Database Host: {database.get('hostname', 'No host')}")
        print(f"Port: {database.get('port', 'No port')}")


if __name__ == "__main__":
    main()