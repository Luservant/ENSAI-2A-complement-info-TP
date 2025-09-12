from abc import ABC, abstractmethod


class AbstractAttack(ABC):
    """
    Base class for all attacks
    """

    def __init__(self, name: str, description: str, power: int):
        self._name = name
        self._description = description
        self._power = power

    @abstractmethod
    def compute_damage(self, attacker, defender) -> int:
        """
        Compute the damage done by the attack.
        Must be implemented by child classes.
        """
        pass
