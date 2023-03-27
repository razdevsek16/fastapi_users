from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):  # type: ignore
        return pwd_cxt.hash(password)
    
    
    def verify(h_password: str, p_password: str):
        return pwd_cxt.verify(p_password,h_password)  # type: ignore
    
    