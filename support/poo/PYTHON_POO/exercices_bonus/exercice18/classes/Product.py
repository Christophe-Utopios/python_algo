class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, index=True)
    quantity = Column(Integer, index=True)
    order_id = Column(Integer, index=True)