class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer) -> None:
        self._observers.append(observer)

    def detach(self, observer) -> None:
        """
        Detaches an observer from the subject.

        Args:
            observer: The observer to be detached from the subject.
        """
        self._observers.remove(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)