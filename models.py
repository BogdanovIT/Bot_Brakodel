from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///brakobaza_2.sqlite3')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    tg_id = mapped_column(BigInteger, primary_key=True)
    name:Mapped[str] = mapped_column()
    region:Mapped[str] = mapped_column()
    town:Mapped[str] = mapped_column()
    location:Mapped[str] = mapped_column()
    email:Mapped[str] = mapped_column()
    post: Mapped[str] = mapped_column()

class Brak(Base):
    __tablename__ = 'brak'

    id: Mapped[int] = mapped_column(primary_key=True)
    Doc_data: Mapped[str] = mapped_column()
    Doc_liter: Mapped[str] = mapped_column()

    Doc_number: Mapped[str] = mapped_column()
    ER_number: Mapped[str] = mapped_column()
    SSCC_number: Mapped[str] = mapped_column()
    NS_Code: Mapped[str] = mapped_column()
    Name_item: Mapped[str] = mapped_column()
    Serial_number: Mapped[str] = mapped_column()
    Sort_select: Mapped[str] = mapped_column()
    Cell_number: Mapped[str] = mapped_column()
    Comment: Mapped[str] = mapped_column()

class Catalog(Base):
    __tablename__ = 'catalog'
    primary_code: Mapped[str] = mapped_column(primary_key=True)
    product: Mapped[str] = mapped_column()
    barcode: Mapped[str] = mapped_column()

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)