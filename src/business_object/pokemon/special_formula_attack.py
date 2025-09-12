from business_object.pokemon.abstract_formula_attack import AbstractFormulaAttack


class SpecialFormulaAttack(AbstractFormulaAttack):

    def get_attack_stat(self, attacker) -> float:
        return attacker.sp_atk_current

    def get_defense_stat(self, defender) -> float:
        return defender.sp_def_current
