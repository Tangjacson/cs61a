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
          872dbe4a4fe5d8451aa842c21194c866
          # locked
          >>> s1
          b9f8886ee7ddbc03b40d55a3c1b576e2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # example 2
          >>> s0, s1 = hog.play(always(2), always(1), score0=0, score1=0, goal=5, dice=hog.make_test_dice(2, 2))
          >>> s0
          c42887e7b9ffe8fc26bb57b61329f916
          # locked
          >>> s1
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # swap after feral hogs
          >>> s0, s1 = hog.play(always(2), always(1), score0=45, score1=5, goal=50, dice=hog.make_test_dice(5, 2))
          >>> s0
          26f5762c932a578994ea1c8fc7fa6c02
          # locked
          >>> s1
          4541999a7580ea23f52926ad2c0bfc02
          # locked
          """,
          'hidden': False,
          'locked': True
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
