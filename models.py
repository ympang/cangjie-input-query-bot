from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DATETIME, Boolean

Base = declarative_base()


class CodeInfo(Base):
    __tablename__ = "code_info"
    id = Column(Integer, primary_key=True)
    word = Column(String)
    code = Column(String)

    def __repr__(self):
        return "<CodeInfo(id='%s', character='%s', code='%s')>" % (
            self.id,
            self.character,
            self.code,
        )
