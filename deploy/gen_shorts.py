# -*- coding: utf-8 -*-
import json, os, glob
D = "/data/scaleearn/terror/stories"
os.makedirs(D, exist_ok=True)
IB = "cinematic horror photography, %s, dark, eerie, foggy, moonlight, dramatic, high detail"
def b(t, i): return {"text": t, "img": IB % i}

# 1) DEDUP: remover uma das 'Loira do Banheiro' (mantem a S06, remove a S01)
removed=[]
for f in glob.glob(D+"/*S01_loira_banheiro*.json"):
    os.remove(f); removed.append(os.path.basename(f))
print("removidos:", removed)

TAGS_BASE=["contos do escuro","terror","lenda","historias de terror","folclore mundial","medo","shorts"]

STORIES=[
 ("G01_la_llorona","A CHORONA","La Llorona: a mãe que chora pelos filhos na água 😱 #shorts #terror #lenda",
  "Ela afogou os próprios filhos e agora chora por eles para sempre. Se você a ouvir, já é tarde.",
  ["la llorona","mexico","lenda mexicana","mulher que chora"],
  [("Na América Latina, perto dos rios, à noite, ouve-se um choro de mulher: 'Ai, meus filhos!'","a weeping woman in white by a dark river at night"),
   ("É La Llorona, a Chorona. Em vida, afogou os próprios filhos num acesso de desespero.","a ghostly woman in white kneeling at a riverbank, crying"),
   ("Arrependida, se matou. Mas no outro lado foi barrada: 'Onde estão as crianças?'","a pale spirit wandering, empty arms, river fog"),
   ("Desde então vaga pelas margens, procurando filhos que nunca vai encontrar.","a white figure drifting along a misty river at night"),
   ("Dizem que ela leva qualquer criança que encontre sozinha perto da água, para substituir as suas.","a child's silhouette near dark water, a white shape approaching"),
   ("E que ouvir o choro perto significa que ela está longe. Ouvir longe, significa que ela já está atrás de você.","close up of a crying ghost face emerging from the dark"),
   ("Por isso, na América Latina, quando as mães ouvem aquele pranto à noite, trancam as portas. E seguram os filhos bem perto.","a dark house by a river, a mother holding a child at the window")]),
 ("G02_el_silbon","O ASSOBIADOR","El Silbón: se o assobio é fraco, ele está perto 😱 #shorts #terror",
  "Um assobio na noite dos Llanos. Quanto mais baixo, mais perto ele está de você.",
  ["el silbon","venezuela","assobiador","llanos"],
  [("Nos campos da Venezuela, à noite, viajantes ouvem um assobio: dó, ré, mi, fá, sol, lá, si.","a vast dark plain at night, a lone traveler, distant sound"),
   ("É El Silbón, o Assobiador: um espírito alto e esquelético que carrega um saco de ossos nas costas.","a tall gaunt figure with a sack of bones, dark field night"),
   ("Conta a lenda que ele matou o próprio pai, e carrega os ossos dele desde então.","a skeletal figure dragging a heavy sack across dark grass"),
   ("A regra que assombra os Llanos é esta: se o assobio soa forte e alto, ele está longe.","a faint silhouette far on the horizon, moonlit plain"),
   ("Mas se o assobio soa fraco e baixinho, ele já está ao seu lado.","an extreme close up of a bony face beside the viewer, dark"),
   ("Dizem que cães latindo e pimenta o afastam. Mas se ele contar os seus ossos e chegar ao fim, alguém morre naquela casa.","a bony hand counting bones by a dim fire, shadows"),
   ("Então, nos campos, quando o assobio enfraquece, ninguém se vira. Só aperta o passo e reza pelo nascer do sol.","a traveler hurrying across a dark plain toward a faint dawn")]),
 ("G03_pontianak","A DAMA DE BRANCO","Pontianak: o perfume de flores antes do horror 😱 #shorts #terror",
  "Na Malásia, um cheiro doce de flores à noite é o primeiro aviso. E o último.",
  ["pontianak","malasia","indonesia","vampira"],
  [("No Sudeste Asiático, se você sentir um perfume doce de flores no meio da noite, prenda a respiração.","a dark tropical street at night, white flowers, mist"),
   ("É o primeiro sinal da Pontianak: o espírito de uma mulher que morreu grávida.","a pale woman in a white dress under a banana tree at night"),
   ("De dia, parece uma mulher bela de vestido branco e cabelo longo e negro.","a beautiful pale woman with long black hair, white dress"),
   ("De noite, revela o rosto apodrecido, as unhas longas, e um riso de bebé que vem do nada.","a decayed ghost face with long nails, horror, blurred"),
   ("O cheiro doce das flores significa que ela está longe. Um cheiro podre significa que ela está logo atrás.","white flowers rotting, dark, a shadow behind"),
   ("Ela caça perto de bananeiras, atacando homens e arrancando os seus órgãos com aquelas unhas.","a clawed hand reaching from behind a banana tree, night"),
   ("Nas aldeias, dizem que um prego cravado na nuca dela a transforma de volta em mulher. Mas quem tem coragem de chegar tão perto?","an old iron nail, a dark tropical night, dread")]),
 ("G04_wendigo","A FOME QUE ANDA","Wendigo: o espírito da fome que nunca se sacia 😱 #shorts #terror",
  "No frio do norte, há uma fome tão grande que vira monstro. E ela está sempre com frio.",
  ["wendigo","america do norte","floresta","inverno"],
  [("Nas florestas geladas do norte da América, os povos antigos temiam um espírito acima de tudo: o Wendigo.","a frozen dark forest, snow, a tall shadow between pines"),
   ("É a fome feita carne. Um ser alto e esquelético, de pele esticada e olhos fundos.","a gaunt towering creature with sunken eyes in the snow"),
   ("Diz a lenda que ele nasce de uma pessoa que, desesperada no inverno, comeu carne humana para sobreviver.","a lone figure in a snowstorm, a dark transformation, cold"),
   ("Quem faz isso nunca mais se sacia. A fome cresce, o corpo se deforma, e a alma se perde.","a distorted starving silhouette howling in the snow"),
   ("O Wendigo imita vozes humanas na floresta para atrair os perdidos para mais longe.","footprints in snow leading into dark woods, a faint voice"),
   ("E ele está sempre com frio, um frio que vem de dentro, e que nunca passa.","frost spreading over dark trees, a breath of ice"),
   ("Por isso, no norte, os caçadores têm uma regra antiga: por pior que seja a fome, há coisas que um homem nunca pode comer. Porque a fome que elas acordam… nunca mais adormece.","a dark snowy forest, a single set of tracks, dread")]),
 ("G05_krampus","O OUTRO LADO DO NATAL","Krampus: o demônio que leva as crianças más 😱 #shorts #terror",
  "Nos Alpes, o Natal tem dois lados. Um te dá presentes. O outro vem te buscar.",
  ["krampus","alpes","austria","natal sombrio"],
  [("Nos Alpes, na noite de 5 de dezembro, as crianças não temem o Papai Noel. Temem o que vem com ele.","a snowy alpine village at night, warm lights, a dark shape"),
   ("É o Krampus: metade bode, metade demônio, com chifres, língua comprida e correntes que arrastam.","a horned goat-demon with chains and a long tongue, snow night"),
   ("Enquanto São Nicolau premia as crianças boas, o Krampus vem atrás das más.","a dark horned figure outside a child's frosted window"),
   ("Ele carrega um feixe de varas de bétula e um cesto nas costas.","a demon with birch branches and a wicker basket, snowy street"),
   ("As crianças desobedientes levam um susto, um açoite. As piores, dizem, vão dentro do cesto.","a basket on a demon's back, small hands gripping the rim"),
   ("Para onde? Para as montanhas. Para o rio gelado. Para lugares de onde não se volta no Natal.","a dark figure dragging a basket up a snowy mountain path"),
   ("Por isso, nos Alpes, as crianças se comportam em dezembro. Não pelo presente que podem ganhar. Mas pelo que pode vir buscá-las na noite.","a snowy window, two horned shadows passing outside")]),
 ("G06_banshee","O GRITO QUE ANUNCIA","Banshee: ouvir o grito dela é ouvir a morte chegar 😱 #shorts #terror",
  "Na Irlanda, um grito na noite não é do vento. É um aviso. E ele é para a sua família.",
  ["banshee","irlanda","presságio","grito"],
  [("Na Irlanda antiga, um grito agudo de mulher cortando a noite gelava o sangue de famílias inteiras.","a misty irish moor at night, an old stone house, a faint wail"),
   ("Era a Banshee: um espírito feminino de cabelos longos, vestida de cinza ou branco.","a pale woman with long grey hair wailing on a dark moor"),
   ("Ela não mata. Ela anuncia. O seu grito significa que alguém daquela família vai morrer em breve.","a ghostly woman keening outside a stone cottage, night fog"),
   ("Às vezes aparece lavando roupas ensanguentadas num rio, à luz da lua.","a spectral woman washing bloodied cloth in a dark river"),
   ("Cada família antiga tinha a sua Banshee, ligada ao sangue, que chorava por eles há gerações.","an old family crest, a pale mourning figure in the dark"),
   ("Ouvir o lamento era o pior presságio: ninguém sabia quem partiria, só que a morte já estava a caminho.","a dim candlelit room, a family listening in dread, night"),
   ("Por isso, na Irlanda, quando o vento parecia chorar com voz de mulher, ninguém dizia que era o vento. Ficavam em silêncio. E esperavam a notícia.","an old window on a stormy irish night, a grey silhouette")]),
 ("G07_churel","A NOIVA VINGATIVA","Churel: a mulher que volta com os pés virados 😱 #shorts #terror",
  "No sul da Ásia, uma mulher morta de injustiça volta. E dá para saber pelos pés.",
  ["churel","india","paquistao","espirito vingativo"],
  [("No sul da Ásia, teme-se o espírito de uma mulher que morreu grávida ou maltratada pela própria família.","a dark south asian village lane at night, a white-clad figure"),
   ("É a Churel: ela volta bela, para seduzir os homens da família que a traiu.","a beautiful woman in white at a doorway, dim lamplight"),
   ("Mas há um detalhe que a denuncia: os seus pés estão virados para trás.","a close up of bare feet pointing backwards, dark ground"),
   ("Ela atrai o homem para um lugar isolado, prometendo amor.","a man following a figure into the dark, a lantern"),
   ("E ali, noite após noite, drena a sua juventude, até ele envelhecer e definhar.","a young man aging rapidly, pale, a shadow feeding, dark"),
   ("Dizem que famílias enterravam as suas mortas com cuidados especiais, com medo de que voltassem assim.","an old grave with protective markings, incense, night"),
   ("Por isso, no sul da Ásia, um homem que encontra uma bela estranha à noite olha primeiro para baixo. Para os pés. Porque é ali que o horror se esconde.","a dim path, a white dress, backward-facing feet in shadow")]),
 ("G08_la_tunda","A IMITADORA","La Tunda: ela tem a cara de alguém que você ama 😱 #shorts #terror",
  "Na selva do Pacífico, ela aparece com o rosto de quem você confia. E te leva embora.",
  ["la tunda","colombia","equador","selva"],
  [("Nas selvas do Pacífico sul-americano, as crianças que somem têm uma explicação sussurrada: La Tunda.","a dense dark jungle at night, mist, a faint figure"),
   ("É uma criatura que muda de forma, assumindo o rosto de alguém que a vítima ama e confia.","a shape shifting figure, half familiar face half monster"),
   ("Com essa aparência, ela chama a pessoa para dentro da mata, com voz doce e familiar.","a child following a familiar silhouette into dark trees"),
   ("Mas há sempre um defeito: uma das pernas termina num pilão de madeira, ou numa pata.","a wooden peg leg stepping on jungle floor, dark"),
   ("Ela leva as vítimas para o fundo da selva e as 'entumba': enfeitiça com comida estragada até perderem a vontade de voltar.","a dazed person eating by a dark swamp, enchanted, fog"),
   ("As famílias precisavam rezar e usar tambores e fumaça para quebrar o feitiço e trazer a pessoa de volta.","villagers with drums and smoke searching a dark jungle"),
   ("Por isso, à beira da mata, quando alguém que você ama te chama de longe à noite… olhe bem para as pernas antes de seguir.","a familiar figure beckoning at the jungle edge, one leg odd")]),
 ("G09_mothman","O HOMEM-MARIPOSA","Mothman: ele aparece pouco antes da tragédia 😱 #shorts #terror",
  "Numa cidade dos EUA, uma criatura de olhos vermelhos apareceu. Logo depois, a ponte caiu.",
  ["mothman","estados unidos","olhos vermelhos","presságio"],
  [("Em 1966, numa cidadezinha dos Estados Unidos, casais começaram a ver uma criatura enorme nos campos.","a dark rural road at night, two red glowing eyes in a field"),
   ("Tinha a forma de um homem alado, com grandes asas e dois olhos vermelhos que brilhavam no escuro.","a tall winged humanoid with glowing red eyes, night sky"),
   ("Perseguia os carros voando, acompanhando a velocidade sem bater as asas.","a winged shadow chasing a car down a dark road, red eyes"),
   ("Durante um ano, dezenas de pessoas o viram. E muitas tiveram pesadelos e visões de desastre.","a frightened person staring up, red light reflected in eyes"),
   ("Então, em dezembro de 1967, a ponte principal da cidade desabou, matando dezenas.","a collapsing bridge at night, dark water, chaos"),
   ("E as aparições pararam. Como se a criatura só tivesse vindo anunciar o que estava por vir.","an empty dark field, two fading red lights in the distance"),
   ("Até hoje se pergunta: o Mothman causava as tragédias… ou aparecia para avisar que elas estavam chegando? Essa história é real. E ninguém sabe a resposta.","a lonely bridge at dusk, a winged silhouette watching")]),
 ("G10_jinn","O QUE MORA NO VAZIO","O Jinn: a criatura de fogo que divide o mundo com a gente 😱 #shorts #terror",
  "Feitos de fogo sem fumaça, eles vivem ao nosso lado, nos lugares vazios. E nem todos são bons.",
  ["jinn","djinn","deserto","criatura de fogo"],
  [("Muito antes das histórias de gênios que realizam desejos, falava-se dos Jinn com verdadeiro medo.","a dark desert night, swirling sand, a faint ember glow"),
   ("A tradição diz que foram criados do fogo sem fumaça, e que vivem num mundo paralelo ao nosso.","wisps of smokeless fire forming a shape in the dark"),
   ("Habitam os lugares que os humanos evitam: ruínas, desertos, banheiros, casas abandonadas.","an abandoned house interior at night, shadows, dust"),
   ("A maioria nos ignora. Mas alguns, os maus, se prendem a pessoas e lugares.","a dark empty room, a distorted shadow in the corner"),
   ("Podem mudar de forma, sussurrar pensamentos, e aterrorizar quem invade o seu espaço sem respeito.","a shifting dark silhouette whispering, cold firelight"),
   ("Por isso, em muitas culturas, se pede licença ao entrar num lugar deserto, e se evita derramar água quente em cantos escuros.","a hand pausing at a dark doorway, a whispered word"),
   ("Porque aquele quarto vazio onde você sente que não está sozinho… segundo eles, talvez você não esteja mesmo.","an empty dark corner, a faint pair of eyes in the shadow")]),
]

written=0
for sid, thumb, title, desc, extra_tags, beats in STORIES:
    d={"id":sid,"thumb":thumb,"title":title,"desc":desc,
       "tags":(TAGS_BASE+extra_tags)[:9],
       "beats":[b(t,i) for (t,i) in beats]}
    # nome de ficheiro que entra JA a seguir (sort antes das S/T pendentes em _01_)
    fn=os.path.join(D,"terror_0000_01_%s.json"%sid)
    json.dump(d,open(fn,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    written+=1
print("escritos:",written,"shorts globais")
