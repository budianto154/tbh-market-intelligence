from datetime import datetime, UTC

from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)

    steam_name: Mapped[str] = mapped_column(
        String(255),
        unique=True
    )

    market_hash_name: Mapped[str] = mapped_column(
        String(255),
        unique=True
    )

    category: Mapped[str] = mapped_column(
        String(100),
        default="Unknown"
    )

    rarity: Mapped[str] = mapped_column(
        String(50),
        default="Unknown"
    )

    market = relationship(
        "MarketSnapshot",
        back_populates="item"
    )


class MarketSnapshot(Base):
    __tablename__ = "market_snapshot"

    id: Mapped[int] = mapped_column(primary_key=True)

    item_id: Mapped[int] = mapped_column(
        ForeignKey("items.id")
    )

    price: Mapped[float] = mapped_column(
        Float,
        default=0
    )

    buy_order: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    sell_listing: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    volume: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )

    item = relationship(
        "Item",
        back_populates="market"
    )