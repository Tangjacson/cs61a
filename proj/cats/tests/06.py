test = {
  'name': 'Problem 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_limit = 10
          >>> swap_diff("car", "cad", big_limit)
          1
          >>> swap_diff("this", "that", big_limit)
          2
          >>> swap_diff("one", "two", big_limit)
          3
          >>> swap_diff("from", "form", big_limit)
          2
          >>> swap_diff("awe", "awesome", big_limit)
          4
          >>> swap_diff("someawe", "awesome", big_limit)
          6
          >>> swap_diff("awful", "awesome", big_limit)
          5
          >>> swap_diff("awful", "awesome", 3) > 3
          True
          >>> swap_diff("awful", "awesome", 4) > 4
          True
          >>> swap_diff("awful", "awesome", 5) > 5
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> big_limit = 10
          >>> swap_diff("goodbye", "good", big_limit)
          3
          >>> swap_diff("pront", "print", big_limit)
          1
          >>> swap_diff("misspollid", "misspelled", big_limit)
          2
          >>> swap_diff("worry", "word", big_limit)
          2
          >>> swap_diff("first", "flashy", big_limit)
          4
          >>> swap_diff("hash", "ash", big_limit)
          4
          >>> swap_diff("ash", "hash", big_limit)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> small_words_list = ["spell", "nest", "test", "pest", "best", "bird", "wired",
          ...                     "abstraction", "abstract", "peeling", "gestate", "west",
          ...                     "spelling", "bastion"]
          >>> autocorrect("speling", small_words_list, swap_diff, 10)
          'peeling'
          >>> autocorrect("abstrction", small_words_list, swap_diff, 10)
          'abstract'
          >>> autocorrect("wird", small_words_list, swap_diff, 10)
          'bird'
          >>> autocorrect("gest", small_words_list, swap_diff, 10)
          'nest'
          >>> # ban iteration
          >>> test.check('typing.py', 'swap_diff', ['While', 'For'])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # ***Check that the recursion stops when the limit is reached***
          >>> import trace, io
          >>> from contextlib import redirect_stdout
          >>> with io.StringIO() as buf, redirect_stdout(buf):
          ...     trace.Trace(trace=True).runfunc(swap_diff, "someaweqwertyuio", "awesomeasdfghjkl", 3)
          ...     output = buf.getvalue()
          >>> len([line for line in output.split('\n') if 'funcname' in line]) < 10
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('thong', 'thong', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('hyper', 'hypebey', k) > k for k in range(7)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('life', 'endif', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('watap', 'watap', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('outer', 'outer', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('wake', 'sutra', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('leach', 'leac', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('mold', 'mjl', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('habit', 'obole', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('zarf', 'zarf', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('clyer', 'pout', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('sate', 'socle', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('succi', 'skcvi', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('aval', 'yelm', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('skean', 'drupe', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('sizer', 'siz', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('kerat', 'rerat', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('twirk', 'twsrkj', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('reply', 'repldd', k) > k for k in range(6)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('sin', 'sin', k) > k for k in range(3)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('cack', 'cawkb', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('redub', 'wedobt', k) > k for k in range(6)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('vocal', 'vocal', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('rust', 'rustc', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('saft', 'doct', k) > k for k in range(4)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('thee', 'th', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('kayak', 'kayak', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('hong', 'wyson', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('rohob', 'eohov', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('gyne', 'boyer', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('cosh', 'vagus', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('slive', 'slivem', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('tikor', 'tikor', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('boba', 'bodif', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('query', 'queit', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('merop', 'mer', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('albe', 'albjn', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('czech', 'mixed', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('borer', 'borea', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('socky', 'socky', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('creed', 'socle', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('blake', 'vp', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('keck', 'kecs', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('somal', 'voma', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('sadic', 'sadicrhl', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('try', 'tryv', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('parch', 'sitio', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('ungum', 'unguma', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('xp', 'flack', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('break', 'orei', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('bouge', 'booeu', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('scoon', 'icon', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('cash', 'cash', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('model', 'modelvtv', k) > k for k in range(8)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('kaput', 'kap', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('solon', 'once', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('glum', 'glum', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('api', 'wyi', k) > k for k in range(3)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('sith', 'sith', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('jute', 'jute', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('dubba', 'jacob', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('cheat', 'mezzo', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('inch', 'inc', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('moule', 'moul', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('alowe', 'bland', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('eche', 'pchee', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('astir', 'astir', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('scram', 'scrpc', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('chank', 'alef', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('soral', 'soral', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('verge', 'vergbdz', k) > k for k in range(7)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('anomy', 'awhet', 100)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('neigh', 'neig', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('plume', 'plut', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('siroc', 'lir', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('geat', 'geat', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('tires', 'tires', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('corol', 'corzn', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('barn', 'bar', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('agnus', 'aenn', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('hemp', 'hempxwm', 100)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('tsere', 'tslreg', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('thar', 'thav', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('blah', 'blahs', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('grank', 'gronb', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('koi', 'koi', k) > k for k in range(3)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('ghz', 'dooli', 100)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('dp', 'dp', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('foo', 'foo', k) > k for k in range(3)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('akund', 'akun', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('jete', 'jete', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('cob', 'co', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('snook', 'snook', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('unorn', 'unorn', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('liz', 'li', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('datum', 'datumoi', 100)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('tosh', 'tos', 100)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_diff('bound', 'bound', 100)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('guib', 'guano', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum([swap_diff('inurn', 'inurn', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from typing import swap_diff, autocorrect
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
