from src.database.base import Base
from sqlalchemy import column

class User_Class(Base):
    __tablename__="User"

    user_id = column(...,nullable=False)
    user_name = column(...,nullable=False)
    user_email = column(..., nullable=False)
    user_password = column(...,nullable=False)
    user_contact = column(...,nullable=False)
    user_role = column(...,nullable=False)
    user_pincode = column(...,nullable=False)
    user_department_id = column(..., nullable=True)
