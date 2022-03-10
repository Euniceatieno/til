# Relationships in sqlalchemy
There exists different relationships between tables  
in sql i.e one to many ,many to many etc  
Below is a code snippet of two models to demostrate database relationships in sql:

```class Product(Base):
    """Product table fields"""

    __tablename__ =  "product"

    id = Column(Integer,primary_key= True,autoincrement="auto")
    name = Column(String,unique=True,nullable=False)
    image = image_attachment('ProductPicture')
    description = Column(String(255),nullable=False)
    category_id = Column(Integer,ForeignKey = "category.id") #relationship added


         """on deleting a category , a product is deleted as well"""

    category = relationship(Category, backref = backref('products', uselist=True, cascade='delete,all'))


    def __repr__():
        return "<Product %r>" % self.

class Product_Item(Base):
    """Product_item table fields"""

    __tablename__ = "product_item"

    id = Column(Integer,primary_key=True,autoincrement="auto")
    product_id = Column(Integer,ForeignKey ="product.id") #relationship added 
    name = Column(String , unique = True , nullable = False)
    description = Column(Text , nullable = False)
    image_url = image_attachment('UserPicture')
    uom_id = Column(Integer ,ForeignKey = "uom.id") #relationship added

    
         """on_deleting a product or a uom , a Product_Item is deleted"""
    product = relationship(Product, backref = backref('product_items', uselist=True, cascade='delete,all'))
    uom = relationship(UOM, backref = backref('product_items', uselist=True, cascade='delete,all'))


    def __repr__(self):
        return "<Product_Item %r>" % self.name


class Category(Base):
    """Category table fields"""

    __tablename__ = "category"

    id = Column(Integer , primary_key = True, autoincrement = "auto")
    name = Column(String(255) , unique = True , nullable = False)
    description = Column(Text , nullable = False)

    def __repr__(self):
        return "<Category %r>" % self.name
```
