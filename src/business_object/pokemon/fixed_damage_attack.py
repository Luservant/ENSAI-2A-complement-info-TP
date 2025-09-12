from business_object.pokemon.abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    def compute_damage(self, attacker, defender) -> int:
        return self._power
