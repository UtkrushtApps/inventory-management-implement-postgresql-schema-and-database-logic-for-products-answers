from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product
from datetime import datetime

async def create_product(session: AsyncSession, name: str, sku: str, quantity: int) -> Product:
    product = Product(name=name, sku=sku, quantity=quantity, last_updated=datetime.utcnow())
    session.add(product)
    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()
        raise
    await session.refresh(product)
    return product

async def get_product_by_sku(session: AsyncSession, sku: str):
    result = await session.execute(select(Product).where(Product.sku == sku))
    return result.scalar_one_or_none()

async def list_products(session: AsyncSession):
    result = await session.execute(select(Product))
    return result.scalars().all()
