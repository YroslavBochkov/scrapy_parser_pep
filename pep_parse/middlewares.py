from scrapy import signals
from itemadapter import is_item, ItemAdapter


class PepParseSpiderMiddleware:
    """Middleware для обработки запросов и ответов в пауках."""

    @classmethod
    def from_crawler(cls, crawler):
        """Создает экземпляр middleware и подключает сигнал открытия паука."""
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        """Обрабатывает входящие ответы перед их передачей в паука."""
        return None  # Продолжить обработку

    def process_spider_output(self, response, result, spider):
        """Обрабатывает результаты, возвращенные пауком."""
        for item in result:
            yield item  # Возвращает элементы

    def process_spider_exception(self, response, exception, spider):
        """Обрабатывает исключения, возникающие в пауке."""
        pass  # Можно добавить обработку исключений

    def process_start_requests(self, start_requests, spider):
        """Обрабатывает начальные запросы паука."""
        for request in start_requests:
            yield request  # Возвращает начальные запросы

    def spider_opened(self, spider):
        """Логирует информацию об открытии паука."""
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:
    """Middleware для обработки запросов и ответов на уровне загрузчика."""

    @classmethod
    def from_crawler(cls, crawler):
        """Создает экземпляр middleware и подключает сигнал открытия паука."""
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        """Обрабатывает каждый запрос перед его отправкой."""
        return None  # Продолжить обработку запроса

    def process_response(self, request, response, spider):
        """Обрабатывает ответ, возвращенный загрузчиком."""
        return response  # Возвращает ответ

    def process_exception(self, request, exception, spider):
        """Обрабатывает исключения, возникающие при загрузке."""
        pass  # Можно добавить обработку исключений

    def spider_opened(self, spider):
        """Логирует информацию об открытии паука."""
        spider.logger.info('Spider opened: %s' % spider.name)
