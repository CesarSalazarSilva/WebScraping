
BOT_NAME = 'mercado'

SPIDER_MODULES = ['mercado.spiders']
NEWSPIDER_MODULE = 'mercado.spiders'

#CSV IMPORTACION
ITEM_PIPELINES = {'mercado.pipelines.MercadoPipeline': 500,
					'mercado.pipelines.MercadoImagenesPipeline': 600, }


ROBOTSTXT_OBEY = True

#Imagenes
IMAGES_STORE = 'url del directorio'
DOWNLOAD_DELAY = 2
