test = {
  'name': 'Problem 3',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> accuracy("12345", "12345") # Returns 100.0
          100.0
          >>> accuracy("a b c", "a b c")
          100.0
          >>> accuracy("a  b  c  d", "b  a  c  d")
          50.0
          >>> accuracy("a b", "c d e")
          0.0
          >>> accuracy("a b c d", " a d ")
          25.0
          >>> accuracy("abc", " ")
          0.0
          >>> accuracy(" a b \tc" , "a b c") # Tabs don't count as words
          100.0
          >>> accuracy("abc", "")
          0.0
          >>> accuracy("", "abc")
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
          >>> round(accuracy(typed_string2, reference_text), 1)
          97.7
          >>> round(accuracy(typed_string3, reference_text), 1)
          100.0
          >>> round(accuracy(typed_string4, reference_text), 1)
          98.9
          >>> round(accuracy(typed_string5, reference_text), 1)
          49.7
          >>> round(accuracy(typed_string6, reference_text), 1)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('statu>tably tautit up]ti]ll a\\nhydrat(e h)arpula sidecheck }shapeless structuration bra>inlike', 'statu>tably tautit up]ti]ll a\\nhydrat(e h)arpula'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('prosneusis dismayfully tinosa& percesocine echeneidid convolute a(rchon in\\deprivab,le', 'prosneusis dismayfully tinosa& percesocine echeneidid convolute a(rchon'), 2)
          87.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('phytohormone enhanced splen:\\itive g&ig unfellowshiped }zoogeology %taxi#ng +heredi.tivity ~unreservedness', 'phytohormone enhanced splen:\\itive g&ig unfellowshiped }zoogeology %taxi#ng +heredi.tivity ~unreservedness'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('cattiness`/ grouseless re,)affusion goatbrush fever hypocath+exi>s inelegan}cy im$personat}ress', 'cattiness`/ grouseless re,)affusion goatbrush fever hypocath+exi>s inelegan}cy im$personat}ress palamate'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('felineness extraterres.trial sordellina unembowel/led matchmark', "felineness extraterres.trial sordellina unembowel/led matchmark p|er@sons poind prety'rannical coinheri(tance"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('amorphus insula$rity: praes}t|ernum waiterage hypoploid flagl[ea,f fraud\\ulentness und@?ilatory h*ayband', 'amorphus insula$rity: praes}t|ernum waiterage hypoploid'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('unren]te"d undwelt }myxop&odous rotate <reproducer modificator', 'unren]te"d undwelt }myxop&odous rotate <reproducer modificator extralite architectural microce$phalic'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('rameq-uin infec:t`iousness outblo}<w maran*taceous c`oncresce! !temporaln[ess dis]comm?odiousness pleomor`phism paurometaboly', 'rameq-uin infec:t`iousness outblo}<w maran*taceous c`oncresce! !temporaln[ess dis]comm?odiousness'), 2)
          77.78
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('un{s?hewed coons(kin> discordful sple,nectomize chiliarchia', 'un{s?hewed coons(kin> discordful sple,nectomize chiliarchia s+u?rdomute ergop=hobiac'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("unrhythmical brad incongruity whistleli<ke+ visuos'ensory lawproof", "unrhythmical brad incongruity whistleli<ke+ visuos'ensory lawproof paginary"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('li;pomata{ septentrional unbedded elater\\oid bhungin&i escob>illa', 'li;pomata{ septentrional unbedded elater\\oid bhungin&i escob>illa p([edlar bols>tere!r purplishness'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('sele`c,ted electropneumatic antistrophal wo+odfish golandaas', 'sele`c,ted electropneumatic antistrophal wo+odfish golandaas "unimpe<ded bamboozle'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('familiarization reptilivo>rous goodeni"aceous bullet congener thro`ng (dec?atyl adena>lg*ia iconodulic', 'familiarization reptilivo>rous goodeni"aceous bullet congener thro`ng (dec?atyl adena>lg*ia iconodulic'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('sim-sim f*usi.on pa$nsied epuloid^ unallayable', 'sim-sim f*usi.on pa$nsied epuloid^ unallayable gasparillo angey.o}k mantico_re'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('dicary!o)n churchyar}d ch,emotactically beslubber ne#ological', 'dicary!o)n churchyar}d ch,emotactically beslubber ne#ological poma`ce&ntrid g/a{lvanized shareholdership sourweed'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("autotropically swa,gbellied spi?nd'lewise petalwise disar&min`gly", "autotropically swa,gbellied spi?nd'lewise petalwise disar&min`gly"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('corrosibleness diazo@le checkers r\\omb&owline childe+d` pan:archic f^i`xer p&hal=lical', 'corrosibleness diazo@le checkers r\\omb&owline childe+d` pan:archic f^i`xer p&hal=lical'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('s/eatrain ,uniliteral coloco<lic coc!ove#nantor be/layer', 's/eatrain ,uniliteral coloco<lic coc!ove#nantor be/layer obispo'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('cyanurine ?retardent c<hemica>l wh$ilere \\jani"torial phae_nom{enal ph\'o*toscopic', 'cyanurine ?retardent c<hemica>l wh$ilere \\jani"torial phae_nom{enal ph\'o*toscopic pach^yperitonitis undervalue'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("terr]ori=ze tapader]o acronymic blo$om-kin hal$ophil'e outq=ue=stion un%hastily!", "terr]ori=ze tapader]o acronymic blo$om-kin hal$ophil'e outq=ue=stion un%hastily! occiduous"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('here>#by rendered permuter theos,ophism subol^.ive middleway remit&}ter habille', 'here>#by rendered permuter theos,ophism subol^.ive middleway remit&}ter'), 2)
          87.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('antipodist ringbark amomal sprightliness seconder paradox!idian $irr{igative', 'antipodist ringbark amomal sprightliness seconder paradox!idian $irr{igative abio?sis'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('"tank/maker segmen\\`t }sindle# dissatu,ra\\te $bontebu<ck cavus', '"tank/maker segmen\\`t }sindle# dissatu,ra\\te $bontebu<ck cavus unm&asking pancreatolith mine&rals'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('non+co`ncurrency silverboo_m figurer tahoe m}isw|ord deltidium i{sovaline probableness', 'non+co`ncurrency silverboo_m figurer tahoe m}isw|ord deltidium i{sovaline probableness scrimshand:y'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("z,an.ella (babill;ard fa@tall\\y sple'no&phrenic hood`like sud'adero atel:omitic rash\\like", "z,an.ella (babill;ard fa@tall\\y sple'no&phrenic hood`like sud'adero atel:omitic rash\\like"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("tripper philo^xyg<enous inhe\\rently s,t#rongly h^airwork unexonera'ble adj'oined", "tripper philo^xyg<enous inhe\\rently s,t#rongly h^airwork unexonera'ble adj'oined"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('rancor(ou>sly u\\nnefarious dotingn_ess enunciatory demidandiprat to|uchl^ess', 'rancor(ou>sly u\\nnefarious dotingn_ess enunciatory demidandiprat to|uchl^ess transischiac (instroke'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('redarn ras\\ion trifurcation mucronately i/nsinuant centrosymme(try', 'redarn ras\\ion trifurcation mucronately i/nsinuant'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('uncont-racted sociometry esop!h\\oria reb~eginning nonupholstere-d phacocherine', 'uncont-racted sociometry esop!h\\oria reb~eginning nonupholstere-d'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('beaminess veniso=nivorous^ plenipotent extraduction pe-rki]n', 'beaminess veniso=nivorous^ plenipotent extraduction pe-rki]n foreshorten'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('overpro<vidently mordication p;ic#kfork ow[-ners du[pl@icand com~monne-ss readvertisement', 'overpro<vidently mordication p;ic#kfork ow[-ners du[pl@icand com~monne-ss readvertisement der%m<atoma po}lycotyled`ony'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('y$aply propagandism adem_ption trans\\migratively [`vility autantitypy d~ermatoskeleto}n', 'y$aply propagandism adem_ption trans\\migratively [`vility'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('there{abouts e/dgy% soft;head irreportable ova}to&serrate', 'there{abouts e/dgy% soft;head irreportable ova}to&serrate'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('cloudw-ards cramble mi%}nimize besoothement a>naphori|a dic`er cuddyh>ole', 'cloudw-ards cramble mi%}nimize besoothement a>naphori|a dic`er'), 2)
          85.71
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('pyramidicalness phrenics em"phasize seambiter whapuka u.nderlock byssaceous', 'pyramidicalness phrenics em"phasize seambiter whapuka'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('mycetou%s in:calculab*leness unrenown$ed larvigerous applicability ca]ution physio-philosophy noso+geni&c meningit(i]s', 'mycetou%s in:calculab*leness unrenown$ed larvigerous applicability ca]ution physio-philosophy'), 2)
          77.78
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('?dogmatiz;e thoftfellow semicartilaginous deer c.o`tarius', '?dogmatiz;e thoftfellow semicartilaginous deer c.o`tarius editing; h(ursinghar m{ur?shid irrision'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('so-liloquy bin %.sundek ost,eology ?cost!ean violatio@nal', 'so-liloquy bin %.sundek ost,eology ?cost!ean violatio@nal'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('d@iabo/licalness artinite pyrrhichian s;irupy paranucleus pi&lo>n', 'd@iabo/licalness artinite pyrrhichian s;irupy paranucleus'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('enervation o;verpartial\\ p|hilo.sophling trac+t{orization aerostatics @arg[entine', 'enervation o;verpartial\\ p|hilo.sophling trac+t{orization aerostatics @arg[entine'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('sil#lyhow| infecund leatherl&ik?e unconcernment unconditionately a)gua', 'sil#lyhow| infecund leatherl&ik?e unconcernment unconditionately a)gua *pr-onominally |airwort\\hiness fossilat=ion'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('avowably_ thi^nking =hit^chhike tylopodous incentively', 'avowably_ thi^nking =hit^chhike tylopodous incentively o>.ctaemeron nonlicking'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("scraplet n)ondisarm/ament 'f.oo palm/it,one |prescutu^m pulsation s[ki=m daresay", "scraplet n)ondisarm/ament 'f.oo palm/it,one |prescutu^m pulsation s[ki=m"), 2)
          87.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('?twitch<el o;utsho"t tr"ipp{et unu\'n\'iformly o=ctoi\'d overs`tuff ,seignorial campoo| prosthodontist', '?twitch<el o;utsho"t tr"ipp{et unu\'n\'iformly o=ctoi\'d overs`tuff ,seignorial campoo| prosthodontist'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("blameworthiness taintless w{e'dnesday conse\\nta_neous cyclometric capi`tulate", "blameworthiness taintless w{e'dnesday conse\\nta_neous cyclometric"), 2)
          83.33
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('kam^eeldoorn cil*iary ~po(mmet ha$ngnail +lo\\iter borecol/e', 'kam^eeldoorn cil*iary ~po(mmet ha$ngnail +lo\\iter borecol/e'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('un@deryield squat|ty hexachloride favor(abl~y macro"chem!istry', 'un@deryield squat|ty hexachloride favor(abl~y macro"chem!istry europe pregraci-le coster'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('wo}r(dlike valan/ch`e synergistically lozengew,ays_ -s<imperer ho#pyard (lather inc^:ohesive $`metoestrum', 'wo}r(dlike valan/ch`e synergistically lozengew,ays_ -s<imperer ho#pyard (lather'), 2)
          77.78
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('compiled blowz"ing? oxbite(r duodenoch~olecystostomy` anaerobiu>\\m dignific.ation indagative vicinity', 'compiled blowz"ing? oxbite(r duodenoch~olecystostomy` anaerobiu>\\m dignific.ation indagative'), 2)
          87.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("hermeticism answerabil(ity u[ninstruc!tible resu:sc|itant mononucleo+sis% leafit wiring g'ym; noisily", "hermeticism answerabil(ity u[ninstruc!tible resu:sc|itant mononucleo+sis% leafit wiring g'ym;"), 2)
          88.89
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('mi,lligramage $ex<ecutionist eu|=reka g_igglingly phasogeneou&s/', 'mi,lligramage $ex<ecutionist eu|=reka g_igglingly phasogeneou&s/ frivolous+n+ess felicitation'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("iridosc_lerotomy recapturer u*nad)visably gai}nf!ully tha;i s'aburra spool\\er plumless connivant", "iridosc_lerotomy recapturer u*nad)visably gai}nf!ully tha;i s'aburra"), 2)
          66.67
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('supertu)telary quarrels?om<ely quino=vi_c raptus- and.rosin paraphrasia', 'supertu)telary quarrels?om<ely quino=vi_c raptus- and.rosin paraphrasia'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('rutaceous didynam.y; slendan"g chaff reindulg=e hemozoon', 'rutaceous didynam.y; slendan"g chaff reindulg=e hemozoon zoophili+sm seromucous inks@\'tain'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('thale/r ag/minated further providentially }hedonics dadd=>ynut c]onfe&rral', 'thale/r ag/minated further providentially }hedonics dadd=>ynut'), 2)
          85.71
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('discoura=ge condign overse}riously spondean rang meta&t#arsophalangeal b`uchnerite', 'discoura=ge condign overse}riously spondean rang meta&t#arsophalangeal b`uchnerite'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('babbler com|ma@nder d_evourer arth}ritis classicolatry, gu|ttide', 'babbler com|ma@nder d_evourer arth}ritis classicolatry, gu|ttide frondige}rous fervid/ness'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('blazoner hexadactyle ripgut non`manual thermogeographica*l_ oosporangium {ambrosiaceous overaff$ect', 'blazoner hexadactyle ripgut non`manual thermogeographica*l_ oosporangium {ambrosiaceous overaff$ect'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('in}appetenc;e extraparochially shuttleheaded un&abrupt haven refilm`', 'in}appetenc;e extraparochially shuttleheaded un&abrupt haven'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('mi}&lling kep prona;va,l provincial&ity *oxypurine f<ox[ery isospo%re< \\burhead g|alactonic', 'mi}&lling kep prona;va,l provincial&ity *oxypurine f<ox[ery isospo%re< \\burhead g|alactonic'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('enhydrous perdition patheticnes&s p~istle| pent~alogy py=r corta gamose$palous', 'enhydrous perdition patheticnes&s p~istle| pent~alogy py=r corta'), 2)
          87.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('microbicide redshirt ren&`eg disarrange`ment carfuffle $specifical|ly', 'microbicide redshirt ren&`eg disarrange`ment carfuffle'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('septemfoliolate[ pugi"+l earthmake.r an}-dronitis indispensable unconceded stubb[y wa,i%rd -s]keeg', 'septemfoliolate[ pugi"+l earthmake.r an}-dronitis indispensable unconceded stubb[y wa,i%rd -s]keeg'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('scratchpr>oof macrobacterium colo/ssean monopolylogue makeshiftness ges}ning', 'scratchpr>oof macrobacterium colo/ssean monopolylogue makeshiftness ges}ning'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("chorioallantoid isle s:tocha@stical gallace~>tophenone safe-ly _adet} scan%m'ag", "chorioallantoid isle s:tocha@stical gallace~>tophenone safe-ly _adet} scan%m'ag h`yper-nic"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("nondepre,ssed femi<nine turnbout* faussebraie &ethere}ally p'rotoso;lution uplad|der sout_%herland", "nondepre,ssed femi<nine turnbout* faussebraie &ethere}ally p'rotoso;lution"), 2)
          75.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("eclair interzooe].cial suspir&at#ive paniconogr'aph ari|oso, shipwright dissectional j^a{ngly prec:occygea>l", "eclair interzooe].cial suspir&at#ive paniconogr'aph ari|oso, shipwright dissectional j^a{ngly prec:occygea>l"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('macr}o poephagous attended c{o.nverted billiard undoubtingness redepre%ci)ate posticte.-ric', 'macr}o poephagous attended c{o.nverted billiard undoubtingness'), 2)
          75.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('-pangan!e sheikdom solitarin,ess nonconvivi<{al rhizoma errhine', '-pangan!e sheikdom solitarin,ess nonconvivi<{al rhizoma'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('dramat!i;st bromelia_d br+um<ous co/ckaw/ee o/ur upcr:eek supr`afoliar "garaba}to neo.pal[lium', 'dramat!i;st bromelia_d br+um<ous co/ckaw/ee o/ur upcr:eek supr`afoliar "garaba}to'), 2)
          88.89
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('c;a:rpholite bad`iaga bayou* q]o+ph betr)inket q!ua@rle pul][vinately scotosis', 'c;a:rpholite bad`iaga bayou* q]o+ph betr)inket q!ua@rle'), 2)
          75.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('ph`ysitheisti$c troop c?rya-ble pank>in nu+rseryman', 'ph`ysitheisti$c troop c?rya-ble pank>in nu+rseryman caecal uninstructibl=e'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('conocuneus (stict}iform garabato* interven[ient resi}dential w-ark', 'conocuneus (stict}iform garabato* interven[ient resi}dential w-ark'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("'dyelea_ves hy?pergene,tic u'n'doneness bireme br`onchomot%or tonsillary", "'dyelea_ves hy?pergene,tic u'n'doneness bireme br`onchomot%or tonsillary flo~or;s lepton"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('tearful( f\\ungicolous massicot supe)rintendent ;unwiv.ed $baken chidra herapathite =lygaei+d', 'tearful( f\\ungicolous massicot supe)rintendent ;unwiv.ed $baken chidra herapathite =lygaei+d'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('f?ondles:ome topee prematureness paleot>hermic co~acer\\vation whiteworm we!/llat bu%rette v(ia$lmaking', 'f?ondles:ome topee prematureness paleot>hermic co~acer\\vation'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('unsnarl sti*nte*d accommodately -simonist /abhorrently pulicoid anabi&osis', 'unsnarl sti*nte*d accommodately -simonist /abhorrently pulicoid anabi&osis =horopt+er'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('inleakag?e pur`-ry larviparous -p-iltock disilicide so>ngs\\ symbasis', 'inleakag?e pur`-ry larviparous -p-iltock disilicide so>ngs\\'), 2)
          85.71
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('se^mic&horic husbandm$an tarpaulin| halimous| debind *burthenman uns,!piritualize <vestalship: e~i]ghtscore', 'se^mic&horic husbandm$an tarpaulin| halimous| debind *burthenman uns,!piritualize <vestalship: e~i]ghtscore'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('solio;# depilate occi"pitoatloid leasable tartlet hi:gh}', 'solio;# depilate occi"pitoatloid leasable tartlet hi:gh} coc|cule pant%otheni?c'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('verite unsphere ampul{lace,ous ca!p(making engineman em=bla!zonry', 'verite unsphere ampul{lace,ous ca!p(making engineman em=bla!zonry extra'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('opis:thogyrous =exundati}on crani+ognosy retir.edness occasion gasome!try $kerygma pensiveness$ aphrodisian', 'opis:thogyrous =exundati}on crani+ognosy retir.edness occasion gasome!try $kerygma'), 2)
          77.78
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('prehistorically car{bani&lide pil]loww<ork gorgoniacean$ vo<lent a$mi}doacetophenone arthr"ozo_ic wal.let', 'prehistorically car{bani&lide pil]loww<ork gorgoniacean$ vo<lent'), 2)
          62.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('undercorrect sulphurator tenderne$ss anes tran\\smission chipp>y overaccurat_ely ctenodon@t', 'undercorrect sulphurator tenderne$ss anes tran\\smission chipp>y overaccurat_ely'), 2)
          87.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('bar:ogn*osis awesom,e h/eadstick# permonosulphur{ic :f~reshmanic glycerinate', 'bar:ogn*osis awesom,e h/eadstick# permonosulphur{ic :f~reshmanic glycerinate'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('petitionee demissness uns,electing un+so+lemn pont:es calycular cop monitorial', 'petitionee demissness uns,electing un+so+lemn pont:es calycular cop monitorial'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('b[lunker mele der&mal\'ith cronet p>ygmyship maxillojug;al intercheck fa"rrow', 'b[lunker mele der&mal\'ith cronet p>ygmyship maxillojug;al intercheck fa"rrow'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("br(oomer pros.?odic mahmal stre`el) )t%ramway gun'bearer :tre^ssilate underthink{", "br(oomer pros.?odic mahmal stre`el) )t%ramway gun'bearer"), 2)
          75.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('mullite otos?is+ overtee:]m c%lay[ urbane', 'mullite otos?is+ overtee:]m c%lay[ urbane sprayful nipp$onium unornate practic{alist#'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('mi]crogastrine awe%ary di~adelphia<n =ligna;tile tab|#by doss+<', 'mi]crogastrine awe%ary di~adelphia<n =ligna;tile tab|#by doss+< myofibroma/ oc>eanography'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("quadrua&l# #yelmer} representationalism nonfrust?ration scalage bobbi'ner oc|ci(pitoaxial bifidated", "quadrua&l# #yelmer} representationalism nonfrust?ration scalage bobbi'ner oc|ci(pitoaxial"), 2)
          87.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('unjokingly` uninterpreted fa\\cula en@tepicondylar co.ntabescence corrup}ting* unallowed unindifferently synenergistic', 'unjokingly` uninterpreted fa\\cula en@tepicondylar co.ntabescence corrup}ting* unallowed unindifferently'), 2)
          88.89
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('absolute f<ritter s)tays rhizo.morphic_ "petiolulate inwand}erin#g', 'absolute f<ritter s)tays rhizo.morphic_ "petiolulate'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("unders!itter prec:redit diphenol 'yolkle[ss dout#.", "unders!itter prec:redit diphenol 'yolkle[ss dout#."), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('nontec[hnological bewitchful s"oaple|es p,hyl.actocarp vecto"r corpor\'ate~ froufrou variforme@@d pean', 'nontec[hnological bewitchful s"oaple|es p,hyl.actocarp vecto"r corpor\'ate~ froufrou variforme@@d pean'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("arth+ritis inter>m'undium @snu[p overspa#n micro/dontism ti<rednes)s", "arth+ritis inter>m'undium @snu[p overspa#n micro/dontism ti<rednes)s"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy(':coxco%mbry cyclopentene tub!;ik sur(tout crimpy^ twister unne^phritic subjectivism unraised', ':coxco%mbry cyclopentene tub!;ik sur(tout crimpy^ twister unne^phritic subjectivism'), 2)
          88.89
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('widower{ship uteroplasty e%mpyreumatize ;conceptuality pancrat{ic #saprophagous hemichromatopsia@ kaja_wah +prebrut#e', 'widower{ship uteroplasty e%mpyreumatize ;conceptuality pancrat{ic #saprophagous hemichromatopsia@'), 2)
          77.78
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('b*anteng ne<math(ecial missing )refugee car,a+melen re_ctocele', 'b*anteng ne<math(ecial missing )refugee car,a+melen'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('s/ymbranchiate@ cloy extraprovincial unassu&redly benzo_y*lation tearthum}b@ apprentic)e ?risque pedicul^ophobi;a', 's/ymbranchiate@ cloy extraprovincial unassu&redly benzo_y*lation tearthum}b@ apprentic)e'), 2)
          77.78
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from typing import accuracy
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
