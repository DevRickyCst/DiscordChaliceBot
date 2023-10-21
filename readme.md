# Discord bot using AWS Chalice

This repo is a sample of a discord bot using AWS chalice.

This webhook will respect the [security steps](https://discord.com/developers/docs/interactions/receiving-and-responding#security-and-authorization) ask by Discord in order that you can interact with the bot API.

## Requirements

- Create your discord bot on : https://discord.com/developers/applications
- Configure your AWS profile in order to use chalice CLI : https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

## Install

Set some environnement variable in order to interact with your bot :

(Actually using SSM but can be changed in app.py)

```
DISCORD_APPLICATION_ID = ssm.get_parameter(Name="DISCORD_APPLICATION_ID")["Parameter"]["Value"]  
DISCORD_BOT_PUBLIC_KEY = ssm.get_parameter(Name="DISCORD_BOT_PUBLIC_KEY")["Parameter"]["Value"]  
DISCORD_PRIVATE_KEY = ssm.get_parameter(Name="DISCORD_PRIVATE_KEY")["Parameter"]["Value"]
```

Now you can deploy your bot locally with :

`chalice local`

Or you can deploy it on an AWS lambda with an API Gateway endpoint using :

`chalice deploy`

## Discord Security Step

Every discord interactions is send to our app with the following headers :
- `X-Signature-Ed25519` as a signature
- `X-Signature-Timestamp` as a timestamp

We must validate the request each time using the signature. If the validation fails, we must return a 401 error code.

## Decorators

#### Authorize

`def verify_key_key(event, get_response)`

Use the verify function from the cryptography library NaCl in order verifies the signature of the signed message using our Discord Public Key

#### Ping_handler

`def ping_handler(event, get_response)`

When aptenting to set up the [INTERACTIONS ENDPOINT URL](https://discord.com/developers/applications/), Discord will send a POST request to that URL with a PING payload. The PING payload has a type: 1. So, to properly ACK the payload, we need to return a 200 response with a payload of type: 1: