# -*- coding: utf-8 -*-
import json, os
EP = "/data/scaleearn/terror_long/episodes"; os.makedirs(EP, exist_ok=True)
IB = "cinematic horror photography, %s, dark, eerie, foggy, moonlight, dramatic, high detail, 16:9"
def bt(t, i): return {"text": t, "img": IB % i}

# ============ L010 — LUGARES ASSOMBRADOS REAIS ============
L010 = {
 "id":"L010",
 "title":"6 Lugares REAIS Onde Ninguém Devia Entrar | Contos do Escuro",
 "thumb_title":"NÃO ENTRE AQUI",
 "channel":"contos",
 "description":"Seis lugares reais, que existem mesmo, e onde já aconteceram coisas que a lógica não explica: a floresta de Aokigahara, a Ilha das Bonecas, as Catacumbas de Paris, a ilha de Poveglia, o Castelo de Bran e o Hotel Cecil. Pode procurar: todos existem. E todos têm história. Fica até ao fim, porque o último tem imagens que ainda hoje assombram a internet.\n\nContos do Escuro — histórias e lugares de arrepiar, no escuro.\n#contosdoescuro #terror #lugaresassombrados #misterio #historiasreais",
 "tags":["contos do escuro","terror","lugares assombrados","misterio","historias reais","aokigahara","poveglia","assombracao","medo","catacumbas de paris"],
 "hook":"Os lugares que vais conhecer esta noite não são lenda. Existem mesmo. Podes vê-los no mapa, alguns podes até visitar. Mas quase todos têm uma regra em comum: há quem entre e não volte igual. E há quem entre e não volte de todo. Seis lugares reais. Uma história cada. No escuro.",
 "hook_img":"an abandoned eerie location at night, no people, cold moonlight, dread",
 "intro":"Bem-vindo de volta aos Contos do Escuro. Esta noite não há folclore nem inventona: são seis lugares que existem mesmo, e o que neles aconteceu está documentado. Fica até ao fim, porque o sexto é talvez o mais perturbador de todos, e tu vais entender porquê.",
 "intro_img":"a dark empty corridor in an abandoned building, flickering light",
 "outro":"Seis lugares reais, seis avisos. Se esta viagem te arrepiou, deixa o teu like, inscreve-te no Contos do Escuro e comenta qual destes lugares nunca visitarias nem de dia. E partilha com aquele amigo corajoso, para ver se ele aguenta até ao fim. Amanhã, à mesma hora, o escuro tem mais uma história à tua espera.",
 "outro_img":"a single candle flickering in total darkness, swirling smoke, deep shadows",
 "stories":[
  {"name":"A Floresta de Aokigahara (Japão)","title_img":"a dense silent dark forest at the foot of mount fuji, twisted roots, fog","beats":[
   bt("Aos pés do Monte Fuji, no Japão, existe uma floresta tão densa e silenciosa que lhe chamam 'o mar de árvores'. Lá dentro, o vento não entra. E o som do mundo desaparece.","a vast dense forest below mount fuji, thick canopy, silence"),
   bt("Aokigahara é real, e é um dos lugares mais evitados do planeta. O solo é vulcânico, cheio de cavernas de gelo, e as bússolas enlouquecem lá dentro.","a hiker holding a spinning compass in a dark forest"),
   bt("Mas não é a geografia que assusta os locais. É a quantidade de gente que entra… e nunca sai.","a single abandoned backpack on the dark forest floor"),
   bt("Visitantes relatam uma sensação de peso, de serem observados, e um silêncio que parece ter vontade própria.","a figure standing still among trees, a feeling of being watched"),
   bt("Deixam-se fitas pelo chão para marcar o caminho de volta. Algumas fitas acabam a meio. E ninguém sabe quem as cortou.","a colored ribbon tied to a tree, the end frayed, dark woods"),
   bt("A tradição japonesa diz que os espíritos dos que ali ficaram não deixam os vivos encontrar a saída. Aokigahara existe. E continua lá, esperando, em silêncio, aos pés da montanha mais sagrada do Japão.","a dark forest path dissolving into fog, no exit in sight")]},
  {"name":"A Ilha das Bonecas (México)","title_img":"an island with hundreds of broken dolls hanging from trees, dark water","beats":[
   bt("Num canal perto da Cidade do México, há uma pequena ilha coberta por centenas de bonecas. Partidas, sujas, de olhos vazios, penduradas em cada árvore.","an island full of old broken dolls hanging from trees, dusk"),
   bt("A Isla de las Muñecas é real. E a história por trás dela é mais triste do que assustadora, ao início.","close up of a dirty doll with one eye, hanging from a branch"),
   bt("Diz-se que um homem, Julián, encontrou o corpo de uma menina afogada no canal. E, logo depois, uma boneca a boiar.","a single doll floating on dark canal water, reeds"),
   bt("Atormentado, começou a pendurar bonecas por toda a ilha, para acalmar o espírito da criança.","a man hanging dolls across an island, obsessive, dark"),
   bt("Fez isso durante cinquenta anos. Visitantes juram que as bonecas mexem a cabeça, abrem os olhos e sussurram quando ninguém olha.","rows of dolls, some heads turned, eyes seeming to follow"),
   bt("Em 2001, Julián foi encontrado afogado. No mesmo ponto exato onde, décadas antes, encontrara a menina. A ilha existe. E as bonecas continuam lá, penduradas, à espera de visitas.","an old man's hat floating on dark water near a doll island")]},
  {"name":"As Catacumbas de Paris (França)","title_img":"endless walls of stacked human skulls and bones in dark underground tunnels","beats":[
   bt("Debaixo das ruas elegantes de Paris, a mais de vinte metros de profundidade, estende-se um labirinto feito de ossos.","dark underground tunnel walls lined with human bones"),
   bt("As Catacumbas guardam os restos de mais de seis milhões de pessoas, empilhados em paredes de crânios que se perdem no escuro.","walls of neatly stacked skulls disappearing into darkness"),
   bt("Só uma pequena parte é aberta ao público. O resto são centenas de quilómetros de túneis proibidos, sem mapa e sem luz.","a narrow flooded tunnel branching into total darkness"),
   bt("Exploradores clandestinos, os 'cataphiles', entram na parte proibida. Nem todos reaparecem.","a lone explorer's headlamp in a vast dark bone-filled tunnel"),
   bt("Em 1793, um homem perdeu-se lá em baixo. O seu corpo só foi encontrado onze anos depois, a poucos metros de uma saída que nunca chegou a ver.","a skeleton collapsed against a tunnel wall, old lantern"),
   bt("Dizem que, no silêncio total daquelas galerias, se ouvem passos que não são os nossos. As Catacumbas existem. E a maior parte delas ninguém, vivo, já percorreu por inteiro.","an endless dark bone tunnel, a faint figure far ahead")]},
  {"name":"A Ilha de Poveglia (Itália)","title_img":"an abandoned overgrown island with a ruined hospital tower, dark lagoon","beats":[
   bt("Na lagoa de Veneza, há uma ilha tão amaldiçoada que o governo italiano a proíbe a visitantes. Chama-se Poveglia.","a small abandoned island with ruins in a misty lagoon"),
   bt("Durante séculos, foi para onde Veneza enviava os doentes da peste, para morrerem longe da cidade.","old plague masks and ruins on an overgrown dark island"),
   bt("Estima-se que mais de cem mil pessoas morreram ali. Dizem que metade do solo da ilha é feito de cinzas humanas.","dark soil mixed with ash and bone fragments, ruins"),
   bt("Mais tarde, construíram um hospício. Reza a história que um médico fazia experiências cruéis nos pacientes.","an abandoned asylum corridor, broken windows, dark"),
   bt("Esse médico atirou-se da torre do sino. Antes de morrer, teria dito que uma névoa saída da terra o engoliu.","a tall ruined bell tower against a grey sky, mist below"),
   bt("Hoje, Poveglia está vazia e proibida. Os pescadores de Veneza não se aproximam. Dizem que, à noite, o sino da torre em ruínas ainda toca sozinho. A ilha existe. E ninguém quer lá pôr os pés.","a silent ruined island at night, a bell tower in fog")]},
  {"name":"O Castelo de Bran (Roménia)","title_img":"a gothic castle on a cliff at night, transylvania, dark forest, full moon","beats":[
   bt("Nas montanhas da Transilvânia, sobre um rochedo, ergue-se um castelo que o mundo inteiro associa a um nome: Drácula.","a gothic castle on a rocky cliff, dark transylvanian night"),
   bt("O Castelo de Bran é real. E embora o vampiro seja ficção, o homem que o inspirou foi bem pior.","an old portrait in a dark castle hall, candlelight"),
   bt("Vlad, o Empalador, aterrorizou a região no século XV com uma crueldade que gelava os seus próprios inimigos.","a dark medieval battlefield silhouette, impaled stakes, dusk"),
   bt("Diz-se que empalou dezenas de milhares de pessoas e jantava tranquilo no meio dos corpos.","a dim medieval banquet hall, a lone figure dining, shadows"),
   bt("Os corredores frios do castelo, as escadas secretas e as masmorras guardam ecos desse tempo.","a narrow dark stone staircase inside a castle, torchlight"),
   bt("Visitantes falam de arrepios súbitos, vultos nas janelas e portas que se fecham sozinhas. O castelo existe, podes visitá-lo. Mas há salas onde até os guias evitam ficar sozinhos depois do anoitecer.","a dark castle window with a faint pale face watching")]},
  {"name":"O Hotel Cecil (EUA)","title_img":"a tall old downtown hotel at night, neon sign, ominous windows","beats":[
   bt("Em Los Angeles, há um hotel com uma reputação tão sombria que mudou de nome para tentar fugir ao próprio passado.","a tall art deco hotel facade at night, dim neon sign"),
   bt("O Hotel Cecil acumulou, ao longo de décadas, uma lista arrepiante de mortes, desaparecimentos e tragédias.","a dim hotel lobby with old chandeliers, empty, eerie"),
   bt("Dois dos piores assassinos em série da América hospedaram-se lá. E muitos hóspedes nunca saíram vivos.","a dark hotel corridor with many closed doors, one ajar"),
   bt("Mas o caso que correu o mundo foi o de uma jovem, em 2013, filmada num elevador a comportar-se de forma impossível de explicar.","an old elevator with doors open, dim flickering light"),
   bt("Dias depois, o seu corpo foi encontrado dentro de um dos depósitos de água do telhado, de onde os hóspedes bebiam. Ninguém sabe como lá chegou.","a dark rooftop water tank against the night sky, ladder"),
   bt("As imagens dela no elevador ainda circulam na internet, e ninguém conseguiu explicar o que aconteceu. O Hotel Cecil existe. E há um andar que, dizem, nunca mais foi o mesmo.","a lone figure reflected in a dark elevator mirror, dread")]}
 ]
}

# ============ L011 — OBJETOS AMALDIÇOADOS ============
L011 = {
 "id":"L011",
 "title":"6 Objetos Amaldiçoados que Destruíram Quem os Tocou | Contos do Escuro",
 "thumb_title":"NÃO TOQUE",
 "channel":"contos",
 "description":"Seis objetos reais aos quais se atribuem maldições e mortes: a Caixa Dybbuk, o Diamante Hope, a boneca Annabelle, o Vaso de Basano, o quadro do Menino Chorão e a máscara de Tutancámon. Todos existem. Todos têm uma história de desgraça atrás de si. Fica até ao fim, porque o sexto amaldiçoou toda uma equipa de arqueólogos.\n\nContos do Escuro — histórias de arrepiar, no escuro.\n#contosdoescuro #terror #objetosamaldicoados #maldicao #historiasreais",
 "tags":["contos do escuro","terror","objetos amaldicoados","maldicao","annabelle","caixa dybbuk","diamante hope","historias reais","misterio","medo"],
 "hook":"Há objetos que não deviam existir. Uma caixa, um diamante, uma boneca, um quadro. À primeira vista, inofensivos. Mas cada um deixou atrás de si um rastro de mortes, acidentes e desgraças que ninguém consegue explicar por acaso. Esta noite, seis objetos amaldiçoados. E todos são reais.",
 "hook_img":"an old ornate box on a dark table, a single light, ominous shadow",
 "intro":"Bem-vindo de volta aos Contos do Escuro. Os objetos desta noite existem mesmo, alguns estão em museus, outros em coleções privadas bem trancadas. E todos partilham a mesma fama: quem os teve, pagou caro. Fica até ao fim, porque o último carrega a maldição mais famosa da história.",
 "intro_img":"a locked glass museum case with a single eerie object inside, dim light",
 "outro":"Seis objetos, seis maldições, todas reais. Se alguma destas histórias te arrepiou, deixa o teu like, inscreve-te no Contos do Escuro e comenta: aceitarias ter algum destes objetos em tua casa? Partilha com um amigo e vê se ele dormia com qualquer um deles por perto. Amanhã, à mesma hora, há mais uma história à tua espera, no escuro.",
 "outro_img":"a single candle flickering in total darkness, swirling smoke, deep shadows",
 "stories":[
  {"name":"A Caixa Dybbuk","title_img":"an old wooden wine cabinet box on a dark shelf, unsettling aura","beats":[
   bt("Começou como um simples armário de vinho antigo, comprado num leilão de espólio de uma senhora idosa.","an old wooden wine cabinet at an estate sale, dim light"),
   bt("Mas a família dela avisou o comprador: aquela caixa nunca devia ser aberta. Dentro, diziam, estava preso um 'dybbuk', um espírito maligno do folclore judaico.","an elderly hand refusing a box, fear in the eyes, dark room"),
   bt("O comprador ignorou. E a partir daí, a sua vida desmoronou: cheiro a urina de gato onde não havia gatos, lâmpadas que explodiam, pesadelos iguais em todos os que a tinham por perto.","a dark room with shattered light bulbs, swirling shadow"),
   bt("Cada pessoa que ficou com a caixa relatou o mesmo: doenças súbitas, sombras ao canto do olho, uma velha de rosto cavado nos sonhos.","a gaunt old hag face appearing in a nightmare, blurred"),
   bt("Ninguém a conseguia ter por muito tempo. Era vendida, dada, devolvida, sempre com as mesmas desgraças a seguir.","a box passing from hand to hand, each owner looking haunted"),
   bt("A Caixa Dybbuk é real, inspirou um filme de Hollywood, e hoje está escondida numa caixa feita por um exorcista. Reza a lenda que, enquanto estiver fechada, o que está lá dentro continua à espera.","a sealed box in a dark vault, faint scratching from within")]},
  {"name":"O Diamante Hope","title_img":"a large deep blue diamond glowing on black velvet, cold light","beats":[
   bt("É uma das joias mais belas e valiosas do mundo: um diamante azul profundo, do tamanho de uma noz. E uma das mais temidas.","a brilliant deep blue diamond on dark velvet, sparkling"),
   bt("Reza a lenda que o Diamante Hope foi arrancado do olho de uma estátua sagrada na Índia. E que, a partir daí, amaldiçoou todos os seus donos.","an ancient temple statue with one empty eye socket, dark"),
   bt("Reis destronados, aristocratas arruinados, uma rainha executada: muitos dos que o possuíram acabaram em tragédia.","a dark royal hall, an empty throne, a fallen crown"),
   bt("Uma das suas donas viu a família morrer um a um, até ela própria perder tudo o que tinha.","an elegant woman alone in a dark mansion, candlelight"),
   bt("Afogamentos, acidentes, falências, suicídios: a lista de desgraças ligadas à pedra tornou-se longa demais para ser coincidência.","a blue gem reflecting dark water, ominous ripples"),
   bt("Hoje, o Diamante Hope está num museu, atrás de vidro grosso, onde milhões o admiram, mas ninguém o leva para casa. Porque alguns dizem que a maldição só adormeceu. E espera por quem o ouse pôr ao pescoço de novo.","a blue diamond behind thick museum glass, cold reflection")]},
  {"name":"A Boneca Annabelle","title_img":"an old rag doll sitting alone in a locked wooden case, dim light","beats":[
   bt("Parece uma boneca de pano inofensiva, daquelas que qualquer criança teria no quarto. Mas esta está trancada dentro de uma caixa de vidro, com um aviso: não abrir.","an old rag doll in a glass case with a warning sign, dark"),
   bt("A história conta que duas jovens, donas da boneca, começaram a encontrá-la em posições diferentes, em divisões onde não a tinham deixado.","a doll moved to a new spot in a dark apartment, unsettling"),
   bt("Apareciam bilhetes escritos à mão: 'socorro'. E a boneca, dizem, começou a sangrar por uma mão.","a child's scrawled note reading help, beside a doll, dark"),
   bt("Investigadores do paranormal foram chamados. Concluíram que não era a boneca que estava 'viva', mas algo que se agarrara a ela.","two silhouettes examining a doll by lamplight, dark room"),
   bt("Um homem que zombou da boneca, dizem, morreu num acidente de mota ao sair do local.","a dark road at night, a crashed motorcycle, headlight beam"),
   bt("A Annabelle real está fechada numa vitrine abençoada, num museu do oculto. Inspirou filmes que o mundo inteiro viu. E, até hoje, ninguém que trabalha lá se atreve a abrir aquela caixa.","a rag doll behind glass, a faint shadow moving behind it")]},
  {"name":"O Vaso de Basano","title_img":"an ornate silver wedding vase on a dark windowsill, moonlight","beats":[
   bt("Em Itália, no século XV, uma noiva recebeu de presente um belo vaso de prata, na véspera do seu casamento.","an ornate silver vase held by a bride, candlelit room"),
   bt("Nessa mesma noite, foi encontrada morta, com o vaso ainda apertado nas mãos. As suas últimas palavras: 'o vaso vai levar-me'.","a bride lying still holding a silver vase, dark bedroom"),
   bt("O vaso passou de mão em mão na família. E, um por um, os donos foram morrendo jovens, sempre de forma estranha.","a silver vase passing between hands, each owner pale"),
   bt("Com medo, esconderam-no, embrulhado, durante séculos. Até que foi redescoberto, com um bilhete lá dentro: 'cuidado, este vaso traz a morte'.","an old folded warning note inside a silver vase, dark"),
   bt("Quem o comprou a seguir, morreu pouco depois. E o seguinte. E o seguinte.","a dusty vase on a shelf, three faded portraits beside it"),
   bt("Diz-se que, por fim, o vaso foi atirado pela janela, caiu aos pés de um polícia, e depois desapareceu em segredo do Estado. O Vaso de Basano existiu. E ninguém quer saber onde ele está agora.","a silver vase falling through a dark night sky, below a window")]},
  {"name":"O Menino Chorão","title_img":"an old framed painting of a crying boy, surrounded by scorch marks on a wall","beats":[
   bt("Nos anos 80, em Inglaterra, acontecia uma coisa impossível: casas ardiam por completo, mas um quadro sobrevivia intacto no meio das cinzas.","a burnt room, everything charred, one painting untouched"),
   bt("Era sempre o mesmo quadro: o retrato de um menino a chorar, de olhos grandes e tristes.","an old painting of a crying boy with big sad eyes, dim light"),
   bt("Dezenas de incêndios, por todo o país. E, em cada um, os bombeiros encontravam o Menino Chorão sem uma única marca de fogo.","firefighters pulling an intact painting from burnt debris"),
   bt("Corria o boato de que o pintor amaldiçoara o quadro, ou que o menino do retrato morrera num incêndio, anos antes.","a dim artist studio, a painting of a sad boy, flames reflected"),
   bt("O pânico foi tanto que um jornal organizou uma queima pública em massa de todas as cópias.","a bonfire of many identical paintings at night, crowd"),
   bt("Mesmo assim, as cópias originais são real, e muitas sobreviveram. E há quem, ainda hoje, se recuse a pendurar o Menino Chorão em casa. Porque onde ele está, dizem, o fogo nunca anda longe.","a crying boy painting on a wall, faint embers glowing nearby")]},
  {"name":"A Maldição de Tutancámon","title_img":"the golden burial mask of an egyptian pharaoh in a dark tomb, torchlight","beats":[
   bt("Em 1922, uma equipa de arqueólogos fez a maior descoberta da história: o túmulo intacto do faraó Tutancámon, no Egito.","archaeologists opening a dark egyptian tomb, torchlight, dust"),
   bt("Diz a lenda que, na entrada, estava uma inscrição: 'a morte virá, em asas rápidas, para quem perturbar o sono do faraó'.","ancient hieroglyphs on a dark tomb wall, torchlight"),
   bt("Poucas semanas depois, o homem que financiou a expedição morreu, de uma picada de mosquito infetada, no exato ponto onde a múmia tinha uma marca no rosto.","a dim 1920s room, a man gravely ill in bed, dark"),
   bt("No instante da sua morte, dizem, as luzes do Cairo apagaram-se todas. E, longe dali, em Inglaterra, o seu cão uivou e caiu morto.","city lights going dark over a 1920s skyline, ominous"),
   bt("Nos anos seguintes, vários membros da equipa morreram de formas estranhas e inesperadas, alimentando o terror da maldição.","faded portraits of expedition members, some crossed out"),
   bt("A ciência fala de fungos antigos selados no túmulo. Os outros falam de algo que não devia ter sido acordado. O túmulo existe, a máscara de ouro está num museu, e a pergunta continua: terá a equipa pago por perturbar o sono de um rei morto há três mil anos?","a golden pharaoh mask glinting in museum darkness")]}
 ]
}

# ============ L012 — RITUAIS PROIBIDOS ============
L012 = {
 "id":"L012",
 "title":"6 Rituais que Você NUNCA Deve Fazer | Contos do Escuro",
 "thumb_title":"NUNCA FAÇA ISTO",
 "channel":"contos",
 "description":"Seis rituais e jogos proibidos que circulam há décadas, com regras muito específicas, e um aviso em comum: há quem os tenha feito e se tenha arrependido. A Loira do Banheiro, o Jogo do Elevador, o Charlie Charlie, o Tabuleiro Ouija, os Três Reis e o Homem da Meia-Noite. Fica até ao fim, mas por favor: não tentes nenhum destes em casa.\n\nContos do Escuro — histórias de arrepiar, no escuro.\n#contosdoescuro #terror #ritualproibido #jogosproibidos #historiasdeterror",
 "tags":["contos do escuro","terror","rituais proibidos","jogos proibidos","ouija","jogo do elevador","charlie charlie","historias de terror","medo","assombracao"],
 "hook":"Existem jogos que não são jogos. Rituais com regras muito claras, passadas de boca em boca há gerações. Se seguires os passos certos, dizem, algo responde. O problema não é começar. O problema é terminar. Esta noite, seis rituais proibidos. E um conselho sincero: ouve até ao fim, mas não tentes nenhum.",
 "hook_img":"a dim room with a candle, a mirror, and a sense of something waiting",
 "intro":"Bem-vindo de volta aos Contos do Escuro. Os rituais desta noite circulam há décadas, em pátios de escola, em fóruns, em sussurros. Todos têm passos exatos e todos têm uma regra para parar, porque, dizem, parar a meio é a pior coisa que podes fazer. Fica até ao fim, porque o último é, de longe, o mais perigoso.",
 "intro_img":"a dark hallway with a single flickering candle on the floor",
 "outro":"Seis rituais, seis portas que é melhor deixar fechadas. Se este episódio te arrepiou, deixa o teu like, inscreve-te no Contos do Escuro e comenta qual destes já tinhas ouvido falar, ou, confessa, qual já quase tentaste. Mas promete uma coisa: deixa-os aqui, no escuro, onde pertencem. Amanhã, à mesma hora, tenho mais uma história para ti.",
 "outro_img":"a single candle flickering in total darkness, swirling smoke, deep shadows",
 "stories":[
  {"name":"A Loira do Banheiro","title_img":"a dim school bathroom with a cracked mirror, a single flickering light","beats":[
   bt("Todo o estudante conhece a regra do banheiro da escola: nunca estejas lá sozinho ao meio-dia, ou depois do último sino.","an empty dim school bathroom, cracked tiles, one light"),
   bt("Diz-se que, se chamares o nome dela três vezes em frente ao espelho, com a torneira a correr, ela atende.","a running tap, a hand reaching toward a dark mirror"),
   bt("É a Loira do Banheiro: o espírito de uma menina que, conta a lenda, morreu afogada numa sanita por colegas cruéis.","a pale girl's face forming in a steamy bathroom mirror"),
   bt("Chamada, ela surge no reflexo, de cabelo loiro encharcado a cobrir o rosto, e puxa quem a invocou para o espelho.","wet blonde hair over a pale face in a dark mirror"),
   bt("A regra para sobreviver, dizem, é nunca olhar diretamente nos olhos dela, e sair sem correr, sem mostrar medo.","a student backing slowly out of a dark bathroom door"),
   bt("Correr, dizem, é o convite. E por isso, em tantas escolas, as crianças nunca vão sozinhas ao banheiro quando o corredor já está vazio. Não por regra. Por medo.","an empty school corridor at dusk, one bathroom door ajar")]},
  {"name":"O Jogo do Elevador","title_img":"an old elevator with buttons, dim flickering light, empty","beats":[
   bt("Este ritual nasceu na Coreia e espalhou-se pelo mundo: usar um elevador para viajar a outro andar, um que não existe.","an old apartment elevator interior, dim buttons, night"),
   bt("As regras são exatas: sozinho, num prédio de pelo menos dez andares, carregas nos botões numa sequência específica, 4, 2, 6, 2, 10, 5.","a hand pressing elevator buttons in a precise sequence"),
   bt("Se fizeres tudo certo, dizem, o elevador sobe sozinho até ao décimo andar. E as portas abrem para um mundo que não é o teu.","elevator doors opening onto a dark empty unfamiliar floor"),
   bt("Tudo estará igual, mas vazio. Sem pessoas, sem som, com uma única luz vermelha ao longe.","a deserted building floor, one distant red light, silence"),
   bt("E há um aviso: se uma mulher entrar no elevador nesse andar, nunca, nunca lhe dirigas a palavra. Ela não é humana.","a dim elevator, a pale woman's silhouette entering"),
   bt("Para voltar, repetes a sequência ao contrário, sem sair. Quem conta estas histórias jura: alguns voltaram diferentes. E outros, dizem, simplesmente nunca mais voltaram ao andar certo.","elevator doors closing on a dark empty floor, red glow")]},
  {"name":"O Charlie Charlie","title_img":"two pencils forming a cross on paper with yes and no written, dim light","beats":[
   bt("Parece uma brincadeira de crianças, e por isso é tão perigoso: só precisas de uma folha, dois lápis e uma pergunta.","two pencils balanced in a cross on a paper, candlelight"),
   bt("Desenhas uma cruz, escreves 'sim' e 'não' nos quadrantes, equilibras um lápis sobre o outro, e perguntas: 'Charlie, Charlie, estás aqui?'","a hand drawing a cross grid with yes and no, dark table"),
   bt("Se o lápis de cima girar e apontar para 'sim', dizem, acabaste de abrir uma porta.","a pencil spinning on its own, pointing to the word yes"),
   bt("Charlie, segundo a lenda, é uma entidade que responde às tuas perguntas, movendo o lápis. Mas nem sempre diz a verdade. E nem sempre quer ir embora.","a pencil moving alone across a paper, cold draft, shadows"),
   bt("A regra mais importante é a de despedida: tens de perguntar 'Charlie, Charlie, podemos parar?' e esperar o 'sim' antes de desfazer tudo.","hands hovering over a charlie charlie paper, hesitating"),
   bt("Quem o faz e esquece de se despedir, dizem, leva Charlie consigo. E a partir daí, pequenas coisas começam a mover-se em casa, quando ninguém está a ver.","an everyday object moved slightly, an empty room, unease")]},
  {"name":"O Tabuleiro Ouija","title_img":"an old ouija board with a planchette, candles, dim seance room","beats":[
   bt("É talvez o ritual mais famoso do mundo, e um dos mais mal compreendidos: o tabuleiro Ouija.","an old ouija board on a dark table, two candles burning"),
   bt("Com letras, números e um 'sim' e 'não', serve, dizem, para falar com os mortos, movendo em conjunto uma pequena peça, a plancheta.","hands resting on a planchette over a ouija board, dim"),
   bt("As regras são de segurança: nunca jogar sozinho, nunca num cemitério, nunca perguntar quando vais morrer, e nunca deixar a plancheta percorrer o alfabeto todo, isso liberta o espírito.","a planchette sliding across ouija letters, candlelight"),
   bt("E a regra de ouro: terminar sempre com 'adeus'. Esse 'adeus' fecha a porta que abriste.","a planchette resting on the word goodbye, fading candle"),
   bt("Quem a usa sem respeito conta histórias de plancheta a desenhar o número oito deitado, o símbolo do infinito, sinal, dizem, de que algo que nunca foi humano está do outro lado.","a planchette tracing a figure eight on a dark board"),
   bt("Médiuns a sério recusam-se a tocar numa Ouija. Porque, dizem, não controlas quem atende. Só controlas se te lembras, no fim, de dizer adeus.","a dim room, a ouija board, the planchette moving alone")]},
  {"name":"Os Três Reis","title_img":"a dark room with two mirrors facing a chair and a single candle","beats":[
   bt("Este ritual é mais elaborado, e mais sério. Chama-se 'Os Três Reis', e serve, dizem, para encontrar respostas no reflexo.","a dim room at 3am, two large mirrors, one chair, candle"),
   bt("À noite, montas um 'trono': uma cadeira entre dois espelhos inclinados, uma vela, uma vasilha de água, e um relógio parado nas 3 e 33.","a candle, water bowl and clock in a mirrored dark room"),
   bt("Sentas-te às 3 e 33 da manhã e, dizem, entras num estado entre acordado e a sonhar, onde consegues falar com entidades: o Rei da Esquerda, o da Direita, e o do Meio, o teu próprio reflexo.","a person sitting between two mirrors in the dark, candle"),
   bt("As regras são rígidas: nunca olhar diretamente para os reis, nunca sair do trono antes das 4 e 34, e manter sempre a vela acesa.","a flickering candle beside a mirror, a dim seated figure"),
   bt("Se a vela se apagar, ou se algo te tocar, deves fechar os olhos e esperar. Sair a meio, dizem, deixa a porta aberta.","a snuffed candle, two dark mirrors, a shape in the glass"),
   bt("É dos rituais mais temidos da internet, justamente pela regra final: o que te responde do espelho pode não ser quem tu pensas. E pode decidir não deixar o reflexo quando o sol nascer.","a pale distorted reflection in a dark mirror at dawn")]},
  {"name":"O Homem da Meia-Noite","title_img":"a dark house at midnight, a single candle, a closed front door","beats":[
   bt("Guardei o pior para o fim. O ritual do Homem da Meia-Noite não é um jogo. É, dizem, uma caçada em que tu és a presa.","a dark house interior at midnight, one candle, dread"),
   bt("À meia-noite em ponto, apagas todas as luzes, escreves o teu nome num papel, pingas uma gota do teu sangue nele, e bates vinte e duas vezes na porta de casa.","a bloodied name on paper pinned to a dark front door"),
   bt("À vigésima segunda pancada, abres a porta, sopras a vela, e acendes de novo. A partir desse instante, dizem, o Homem da Meia-Noite está dentro de casa, contigo.","a candle being blown out by a dark doorway, midnight"),
   bt("O objetivo é sobreviver até às 3 e 33 da manhã, andando pela casa com uma vela acesa, fugindo da presença.","a person walking a dark house holding a single candle"),
   bt("Se a tua vela se apagar sozinha, tens cinco segundos para a reacender. Se não conseguires, deves rodear-te de sal, depressa, ou ele apanha-te.","a candle flame dying, a circle of salt poured in panic"),
   bt("Reza o aviso que, se falhares, ele te mostra a tua pior memória, ou algo pior. Por isso, de todos os rituais desta noite, este é o único que vem com uma regra acima de todas: nunca, jamais, o faças. Deixa o Homem da Meia-Noite aqui. No escuro.","a dark figure standing at the end of a candlelit hallway")]}
 ]
}

for ep in (L010, L011, L012):
    f = os.path.join(EP, "ep_%s.json" % ep["id"])
    json.dump(ep, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", f, "| stories:", len(ep["stories"]))
print("OK")
