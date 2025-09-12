from business_object.pokemon.abstract_formula_attack import AbstractFormulaAttack


class PhysicalFormulaAttack(AbstractFormulaAttack):

    def get_attack_stat(self, attacker) -> float:
        return attacker.attack_current

    def get_defense_stat(self, defender) -> float:
        return defender.defense_current
