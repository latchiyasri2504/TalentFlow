
import secrets
import hashlib
from datetime import datetime, timedelta, timezone


def generate_otp() -> str:
    return str(secrets.randbelow(900000) + 100000)


def hash_otp(otp: str) -> str:
    return hashlib.sha256(otp.encode()).hexdigest()


def verify_otp(otp: str, stored_hash: str) -> bool:
    return hash_otp(otp) == stored_hash


def get_expiry_time():
    return datetime.now(timezone.utc) + timedelta(minutes=5)
