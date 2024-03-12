from datetime import datetime

class Score:
    def __init__(self, name, word, missing, seconds, time):
        self.__name = name
        self.__word = word
        self.__missing = missing
        self.__seconds = seconds if isinstance(seconds, int) else 0
        self.__time = self.validate_time(time)

    @property
    def name(self):
        return self.__name

    @property
    def word(self):
        return self.__word

    @property
    def missing(self):
        return self.__missing

    @property
    def seconds(self):
        return self.__seconds

    @property
    def time(self):
        return self.__time

    def validate_time(self, time_str):
        try:
            datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
            return time_str
        except ValueError:
            return datetime.now().strftime('%Y-%m-%d %H:%M:%S')