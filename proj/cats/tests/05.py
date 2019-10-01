test = {
  'name': 'Problem 5',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
          >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
          'cult'
          >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
          'cul'
          >>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
          'car'
          >>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
          >>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
          'word'
          >>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
          'inside'
          >>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
          'idea'
          >>> autocorrect("outside", ["idea", "insider"], first_diff, 0.5)
          'outside'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> matching_diff = lambda w1, w2, limit: sum([w1[i] != w2[i] for i in range(min(len(w1), len(w2)))]) # Num matching chars
          >>> autocorrect("tosting", ["testing", "asking", "fasting"], matching_diff, 10)
          'testing'
          >>> autocorrect("tsting", ["testing", "rowing"], matching_diff, 10)
          'rowing'
          >>> autocorrect("bwe", ["awe", "bye"], matching_diff, 10)
          'awe'
          >>> autocorrect("bwe", ["bye", "awe"], matching_diff, 10)
          'bye'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> words_list = sorted(lines_from_file('data/words.txt')[:10000])
          >>> autocorrect("testng", words_list, lambda w1, w2, limit: 1, 10)
          'a'
          >>> autocorrect("testing", words_list, lambda w1, w2, limit: 1, 10)
          'testing'
          >>> autocorrect("gesting", words_list, lambda w1, w2, limit: sum([w1[i] != w2[i] for i in range(min(len(w1), len(w2)))]) + abs(len(w1) - len(w2)), 10)
          'getting'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('statutably', ['statutably'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'statutably'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('decephalization', ['tautit', 'misorder', 'uptill', 'urostealith', 'cowy', 'sinistrodextral'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'sinistrodextral'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('hypostasis', ['tinosa'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'hypostasis'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('indeprivable', ['echeneidid', 'iridiate', 'conjugality', 'convolute', 'momentariness', 'hotelless', 'archon', 'rheotome', 'transformistic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'conjugality'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('helena', ['ailment', 'undeclared', 'staphyloplastic', 'ag', 'sulphurless', 'ungrappler', 'ascertainer', 'dormitory', 'zoarial'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'helena'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('lictorian', ['felineness', 'deontological', 'extraterrestrial', 'experimentalist', 'incomputable'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'lictorian'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('mousehound', ['unembowelled', 'indigene', 'kersmash', 'mousehound', 'matchmark', 'proportionably', 'persons', 'suprasternal', 'agomphious'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'mousehound'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('chamfer', ['pretyrannical'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'pretyrannical'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('locksman', ['coinheritance', 'fourscore', 'naggingly', 'scutelliplantar', 'shiftful', 'prolonger'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'shiftful'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('nonextensional', ['unlivably', 'error', 'emoloa'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'nonextensional'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('incavern', ['donnert', 'incavern'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'incavern'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('disable', ['semiductile', 'microcephalic', 'coauthor', 'whorishness', 'disable'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'disable'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('antigravitational', ['brad'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'antigravitational'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('trifurcation', ['trifurcation', 'formative'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'trifurcation'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('phlogistic', ['mangue', 'lawproof', 'paginary', 'eruption', 'ambrosin', 'tubularly', 'alienee'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'tubularly'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('psychotic', ['cylinderlike', 'filipendulous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'psychotic'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('terpodion', ['terpodion', 'wintertide'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'terpodion'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('socky', ['childed', 'peoplehood', 'foxwood', 'brachistochronic', 'dentilation', 'luteous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'socky'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('wedding', ['mordaciously', 'quinia', 'fixer', 'wedding', 'sendable', 'ainoi'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'wedding'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('unarrestable', ['unmarring', 'cationic', 'nunhood', 'martyrdom', 'perambulation', 'gaseous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'perambulation'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('sprightliness', ['unlimb', 'octamerism', 'antipodist', 'caprinic', 'ringbark', 'suboptimal', 'kingfish', 'amomal'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'sprightliness'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('veteraness', ['wavement', 'paradoxidian', 'hypergeometrical', 'veteraness', 'purposeful', 'irrigative', 'ultramontanism', 'epephragmal'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'veteraness'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('hyperphysics', ['thiouracil', 'cibophobia', 'katamorphism', 'trimorphism', 'norie'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'katamorphism'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('evagation', ['sensationalize', 'stamphead', 'tankmaker', 'becut', 'oenochoe', 'digoneutic', 'refinement', 'tininess', 'benedictively', 'segment'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'stamphead'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('ashine', ['nonfrustration', 'perineostomy', 'nonupholstered', 'hypocoristically', 'plushlike', 'rancorously'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'ashine'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('unshameful', ['ger', 'ahoy', 'ventriloquial'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'unshameful'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('dramatist', ['tournament', 'acclinate', 'rasion'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'acclinate'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('beewort', ['terrestrious', 'sociometry'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'beewort'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('claylike', ['houndish', 'muirfowl', 'unexplorative'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'houndish'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('columbine', ['nonupholstered', 'columbine', 'entoptical', 'spondylolisthetic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'columbine'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('owners', ['choledochostomy', 'superobstinate', 'pagoscope'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'owners'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('tampa', ['commonness', 'incentively', 'courtezanship', 'unapproachableness', 'readvertisement', 'strumiprivous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'tampa'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('reaffirmance', ['reaffirmance', 'nursy'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'reaffirmance'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('photonasty', ['decisively', 'uninclosed', 'chlor'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'decisively'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('intercepter', ['empiecement'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'empiecement'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('semideity', ['roundseam', 'misrule', 'cardioblast', 'semideity', 'yaply', 'anthroponomy'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'semideity'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('served', ['cecomorphic', 'ademption', 'impassibility', 'introvert', 'reintrench', 'transmigratively', 'commerge', 'hematocryal'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'commerge'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('unliterally', ['vility', 'copellidine', 'creditor', 'parvenuism', 'hindbrain', 'autantitypy', 'sailing', 'dermatoskeleton'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'copellidine'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('growth', ['assassinator'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'growth'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('thereabouts', ['quantifiable', 'exterritorial', 'believe', 'untemporal', 'thereabouts'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'thereabouts'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('goblinism', ['bobby', 'thig', 'plasterwork', 'unhyphenated', 'subessential', 'softhead', 'metrocracy', 'understem'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'understem'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('resoutive', ['hydroseparation', 'descry', 'apodosis', 'atavist'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'apodosis'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('unwebbed', ['cramble', 'pseudopopular', 'unwebbed', 'minimize', 'ricinoleate', 'arthrogastran', 'testaceography'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'unwebbed'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('emphasize', ['putchen'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'emphasize'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('whapuka', ['seambiter', 'cogman', 'polymorphistic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'cogman'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('cubatory', ['byssaceous', 'begins', 'cubatory', 'galvanothermometer', 'appearanced', 'proavian'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'cubatory'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('singler', ['mycetous', 'singler'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'singler'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('esquirearchy', ['souper', 'ark', 'niccolite', 'reagin', 'esquirearchy', 'effeminatize'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'esquirearchy'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('evulse', ['uniocular', 'caution', 'unhoofed', 'misinterpret', 'ooscope', 'physiophilosophy', 'potteringly', 'wartyback'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'evulse'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('underpopulation', ['adenocarcinomatous', 'soliloquy', 'antispace', 'slimeman', 'cardioncus', 'bin', 'undervalve', 'sundek'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'underpopulation'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('osteology', ['transphenomenal'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'osteology'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('solenaceous', ['padding', 'pixel', 'unalimentary', 'dyschroa', 'undefinedly', 'violational', 'bisulfid', 'pralltriller', 'demonstration'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'undefinedly'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('diabolicalness', ['cronstedtite', 'precipitate', 'undertook', 'unconspicuousness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'cronstedtite'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('airworthiness', ['sep'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'airworthiness'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('pseudomorula', ['toprope', 'doltishly', 'radiotelegraphic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'pseudomorula'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('hauld', ['pyrenodean', 'hauld'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'hauld'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('doll', ['stylolitic', 'altigraph', 'doll', 'avowably', 'manzana', 'galloon'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'doll'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('rachilla', ['tridentated', 'bridgework', 'coif', 'hitchhike', 'rachilla', 'uptaker', 'penalty', 'commitment', 'supervisor', 'unquartered'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'rachilla'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('ventriculogram', ['luggie', 'septectomy', 'unproctored', 'volition', 'straked', 'oliver', 'telescopic', 'scarabaeoid'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'ventriculogram'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('arsonvalization', ['nondisarmament', 'arsonvalization', 'ketyl', 'tussle', 'rhabdomysarcoma'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'arsonvalization'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('photospectroscopical', ['unenclosed', 'sagacious', 'saur', 'gloveress', 'limbless', 'daresay', 'mysticize'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'photospectroscopical'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('tupara', ['unkerchiefed', 'dormant', 'triplite', 'bimuscular', 'insider', 'coadjacency', 'unslighted', 'perichordal'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'dormant'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('odontoglossate', ['odontoglossate', 'conceivableness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'odontoglossate'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('retro', ['grayback'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'retro'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('pung', ['campoo'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'pung'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('liberal', ['owse', 'ingenerable', 'patrol', 'kenosis', 'wetted'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'kenosis'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('disclaimer', ['psiloi', 'kusti', 'vallation', 'reprehensive', 'blameworthiness', 'proteiform', 'taintless', 'incruent', 'wednesday', 'codebtor'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'proteiform'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('orthological', ['consentaneous', 'orthological'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'orthological'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('amylemia', ['chirotonsory', 'loiter', 'ulnad', 'ticklebrain'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'amylemia'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('amendableness', ['baked', 'nonpriestly', 'unfavorably', 'amendableness', 'curatorship', 'intermediacy'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'amendableness'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('gammoning', ['weariedly', 'elongation', 'xanthous', 'squatty', 'dermad', 'iamatology', 'hexachloride', 'womanize', 'favorably'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'weariedly'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('siliciferous', ['siliciferous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'siliciferous'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('patrization', ['deuteropathy', 'pregracile'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'deuteropathy'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('royetously', ['coster', 'microbiological', 'royetously'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'royetously'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('unbewritten', ['camphane', 'unbewritten', 'meditationist', 'hydriform'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'unbewritten'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('searing', ['ultrapapist', 'shriekingly', 'scratchiness', 'searing', 'pot', 'valanche', 'subterraqueous', 'helleboraceous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'searing'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('arara', ['synergistically', 'prerecital', 'lozengeways', 'coessentially', 'cubicontravariant', 'snootiness', 'hetaerocracy', 'acaudate', 'simperer'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'acaudate'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('uptowner', ['hopyard'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'hopyard'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('presettlement', ['previsit'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'presettlement'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('soak', ['upside', 'demirevetment', 'undelineated', 'excusative', 'engagingness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'upside'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('reduction', ['gym'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'reduction'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('doctorship', ['peccable', 'jussive', 'doctorship', 'overgladly', 'lurdanism', 'channel', 'malpublication', 'derringer', 'amental'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'doctorship'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('wintry', ['scyllitol', 'seringhi', 'ditchdown', 'procursive', 'unwholesome', 'unholiday', 'eureka', 'feathertop'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'eureka'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('transborder', ['conciliative', 'undercoachman', 'phasogeneous', 'philobrutish'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'conciliative'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('pericycloid', ['viertelein', 'felicitation', 'aortolith', 'nonpresbyter', 'germinable', 'illegibleness', 'undercondition', 'introverted', 'noselessly', 'tramming'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'introverted'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('indissolvability', ['hotbox', 'tokay', 'palaeofauna', 'indissolvability'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'indissolvability'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('soubrettish', ['unadvisably', 'unoften', 'unsecreted', 'precessional', 'erosional'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'unadvisably'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('semiopacity', ['animotheism', 'recoupment', 'juvenescence', 'scalable', 'thai', 'semiopacity'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'semiopacity'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('penwomanship', ['pyrocondensation', 'spooler', 'archorrhea', 'penwomanship', 'acheirus', 'lieutenant', 'plumless'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'penwomanship'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('subcordiform', ['subcordiform'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'subcordiform'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('quarrelsomely', ['concert', 'canonics', 'hip', 'uncrested', 'ectoethmoid', 'supertutelary', 'ignore'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'supertutelary'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('ditchdown', ['gonapophysis', 'permeability'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'ditchdown'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('suborbiculate', ['prisonable', 'rhapsodist', 'suborbiculate'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'suborbiculate'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('quiesce', ['synedria', 'apesthesia', 'squawbush', 'devourer', 'tetany', 'quiesce'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'quiesce'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('shiv', ['unconceivableness', 'inappetence'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'shiv'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('shuttleheaded', ['uterovaginal', 'extraparochially', 'serolipase'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'shuttleheaded'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('hilarity', ['valorously', 'hilarity', 'fungilliform', 'haven', 'torsk', 'thing', 'pickerel', 'refilm'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'hilarity'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('prefunctional', ['kep'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'prefunctional'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('oxypurine', ['overpensiveness', 'overindustrialize', 'lightweight', 'provinciality', 'telestereoscope', 'vastidity'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'vastidity'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('forewarningly', ['foxery'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'foxery'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from typing import autocorrect, lines_from_file
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
