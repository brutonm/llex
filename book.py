class book():
    def __init__(self, author: str, pages: int, hardcover: bool, topic: str) -> None:      
        self._author: str = author
        self._pages: int = pages
        self._hardcover: bool = hardcover
        self._topic: str = topic

    @property
    def author(self) -> str:
        return self._author
    @author.setter
    def author(self, value: str):
            self._author = value

    @property
    def pages(self) -> int:
        return self._pages
    @pages.setter
    def pages(self, value: int):
            self._pages = value

    @property
    def hardcover(self) -> bool:
        return self._hardcover
    @hardcover.setter
    def hardcover(self, value: bool):
            self._hardcover = value

    @property
    def topic(self) -> str:
        return self._topic
    @topic.setter
    def topic(self, value: str):
            self._topic = value