from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class ModernMultiFunctionMachine(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


# In older machine, scan and fax may not be available. But still Machine Interface
# will force you to implement those other methods. May be you can add some comments or return some error message
# but still it will confuse client whoever is consuming it. so we should break the interface
class OlderFunctionMachine(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        """NOT IMPLEMENTED"""
        pass

    def scan(self, document):
        raise NotImplementedError("It is the not Implemented")


class Printer:
    def print(self, document):
        pass


class Scanner:
    def scan(self, document):
        pass


class Faxer:
    def fax(self, document):
        pass


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiDevice(Printer, Scanner, Faxer):

    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass


class MultiFunctionDevice(MultiDevice):
    def print(self, document):
        self.print(document)

    def scan(self, document):
        self.scan(document)

    def fax(self, document):
        self.fax(document)

# You can segregate and use the Interfaces like this. Having one interce is not good idea
