import secrets
import string


def get_custom_alliance_name(name_alliance_len: int = 8) -> str:
    latin_letters_name = string.ascii_letters + string.digits
    return str("".join(secrets.choice(latin_letters_name) for _ in range(name_alliance_len))) + " Автотест"
