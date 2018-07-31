
BOT_NAME = 'virgin'

SPIDER_MODULES = ['virgin.spiders']
NEWSPIDER_MODULE = 'virgin.spiders'

#CSV IMPORTACION
ITEM_PIPELINES = {'virgin.pipelines.virginPipeline': 500}


ROBOTSTXT_OBEY = True

#Imagenes

