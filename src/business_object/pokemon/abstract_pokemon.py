import copy
from abc import ABC, abstractmethod
from business_object.statistic import Statistic


class AbstractPokemon(ABC):
    """
    Abstract class representing a Pokemon.
    """

    def __init__(self, stat_max: Statistic = None, stat_current: Statistic = None,
                 level: int = 0, name: str = None):
        self._stat_max: Statistic = stat_max
        self._stat_current: Statistic = stat_current or copy.deepcopy(stat_max)
        self._level: int = level
        self._name: str = name

    # -------------------------------------------------------------------------
    # Abstract method
    # -------------------------------------------------------------------------
    @abstractmethod
    def get_pokemon_attack_coef(self) -> float:
        """Compute the damage multiplier depending on the Pokemon type."""
        pass

    # -------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------
    def level_up(self) -> None:
        self._level += 1

    def reset_actual_stat(self) -> None:
        self._stat_current = copy.deepcopy(self._stat_max)

    def get_hit(self, damage: float) -> None:
        if damage > 0:
            self.hp_current = max(0, self.hp_current - damage)

    def __str__(self):
        return f"I am {self.name}, level: {self.level}, attack coef: {
            self.get_pokemon_attack_coef():.2f}"

    # -------------------------------------------------------------------------
    # Getters and Setters
    # -------------------------------------------------------------------------
    @property
    def attack(self):
        return self._stat_max.attack

    @property
    def hp(self):
        return self._stat_max.hp

    @property
    def defense(self):
        return self._stat_max.defense

    @property
    def sp_atk(self):
        return self._stat_max.sp_atk

    @property
    def sp_def(self):
        return self._stat_max.sp_def

    @property
    def speed(self):
        return self._stat_max.speed

    @property
    def attack_current(self):
        return self._stat_current.attack

    @attack_current.setter
    def attack_current(self, value):
        self._stat_current.attack = value

    @property
    def hp_current(self):
        return self._stat_current.hp

    @hp_current.setter
    def hp_current(self, value):
        self._stat_current.hp = value

    @property
    def defense_current(self):
        return self._stat_current.defense

    @defense_current.setter
    def defense_current(self, value):
        self._stat_current.defense = value

    @property
    def sp_atk_current(self):
        return self._stat_current.sp_atk

    @sp_atk_current.setter
    def sp_atk_current(self, value):
        self._stat_current.sp_atk = value

    @property
    def sp_def_current(self):
        return self._stat_current.sp_def

    @sp_def_current.setter
    def sp_def_current(self, value):
        self._stat_current.sp_def = value

    @property
    def speed_current(self):
        return self._stat_current.speed

    @speed_current.setter
    def speed_current(self, value):
        self._stat_current.speed = value

    @property
    def level(self):
        return self._level

    @property
    def name(self):
        return self._name
