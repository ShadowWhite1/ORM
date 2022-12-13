import sqlalchemy
from sqlalchemy.orm import sessionmaker
from main import create_tables, Publisher, Shop, Book, Stock, Sale

DSN = "postgresql://postgres:@localhost:5432/netology_db1"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# author1 = Publisher(name="Пушкин")
# author2 = Publisher(name="Шевченко")
# session.add_all([author1,author2])
# session.commit()

# shop1 = Shop(name='Читай Город')
# shop2 = Shop(name='Буковка')
# session.add_all([shop1,shop2])
# session.commit()

# book1 = Book(title="Евгений Онегин", id_publisher = '1')
# book2 = Book(title="Руслана и Людмила", id_publisher = '1')
# book3 = Book(title="Кобзарь", id_publisher = '2')
# book4 = Book(title="Катерина", id_publisher = '2')
# session.add_all([book1,book2,book3,book4])
# session.commit()

# stock1 = Stock(id='1',id_book='1',id_shop='1',count='5')
# stock2 = Stock(id='2',id_book='2',id_shop='1',count='1')
# stock3 = Stock(id='3',id_book='2',id_shop='1',count='2')
# stock4 = Stock(id='4',id_book='3',id_shop='2',count='9')
# stock5 = Stock(id='5',id_book='4',id_shop='2',count='8')
# stock6 = Stock(id='6',id_book='3',id_shop='2',count='9')
# session.add_all([stock1,stock2,stock3,stock4,stock5,stock6])
# session.commit()

# sale1 = Sale(id='1',price='100', date_sale= '01/01/2022',id_stock='1')
# sale2 = Sale(id='2',price='500', date_sale= '16/02/2022',id_stock='2')
# sale3 = Sale(id='3',price='600', date_sale= '28/05/2022',id_stock='3')
# sale4 = Sale(id='4',price='150', date_sale= '15/07/2022',id_stock='4')
# sale5 = Sale(id='5',price='700', date_sale= '05/10/2022',id_stock='5')
# sale6 = Sale(id='6',price='600', date_sale= '12/12/2022',id_stock='6')
# session.add_all([sale1,sale2,sale3,sale4,sale5,sale6])
# session.commit()

name = input("Введите имя автора: ")
query = session.query(Stock,Book.title,Shop.name,Sale.price,Sale.date_sale)
query = query.join(Sale)
query = query.join(Shop)
query = query.join(Book)
query = query.join(Publisher)
records = query.filter(Publisher.name == (name))
for c in records:
    print(f'Название книги: {c[1]}, Магазин: {c[2]}, Стоимость: {c[3]}, Дата покупки: {(c[4]).day}-{(c[4]).month}-{(c[4]).year}')

session.close()