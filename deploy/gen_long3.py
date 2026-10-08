# -*- coding: utf-8 -*-
import json, os
EP="/data/scaleearn/terror_long/episodes"; os.makedirs(EP,exist_ok=True)
IB="cinematic horror photography, %s, dark, eerie, foggy, moonlight, dramatic, high detail, 16:9"
def bt(t,i): return {"text":t,"img":IB%i}
def ep(_id,title,thumb,desc,tags,hook,hook_img,intro,intro_img,outro_img,stories):
    return {"id":_id,"title":title,"thumb_title":thumb,"channel":"contos","description":desc,
            "tags":tags,"hook":hook,"hook_img":IB%hook_img,"intro":intro,"intro_img":IB%intro_img,
            "outro":"Se este episódio te arrepiou, deixa o teu like, inscreve-te no Contos do Escuro e comenta qual destes casos ainda vai ficar contigo esta noite. Partilha com um amigo e vê se ele aguenta até ao fim. Amanhã, à mesma hora, o escuro tem mais uma história à tua espera.",
            "outro_img":IB%"a single candle flickering in total darkness, swirling smoke, deep shadows",
            "stories":stories}

def story(name,img,beats): return {"name":name,"title_img":IB%img,"beats":[bt(t,i) for (t,i) in beats]}

# ===== L013 — CASOS REAIS SEM EXPLICACAO =====
L013=ep("L013",
 "6 Casos Reais Que a Ciência NUNCA Conseguiu Explicar | Contos do Escuro",
 "SEM EXPLICAÇÃO",
 "Seis casos reais, documentados, que continuam sem resposta até hoje: o Passo Dyatlov, o massacre de Hinterkaifeck, a epidemia de riso de Tanganica, os gémeos Pollock, o sinal Wow! e o Bloop. Todos aconteceram mesmo. Nenhum foi explicado. Fica até ao fim, porque o primeiro é dos mistérios mais perturbadores de sempre.\n\nContos do Escuro — histórias de arrepiar, no escuro.\n#contosdoescuro #terror #misteriosreais #semexplicacao #casosreais",
 ["contos do escuro","terror","misterios reais","sem explicacao","passo dyatlov","casos reais","assombracao","medo","investigacao","sobrenatural"],
 "Os seis casos desta noite têm uma coisa em comum: aconteceram mesmo, foram investigados a fundo… e continuam sem explicação. Não são lendas. São relatórios, fotografias, corpos reais. E a verdade é que, por mais que a ciência tente, alguns mistérios simplesmente não querem ser resolvidos.",
 "a dark investigation room with old photos and files, single lamp",
 "Bem-vindo de volta aos Contos do Escuro. Esta noite não há folclore: só casos reais, daqueles em que os peritos desistiram de encontrar respostas. Fica até ao fim, porque cada um destes mistérios ainda tem gente, hoje, a tentar resolvê-los.",
 "old case files and black and white photographs on a dark desk",
 "",
 [
  story("O Passo Dyatlov","nine tents torn open on a snowy mountain at night, dark",[
   ("Em 1959, nas montanhas geladas dos Urais, nove alpinistas experientes montaram acampamento numa encosta nevada. Nenhum voltou.","a lit tent on a dark snowy mountain slope, blizzard"),
   ("Quando os encontraram, a tenda estava rasgada de dentro para fora. Eles tinham fugido para o frio, descalços, a menos trinta graus.","a tent slashed open from inside, footprints in deep snow"),
   ("Alguns morreram de hipotermia. Mas outros tinham fraturas violentas no crânio e nas costelas, sem qualquer ferida externa.","dark snow, scattered belongings, a torchlight beam at night"),
   ("A uma delas faltava a língua e os olhos. E a roupa de alguns continha níveis anormais de radiação.","a frozen figure in the snow, a geiger counter needle, dark"),
   ("A investigação soviética encerrou o caso com uma frase que só gerou mais perguntas: 'uma força natural desconhecida'.","an old soviet case file stamped closed, dim light"),
   ("Avalanche? Militares? Algo que viram e os fez correr para a morte? Mais de sessenta anos depois, ninguém sabe o que aconteceu, naquela noite, no Passo Dyatlov.","a dark empty snowy pass at night, nine faint silhouettes")]),
  story("O Massacre de Hinterkaifeck","an isolated snowy farmhouse at night, one dark window lit",[
   ("Numa quinta isolada na Alemanha, em 1922, uma família inteira foi assassinada. Mas o verdadeiro horror começou dias antes.","an isolated bavarian farm in snow, dusk, ominous"),
   ("O dono da quinta contou aos vizinhos que ouvia passos no sótão, via pegadas na neve que iam para a casa, mas nenhuma a sair.","footprints in snow leading to a dark farmhouse, none leaving"),
   ("Encontrou um jornal que ninguém da família tinha comprado. E ouvia ruídos à noite, por toda a casa.","an old newspaper on a dark wooden table, candlelight"),
   ("Poucos dias depois, os seis membros da família foram atraídos um a um ao celeiro e mortos com uma picareta.","a dark barn interior, a single hanging lantern, shadows"),
   ("O mais perturbador: o assassino ficou a viver na quinta durante dias. Alguém alimentou o gado e acendeu o fogão, com os corpos lá dentro.","smoke rising from a farmhouse chimney, a dark figure inside"),
   ("Nunca foi apanhado. Mais de cem anos depois, o caso de Hinterkaifeck continua aberto, e ninguém sabe quem, ou o quê, viveu com aqueles corpos.","an old farmhouse at night, one window glowing, snow falling")]),
  story("A Epidemia de Riso","a dark 1960s african schoolyard, blurred laughing figures",[
   ("Em 1962, numa escola na Tanzânia, três meninas começaram a rir. Um riso que não conseguiam parar.","a dim classroom, young students, an unsettling atmosphere"),
   ("Em poucos dias, o riso espalhou-se para quase cem alunas. Riam durante horas, às vezes dias, até caírem de exaustão.","a group of figures laughing uncontrollably, motion blur, dark"),
   ("Não era alegria. Vinha acompanhado de choro, dores, desmaios e ataques de pânico.","a person laughing and crying at once, tears, dark room"),
   ("A escola fechou. Mas as meninas levaram o 'riso' para casa, e ele espalhou-se por aldeias inteiras.","a dark village, faint sounds of laughter in the night"),
   ("Mais de mil pessoas foram afetadas. Dezenas de escolas tiveram de fechar durante quase dois anos.","empty classrooms with closed doors, dim light, silence"),
   ("Os médicos nunca encontraram vírus nem veneno. Até hoje, a epidemia de riso de Tanganica não tem explicação. Só o eco de milhares de pessoas a rir, sem conseguir parar.","a dark empty schoolyard at dusk, a faint distant laugh")]),
  story("Os Gémeos Pollock","two identical young girls standing in a dim room, old photo style",[
   ("Em 1957, na Inglaterra, duas irmãs foram atropeladas e morreram. Os pais, destroçados, acreditavam que elas voltariam.","two children's shoes by a dark roadside, dim evening"),
   ("Um ano depois, a mãe deu à luz gémeas. E, desde cedo, as recém-nascidas trouxeram coisas impossíveis.","a dim nursery, two cradles, soft eerie light"),
   ("Uma delas tinha a mesma marca de nascença, no mesmo sítio, de uma das irmãs falecidas.","a close up of a birthmark on a baby, soft dark light"),
   ("Quando cresceram, reconheceram brinquedos das irmãs mortas, que nunca lhes tinham mostrado, e chamaram-nos pelo nome.","old toys on a dark shelf, two small hands reaching"),
   ("Levadas a uma cidade onde nunca tinham estado, apontaram a escola e o parque das irmãs, como se fossem seus.","two girls pointing at a building, a grey street, dim"),
   ("E ambas entravam em pânico ao ver carros a aproximar-se. Coincidência, ou memória? O caso Pollock foi estudado por investigadores a sério, e nunca foi explicado.","two identical girls holding hands, a car headlight approaching")]),
  story("O Sinal Wow!","a vast radio telescope against a dark starry sky, eerie",[
   ("Em 1977, um radiotelescópio nos Estados Unidos apontava para o espaço profundo, à procura de sinais de vida.","a giant radio telescope dish under a dark starry sky"),
   ("Durante setenta e dois segundos, captou um sinal forte, claro, vindo da direção da constelação de Sagitário.","a radio signal spike on old printed data, red circle"),
   ("Era exatamente o tipo de transmissão que os cientistas esperavam de uma civilização inteligente.","an old computer printout, a cosmic frequency pattern, dark"),
   ("O astrónomo que o viu ficou tão espantado que escreveu ao lado, a vermelho: 'Wow!'. E esse é o nome que ficou.","a handwritten word Wow next to data, red ink, dim light"),
   ("O problema: nunca mais se repetiu. Apontaram o telescópio para o mesmo ponto centenas de vezes. Silêncio total.","a radio dish pointing at an empty dark sky, static"),
   ("Até hoje, ninguém sabe o que o enviou. Durante setenta e dois segundos, algo falou connosco a partir do fundo do espaço. E depois, calou-se para sempre.","deep space, distant stars, a single fading signal line")]),
  story("O Bloop","dark deep ocean, a sound wave ripple in black water",[
   ("No fundo dos oceanos, há sons que viajam milhares de quilómetros. Em 1997, os sensores captaram um que gelou os cientistas.","dark deep ocean water, sonar ripples, cold blue light"),
   ("Era um som ultra-baixo, poderoso, detetado por microfones a mais de cinco mil quilómetros de distância um do outro.","a sonar screen glowing in a dark room, a massive signal"),
   ("Chamaram-lhe 'the Bloop'. E o detalhe que arrepiou todos foi este: tinha o perfil de um ser vivo.","an operator staring at a dark sonar screen, dread"),
   ("Mas, para produzir um som tão alto, essa criatura teria de ser muito maior do que a maior baleia conhecida.","a vast dark ocean, an enormous shadow far below the surface"),
   ("Durante anos, a origem foi um mistério, alimentando teorias sobre o que poderia viver nas profundezas do Pacífico.","deep black water, a faint colossal silhouette, bubbles"),
   ("Mais tarde, atribuíram-no a gelo a partir-se na Antártida. Muitos aceitaram. Outros, não. Porque o oceano é fundo, escuro, e quase todo inexplorado. E lá em baixo, ainda há coisas que nunca vimos.","the dark ocean surface at night, something moving beneath")])])

# ===== L014 — CRIATURAS AVISTADAS NA VIDA REAL =====
L014=ep("L014",
 "6 Criaturas Que Foram Avistadas na Vida Real | Contos do Escuro",
 "ELES EXISTEM?",
 "Seis criaturas que centenas de pessoas juram ter visto, com relatos, fotos e testemunhos reais: o Monstro de Loch Ness, o Yeti, o Diabo de Jersey, o Monstro de Flatwoods, o Chupa-Cabra e o Demónio de Dover. Lenda ou algo mais? Fica até ao fim e decide por ti.\n\nContos do Escuro — histórias de arrepiar, no escuro.\n#contosdoescuro #terror #criaturas #criptideos #avistamentos",
 ["contos do escuro","terror","criaturas","criptideos","avistamentos","loch ness","yeti","chupacabra","misterio","medo"],
 "As seis criaturas desta noite têm algo em comum: não são só história para assustar. São relatos de gente real, muitas vezes várias pessoas ao mesmo tempo, que juram tê-las visto com os próprios olhos. Lenda coletiva, ou algo que a ciência ainda não quer admitir? Decide tu. No escuro.",
 "a dark forest edge at night, two faint glowing eyes watching",
 "Bem-vindo de volta aos Contos do Escuro. Esta noite falamos de criaturas avistadas na vida real, por caçadores, por famílias inteiras, por polícias. Fica até ao fim, porque algumas destas aparições nunca tiveram explicação, e continuam a ser vistas até hoje.",
 "an old blurry photograph of a strange creature, dim desk",
 "",
 [
  story("O Monstro de Loch Ness","a long dark shape rising from a misty scottish lake, dusk",[
   ("Na Escócia, há um lago fundo, frio e negro, com mais de duzentos metros de profundidade. E, dizem, com um habitante antigo.","a vast dark scottish loch at dusk, mist, mountains"),
   ("Há mais de mil e quinhentos anos que se fala de uma criatura nas suas águas. Longa, de pescoço comprido, como um réptil pré-histórico.","a long necked shadow in dark lake water, ripples"),
   ("Em 1934, uma fotografia espalhou a lenda pelo mundo: uma silhueta de pescoço fino a emergir da água.","an old grainy photo of a neck above dark water, vintage"),
   ("Desde então, milhares de pessoas juram tê-la visto. Alguns sonares detetaram objetos grandes e móveis no fundo.","a dark sonar screen showing a large moving object, lake"),
   ("Nunca ninguém provou que existe. Mas também nunca ninguém provou que não.","a calm dark loch surface at night, a single large ripple"),
   ("E assim, o Monstro de Loch Ness continua lá, no fundo frio da Escócia, à espera da próxima pessoa que olhe para a água na hora certa.","moonlight on a dark loch, a shadow passing beneath the surface")]),
  story("O Yeti","a huge white furred figure in a snowy mountain blizzard",[
   ("Nas montanhas mais altas do mundo, os Himalaias, os povos locais temem uma criatura há séculos: o Yeti, o abominável homem das neves.","snowy himalayan peaks at dusk, a dark figure in the distance"),
   ("Descrito como enorme, coberto de pelo, caminhando ereto como um homem, deixa pegadas gigantes na neve virgem.","giant footprints in fresh snow on a dark mountain slope"),
   ("Alpinistas experientes, incluindo os que conquistaram o Evereste, relataram pegadas sem explicação a milhares de metros de altitude.","a climber beside enormous footprints, snowy ridge"),
   ("Mosteiros guardam o que dizem ser relíquias do Yeti: couro cabeludo, ossos, mãos mumificadas.","an old monastery relic in dim light, fur and bone"),
   ("A ciência explicou alguns casos com ursos. Mas não todos. E os sherpas, que vivem naquelas montanhas, não têm dúvidas.","a snowy mountain trail at dusk, a large shadow between rocks"),
   ("Porque nas alturas geladas dos Himalaias, onde o ar é rarefeito e o silêncio é total, há zonas onde nenhum homem vai. E onde, dizem, algo já estava primeiro.","a lone figure on a vast snowy peak, a giant shape far off")]),
  story("O Diabo de Jersey","a winged kangaroo-like demon with a horse head in a dark pine forest",[
   ("Nos bosques de pinheiros de Nova Jersey, nos Estados Unidos, vive, dizem, uma criatura nascida de uma maldição.","a dark pine barrens forest at night, mist, dread"),
   ("A lenda conta que, em 1735, uma mulher, ao ter o seu décimo terceiro filho, o amaldiçoou. E ele nasceu como um demónio.","a stormy night, a dark cabin, a terrible cry inside"),
   ("Descrevem-no com cabeça de cavalo, asas de morcego, patas com garras e uma cauda longa.","a winged demonic silhouette with a horse head, moonlit forest"),
   ("Em 1909, durante uma semana inteira, centenas de pessoas em várias cidades relataram tê-lo visto, ao mesmo tempo.","frightened townsfolk pointing at the night sky, 1900s street"),
   ("Encontraram pegadas estranhas em telhados e na neve. Escolas e fábricas fecharam de medo.","strange hoofprints on a snowy rooftop, dark"),
   ("Mais de duzentos anos depois, ainda há avistamentos nos pinhais. O Diabo de Jersey tornou-se tão real para os locais que é, oficialmente, o símbolo do estado.","a dark pine forest, two red eyes and wings in the shadows")]),
  story("O Monstro de Flatwoods","a tall dark figure with a glowing red face and hood in a foggy field",[
   ("Em 1952, numa pequena cidade da Virgínia Ocidental, algo caiu do céu numa colina. Um grupo foi investigar.","a dark hill at night, a faint glow at the top, fog"),
   ("No topo, encontraram uma neblina estranha e, no meio dela, uma figura altíssima, com mais de três metros.","a towering dark silhouette in glowing mist on a hilltop"),
   ("Tinha um rosto vermelho brilhante, em forma de coração, e flutuava acima do chão, envolta numa espécie de capa.","a glowing red heart-shaped face in darkness, hovering"),
   ("Um cheiro intenso encheu o ar. As testemunhas fugiram. Várias adoeceram nas horas seguintes, com náuseas e irritação.","people fleeing down a dark hill, a glow behind them"),
   ("A polícia e a imprensa investigaram. Encontraram marcas no chão e um rasto de óleo estranho.","strange skid marks and residue on dark grass, torchlight"),
   ("Nunca houve explicação aceite por todos. O Monstro de Flatwoods foi visto por várias pessoas, na mesma noite. E nenhuma delas, até ao fim da vida, mudou a sua história.","a foggy field at night, a tall glowing-faced shape")]),
  story("O Chupa-Cabra","a spiny reptilian dog-like creature with red eyes in the dark",[
   ("Nos anos 90, por toda a América Latina, animais começaram a aparecer mortos de uma forma estranha: sem uma gota de sangue.","dead livestock in a dark field at night, no wounds visible"),
   ("As vítimas, sobretudo cabras, tinham apenas duas pequenas perfurações no pescoço. Daí o nome: Chupa-Cabra.","a goat lying still with two neck punctures, dark barn"),
   ("As testemunhas descreviam uma criatura do tamanho de um cão, com espinhos pelas costas, garras e olhos vermelhos brilhantes.","a spiny creature with glowing red eyes crouched in the dark"),
   ("O pânico espalhou-se de Porto Rico ao México, ao Brasil, aos Estados Unidos. Milhares de relatos, sempre com o mesmo padrão.","a dark rural road, red eyes reflecting in the headlights"),
   ("Alguns corpos de 'chupa-cabras' foram encontrados, mas revelaram-se, quase sempre, animais doentes.","a strange hairless animal carcass on dark ground, torchlight"),
   ("Quase sempre. Porque ainda há casos, e fazendeiros, que juram que o que mata o seu gado de noite não é coiote nenhum. É outra coisa. Algo que só sai no escuro.","a dark farm at night, two red eyes watching the animals")]),
  story("O Demónio de Dover","a thin grey creature with a large head and glowing orange eyes on a wall",[
   ("Em 1977, na pequena cidade de Dover, nos Estados Unidos, quatro adolescentes, em noites seguidas, viram a mesma coisa impossível.","a dark new england road at night, a low stone wall"),
   ("Uma criatura pequena, magérrima, de pele cinzenta e lisa, com uma cabeça enorme em forma de melão.","a thin grey humanoid with an oversized head, dark wall"),
   ("Não tinha nariz nem boca. Só dois grandes olhos que brilhavam, laranja num, verde no outro.","a close up of glowing orange eyes in the dark, grey skin"),
   ("Agarrava-se a um muro de pedra com dedos longos e finos, como ramos.","long thin fingers gripping a dark stone wall, moonlight"),
   ("As testemunhas, que não se conheciam todas, desenharam a mesma criatura, de forma independente.","four separate sketches of the same strange creature, dim"),
   ("Nunca foi identificada. O Demónio de Dover apareceu durante três noites, foi visto por quatro pessoas, e depois desapareceu para sempre. Deixando só desenhos iguais, e perguntas sem resposta.","an empty dark stone wall at night, a faint grey shape fading")])])

# ===== L015 — LUGARES ABANDONADOS =====
L015=ep("L015",
 "6 Lugares Abandonados Que Escondem Segredos Terríveis | Contos do Escuro",
 "ABANDONADOS",
 "Seis lugares reais que foram abandonados de um dia para o outro e guardam histórias arrepiantes: Pripyat (Chernobyl), a ilha-prisão de Hashima, a cidade em chamas de Centralia, Oradour-sur-Glane, a vila de diamantes engolida pelo deserto e a cidade fantasma de Bodie. Fica até ao fim.\n\nContos do Escuro — histórias de arrepiar, no escuro.\n#contosdoescuro #terror #lugaresabandonados #cidadesfantasma #misterio",
 ["contos do escuro","terror","lugares abandonados","cidades fantasma","chernobyl","pripyat","misterio","historia","medo","assombracao"],
 "Imagina acordar e ter de abandonar a tua cidade para sempre, deixando tudo para trás: a comida na mesa, os brinquedos no chão, as fotos na parede. Os seis lugares desta noite ficaram exatamente assim. Congelados no tempo, vazios de gente, mas cheios de histórias. E alguns, dizem, não estão assim tão vazios.",
 "an abandoned overgrown town street at dusk, empty, silent",
 "Bem-vindo de volta aos Contos do Escuro. Esta noite percorremos seis lugares reais que a humanidade abandonou. Podes ver fotos de todos. Fica até ao fim, porque o que aconteceu no quarto deles ainda arrepia a Europa inteira.",
 "an empty decayed room with peeling walls, a child's toy, dim",
 "",
 [
  story("Pripyat (Chernobyl)","an abandoned soviet city with a rusted ferris wheel, overgrown",[
   ("Em 1986, a cidade de Pripyat, na Ucrânia, tinha cinquenta mil habitantes e um parque de diversões novo em folha, prestes a abrir.","a soviet era city square with a new ferris wheel, overcast"),
   ("Mas, a poucos quilómetros, o reator nuclear de Chernobyl explodiu. E uma nuvem invisível e mortal cobriu tudo.","a distant nuclear plant with smoke, a grey ominous sky"),
   ("A cidade foi evacuada em horas. Disseram às pessoas que voltariam em poucos dias. Nunca voltaram.","a line of buses leaving a city, abandoned belongings, 1980s"),
   ("Pripyat ficou congelada no tempo: cadernos nas escolas, bonecas nas camas, a roda-gigante que nunca girou com ninguém.","a rusted ferris wheel over an empty overgrown square"),
   ("Hoje, a natureza tomou conta de tudo. Árvores crescem dentro dos prédios. Lobos passeiam pelas ruas vazias.","trees growing inside a ruined soviet apartment block"),
   ("É das poucas cidades do mundo onde ninguém pode viver durante milhares de anos. Um lugar lindo e terrível, onde o silêncio é a única coisa que sobrou, de uma cidade inteira apagada num só dia.","an empty radioactive city at dusk, overgrown and silent")]),
  story("A Ilha de Hashima (Japão)","a grey concrete island of ruined buildings in a dark sea",[
   ("Ao largo do Japão, há uma ilha de betão cinzento que parece um navio de guerra. Chamam-lhe a Ilha do Encouraçado.","a grey concrete island shaped like a battleship, dark sea"),
   ("Hashima foi, durante décadas, o lugar mais densamente povoado da Terra. Milhares de pessoas apinhadas, por cima de uma mina de carvão submarina.","a crowded old industrial island, grey apartment blocks"),
   ("Famílias viviam em apartamentos minúsculos, enquanto os homens desciam quilómetros abaixo do mar para extrair carvão.","dark narrow mine tunnels under the sea, dim lamps"),
   ("Muitos trabalhadores, incluindo prisioneiros forçados, morreram nas minas ou afogados.","a dark flooded mine shaft, old helmets, eerie"),
   ("Quando o carvão acabou, em 1974, toda a população partiu em semanas. A ilha foi deixada a apodrecer no mar.","empty crumbling apartment blocks on a grey island, dusk"),
   ("Hoje, os prédios estão a desfazer-se, as escadas levam ao vazio, e o vento uiva pelos corredores vazios. Hashima existe. E guarda, no fundo das suas minas, segredos que o mar nunca vai devolver.","a decayed concrete building interior, broken stairs, dark")]),
  story("Centralia, a Cidade em Chamas","a cracked road with smoke rising from the ground, abandoned town",[
   ("Na Pensilvânia, nos Estados Unidos, existe uma cidade onde o chão arde. E arde há mais de sessenta anos.","a road with smoke seeping from cracks, grey sky, empty"),
   ("Em 1962, um incêndio atingiu uma mina de carvão por baixo de Centralia. O fogo entrou nos túneis e nunca mais se apagou.","underground tunnels glowing with fire beneath a town"),
   ("A cidade começou a fumegar. O chão abria-se em fendas quentes. Gases tóxicos subiam dos quintais.","smoke rising from a crack in a suburban backyard, dark"),
   ("Em 1981, um menino quase foi engolido quando o chão se abriu sob os seus pés, revelando um poço fumegante sem fundo.","a sinkhole opening in dark ground, smoke, danger"),
   ("O governo pagou para todos saírem. Quase toda a gente partiu. As ruas foram arrancadas, as casas demolidas.","an empty cracked street, smoke, no houses, grey dusk"),
   ("Hoje, Centralia é quase uma cidade fantasma, de onde ainda sobe fumo pelas fendas do asfalto. E o fogo, dizem os geólogos, pode continuar a arder por mais duzentos e cinquenta anos.","a lone smoking crack in a deserted road at dusk")]),
  story("Oradour-sur-Glane (França)","a ruined village street with rusted cars frozen in time",[
   ("Em França, há uma aldeia inteira que foi deixada em ruínas de propósito, como a encontraram num dia terrível de 1944.","a ruined french village street, roofless stone houses"),
   ("Nesse dia, durante a guerra, soldados cercaram a aldeia de Oradour-sur-Glane sem aviso.","an empty village square at dusk, long shadows, dread"),
   ("Reuniram os homens nos celeiros, as mulheres e as crianças na igreja. E depois, o impensável aconteceu.","an old stone church interior in ruins, dim light"),
   ("Seiscentas e quarenta e duas pessoas morreram naquele dia. Quase toda a aldeia foi apagada em poucas horas.","a destroyed village, rusted bicycles and cars, grey"),
   ("Após a guerra, decidiram não reconstruir. Deixaram tudo exatamente como ficou: os carros enferrujados, as máquinas de costura, os utensílios na mesa.","a rusted old car parked in a ruined street, frozen in time"),
   ("Oradour é hoje um monumento silencioso. Andar pelas suas ruas vazias é andar dentro de um dia que nunca terminou. Um lugar real, onde o tempo parou, para que ninguém esqueça.","a silent ruined village street at dusk, no people")]),
  story("Kolmanskop, a Vila de Diamantes","sand-filled abandoned mansion rooms, desert, golden dark light",[
   ("No deserto da Namíbia, a areia engoliu uma vila inteira. Mas, em tempos, foi um dos lugares mais ricos do mundo.","sand dunes swallowing an abandoned desert town, dusk"),
   ("Kolmanskop nasceu quando encontraram diamantes à flor do chão. Em poucos anos, surgiu uma vila de luxo no meio do nada.","an elegant old colonial town in the desert, vintage"),
   ("Tinha salão de baile, hospital, até a primeira máquina de raios-x do hemisfério. Tudo pago a diamantes.","a grand ballroom interior, elegant, dim golden light"),
   ("Mas os diamantes acabaram. E, nos anos 50, a vila foi abandonada à pressa.","an empty luxury room, open doors, dust in the air"),
   ("Então o deserto começou a entrar. A areia invadiu as casas, subiu pelas escadas, encheu os quartos até às janelas.","sand pouring through a doorway, filling an elegant room"),
   ("Hoje, Kolmanskop é uma vila fantasma meio enterrada, onde se anda dentro de mansões cheias de areia dourada. Um lugar real, onde a riqueza foi engolida pelo deserto, grão a grão.","a sand-filled mansion room, golden light through broken windows")]),
  story("Bodie, a Cidade Amaldiçoada","an old wild west ghost town at dusk, wooden buildings, empty",[
   ("Na Califórnia, há uma cidade do Velho Oeste que ficou exatamente como estava quando o último morador partiu.","an old west ghost town street, wooden buildings, dusk"),
   ("Bodie nasceu da corrida ao ouro. No seu auge, teve dez mil pessoas, e uma reputação de violência brutal.","a dusty old west saloon interior, dim, abandoned"),
   ("Dizem que havia um assassinato por dia. As ruas eram tão perigosas que ganharam fama no país inteiro.","a dark old west street at night, long shadows, dread"),
   ("Quando o ouro acabou, a cidade esvaziou-se. Hoje está preservada em 'decadência congelada': casas com mobília, lojas com mercadoria, tudo intacto.","an abandoned general store with goods still on shelves, dim"),
   ("E há uma lenda tenaz: quem leva o que quer que seja de Bodie, até uma pedra, fica amaldiçoado.","a hand reaching for an old object in a dusty ghost town"),
   ("Os guardas do parque recebem, todos os anos, pacotes de turistas devolvendo objetos roubados, com cartas a implorar que a má sorte pare. A Maldição de Bodie, dizem, é bem real.","an old wooden ghost town at dusk, silent, a lone object on the ground")])])

# ===== L016 — GRAVACOES E FOTOS =====
L016=ep("L016",
 "6 Gravações e Fotos Que Nunca Deviam Existir | Contos do Escuro",
 "NÃO VEJA ISTO",
 "Seis registos reais, fotos e gravações, que correram a internet e nunca foram totalmente explicados: a invasão do sinal da TV por Max Headroom, o vídeo perturbador 'I Feel Fantastic', o disco misterioso 11B-X-1371, a fotografia do suposto viajante do tempo, as últimas fotos do Passo Dyatlov e a foto da família de Cooper. Fica até ao fim.\n\nContos do Escuro — histórias de arrepiar, no escuro.\n#contosdoescuro #terror #misteriosdainternet #gravacoes #creepy",
 ["contos do escuro","terror","misterios da internet","gravacoes","fotos misteriosas","creepy","max headroom","medo","assombracao","investigacao"],
 "Nem tudo o que a câmara capta devia ter sido captado. Esta noite são seis registos reais, fotografias e vídeos, que apareceram e deixaram o mundo sem resposta. Podes procurar por quase todos. Mas vais ver: algumas coisas, depois de vistas, não se conseguem esquecer.",
 "an old crt television showing static in a dark room",
 "Bem-vindo de volta aos Contos do Escuro. Esta noite não há criaturas: há câmaras, ecrãs e fotografias. Registos reais que correram o mundo e que ninguém explicou por completo. Fica até ao fim, porque o último é uma fotografia que ainda divide a internet.",
 "an old photograph being examined under a lamp in the dark",
 "",
 [
  story("A Invasão de Max Headroom","a glitchy figure in a suit and sunglasses on a television screen, dark",[
   ("Em 1987, em Chicago, milhares de pessoas viam televisão, quando o sinal foi, de repente, sequestrado.","a 1980s living room at night, a glitching tv screen"),
   ("O ecrã tremeu e apareceu uma figura com uma máscara, imitando uma personagem famosa da época, com um fundo que rodava sem parar.","a masked figure with a spinning background, tv static"),
   ("Durou pouco mais de um minuto. A figura ria, murmurava frases sem sentido, e fazia gestos perturbadores.","a distorted masked face laughing on a tv screen, dark"),
   ("Não havia áudio decente, só um zumbido e palavras entrecortadas que ninguém entendia bem.","a glitchy tv broadcast with garbled distorted audio bars"),
   ("E depois, o sinal voltou ao normal, como se nada fosse.","a tv returning to a normal broadcast, a dark room"),
   ("Até hoje, ninguém sabe quem o fez. Precisavam de equipamento caríssimo para sequestrar um canal inteiro. A invasão de Max Headroom continua por resolver, uma das maiores piratarias televisivas da história.","an old tv showing static alone in a dark empty room")]),
  story("O Vídeo 'I Feel Fantastic'","a creepy mannequin-like figure in a garden, unsettling, dim",[
   ("Nos primórdios da internet, surgiu um vídeo caseiro que arrepiou milhões: uma figura semelhante a um manequim, a cantar.","a mannequin-like figure standing stiffly in a dim room"),
   ("Era uma espécie de robô ou boneca humana, movendo-se de forma rígida, cantando uma música alegre com voz mecânica.","a stiff humanoid figure singing, mechanical, eerie light"),
   ("A letra dizia 'eu sinto-me fantástico', mas o tom e a imagem passavam exatamente o contrário.","a close up of a mannequin face, a forced unsettling smile"),
   ("O que correu a internet foi uma teoria sombria: algumas cenas mostravam a figura em jardins e bosques.","a mannequin figure outdoors in a dark garden at dusk"),
   ("As pessoas convenceram-se de que o fundo escondia pistas de algo terrível, enterrado por perto.","dark woods at night, a figure standing among the trees"),
   ("O criador acabou por explicar que era só arte perturbadora, um robô que construiu. Mas o vídeo tornou-se uma lenda da internet, daquelas que ninguém consegue ver sozinho, de luz apagada.","an old computer screen glowing with an eerie video, dark room")]),
  story("O Disco 11B-X-1371","a hooded figure in a plague mask holding a sign in a dark field",[
   ("Em 2015, um youtuber recebeu pelo correio um pacote sem remetente. Dentro, um DVD, e nada mais.","an unmarked package and a plain disc on a dark table"),
   ("O vídeo mostrava uma figura de capa e máscara de peste, numa floresta, fazendo gestos lentos e inquietantes.","a plague-masked hooded figure gesturing in a dark forest"),
   ("Mas o verdadeiro horror estava escondido no ficheiro. Nos sons e nas imagens, havia mensagens codificadas.","audio waveforms hiding a secret image, dark screen"),
   ("Decifradas, revelaram ameaças, coordenadas de lugares reais, e fotografias perturbadoras, incluindo de vítimas.","coordinates and cryptic symbols glowing on a dark screen"),
   ("A mensagem terminava com um aviso arrepiante, dirigido a quem estava a ver.","a cryptic warning message on a black screen, red text"),
   ("A polícia investigou. Houve teorias de tudo: um jogo, um alternate reality game, ou algo muito pior. Mas quem enviou o disco 11B-X-1371, e porquê, continua a ser um mistério total.","a plain disc spinning in a dark room, a masked figure on screen")]),
  story("A Fotografia do Viajante do Tempo","an old 1940s crowd photo, one man dressed oddly modern, grainy",[
   ("Em 2010, uma fotografia antiga, de 1941, tirada na inauguração de uma ponte no Canadá, espalhou-se pela internet.","a vintage 1940s crowd at an outdoor event, grainy photo"),
   ("Na multidão, toda vestida à moda dos anos 40, um homem destacava-se de forma impossível.","a crowd in 1940s clothes, one figure standing out, dim"),
   ("Usava o que parecia ser uma camisola moderna, óculos de sol atuais, e segurava algo parecido com uma câmara compacta.","a man in modern-looking clothes among 1940s people, grainy"),
   ("Para muitos, era a prova: um viajante do tempo, apanhado por acidente numa fotografia de oitenta anos.","a blurry close up of a man holding a small modern device"),
   ("Os céticos explicaram: as roupas e os óculos já existiam, de forma rara, na época.","vintage sunglasses and knitwear from the 1940s, dim light"),
   ("Mas a imagem é real, não foi manipulada, e ninguém nunca identificou o homem. E assim ele continua ali, parado na multidão, a olhar para a câmara, um rosto fora do seu tempo.","a vintage crowd photo, one face circled, out of place")]),
  story("As Últimas Fotos de Dyatlov","a grainy black and white photo of a blurry glowing shape at night",[
   ("Voltamos ao Passo Dyatlov, mas desta vez à prova mais perturbadora: os rolos de filme encontrados com os corpos.","old film rolls and a camera found in the snow, dark"),
   ("Os alpinistas fotografaram a sua própria viagem, até à última noite. E essas fotos foram reveladas.","a developing photograph in a dark room, red light"),
   ("As primeiras mostram jovens sorridentes na neve. As últimas, tiradas naquela noite, mostram algo diferente.","happy hikers in old photos, then darker frames, grainy"),
   ("Num dos últimos fotogramas, vê-se apenas escuridão, e uma luz estranha, difusa, ao longe.","a black and white photo of a strange glowing light in the dark"),
   ("Ninguém sabe se foi um acidente da câmara, ou se eles fotografaram o que quer que os fez fugir.","a grainy frame showing a blurry bright shape at night"),
   ("Essa imagem, a última que alguns deles tiraram, continua a alimentar teorias até hoje. Porque talvez, naquele fotograma escuro, esteja a resposta para tudo. Uma resposta que ninguém consegue ler.","an old photograph of darkness and a single glowing blur")]),
  story("A Fotografia de Cooper","an old family photo in a house, a dark shape on the ceiling",[
   ("Em 1959, uma família mudou-se para uma nova casa no Texas. Para celebrar, tiraram uma fotografia de família.","a 1950s family posing in a living room, vintage photo"),
   ("Quando a revelaram, encontraram algo que não estava lá quando a tiraram.","a developing family photo in a dark room, red glow"),
   ("No teto, por cima deles, havia uma figura. O que parecia ser um corpo a cair, de cabeça para baixo, do teto.","an old photo with a blurry falling figure on the ceiling"),
   ("Nenhum dos presentes tinha visto nada. A figura não correspondia a ninguém da família.","a family looking up in confusion, a dark shape above, dim"),
   ("Analistas estudaram a imagem durante décadas. Alguns dizem ser um defeito do rolo. Outros, não têm tanta certeza.","an old negative held up to light, a strange shape, dark"),
   ("A 'Cooper Falling Body' é uma fotografia real, muito estudada, e nunca explicada por completo. Uma imagem de uma família feliz, com algo impossível, pendurado por cima das suas cabeças.","a vintage family photo, a falling figure on the ceiling, eerie")])])

# ===== L017 — DESAPARECIMENTOS =====
L017=ep("L017",
 "6 Pessoas Que Desapareceram Sem Deixar Rasto | Contos do Escuro",
 "DESAPARECIDOS",
 "Seis casos reais de desaparecimento que nunca foram resolvidos: as crianças Sodder, o misterioso D.B. Cooper, o jovem Brandon Swanson ao telefone com os pais, os cinco rapazes de Yuba County, Granger Taylor e a sua nave, e Lars Mittank. Pessoas reais, que existiram mesmo, e que um dia simplesmente deixaram de existir. Fica até ao fim.\n\nContos do Escuro — histórias de arrepiar, no escuro.\n#contosdoescuro #terror #desaparecimentos #casosreais #misterio",
 ["contos do escuro","terror","desaparecimentos","casos reais","misterio","sem explicacao","investigacao","medo","assombracao","sumico"],
 "Todos os anos, pessoas desaparecem. A maioria é encontrada. Mas algumas evaporam-se, como se o chão as tivesse engolido. Sem corpo, sem pistas, sem explicação. Os seis casos desta noite são reais, estão nos arquivos da polícia, e continuam abertos. Porque, às vezes, a pergunta mais assustadora não é 'quem', mas 'para onde'.",
 "a dark empty road at night disappearing into fog",
 "Bem-vindo de volta aos Contos do Escuro. Esta noite falamos de pessoas reais que desapareceram sem deixar rasto, e cujas famílias, muitas delas, ainda esperam por respostas. Fica até ao fim, com respeito, porque alguns destes mistérios ainda podem, um dia, ser resolvidos.",
 "old missing person photographs pinned to a dark board",
 "",
 [
  story("As Crianças Sodder","an old house on fire at night, five small shadows in a window",[
   ("Na véspera de Natal de 1945, nos Estados Unidos, a casa da família Sodder incendiou-se durante a noite.","a house engulfed in flames on a snowy christmas night"),
   ("Os pais e quatro filhos escaparam. Mas cinco das crianças, que dormiam lá em cima, nunca foram encontradas.","a burning house, parents watching helpless, snow, dark"),
   ("O estranho é que, apesar do fogo, não restaram ossos nem restos das cinco crianças. Nada.","firefighters searching cold ashes of a house, finding nothing"),
   ("Antes do incêndio, a linha de telefone fora cortada, e uma escada desaparecera. Testemunhas disseram ter visto as crianças, depois, num carro.","a cut telephone wire in the snow, a dark car leaving"),
   ("Anos mais tarde, a mãe recebeu pelo correio a fotografia de um jovem, com uma mensagem no verso, que, jurava, era um dos seus filhos crescido.","an old photo of a young man, a cryptic note on the back"),
   ("A família nunca desistiu. Puseram um enorme cartaz na estrada durante décadas, com os rostos das cinco crianças. Até hoje, ninguém sabe o que lhes aconteceu, naquela noite de Natal.","a weathered billboard with five children's faces, dusk")]),
  story("D.B. Cooper","a man in a suit with a parachute jumping from a plane into a storm",[
   ("Em 1971, um homem de fato e gravata comprou um bilhete de avião com um nome falso: Dan Cooper.","a 1970s airport, a man in a suit boarding a plane"),
   ("A meio do voo, entregou um bilhete à comissária. Dizia que tinha uma bomba na pasta.","a hand passing a note on a plane, a briefcase, tense"),
   ("Exigiu duzentos mil dólares e quatro paraquedas. As autoridades cederam, e a maioria dos passageiros foi libertada.","stacks of cash and parachutes handed over on a tarmac, night"),
   ("Com o dinheiro e os paraquedas, mandou o avião levantar voo de novo. E então, sobre a floresta escura, abriu a porta traseira e saltou.","a man jumping from a plane's rear stairs into a dark storm"),
   ("Nunca mais foi visto. Nem vivo, nem morto. Anos depois, uma criança encontrou parte do dinheiro enterrado num rio.","decayed banknotes found on a dark riverbank, torchlight"),
   ("Foi a única pirataria aérea não resolvida da história dos Estados Unidos. D.B. Cooper saltou para o escuro, e levou o seu segredo consigo, para onde quer que tenha caído.","a dark stormy forest seen from above, a single parachute")]),
  story("Brandon Swanson","a young man's car in a dark ditch, a phone light in a field at night",[
   ("Em 2008, um jovem americano, Brandon, ligou aos pais à noite. Tinha saído da estrada e o carro estava preso numa vala.","a car stuck in a roadside ditch at night, headlights on"),
   ("Estava bem, sem ferimentos. Combinou encontrar-se com os pais, que foram de carro buscá-lo.","parents driving on a dark rural road at night, worried"),
   ("Ao telefone, Brandon dizia ver as luzes de uma vila ao longe, e decidiu caminhar em direção a elas.","a young man walking across a dark field toward distant lights"),
   ("Os pais ficaram ao telefone com ele durante quase uma hora, enquanto ele atravessava campos no escuro.","a phone held to an ear, a dark field, faint village lights"),
   ("E então, a meio de uma frase, Brandon soltou um palavrão, como se tivesse tropeçado em algo. E a chamada ficou em silêncio.","a dropped phone glowing in dark grass, no one around"),
   ("Nunca mais atendeu. Nunca mais foi encontrado. Buscas enormes não revelaram nada. Brandon Swanson desapareceu no meio de uma conversa, no escuro de um campo, a poucos passos dos pais que o ouviam.","an empty dark field at night, a faint phone glow fading")]),
  story("Os Cinco de Yuba County","five young men's car abandoned on a dark mountain road, snow",[
   ("Em 1978, cinco amigos foram a um jogo de basquetebol e, no regresso, desapareceram todos de uma vez.","five friends in an old car driving at night, headlights"),
   ("O carro deles foi encontrado abandonado numa estrada de montanha, longe do caminho de casa, com combustível e sem avarias.","an abandoned car on a snowy mountain road, doors closed"),
   ("Não fazia sentido. Porque tinham subido a montanha gelada, à noite, deixando o carro bom para trás?","a dark forest mountain road, deep snow, an empty car"),
   ("Meses depois, encontraram os corpos de quatro deles, espalhados pela floresta, tendo morrido de frio e fome.","a dark snowy forest, scattered search lights at dusk"),
   ("Um deles tinha-se abrigado numa cabana de guardas florestais, com comida e mantimentos ali mesmo, e mesmo assim morreu.","an old ranger cabin in snow, dim, supplies untouched inside"),
   ("O quinto nunca foi encontrado. Porque subiram a montanha? Do que fugiam? O caso dos Cinco de Yuba County continua sem explicação, um dos mais estranhos de sempre.","five faint silhouettes walking into a dark snowy forest")]),
  story("Granger Taylor","a man building a metal spaceship in a dark field, workshop lights",[
   ("No Canadá, nos anos 70, vivia Granger Taylor, um génio da mecânica que largou a escola e construía máquinas impossíveis.","a man in a workshop surrounded by machines, dim light"),
   ("Obcecado com o espaço, construiu, no quintal, uma réplica de uma nave espacial a partir de sucata.","a homemade metal flying saucer in a dark field, workshop glow"),
   ("Dizia aos amigos que falava com extraterrestres nos sonhos, e que eles o tinham convidado para uma viagem.","a man staring at the night sky, stars, a strange glow"),
   ("Numa noite de tempestade, em 1980, deixou um bilhete aos pais. Dizia que ia partir numa viagem pelo espaço, por quarenta e dois meses.","a handwritten note on a dark table, a storm outside"),
   ("Nessa noite, desapareceu. E a sua nave caseira desapareceu com ele.","an empty field where a structure once stood, storm, night"),
   ("Anos depois, encontraram destroços de um carro numa explosão na montanha, possivelmente dele. Mas nunca houve certeza. Granger Taylor disse que ia viajar para as estrelas, e simplesmente nunca mais voltou.","a stormy night sky over dark mountains, a single strange light")]),
  story("Lars Mittank","a young man looking back at an airport camera, running, night",[
   ("Em 2014, um jovem alemão, Lars, estava de férias na Bulgária com amigos. No fim da viagem, tudo mudou.","a sunny beach resort fading to a dark unsettling street"),
   ("Envolveu-se numa briga e ficou com uma lesão no ouvido. O médico disse-lhe para não voar, e ficar mais uns dias.","a dim clinic room, a worried young man, bandage"),
   ("Sozinho, num hotel estranho, Lars começou a enviar mensagens assustadas aos pais, dizendo que quatro homens o perseguiam e queriam matá-lo.","a young man texting nervously in a dark hotel room, fear"),
   ("No aeroporto, no dia seguinte, foi filmado pelas câmaras a comportar-se de forma cada vez mais aterrorizada.","airport security footage of a nervous man looking around"),
   ("De repente, agarrou a mochila, saltou por cima de um balcão, e desatou a correr para fora do aeroporto, para o escuro.","a man running out of an airport exit into the night, cameras"),
   ("Foi a última vez que alguém o viu. A imagem dele, a olhar para trás e a fugir, é tudo o que resta. Lars Mittank correu para fora daquela câmara, para o escuro, e nunca mais foi encontrado.","an empty airport exit at night, a last frozen camera frame")])])

for e in (L013,L014,L015,L016,L017):
    f=os.path.join(EP,"ep_%s.json"%e["id"])
    json.dump(e,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("wrote",f,"| stories:",len(e["stories"]))
print("OK")
