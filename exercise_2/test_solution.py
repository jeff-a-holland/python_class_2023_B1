#!/Users/jeff/.pyenv/shims/python
#!/usr/bin/env python3

import solution
import pytest

def test_myrange2_is_a_list():
    output = solution.myrange2(10)
    assert type(output) is list

@pytest.mark.parametrize('first, second, third, output', [
    (10, None, None, list(range(10))),
    (10, 20, None, list(range(10,20))),
    (20, 10, None, []),
    (10, 20, 2, list(range(10,20,2))),
    (10, 20, 3, list(range(10,20,3)))
])
def test_myrange2(first, second, third, output):
    if third:
        assert solution.myrange2(first, second, third) == output
    else:
        assert solution.myrange2(first, second) == output

def test_myrange3_is_a_generator():
    output = solution.myrange3(10)
    assert iter(output) is output

@pytest.mark.parametrize('first, second, third, output', [
    (10, None, None, list(range(10))),
    (10, 20, None, list(range(10,20))),
    (20, 10, None, []),
    (10, 20, 2, list(range(10,20,2))),
    (10, 20, 3, list(range(10,20,3)))
])
def test_myrange3(first, second, third, output):
    if third:
        assert list(solution.myrange3(first, second, third)) == output
    else:
        assert list(solution.myrange3(first, second)) == output