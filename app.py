from chalice import Chalice
from chalicelib.discord import DiscordBot

from chalicelib.decorators.authorize import verify_key_key
from chalicelib.decorators.ping_handler import ping_handler

import boto3

app = Chalice(app_name="Discord Bot")

ssm = boto3.client("ssm")

DISCORD_APPLICATION_ID = ssm.get_parameter(Name="DISCORD_APPLICATION_ID")["Parameter"][
    "Value"
]
DISCORD_BOT_PUBLIC_KEY = ssm.get_parameter(Name="DISCORD_BOT_PUBLIC_KEY")["Parameter"][
    "Value"
]
DISCORD_PRIVATE_KEY = ssm.get_parameter(Name="DISCORD_PRIVATE_KEY")["Parameter"][
    "Value"
]

discord = DiscordBot(
    DISCORD_APPLICATION_ID, DISCORD_BOT_PUBLIC_KEY, DISCORD_PRIVATE_KEY
)


app.register_middleware(verify_key_key, "all")
app.register_middleware(ping_handler, "all")


@app.route("/", methods=["POST"])
def index():
    params = app.current_request.json_body
    data = params["data"]
    command_name = data["name"]

    response = {"type": 4, "data": {"content": params}}

    return response
