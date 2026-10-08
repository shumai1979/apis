# -*- coding: utf-8 -*-
import json, os
EP = "/data/scaleearn/terror_long/episodes"
os.makedirs(EP, exist_ok=True)
IMGBASE = "cinematic horror photography, %s, dark, eerie, foggy, moonlight, dramatic, high detail"

def beat(t, img): return {"text": t, "img": IMGBASE % img}

# ---------------- L008: JAPAO ----------------
L008 = {
 "id":"L008",
 "title":"6 Lendas de Terror do Japão Que Tiram o Sono | Contos do Escuro",
 "thumb_title":"TERROR DO JAPÃO",
 "channel":"contos",
 "description":"Seis lendas de terror do Japão, das que se sussurram nas ruas vazias à noite: a Kuchisake-onna, a Teke Teke, o Aka Manto, a Yuki-onna, o Kappa e a boneca Okiku. A versão tradicional, contada como deve ser. Fica até ao fim.\n\nContos do Escuro — folclore e lendas do mundo, no escuro.\n#contosdoescuro #terror #lendasjaponesas #japao #historiasdeterror",
 "tags":["contos do escuro","terror","lendas japonesas","japao","yokai","kuchisake onna","yuki onna","folclore","lendas","historias de terror","medo"],
 "hook":"No Japão, há histórias que não se contam de dia. São sussurradas à noite, nas ruas vazias, por quem já encontrou algo que não devia. Estas seis atravessaram séculos. E esta noite são contadas como devem ser. No escuro.",
 "hook_img":"an empty japanese alley at night, red lanterns, mist, a lone silhouette",
 "intro":"Bem-vindo de volta aos Contos do Escuro. Seis lendas do Japão te esperam, das que fazem as crianças correr pra casa antes do sol se pôr. Fica até ao fim, porque a última ainda assombra um templo de verdade.",
 "intro_img":"a dark shinto shrine at night, stone lanterns, fog, moonlight",
 "outro":"Seis lendas, seis avisos vindos do outro lado do mundo. Se alguma te arrepiou, deixa o teu like, inscreve-te no Contos do Escuro e comenta qual delas não vais conseguir esquecer. Amanhã, à mesma hora, o escuro tem mais uma história pra ti.",
 "outro_img":"a single candle flickering in total darkness, swirling smoke, deep shadows",
 "stories":[
  {"name":"A Kuchisake-onna","title_img":"a woman wearing a surgical mask on a dark street at night, unsettling eyes","beats":[
   beat("Numa rua vazia, uma mulher de máscara cirúrgica te aborda e faz uma pergunta simples: 'Eu sou bonita?'","a woman in a surgical mask approaching on an empty night street"),
   beat("É a Kuchisake-onna, a mulher da boca rasgada. E não existe resposta segura.","close up of a masked woman, cold eyes, dark street"),
   beat("Se você disser que não, ela te corta ali mesmo com uma tesoura enorme.","a giant pair of scissors glinting in the dark, a shadow looming"),
   beat("Se disser que sim, ela arranca a máscara, revelando a boca rasgada de orelha a orelha, e pergunta de novo: 'E agora?'","a torn mouth slit ear to ear, horror, blurred"),
   beat("Dizem que a única saída é responder 'você está mais ou menos' e fugir enquanto ela hesita.","a person running down a dark japanese alley, a figure behind"),
   beat("Mas ela é rápida. Mais rápida do que qualquer um que já tentou correr. Por isso, à noite, no Japão, ninguém pergunta por direções a uma mulher de máscara.","an empty foggy street, a single mask dropped on the ground")]},
  {"name":"A Teke Teke","title_img":"a pale figure dragging itself on its hands across train tracks at night","beats":[
   beat("Dizem que uma garota caiu nos trilhos do trem e foi partida ao meio. Mas ela não morreu. Não de todo.","a dark train platform at night, empty, cold light"),
   beat("Virou a Teke Teke: um torso que se arrasta pelas mãos, fazendo um som seco contra o chão. Teke… teke… teke.","a torso figure crawling fast on hands, sparks on concrete"),
   beat("O nome vem justamente desse barulho, o das unhas e dos cotovelos raspando o asfalto na perseguição.","close up of hands scraping dark ground, motion blur"),
   beat("Ela é absurdamente veloz. Alcança um adulto correndo em poucos segundos.","a shadow rushing low across a dark street, speed"),
   beat("E quando alcança, corta a vítima ao meio, na cintura, deixando-a igual a ela.","a dark scythe shape, red reflection, shadows"),
   beat("Por isso dizem: se ouvir um 'teke teke' se aproximando atrás de você à noite, não olhe para trás. Só corra. E reze para chegar a uma porta.","a person reaching for a distant lit door in a dark street")]},
  {"name":"O Aka Manto","title_img":"a tall figure in a red cloak and white mask standing in a dark bathroom stall","beats":[
   beat("Num banheiro público, a última cabine, uma voz pergunta: 'Você quer papel vermelho ou papel azul?'","a row of dark toilet stalls, one door slightly open, cold light"),
   beat("É o Aka Manto, o manto vermelho, um espírito de máscara branca e capa escarlate.","a figure in a red cloak, white mask, shadow on tiled wall"),
   beat("Se você escolher vermelho, ele te corta até sua roupa ficar encharcada da sua própria cor.","red liquid dripping down white tiles, horror, blurred"),
   beat("Se escolher azul, ele te sufoca até você ficar roxo, sem ar.","a pale hand over a mouth, blue cold light, panic"),
   beat("Escolher outra cor? Mãos surgem do chão e te puxam para baixo, para nunca mais.","pale hands reaching up from a dark bathroom floor"),
   beat("A única saída, dizem, é recusar: 'não quero nenhum' e sair sem olhar. Nunca entre na última cabine. Nunca responda a uma voz que não devia estar ali.","an empty bathroom, the last stall door swinging slowly")]},
  {"name":"A Yuki-onna","title_img":"a beautiful pale woman in a white kimono standing in a snowstorm at night","beats":[
   beat("Na montanha, durante a nevasca, um viajante vê uma mulher de branco, linda, parada na neve. Ela não sente frio.","a pale woman in white in a heavy snowstorm, blue night"),
   beat("É a Yuki-onna, a mulher da neve. Sua pele é gelo, seu hálito congela o ar.","close up of a woman with ice-pale skin, frost on eyelashes"),
   beat("Ela se aproxima dos perdidos com um sorriso doce, e com um sopro os transforma em estátuas de gelo.","a frozen figure covered in frost in the snow, moonlight"),
   beat("A alguns ela poupa, por beleza ou piedade, com uma condição: nunca contar que a viram.","a snowy mountain pass at night, a lone trail of footprints"),
   beat("Diz a lenda que um homem poupado se casou anos depois com uma mulher pálida e bela. Numa noite, contou à esposa do fantasma que vira na neve.","a candlelit room, a pale woman listening, shadows"),
   beat("A esposa se levantou. Era ela. 'Você prometeu', sussurrou, antes de desaparecer no frio, para sempre. No Japão, a neve guarda segredos. E cobra quem os quebra.","a woman dissolving into snow and wind, open window, cold")]},
  {"name":"O Kappa","title_img":"a green humanoid creature with a water-filled dish on its head lurking in a dark river","beats":[
   beat("Nos rios e lagoas do Japão vive o Kappa: do tamanho de uma criança, pele de réptil, com um prato de água no topo da cabeça.","a green reptilian creature peering from dark river water"),
   beat("Esse prato é a sua força e a sua fraqueza: se a água entornar, ele perde todo o poder.","close up of a shallow water dish on a creature's head, ripples"),
   beat("Ele parece brincalhão, mas afoga pessoas e animais que chegam perto demais da margem.","a child's sandal floating on dark river water at night"),
   beat("Puxa as vítimas para o fundo pelos tornozelos, com uma força impossível para o seu tamanho.","a hand gripping an ankle underwater, bubbles, dark"),
   beat("A tradição ensina um truque: faça uma reverência ao Kappa. Educado, ele retribui, a água do prato cai, e ele enfraquece.","a small creature bowing at a riverbank, water spilling"),
   beat("Por isso, até hoje, se ensina às crianças: não brinque sozinho perto da água parada. Nunca se sabe o que espera, logo abaixo da superfície.","still dark pond at night, a single ripple spreading")]},
  {"name":"A Boneca Okiku","title_img":"an old japanese doll with long human hair in a dim temple shrine","beats":[
   beat("Em 1918, um menino comprou para a irmãzinha uma boneca de cabelo curto. A menina a amava, dormia com ela todas as noites.","an old shop, a child holding a japanese doll, warm dim light"),
   beat("A menina morreu pouco depois, de uma febre, com apenas dois anos. A família guardou a boneca num altar, em memória dela.","a small home altar with a doll, candle, incense smoke"),
   beat("Semanas depois, notaram algo impossível: o cabelo da boneca estava crescendo.","close up of a doll's hair, unnaturally long, dim light"),
   beat("Cortavam, e ele voltava a crescer, chegando até os ombros, como cabelo humano de verdade.","scissors beside a doll with long black hair, shadows"),
   beat("A boneca, chamada Okiku, foi levada a um templo, onde está até hoje, no templo Mannenji.","a doll on a temple shelf, offerings, dim sacred light"),
   beat("Os monges juram que o cabelo continua a crescer, e cortam-no com respeito, ano após ano. Dizem que é a alma da menina, que nunca quis se despedir da única amiga que teve. Essa história é real. E a boneca, você ainda pode visitar.","an old doll in a glass case, long hair, temple darkness")]}
 ]
}

# ---------------- L009: ESLAVAS / EUROPA DE LESTE ----------------
L009 = {
 "id":"L009",
 "title":"6 Lendas Sombrias da Europa de Leste | Contos do Escuro",
 "thumb_title":"BRUXAS DO LESTE",
 "channel":"contos",
 "description":"Seis lendas eslavas que assombram as florestas e aldeias da Europa de Leste: a Baba Yaga, a Rusalka, o Leshy, o Vampiro original, a Nocnitsa e o Domovoi. Folclore antigo, contado como deve ser. Fica até ao fim.\n\nContos do Escuro — folclore e lendas do mundo, no escuro.\n#contosdoescuro #terror #lendaseslavas #babayaga #historiasdeterror",
 "tags":["contos do escuro","terror","lendas eslavas","europa de leste","baba yaga","rusalka","vampiro","folclore","lendas","historias de terror","medo"],
 "hook":"Nas florestas antigas da Europa de Leste, onde as árvores são mais velhas que as aldeias, o medo tem nomes próprios. Bruxas, afogadas, senhores da mata. Estas seis lendas são contadas há séculos à luz da lareira. Esta noite, são tuas. No escuro.",
 "hook_img":"an ancient dark slavic forest at night, twisted trees, fog, a distant hut light",
 "intro":"Bem-vindo de volta aos Contos do Escuro. Seis lendas eslavas te esperam, das que as avós contavam para manter as crianças longe da floresta ao anoitecer. Fica até ao fim, porque a última mora dentro da tua própria casa.",
 "intro_img":"a dim village cottage interior at night, firelight, long shadows",
 "outro":"Seis lendas vindas das florestas frias do Leste. Se alguma te arrepiou, deixa o teu like, inscreve-te no Contos do Escuro e comenta qual delas levarias contigo para o escuro. Amanhã, à mesma hora, há mais uma história à tua espera.",
 "outro_img":"a single candle flickering in total darkness, swirling smoke, deep shadows",
 "stories":[
  {"name":"A Baba Yaga","title_img":"an ancient witch in a hut standing on giant chicken legs in a dark forest","beats":[
   beat("No fundo da floresta existe uma cabana que anda. Ela se equilibra sobre duas enormes pernas de galinha e gira para onde quer.","a wooden hut on giant chicken legs in a dark misty forest"),
   beat("Lá dentro vive a Baba Yaga: uma bruxa velhíssima, de nariz adunco e dentes de ferro.","an ancient hag with iron teeth by a fire, dark hut interior"),
   beat("Ela voa num grande pilão, remando o ar com um pilão de pedra e varrendo o próprio rastro com uma vassoura.","an old witch flying in a stone mortar over the forest at night"),
   beat("A cerca ao redor da sua casa é feita de ossos. E os crânios no topo brilham no escuro.","a fence made of bones with glowing skulls on top, night"),
   beat("Ela pode te devorar, ou te ajudar, dependendo do respeito e da coragem com que você fala.","a traveler standing small before a towering dark hut"),
   beat("Quem a procura por ganância, nunca volta. Quem a procura com humildade, às vezes recebe um dom. A floresta do Leste não é cruel por maldade. É cruel com os tolos.","a lone figure walking into a dark forest, skull fence behind")]},
  {"name":"A Rusalka","title_img":"a pale drowned woman with long wet hair rising from a dark lake at night","beats":[
   beat("À beira do lago, numa noite de verão, você ouve risos de mulher e um canto doce vindo da água.","moonlit lake at night, mist over the water, reeds"),
   beat("É a Rusalka: o espírito de uma jovem que se afogou, ou que foi afogada, antes do tempo.","a pale woman with wet hair emerging from dark water"),
   beat("De dia, dorme no fundo. De noite, sobe à superfície, linda, de cabelos longos e pele pálida.","a beautiful pale figure floating on a moonlit lake surface"),
   beat("Ela atrai os homens com o canto e a dança, para as águas fundas.","a man wading into a dark lake, a hand reaching from the water"),
   beat("E quando eles entram, ela os enlaça e os puxa para baixo, até o último sopro.","two figures sinking into dark water, bubbles rising"),
   beat("Dizem que, se a sua morte for vingada ou chorada, a Rusalka finalmente descansa. Até lá, ela canta. E o lago espera, paciente, por quem chega perto demais da margem.","still dark lake, a single ripple, long wet hair on the surface")]},
  {"name":"O Leshy","title_img":"a towering humanoid made of bark and roots looming between dark trees","beats":[
   beat("A floresta tem um dono. E ele te observa desde o momento em que você pisa entre as árvores.","a vast dark forest, a huge shadow among the trunks"),
   beat("É o Leshy: um gigante de pele de casca e cabelo de musgo, que muda de tamanho conforme a mata.","a giant figure of bark and moss towering over trees"),
   beat("Ele pode ser alto como um carvalho, ou baixo como a relva. E imita vozes que você conhece.","a humanoid shape shrinking among grass, eerie"),
   beat("Com assobios e chamados familiares, ele leva os viajantes a andar em círculos, até se perderem para sempre.","a lost traveler walking in circles in identical dark woods"),
   beat("Quem respeita a floresta, pede licença e não desperdiça, passa ileso.","a person bowing respectfully at the forest edge, dusk"),
   beat("Mas quem entra com arrogância, cortando e matando à toa, descobre que a mata se fecha atrás de si. E que o dono dela nunca esquece um rosto.","dense dark trees closing in, no path, fog")]},
  {"name":"O Vampiro","title_img":"a pale gaunt figure rising from a grave in a foggy slavic cemetery at night","beats":[
   beat("Antes dos filmes e das capas elegantes, o vampiro das aldeias do Leste era outra coisa. Mais sujo. Mais próximo.","an old slavic village graveyard at night, fog, crooked crosses"),
   beat("Era o 'upir': um morto que não ficava morto. Inchado, de rosto corado, voltava à noite para visitar a família.","a bloated pale corpse-like figure at a cottage window, night"),
   beat("Começava sufocando os vivos durante o sono, ou bebendo o sangue de quem amava em vida.","a sleeping person, a dark shadow leaning over, cold light"),
   beat("As aldeias temiam quem morria amaldiçoado, ou sem rito. Esses eram os que voltavam.","villagers with torches around a grave at night, fear"),
   beat("Para impedir, abriam o túmulo e encontravam o corpo sem sinal de decomposição, às vezes com sangue fresco nos lábios.","an open grave, a preserved pale body, torchlight"),
   beat("Então cravavam uma estaca, enchiam a boca de alho, e por vezes queimavam tudo. Não por crueldade. Por terror. Porque na aldeia todos sabiam: nem sempre a morte é o fim.","a wooden stake and garlic by an open grave, night fog")]},
  {"name":"A Nocnitsa","title_img":"a shadowy witch hag crouching on the chest of a sleeping child in a dark room","beats":[
   beat("As mães do Leste conheciam o motivo dos gritos das crianças no meio da noite. E tinha nome.","a dark child's bedroom at night, moonlight, a small bed"),
   beat("A Nocnitsa, a bruxa da noite. Ela vem no escuro e se senta sobre o peito de quem dorme.","a dark hag crouching over a sleeping child, heavy shadow"),
   beat("A vítima acorda sem conseguir respirar, sem conseguir se mexer, com um peso esmagador sobre o corpo.","a child awake, unable to move, a weight pressing down"),
   beat("Ela se alimenta do medo, voltando noite após noite para a mesma criança.","a shadow figure at a bedside, the same every night, dread"),
   beat("Para afastá-la, punham uma faca de ferro sob o travesseiro, ou um círculo riscado no chão ao redor da cama.","an iron knife under a pillow, a chalk circle on the floor"),
   beat("Hoje chamamos de paralisia do sono. Mas pergunta a quem já acordou sem ar, com algo sentado no peito, se foi só ciência. No escuro, a Nocnitsa ainda não acredita em explicações.","a dark room, a faint hag silhouette dissolving at dawn")]},
  {"name":"O Domovoi","title_img":"a small shadowy bearded spirit watching from behind a stove in a dim cottage","beats":[
   beat("Nem tudo que vive na sua casa é da sua família. Nas aldeias do Leste, atrás do fogão, mora o Domovoi.","a dim old cottage interior, a stove, a small shadow behind it"),
   beat("É um espírito pequeno e barbudo, o guardião do lar. E ele decide se a sua casa prospera ou apodrece.","a small bearded spirit by a warm stove, firelight"),
   beat("Se você é limpo, respeitoso e deixa comida para ele, ele protege a casa, o gado e as crianças.","a tidy warm kitchen at night, a bowl of food left out"),
   beat("Mas se a casa vive em brigas, sujeira e desrespeito, ele se vira contra você.","a dark messy room, overturned objects, a cold draft"),
   beat("Começa a quebrar coisas, azedar o leite, sufocar quem dorme e assombrar os corredores à noite.","spilled milk, broken plates, a shadow in a dark hallway"),
   beat("Diz a tradição que, quando uma família se muda, deve convidar o Domovoi a ir junto. Porque uma casa sem o seu guardião não é um lar. É só um lugar à espera de quem o ocupe, do outro lado.","an empty dark house, a single door creaking open")]}
 ]
}

for ep in (L008, L009):
    f = os.path.join(EP, "ep_%s.json" % ep["id"])
    json.dump(ep, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", f, "| stories:", len(ep["stories"]))
print("OK")
