from flask import current_app
from jwt.exceptions import InvalidIssuerError


def parse_jwt(verifier, encoded_jwt):
    """Decode an encoded JWT using stored config."""
    claims = verifier.verify_jwt(
        encoded_jwt,
        current_app.config.asap['VALID_AUDIENCE'],
        leeway=60,
        verify=current_app.config.asap.get('VERIFY_TLS_CERT', True)
    )

    valid_issuers = current_app.config.asap.get('VALID_ISSUERS')
    if valid_issuers and claims.get('iss') not in valid_issuers:
        raise InvalidIssuerError

    return claims