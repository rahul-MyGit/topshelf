from passlib.context import CryptContext

password_context = CryptContext(
    schemes=['bcrypt']
)

def generate_hash(password: str) -> str:
    return password_context.hash(password)

def verify_hash(password: str, hash: str) -> bool:
    return password_context.verify(password, hash)