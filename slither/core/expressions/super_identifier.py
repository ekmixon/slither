from slither.core.expressions.identifier import Identifier


class SuperIdentifier(Identifier):
    def __str__(self):
        return f"super.{str(self._value)}"
