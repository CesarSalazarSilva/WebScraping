# -*- coding: utf-8 -*-

import scrapy


class MercadoItem(scrapy.Item):

    #info de producto
    titulo = scrapy.Field()
    modelo = scrapy.Field()
    marca = scrapy.Field()
    tecnologia = scrapy.Field()
    tipo = scrapy.Field()
    precio = scrapy.Field()
    condicion = scrapy.Field()
    envio = scrapy.Field()
    ubicacion = scrapy.Field()
    opiniones = scrapy.Field()

    #imagenes
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_name = scrapy.Field()


    #info de la tienda o vendedor
    vendedor_url = scrapy.Field()
    tipo_vendedor = scrapy.Field()
    ventas_vendedor = scrapy.Field()
