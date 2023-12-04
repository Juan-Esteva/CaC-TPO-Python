products = []
# Agregar producto
def add_product(product_code, barcode, description, stock, price, content, unit, picture, supplier):
  if exist_product(product_code):
    return False
  new_product = {
    'product_code': product_code, # PK Int ascii
    'barcode': barcode,           # EAN Code str
    'description': description,   # setattr
    'stock': stock,               # float
    'price': price,               # float
    'content': content,         # float
    'unit': unit,                 # str
    'picture': picture,           # str
    'supplier': supplier          # FK Int
    }
  products.append(new_product)
  return True
# verificar si existe producto 
def exist_product(product_code):
  for product in products:
    if product['product_code'] == product_code:
      #print(product_code, " ya Existe")
      return product
  #print(product_code, " no Existe") 
  return False
# Carga una lista de datos de prueba
def load_data():
  data_hc = [
    [ 1 , "",  "Leche en Polvo",  5, 3750.00, 800, "gramos", "", 57],
    [ 2 , "", "Azúcar Común"   , 15, 1180.00,   1, "kilogramo", "", 18],
    [ 3 , "", "Harina leudante", 25,  480.00,   1, "kilogramo", "", 23],
    [ 4 , "", "Aceite de maiz",  10,  690.00,   1,     "litro", "", 23],
    [ 5 , "",  "Queso cremoso",  10, 2360.00,   1,     "kilogramo", "", 57],
    ]
  for product in data_hc:
    # print(product)
    add_product(product[0], 
                product[1], 
                product[2],
                product[3],
                product[4], 
                product[5], 
                product[6],
                product[7],
                product[8])
  return True
# Reemplaza datos producto
def replace_product(product_code, new_barcode, new_description, new_stock, new_price, new_content, new_unit, new_picture, new_supplier):
  for product in products:
    if product['product_code'] == product_code:
      product['barcode']     = new_barcode
      product['description'] = new_description
      product['stock']       = new_stock
      product['price']       = new_price
      product['content']    = new_content
      product['unit']        = new_unit
      product['picture']     = new_picture
      product['supplier']    = new_supplier
      return True
  return False
# Listado de Productos
def list_products():
  sep = "-" * 75
  print(sep)
  for product in products:
    print(f"Código ......: {product['product_code']}")
    print(f"Descripción .: {product['description']}")
    print(f"Stock .......: {product['stock']}")
    print(f"Precio ......: {product['price']}")
    print(f"Contenido ...: {product['content']}")
    print(f"Unidad ......: {product['unit']}")
    print(f"Imágen ......: {product['picture']}")
    print(f"Proveedor ...: {product['supplier']}")
    print(sep)
  return True
# Eliminar Producto
def remove_product(product_code):
  for product in products:
    if product['product_code'] == product_code:
      products.remove(product)
      return True
  return False
  
# Pruebas del código
load_data()
list_products()
# print(products[3])
# replace_product( 4, "", "Leche en Polvo Descremada", 5, 2700.90, 800, "gramos", "", 57)
remove_product(1)
list_products()
#:add_product( 1, "", "Leche en Polvo", 5, 2700.90, 800, "gramos", "", 57)