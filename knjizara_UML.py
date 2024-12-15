from graphviz import Digraph

# Kreiranje novog dijagrama
uml = Digraph('UML_Diagram', filename='bookstore_inventory', format='png')
uml.attr(rankdir='LR')

# Apstraktna klasa Book
uml.node('Book', '''<<abstract>> Book
- title: str
- author: str
- price: float
- quantity: int
+ get_details()''', shape='record')

# Podklase Textbook, PictureBook, i Novel
uml.node('Textbook', '''Textbook
- subject: str
- academic_level: str
+ get_details()''', shape='record')

uml.node('PictureBook', '''PictureBook
- illustrator: str
- recommended_age: int
+ get_details()''', shape='record')

uml.node('Novel', '''Novel
- genre: str
- is_bestseller: bool
+ get_details()''', shape='record')

# Klasa Inventory
uml.node('Inventory', '''Inventory
- books: List[Book]
+ add_book(book: Book)
+ remove_book(book: Book)
+ search_book(title: str)
+ display_inventory()''', shape='record')

# Klasa Order
uml.node('Order', '''Order
- order_id: int
- books: List[Book]
- total_price: float
+ add_book_to_order(book: Book)
+ calculate_total_price()''', shape='record')

# Klasa Customer
uml.node('Customer', '''Customer
- customer_id: int
- name: str
- phone: str
- address: str
- email: str
- orders: List[Order]
+ place_order(order: Order)
+ get_order_history()''', shape='record')

# Relacije između klasa
uml.edge('Book', 'Textbook', arrowhead='empty', label='inherits')
uml.edge('Book', 'PictureBook', arrowhead='empty', label='inherits')
uml.edge('Book', 'Novel', arrowhead='empty', label='inherits')

uml.edge('Inventory', 'Book', arrowhead='diamond', label='contains')
uml.edge('Order', 'Book', arrowhead='diamond', label='contains')
uml.edge('Customer', 'Order', arrowhead='diamond', label='contains')

# Generisanje dijagrama
uml.render()
