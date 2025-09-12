from business_object.pokemon.fixed_damage_attack import FixedDamageAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.statistic import Statistic


class TestFixedDamageAttack:

    def test_compute_damage(self):
        # GIVEN
        attack = FixedDamageAttack(name="Tackle", description="A simple hit", power=50)
        attacker = AttackerPokemon(stat_current=Statistic(attack=50, speed=50))
        defender = AttackerPokemon(stat_current=Statistic(attack=30, speed=30))

        # WHEN
        damage = attack.compute_damage(attacker, defender)

        # THEN
        assert damage == 50
