from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()


class Message(Base):
    __tablename__ = "messages"
    id: Mapped[int] = mapped_column(primary_key=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    message: Mapped[str] = mapped_column(String)
    date: Mapped[str] = mapped_column(String)

    def __repr__(self) -> str:
        return f"Message(id={self.id!r}, project_id={self.project_id!r}, message={self.message!r}, date={self.date!r})"
