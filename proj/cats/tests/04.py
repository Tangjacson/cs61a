test = {
  'name': 'Problem 4',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> wpm("12345", 3) # Note: wpm returns a float (with a decimal point)
          20.0
          >>> wpm("a b c", 20)
          3.0
          >>> wpm("", 10)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> wpm("a  b  c  d", 5)
          24.0
          >>> wpm("a b c", 120)
          0.5
          >>> wpm("abc", 1)
          36.0
          >>> wpm(" a b \tc" , 1)
          84.0
          >>> wpm("", 10)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> reference_text = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art."
          >>> typed_string1 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art."
          >>> typed_string2 = "Abstraction, in general, is a fundamentl concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction usd in other fields such as art."
          >>> typed_string3 = "Abstraction,"
          >>> typed_string4 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. extra"
          >>> typed_string5 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. art"
          >>> typed_string6 = "abstraction"
          >>> round(wpm(typed_string1, 67), 1)
          99.2
          >>> round(wpm(typed_string2, 67), 1)
          98.9
          >>> round(wpm(typed_string3, 67), 1)
          2.1
          >>> round(wpm(typed_string4, 67), 1)
          100.3
          >>> round(wpm(typed_string5, 67), 1)
          199.3
          >>> round(wpm(typed_string6, 1), 1)
          132.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('neurine statutably quantivalent intrarachidian itinerantly', 18.95), 2)
          36.73
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('tautit misorder uptill urostealith cowy', 93.86), 2)
          4.99
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('sarcoplastic', 66.96), 2)
          2.15
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('lammer harpula physiologically sidecheck exampleless ferngrower shapeless bulgarian', 61.55), 2)
          16.18
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('', 96.77), 2)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('brainlike paramnesia crumenal undelivered urethrostenosis novemnervate vascularity swallowable', 29.88), 2)
          37.75
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('', 28.23), 2)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('obtruncate ornithomyzous acupress spiniferous', 21.81), 2)
          24.76
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('megacephalia tinosa', 39.15), 2)
          5.82
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('percesocine echeneidid iridiate conjugality convolute momentariness', 20.1), 2)
          40.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('rheotome', 1.36), 2)
          70.59
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('adjudicator touchous countenancer', 5.43), 2)
          72.93
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('', 10.95), 2)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('psychotic belauder prochlorite adsmithing perligenous', 92.96), 2)
          6.84
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('phytohormone condos enhanced mali', 23.53), 2)
          16.83
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('lanced cavalierness graminivorous gig matronal upaisle unfellowshiped', 14.6), 2)
          56.71
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('inport taxing electrostenolysis ophthalmorrhagia importableness', 96.35), 2)
          7.85
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('subdenomination erythrophilous', 1.31), 2)
          274.81
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('bacteriostat ordinable alacha peastone preaffect', 2.44), 2)
          236.07
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('easing unions xiphophyllous tetrapous freshwoman irritant medially', 48.95), 2)
          16.18
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('zoomorphism cattiness reaggravation', 1.88), 2)
          223.4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('term', 87.36), 2)
          0.55
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('jugful goatbrush graphite fever scouse hypocathexis malposed misdread', 31.56), 2)
          26.24
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('golf impersonatress scirrhoma vaginoscopy harold mesonotal livier palamate', 19.77), 2)
          44.92
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('undeclared staphyloplastic ag sulphurless ungrappler ascertainer dormitory zoarial', 47.25), 2)
          20.83
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('', 72.64), 2)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('extraterrestrial experimentalist incomputable lictorian sordellina pudsy', 10.81), 2)
          79.93
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('matchmark proportionably persons suprasternal agomphious oneanother albicans capeline poind', 18.97), 2)
          57.56
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('shivereens library coinheritance fourscore naggingly scutelliplantar shiftful prolonger locksman', 19.38), 2)
          59.44
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('handset alvine nonabandonment grat swashbucklery tunelessly', 1.11), 2)
          637.84
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('amorphus disbursement insularity comfortingly swing oaritic camphoryl passless', 20.0), 2)
          46.8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('mimotypic strippage purolymph peganite waiterage bogmire', 1.99), 2)
          337.69
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('butterless coprolitic bicuspid eleutheromorph', 3.23), 2)
          167.18
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('fraudulentness eloquence holotype scrappler sphincterate undilatory anotherkins blandiloquence', 17.92), 2)
          62.95
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('gardenlike hayband ductible', 97.55), 2)
          3.32
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('pericolpitis cledonism xanthocyanopsia urethratome further monoazo otidium', 6.32), 2)
          140.51
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('phagedenous colature unrented spalt unenvironed fissiparous trunked', 4.22), 2)
          190.52
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('', 64.0), 2)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('error emoloa nonextensional stylelike rotate', 50.62), 2)
          10.43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('donnert', 3.71), 2)
          22.64
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('extralite handicraft architectural semiductile microcephalic coauthor whorishness disable', 47.12), 2)
          22.67
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('astay witnessdom', 54.31), 2)
          3.54
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('tapadera nonadherence', 5.51), 2)
          45.74
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('ramequin rehoist', 33.44), 2)
          5.74
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('inquinate actinoid', 7.47), 2)
          28.92
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('otocranial trail nontoxic kelpie marantaceous ataraxia', 39.15), 2)
          16.55
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('hyloid vinegarweed concresce herne irreclaimableness granose happiest weightedness analyzability', 52.08), 2)
          22.12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('', 21.79), 2)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('', 7.93), 2)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('flinchingly clow bases squiffed pleomorphism retelegraph electrocardiograph paurometaboly', 10.73), 2)
          99.53
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('dealbuminize itacolumite nonintoxicant cernuous pointful dray ureterogenital', 24.37), 2)
          37.42
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('theriomorph constraining ichthyopaleontology unshewed', 7.45), 2)
          85.37
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('decaudate coonskin nonexistent reappointment', 5.3), 2)
          99.62
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('prologist lowmen liquate discordful retiarius splenectomize limiting marketing', 56.81), 2)
          16.48
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('talon resolutions berginize acheilia', 22.45), 2)
          19.24
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('pharyngoceratosis crackerjack', 3.72), 2)
          93.55
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('coordinated austral unbank bemuddle balancelle porthook tarrass', 1.7), 2)
          444.71
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('', 1.21), 2)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('postcostal vespertilian trifurcation', 46.87), 2)
          9.22
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('unchoral mangue lawproof paginary eruption ambrosin tubularly alienee phlogistic', 34.69), 2)
          27.67
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('sophic', 37.78), 2)
          1.91
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('intradepartmental overappraise', 6.37), 2)
          56.51
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('planeness unbedded cantish elateroid excogitator hydatidiform pincement', 9.59), 2)
          88.84
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('beflag', 39.18), 2)
          1.84
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('ashpan', 3.19), 2)
          22.57
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('unegoistical sacrosanctity outscent', 25.74), 2)
          16.32
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('chloral parao fluid purplishness zoomorphism objectation chololithic neurography desquamation', 97.18), 2)
          11.48
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('chaff hamule sebiparous hatchgate', 63.23), 2)
          6.26
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('daggletail electropneumatic decigramme antistrophal', 2.76), 2)
          221.74
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('carneous pipework', 1.01), 2)
          201.98
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('psychotic unimpeded deferentially', 1.8), 2)
          220.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('bamboozle haphazardly bookmaker defoul fibdom autobiographist airworthy', 7.56), 2)
          112.7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('', 23.7), 2)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('pornograph goodeniaceous malinowskite', 28.52), 2)
          15.57
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('congener nonvisceral throng mythopoeic amphictyony pinfeathered decatyl lodged', 44.57), 2)
          21.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('cesarevitch unconcealably adenalgia', 47.43), 2)
          8.86
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('prudist dumbfounderment touristdom iconodulic airmonger superacknowledgment pneumolysis forestish folliculated', 86.59), 2)
          15.24
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('pseudopopular exocrine reestle gulinular unhollow billy nontransferability fissiparity infusory', 4.03), 2)
          282.88
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('tenantless polyadic blueback extant tracheobronchitis pansied untripe canellaceous septangle', 2.66), 2)
          415.04
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('stech unallayable hacker gasparillo angeyok tetrahedron recable garmin interval', 78.8), 2)
          12.03
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('love undepurated scrupulous', 1.87), 2)
          173.26
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('revengement isodiametrical', 52.3), 2)
          5.97
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('fecklessness mirror arbusterol featness champac churchyard subangulate unexplorable', 74.57), 2)
          13.36
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('pencel quadriparous beslubber under neological shrineless', 83.6), 2)
          8.18
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('related ev galvanized overharsh sleeplike', 18.98), 2)
          25.92
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('purgery shareholdership', 56.09), 2)
          4.92
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('', 92.96), 2)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('paulopost frolicly windflaw', 1.03), 2)
          314.56
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('hypothesist eclat heritage peership postposited autotropically underspar voeten', 1.97), 2)
          481.22
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('spindlewise uberous forebitter leafboy quadrisyllabous', 1.11), 2)
          583.78
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('hippiatry purolymph unthoughtful pansophism demonish freemason', 60.46), 2)
          12.31
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('badderlocks', 97.36), 2)
          1.36
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('diazole vassalry attercop checkers rombowline oleaginousness exsiliency coccygomorphic', 41.96), 2)
          24.59
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('childed peoplehood foxwood brachistochronic dentilation', 6.83), 2)
          96.63
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('panarchic hideous mordaciously quinia fixer wedding sendable ainoi', 68.66), 2)
          11.54
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('cnet coprophagan', 94.88), 2)
          2.02
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('sniperscope croconate unmisanthropic purchasable interapophyseal', 21.17), 2)
          36.28
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('perambulation', 98.12), 2)
          1.59
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('stamened registrable', 9.79), 2)
          24.51
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('', 6.21), 2)
          0.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from typing import wpm
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
