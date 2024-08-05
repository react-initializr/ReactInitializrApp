from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from reactinitializrapp.utils.database import Base


class Project(Base):
    __tablename__ = "projects"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"Project(id={self.id!r}, name={self.name!r})"
