# TL,DR: 9
AKA "Attack of the Bignums".

To do: get last digit of 2017^2018.

Tried methods:

1. `math.pow(2017, 2018)` ->FAIL. `OverflowError: math range error`. Obviously, the `math` module is doing something overly clever.
2. `for i in range(2018): n*=2017` ->SUCCESS. The result: 9.

For completeness, 2017^2018 is equal to (bignum incoming):

`787957136670982482675695039517959047047596688714403112524376487608279928726729730075911551273406186899142855126591877736417977968493443155779560015222369761333246442574144353867415912919634745895710769124487115103294079713583091112754890355078005853990581540994735208347804827185761749006437355068540585585362246896983437675760170750032501716073704194681809344705367279875664599666246911861378500524366640721317944210544594405221809167075528947444346771143848903677575399991630299848556866643499411870674243109208490006647501672921371680713260188889430621611106727421130614197756639580932506215894918420093697447486910042186684864815326347738573031814033708528836256092184602350432305838427833135229721336559540140935151859422738829453167097168549469129954226761538014664485605101569689706336226312966635895145632182875126315706577581379016201928673352905691393291106621328181347138213996663801819724205023160732742459325788169483852831395172432595143361486569049374590535266498340716787305720686281560210239769433601761608740129259314539574855541973680137979181872356425895999383939708117823437077826401458097965206115969509657246699730568960938167681456579379792307597084210786562239623377120213269334628715073878693436928838829253606163909856137364621089404476603345584219519866560244949437601662494642437822860305786730019710195651686157232281520977840073146655449520753817602834111041891915204137569435367802056901433610875422511636749276186614408281410015795830277308673628880450120328752012389096434755885274446908136941798656395889716068364529544070718638586230121718875840628217345604107983856285617039511603406815614638767687745376404343105331878450549253971462964387773306153566630674840374532484010284466314569633599127797421487246463952756669564659558669079793559800747558797837841474499469976596639880120405310649191169842454136697816181442098401676387054579206647166597982689565650978146693884790208132020379328189009610027878631946133862531592239341801130419358347908820871088500360904650546410983807079509161512856763931141826096779136890425936192318858255971485254370410129805711769933311871677505444139662204748280725195792892852548521606877360210077542432475004085467568613867691051221194726235801983612118543462156372276552589270713886217263120258267554549618355318036093466566963653016571826155249815841472774791040738788606414147621783047043493464953291228933055296969452529023308868190502999133117161276500976579289709785699962781757291033948035948862083643436542103698704662223062871075243240519798256660492453597995165716255285489257946672282932308324153950871208274576938877625184215620798046441709948658134604001937001176731745686190292999282978984274907745748434790235861824019666586609249519776664986439359588280777881607710439001602143718721726935422014890123106374223705898732918511213307698533020567403727487230290789843961071396877939946572579638825418869591768831099035740196357268749791480043041918047403473306510507612016936007966105345491545957532799396944926416816019983677955472949264650381831712231344132405649058282115696581334905937716853332283314427534141215813859223607323961247047758193583212644080344659694016673979151029701609973351222055698229124292569229328011018233359916992501555679409114611952030330078185135471011316537914686355515129258117581134133569267013745092709884073868722522834283411343867050461544109477554638650463355122486611693928450754286480903488914904776667371620285226703850412463688335362863713186488065879305457671830549513947651672772342688255995164927255836275067870143462717840407134691472661019119753468167882915086173819434456414718521626518630168243012613778951287746039311986001944315284806855195577732949256061063533088510328708032028965285249636321829359905234269878543362688336640798140669612017033476253249563529072584302922863606123001705755748856491343760162141780071181953139665888724755565336475626443598744606199400534950349207300917340918210225913943848617387675039603230210845054044835572287816618264832691315845379337888932510889274761386839898156555830525572108782689729532575119496237774060679118188849265098115063370018634197699667179682137479227845502010325452545552776600172634082601256052063449964751892730503956866249526088394733489857380189396097039232357576008171667030704779486637051119598344007959947579064182340987142046981488576411002461827500001109571338707334178227586972934230995594600268638530329632060505174634458473260838878873347192665521146687834987663443694598172872075997350382433383827735899470759756887948143807277541240549015889309794922509227574581186617911271758704635748203076550553173872832338899700040743557674442413924281026769782880070501424861201319231085126460288662047445345429767554980513336519465778949394369189464302497931572419642312285069562757193338398714713935037311954325909408766736046353768712145044743481759999784133499284398428528065455087862428006345109727428686690366234198785276975810406101152159068832677174982510129762112956028010206709798660160980913355370254051880012509256263902234416948473478567747780531059546590050422506627974404611836772319610159212435145344942193404924465861779932137138973317022557015339334271518248534864225171475606151982926470572180856418020190216329026723947377241406126493534927392718040339729546942547191986702369293463559572260682351600921210212023728561307499885079268387652563784683778171757624085110176737908399761094300143599941214536086714836630145207437295824073896599362999855319789260485922192656207040111519253290744252319153572611470725992554882453212139944393996388714423829536627761323296582090127398660160951580461082327881222494620236236183658710778070424648722935559958354501670187507162979537010012352907691437386655727441584903250860865153047540909048330983697073307211973503134163732009008550396333608232657124812640946465014579525477941942556949274543643812455527015281231408925630094792474271881295897193763364032212846460534776788960769539741863646694490013595546951223952798867435271952936203999960240518565275279260782085141812965691027203803600735981539351670854568194700518650332732548744927656029151549091954093526683244224512391993697987621731999123527230452918488187983319019944655613751531696978645384720378498433348107530130149699073555704604365200121201971527729537012515646701166301280146475648932865891007739337625152005710116953232083463204721869063221348874680455014227054003446837414240946109154431332515587056504626286967991790550573216433003320328225764752489452861211063828668767153375905867129565823073078267335221773924705505393237000005646788618648109853978961054605639823137526577273286465473361473061135205139239691096240938292170540279393404803009`