import requests
import yaml


class DiscordBot:
    def __init__(
        self, application_id: int, discord_public_key: str, bot_private_key: str
    ) -> None:
        self.application_id = application_id
        self.discord_public_key = discord_public_key
        self.bot_private_key = bot_private_key
        self.headers = {
            "Authorization": f"Bot {bot_private_key}",
            "Content-Type": "application/json",
        }
        with open("./chalicelib/discord_commands.yaml", "r") as file:
            yaml_content = file.read()
        self.commands = yaml.safe_load(yaml_content)

    def register_commands(self):

        URL = f"https://discord.com/api/v10/applications/{self.application_id}/commands"

        for command in self.commands:
            response = requests.post(URL, json=command, headers=self.headers)
            command_name = command["name"]
            print(f"Command {command_name} created: {response.status_code}")

            if response.status_code != "200":
                print(response.content)

    def delete_commands(self):

        URL = f"https://discord.com/api/v10/applications/{self.application_id}/commands"

        for command in self.commands:
            response = requests.delete(URL, json=command, headers=self.headers)
            command_name = command["name"]
            print(f"Command {command_name} created: {response.status_code}")

            if response.status_code != "200":
                print(response.content)
