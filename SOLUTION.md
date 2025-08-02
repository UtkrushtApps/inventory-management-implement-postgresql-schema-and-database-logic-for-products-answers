# Solution Steps

1. 1. Create an Alembic migration (e.g. in alembic/versions/) that defines a 'products' table with fields: id (PK), name, sku (unique, indexed), quantity, last_updated (updated at). Add indices for sku (unique) and name (for search).

2. 2. In app/models/, define a Product SQLAlchemy model matching the table schema: id, name, sku (unique), quantity, last_updated, all with correct types and constraints. Apply indices where needed.

3. 3. In app/db/session.py, set up the async SQLAlchemy engine and session using create_async_engine and sessionmaker, exposing an async dependency 'get_session' for getting an AsyncSession.

4. 4. In app/db/crud_product.py, implement async DB logic using SQLAlchemy ORM and AsyncSession: (a) create_product for inserting new products (with uniqueness check on SKU), (b) get_product_by_sku for fetching one product by SKU, and (c) list_products to retrieve all products.

5. 5. Do not modify or touch any FastAPI route logic; use only the above model, session, and CRUD logic for the database layer.

6. 6. Ensure that all DB operations are performed asynchronously and that appropriate indices and constraints are set up for performance and data consistency.

