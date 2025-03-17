from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        """
        Receive a message and perform an update.

        Args:
            message (str): The message to be processed during the update.
        """
        pass