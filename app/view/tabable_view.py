from abc import abstractmethod


class TabableView:

    @abstractmethod
    def closeable(self):
        pass

    @abstractmethod
    def tab_name(self):
        pass