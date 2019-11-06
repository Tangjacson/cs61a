test = {
  'name': 'Problem 8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> typed = ['I', 'have', 'begun']
          >>> prompt = ['I', 'have', 'begun', 'to', 'type']
          >>> print_progress({'id': 1, 'progress': 0.6})
          ID: 1 Progress: 0.6
          >>> report_progress(typed, prompt, 1, print_progress) # print_progress is called on the report
          ID: 1 Progress: 0.6
          0.6
          >>> report_progress(['I', 'begun'], prompt, 2, print_progress)
          ID: 2 Progress: 0.2
          0.2
          >>> report_progress(['I', 'hve', 'begun', 'to', 'type'], prompt, 3, print_progress)
          ID: 3 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['neurine'], ['neurine', 'statutably', 'quantivalent', 'intrarachidian', 'itinerantly'], 21, print_progress)
          ID: 21 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['misorder', 'uptill'], 88, print_progress)
          ID: 88 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['fdecEphaliZation;', 'greenless', 'anhydrate', 'sarcoplastic', 'pseudoscopically'], ['decephalization', 'greenless', 'anhydrate', 'sarcoplastic', 'pseudoscopically', 'medullate', 'lammer', 'harpula'], 34, print_progress)
          ID: 34 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['tinosa'], 53, print_progress)
          ID: 53 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['punnage'], ['punnage', 'percesocine', 'echeneidid', 'iridiate', 'conjugality'], 58, print_progress)
          ID: 58 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['archon', 'rheotome', 'f$!transformistic', 'indeprivable', 'greenfinch', 'adjudicator'], ['archon', 'rheotome', 'transformistic', 'indeprivable', 'greenfinch', 'adjudicator', 'touchous', 'countenancer'], 94, print_progress)
          ID: 94 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['nonsubstantiation', 'algologist', 'darkle'], 81, print_progress)
          ID: 81 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['reaggravation', 'brachyphalangia'], 65, print_progress)
          ID: 65 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['reaffusion', 'catfish', 'monoparental'], ['reaffusion', 'catfish', 'monoparental', 'glutinousness'], 54, print_progress)
          ID: 54 Progress: 0.75
          0.75
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['hypocathexis'], 19, print_progress)
          ID: 19 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['}myatrophyn'], ['myatrophy', 'lackland', 'inelegancy'], 67, print_progress)
          ID: 67 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['extraterrestrial', 'experimentalist', 'incomputable', 'lictorian', 'sordellina'], ['extraterrestrial', 'experimentalist', 'incomputable', 'lictorian', 'sordellina', 'pudsy'], 32, print_progress)
          ID: 32 Progress: 0.8333333333333334
          0.8333333333333334
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['chamfer'], ['chamfer', 'draftsman', 'nonpurchaser', 'shivereens'], 79, print_progress)
          ID: 79 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['primulic'], ['primulic', 'retroreception'], 38, print_progress)
          ID: 38 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['tunelessly'], 44, print_progress)
          ID: 44 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['amorphus', 'disbursement', 'insularity', 'comfortingly', 'swing', 'oaritic'], ['amorphus', 'disbursement', 'insularity', 'comfortingly', 'swing', 'oaritic', 'camphoryl', 'passless'], 37, print_progress)
          ID: 37 Progress: 0.75
          0.75
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['fraudulentness', 'eloquence', 'holotype', 'scrappler', 'sphincterate'], ['fraudulentness', 'eloquence', 'holotype', 'scrappler', 'sphincterate', 'undilatory', 'anotherkins', 'blandiloquence'], 23, print_progress)
          ID: 23 Progress: 0.625
          0.625
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['pericolpitis', 'cledonism', 'xanthocyanopsia'], 3, print_progress)
          ID: 3 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['P$Hagedenous', 'colature', 'unrented', 'spalt'], ['phagedenous', 'colature', 'unrented', 'spalt', 'unenvironed', 'fissiparous', 'trunked'], 92, print_progress)
          ID: 92 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['schistaceous', 'glucoside'], ['schistaceous', 'glucoside', 'hyloid'], 96, print_progress)
          ID: 96 Progress: 0.6666666666666666
          0.6666666666666666
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['temporalness'], 58, print_progress)
          ID: 58 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['illucidation'], 63, print_progress)
          ID: 63 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['fittingly'], 36, print_progress)
          ID: 36 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['flinchingly', 'clow', 'bases', 'squiffed', 'pleomorphism', 'retelegraph', 'electrocardiograph', 'paurometaboly'], 71, print_progress)
          ID: 71 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['dealbuminize', 'itacolumite', 'nonintoxicant'], ['dealbuminize', 'itacolumite', 'nonintoxicant', 'cernuous', 'pointful', 'dray', 'ureterogenital'], 32, print_progress)
          ID: 32 Progress: 0.42857142857142855
          0.42857142857142855
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['plumery', 'decaudate', 'coonskin', 'nonexistent', 'reappointment', 'crozzly'], 61, print_progress)
          ID: 61 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['discordful', 'retiarius', 'splenectomize', 'limiting'], ['discordful', 'retiarius', 'splenectomize', 'limiting', 'marketing'], 91, print_progress)
          ID: 91 Progress: 0.8
          0.8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['ergophobiac', 'quarreled'], ['ergophobiac', 'quarreled', 'pharyngoceratosis'], 55, print_progress)
          ID: 55 Progress: 0.6666666666666666
          0.6666666666666666
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['unbank'], ['unbank', 'bemuddle'], 53, print_progress)
          ID: 53 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['brad'], 59, print_progress)
          ID: 59 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['incongruity'], 35, print_progress)
          ID: 35 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['trifurcation'], 73, print_progress)
          ID: 73 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['mangue', 'lawproof', 'paginary', 'eruption', 'ambrosin', 'tubularly'], 79, print_progress)
          ID: 79 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['adeptship', 'forego', 'autoscience', 'sophic', 'owse', 'lipomata', 'halitus', 'intradepartmental'], 56, print_progress)
          ID: 56 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['septentrional', 'heterochrome'], 4, print_progress)
          ID: 4 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['elateroid'], ['elateroid', 'excogitator', 'hydatidiform', 'pincement'], 97, print_progress)
          ID: 97 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['gasometer', 'conjunctiva', 'escobilla'], ['gasometer', 'conjunctiva', 'escobilla', 'apepsy', 'ashpan'], 54, print_progress)
          ID: 54 Progress: 0.6
          0.6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['parao'], 36, print_progress)
          ID: 36 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['zoomorphism'], 3, print_progress)
          ID: 3 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['aspiringness'], 36, print_progress)
          ID: 36 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['hamule', 'sebiparous'], ['hamule', 'sebiparous', 'hatchgate', 'selected'], 63, print_progress)
          ID: 63 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['daggletail', 'electropneumatic', 'decigramme'], ['daggletail', 'electropneumatic', 'decigramme', 'antistrophal'], 74, print_progress)
          ID: 74 Progress: 0.75
          0.75
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['golandaas'], ['golandaas', 'cylinderlike'], 58, print_progress)
          ID: 58 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['allotrophic'], 0, print_progress)
          ID: 0 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['bamboozle', 'haphazardly', 'bookmaker', 'defoul'], ['bamboozle', 'haphazardly', 'bookmaker', 'defoul', 'fibdom', 'autobiographist', 'airworthy'], 73, print_progress)
          ID: 73 Progress: 0.5714285714285714
          0.5714285714285714
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['malinowskite', 'bullet', 'pseudaposporous'], ['malinowskite', 'bullet', 'pseudaposporous', 'congener', 'nonvisceral'], 84, print_progress)
          ID: 84 Progress: 0.6
          0.6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['cesarevitch', 'Unconcealablye', 'adenalg_ia'], ['cesarevitch', 'unconcealably', 'adenalgia', 'lasher', 'kerseymere', 'isocephalous', 'preinsurance'], 92, print_progress)
          ID: 92 Progress: 0.14285714285714285
          0.14285714285714285
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['related', 'ev'], ['related', 'ev', 'galvanized', 'overharsh', 'sleeplike'], 96, print_progress)
          ID: 96 Progress: 0.4
          0.4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['hussyness'], 10, print_progress)
          ID: 10 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['physicomorphism'], 27, print_progress)
          ID: 27 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['hypothesist', 'eclat', 'iheritagE', 'peership'], ['hypothesist', 'eclat', 'heritage', 'peership', 'postposited', 'autotropically', 'underspar', 'voeten'], 90, print_progress)
          ID: 90 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['luteous', 'socky', 'onwards'], ['luteous', 'socky', 'onwards', 'panarchic', 'hideous', 'mordaciously'], 57, print_progress)
          ID: 57 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['phallical'], ['phallical', 'bellipotent', 'stainless'], 4, print_progress)
          ID: 4 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['instructors'], 63, print_progress)
          ID: 63 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['purchasable'], ['purchasable', 'interapophyseal', 'unmarring', 'cationic', 'nunhood', 'martyrdom', 'perambulation', 'gaseous'], 97, print_progress)
          ID: 97 Progress: 0.125
          0.125
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['uniliteral'], 53, print_progress)
          ID: 53 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['colocolic'], 33, print_progress)
          ID: 33 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['tangram'], 12, print_progress)
          ID: 12 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['cocovenantor'], ['cocovenantor', 'tormentry', 'billywix', 'slothfully', 'unfathomable', 'belayer'], 52, print_progress)
          ID: 52 Progress: 0.16666666666666666
          0.16666666666666666
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['regulatory'], 73, print_progress)
          ID: 73 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['nemertean'], ['nemertean', 'cyanurine'], 37, print_progress)
          ID: 37 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['coascend', 'unperpetrated', 'chemical'], ['coascend', 'unperpetrated', 'chemical', 'abolitionize'], 29, print_progress)
          ID: 29 Progress: 0.75
          0.75
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['pitwork'], ['pitwork', 'janitorial', 'yesteryear'], 80, print_progress)
          ID: 80 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['mouselike'], ['mouselike', 'cachinnatory'], 48, print_progress)
          ID: 48 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['batster', 'bandrol'], 89, print_progress)
          ID: 89 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['wri!teA', 'undervalue', 'imputedlY', 'dishonestly'], ['write', 'undervalue', 'imputedly', 'dishonestly', 'coatie'], 15, print_progress)
          ID: 15 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['prepubescent', 'indigenist'], ['prepubescent', 'indigenist', 'kobold', 'serene', 'samel', 'dusting'], 85, print_progress)
          ID: 85 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['hyperurbanism', 'berrugate'], 29, print_progress)
          ID: 29 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['imprime'], ['imprime', 'permuter', 'hyperspherical'], 65, print_progress)
          ID: 65 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['subolive', 'graduateship', 'corybulbin', 'impenetrableness'], ['subolive', 'graduateship', 'corybulbin', 'impenetrableness', 'mucusin'], 26, print_progress)
          ID: 26 Progress: 0.8
          0.8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['milord', 'unscratchable', 'commendation', 'habille', 'pouce'], 80, print_progress)
          ID: 80 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['bronchostomy'], 10, print_progress)
          ID: 10 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['unclipped'], 22, print_progress)
          ID: 22 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['antipodist', 'caprinic', 'ringbark'], 5, print_progress)
          ID: 5 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['seconder'], 7, print_progress)
          ID: 7 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['paradoxidian', 'hypergeometrical', 'veteraness'], ['paradoxidian', 'hypergeometrical', 'veteraness', 'purposeful'], 61, print_progress)
          ID: 61 Progress: 0.75
          0.75
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['porcellanize', 'abiosis', 'coalternative'], 56, print_progress)
          ID: 56 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['hyperphysics', 'quince', 'dodecahydrated', 'sensationalize', 'stamphead', 'KtankmakerD'], ['hyperphysics', 'quince', 'dodecahydrated', 'sensationalize', 'stamphead', 'tankmaker', 'becut', 'oenochoe'], 67, print_progress)
          ID: 67 Progress: 0.625
          0.625
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['silverboom', 'draconites', 'inteRsperse', 'protomanganese'], ['silverboom', 'draconites', 'intersperse', 'protomanganese', 'birdcraft', 'figurer'], 82, print_progress)
          ID: 82 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['mastooccipital', 'unfading', 'superstrong', 'splenophrenic'], ['mastooccipital', 'unfading', 'superstrong', 'splenophrenic', 'repudiable', 'laryngismus', 'flowoff'], 88, print_progress)
          ID: 88 Progress: 0.5714285714285714
          0.5714285714285714
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['characterologist'], 84, print_progress)
          ID: 84 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['pO\\sItIoning'], ['positioning', 'skinful'], 16, print_progress)
          ID: 16 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['taihoa', 'conn', 'jungle', 'tardy', 'ritualist', 'unarguableness'], ['taihoa', 'conn', 'jungle', 'tardy', 'ritualist', 'unarguableness', 'nonfrustration'], 11, print_progress)
          ID: 11 Progress: 0.8571428571428571
          0.8571428571428571
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['unsignatured', 'carious', 'enunciatory'], 68, print_progress)
          ID: 68 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['allotropical', 'breastpiece'], ['allotropical', 'breastpiece', 'unestopped', 'loverwise', 'agamically'], 3, print_progress)
          ID: 3 Progress: 0.4
          0.4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['scrinch', 'supercaution', 'marquisette', 'unrestful', 'multilirate'], 60, print_progress)
          ID: 60 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['Scoprophi"lia'], ['coprophilia', 'xylogen', 'algesic', 'ger', 'ahoy', 'ventriloquial', 'unshameful'], 12, print_progress)
          ID: 12 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['cliffed', 'infrigidate', 'euphemizer', 'curare'], 1, print_progress)
          ID: 1 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['guaiol'], ['guaiol', 'venisonivorous'], 82, print_progress)
          ID: 82 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['cicatrix', 'plenipotent'], ['cicatrix', 'plenipotent', 'extraduction', 'goli', 'alliaceous', 'perkin'], 78, print_progress)
          ID: 78 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['confidential'], ['confidential', 'blousing', 'iniome', 'boneblack'], 44, print_progress)
          ID: 44 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['fiscal', 'caduac', 'claro', 'piliferous'], ['fiscal', 'caduac', 'claro', 'piliferous', 'hydrazidine', 'insurgent', 'haemathermal'], 87, print_progress)
          ID: 87 Progress: 0.5714285714285714
          0.5714285714285714
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['pickfork'], 90, print_progress)
          ID: 90 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['choledochostomy'], 17, print_progress)
          ID: 17 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['Eowners$D', 'p:rofanablek'], ['owners', 'profanable', 'biradiate', 'chelem'], 81, print_progress)
          ID: 81 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['served', 'cyanophycean', 'photoradio', 'vility', 'copellidine', 'creditor', 'parvenuism'], 56, print_progress)
          ID: 56 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['unliterally', 'taxology'], 81, print_progress)
          ID: 81 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['assassinator'], 7, print_progress)
          ID: 7 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['nigrosine'], 75, print_progress)
          ID: 75 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['untemporal', 'thereabouts'], ['untemporal', 'thereabouts', 'oligoplasmia', 'cotemporaneous', 'sangrel', 'untile', 'edgy', 'cathedra'], 57, print_progress)
          ID: 57 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from typing import report_progress
      >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
