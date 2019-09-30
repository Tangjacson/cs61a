test = {
  'name': 'Problem 9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p0 = [word_time('START', 0), word_time('What', 0.2), word_time('great', 0.4), word_time('luck', 0.8)]
          >>> p1 = [word_time('START', 0), word_time('What', 0.6), word_time('great', 0.8), word_time('luck', 1.19)]
          >>> fastest_words([p0, p1])
          8e46fe768e646201a51b6caf0ae65fdb
          # locked
          >>> fastest_words([p0, p1], 0.1)  # with a large margin, both typed "luck" the fastest
          c8f4afb99c22926d63b4937678249c68
          # locked
          >>> p2 = [word_time('START', 0), word_time('What', 0.2), word_time('great', 0.3), word_time('luck', 0.6)]
          >>> fastest_words([p0, p1, p2])
          26d9e18fe121bc000bf2abf00214a032
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 44)], [word_time('START', 44)]]
          >>> fastest_words(p, 0.020833333333333332)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 67), word_time('homonymous' , 68.0), word_time('tautit' , 68.2), word_time('misorder' , 68.7)], [word_time('START', 67), word_time('homonymous' , 68.0), word_time('tautit' , 68.33333333333333), word_time('misorder' , 69.33333333333333)]]
          >>> fastest_words(p, 0.014705882352941176)
          [['homonymous', 'tautit', 'misorder'], ['homonymous']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 81), word_time('physiologically' , 82.0), word_time('sidecheck' , 82.25), word_time('exampleless' , 82.75), word_time('ferngrower' , 83.0), word_time('shapeless' , 84.0)], [word_time('START', 81), word_time('physiologically' , 81.33333333333333), word_time('sidecheck' , 82.33333333333333), word_time('exampleless' , 82.58333333333333), word_time('ferngrower' , 82.83333333333333), word_time('shapeless' , 83.33333333333333)]]
          >>> fastest_words(p, 0.02631578947368421)
          [['sidecheck', 'ferngrower'], ['physiologically', 'exampleless', 'ferngrower', 'shapeless']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 9), word_time('vorticose' , 9.25), word_time('obtruncate' , 9.5)]]
          >>> fastest_words(p, 0.017241379310344827)
          [['vorticose', 'obtruncate']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 55)], [word_time('START', 55)], [word_time('START', 55)]]
          >>> fastest_words(p, 0.034482758620689655)
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 0), word_time('punnage' , 0.5), word_time('percesocine' , 0.8333333333333333), word_time('echeneidid' , 1.3333333333333333), word_time('iridiate' , 1.8333333333333333), word_time('conjugality' , 2.083333333333333)], [word_time('START', 0), word_time('punnage' , 0.3333333333333333), word_time('percesocine' , 1.3333333333333333), word_time('echeneidid' , 1.8333333333333333), word_time('iridiate' , 2.333333333333333), word_time('conjugality' , 2.583333333333333)]]
          >>> fastest_words(p, 0.02702702702702703)
          [['percesocine', 'echeneidid', 'iridiate', 'conjugality'], ['punnage', 'echeneidid', 'iridiate', 'conjugality']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 46), word_time('supervisory' , 46.25), word_time('roommates' , 46.45), word_time('psychotic' , 46.650000000000006), word_time('belauder' , 46.85000000000001), word_time('prochlorite' , 47.10000000000001), word_time('adsmithing' , 47.30000000000001)]]
          >>> fastest_words(p, 0.012048192771084338)
          [['supervisory', 'roommates', 'psychotic', 'belauder', 'prochlorite', 'adsmithing']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 52), word_time('reasoner' , 53.0), word_time('presentational' , 53.5), word_time('lanced' , 54.0)]]
          >>> fastest_words(p, 0.012658227848101266)
          [['reasoner', 'presentational', 'lanced']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 35), word_time('taxing' , 35.333333333333336), word_time('electrostenolysis' , 36.333333333333336), word_time('ophthalmorrhagia' , 37.333333333333336), word_time('importableness' , 37.66666666666667), word_time('hairiness' , 38.00000000000001), word_time('hereditivity' , 38.33333333333334)], [word_time('START', 35), word_time('taxing' , 35.333333333333336), word_time('electrostenolysis' , 35.833333333333336), word_time('ophthalmorrhagia' , 36.16666666666667), word_time('importableness' , 36.41666666666667), word_time('hairiness' , 36.66666666666667), word_time('hereditivity' , 37.16666666666667)]]
          >>> fastest_words(p, 0.015384615384615385)
          [['taxing', 'hereditivity'], ['taxing', 'electrostenolysis', 'ophthalmorrhagia', 'importableness', 'hairiness']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 98), word_time('medially' , 98.25), word_time('nonsubstantiation' , 98.58333333333333), word_time('algologist' , 98.91666666666666)], [word_time('START', 98), word_time('medially' , 98.2), word_time('nonsubstantiation' , 98.45), word_time('algologist' , 98.95)], [word_time('START', 98), word_time('medially' , 98.5), word_time('nonsubstantiation' , 99.0), word_time('algologist' , 99.2)]]
          >>> fastest_words(p, 0.015873015873015872)
          [[], ['medially', 'nonsubstantiation'], ['algologist']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 10), word_time('jugful' , 11.0), word_time('goatbrush' , 11.25), word_time('graphite' , 11.583333333333334)]]
          >>> fastest_words(p, 0.011494252873563218)
          [['jugful', 'goatbrush', 'graphite']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 56), word_time('golf' , 56.333333333333336), word_time('impersonatress' , 56.583333333333336), word_time('scirrhoma' , 57.583333333333336), word_time('vaginoscopy' , 58.583333333333336), word_time('harold' , 59.583333333333336)]]
          >>> fastest_words(p, 0.01639344262295082)
          [['golf', 'impersonatress', 'scirrhoma', 'vaginoscopy', 'harold']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 19), word_time('ungrappler' , 19.2), word_time('ascertainer' , 19.45)]]
          >>> fastest_words(p, 0.010416666666666666)
          [['ungrappler', 'ascertainer']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 61), word_time('felineness' , 61.25), word_time('deontological' , 62.25), word_time('extraterrestrial' , 63.25), word_time('experimentalist' , 64.25)]]
          >>> fastest_words(p, 0.06666666666666667)
          [['felineness', 'deontological', 'extraterrestrial', 'experimentalist']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 29), word_time('matchmark' , 29.2)], [word_time('START', 29), word_time('matchmark' , 29.5)], [word_time('START', 29), word_time('matchmark' , 29.25)]]
          >>> fastest_words(p, 0.045454545454545456)
          [['matchmark'], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 33), word_time('draftsman' , 34.0), word_time('nonpurchaser' , 35.0), word_time('shivereens' , 35.5)]]
          >>> fastest_words(p, 0.030303030303030304)
          [['draftsman', 'nonpurchaser', 'shivereens']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 18), word_time('nonabandonment' , 18.5), word_time('grat' , 19.5), word_time('swashbucklery' , 19.833333333333332)], [word_time('START', 18), word_time('nonabandonment' , 18.5), word_time('grat' , 19.5), word_time('swashbucklery' , 19.75)], [word_time('START', 18), word_time('nonabandonment' , 18.2), word_time('grat' , 18.45), word_time('swashbucklery' , 18.78333333333333)]]
          >>> fastest_words(p, 0.024390243902439025)
          [[], ['swashbucklery'], ['nonabandonment', 'grat']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 76), word_time('strippage' , 77.0), word_time('purolymph' , 77.25), word_time('peganite' , 77.58333333333333), word_time('waiterage' , 78.08333333333333), word_time('bogmire' , 78.33333333333333), word_time('hypoploid' , 78.83333333333333)], [word_time('START', 76), word_time('strippage' , 76.2), word_time('purolymph' , 76.4), word_time('peganite' , 76.65), word_time('waiterage' , 76.9), word_time('bogmire' , 77.15), word_time('hypoploid' , 77.65)], [word_time('START', 76), word_time('strippage' , 76.33333333333333), word_time('purolymph' , 77.33333333333333), word_time('peganite' , 77.58333333333333), word_time('waiterage' , 77.78333333333333), word_time('bogmire' , 78.28333333333333), word_time('hypoploid' , 78.53333333333333)]]
          >>> fastest_words(p, 0.027777777777777776)
          [['bogmire'], ['strippage', 'purolymph', 'peganite', 'bogmire'], ['peganite', 'waiterage', 'hypoploid']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 46), word_time('further' , 46.5), word_time('monoazo' , 46.833333333333336), word_time('otidium' , 47.833333333333336), word_time('outbetter' , 48.083333333333336)], [word_time('START', 46), word_time('further' , 46.2), word_time('monoazo' , 47.2), word_time('otidium' , 47.400000000000006), word_time('outbetter' , 47.73333333333334)], [word_time('START', 46), word_time('further' , 46.333333333333336), word_time('monoazo' , 46.833333333333336), word_time('otidium' , 47.833333333333336), word_time('outbetter' , 48.833333333333336)]]
          >>> fastest_words(p, 0.01098901098901099)
          [['monoazo', 'outbetter'], ['further', 'otidium'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 62), word_time('donnert' , 63.0)], [word_time('START', 62), word_time('donnert' , 62.25)]]
          >>> fastest_words(p, 0.1111111111111111)
          [[], ['donnert']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 91), word_time('microcephalic' , 91.2), word_time('coauthor' , 91.45), word_time('whorishness' , 91.78333333333333), word_time('disable' , 92.28333333333333)]]
          >>> fastest_words(p, 0.024390243902439025)
          [['microcephalic', 'coauthor', 'whorishness', 'disable']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 33), word_time('uphelya' , 33.2), word_time('argentose' , 33.45), word_time('pedaliter' , 33.95), word_time('ramequin' , 34.150000000000006), word_time('rehoist' , 34.400000000000006)], [word_time('START', 33), word_time('uphelya' , 33.333333333333336), word_time('argentose' , 33.583333333333336), word_time('pedaliter' , 33.91666666666667), word_time('ramequin' , 34.16666666666667), word_time('rehoist' , 34.66666666666667)]]
          >>> fastest_words(p, 0.05263157894736842)
          [['uphelya', 'argentose', 'ramequin', 'rehoist'], ['argentose', 'pedaliter', 'ramequin']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 41), word_time('concresce' , 41.2), word_time('herne' , 41.7), word_time('irreclaimableness' , 42.7), word_time('granose' , 43.7), word_time('happiest' , 43.95)], [word_time('START', 41), word_time('concresce' , 41.25), word_time('herne' , 41.583333333333336), word_time('irreclaimableness' , 41.91666666666667), word_time('granose' , 42.116666666666674), word_time('happiest' , 43.116666666666674)], [word_time('START', 41), word_time('concresce' , 41.5), word_time('herne' , 42.5), word_time('irreclaimableness' , 42.7), word_time('granose' , 42.95), word_time('happiest' , 43.95)]]
          >>> fastest_words(p, 0.010638297872340425)
          [['concresce', 'happiest'], ['herne', 'granose'], ['irreclaimableness']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 91)], [word_time('START', 91)], [word_time('START', 91)]]
          >>> fastest_words(p, 0.010638297872340425)
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 19), word_time('nonintoxicant' , 19.2), word_time('cernuous' , 19.45)], [word_time('START', 19), word_time('nonintoxicant' , 20.0), word_time('cernuous' , 20.2)]]
          >>> fastest_words(p, 0.0136986301369863)
          [['nonintoxicant'], ['cernuous']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 36), word_time('unshewed' , 36.2), word_time('quadrans' , 36.400000000000006)]]
          >>> fastest_words(p, 0.038461538461538464)
          [['unshewed', 'quadrans']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 82), word_time('reappointment' , 83.0), word_time('crozzly' , 83.25), word_time('bullneck' , 83.58333333333333)], [word_time('START', 82), word_time('reappointment' , 83.0), word_time('crozzly' , 83.2), word_time('bullneck' , 83.53333333333333)], [word_time('START', 82), word_time('reappointment' , 83.0), word_time('crozzly' , 83.2), word_time('bullneck' , 83.4)]]
          >>> fastest_words(p, 0.014492753623188406)
          [['reappointment'], ['reappointment', 'crozzly'], ['reappointment', 'crozzly', 'bullneck']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 49), word_time('pharyngoceratosis' , 49.333333333333336), word_time('crackerjack' , 49.53333333333334)], [word_time('START', 49), word_time('pharyngoceratosis' , 49.25), word_time('crackerjack' , 49.45)]]
          >>> fastest_words(p, 0.010869565217391304)
          [['crackerjack'], ['pharyngoceratosis', 'crackerjack']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 18), word_time('tarrass' , 18.333333333333332), word_time('unrhythmical' , 18.583333333333332), word_time('unmovable' , 19.083333333333332), word_time('brad' , 19.583333333333332), word_time('antigravitational' , 20.083333333333332), word_time('allopsychic' , 21.083333333333332)], [word_time('START', 18), word_time('tarrass' , 18.2), word_time('unrhythmical' , 18.53333333333333), word_time('unmovable' , 18.866666666666664), word_time('brad' , 19.066666666666663), word_time('antigravitational' , 20.066666666666663), word_time('allopsychic' , 21.066666666666663)]]
          >>> fastest_words(p, 0.021739130434782608)
          [['unrhythmical', 'antigravitational', 'allopsychic'], ['tarrass', 'unmovable', 'brad', 'allopsychic']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 22)], [word_time('START', 22)]]
          >>> fastest_words(p, 0.0125)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 99), word_time('lipomata' , 100.0), word_time('halitus' , 101.0), word_time('intradepartmental' , 101.2), word_time('overappraise' , 101.7)], [word_time('START', 99), word_time('lipomata' , 99.33333333333333), word_time('halitus' , 99.53333333333333), word_time('intradepartmental' , 99.73333333333333), word_time('overappraise' , 100.23333333333333)]]
          >>> fastest_words(p, 0.14285714285714285)
          [['intradepartmental', 'overappraise'], ['lipomata', 'halitus', 'intradepartmental', 'overappraise']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 20), word_time('conjunctiva' , 20.25)], [word_time('START', 20), word_time('conjunctiva' , 20.5)]]
          >>> fastest_words(p, 0.01020408163265306)
          [['conjunctiva'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 53), word_time('outscent' , 54.0), word_time('exoascaceous' , 54.2), word_time('hexamethylenetetramine' , 54.53333333333334), word_time('bolsterer' , 54.73333333333334), word_time('chloral' , 55.73333333333334), word_time('parao' , 55.98333333333334)], [word_time('START', 53), word_time('outscent' , 53.2), word_time('exoascaceous' , 54.2), word_time('hexamethylenetetramine' , 54.7), word_time('bolsterer' , 54.900000000000006), word_time('chloral' , 55.23333333333334), word_time('parao' , 55.48333333333334)], [word_time('START', 53), word_time('outscent' , 53.5), word_time('exoascaceous' , 53.75), word_time('hexamethylenetetramine' , 53.95), word_time('bolsterer' , 54.95), word_time('chloral' , 55.95), word_time('parao' , 56.150000000000006)]]
          >>> fastest_words(p, 0.019230769230769232)
          [['exoascaceous', 'bolsterer'], ['outscent', 'bolsterer', 'chloral'], ['hexamethylenetetramine', 'parao']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 70), word_time('antistrophal' , 70.33333333333333), word_time('sternopericardiac' , 70.83333333333333), word_time('increpate' , 71.16666666666666)]]
          >>> fastest_words(p, 0.1)
          [['antistrophal', 'sternopericardiac', 'increpate']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 98), word_time('deferentially' , 99.0), word_time('allotrophic' , 99.33333333333333), word_time('terpodion' , 99.53333333333333), word_time('wintertide' , 99.78333333333333)]]
          >>> fastest_words(p, 0.01020408163265306)
          [['deferentially', 'allotrophic', 'terpodion', 'wintertide']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 69), word_time('airworthy' , 69.2)], [word_time('START', 69), word_time('airworthy' , 69.2)], [word_time('START', 69), word_time('airworthy' , 69.33333333333333)]]
          >>> fastest_words(p, 0.14285714285714285)
          [['airworthy'], ['airworthy'], ['airworthy']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 96), word_time('malinowskite' , 96.25), word_time('bullet' , 96.45), word_time('pseudaposporous' , 96.65), word_time('congener' , 97.65), word_time('nonvisceral' , 97.9)], [word_time('START', 96), word_time('malinowskite' , 96.25), word_time('bullet' , 96.5), word_time('pseudaposporous' , 96.75), word_time('congener' , 97.0), word_time('nonvisceral' , 97.5)]]
          >>> fastest_words(p, 0.019230769230769232)
          [['malinowskite', 'bullet', 'pseudaposporous', 'nonvisceral'], ['malinowskite', 'congener']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 83), word_time('iconodulic' , 84.0), word_time('airmonger' , 84.5), word_time('superacknowledgment' , 84.75), word_time('pneumolysis' , 85.0), word_time('forestish' , 85.25)], [word_time('START', 83), word_time('iconodulic' , 83.25), word_time('airmonger' , 83.58333333333333), word_time('superacknowledgment' , 83.91666666666666), word_time('pneumolysis' , 84.91666666666666), word_time('forestish' , 85.24999999999999)]]
          >>> fastest_words(p, 0.125)
          [['superacknowledgment', 'pneumolysis', 'forestish'], ['iconodulic', 'airmonger', 'superacknowledgment', 'forestish']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 78), word_time('caxiri' , 78.25)], [word_time('START', 78), word_time('caxiri' , 78.5)], [word_time('START', 78), word_time('caxiri' , 78.33333333333333)]]
          >>> fastest_words(p, 0.030303030303030304)
          [['caxiri'], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 45), word_time('untripe' , 45.5), word_time('canellaceous' , 46.0), word_time('septangle' , 46.5), word_time('epuloid' , 46.833333333333336), word_time('bandwidth' , 47.333333333333336)], [word_time('START', 45), word_time('untripe' , 45.2), word_time('canellaceous' , 45.400000000000006), word_time('septangle' , 45.73333333333334), word_time('epuloid' , 45.98333333333334), word_time('bandwidth' , 46.31666666666668)]]
          >>> fastest_words(p, 0.2)
          [['septangle', 'epuloid', 'bandwidth'], ['untripe', 'canellaceous', 'septangle', 'epuloid', 'bandwidth']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 55), word_time('refledge' , 55.2), word_time('irrigative' , 56.2), word_time('enterosyphilis' , 56.7), word_time('revengement' , 56.900000000000006), word_time('isodiametrical' , 57.23333333333334), word_time('amylin' , 57.48333333333334)], [word_time('START', 55), word_time('refledge' , 55.333333333333336), word_time('irrigative' , 55.66666666666667), word_time('enterosyphilis' , 55.91666666666667), word_time('revengement' , 56.41666666666667), word_time('isodiametrical' , 56.75000000000001), word_time('amylin' , 56.95000000000001)], [word_time('START', 55), word_time('refledge' , 56.0), word_time('irrigative' , 56.25), word_time('enterosyphilis' , 56.583333333333336), word_time('revengement' , 57.083333333333336), word_time('isodiametrical' , 57.28333333333334), word_time('amylin' , 57.616666666666674)]]
          >>> fastest_words(p, 0.037037037037037035)
          [['refledge', 'revengement'], ['enterosyphilis', 'amylin'], ['irrigative', 'isodiametrical']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 46), word_time('shareholdership' , 47.0)], [word_time('START', 46), word_time('shareholdership' , 46.5)], [word_time('START', 46), word_time('shareholdership' , 47.0)]]
          >>> fastest_words(p, 0.010638297872340425)
          [[], ['shareholdership'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 66), word_time('windflaw' , 66.25), word_time('physicomorphism' , 67.25)], [word_time('START', 66), word_time('windflaw' , 67.0), word_time('physicomorphism' , 67.5)]]
          >>> fastest_words(p, 0.0136986301369863)
          [['windflaw'], ['physicomorphism']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 64), word_time('underspar' , 64.2), word_time('voeten' , 64.45)]]
          >>> fastest_words(p, 0.014285714285714285)
          [['underspar', 'voeten']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 83), word_time('leafboy' , 83.2), word_time('quadrisyllabous' , 83.4), word_time('petalwise' , 83.65), word_time('subtext' , 84.65)], [word_time('START', 83), word_time('leafboy' , 83.25), word_time('quadrisyllabous' , 83.5), word_time('petalwise' , 83.75), word_time('subtext' , 84.25)], [word_time('START', 83), word_time('leafboy' , 83.5), word_time('quadrisyllabous' , 84.0), word_time('petalwise' , 84.33333333333333), word_time('subtext' , 85.33333333333333)]]
          >>> fastest_words(p, 0.011235955056179775)
          [['leafboy', 'quadrisyllabous', 'petalwise'], ['petalwise', 'subtext'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 25), word_time('childed' , 26.0), word_time('peoplehood' , 26.333333333333332), word_time('foxwood' , 26.666666666666664), word_time('brachistochronic' , 27.166666666666664), word_time('dentilation' , 27.666666666666664)], [word_time('START', 25), word_time('childed' , 25.25), word_time('peoplehood' , 25.5), word_time('foxwood' , 25.833333333333332), word_time('brachistochronic' , 26.083333333333332), word_time('dentilation' , 26.333333333333332)]]
          >>> fastest_words(p, 0.02631578947368421)
          [['foxwood'], ['childed', 'peoplehood', 'foxwood', 'brachistochronic', 'dentilation']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 78), word_time('pathfinding' , 79.0), word_time('teretish' , 80.0)], [word_time('START', 78), word_time('pathfinding' , 78.25), word_time('teretish' , 78.45)]]
          >>> fastest_words(p, 0.012048192771084338)
          [[], ['pathfinding', 'teretish']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 58), word_time('seatrain' , 58.5)]]
          >>> fastest_words(p, 0.02)
          [['seatrain']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 78), word_time('outshut' , 78.5), word_time('pali' , 78.7), word_time('colocolic' , 79.03333333333333)], [word_time('START', 78), word_time('outshut' , 78.5), word_time('pali' , 79.5), word_time('colocolic' , 79.75)]]
          >>> fastest_words(p, 0.125)
          [['outshut', 'pali', 'colocolic'], ['outshut', 'colocolic']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 87), word_time('obispo' , 87.5), word_time('sarrusophone' , 88.0)], [word_time('START', 87), word_time('obispo' , 88.0), word_time('sarrusophone' , 88.33333333333333)], [word_time('START', 87), word_time('obispo' , 87.2), word_time('sarrusophone' , 87.4)]]
          >>> fastest_words(p, 0.038461538461538464)
          [[], [], ['obispo', 'sarrusophone']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 7), word_time('flandan' , 7.333333333333333), word_time('adulterous' , 7.583333333333333), word_time('coascend' , 8.083333333333332), word_time('unperpetrated' , 8.416666666666666)]]
          >>> fastest_words(p, 0.25)
          [['flandan', 'adulterous', 'coascend', 'unperpetrated']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 49), word_time('yesteryear' , 50.0), word_time('mesotonic' , 50.2), word_time('chattelhood' , 51.2), word_time('extrusive' , 51.53333333333334)], [word_time('START', 49), word_time('yesteryear' , 49.333333333333336), word_time('mesotonic' , 49.66666666666667), word_time('chattelhood' , 50.00000000000001), word_time('extrusive' , 50.20000000000001)], [word_time('START', 49), word_time('yesteryear' , 49.333333333333336), word_time('mesotonic' , 49.53333333333334), word_time('chattelhood' , 50.03333333333334), word_time('extrusive' , 50.23333333333334)]]
          >>> fastest_words(p, 0.03333333333333333)
          [['mesotonic'], ['yesteryear', 'chattelhood', 'extrusive'], ['yesteryear', 'mesotonic', 'extrusive']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 89), word_time('coatie' , 89.2)]]
          >>> fastest_words(p, 0.01098901098901099)
          [['coatie']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 97), word_time('freshet' , 97.5), word_time('epiphloeum' , 97.83333333333333)]]
          >>> fastest_words(p, 0.02631578947368421)
          [['freshet', 'epiphloeum']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 88), word_time('uliginous' , 88.25), word_time('purposes' , 88.45), word_time('tapadero' , 89.45), word_time('blepharochromidrosis' , 89.78333333333333), word_time('foraminule' , 90.03333333333333), word_time('acronymic' , 90.23333333333333)]]
          >>> fastest_words(p, 0.012048192771084338)
          [['uliginous', 'purposes', 'tapadero', 'blepharochromidrosis', 'foraminule', 'acronymic']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 83)], [word_time('START', 83)], [word_time('START', 83)]]
          >>> fastest_words(p, 0.021739130434782608)
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 10), word_time('stoical' , 10.25), word_time('spermatocyst' , 10.583333333333334), word_time('outquestion' , 11.583333333333334)], [word_time('START', 10), word_time('stoical' , 10.333333333333334), word_time('spermatocyst' , 10.533333333333333), word_time('outquestion' , 10.733333333333333)], [word_time('START', 10), word_time('stoical' , 10.333333333333334), word_time('spermatocyst' , 10.583333333333334), word_time('outquestion' , 11.083333333333334)]]
          >>> fastest_words(p, 0.014705882352941176)
          [['stoical'], ['spermatocyst', 'outquestion'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 66), word_time('prepubescent' , 66.33333333333333), word_time('indigenist' , 66.58333333333333), word_time('kobold' , 66.91666666666666), word_time('serene' , 67.24999999999999), word_time('samel' , 67.58333333333331), word_time('dusting' , 67.83333333333331)]]
          >>> fastest_words(p, 0.01020408163265306)
          [['prepubescent', 'indigenist', 'kobold', 'serene', 'samel', 'dusting']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 2), word_time('rendered' , 3.0)], [word_time('START', 2), word_time('rendered' , 2.2)]]
          >>> fastest_words(p, 0.012987012987012988)
          [[], ['rendered']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 53), word_time('strette' , 53.5), word_time('yolk' , 54.0), word_time('subolive' , 55.0), word_time('graduateship' , 55.5)], [word_time('START', 53), word_time('strette' , 53.2), word_time('yolk' , 53.400000000000006), word_time('subolive' , 53.73333333333334), word_time('graduateship' , 54.73333333333334)], [word_time('START', 53), word_time('strette' , 53.2), word_time('yolk' , 54.2), word_time('subolive' , 54.45), word_time('graduateship' , 55.45)]]
          >>> fastest_words(p, 0.015151515151515152)
          [['graduateship'], ['strette', 'yolk'], ['strette', 'subolive']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 80), word_time('dorsothoracic' , 81.0), word_time('roundridge' , 81.2)], [word_time('START', 80), word_time('dorsothoracic' , 80.33333333333333), word_time('roundridge' , 80.58333333333333)], [word_time('START', 80), word_time('dorsothoracic' , 80.25), word_time('roundridge' , 80.45)]]
          >>> fastest_words(p, 0.030303030303030304)
          [['roundridge'], [], ['dorsothoracic', 'roundridge']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 5), word_time('sprightliness' , 5.2), word_time('seconder' , 6.2)]]
          >>> fastest_words(p, 0.010752688172043012)
          [['sprightliness', 'seconder']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 29), word_time('celiosalpingotomy' , 29.5), word_time('naut' , 30.5), word_time('porcellanize' , 31.0), word_time('abiosis' , 31.2)], [word_time('START', 29), word_time('celiosalpingotomy' , 29.2), word_time('naut' , 30.2), word_time('porcellanize' , 30.7), word_time('abiosis' , 31.2)], [word_time('START', 29), word_time('celiosalpingotomy' , 29.2), word_time('naut' , 30.2), word_time('porcellanize' , 30.7), word_time('abiosis' , 30.9)]]
          >>> fastest_words(p, 1.0)
          [['celiosalpingotomy', 'naut', 'porcellanize', 'abiosis'], ['celiosalpingotomy', 'naut', 'porcellanize', 'abiosis'], ['celiosalpingotomy', 'naut', 'porcellanize', 'abiosis']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 16), word_time('forestside' , 16.333333333333332), word_time('sindle' , 16.666666666666664), word_time('clericate' , 16.999999999999996)], [word_time('START', 16), word_time('forestside' , 17.0), word_time('sindle' , 17.25), word_time('clericate' , 17.75)], [word_time('START', 16), word_time('forestside' , 16.25), word_time('sindle' , 16.583333333333332), word_time('clericate' , 16.833333333333332)]]
          >>> fastest_words(p, 0.013888888888888888)
          [[], ['sindle'], ['forestside', 'clericate']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 71), word_time('roisterly' , 71.25), word_time('unmasking' , 72.25), word_time('benzdiazine' , 73.25), word_time('developmentist' , 73.75), word_time('biseriate' , 73.95)]]
          >>> fastest_words(p, 0.016666666666666666)
          [['roisterly', 'unmasking', 'benzdiazine', 'developmentist', 'biseriate']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 1)], [word_time('START', 1)]]
          >>> fastest_words(p, 0.03333333333333333)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 40), word_time('cockpit' , 40.333333333333336), word_time('nonconcurrency' , 40.53333333333334), word_time('unhooded' , 41.53333333333334)], [word_time('START', 40), word_time('cockpit' , 40.25), word_time('nonconcurrency' , 40.583333333333336), word_time('unhooded' , 40.78333333333334)], [word_time('START', 40), word_time('cockpit' , 40.25), word_time('nonconcurrency' , 40.75), word_time('unhooded' , 41.25)]]
          >>> fastest_words(p, 0.043478260869565216)
          [['nonconcurrency'], ['cockpit', 'unhooded'], ['cockpit']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 51), word_time('slifter' , 51.25), word_time('nourishingly' , 52.25), word_time('conceivability' , 52.75), word_time('deltidium' , 53.25), word_time('megaphonic' , 54.25), word_time('isovaline' , 54.5)], [word_time('START', 51), word_time('slifter' , 51.2), word_time('nourishingly' , 52.2), word_time('conceivability' , 52.7), word_time('deltidium' , 53.2), word_time('megaphonic' , 53.45), word_time('isovaline' , 53.7)], [word_time('START', 51), word_time('slifter' , 51.5), word_time('nourishingly' , 51.833333333333336), word_time('conceivability' , 52.833333333333336), word_time('deltidium' , 53.833333333333336), word_time('megaphonic' , 54.083333333333336), word_time('isovaline' , 54.583333333333336)]]
          >>> fastest_words(p, 0.024390243902439025)
          [['conceivability', 'deltidium', 'isovaline'], ['slifter', 'conceivability', 'deltidium', 'megaphonic', 'isovaline'], ['nourishingly', 'megaphonic']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 7), word_time('noncommissioned' , 7.333333333333333), word_time('fatally' , 8.333333333333332), word_time('incretionary' , 8.666666666666666), word_time('unhaggled' , 8.866666666666665), word_time('mastooccipital' , 9.366666666666665), word_time('unfading' , 9.616666666666665)]]
          >>> fastest_words(p, 0.037037037037037035)
          [['noncommissioned', 'fatally', 'incretionary', 'unhaggled', 'mastooccipital', 'unfading']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 36), word_time('spout' , 36.5), word_time('atelomitic' , 37.0), word_time('halidom' , 37.333333333333336), word_time('characterologist' , 37.583333333333336), word_time('itemy' , 37.78333333333334), word_time('rashlike' , 38.116666666666674)], [word_time('START', 36), word_time('spout' , 36.2), word_time('atelomitic' , 37.2), word_time('halidom' , 37.45), word_time('characterologist' , 37.7), word_time('itemy' , 38.2), word_time('rashlike' , 38.53333333333334)]]
          >>> fastest_words(p, 0.16666666666666666)
          [['atelomitic', 'halidom', 'characterologist', 'itemy', 'rashlike'], ['spout', 'halidom', 'characterologist', 'rashlike']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 21), word_time('anormal' , 21.2), word_time('arcane' , 21.53333333333333)], [word_time('START', 21), word_time('anormal' , 21.2), word_time('arcane' , 21.45)], [word_time('START', 21), word_time('anormal' , 21.2), word_time('arcane' , 21.53333333333333)]]
          >>> fastest_words(p, 0.047619047619047616)
          [['anormal'], ['anormal', 'arcane'], ['anormal']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 97), word_time('skeletogenous' , 97.5), word_time('stickful' , 98.5), word_time('lime' , 98.75)]]
          >>> fastest_words(p, 0.05)
          [['skeletogenous', 'stickful', 'lime']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 16), word_time('conn' , 16.333333333333332), word_time('jungle' , 16.53333333333333), word_time('tardy' , 16.78333333333333)], [word_time('START', 16), word_time('conn' , 16.5), word_time('jungle' , 16.75), word_time('tardy' , 17.25)], [word_time('START', 16), word_time('conn' , 16.25), word_time('jungle' , 16.75), word_time('tardy' , 17.0)]]
          >>> fastest_words(p, 0.041666666666666664)
          [['jungle', 'tardy'], [], ['conn', 'tardy']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 67)], [word_time('START', 67)], [word_time('START', 67)]]
          >>> fastest_words(p, 0.01282051282051282)
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 68), word_time('loverwise' , 68.2), word_time('agamically' , 68.45), word_time('morphophyly' , 68.7), word_time('unintoxicating' , 68.9), word_time('transischiac' , 69.15)], [word_time('START', 68), word_time('loverwise' , 68.25), word_time('agamically' , 68.75), word_time('morphophyly' , 69.75), word_time('unintoxicating' , 70.0), word_time('transischiac' , 70.5)]]
          >>> fastest_words(p, 0.011494252873563218)
          [['loverwise', 'agamically', 'morphophyly', 'unintoxicating', 'transischiac'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 18)]]
          >>> fastest_words(p, 0.018518518518518517)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 85)], [word_time('START', 85)]]
          >>> fastest_words(p, 0.011235955056179775)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 82), word_time('dramatist' , 83.0), word_time('ridiculize' , 83.2), word_time('undeclaiming' , 83.53333333333333), word_time('pantaloonery' , 84.03333333333333), word_time('trifurcation' , 84.23333333333333)]]
          >>> fastest_words(p, 0.08333333333333333)
          [['dramatist', 'ridiculize', 'undeclaiming', 'pantaloonery', 'trifurcation']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 11), word_time('asmalte' , 12.0), word_time('oversensitive' , 12.2), word_time('surnay' , 12.533333333333333), word_time('multistoried' , 13.533333333333333), word_time('mesopodiale' , 13.783333333333333)], [word_time('START', 11), word_time('asmalte' , 11.5), word_time('oversensitive' , 12.5), word_time('surnay' , 12.75), word_time('multistoried' , 12.95), word_time('mesopodiale' , 13.2)], [word_time('START', 11), word_time('asmalte' , 11.5), word_time('oversensitive' , 12.5), word_time('surnay' , 12.833333333333334), word_time('multistoried' , 13.833333333333334), word_time('mesopodiale' , 14.333333333333334)]]
          >>> fastest_words(p, 0.038461538461538464)
          [['oversensitive', 'mesopodiale'], ['asmalte', 'surnay', 'multistoried', 'mesopodiale'], ['asmalte']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 12), word_time('cliffed' , 13.0), word_time('infrigidate' , 14.0), word_time('euphemizer' , 14.333333333333334), word_time('curare' , 14.533333333333333)], [word_time('START', 12), word_time('cliffed' , 12.5), word_time('infrigidate' , 12.75), word_time('euphemizer' , 13.083333333333334), word_time('curare' , 13.333333333333334)], [word_time('START', 12), word_time('cliffed' , 12.333333333333334), word_time('infrigidate' , 12.583333333333334), word_time('euphemizer' , 13.083333333333334), word_time('curare' , 14.083333333333334)]]
          >>> fastest_words(p, 0.021739130434782608)
          [['euphemizer', 'curare'], ['infrigidate', 'euphemizer'], ['cliffed', 'infrigidate']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 57), word_time('antiodontalgic' , 57.2), word_time('phonophile' , 57.45), word_time('foreshorten' , 57.7), word_time('despoilment' , 57.900000000000006)]]
          >>> fastest_words(p, 0.01694915254237288)
          [['antiodontalgic', 'phonophile', 'foreshorten', 'despoilment']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 15), word_time('piliferous' , 15.5), word_time('hydrazidine' , 16.0), word_time('insurgent' , 16.5), word_time('haemathermal' , 17.5), word_time('chunnia' , 18.0), word_time('overprovidently' , 19.0)], [word_time('START', 15), word_time('piliferous' , 15.5), word_time('hydrazidine' , 16.5), word_time('insurgent' , 16.833333333333332), word_time('haemathermal' , 17.166666666666664), word_time('chunnia' , 17.366666666666664), word_time('overprovidently' , 17.566666666666663)]]
          >>> fastest_words(p, 0.011363636363636364)
          [['piliferous', 'hydrazidine'], ['piliferous', 'insurgent', 'haemathermal', 'chunnia', 'overprovidently']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 22), word_time('duplicand' , 22.333333333333332), word_time('loxotomy' , 22.53333333333333)], [word_time('START', 22), word_time('duplicand' , 23.0), word_time('loxotomy' , 23.25)], [word_time('START', 22), word_time('duplicand' , 22.333333333333332), word_time('loxotomy' , 22.833333333333332)]]
          >>> fastest_words(p, 0.0125)
          [['duplicand', 'loxotomy'], [], ['duplicand']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 27), word_time('unpacified' , 27.25), word_time('reaffirmance' , 27.45), word_time('nursy' , 27.95), word_time('polycotyledony' , 28.45)], [word_time('START', 27), word_time('unpacified' , 27.25), word_time('reaffirmance' , 27.5), word_time('nursy' , 28.5), word_time('polycotyledony' , 29.5)], [word_time('START', 27), word_time('unpacified' , 27.333333333333332), word_time('reaffirmance' , 27.53333333333333), word_time('nursy' , 28.53333333333333), word_time('polycotyledony' , 28.78333333333333)]]
          >>> fastest_words(p, 0.02040816326530612)
          [['unpacified', 'reaffirmance', 'nursy'], ['unpacified'], ['reaffirmance', 'polycotyledony']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 21)], [word_time('START', 21)], [word_time('START', 21)]]
          >>> fastest_words(p, 0.010526315789473684)
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 17), word_time('deadish' , 17.25), word_time('brevirostral' , 17.583333333333332), word_time('propagandism' , 17.916666666666664)], [word_time('START', 17), word_time('deadish' , 18.0), word_time('brevirostral' , 18.2), word_time('propagandism' , 18.4)]]
          >>> fastest_words(p, 0.09090909090909091)
          [['deadish'], ['brevirostral', 'propagandism']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 6), word_time('cyanophycean' , 7.0), word_time('photoradio' , 7.2), word_time('vility' , 7.533333333333333), word_time('copellidine' , 7.733333333333333), word_time('creditor' , 8.733333333333334), word_time('parvenuism' , 8.933333333333334)], [word_time('START', 6), word_time('cyanophycean' , 7.0), word_time('photoradio' , 7.333333333333333), word_time('vility' , 7.833333333333333), word_time('copellidine' , 8.833333333333332), word_time('creditor' , 9.083333333333332), word_time('parvenuism' , 9.283333333333331)]]
          >>> fastest_words(p, 0.030303030303030304)
          [['cyanophycean', 'photoradio', 'vility', 'copellidine', 'parvenuism'], ['cyanophycean', 'creditor', 'parvenuism']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 32)], [word_time('START', 32)]]
          >>> fastest_words(p, 0.011764705882352941)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 0), word_time('sangrel' , 0.3333333333333333), word_time('untile' , 0.5333333333333333), word_time('edgy' , 1.5333333333333332), word_time('cathedra' , 2.033333333333333)], [word_time('START', 0), word_time('sangrel' , 0.2), word_time('untile' , 0.7), word_time('edgy' , 0.8999999999999999), word_time('cathedra' , 1.0999999999999999)]]
          >>> fastest_words(p, 0.011764705882352941)
          [['untile'], ['sangrel', 'edgy', 'cathedra']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 80), word_time('harborless' , 80.5), word_time('autotropism' , 81.0), word_time('hydroseparation' , 81.2), word_time('descry' , 81.4), word_time('apodosis' , 81.60000000000001), word_time('atavist' , 81.85000000000001)], [word_time('START', 80), word_time('harborless' , 81.0), word_time('autotropism' , 81.2), word_time('hydroseparation' , 81.45), word_time('descry' , 81.7), word_time('apodosis' , 82.03333333333333), word_time('atavist' , 82.23333333333333)]]
          >>> fastest_words(p, 0.012048192771084338)
          [['harborless', 'hydroseparation', 'descry', 'apodosis'], ['autotropism', 'atavist']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 35), word_time('aggrandizer' , 35.25), word_time('unindentable' , 35.75), word_time('dicer' , 36.0)], [word_time('START', 35), word_time('aggrandizer' , 35.25), word_time('unindentable' , 35.5), word_time('dicer' , 35.7)]]
          >>> fastest_words(p, 0.06666666666666667)
          [['aggrandizer', 'dicer'], ['aggrandizer', 'unindentable', 'dicer']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 56), word_time('herolike' , 56.333333333333336), word_time('indisputableness' , 57.333333333333336)], [word_time('START', 56), word_time('herolike' , 57.0), word_time('indisputableness' , 58.0)], [word_time('START', 56), word_time('herolike' , 56.333333333333336), word_time('indisputableness' , 56.53333333333334)]]
          >>> fastest_words(p, 0.045454545454545456)
          [['herolike'], [], ['herolike', 'indisputableness']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 98), word_time('peritrochal' , 98.2), word_time('seambiter' , 98.4), word_time('cogman' , 98.73333333333333)], [word_time('START', 98), word_time('peritrochal' , 98.33333333333333), word_time('seambiter' , 98.83333333333333), word_time('cogman' , 99.08333333333333)]]
          >>> fastest_words(p, 0.07142857142857142)
          [['peritrochal', 'seambiter'], ['cogman']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 12), word_time('proavian' , 12.333333333333334), word_time('telekinetic' , 12.533333333333333), word_time('unpeople' , 12.783333333333333), word_time('unimprovable' , 12.983333333333333)], [word_time('START', 12), word_time('proavian' , 12.333333333333334), word_time('telekinetic' , 12.833333333333334), word_time('unpeople' , 13.333333333333334), word_time('unimprovable' , 13.833333333333334)]]
          >>> fastest_words(p, 0.015384615384615385)
          [['proavian', 'telekinetic', 'unpeople', 'unimprovable'], ['proavian']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 15), word_time('conscript' , 15.25), word_time('pectoriloquy' , 15.5), word_time('nonsympathizer' , 15.7), word_time('unrenowned' , 16.7), word_time('upmaking' , 16.9)], [word_time('START', 15), word_time('conscript' , 16.0), word_time('pectoriloquy' , 17.0), word_time('nonsympathizer' , 17.25), word_time('unrenowned' , 17.583333333333332), word_time('upmaking' , 17.833333333333332)]]
          >>> fastest_words(p, 0.05263157894736842)
          [['conscript', 'pectoriloquy', 'nonsympathizer', 'upmaking'], ['nonsympathizer', 'unrenowned', 'upmaking']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 81), word_time('hyponeuria' , 81.33333333333333), word_time('affectate' , 81.53333333333333)], [word_time('START', 81), word_time('hyponeuria' , 82.0), word_time('affectate' , 82.25)], [word_time('START', 81), word_time('hyponeuria' , 81.25), word_time('affectate' , 81.5)]]
          >>> fastest_words(p, 0.022222222222222223)
          [['affectate'], [], ['hyponeuria']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 30)]]
          >>> fastest_words(p, 0.125)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 15)], [word_time('START', 15)]]
          >>> fastest_words(p, 0.09090909090909091)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 18)]]
          >>> fastest_words(p, 0.013888888888888888)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[word_time('START', 32)]]
          >>> fastest_words(p, 0.025)
          [[]]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from typing import word_time, fastest_words
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> test.swap_implementations(typing)
          >>> p0 = [typing.word_time('START', 0), typing.word_time('What', 0.2), typing.word_time('great', 0.4), typing.word_time('luck', 0.8)]
          >>> p1 = [typing.word_time('START', 0), typing.word_time('What', 0.6), typing.word_time('great', 0.8), typing.word_time('luck', 1.19)]
          >>> typing.fastest_words([p0, p1])
          [['What', 'great'], ['great', 'luck']]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import typing
      >>> import tests.abstraction_check as test
      """,
      'teardown': r"""
      >>> test.restore_implementations(typing)
      """,
      'type': 'doctest'
    }
  ]
}
