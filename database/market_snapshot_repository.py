from sqlalchemy.orm import Session

from database.models import MarketSnapshot


class MarketSnapshotRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        item_id: int,
        price: float,
        buy_order: int = 0,
        sell_listing: int = 0,
        volume: int = 0
    ):

        snapshot = MarketSnapshot(
            item_id=item_id,
            price=price,
            buy_order=buy_order,
            sell_listing=sell_listing,
            volume=volume
        )

        self.db.add(snapshot)
        self.db.commit()
        self.db.refresh(snapshot)

        return snapshot

    def get_latest_by_item_id(
        self,
        item_id: int
    ):

        return (
            self.db.query(MarketSnapshot)
            .filter(
                MarketSnapshot.item_id == item_id
            )
            .order_by(
                MarketSnapshot.updated_at.desc()
            )
            .first()
        )

    def get_history_by_item_id(
        self,
        item_id: int
    ):

        return (
            self.db.query(MarketSnapshot)
            .filter(
                MarketSnapshot.item_id == item_id
            )
            .order_by(
                MarketSnapshot.updated_at.asc()
            )
            .all()
        )