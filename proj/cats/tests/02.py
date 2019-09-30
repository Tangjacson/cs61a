test = {
  'name': 'Problem 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> dogs = about(['dogs', 'hounds'])
          >>> dogs('A paragraph about cats.')
          False
          >>> dogs('A paragraph about dogs.')
          True
          >>> dogs('Release the Hounds!')
          True
          >>> dogs('"DOGS" stands for Department Of Geophysical Science.')
          True
          >>> dogs('Do gs and ho unds don\'t count')
          False
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from typing import about
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> ab = about(['neurine', 'statutably', 'quantivalent', 'intrarachidian', 'itinerantly', 'cloaklet'])
          >>> ab('unhollow simsim dcloakletB itinerantly cloakLet dQUaNtivalentJ gnEurinE fissiparity Mneurinel')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['pomacentrid', 'snary', 'related'])
          >>> ab('Urelated pyrexical ure"+lated tasmanite relAteDT snaryf imputedly')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['synoeciosis'])
          >>> ab('snap esY=*noecioSisy unshameful algesic theomorphism ger')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['cliffed', 'infrigidate', 'euphemizer', 'curare', 'hungerless'])
          >>> ab('infrigidate shoesmith hHuNgerless curAre euphemi.zerL infrigidate gridelin')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['omniscribent', 'orleways', 'tenure'])
          >>> ab('mononucleosis Uor_l(ewaysE dorleWays ko<r-leways o_mnIscribe=ntU omniscribent')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['ignore', 'quarrelsomely', 'colauxe', 'allodelphite', 'wherewith'])
          >>> ab('manifestatively lquarrEls*ome]Lyg Uallodelphit#eE Hall~odelp+hitew UwhErewit_hm')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['repattern'])
          >>> ab('zr[epAtTeRn!e repattern occasion repatternm retiredness yrepatt*ernt')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['curlicue', 'revetement', 'retributor', 'natatorial', 'limuloid', 'anthropomorphological', 'gastrogenital', 'plang', 'immunogenetics'])
          >>> ab('marquisship natatoRiaL politeness ILImuloi[d} anthropomorphological hypocaust')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['quartole'])
          >>> ab('malaprop L>quartole+ q%uartOled fossillike inspection')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['yauld', 'semiblind', 'batsmanship'])
          >>> ab('VbatsmanSh^ipT slipped Yauld redbreast epexegetically batsmanship assoilzie')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['veilmaker'])
          >>> ab('tveiLmaker inheritance Y;veil)maker sicklily lveilmaker worldly AvEi+lmaker observative')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['parepididymal', 'prizeworthy', 'visorlike', 'sealery'])
          >>> ab('GvisorlikEx pArepidIdymall seAleryf prizeworthy visorlike pictorialize parepididymalt sealeryv')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['adelphogamy', 'peeringly', 'incontaminateness', 'steelworker'])
          >>> ab('muscle prosecute steelworker steelwOrkera diolefin')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['anticombination', 'lubrify', 'fellowship'])
          >>> ab('cloriodid proboscidian oanticombinationV lubrify f/e_llowsHipg JLUbr$ify%k aNticombinatIonN amphithecium ffeLlOwshiPE')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['groundman', 'preconstruct', 'predevotion', 'countersign', 'cop'])
          >>> ab('}c]opF gasterozooid prEdevotiOnq gprecoNStructC coPl cellobiose')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['misericord', 'woodenweary', 'swarf', 'cardiotoxic', 'noncontraction', 'uncheerable', 'titman'])
          >>> ab('woodenweaRyA engrieve carnivoracity eNoncontracTion magnify woodEnwearyf dogeless')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['unimpinging', 'deheathenize', 'zeallessness'])
          >>> ab('operettist zeal!Less{nesse misoneism megaweber zeallessnessk pare xdeheAthenizeK scleriasis un*i*mpingingn')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['velvety', 'unitarism', 'dult'])
          >>> ab('unita%rismP pdult funitarism sunitarism nonimprovement electrosurgical')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['glucosidic', 'atomize', 'salpa', 'taxer', 'pilpul', 'mythopoem', 'ooplast', 'gaming'])
          >>> ab('a&~tomizef NgluCosidic atomizeJ WGam<iNg atomizej ooplast')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['shovelweed', 'intersect', 'radiator', 'echo', 'dratchell', 'stereochromically'])
          >>> ab('reshunt wshovelweedV overweep y@ech)op unifiedly trimethylene')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['pronephros', 'archaeolatry', 'organotrophic', 'remediableness', 'blistered'])
          >>> ab('waremaking gynocracy interracial Porga?>nOTroPhicE qPronep=hR+os bli:steredp Horga_notropHicl')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['author'])
          >>> ab('cleck gauthor isochor interchangeably autoceptive studerite')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['unpleasantly', 'staggerer', 'maritally', 'exactly'])
          >>> ab('MunplEasantl[y unpleasantlYq unpleasantly eXactlYU exactly QstaggererN stag[gerer(')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['nonrestrictive', 'kittle', 'isolecithal', 'abettor', 'puckerel', 'goalee', 'vallidom'])
          >>> ab('moodily nonrestrictive ;puckereLu +vall`iDomd ekittlee puckere-l abEttor nonresTrictiVe WPuckeRel')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['skills', 'superincentive', 'phrenic', 'punch', 'flatboat', 'beansetter'])
          >>> ab('waldmeister hsuperi\\ncen[Tive u>phreni[Cs xpUnch toatoa epithelium suPerincentiVe')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['alloxan'])
          >>> ab('calorimetry orographical stranger autopelagic weblog')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['drum', 'unglittering', 'oxyrhine', 'matriliny', 'pilomotor', 'windless'])
          >>> ab('pilomoTorr yunglittE/ring oxyrhine Rdru)"mL carbodiimide Zpilomo@/torQ @druM(Z drum AwinDlesS')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['coharmoniously', 'adiaphonon', 'nonsubstantial', 'adding', 'loiteringly', 'electropathic', 'bombinate'])
          >>> ab('electrop#athi{cr anonsubs!tantialX amphidisc eele#ctropathick endamask adDingO zbombin<atE')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['tickleweed', 'intestate', 'membranaceous', 'retire'])
          >>> ab('coronillin retiret diffame serosynovial trailingly')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['wholeheartedness', 'muffishness', 'intergossip'])
          >>> ab('namda iNtergossipj apprizement kiNT,ergosSIpd objectives')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['generation', 'granospherite'])
          >>> ab('granospherite Pgener;atiOnR mgranospheritef compulsoriness dredgeful')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['feticidal'])
          >>> ab('subendocardial bursiform battarism womanwise ectoplacenta recontemplate jfeticidalW')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['enfeebler'])
          >>> ab('oxycellulose enfeebl>er spiritleaf retiral statued enfeeBler reloan')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['tetrander'])
          >>> ab('bromiodide uncircumspectly impeccancy unsignable aftershine')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['dozer'])
          >>> ab('$doze(rD angrily tralatitiously nonmineral mdozerQ pdOzer encrimson id/o#zerf')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['pretensive', 'redivide', 'noctuid', 'exorcisory', 'cation', 'unoffensive'])
          >>> ab('p>retensivEH zexorcisory OexorcisoryC persicot cyclotomy')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['anticonscriptive', 'extorsively', 'lathyrism'])
          >>> ab('prase anticOn}scr;iptIveM SantiConscriptive mid anticonscriptive hetaery zlathyrism')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['aconitia', 'bioclimatic', 'lithemic'])
          >>> ab('sardonical unwakeful Gbio.cLimatici surmullet consist')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['rove', 'geek', 'gunlock', 'ecdemite', 'diadoche', 'aggravatingly'])
          >>> ab('ca@g%gravatingly unamicable surgeonless advocate Rgeek-= gunlockO')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['nagual', 'schriesheimite'])
          >>> ab('prevaricator tortulaceous reddleman quintillionth gN_ag+Ualj average spinelet')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['tronc', 'uptear', 'carcerate', 'acromicria', 'contumaciously', 'limbous', 'diaconicum', 'enquicken', 'unnovercal'])
          >>> ab('CDiaconicumR dia\\cOnI[cum ca$rcerate<x uptear carcerate^I XunnovERcalF jcontumaci*ousl^y')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['hogweed', 'cinchophen'])
          >>> ab('Rcinchoph|en dolioform ho/gwe(ed unsauced heathberry')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['unhampered', 'importunance', 'unempaneled', 'pulldrive', 'jailering'])
          >>> ab('importunance repudiation wickedish >pulldrivE"A p&Ull$drived')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['rollable', 'attractively', 'remold', 'blepharocoloboma'])
          >>> ab('tariric rollable antefix attracTivelys yattractively battract@iv$ely')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['decisiveness', 'amissible', 'comply'])
          >>> ab('disincrustant damissiblex Nami(ssi-ble pAmi:ssible cortication diazoaminobenzene stepgrandmother decisiVenessZ ami|ssibleF')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['camshachle', 'cohortation', 'platinum', 'maidenly', 'fossilify', 'unfunnily', 'oilskinned', 'distrustfully'])
          >>> ab('ca$mshacHleo preministry unfuNniLyA pma%IdenLyV YdistrustfuLlY')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['polysemous', 'avodire'])
          >>> ab('avodir$e$ avo;dire parvirostrate slue villanage petticoatery yav/OdI!reU DaVodiRe')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['tapinocephaly', 'sequences', 'unextorted', 'counterdistinction', 'scorbutically', 'synapticula', 'rhodonite'])
          >>> ab('}RhO~donite unextorted zuneXtortEd>H hunextortedJ sequences jcounteRdisTiNctiOng')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['appropinquate', 'perlitic'])
          >>> ab('perlitic perlItic perlitic nirvana tartramate unlittered labrosaurid lineated')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['pseudohyoscyamine', 'variform', 'duskly', 'uncarefully', 'dale', 'opeidoscope', 'insulary', 'milkeress'])
          >>> ab('uncarefullyy variform XiNsuLa?ry`y v!arifor<mJ Apseu#.dohyoScyAmine')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['covibration', 'nipple', 'sublevate', 'engine'])
          >>> ab('nipple dnipp`le< gorged disintegrationist sublevate')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['dale', 'snurt', 'vagiform', 'neurogenic', 'shingly'])
          >>> ab('sNu~r)tU ascarid Kvagiformh netted vagiformQ snurtb subserous')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['pathologic', 'pedunculated', 'tinful', 'dotardism', 'nonvisual', 'nable'])
          >>> ab('hardihood hpeduNculatedz KtinfuLJ RnabLer hdotArdisMV tinfulW joel')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['grudge', 'miscast', 'polypragmon', 'peristole'])
          >>> ab('gPolypragmonv mIsca~sTH miscast bperistoleK hgrudge')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['spermogoniferous', 'tasteable', 'neonomianism', 'sociable', 'premandibular', 'overrapture', 'baruria'])
          >>> ab('TnEonoMianismT opremandi{bular baRuriaU Vpr}EmanDibular FneonoMianiSm')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['chapatty', 'usury', 'inlooker', 'planaridan', 'retrogressionist', 'supermagnificently', 'kolokolo'])
          >>> ab('in?;loOkerb chapattyh vcHapattyt triangularly yusuryS crabwise')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['paucifolious', 'tomb', 'rely'])
          >>> ab('paucifoliousA y*rel$y hpAuciFoLio]Us rely tomb')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['tuitive', 'nonvalidity', 'individualizingly', 'templarlikeness', 'saltman'])
          >>> ab('St&emplarLikeness teMplarLikeneSsm nemathelminth nonvalIdityN s|a&ltmano')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['perseveringly', 'needleman', 'yonner', 'submaximal', 'impersonatrix', 'pauperize', 'overwrested', 'twinebush'])
          >>> ab('ambisinistrous LperSev!eringly fictionalize needlema(nF counterscoff hearts JpAuperize sorcer shelfful')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['inosite', 'dragoman', 'unsolemnized'])
          >>> ab('broccoli dragomAnt junsolemnIzed noncranking AinositeN bdrAgo<m[anT dragoMa`n ldragOman')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['morphonomy', 'pretext', 'annexa', 'triphenylmethyl', 'platinous', 'audience', 'thoroughstitch', 'secured'])
          >>> ab('Cprete#xtk EtriphenyLmethyl yam hmorphonOmY thoroughstitch zpret#e]xT triphenylmethyl finals')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['bowllike', 'kanephoros', 'gigster', 'adscendent', 'gynandrosporous', 'res', 'metrosynizesis', 'aquicultural', 'orotherapy'])
          >>> ab('Dmetrosynizesis Ures MgynanDrospor^ousS gigster metrosyNizesis')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['reject', 'ruga', 'myriologist', 'chint'])
          >>> ab('hoga lacmoid #Chint ruga rejectT chint')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['awkwardness', 'collop', 'sphygmographic', 'twaddling', 'kissar', 'synchronizer', 'paleoclimatic'])
          >>> ab('fsp`hygmo@grAphicH tw\\addli/ngv crazingmill twaddlin^gG Ssynch^ro{nizer')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['persecution', 'philhymnic', 'replantation', 'rouille', 'pneumatogenic', 'separate', 'chid'])
          >>> ab('replantation Ssep]arate persecution dihysteria roUillE nonvirtue ?ch:iD')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['miscolor', 'millinormality', 'bluffy', 'clan', 'volumometer', 'durability'])
          >>> ab('hmillinormality dime YdurabilityU unsanguinary OclanB')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['priest', 'spumous', 'redemptress', 'gnomide', 'melagra'])
          >>> ab('Ppriesti f/priesT gnomIdeq full Mgnomide floating')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['loined', 'armstrong', 'engarb', 'hexosemonophosphoric'])
          >>> ab('XhexosemonophosphoricE hexosemonophosphoric BhexosemonoPhosphoric twistiness loined hexosemonophoSphori[c$ digressingly ungarrisoned')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['specificize', 'bodiless', 'postglacial', 'soleas', 'pty'])
          >>> ab('KbodiLesSQ splatterdock ssoleas grateful Lsole{asc pangolin')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['abelmosk', 'strunt'])
          >>> ab('alcoholmetric abelmosk strunT` pyxidate strunt parachromatism')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['upstrive', 'silicean', 'attentive', 'antiprimer', 'uredosporous', 'dense', 'consumingness', 'sainthood', 'televisionary'])
          >>> ab('antiprimer attentive atten+tive xured_osPorousM televisionaryn')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['cadential', 'turnipwise'])
          >>> ab('sphericle curassow mcade&ntiale moner protestant')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['resanctify', 'pence', 'kneehole', 'columbium', 'substructional', 'overkind', 'incipient', 'antecubital'])
          >>> ab('incipient vincipients incipieNtB AntecubitalU Ik$neeholeT wiggen kneehole QkneehOleg kneeh$olek')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['grossular'])
          >>> ab('actinoelectrically lightboat gro>sSular counteridea hgrossular lactovegetarian')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['counterhaft', 'unfeasted'])
          >>> ab('hookmaking KunfeaStedH tyrannical perusable counterhaft emphyteutic psoriasis')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['intubationist', 'disreputable', 'flirtishness', 'licheniform', 'littling', 'immutilate', 'forestaysail', 'hypostrophe', 'unparliamented'])
          >>> ab('unmollifiably snowish silicoflagellate birchen imm|utilateq isophylly LittlingI exportability')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['trichiniasis', 'resilifer', 'galilee', 'apoharmine', 'circumgyration', 'allicient', 'nonarithmetical'])
          >>> ab('malmsey ,galile\'e tnonarithmeticalD wapoHarmineQ apo}harmi;nE unon^a"rIthmetical')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['symphonize', 'hydroperitoneum', 'glistening', 'impenitible', 'consultor', 'orbitotomy', 'plutonomist'])
          >>> ab('zymome timpenitible BglisteningY macaronical tackleman')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['ramificate', 'taeniiform', 'trepidness', 'unsubscribing', 'caliphate'])
          >>> ab('orohydrographical taeniiform trepidness$d ktrepidness trichuriasis t>repid^neSsx')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['gunnery', 'ceraunoscopy', 'glycolic', 'patella'])
          >>> ab('Qglycolicd qg&unneryj topiarist endobatholithic coccal')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['playfield', 'unwarming'])
          >>> ab('normated unmerchantlike faunish allophylic mottolike Xunw\\arming\\')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['stonishment', 'lapstone'])
          >>> ab('gla}&pstoneW anfractuous balustraded A=stonis\\Hment idiomatic')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['cephalotrocha', 'subworkman', 'simplexity', 'humilitude'])
          >>> ab('rhapontin poleman Dsubwork[m`an sim$plExityG PsimPlexitym baksheesh')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['orchiocele', 'authentic', 'wr', 'wrainbolt', 'recompensive'])
          >>> ab('XrEcoMpensIveL fodderless Nwrainbol~t uncounted incudectomy')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['semilanceolate', 'apogaeic', 'tapirine', 'cankered', 'corpse', 'ms'])
          >>> ab('FT<aPirinep cankeredJ vap_ogaeicU tapirineo Pco!rp)se Rsemila*nceolate autoicous orthogranite')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['incurability', 'weretiger', 'abecedarian'])
          >>> ab('iNcurabIliTyX unuxorial Yincur>ability}k AbecedariaNT anthecological weretiger JwereTiger beclamor postlabial')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['increately', 'fraxin', 'chorionic', 'infect', 'ochro', 'pantaletted', 'tranchet', 'undear'])
          >>> ab('chorIon>i*cy RfrAxIn UfrAxin tranchet oincreat>e~lyM')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['occult', 'paronomasia', 'overwalk', 'pathfinding', 'subcaudate', 'indexically', 'thiocarbonyl', 'preconcession'])
          >>> ab('Soccu=lt PreconCeSSiONv pAthfindingr XpathfinDin\\g gprecOncessiong Jp`re?concessionM sweethearting')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['avadavat', 'superintendence', 'gypsite', 'categoricalness', 'defloration', 'highjacker'])
          >>> ab('gerent gsuperiNtEndence Rh~ig\\hjackerM highjackerl divided avadav)at higHjackE+>r DGypsitek fsupeRintendenceQ')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['booklover', 'impressibleness', 'barrack', 'cornified'])
          >>> ab('pirr sprout e$COrniFied_R shopkeeperish gcornified')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['cryophilic', 'tesseratomy'])
          >>> ab('hcryOPhil$ic conservatorio dialystely oxalonitril wagger lucriferous')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['settleable'])
          >>> ab('settleable settleabL(e} wettish syringomyelia screened sanctitude')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['cockthrowing', 'hypomorph'])
          >>> ab("arthur ecockth$rowinG ZhypomorpHF presentimental IC~ockthrowing gcockthR'owingh teleosteous makers")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['factuality', 'mirthsome', 'wreathe', 'foreshock', 'hitchhike'])
          >>> ab('jMirthsomeK wr{eathe Dfactual*ity antivibrator T{factualItyp lmir<thSome')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['nicknamee', 'mi', 'predisagreement'])
          >>> ab('ravelin fpredis#agr%eemEntA mi Vmi nicknamee hilliness')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['archband', 'inpardonable', 'downshare', 'draftee'])
          >>> ab('aRchbandb xinPardon*abl}e reminder unifaced cynegetics drafteeo drafteeX circumzenithal')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['hearse', 'heortological', 'cinematic', 'malchite', 'unpunctual', 'dissepimental', 'reviver', 'drapeable', 'tiffy'])
          >>> ab('palpulus interosculation un&punctualU jungle complexionist tiffy')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['aslumber', 'coking', 'labiograph'])
          >>> ab('preventible genapp floroon RlaB-iogrAph sudatorium labiograp"h labioGraph')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['redifferentiate', 'seetulputty', 'besoil', 'clad', 'bicrenate', 'lowering', 'ipseity'])
          >>> ab('clAd{: seetul&puttyr besoIlB laniform vseeTulputtyz clad Fclad`o ipseity')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['autointellectual', 'photodromy', 'zoeal', 'gainly', 'gumdigger', 'phyllocladium'])
          >>> ab('equipment gainly tarradiddler platinum programmer')
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from typing import about
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
