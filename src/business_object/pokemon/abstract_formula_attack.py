from abc import ABC, abstractmethod
from business_object.pokemon.abstract_attack import AbstractAttack
import random


class AbstractFormulaAttack(AbstractAttack, ABC):
    """
    Template method for variable damage attacks
    """

    def compute_damage(self, attacker, defender) -> int:
        """
        Compute the damage using the formula:
        damage = power * attack_stat / defense_stat * modifier
        modifier is a random float in [0.85, 1.0]
        """
        attack_stat = self.get_attack_stat(attacker)
        defense_stat = self.get_defense_stat(defender)
        modifier = random.uniform(0.85, 1.0)
        damage = int(self._power * attack_stat / defense_stat * modifier)
        return max(1, damage)  # minimum 1 damage

    @abstractmethod
    def get_attack_stat(self, attacker) -> float:
        """Return the relevant attack stat for this attack"""
        pass

    @abstractmethod
    def get_defense_stat(self, defender) -> float:
        """Return the relevant defense stat for this attack"""
        pass
