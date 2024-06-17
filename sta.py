
class SpaceTimeElement:
    def __init__(self, value):
        if isinstance(value, int) and value >= 0:
            self.value = value
        elif isinstance(value, str) and value == '∞':
            self.value = value
        else:
            raise ValueError("Value must be a non-negative integer or '∞'")

    def value(self):
        return self.value

    def __repr__(self):
        return str(self.value)

    def __eq__(self, x):
        if not isinstance(x, SpaceTimeElement):
            return NotImplemented
        return self.value == x.value

    def __lt__(self, x):
        if not isinstance(x, SpaceTimeElement):
            return NotImplemented
        if isinstance(x.value, str):
            return isinstance(self.value, int)
        return isinstance(self.value, int) and self.value < x.value

    def __le__(self, x):
        if not isinstance(x, SpaceTimeElement):
            return NotImplemented
        if isinstance(x.value, str):
            return True
        return isinstance(self.value, int) and self.value <= x.value


STE = SpaceTimeElement

inf = STE('∞')

# 1-ary primitives

def st_id(a: STE) -> STE:
    return a

def st_inc(a: STE) -> STE:
    return a if a == inf else STE(a.value + 1)

# 2 -ary primitives

## commutative

def st_min(a: STE, b: STE) -> STE:
    return a if a <= b else b

def st_max(a: STE, b: STE) -> STE:
    return a if a >= b else b

def st_xmin(a: STE, b: STE) -> STE:
    return a if a < b else b if b < a else inf

def st_xmax(a: STE, b: STE) -> STE:
    return a if a > b else b if b > a else inf

def st_eq(a: STE, b: STE) -> STE:
    return a if a == b else inf

## non-commutative

def st_neq(a: STE, b: STE) -> STE:
    return a if a != b else inf

def st_lt(a: STE, b: STE) -> STE:
    return a if a < b else inf

def st_lte(a: STE, b: STE) -> STE:
    return a if a <= b else inf

def st_gt(a: STE, b: STE) -> STE:
    return a if a > b else inf

def st_gte(a: STE, b: STE) -> STE:
    return a if a >= b else inf
    

def run():
    st0 = STE(0)
    st1 = STE(1)
    print(f"{st0} + 1 = {st_inc(st0)}")
    print(f"{st1} + 1 = {st_inc(st1)}")
    print(f"{inf} + 1 = {st_inc(inf)}")
    print(st_min(st0, st1))
    print(st_max(st0, st1))
    print(st_eq(st0, st1), st_neq(st0, st1))
    print(st_eq(st1, st0), st_neq(st1, st0))
    print(st_eq(st1, st1), st_neq(st1, st1))
    print(st_xmin(st0, st1), st_xmin(st1, st0), st_xmin(st0, st0))
    print(st_xmax(st0, st1), st_xmax(st1, st0), st_xmax(st1, st1))

    print(st_lt(st0, st1), st_lte(st0, st1), st_gt(st0, st1), st_gte(st0, st1))
    print(st_lt(st1, st1), st_lte(st1, st1), st_gt(st1, st1), st_gte(st1, st1))


if __name__ == '__main__':
    run()
