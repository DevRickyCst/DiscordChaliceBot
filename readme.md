# Discord bot using AWS Chalice

This repo is a sample of a discord bot using AWS chalice.

This webhook will respect the [security steps](https://discord.com/developers/docs/interactions/receiving-and-responding#security-and-authorization) ask by Discord in order that you can interact with the bot API.


## Install

Set some environnement variable in order to interact with your bot :

(Actually using SSM but can be changed in app.py)

```
DISCORD_APPLICATION_ID = ssm.get_parameter(Name="DISCORD_APPLICATION_ID")["Parameter"]["Value"]  
DISCORD_BOT_PUBLIC_KEY = ssm.get_parameter(Name="DISCORD_BOT_PUBLIC_KEY")["Parameter"]["Value"]  
DISCORD_PRIVATE_KEY = ssm.get_parameterName="DISCORD_PRIVATE_KEY")["Parameter"]["Value"]
```

Now you can deploy your bot locally with :

`chalice local`

Or you can deploy it on an AWS lambda with an API Gateway endpoint using :

`chalice deploy`