from sqlalchemy import String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Membership(Base):
    __tablename__ = "memberships"

    id: Mapped[int] = mapped_column(primary_key=True)

    gym_id: Mapped[int] = mapped_column(
        ForeignKey("gyms.id")
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    duration_months: Mapped[int] = mapped_column(
        Integer
    )

    price: Mapped[float] = mapped_column(
        Float
    )

    joining_fee: Mapped[float] = mapped_column(
        Float,
        default=0
    )

    description: Mapped[str] = mapped_column(
        String(500)
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )