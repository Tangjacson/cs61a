test = {
  'name': 'Problem 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ps = ['short', 'really long', 'tiny']
          >>> s = lambda p: len(p) <= 5
          >>> choose(ps, s, 0)
          'short'
          >>> choose(ps, s, 1)
          'tiny'
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from typing import choose
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> ps = ['d', 'Njtv', 'Kxg', 'ym6bMNxUy', 'Lz']
          >>> s = lambda p: p == 'Kxg' or p == 'Lz' or p == 'd'
          >>> choose(ps, s, 0)
          'd'
          >>> choose(ps, s, 1)
          'Kxg'
          >>> choose(ps, s, 2)
          'Lz'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['pVasJy', 'ZD', 'toNG']
          >>> s = lambda p: p == 'ZD' or p == 'pVasJy' or p == 'toNG'
          >>> choose(ps, s, 0)
          'pVasJy'
          >>> choose(ps, s, 1)
          'ZD'
          >>> choose(ps, s, 2)
          'toNG'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['JlY3CIaa', '1fMO0', 'pe', 'Q6F4bbNP5J']
          >>> s = lambda p: p == '1fMO0' or p == 'pe'
          >>> choose(ps, s, 0)
          '1fMO0'
          >>> choose(ps, s, 1)
          'pe'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['o', '1m5Q']
          >>> s = lambda p: p == '1m5Q'
          >>> choose(ps, s, 0)
          '1m5Q'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['eV0dmK0', 'opuJ6xpn1', 'WXfPJa', 'EaXYKI']
          >>> s = lambda p: p == 'WXfPJa' or p == 'opuJ6xpn1'
          >>> choose(ps, s, 0)
          'opuJ6xpn1'
          >>> choose(ps, s, 1)
          'WXfPJa'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['jakYR6', '7c5IJE7d', 'UJu', 'YB', '6bKkwROlcZ', 'G', 'aMtUQZ4']
          >>> s = lambda p: p == 'G' or p == 'UJu'
          >>> choose(ps, s, 0)
          'UJu'
          >>> choose(ps, s, 1)
          'G'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['RnW', 'itFiAc40d', 'e']
          >>> s = lambda p: p == 'RnW' or p == 'e' or p == 'itFiAc40d'
          >>> choose(ps, s, 0)
          'RnW'
          >>> choose(ps, s, 1)
          'itFiAc40d'
          >>> choose(ps, s, 2)
          'e'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Tl4qyDvUzq', '219tHOGK77', 'gvFnh4ypPs', '2plMVD5bF', 'Sy9ydsV', 'QmMJ']
          >>> s = lambda p: p == '2plMVD5bF' or p == 'QmMJ' or p == 'Sy9ydsV' or p == 'gvFnh4ypPs'
          >>> choose(ps, s, 0)
          'gvFnh4ypPs'
          >>> choose(ps, s, 1)
          '2plMVD5bF'
          >>> choose(ps, s, 2)
          'Sy9ydsV'
          >>> choose(ps, s, 3)
          'QmMJ'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['k2RL9', 'cBtzx1ZUu', 'DdJNjj', 'xdUAYSdFjk', 'N9vHSIIy', 'fO', 'alIf1', 'i']
          >>> s = lambda p: p == 'DdJNjj' or p == 'N9vHSIIy' or p == 'alIf1' or p == 'cBtzx1ZUu' or p == 'k2RL9'
          >>> choose(ps, s, 0)
          'k2RL9'
          >>> choose(ps, s, 1)
          'cBtzx1ZUu'
          >>> choose(ps, s, 2)
          'DdJNjj'
          >>> choose(ps, s, 3)
          'N9vHSIIy'
          >>> choose(ps, s, 4)
          'alIf1'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['WzdN8', 'YEDX', 'sr', '9cfLm']
          >>> s = lambda p: p == 'YEDX' or p == 'sr'
          >>> choose(ps, s, 0)
          'YEDX'
          >>> choose(ps, s, 1)
          'sr'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['NlwErghs', 'XPDU', 'jzYGBj', 'P6', 'w']
          >>> s = lambda p: p == 'NlwErghs'
          >>> choose(ps, s, 0)
          'NlwErghs'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['dZi4B', 'Gtihxn6r', '03alCKzGQ', 'CusewJ6', 'hi9n', 'aipp1l', 'NCTAk', 'UXBZJ']
          >>> s = lambda p: p == '03alCKzGQ' or p == 'NCTAk' or p == 'dZi4B' or p == 'hi9n'
          >>> choose(ps, s, 0)
          'dZi4B'
          >>> choose(ps, s, 1)
          '03alCKzGQ'
          >>> choose(ps, s, 2)
          'hi9n'
          >>> choose(ps, s, 3)
          'NCTAk'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Txb', 'Q1WE7qA', '6XQj', 'gMNin4hq4w', 'pziJgrhuz', '8q4', 'Txy']
          >>> s = lambda p: p == 'gMNin4hq4w' or p == 'pziJgrhuz'
          >>> choose(ps, s, 0)
          'gMNin4hq4w'
          >>> choose(ps, s, 1)
          'pziJgrhuz'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['HL5xB', 'Z1', 'Zw2hPXj2', 't', 'Kru1WdQbu', 'eqWVk', 'EBRFugj8B', 'tmsX', 'HRd']
          >>> s = lambda p: p == 'EBRFugj8B' or p == 'Kru1WdQbu' or p == 't'
          >>> choose(ps, s, 0)
          't'
          >>> choose(ps, s, 1)
          'Kru1WdQbu'
          >>> choose(ps, s, 2)
          'EBRFugj8B'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['fgdI', 'O8HCeAG4TZ', '1fHh9Ei2uh', 'vBSd']
          >>> s = lambda p: p == '1fHh9Ei2uh' or p == 'vBSd'
          >>> choose(ps, s, 0)
          '1fHh9Ei2uh'
          >>> choose(ps, s, 1)
          'vBSd'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['thvLCiRUaO', 'MzkZ', '7xG', 'AoGZ', 'HS75YTP']
          >>> s = lambda p: p == '7xG' or p == 'AoGZ' or p == 'HS75YTP' or p == 'MzkZ'
          >>> choose(ps, s, 0)
          'MzkZ'
          >>> choose(ps, s, 1)
          '7xG'
          >>> choose(ps, s, 2)
          'AoGZ'
          >>> choose(ps, s, 3)
          'HS75YTP'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['uT5', 'KPeXYnET', 'IJjA3A2w']
          >>> s = lambda p: p == 'KPeXYnET'
          >>> choose(ps, s, 0)
          'KPeXYnET'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Uq98V6O', 'k', 'EgT1EpPM']
          >>> s = lambda p: p == 'Uq98V6O' or p == 'k'
          >>> choose(ps, s, 0)
          'Uq98V6O'
          >>> choose(ps, s, 1)
          'k'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Pc', 'CoL', 'KFDY8UD', 'HmG', 'qciZ9kWAB4', 'bafyIpd8U', 'Rtygug']
          >>> s = lambda p: p == 'CoL'
          >>> choose(ps, s, 0)
          'CoL'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['TjK2nv', 'JT', '6izv', 'wqzU3L', 'fg']
          >>> s = lambda p: p == 'wqzU3L'
          >>> choose(ps, s, 0)
          'wqzU3L'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['TfV7QdkY', 'Bzd9osf6er', 'EydfOK', '3y', 'sH', 'h1', '0', 'rD']
          >>> s = lambda p: p == '0' or p == 'rD'
          >>> choose(ps, s, 0)
          '0'
          >>> choose(ps, s, 1)
          'rD'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['R0P', 'm', 'jsehdWm', '0TWTsZ', 'hA', 'UD', 'kuQb', 'uqQYCAx0', 'c']
          >>> s = lambda p: p == 'UD' or p == 'c' or p == 'kuQb' or p == 'm'
          >>> choose(ps, s, 0)
          'm'
          >>> choose(ps, s, 1)
          'UD'
          >>> choose(ps, s, 2)
          'kuQb'
          >>> choose(ps, s, 3)
          'c'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['PkmOH', 'NG6HAJ', 'YysuECiszy', 'Q7CysdSt']
          >>> s = lambda p: p == 'PkmOH'
          >>> choose(ps, s, 0)
          'PkmOH'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['BJ5gtIY', 'MuR', 'aKTPcHm']
          >>> s = lambda p: p == 'BJ5gtIY' or p == 'aKTPcHm'
          >>> choose(ps, s, 0)
          'BJ5gtIY'
          >>> choose(ps, s, 1)
          'aKTPcHm'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Mbkg9g', 'MlYvYYZ', 'mDj', 'if01', 'Rp', '4sznEC', 'vgKWOAEfpL']
          >>> s = lambda p: p == 'Mbkg9g' or p == 'MlYvYYZ' or p == 'if01' or p == 'mDj'
          >>> choose(ps, s, 0)
          'Mbkg9g'
          >>> choose(ps, s, 1)
          'MlYvYYZ'
          >>> choose(ps, s, 2)
          'mDj'
          >>> choose(ps, s, 3)
          'if01'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['tfKtKfC', 'tm', 'h0qDaxp', '9dqW', 'u0L44Wr15j', 'oHeqKhx', '9wIE2qBV']
          >>> s = lambda p: p == '9dqW' or p == 'h0qDaxp' or p == 'oHeqKhx' or p == 'tfKtKfC'
          >>> choose(ps, s, 0)
          'tfKtKfC'
          >>> choose(ps, s, 1)
          'h0qDaxp'
          >>> choose(ps, s, 2)
          '9dqW'
          >>> choose(ps, s, 3)
          'oHeqKhx'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['rJhT7WL', '1nLtR']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['8Kb9Df']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['OwEteuQk7', 'w8L6', 'O8rZO7QEDH', 'yqJND8', 'xi', 'x']
          >>> s = lambda p: p == 'O8rZO7QEDH' or p == 'OwEteuQk7' or p == 'w8L6' or p == 'x' or p == 'xi'
          >>> choose(ps, s, 0)
          'OwEteuQk7'
          >>> choose(ps, s, 1)
          'w8L6'
          >>> choose(ps, s, 2)
          'O8rZO7QEDH'
          >>> choose(ps, s, 3)
          'xi'
          >>> choose(ps, s, 4)
          'x'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['3pLPrqWRU', '2tVwTl', 'h3', 'h', 'GKsxvci', 'MMKb17']
          >>> s = lambda p: p == '2tVwTl' or p == 'GKsxvci' or p == 'h3'
          >>> choose(ps, s, 0)
          '2tVwTl'
          >>> choose(ps, s, 1)
          'h3'
          >>> choose(ps, s, 2)
          'GKsxvci'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Yj3eX']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['dnln', 'rAgVI']
          >>> s = lambda p: p == 'dnln'
          >>> choose(ps, s, 0)
          'dnln'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Lz', 'v3KeV', 'lIH', 'WlHz', 'FT', 'zyTMZqx', 'AU6D', 'f5h', '0N2h']
          >>> s = lambda p: p == '0N2h' or p == 'AU6D' or p == 'FT' or p == 'Lz' or p == 'WlHz' or p == 'f5h' or p == 'lIH' or p == 'zyTMZqx'
          >>> choose(ps, s, 0)
          'Lz'
          >>> choose(ps, s, 1)
          'lIH'
          >>> choose(ps, s, 2)
          'WlHz'
          >>> choose(ps, s, 3)
          'FT'
          >>> choose(ps, s, 4)
          'zyTMZqx'
          >>> choose(ps, s, 5)
          'AU6D'
          >>> choose(ps, s, 6)
          'f5h'
          >>> choose(ps, s, 7)
          '0N2h'
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['784e1Zw5D', 'loszSdL', 'Doljlq87', '7bs1Cavy', 'islC1Zr3pd', 'vC6voVbml', 'NlATIbqbqH']
          >>> s = lambda p: p == '784e1Zw5D' or p == 'vC6voVbml'
          >>> choose(ps, s, 0)
          '784e1Zw5D'
          >>> choose(ps, s, 1)
          'vC6voVbml'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Gxe', 'aLFptpZ', 'mTk0PqgvEd']
          >>> s = lambda p: p == 'mTk0PqgvEd'
          >>> choose(ps, s, 0)
          'mTk0PqgvEd'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['R', 's5w']
          >>> s = lambda p: p == 'R' or p == 's5w'
          >>> choose(ps, s, 0)
          'R'
          >>> choose(ps, s, 1)
          's5w'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['56ymnsoou', '3SR1BSp9', 'lnDFUseC', 'XX', '5qPAWcVr', 'MagSw', 'OM2']
          >>> s = lambda p: p == '56ymnsoou' or p == 'MagSw' or p == 'lnDFUseC'
          >>> choose(ps, s, 0)
          '56ymnsoou'
          >>> choose(ps, s, 1)
          'lnDFUseC'
          >>> choose(ps, s, 2)
          'MagSw'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['5NB7WkerdL', 'DM7ElcD8', 'Z0jxaWrO']
          >>> s = lambda p: p == '5NB7WkerdL' or p == 'DM7ElcD8'
          >>> choose(ps, s, 0)
          '5NB7WkerdL'
          >>> choose(ps, s, 1)
          'DM7ElcD8'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['dN']
          >>> s = lambda p: p == 'dN'
          >>> choose(ps, s, 0)
          'dN'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['qIe9AKgG', '32', 'L3BZo7']
          >>> s = lambda p: p == '32'
          >>> choose(ps, s, 0)
          '32'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['6rC', 'i', 'ShmGuRlD', 'auTCnLV9N', 'eUm', '3LWePKqsLE', 'UJWaX5', 'YHWXmg8ZKJ']
          >>> s = lambda p: p == 'YHWXmg8ZKJ' or p == 'eUm'
          >>> choose(ps, s, 0)
          'eUm'
          >>> choose(ps, s, 1)
          'YHWXmg8ZKJ'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['rdDBdH1Z2', '4vNQk', 'D9']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['7nb', 'ct0', 'vnXAZmXa', 'Kk']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['nt', 'Kh']
          >>> s = lambda p: p == 'nt'
          >>> choose(ps, s, 0)
          'nt'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['D18', 'cDr', '4tqx', 'T4cu', 'rSMQ', 'QOVBeZ', 'LJEhyyV', 'nN4L', 'sh8yGSN0']
          >>> s = lambda p: p == '4tqx'
          >>> choose(ps, s, 0)
          '4tqx'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['U', 'E', 'xpSt3', 'IBTIrxBn', 'x', '5NHXIC', 'bevi8', 'H2J']
          >>> s = lambda p: p == '5NHXIC' or p == 'E' or p == 'H2J' or p == 'IBTIrxBn' or p == 'bevi8' or p == 'x' or p == 'xpSt3'
          >>> choose(ps, s, 0)
          'E'
          >>> choose(ps, s, 1)
          'xpSt3'
          >>> choose(ps, s, 2)
          'IBTIrxBn'
          >>> choose(ps, s, 3)
          'x'
          >>> choose(ps, s, 4)
          '5NHXIC'
          >>> choose(ps, s, 5)
          'bevi8'
          >>> choose(ps, s, 6)
          'H2J'
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['zKnSYBGR']
          >>> s = lambda p: p == 'zKnSYBGR'
          >>> choose(ps, s, 0)
          'zKnSYBGR'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['qWQ5R', 'itUa']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['vyc99h', 'C2Fb']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['VVfHQc', '3tphSDJHW']
          >>> s = lambda p: p == 'VVfHQc'
          >>> choose(ps, s, 0)
          'VVfHQc'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['6fZ69QtrT', 'w', 'Mj', 'm9Q3q7', 'e8', 'oT91rDgCkf', 'Ku3YY', '1kR7E7o']
          >>> s = lambda p: p == '1kR7E7o' or p == '6fZ69QtrT' or p == 'm9Q3q7' or p == 'oT91rDgCkf'
          >>> choose(ps, s, 0)
          '6fZ69QtrT'
          >>> choose(ps, s, 1)
          'm9Q3q7'
          >>> choose(ps, s, 2)
          'oT91rDgCkf'
          >>> choose(ps, s, 3)
          '1kR7E7o'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['P0GxoIDZ', '1ea7Auf6yr', '4GXri', 'KFEjSWJGo9', 'G4CRHYUS']
          >>> s = lambda p: p == '1ea7Auf6yr' or p == 'G4CRHYUS'
          >>> choose(ps, s, 0)
          '1ea7Auf6yr'
          >>> choose(ps, s, 1)
          'G4CRHYUS'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['WYDL4w', 'h3X', 'eTzA8ZVto']
          >>> s = lambda p: p == 'h3X'
          >>> choose(ps, s, 0)
          'h3X'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['uSdsnZX', 'sm', 'IhETqbyq', 'YyWmeW']
          >>> s = lambda p: p == 'uSdsnZX'
          >>> choose(ps, s, 0)
          'uSdsnZX'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['newpDoQ']
          >>> s = lambda p: p == 'newpDoQ'
          >>> choose(ps, s, 0)
          'newpDoQ'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['39cz9', 'aF4UgswU7', 'nmLtF3C74t', 'O5zVDC0Qk', 'raNMI', 'Ww']
          >>> s = lambda p: p == '39cz9' or p == 'nmLtF3C74t' or p == 'raNMI'
          >>> choose(ps, s, 0)
          '39cz9'
          >>> choose(ps, s, 1)
          'nmLtF3C74t'
          >>> choose(ps, s, 2)
          'raNMI'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['cGYgMJ']
          >>> s = lambda p: p == 'cGYgMJ'
          >>> choose(ps, s, 0)
          'cGYgMJ'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Z6sMzUpX', 'bjZrla', 'd592KutV', 'u9ePqq']
          >>> s = lambda p: p == 'Z6sMzUpX' or p == 'bjZrla'
          >>> choose(ps, s, 0)
          'Z6sMzUpX'
          >>> choose(ps, s, 1)
          'bjZrla'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['CPkMCFSlI', 'hN', '36fjymO']
          >>> s = lambda p: p == 'CPkMCFSlI' or p == 'hN'
          >>> choose(ps, s, 0)
          'CPkMCFSlI'
          >>> choose(ps, s, 1)
          'hN'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['0chTifN', 'zwzztDjl9J', 'sibJYXU3', 'FRBno3fxQ']
          >>> s = lambda p: p == '0chTifN' or p == 'sibJYXU3' or p == 'zwzztDjl9J'
          >>> choose(ps, s, 0)
          '0chTifN'
          >>> choose(ps, s, 1)
          'zwzztDjl9J'
          >>> choose(ps, s, 2)
          'sibJYXU3'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['RyrvEszDL', 'OX', 'l41oGb51', 'K6', 'miYmytdkh0']
          >>> s = lambda p: p == 'miYmytdkh0'
          >>> choose(ps, s, 0)
          'miYmytdkh0'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['x9', '1mTh6V', 'EtQTYbRs']
          >>> s = lambda p: p == '1mTh6V' or p == 'EtQTYbRs'
          >>> choose(ps, s, 0)
          '1mTh6V'
          >>> choose(ps, s, 1)
          'EtQTYbRs'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['4iYIAlSlO', 'XmrFk', 'k', 'kmX', 'Wkc5VlUZ']
          >>> s = lambda p: p == 'Wkc5VlUZ' or p == 'XmrFk' or p == 'kmX'
          >>> choose(ps, s, 0)
          'XmrFk'
          >>> choose(ps, s, 1)
          'kmX'
          >>> choose(ps, s, 2)
          'Wkc5VlUZ'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['dtrqh', 'lw8BciizM', 'HyveF', 'lLhw', 'jZZsxtz', 'fzTVyZ7SA4']
          >>> s = lambda p: p == 'HyveF' or p == 'dtrqh' or p == 'lw8BciizM'
          >>> choose(ps, s, 0)
          'dtrqh'
          >>> choose(ps, s, 1)
          'lw8BciizM'
          >>> choose(ps, s, 2)
          'HyveF'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['9', '2V', 'RApekvN', 'ar6mBR2', 'F0IIQe6', 'tSrWV', 'gWjCn4j']
          >>> s = lambda p: p == '9' or p == 'RApekvN'
          >>> choose(ps, s, 0)
          '9'
          >>> choose(ps, s, 1)
          'RApekvN'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['k', 'Lhx', 'dV', 'qZs']
          >>> s = lambda p: p == 'Lhx'
          >>> choose(ps, s, 0)
          'Lhx'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['AXNQUf', 'kkjB', 'lGMF']
          >>> s = lambda p: p == 'AXNQUf'
          >>> choose(ps, s, 0)
          'AXNQUf'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['H9SPZR', 'P6x9', '0x6iPT8Vp', 'bELQa', 'gDdF', 'd', 'PLlr39R', 'uB3C', 'J']
          >>> s = lambda p: p == 'H9SPZR' or p == 'J' or p == 'P6x9' or p == 'PLlr39R' or p == 'bELQa' or p == 'gDdF'
          >>> choose(ps, s, 0)
          'H9SPZR'
          >>> choose(ps, s, 1)
          'P6x9'
          >>> choose(ps, s, 2)
          'bELQa'
          >>> choose(ps, s, 3)
          'gDdF'
          >>> choose(ps, s, 4)
          'PLlr39R'
          >>> choose(ps, s, 5)
          'J'
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Gbw', '5eTONy', 'r0AifHw', 'kDl', '6EQvhzS2', 'tzT5Qd0', 'Xt5LH']
          >>> s = lambda p: p == 'kDl' or p == 'r0AifHw' or p == 'tzT5Qd0'
          >>> choose(ps, s, 0)
          'r0AifHw'
          >>> choose(ps, s, 1)
          'kDl'
          >>> choose(ps, s, 2)
          'tzT5Qd0'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['T', 'NHHbjxeyg']
          >>> s = lambda p: p == 'T'
          >>> choose(ps, s, 0)
          'T'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['735kD', 'Cydsvguv3', 'aUd1Lh4qll', '2fr', 'orPUSE', 'daD', '9arD', 'YZK']
          >>> s = lambda p: p == '735kD' or p == '9arD' or p == 'Cydsvguv3' or p == 'aUd1Lh4qll' or p == 'daD'
          >>> choose(ps, s, 0)
          '735kD'
          >>> choose(ps, s, 1)
          'Cydsvguv3'
          >>> choose(ps, s, 2)
          'aUd1Lh4qll'
          >>> choose(ps, s, 3)
          'daD'
          >>> choose(ps, s, 4)
          '9arD'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['wTrS1wnYVc']
          >>> s = lambda p: p == 'wTrS1wnYVc'
          >>> choose(ps, s, 0)
          'wTrS1wnYVc'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['O2Z', 'kXg2S', 'iiSLscfD5', 'KQDBr6', 'iy', 'Wl5Y', 'd2K8NvD1d4', 'pTApHl3f', '7GLR9']
          >>> s = lambda p: p == 'Wl5Y' or p == 'd2K8NvD1d4' or p == 'iiSLscfD5' or p == 'iy' or p == 'kXg2S' or p == 'pTApHl3f'
          >>> choose(ps, s, 0)
          'kXg2S'
          >>> choose(ps, s, 1)
          'iiSLscfD5'
          >>> choose(ps, s, 2)
          'iy'
          >>> choose(ps, s, 3)
          'Wl5Y'
          >>> choose(ps, s, 4)
          'd2K8NvD1d4'
          >>> choose(ps, s, 5)
          'pTApHl3f'
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['oM', 'zGYOgEw', 'ueeX', 'D9BVt', 'AAjYFErh4', 'JjCV', '3', '1d7hiLfH']
          >>> s = lambda p: p == '1d7hiLfH' or p == 'AAjYFErh4' or p == 'oM'
          >>> choose(ps, s, 0)
          'oM'
          >>> choose(ps, s, 1)
          'AAjYFErh4'
          >>> choose(ps, s, 2)
          '1d7hiLfH'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['9', 'lFk']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['hDfoY', 'Gx5B', 'j4blx8g', '8KmJf6msa', 'un', 'R', 'onOdPr', 'ABRTPn']
          >>> s = lambda p: p == 'ABRTPn' or p == 'hDfoY' or p == 'onOdPr' or p == 'un'
          >>> choose(ps, s, 0)
          'hDfoY'
          >>> choose(ps, s, 1)
          'un'
          >>> choose(ps, s, 2)
          'onOdPr'
          >>> choose(ps, s, 3)
          'ABRTPn'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['eR', 'i6Bgh134A7', 'DXuD34', 'Cx5jaMth', 'Md8', '4Pf7qA', 'zlrFFuA']
          >>> s = lambda p: p == 'eR' or p == 'i6Bgh134A7' or p == 'zlrFFuA'
          >>> choose(ps, s, 0)
          'eR'
          >>> choose(ps, s, 1)
          'i6Bgh134A7'
          >>> choose(ps, s, 2)
          'zlrFFuA'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['M7lN', '2', 'slZI6', 'C', 'LirWSCzE7L', '76smbBkd9q', 'ahzd740']
          >>> s = lambda p: p == 'C' or p == 'LirWSCzE7L' or p == 'M7lN' or p == 'ahzd740'
          >>> choose(ps, s, 0)
          'M7lN'
          >>> choose(ps, s, 1)
          'C'
          >>> choose(ps, s, 2)
          'LirWSCzE7L'
          >>> choose(ps, s, 3)
          'ahzd740'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['QHKeBnn', 'igEmIdOqfO', 'D1wLx76K', 'ggy', 'FW', 'akXSeF', 'PW', 'PmSZ']
          >>> s = lambda p: p == 'QHKeBnn' or p == 'akXSeF'
          >>> choose(ps, s, 0)
          'QHKeBnn'
          >>> choose(ps, s, 1)
          'akXSeF'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['YVaXL', 'OUqqkf']
          >>> s = lambda p: p == 'OUqqkf' or p == 'YVaXL'
          >>> choose(ps, s, 0)
          'YVaXL'
          >>> choose(ps, s, 1)
          'OUqqkf'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['WsEqFQV', 'H3kSFt', 'tFY']
          >>> s = lambda p: p == 'H3kSFt' or p == 'WsEqFQV' or p == 'tFY'
          >>> choose(ps, s, 0)
          'WsEqFQV'
          >>> choose(ps, s, 1)
          'H3kSFt'
          >>> choose(ps, s, 2)
          'tFY'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['S2E6N']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['Tu6Em', 'HAsg4c', 'nB5LTvR4f5', 'zm', 'gV9jk', 'AqFELMW8g']
          >>> s = lambda p: p == 'AqFELMW8g' or p == 'gV9jk' or p == 'nB5LTvR4f5' or p == 'zm'
          >>> choose(ps, s, 0)
          'nB5LTvR4f5'
          >>> choose(ps, s, 1)
          'zm'
          >>> choose(ps, s, 2)
          'gV9jk'
          >>> choose(ps, s, 3)
          'AqFELMW8g'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['UawKAu']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ps = ['XU9', 'ji0ux', 'N', 'V5jBALIgP', 'g6vdlQ', 'ARqJ', 'rqk58']
          >>> s = lambda p: p == 'ARqJ' or p == 'N' or p == 'V5jBALIgP' or p == 'XU9' or p == 'ji0ux' or p == 'rqk58'
          >>> choose(ps, s, 0)
          'XU9'
          >>> choose(ps, s, 1)
          'ji0ux'
          >>> choose(ps, s, 2)
          'N'
          >>> choose(ps, s, 3)
          'V5jBALIgP'
          >>> choose(ps, s, 4)
          'ARqJ'
          >>> choose(ps, s, 5)
          'rqk58'
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from typing import choose
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
