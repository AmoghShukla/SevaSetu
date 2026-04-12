from src.database.base import Base
from sqlalchemy import column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

class User_Class(Base):
    __tablename__="User"

    user_id = column(Integer, primary_key=True,index=True)
    user_name = column(String, nullable=False)
    user_email = column(String, nullable=False)
    user_password = column(String, nullable=False)
    user_contact = column(String, nullable=False)
    user_role = column(String, nullable=False)
    user_pincode = column(Integer, nullable=False)
    user_department_id = column(Integer, nullable=False)
