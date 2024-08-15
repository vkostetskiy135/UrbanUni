from Module17.HW2024_03_03.app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from Module17.HW2024_03_03.app.models.user import User
class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, index=True, unique=True)
    user = relationship('User', back_populates='tasks')


from sqlalchemy.schema import CreateTable, DropTable
print(CreateTable(Task.__table__))
print(CreateTable(User.__table__))
