from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(primary_key=True)

    gym_id: Mapped[int] = mapped_column(
        ForeignKey("gyms.id")
    )

    customer_name: Mapped[str] = mapped_column(
        String(100)
    )

    phone: Mapped[str] = mapped_column(
        String(20)
    )

    interested_in: Mapped[str] = mapped_column(
        String(100)
    )

    source: Mapped[str] = mapped_column(
        String(50)
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="NEW"
    )

    notes: Mapped[str] = mapped_column(
        String(500),
        default=""
    )