test = {
  'name': 'Question 5b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # example 1
          >>> s0, s1 = hog.play(lambda score, other: (score + 3) // 4 * 2 + 3, lambda score, other: 4 - other // 4 * 2, score0=0, score1=0, goal=10, dice=always_one)
          >>> s0
          9
          >>> s1
          18
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # example 2
          >>> s0, s1 = hog.play(always(2), always(1), score0=0, score1=0, goal=5, dice=hog.make_test_dice(2, 2))
          >>> s0
          7
          >>> s1
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # swap after feral hogs
          >>> s0, s1 = hog.play(always(2), always(1), score0=45, score1=5, goal=50, dice=hog.make_test_dice(5, 2))
          >>> s0
          5
          >>> s1
          55
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_one = hog.make_test_dice(1)
      >>> always_two = hog.make_test_dice(2)
      >>> always_three = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> tests.play_utils.check_play_function(hog)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> # Fuzz Testing
      >>> # Plays a lot of random games, and calculates a secret value.
      >>> # Failing this test means something is wrong, but you should
      >>> # look at other tests to see where the problem might be.
      >>> # Hint: make sure you're only calling take_turn once per turn!
      >>> #
      >>> import hog, importlib
      >>> importlib.reload(hog)
      >>> import tests.play_utils
      """,
      'teardown': r"""
      
      """,
      'type': 'doctest'
    }
  ]
}
