class Logger(object):
    """
    A file based message logger with following properties

    Attributes:
        filename: full path of the log file to which logger will write its message
    """

    def __init__(self, filename):
        self.filename = filename

    def _write_log(self, level, msg):
        with open(self.filename, "a") as log_file:
            log_file.write("[{0}] {1}\n".format(level, msg))

    def critical(self, msg):
        self._write_log("CRITICAL", msg)

    def error(self, msg):
        self._write_log("ERROR", msg)

    def warn(self, msg):
        self._write_log("WARN", msg)

    def info(self, msg):
        self._write_log("INFO", msg)

    def debug(self, msg):
        self._write_log("DEBUG", msg)

