import math
import re

data = [('neg', "http://twitpic.com/664b7 - miss my bestfriend :\'( now she left school"),
        ('neg', "@shaundiviney i didnt get the msg!! :\'( but i bought princess"),
        ('neg', "@Jack_O_C I\'m seriously screwed  I haven\'t studied at all!!!! :\'("),
        ('neg', "&quot;I\'m giving up on you. I don\'t care how you mess up your life now.&quot;... :\'("),
        ('neg',
         "jake thomas looks so precious :\'( i hate when they say &quot;there it is i see the white light&quot; in every ghost whisperer show"),
        ('neg', "@_YoureMyHeroine :\'( i really know how you feelin. i wish i could hug you"),
        ('neg',
         "im well bored  had a great half term and i dont wanna go back to school on monday :\'( enjoying the hot weatler lo0l ;)"),
        ('neg', "@billbathgate im not a doofus  it could happen wahhh!!! :\'(!!!!!!!!!! im on my break!!"),
        ('neg', "Manchester was wayyyyy to busy!  so warm today also! :\'("),
        ('neg', "@RobynHumes Can\'t  Bro on laptop &amp; Salm on comp! Me stuck with Wii :\'( xx"),
        ('neg', "@iamdiddy I need a hug  I\'m doing my junior cert this week and I\'m totally stressed out :\'("),
        ('neg', "@danger_skies miss you too :\'( it is!i never want to come home.....seriously"),
        ('neg', "the suns gone  hopefully nice weather tommorrow. ALL THE WORK IS SO DEPRESSING! :\'("),
        ('neg', "going out  I can\'t do this crap anymore :\'("),
        ('neg',
         "im not happy   my ipod or laptop dont know whih but one has decided to refuse to let me sync my songs :\'( how can i live without it :/"),
        ('neg',
         "Awww that lil girl on bgt :\'( when they said she didnt have time :\'( that was soo sad  and them huggin her"),
        ('neg', "@mileycyrus i wish i could meet you once  do u think this will happen someday? :\'("),
        ('neg',
         ":\'( big brother in 4 days! This means constant live tripe on e4 and no scrubs to fall asleep to! Not happy"),
        ('neg',
         "Its coming out the socket  I feel like my phones hole is not a virgin. That\'s how loose it is... :\'("),
        ('neg', "What I\'m gonna do  life is not good:\'( no more Exit in this hallway I\'m stuck in my world..."),
        ('neg', "@marting05  I know... he\'s mad at us... :\'("),
        ('neg', "&quot;your true theatre calling? - musical theatre actor&quot;  i wish :\'( xxx"),
        ('neg',
         "@gimboland sorry change of plans for me   :\'( revision for monday exam in a park with one of my friends"),
        ('neg', "ok... twitter I almost pass out because of you!! bastard    :\'("),
        ('neg', "@TheNewBradie my tvs not working  i wanna watch vhits :\'("),
        ('pos',
         "@DavidArchie &lt;3 your gonna be the first  twitter ;) cause your amazing lol. come to canada  would do anything to see you perform"),
        ('neg', "@__sugar oh no  i am always here ;) &lt;3"),
        ('pos', "@kaseypoteet LOL yeah yeah you big perv ;) Was hoping to see you next week but scrapped plans"),
        ('pos',
         "@mattpro13 Maatt Havent spoken to you in ages dudeee  Dont forget bout ur Aussie fan  ;) lool. Love ya xx"),
        ('neg',
         "@hot30 i want to! but im not over 18 and t&amp;c says over 18\'s only  wanna make an exception for me ;)"),
        ('pos',
         "just got Up and going to get ready to go to meadowhall ;) can\'t believe my internet broke yesterday  GUTTED"),
        ('pos',
         "hmm..Osaka. Last show today.Very sad  . i can decode ur msg ;) haha cant wait till u get 2 Sydney ;D i missed out on tickets tho :o xx"),
        ('pos', "Lobbying in twitter! Here too!!  Yuk! Gettin rid of groupies ;)"),
        ('neg', "@MAVinBKK I know but the wait will be worth it - November just seems so far away at the moment  ;)"),
        ('pos', "Raining...  I missed the rain so much...  I am grateful for it ;)"),
        ('neg', "@billbathgate ....any  sorry wahh!! lub u toooo ;)"),
        ('pos', "I am sick  but Ians coming over so its all good ;)"),
        ('neg', "@theguigirl Awwww...thanks!! ;) Unfortunately"),
        ('pos',
         "@xXHAZELXx: Ok its suppose 2b followfriday not unfollow Friday  aw well I have nice tweeters anyway! &lt;-almost doesnt sound right...lol;)"),
        ('neg',
         "im well bored  had a great half term and i dont wanna go back to school on monday :\'( enjoying the hot weatler lo0l ;)"),
        ('pos', "NOOOO!!!  &quot;thehannabeth: i have a crush... ;)&quot;"),
        ('pos',
         "@nattymsmith awww she\'s laavly ;) I had to come in  but I\'ve got a stunning wee tan (l) ;) yourself?"),
        ('neg', "@CursedChimera; Re: Home - that\'s exactly what I meant... home in D-town. ;) Also"),
        ('pos', "@MissShell20 eeeeep so jealous ;) I\'m at work  um"),
        ('pos', "@christa42 you mean the post concert blues ;) *lol*  Well"),
        ('pos', "@mike03p IM SOWWIE I WAS A LIL LATE  LOL it looked good though ;)"),
        ('pos', "@nick_carter  awww poor you  - but you know ... you\'re doing it for US - bless you ;)))"),
        ('neg',
         "@thewhitemage It does it sometimes - it should come back ;) And the car thing sucks - I feel all anxious and yucky now"),
        ('neg', "Next weeks dlc is fail  Can\'t wait for Maiden in two weeks though ;)"),
        ('neg',
         "@reemerband Hiyaa! How was Tour? Really disappointed that I couldn\'t make it   Hope your all Dandy ;) xxxxxxxx"),
        ('neg', "@Dayna_aka_Rowan he could be talking to me  (he\'s probably not though ;) )"),
        ('pos',
         "@princesspooh90 Yeah but it doesn\'t sound indie enough  i need2learn some other tunes and then pick up mo style =] 1hour! I\'ll c u then ;)"),
        ('pos', "@laydmaxix aww  i will keep sending it ;)"),
        ('pos', "@sunshineangel89 Yeah..  Of course next time. ;) ICQ?"),
        ('neg',
         "@letter2twilight LMAO! I don\'t fake being Paris anymore. Look at my bio ;) and by the way I can\'t log onto your forum..."),
        ('neg',
         "I shrunk my favourite cardigan.  Hubby said he\'d buy me a new one. I practically lived in it and it\'s gone. I shall say a few words ;)"),
        ('neg', "likewise @Buttahbrown you better ask about me ;)  I don\'t appreciate you neglecting the sir fresh."),
        ('neg',
         "@smaknews sorry about that anna wintour repeated tweets!! sooo sorry  somethings up... | was wondering abt the quad tweet ;)"),
        ('pos',
         "@welsh_lottie Not one of my favourite pastimes  This weekend is a long weekend here so Monday I\'m off to an Ice Show w/ the G/daughter ;)"),
        ('neg', "wanted to go to the club...dancing;)..but now iГЇВїВЅm tired anyways i have to go to work tomorrow!"),
        ('pos', "show was amazing. so cold out now  hope I can give victoria my card and get my dvds back ;) ha"),
        ('neg',
         "@Jamiebower  you should come to Chile and your band too;) why everything  happens far away from here?? lol we\'re losing good live music!"),
        ('pos',
         "@montiAsutton I wish I could really do that  I love having u around! Ill see what I can do.. ;) try to use that national champ pull lol"),
        ('pos', "@janetfraser so true   sad to say.  I\'m glad you\'ll be with me to be my support group ;)"),
        ('pos', "@spjwebster wish @njwebster was coming too  I guess we can make time for you though if we have to ;)"),
        ('pos', "@NanaSuzee i\'m on my mobile so it won\'t let me  but i can\'t stop thinking about you ;)x"),
        ('pos',
         "because he @the_real_nash wants to be an honorary Filipino  i\'ll follow him now ;)) thanks @daxvelando!"),
        ('pos', "@marygrrl aww  loves you! way too cute ;)"),
        ('neg', "@jordanknight TINK! (whatever the f**k it means!!) from your JKUK girls! Show us some love! ;)  xx"),
        ('neg',
         "Redford - Sufjan Stevens ][ for @yoochun ill make you cry again &lt;3  @mimacruz sure no prob slugger ;;) add th... ? http://blip.fm/~5jdtm"),
        ('pos', "Thanks to all who follow me  ... wish ya\'ll the best ;)"),
        ('pos', "@taylorswift13 oh great!  hope you\'ll have a blast there! ;)"),
        ('pos', "@datadirt hahah  okay then thanks for this short explanation ;)"),
        ('neg', "@QueenieCyrus morning miss sarah cyrus ;) WHAT\'S UP?  x"),
        ('pos', "Happy Star Wars Day  May the fourth be with you ;)"),
        ('pos', "@deanomarr Italy or greece for me  Love Italian men hehe ;)"),
        ('pos',
         "@CyranDorman Woot! I have created something inspirational! ;) Look forward to seeing more of your writings"),
        ('neg', "gooooodnight  i fully gave up on my english. pride and prejudice. love the movie HATE the book ;)"),
        ('pos', "@ckanal funny you should say...am filling it out as we speak ;) cheers!"),
        ('pos', "i\'m off to see a movie (&quot;17 again&quot;)"),
        ('pos', "good morning!  i hope you all have a good day today!! although its a monday... be positive! ;)"),
        ('pos',
         "@bombchelle512 happy birthday  and @joemwestbrook congrats  wish you were here for your lady..ill take care of her;)"),
        ('pos', "@emilyosment http://twitpic.com/48gy0 -  He\'s Well Cooool ;) Lovve The Ro&amp;Co Shoooow"),
        ('pos',
         "@SteveHealy - I shall post a notice in town so us Cork ladies know to watch out!! lol  You had fun then?? Sevens were the business !! ;)"),
        ('neg', "@sensualbodyrubs Hope you get your car today   Hate anything that stops me from my work ;)"),
        ('pos', "@TheOlifants  de wereld need more ppl like you! ;)"),
        ('pos', "excited how the jon does will do today  Good luck guys ;)"),
        ('pos', "14:14 .. someone is thinking of me  good luck to lynny and her tattoo ;)"),
        ('neg',
         "10.11PM~ todays a drag for me. so bored. im about to get into the romance book so i prob wont be on til the morn  night twitter babes ;)"),
        ('neg',
         "@leannarenee hope sequel edits go well   me and my notebook will be looking for a place to sit after pt ;)"),
        ('neg', "@tsarnick Ohhhh I don\'t know ;) an older mature lady?"),
        ('pos',
         "@amorphia delegate  I am now eating pate on toast a my wife is editing yesterday\'s engagement shoot ;)"),
        ('pos', "@dannywood ...hey danny .. did u run already ???    hope you have a good day ;)   i love you !!!!"),
        ('pos',
         "@absolutspacegrl I could feel the excitement in that tweet! ;) I\'ll be watching the launch on NASA tv! How I love my directv!  seriously."),
        ('neg', "@ianweiqiang Interesting Combination  Have a great one ;)"),
        ('neg', "@Helmuts hey helmuts!  im ratty if u remember me from scootertechno.. ;)"),
        ('pos', "@Raderr but yeah i like purple maybe thats why!! ;)  :p :d"),
        ('neg', "@readerwave if I know what you want it is easier to please you ;). I am glad you mentioned it"),
        ('pos', "@spazzyyarn he totally got you! ;) i think it\'s awesome."),
        ('pos', "it\'s after 3 AM.!!  I think it\'s time to bed.!!  have a good night twitts.! ;))"),
        ('pos', "@NeilMcDaid looks class the water splash looks so real  looking forward to my review copy ;)"),
        ('pos', "@LifeByChocolate alredy had my chocolate  it is impossible to resist ;)"),
        ('pos',
         "What a beautiful day! Hangin with the guys Graham and Josiah  lol waiting for the others. If you wanna stop by come on over ;) with food"),
        ('pos', "@wendywings cute   Time for a twitpic ;)"),
        ('pos', "@Lilayy hi.wanna see 17 again again with me ;) i\'ll fly to cali and see it with you"),
        ('pos', "@miizronnie aha speaking German  haha maybe i should send some stuff in Italian ;)"),
        ('pos', "@garrettmurray Same here!  I just wanted it to keep going and not end... ever! ;)"),
        ('pos', "@xxLOVExxPEACE yes  and i want you to keep going if you would ;)"),
        ('pos',
         "@David_Henrie haha i WISH i coudl meet you.. you should stop by seattle some time  home of the STARBUKS ;) I LOVE YOU DAVID!!"),
        ('pos',
         "@erikarbautista ! HE HAS A FAVOURITE! You\'re his favourite ;) OMGAAH.   sorry for creepering? ..not really lol"),
        ('pos', "watching my baby on snl !  baby you look greaaaaat ;)"),
        ('pos', "@missSHANNAbaby YAY  u get to see ddub again ;) those 5 men always keep me happy &amp; motivated"),
        ('neg', "@Peacehippie04 is a loser;) baha"),
        ('pos', "@odangitsnikki There\'s a way around that 72 Minute Limit ;) AIM me and I\'ll tell you"),
        ('pos', "@SicilyYoder no not yet I ate a couple ;) I love Reeces but they are hard to get in NZ"),
        ('pos',
         "@james_a_michael CUTE  thanks for sharing! AND PLEASE Direct Message ME before you go to bed James ;) ;) you know you want to!"),
        ('neg', "Hi Everyone miss me much?  muahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh ;)"),
        ('pos',
         "I think I would be a good radio dj...I like awesome music and I have a great personality!!!!  ;) !!!   !!!"),
        ('neg',
         "@findingurstyle lol it\'s funny but it\'s not the back... it\'s all in the legs ;) and I\'ve never hurt my back! Thank God!  Thanks 4 watchin!"),
        ('pos', "@mileycyrus HI!  I\'m Eunice Kyna! I\'m a HUGE fan of yours! Can\'t wait for your next album! ;)"),
        ('pos',
         "@JJRogue I have an interview on tuesday so things are turning around I think!! yay! so dont worry!  And Japsicans are a rare breed. ;)"),
        ('pos',
         "@ztnewetnorb hha yeah  like they have your heart too but weve met shaun and bradie... it seems more real ;)"),
        ('neg', "@parboo LOL - Birmingham was my 1st love... but it\'s time to move on! ;) Good Morning"),
        ('neg', "@KiwiLucy ahhh ;) I know who wins the entire thing"),
        ('pos', "@jasonperryrock Is you cat clean again?  Hope so ;) Xx"),
        ('pos',
         "Alright... i need to get sleep so i can ACTUALLY be awake for my mothers\' day! ;) Nighty Nightzzz Or good morning my twitter friends!!!"),
        ('pos', "I need 4 followers to get 100 followers!!  Fallow me!!!  I fallow you back!! ;)"),
        ('neg',
         "I\'m not! They frighten me to death............I just like to see all the boys in their leathers!  ;) We go every year. Brilliant atmos!"),
        ('pos', "@dannymasterson the honesty\'s to much...........  Sorry couldn\'t resist;)"),
        ('pos', "@beautyholic woohoooo ;) to BOTH! retail therapy and surprise visits  two things i love."),
        ('neg', "@damohopo I didn\'t headbutt anyone! Not that I know about anyway! ;) You ok today?  Football today?"),
        ('neg',
         "Yang4 - finally got it  Chinese is hard when every other kid has a Zhonguoren adult at home! We\'re all foreign devils here ;)"),
        ('neg',
         "@NursingDrPepper I told you I\'d be back  Just won\'t be updating as much before my exams. Looking forward to a day or two in your house ;)"),
        ('neg', "doing the andy dance  the one on fonzie gomez show ;) haha"),
        ('pos',
         "just saw UP  it was a cute movie (:passed by a place called a peasants kitchen. wtf? that names kinda sad"),
        ('pos', "such a good day!! even though my so called friends did try to row away from me  but god i love em :p"),
        ('neg',
         "@nathanblevins  Maybe next time. Can\'t be away this weekend as much as I\'d like to jump in the car and go. ::pout::"),
        ('neg', "Waiting for the Denver game to come on.. but i dont think their gonna win it  Lakers suck lol :p"),
        ('pos',
         "@funkylovin ah mine is never home before 8   I handed off the kids and grabbed the bottle of malibu and a coke..momma getting drinky :para"),
        ('neg',
         "@Kayleigh_Stack i wish i could go to both but i don\'t think i\'ll be allowed :p either way with two shows going your bound to get a ticket"),
        ('neg', "@lynnftw I know exactly what you are saying.. its so not cool... that is why tapes were better  :p"),
        ('neg',
         "@emzyjonas Yea once - me and my friends flew out to amercia to see her w/ the Jonas brothers  . have u? haha i hate bebo :p . aw cant wait"),
        ('pos', "@YousifMind good morning  3asa mo bs important classes ? :p"),
        ('pos',
         "@xx_Megan_xx oh dear lmao that a key ingredient :p cakes in the oven and now I\'m cooking my lunch paprika and chilli chicken YUM haha"),
        ('pos', "@Raderr but yeah i like purple maybe thats why!! ;)  :p :d"),
        ('neg', "@Afey umm how abt a comment like that :p &quot;i dont like this&quot;"),
        ('pos',
         "I gave a homeless lady named Ruby an Ice Cream sandwich and a cigarette.  That is my g00d deed for the day. :p"),
        ('neg', "i blame you all!  got it??? good :p she better be in good condition 2! &lt;33 night"),
        ('pos', "@KOLsweetie hell yeah! Belgian beer is the bomb!!  :p"),
        ('pos', "@Willy9e  shouldn\'t I be going to sleep? Just kidding :p"),
        ('pos',
         "@andyclemmensen would that just eat away at your masculinity? What masculinity did you have? :p haha u\'d probs beat me tho  haha xo"),
        ('pos', "#f1 soon  good luck brawn and mclaren fix up look sharp :p"),
        ('pos',
         "@sosolid2k turtles and shoes make an awesome couple  if only shoes could talk back to the turtle :p lol"),
        ('neg', "@n00rtje Thanks  I\'ll explain on msn or something :p and I HATE SPIDERS TOO! What happened"),
        ('neg',
         "@ether_radio yeah :S i feel all funny cause i haven\'t slept enough  i woke my mum up cause i was singing she\'s not impressed :S you?"),
        ('neg',
         "even though everyone wanted to do a newish song and our teacher agreed :S old grumpy doesn\'t like us happy  haha"),
        ('pos',
         "I am soo happy! But frustrated at the same time!  :]  :S. Ohh noo!!! Britney is recording her new video for Radar!!!  Sooo ExxCiiTeed!!!"),
        ('pos',
         "I love music so much that i\'ve gone through pain to play :S my sides of my fingers now are peeling and have blisters from playing so much"),
        ('neg',
         "in about half a hour i\'m going to my english lesson...guess i\'ll have to wait...and wait for a couple hours so i\'m over with it.(( :S   ))"),
        ('neg', "@t0ns:  nou moe... stomme banken/crisis shit :S"),
        ('neg',
         "@gfalcone601 ino :O i was near crying for her  sometimes i forget that its actually live tv =/ .....am i talkin about the sme thing?:Sxxxx"),
        ('neg', "@FreyaLynn lol seriously.  fail. ::sigh::"),
        ('pos',
         "@changedforgood Aww that sucks   It wasn\'t that long though but Dianne was SO cute as usual &lt;3 Hopeflly some1 mite put it on youtube :S"),
        ('neg', "My computer dies soon  - its so much virus on it but my virus scanner  cant find it :S"),
        ('pos',
         "Greg:Showing my friends AudioBoo http://audioboo.fm/ Everyone seems 2 love it. Ta for the headzup bro. So need 2 get iPhone. Roll on June"),
        ('pos', "@CARAciao haha :S i started yesterday my dad helped me so much!!!"),
        (
        'pos', "BOOK NOW &amp; SAVE:SUMMER 2009 * THE AMAZONES VILLAGE SUITES****-CRETE-GREECE! THE BEST PLACE TO BE!"),
        ('neg', "thank you @ddlovato (: cant wait!!!! ummm btw ima crash still sick"),
        ('neg', "@ddlovato Caan\'t Iht Be Earlier? ICant Wait That Long.  Ahar. (:"),
        ('pos',
         "@AnnetteStatus I luv urs! admitting niley with a kiss (: but then they change their minds  haha &amp; demi/sterling (: not jemi but still cute"),
        ('neg', "My siblings left me alone.   Bored. (:|"),
        ('pos', "slept all day.. lol. now time to start on my UN article.. what fun (: ..."),
        ('neg', "@mixxxonn we watched the today show(: we didnt see you though"),
        ('pos', "Had quite a cool day with Charlie and then Ben aswell (: got lost and stung by nettles"),
        ('neg', "In school ; With Victoria &amp; Bryan (: _ no more school soon"),
        ('neg', "last day at the Ko Olina.  off to north shoreee(:"),
        ('pos', "this week of mine was not easy!  but finally it\'s over! (:"),
        ('pos', "Aww what a sunny day! Tasty barbeque with the family (: Got bad sunburn though"),
        ('pos',
         "just saw UP  it was a cute movie (:passed by a place called a peasants kitchen. wtf? that names kinda sad"),
        ('neg', "He didnt leave a voicemail..  -121908inlove(:"),
        ('neg', "@Spidersamm ohh yeahh (: i\'m probs gonna be a loner to start with"),
        ('neg', "no Santa cruz for me  but I do have an interview at jamba tomorrow morning (:"),
        ('neg',
         "Can\'t beat all time low.. (: I soooooo want to go to Metro Station..  Your cheap shots wont be able to break bones"),
        ('pos', "@grcrssl Helloooo (: Star Wars day is cool  LOOL. Wen do you go to Cnaterbury then ? x"),
        ('pos',
         "@torilovesbradie no probs(: and yeah im still sick. no school today  lol. feel really crap but thats because im dancing lol . thanks"),
        ('pos', "Gdnight Tweeters (: Night @athenakg sleep tight and don\'t steal my blankets  Otay! I love YOUS"),
        ('pos',
         "I\'m still up! Thank you all for praying (: AHAHAHA! I\'m watching Britney: For the Record until school. Today should be a good day"),
        ('pos', "@taylorswift13 i love you so much tay (: youre so amazing &lt;3 you should come to denmark"),
        ('pos',
         "@johncmayer heylo johnn (: im a huge fan. hope ur day is awesomee. cuzz im home sick and its kinda less than awesome.. anyways.. PEACE"),
        ('pos',
         "Watching TV with the best people in the whole world !!!!! My Mum and My Sis Agus (: Love you all ! Twitter you later ha"),
        ('pos', "@yaykimo baaha  &amp; healthy choice my friend! (:"),
        ('pos',
         "Korean music festival &lt;33 i miss you ): Hahaha sexy time ! (: &lt;3 Can\'t wait till SHINee ! LOL !"),
        ('pos', "just got out of the pool!!   so fun..now gonna watch tv and do stuff on the computer. (:"),
        ('pos', "just had cheese on toast with ham (: about to get ready to go to LONDON!"),
        ('pos', "YES! getting my sky + back on wednesday  been waiting weeks for it (:"),
        ('pos',
         "14 dayssss ahhhh super excited   \'they\'re telling me that my heart wont beat again\'   JLS were awesome yesterday (:")]


def get_words(doc):
    """Поделба на документот на зборови. Стрингот се дели на зборови според
    празните места и интерпукциските знаци

    :param doc: документ
    :type doc: str
    :return: множество со зборовите кои се појавуваат во дадениот документ
    :rtype: set(str)
    """
    # подели го документот на зборови и конвертирај ги во мали букви
    # па потоа стави ги во резултатот ако нивната должина е >2 и <20
    words = list()
    for word in re.split('\\W+', doc):
        if 2 < len(word) < 20:
            words.append(word.lower())
    return words


def get_vocabulary(documents):
    """Враќа множество од сите зборови кои се појавуваат во документите.

    :param documents: листа со документи
    :type documents: list(str)
    :return: множество зборови
    :rtype: set(str)
    """
    vocab = set()
    for doc_text in documents:
        words = get_words(doc_text)
        words_set = set(words)
        vocab.update(words_set)
    return sorted(vocab)


def cosine(v1, v2):
    """Ја враќа косинусната сличност помеѓу два вектори v1 и v2.

    :param v1: вектор1
    :type v1: list(float)
    :param v2: вектор2
    :type v2: list(float)
    :return: сличност помеѓу вектор и вектор2
    :rtype: float
    """
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumxx += x * x
        sumyy += y * y
        sumxy += x * y
    return sumxy / math.sqrt(sumxx * sumyy)


def pearson(v1, v2):
    """ Го враќа коефициентот на Пирсонова корелација помеѓу два вектори v1 и v2.

    :param v1: вектор1
     :type v1: list(float)
    :param v2: вектор2
    :type v2: list(float)
    :return: сличност помеѓу вектор и вектор2
    :rtype: float
    """
    sum1 = 0
    sum2 = 0
    sum1Sq = 0
    sum2Sq = 0
    pSum = 0
    n = len(v1)
    for i in range(n):
        x1 = v1[i]
        x2 = v2[i]
        sum1 += x1
        sum1Sq += x1 ** 2
        sum2 += x2
        sum2Sq += x2 ** 2
        pSum += x1 * x2
    num = pSum - (sum1 * sum2 / n)
    den = math.sqrt((sum1Sq - sum1 ** 2 / n) * (sum2Sq - sum2 ** 2 / n))
    if den == 0: return 0
    r = num / den
    return r


def calculate_document_frequencies(documents):
    """Враќа речник со број на појавување на зборовите.

    :param documents: листа со документи
    :type documents: list(str)
    :return: речник со број на појавување на зборовите
    :rtype: dict(str, int)
    """
    df = {}
    documents_words = []
    for doc_text in documents:
        words = get_words(doc_text)
        documents_words.append(words)
        words_set = set(words)
        for word in words_set:
            df.setdefault(word, 0)
            df[word] += 1
    return df


def calc_vector(cur_tf_idf, vocab):
    """Пресметува tf-idf вектор за даден документ од дадениот вокабулар.

    :param cur_tf_idf: речник со tf-idf тежини
    :type cur_tf_idf: dict(str, float)
    :param vocab: множество од сите зборови кои се појавуваат во барем еден документ
    :type vocab: set(str)
    :return: tf-idf вектор за дадениот документ
    """
    vec = []
    for word in vocab:
        tf_idf = cur_tf_idf.get(word, 0)
        vec.append(tf_idf)
    return vec


def process_document(doc, df, N, vocab):
    """Пресметува tf-idf за даден документ.

    :param doc: документ
    :type doc: str
    :param df: речник со фреквенции на зборовите во дадениот документ
    :type df: dict(str, int)
    :param N: вкупен број на документи
    :param vocab: множество од сите зборови кои се појавуваат во барем еден документ
    :type vocab: set(str)
    :return: tf-idf вектор за дадениот документ
    """
    if isinstance(doc, str):
        words = get_words(doc)
    else:
        words = doc
    idf = {}
    for word, cdf in df.items():
        idf[word] = math.log(N / cdf)
    f = {}  # колку пати се јавува секој збор во овој документ
    for word in words:
        f.setdefault(word, 0)
        f[word] += 1
    max_f = max(f.values())  # колку пати се појавува најчестиот збор во овој документ
    tf_idf = {}
    for word, cnt in f.items():
        ctf = cnt * 1.0 / max_f
        tf_idf[word] = ctf * idf.get(word, 0)
    vec = calc_vector(tf_idf, vocab)
    return vec


def rank_documents(doc, documents, sim_func=cosine):
    """Враќа најслични документи со дадениот документ.

    :param doc: документ
    :type doc: str
    :param documents: листа со документи
    :type documents: list(str)
    :param sim_func: функција за сличност
    :return: листа со најслични документи
    """
    df = calculate_document_frequencies(documents)
    N = len(documents)
    vocab = get_vocabulary(documents)
    doc_vectors = []
    for document in documents:
        vec = process_document(document, df, N, vocab)
        doc_vectors.append(vec)
    query_vec = process_document(doc, df, N, vocab)
    similarities = []
    for i, doc_vec in enumerate(doc_vectors):
        dist = sim_func(query_vec, doc_vec)
        similarities.append((dist, i))
    similarities.sort(reverse=True)
    return similarities


def create_dataset(documents, labels):
    """Формира податочно множество со tf-idf тежини и класи, соодветно за класификација со дрва на одлука.

    :param documents: листа со документи
    :type documents: list(str)
    :param labels: листа со класи
    :type labels: list
    :return: податочно множество со tf-idf тежини и класи, речник со френвенции на појавување на зборовите,
            број на документи во множеството, вокабулар од даденото множество на аборови
    :rtype: list(list), dict(str, int), int, set(word)
    """
    dataset = []
    doc_vectors = []
    df = calculate_document_frequencies(documents)
    N = len(documents)
    vocab = get_vocabulary(documents)
    for document in documents:
        vec = process_document(document, df, N, vocab)
        doc_vectors.append(vec)
    for doc_vec, label in zip(doc_vectors, labels):
        doc_vec.append(label)
        dataset.append(doc_vec)
    return dataset, df, N, vocab


from math import log


def unique_counts(rows):
    """Креирај броење на можни резултати (последната колона
    во секоја редица е класата)

    :param rows: dataset
    :type rows: list
    :return: dictionary of possible classes as keys and count
             as values
    :rtype: dict
    """
    results = {}
    for row in rows:
        # Клацата е последната колона
        r = row[len(row) - 1]
        if r not in results:
            results[r] = 0
        results[r] += 1
    return results


def gini_impurity(rows):
    """Probability that a randomly placed item will
    be in the wrong category

    :param rows: dataset
    :type rows: list
    :return: Gini impurity
    :rtype: float
    """
    total = len(rows)
    counts = unique_counts(rows)
    imp = 0
    for k1 in counts:
        p1 = float(counts[k1]) / total
        for k2 in counts:
            if k1 == k2:
                continue
            p2 = float(counts[k2]) / total
            imp += p1 * p2
    return imp


def entropy(rows):
    """Ентропијата е сума од p(x)log(p(x)) за сите
    можни резултати

    :param rows: податочно множество
    :type rows: list
    :return: вредност за ентропијата
    :rtype: float
    """
    log2 = lambda x: log(x) / log(2)
    results = unique_counts(rows)
    # Пресметка на ентропијата
    ent = 0.0
    for r in results.keys():
        p = float(results[r]) / len(rows)
        ent = ent - p * log2(p)
    return ent


class DecisionNode:
    def __init__(self, col=-1, value=None, results=None, tb=None, fb=None):
        """
        :param col: индексот на колоната (атрибутот) од тренинг множеството
                    која се претставува со оваа инстанца т.е. со овој јазол
        :type col: int
        :param value: вредноста на јазолот според кој се дели дрвото
        :param results: резултати за тековната гранка, вредност (различна
                        од None) само кај јазлите-листови во кои се донесува
                        одлуката.
        :type results: dict
        :param tb: гранка која се дели од тековниот јазол кога вредноста е
                   еднаква на value
        :type tb: DecisionNode
        :param fb: гранка која се дели од тековниот јазол кога вредноста е
                   различна од value
        :type fb: DecisionNode
        """
        self.col = col
        self.value = value
        self.results = results
        self.tb = tb
        self.fb = fb


def compare_numerical(row, column, value):
    """Споредба на вредноста од редицата на посакуваната колона со
    зададена нумеричка вредност

    :param row: дадена редица во податочното множество
    :type row: list
    :param column: индекс на колоната (атрибутот) од тренирачкото множество
    :type column: int
    :param value: вредност на јазелот во согласност со кој се прави
                  поделбата во дрвото
    :type value: int or float
    :return: True ако редицата >= value, инаку False
    :rtype: bool
    """
    return row[column] >= value


def compare_nominal(row, column, value):
    """Споредба на вредноста од редицата на посакуваната колона со
    зададена номинална вредност

    :param row: дадена редица во податочното множество
    :type row: list
    :param column: индекс на колоната (атрибутот) од тренирачкото множество
    :type column: int
    :param value: вредност на јазелот во согласност со кој се прави
                  поделбата во дрвото
    :type value: str
    :return: True ако редицата == value, инаку False
    :rtype: bool
    """
    return row[column] == value


def divide_set(rows, column, value):
    """Поделба на множеството според одредена колона. Може да се справи
    со нумерички или номинални вредности.

    :param rows: тренирачко множество
    :type rows: list(list)
    :param column: индекс на колоната (атрибутот) од тренирачкото множество
    :type column: int
    :param value: вредност на јазелот во зависност со кој се прави поделбата
                  во дрвото за конкретната гранка
    :type value: int or float or str
    :return: поделени подмножества
    :rtype: list, list
    """
    # Направи функција која ни кажува дали редицата е во
    # првата група (True) или втората група (False)
    if isinstance(value, int) or isinstance(value, float):
        # ако вредноста за споредба е од тип int или float
        split_function = compare_numerical
    else:
        # ако вредноста за споредба е од друг тип (string)
        split_function = compare_nominal

    # Подели ги редиците во две подмножества и врати ги
    # за секој ред за кој split_function враќа True
    set1 = [row for row in rows if
            split_function(row, column, value)]
    # set1 = []
    # for row in rows:
    #     if not split_function(row, column, value):
    #         set1.append(row)
    # за секој ред за кој split_function враќа False
    set2 = [row for row in rows if
            not split_function(row, column, value)]
    return set1, set2


def build_tree(rows, scoref=entropy):
    """Градење на дрво на одлука.

    :param rows: тренирачко множество
    :type rows: list(list)
    :param scoref: функција за одбирање на најдобар атрибут во даден чекор
    :type scoref: function
    :return: коренот на изграденото дрво на одлука
    :rtype: DecisionNode object
    """
    if len(rows) == 0:
        return DecisionNode()
    current_score = scoref(rows)

    # променливи со кои следиме кој критериум е најдобар
    best_gain = 0.0
    best_criteria = None
    best_sets = None

    column_count = len(rows[0]) - 1
    for col in range(0, column_count):
        # за секоја колона (col се движи во интервалот од 0 до
        # column_count - 1)
        # Следниов циклус е за генерирање на речник од различни
        # вредности во оваа колона
        column_values = {}
        for row in rows:
            column_values[row[col]] = 1
        # за секоја редица се зема вредноста во оваа колона и се
        # поставува како клуч во column_values
        for value in column_values.keys():
            (set1, set2) = divide_set(rows, col, value)

            # Информациона добивка
            p = float(len(set1)) / len(rows)
            gain = current_score - p * scoref(set1) - (1 - p) * scoref(set2)
            if gain > best_gain and len(set1) > 0 and len(set2) > 0:
                best_gain = gain
                best_criteria = (col, value)
                best_sets = (set1, set2)

    # Креирај ги подгранките
    if best_gain > 0:
        true_branch = build_tree(best_sets[0], scoref)
        false_branch = build_tree(best_sets[1], scoref)
        return DecisionNode(col=best_criteria[0], value=best_criteria[1],
                            tb=true_branch, fb=false_branch)
    else:
        return DecisionNode(results=unique_counts(rows))


def print_tree(tree, indent=''):
    """Принтање на дрво на одлука

    :param tree: коренот на дрвото на одлучување
    :type tree: DecisionNode object
    :param indent:
    :return: None
    """
    # Дали е ова лист јазел?
    if tree.results:
        print(str(tree.results))
    else:
        # Се печати условот
        print(str(tree.col) + ':' + str(tree.value) + '? ')
        # Се печатат True гранките, па False гранките
        print(indent + 'T->', end='')
        print_tree(tree.tb, indent + '  ')
        print(indent + 'F->', end='')
        print_tree(tree.fb, indent + '  ')


def classify(observation, tree):
    """Класификација на нов податочен примерок со изградено дрво на одлука

    :param observation: еден ред од податочното множество за предвидување
    :type observation: list
    :param tree: коренот на дрвото на одлучување
    :type tree: DecisionNode object
    :return: речник со класите како клуч и бројот на појавување во листот на дрвото
    за класификација како вредност во речникот
    :rtype: dict
    """
    if tree.results:
        return tree.results
    else:
        value = observation[tree.col]
        if isinstance(value, int) or isinstance(value, float):
            compare = compare_numerical
        else:
            compare = compare_nominal

        if compare(observation, tree.col, tree.value):
            branch = tree.tb
        else:
            branch = tree.fb

        return classify(observation, branch)


if __name__ == '__main__':
    sample_ind = int(input())

    train_documents, test_data, labels = [], [], []
    for i, item in enumerate(data):
        if i == sample_ind:
            test_data.append(item[1])
        else:
            train_documents.append(item[1])
            labels.append(item[0])

    dataset, df, N, vocab = create_dataset(train_documents, labels)
    tree = build_tree(dataset)
    test_data = process_document(test_data[0], df, N, vocab)
    predicted_classes = classify(test_data, tree)
    print(sorted(predicted_classes.items(), key=lambda item: item[1], reverse=True)[0][0])