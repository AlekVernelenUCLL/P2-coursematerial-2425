from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
    assert overlapping_intervals((3, 9), (9, 9))
    assert overlapping_intervals((1, 4), (1, 9))
    assert not overlapping_intervals((9, 8), (8, 9))
    assert overlapping_intervals((1, 1), (1, 1))
    assert overlapping_intervals((-5, 3), (-2, 6))
    assert not overlapping_intervals((-5, 3), (-7, -6))
    assert not overlapping_intervals((-2, 2), (4, 1))