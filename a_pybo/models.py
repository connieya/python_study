from sqlalchemy import Column , Integer , String , Text, DateTime ,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# 질문 모델
class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)

# 답변 모델
class Answer(Base):
    __tablename__ = "answer"
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")