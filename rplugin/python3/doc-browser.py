import neovim
import logging
import os
import http.client

@neovim.plugin
class Docbrowser():
    def __init__(self, nvim):
        self.nvim = nvim
        self.logger = logging.getLogger('docbrowser')
        self.logfile = os.getenv('DOCBROWSER_DEBUG_LOG', None)
        if self.logfile:
            log_format = '%(asctime)s %(levelname)-8s (%(name)s) %(message)s'
            formatter = logging.Formatter(log_format)
            handler = logging.FileHandler(filename=self.logfile)
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.DEBUG)


    @neovim.function('DocbrowserSummon', range=False, sync=False)
    def summon(self, args):
        [query] = args
        conn = http.client.HTTPConnection('localhost:7701')
        conn.request("GET", f'/summon?q={query}')
        resp = conn.getresponse()
        return resp.status
