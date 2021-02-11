BOT_NAME = 'brsspa'

SPIDER_MODULES = ['brsspa.spiders']
NEWSPIDER_MODULE = 'brsspa.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'brsspa.pipelines.BrsspaPipeline': 100,

}