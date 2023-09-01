import abc


class IAnimal(abc.ABC):
    @abc.abstractmethod
    def hacer_sonido(self):
        pass
