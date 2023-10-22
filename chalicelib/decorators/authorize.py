from chalice import Response
from nacl.signing import VerifyKey

from app import DISCORD_BOT_PUBLIC_KEY


def verify_key(
    raw_body: bytes, signature: str, timestamp: str, client_public_key: str
) -> bool:
    message = timestamp.encode() + raw_body
    try:
        vk = VerifyKey(bytes.fromhex(client_public_key))
        vk.verify(message, bytes.fromhex(signature))
        return True
    except Exception as ex:
        print(ex)
    return False


def verify_key_key(event, get_response):
    headers = event.headers
    signature = headers.get("X-Signature-Ed25519")
    timestamp = headers.get("X-Signature-Timestamp")

    if (
        signature is None
        or timestamp is None
        or not verify_key(event.raw_body, signature, timestamp, DISCORD_BOT_PUBLIC_KEY)
    ):
        return Response(status_code=401, body="invalide credentiels")
    response = get_response(event)
    return response
