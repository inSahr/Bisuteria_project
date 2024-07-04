from flask import Flask, render_template, request, redirect
from conexion import Conexion
app =Flask(__name__)

@app.route("/")
def inicio():
    return render_template("base.html")



#DESDE AQUI EMPIEZA CLIENTES




@app.route("/clientes")
def clientes():
    return render_template("clientes/clientes.html")

@app.route("/clientes/crear")
def crearClientes():
    return render_template("clientes/crearClientes.html")

@app.route("/clientes/guardar", methods=["POST"])
def guardarClientes():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    correo = request.form["correo"]
    direccion = request.form["direccion"]

    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("INSERT INTO CLIENTES(nombre, apellido, correo, direccion) VALUES (%s, %s, %s, %s)",
                       (nombre, apellido, correo, direccion))
        conect.commit()
        conect.close()
        return redirect("/clientes/mostrar")
    
@app.route("/clientes/mostrar", methods=["GET"])
def mostrarClientes():
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("SELECT * FROM CLIENTES")
        clientes = cursor.fetchall()
    conect.close()
    return render_template("clientes/mostrarClientes.html", clientes=clientes)

@app.route("/clientes/editar/<int:id>")
def editarCliente(id):
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("SELECT * FROM CLIENTES WHERE idcliente = %s", (id))
        cliente = cursor.fetchone()
    conect.close()
    return render_template("clientes/editarClientes.html", cliente=cliente)

@app.route("/clientes/actualizar/<int:id>", methods=["POST"])
def actualizarCliente(id):
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    correo = request.form["correo"]
    direccion = request.form["direccion"]

    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("UPDATE CLIENTES SET nombre = %s, apellido = %s, correo = %s, direccion = %s WHERE idcliente = %s", (nombre, apellido, correo, direccion, id))
        conect.commit()
    conect.close()
    return redirect("/clientes/mostrar")

@app.route("/clientes/eliminar/<int:id>")
def eliminarCliente(id):
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("DELETE FROM CLIENTES WHERE idcliente = %s",(id))
        conect.commit()
    conect.close()
    return redirect("/clientes/mostrar")





#DESDE AQUI EMPIEZA PRODUCTOS





@app.route("/productos")
def productos():
    return render_template("productos/productos.html")

@app.route("/productos/crear")
def crearProductos():
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("SELECT * FROM CATEGORIAS")
        categorias = cursor.fetchall()
    conect.close()
    return render_template("productos/crearProductos.html", categorias=categorias)

@app.route("/productos/guardar", methods=["POST"])
def guardarProductos():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    stock = request.form["stock"]
    categoria = request.form["categoria"]

    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("INSERT INTO PRODUCTOS(nombre, descripcion, precio, stock, idcategoria) VALUES (%s,%s,%s,%s,%s)", (nombre, descripcion, precio, stock, categoria))
        conect.commit()
    conect.close()
    return redirect("/productos/mostrar")
    
@app.route("/productos/mostrar", methods=["GET"])
def mostrarProductos():
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("SELECT p.idproducto, p.nombre, p.descripcion, p.precio, p.stock, c.nombrecategoria FROM PRODUCTOS AS P JOIN CATEGORIAS AS C ON P.IDCATEGORIA = C.IDCATEGORIA")
        productos = cursor.fetchall()
    conect.close()
    return render_template("productos/mostrarProductos.html", productos=productos)

@app.route("/productos/editar/<int:id>")
def editarProducto(id):
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("SELECT * FROM PRODUCTOS WHERE idproducto = %s", (id))
        producto = cursor.fetchone()
        cursor.execute("SELECT * FROM CATEGORIAS")
        categorias = cursor.fetchall()
    conect.close()
    return render_template("productos/editarProductos.html", producto=producto, categorias=categorias)

@app.route("/productos/actualizar/<int:id>", methods=["POST"])
def actualizarProducto(id):
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    stock = request.form["stock"]
    categoria = request.form["categoria"]
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("UPDATE PRODUCTOS SET nombre = %s, descripcion = %s, precio = %s, stock = %s, categoria = %s WHERE idproducto = %s", (nombre, descripcion, precio, stock, categoria, id))
        conect.commit()
    conect.close()
    return redirect("/productos/mostrar")

@app.route("/productos/eliminar/<int:id>")
def eliminarProducto(id):
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("DELETE FROM PRODUCTOS WHERE idproducto = %s",(id))
        conect.commit()
    conect.close()
    return redirect("/productos/mostrar")




#DESDE AQUI EMPIEZA CATEGORIAS




@app.route("/categorias")
def categorias():
    return render_template("categorias/categorias.html")

@app.route("/categorias/crear")
def crearCategorias():
    return render_template("categorias/crearCategorias.html")

@app.route("/categorias/guardar", methods=["POST"])
def guardarCategorias():
    nombre = request.form["nombre"]
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("INSERT INTO CATEGORIAS(nombrecategoria) VALUES (%s)", (nombre))
        conect.commit()
    conect.close()
    return redirect("/categorias/mostrar")

@app.route("/categorias/mostrar", methods=["GET"])
def mostrarCategorias():
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("SELECT * FROM CATEGORIAS")
        categorias = cursor.fetchall()
    conect.close()
    return render_template("categorias/mostrarCategorias.html", categorias=categorias)

@app.route("/categorias/editar/<int:id>")
def editarCategoria(id):
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("SELECT * FROM CATEGORIAS WHERE idcategoria = %s", (id))
        categoria = cursor.fetchone()
    conect.close()
    return render_template("categorias/editarCategorias.html", categoria=categoria)

@app.route("/categorias/actualizar/<int:id>", methods=["POST"])
def actualizarCategoria(id):
    nombre = request.form["nombre"]
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("UPDATE CATEGORIAS SET nombrecategoria = %s WHERE idcategoria = %s", (nombre, id))
        conect.commit()
    conect.close()
    return redirect("/categorias/mostrar")

@app.route("/categorias/eliminar/<int:id>")
def elimiarCategoria(id):
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("DELETE FROM CATEGORIAS WHERE idcategoria = %s",(id))
        conect.commit()
    conect.close()
    return redirect("/categorias/mostrar")




#DESDE AQUI EMPIEZA PEDIDOS




@app.route("/pedidos")
def pedidos():
    return render_template("pedidos/pedidos.html")

@app.route("/pedidos/crear")
def crearPedidos():
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("SELECT * FROM CLIENTES")
        clientes = cursor.fetchall()
    conect.close()
    return render_template("pedidos/crearPedidos.html", clientes = clientes)

@app.route("/pedidos/guardar", methods=["POST"])
def guardarPedidos():
    fecha = request.form["fecha"]
    total = request.form["total"]
    cliente = request.form["cliente"]
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("INSERT INTO PEDIDOS(fecha, total, idcliente) VALUES (%s,%s,%s)", (fecha, total, cliente))
        conect.commit()
    conect.close()
    return redirect("/pedidos/mostrar")    

@app.route("/pedidos/mostrar", methods=["GET"])
def mostrarPedidos():
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("SELECT P.IDPEDIDO, P.FECHA, P.TOTAL, C.NOMBRE FROM PEDIDOS AS P JOIN CLIENTES AS C ON P.IDCLIENTE = C.IDCLIENTE")
        pedidos = cursor.fetchall()
    conect.close()
    return render_template("pedidos/mostrarPedidos.html", pedidos=pedidos)

@app.route("/pedidos/editar/<int:id>")
def editarPedidos(id):
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("SELECT * FROM PEDIDOS WHERE idpedido = %s", (id))
        pedido = cursor.fetchone()
        cursor.execute("SELECT * FROM CLIENTES")
        clientes = cursor.fetchall()
    conect.close()
    return render_template("pedidos/editarPedidos.html", pedido=pedido, clientes=clientes)

@app.route("/pedidos/actualizar/<int:id>", methods=["POST"])
def actualizarPedidos(id):
    fecha = request.form["fecha"]
    total = request.form["total"]
    cliente = request.form["cliente"]
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("UPDATE PEDIDOS SET fecha = %s, total = %s, idcliente = %s WHERE idpedido = %s", (fecha, total, cliente, id))
        conect.commit()
    conect.close()
    return redirect("/pedidos/mostrar")

@app.route("/pedidos/eliminar/<int:id>")
def eliminarPedidos(id):
    conect = Conexion.obtener_conexion()
    with conect.cursor() as cursor:
        cursor.execute("DELETE FROM PEDIDOS WHERE idpedido = %s",(id))
        conect.commit()
    conect.close()
    return redirect("/pedidos/mostrar")


if __name__ == '__main__':
    app.run(debug=True)