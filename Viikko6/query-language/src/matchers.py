class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class Not:
    def __init__(self, to_negate):
        self._to_negate = to_negate

    def test(self, player):
        return not self._to_negate.test(player)

class HasFewerThan:
    def __init__(self, value, attr):
        self._has_at_least = HasAtLeast(value, attr)
        self._negation = Not(self._has_at_least)
    
    def test(self, player):
        return self._negation.test(player)

class All:
    def __init__(self, condition=None):
        self._condition = condition

    def test(self, players):
        if self._condition is None:
            return players
        return all(self._condition.test(p) for p in players)

class Or:
    def __init__(self, *conditions):
        self._conditions = conditions

    def test(self, player):
        return any(cond.test(player) for cond in self._conditions)