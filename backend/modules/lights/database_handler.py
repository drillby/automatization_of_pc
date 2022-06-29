from typing import List
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import INTEGER


Base = declarative_base()


class Device(Base):
    __tablename__ = "Devices"
    id = sa.Column(INTEGER(unsigned=True), primary_key=True,
                   autoincrement=True)
    name = sa.Column(sa.String)
    device_type = sa.Column(sa.String)
    ip = sa.Column(sa.String)
    room = sa.Column(sa.String)
    status = sa.Column(sa.Boolean)


class DatabaseHandler:
    def __init__(
        self, db_type: str, host: str, port: int, user: str, password: str, db_name: str
    ) -> None:
        """Will connect to the database and create a session
        Args:
            db_type (str): Type of database (mysql, sqlite, etc.)
            host (str): Hostname of the database
            port (int): Port of the database
            user (str): Username of the database
            password (str): Password of the database
            db_name (str): Name of the database
        """
        engine = sa.create_engine(
            f"{db_type}://{user}:{password}@{host}:{port}/{db_name}"
        )
        self.Session = sa.orm.sessionmaker()
        self.Session.configure(bind=engine)
        self.Session = self.Session()

    @property
    def get_devices(self) -> List[Device]:
        """Will get all devices in databsae

        Returns:
            List[Device]: List of all devices
        """
        devices = self.Session.query(Device).distinct().all()
        return [device[0] for device in devices]

    @property
    def get_rooms(self) -> List[str]:
        """Returns names of all rooms

        Returns:
            List[str]: List of strings(room names)
        """
        return self.Session.query(Device.room).distinct().all()

    def get_device_by_id(self, id: int) -> Device:
        return self.Session.query(Device).filter(Device.id == id).first()
