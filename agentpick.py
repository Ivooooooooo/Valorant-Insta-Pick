import json
import time
from valclient.client import Client
import sys

class ValorantAgentLocker:
    def __init__(self):
        try:
            with open('config.json') as config_file:
                config_data = json.load(config_file)
            self.region = config_data['instantlocker']["region"].lower()
            self.selected_agent = config_data['instantlocker']["preferred_agent"].lower()
            self.ask_to_change_agent = config_data['instantlocker']["askToChangeAgent"]
        except (KeyError, FileNotFoundError) as e:
            print(f"Error loading configuration file: {e}")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON file: {e}")
            sys.exit(1)

        try:
            with open('agents.json') as agents_file:
                self.agent_list = json.load(agents_file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading agents file: {e}")
            sys.exit(1)

        self.locked_matches = []

        self.selected_agent = self.get_preferred_agent()

    def start_client(self):
        while True:
            try:
                self.client = Client(region=self.region)
                self.client.activate()
                print(f"Client activated in region: {self.region.upper()}")
            except Exception as e:
                print(f"Error activating client: {e}. Please make sure the game is open.")
                time.sleep(5)
                continue
            self.run_locker()

    def get_preferred_agent(self):
        if not self.ask_to_change_agent:
            print(f"Auto-locking agent: {self.selected_agent.capitalize()}")
            return self.selected_agent

        while True:
            try:
                if self.selected_agent in self.agent_list:
                    print(f"Current preferred agent: {self.selected_agent.capitalize()}")
                    change_agent = input("Would you like to change your agent? (yes/no): ").strip().lower()
                    if change_agent == 'yes':
                        return self.change_agent()
                    return self.selected_agent
                else:
                    print(f"Agent '{self.selected_agent}' is not valid. Please choose a new agent.")
                    return self.change_agent()
            except Exception as e:
                print(f"Error selecting agent: {e}")
                time.sleep(1)

    def change_agent(self):
        print("Available agents:")
        for agent in self.agent_list.keys():
            print(f"- {agent.capitalize()}")

        while True:
            new_agent = input("Enter the name of the agent you want to lock: ").strip().lower()
            if new_agent in self.agent_list:
                self.selected_agent = new_agent
                print(f"Preferred agent changed to: {new_agent.capitalize()}")
                return new_agent
            else:
                print("Invalid agent name. Please try again.")

    def run_locker(self):
        print("Waiting for Agent Select phase...")
        while True:
            time.sleep(1)
            try:
                game_state = self.client.fetch_presence(self.client.puuid).get('sessionLoopState')
                match_id = self.client.pregame_fetch_match().get('ID')

                print(f'''Match ID: {match_id} Session state: {game_state}   ''', end="\r")

                if game_state == "PREGAME" and match_id not in self.locked_matches:
                    print('Agent Select phase detected.')
                    preferred_agent = self.selected_agent
                    agent_id = self.agent_list[preferred_agent]

                    try:
                        self.client.pregame_select_character(agent_id)
                        self.client.pregame_lock_character(agent_id)
                        self.locked_matches.append(match_id)
                        print(f"{preferred_agent.capitalize()} selected and locked successfully.")
                    except Exception as e:
                        print(f"Error selecting or locking agent: {e}")

                    if self.ask_to_change_agent:
                        self.selected_agent = self.get_preferred_agent()
            except Exception as e:
                print(f"Error fetching game state or match ID: {e}")

def main():
    agent_locker = ValorantAgentLocker()
    agent_locker.start_client()

if __name__ == "__main__":
    main()
