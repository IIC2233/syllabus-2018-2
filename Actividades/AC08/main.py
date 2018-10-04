from dccontrolador import PedidoOnline, Producto, Supermercado


def cargar_productos(ruta):
    with open(ruta) as archivo:
        next(archivo)
        yield from archivo


def procesar_linea(linea):
    nombre, codigo, precio_base, descuento = linea.strip().split(',')
    return codigo, Producto(nombre, float(precio_base), float(descuento))


def poblar_supermercado(supermercado, ruta):
    for codigo, producto in map(procesar_linea, cargar_productos('datos.csv')):
        supermercado.agregar_producto(codigo, producto)


def armar_pedido(pedido_online, orden):
    supermercado = pedido_online.supermercado

    for codigo, cantidad in orden.items():
        if codigo not in supermercado:
            continue
        producto = supermercado[codigo]
        pedido_online.añadir_producto(producto, cantidad)


if __name__ == '__main__':
    dccomercio = Supermercado('DCComercio')
    dcc_bm = Supermercado('DCCBM')

    poblar_supermercado(dccomercio, 'datos.csv')
    poblar_supermercado(dcc_bm, 'datos.csv')

    dccomercio_online = PedidoOnline(dccomercio)
    www_dccomercio = PedidoOnline(dccomercio)
    dcc_bm_web = PedidoOnline(dcc_bm)

    primera_orden = {
        '38.46.54': 1,
        '16.36.09': 2,
        '29.39.45': 2,
    }
    armar_pedido(dccomercio_online, primera_orden)
    print(f'El primer pedido cuesta: ${dccomercio_online.total:.2f}')

    segunda_orden = {
        '70.93.47': 3,
        '29.34.29': 1,
        '20.38.76': 2,
    }
    armar_pedido(www_dccomercio, segunda_orden)
    print(f'El segundo pedido cuesta: ${www_dccomercio.total:.2f}')

    tercera_orden = {
        '16.36.09': 2,
        '29.39.45': 1,
        '70.93.47': 3,
        '29.34.29': 3,
    }
    armar_pedido(dcc_bm_web, tercera_orden)
    print(f'El tercer pedido cuesta: ${dcc_bm_web.total:.2f}')

    primer_gran_pedido = dccomercio_online + www_dccomercio
    print(f'Primer y segundo pedido cuesta: ${primer_gran_pedido.total:.2f}')

    segundo_gran_pedido = dccomercio_online + dcc_bm_web
    print(f'Primer y tercer pedidos cuestas: ${segundo_gran_pedido.total:.2f}')
