
BOT_NAME = 'movistar'

SPIDER_MODULES = ['movistar.spiders']
NEWSPIDER_MODULE = 'movistar.spiders'

#CSV IMPORTACION
ITEM_PIPELINES = {'movistar.pipelines.movistarPipeline': 500}


ROBOTSTXT_OBEY = True

#Imagenes

