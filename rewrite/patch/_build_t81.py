#!/usr/bin/env python3
"""Build T81 Koch batch-B manifest: 10 blends (Abnoba→Bath) + 3 batch-A
sources gains (Badb, boar, aisling). Koch 2006 enrichment, own-words
CSG-SME1000 prose, verbatim-6 self-checked against culture.txt + myth.txt."""
import json, re, unicodedata

REPO = "/home/hermes/code/openordu/pce-clawson"

def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace("’", "'").replace("‘", "'")
    s = re.sub(r"[^a-z0-9' ]", " ", s)
    return " ".join(s.split())

# corpus for verbatim-6 probe
corpus = ""
for c in ("sources/culture.txt", "sources/myth.txt"):
    corpus += norm(open(f"{REPO}/{c}", encoding="utf-8", errors="replace").read()) + "\n"
corpus_toks = corpus.split()
CORPUS6 = {" ".join(corpus_toks[i:i+6]) for i in range(len(corpus_toks) - 5)}

def lint(text, label):
    assert "\n" not in text, label + ": newline"
    assert ";" not in text, label + ": semicolon"
    low = " " + text.lower() + " "
    for bad in (" very ", " really ", " truly ", " extremely ", " incredibly "):
        assert bad not in low, label + ": intensifier " + bad.strip()
    for s in re.split(r"(?<=[.!?]) ", text):
        assert len(s.split()) <= 30, label + ": long sentence (" + str(len(s.split())) + "w): " + s[:70]
    assert len(text) >= 150, label + ": text <150"
    toks = norm(text).split()
    for i in range(len(toks) - 5):
        run = " ".join(toks[i:i+6])
        assert run not in CORPUS6, label + ": verbatim-6 [" + run + "]"

ALLOWED = {"Person", "Place", "Deity", "Being", "Creature", "Event", "Artifact",
           "Concept", "Culture", "Group", "Animal", "Object", "Role", "Title",
           "Festival", "Motif", "Country", "Plant", "Saint", "Organization"}

M = {}

def blend(fn, cite, text, ents_new, attrs_new, okr):
    lint(text, fn)
    for e, t in ents_new:
        assert t in ALLOWED, fn + ": type " + t
    M[fn] = {"text": text,
             "entities": [{"entity": e, "type": t} for e, t in ents_new],
             "attributes": [{"entity": e, "attribute": a} for e, a in attrs_new],
             "okr": okr,
             "add_sources": [cite]}

# ---------- 1. Abnoba ----------
blend("Abnoba.json", "Koch 2006, s.v. 'Abnoba'.",
 "Abnoba is a Celtic goddess honoured in Britain and on the mainland. "
 "She gave her name to rivers called Avon, as the one in England that runs through Stratford. "
 "Rome called the Black Forest Mons Abnoba in her honor, and streams from its eastern slopes meet to form the young river Danube. "
 "A stone statue from Mühlburg shows her dressed as Diana, touching a tree while a hound and a hare rest beneath. "
 "A relief at the source of the Brigach adds a stag and a bird to her company. "
 "The hare ties her to the same ritual world as the goddess Andraste. "
 "Inscriptions from Muhlbach and Rothenburg keep her name, and a bronze native Diana in Köln may show her or the goddess Arduinna. "
 "Pliny and Tacitus both name her in their writings. "
 "Her image shows a huntress, her hunting dog, and a stag beside her.",
 [("Abnoba", "Being"), ("Diana", "Being"), ("Black Forest", "Place"),
  ("Danube", "Place"), ("Arduinna", "Deity"), ("Brigach", "Place")],
 [("Abnoba", "gave her name to the river Avon"),
  ("Abnoba", "ruled the source of the Danube"),
  ("Black Forest", "the Mons Abnoba of the Romans, where she was tutelary goddess"),
  ("Abnoba", "shown as Diana touching a tree with a hound and a hare at Mühlburg"),
  ("Brigach", "her relief at its source adds a stag and a bird")],
 {"objective": "Record Abnoba, the Black Forest goddess whom Rome read as Diana.",
  "key_results": ["Rome named the Black Forest Mons Abnoba, and its eastern streams form the Danube's source.",
                  "A statue at Mühlburg shows her as Diana with a tree, a hound, and a hare.",
                  "A relief at the Brigach source adds a stag and a bird, and inscriptions keep her name.",
                  "Pliny and Tacitus both record her."],
  "evidence": "Monaghan 2003, s.v. Abnoba; Koch 2006, s.v. 'Abnoba'."})

# ---------- 2. Andraste ----------
blend("Andraste.json", "Koch 2006, s.v. 'Andraste / Andrasta'.",
 "Andraste is a British goddess, also written Andrasta. "
 "The historian Cassius Dio preserves the only surviving account of her, and he says the name meant victory. "
 "The form looks like a feminine name built on a verb that carries the Celtic negative prefix an-, so it may suggest the unconquerable one. "
 "The warrior queen Boudicca of the Iceni called on her during the rising of ad 61. "
 "In the rite Boudicca freed a hare from among the folds of her garment, and the way it ran told the warriors the attack held favor. "
 "In her speech she hailed the goddess as one woman to another and asked for triumph, life, and freedom. "
 "Dio adds that the goddess was worshipped in a grove, a nemeton, where Roman women were put to death during the revolt. "
 "The hare was an occasional symbol of the warrior queen Medb, famed in Ireland. "
 "It turns fierce when caught, and so it fits an image of defense. "
 "Boudicca came close to driving the Romans from her land. "
 "When the war turned against her, she died by her own hand rather than face the humiliations the Romans gave their defeated enemies.",
 [("Andraste", "Being"), ("Andrasta", "Being"), ("Cassius Dio", "Person"),
  ("Boudicca", "Person"), ("Iceni", "Organization"), ("Romans", "Organization"),
  ("Medb", "Person"), ("hare", "Being"), ("nemeton", "Concept")],
 [("Boudicca", "invoked her in a sacred rite before battle"),
  ("Andraste", "name means victory, from a verb with the negative prefix an-"),
  ("hare", "released in her ritual, a symbol of the queen Medb"),
  ("Boudicca", "freed a hare from her garment to read the omen"),
  ("Andraste", "worshipped in a grove where Roman women died in the revolt"),
  ("Cassius Dio", "preserves the only surviving account of the goddess")],
 {"objective": "Record Andraste, the British victory goddess invoked by Boudicca.",
  "key_results": ["Cassius Dio preserves the only surviving account and gives the name the sense of victory.",
                  "Boudicca freed a hare from her garment as an omen before the rising of ad 61.",
                  "The goddess was worshipped in a grove, a nemeton, where Roman women died in the revolt."],
  "evidence": "Monaghan 2003, s.v. Andraste; Koch 2006, s.v. 'Andraste / Andrasta'."})

# ---------- 3. Annwn ----------
blend("Annwn.json", "Koch 2006, s.v. 'Annwn / Annwfn'.",
 "Annwn, also called Annwyn and Annwfn, is the Welsh Otherworld, the Un-world that lies on the far side of ordinary life. "
 "Its name may grow from the old Celtic word dwfn, deep. "
 "A Gaulish inscription from Collias invokes underworld spirits with the word andounnabo, set at a ritual spring. "
 "The Welsh, like the Irish, offered several places for the Otherworld. Annwn means abyss. "
 "The Welsh saw it as a castle by the sea, called Caer Siddi. "
 "They also saw it as a court of intoxication, called Caer Feddwid, and as a palace of glass, called Caer Wydyr. "
 "Like Tir na nOg, that Irish island of the blessed, Annwn was a land of sweetness and charm. "
 "Its people knew neither age nor suffering. A magic cauldron fed each of them their fill. "
 "An unfailing well quenched their thirst. "
 "Two kings ruled Annwn, Arawn and Hafgan, locked in endless war. "
 "The legends tell more of Arawn. "
 "In the Mabinogi's first branch, the prince Pwyll met Arawn while hunting, and the two traded shapes for a year. "
 "That season bound the royal house of Dyfed to the powers of Annwfn. "
 "In the early poem Preiddiau Annwfn, which tells of the spoils of Annwn, Arthur and his men stormed stronghold after stronghold in that other realm.",
 [("Annwn", "Place"), ("Annwyn", "Place"), ("Annwfn", "Place"), ("Caer Siddi", "Place"),
  ("Caer Feddwid", "Place"), ("Caer Wydyr", "Place"), ("Tir na nOg", "Place"),
  ("Arawn", "Person"), ("Hafgan", "Person"), ("Pwyll", "Person"), ("Arthur", "Person"),
  ("Preiddiau Annwfn", "Title"), ("dwfn", "Concept"), ("andounnabo", "Concept")],
 [("Annwn", "a Welsh Otherworld known as abyss, shown as castle, court, and palace"),
  ("Caer Siddi", "a seagirt castle form of Annwn"),
  ("Caer Feddwid", "a court of intoxication form of Annwn"),
  ("Caer Wydyr", "a palace of glass form of Annwn"),
  ("Arawn", "one of two warring kings of Annwn"),
  ("Hafgan", "one of two warring kings of Annwn"),
  ("Annwn", "the Un-world, whose name may grow from the Celtic word dwfn, deep"),
  ("Pwyll", "traded shapes with Arawn for a year in the first branch"),
  ("Arthur", "stormed its strongholds in the poem Preiddiau Annwfn")],
 {"objective": "Record Annwn, the Welsh Otherworld, from its name to its kings.",
  "key_results": ["The name may grow from Celtic dwfn, deep, and a Gaulish form marks underworld spirits.",
                  "Its three forms are a seagirt castle, a court of intoxication, and a palace of glass.",
                  "Two kings, Arawn and Hafgan, ruled it, and Pwyll traded shapes with Arawn for a year.",
                  "Arthur raided its strongholds in the poem Preiddiau Annwfn."],
  "evidence": "Monaghan 2003, s.v. Annwn; Koch 2006, s.v. 'Annwn / Annwfn'."})

# ---------- 4. Arawn ----------
blend("Arawn.json", "Koch 2006, s.v. 'Arawn'.",
 "Arawn is a Welsh god. He is the lord of Annwn, the Welsh Otherworld. "
 "His world is a typical Celtic Otherworld. It is beautiful and unchanging, without pain, death, or disease. "
 "Its residents pass their time in merrymaking and games. "
 "Koch calls him the king of Annwfn in the Mabinogi's opening branch. "
 "Arawn owned a magical cauldron. It suggests a parallel with the Dagda, the Irish father god. "
 "Arawn had magical pigs, another motif of the Dagda. He handed the pigs to the mortal king Pryderi as a gift. "
 "Gwydion the bard stole them, and for that theft he was caught and held in Annwn. "
 "Three magical animals of Arawn were stolen by the obscure god Amaethon. "
 "The motif holds that domesticated animals once belonged to the gods. "
 "People had to bring them to this world by force or trickery. "
 "In the Mabinogi tale of Pwyll, Arawn exchanged identities with the mortal king for a year. "
 "Pwyll spent his year in the Otherworld and killed Arawn's enemy and rival, Hafgan. "
 "Koch adds a rule to that combat. A single blow could kill Hafgan, but a second blow gave him back his strength. "
 "So the victor had to strike once and stop. Pwyll learned the rule and ended the long war in one stroke. "
 "In return Arawn built a model kingdom in Dyfed, known for warmth, kindness, and a clear sense of justice. "
 "An early poem about the spoils of Annwfn still remembers the king and his realm.",
 [("Arawn", "Person"), ("Annwn", "Place"), ("cauldron", "Artifact"), ("Dagda", "Person"),
  ("pigs", "Being"), ("Pryderi", "Person"), ("Gwydion", "Person"), ("Amaethon", "Person"),
  ("Pwyll", "Person"), ("Hafgan", "Person"), ("Preiddiau Annwfn", "Title")],
 [("Arawn", "lord of the Welsh Otherworld, Annwn, owner of a magical cauldron"),
  ("cauldron", "a magical vessel owned by Arawn, parallel to the Dagda's"),
  ("Hafgan", "a single blow could kill him, but a second restored his strength"),
  ("Arawn", "made Dyfed a model kingdom known for kindness and justice"),
  ("Arawn", "fought Hafgan until Pwyll ended the war in one stroke")],
 {"objective": "Record Arawn, the Welsh lord of Annwn.",
  "key_results": ["He rules the Otherworld and owns the cauldron and pigs that parallel the Dagda.",
                  "He traded shapes with Pwyll for a year in the first branch.",
                  "Pwyll killed Hafgan with a single blow, since a second blow restored his strength.",
                  "Arawn answered with a model kingdom known for kindness and justice."],
  "evidence": "Monaghan 2003, s.v. Arawn; Koch 2006, s.v. 'Arawn'."})

# ---------- 5. Arberth ----------
blend("Arberth.json", "Koch 2006, s.v. 'Arberth'.",
 "Arberth is a Welsh mythological site. "
 "The name belongs to a magical fairy mound within the realm of Pwyll. "
 "Koch identifies it with Narberth in Pembrokeshire and calls it the royal seat of the old kingdom of Dyfed. "
 "People went there to see visions. The mound itself bears the name Gorsedd Arberth, and strange events gather around it. "
 "It is the scene of much of the Mabinogi, standing at the heart of the first and fourth branches. "
 "In Pwyll's tale, the mysterious horsewoman Rhiannon appears on the mound. "
 "No rider could catch her, though her horse seemed only to walk. "
 "In the tale of Manawydan, a mist descends on the mound and takes the people of Dyfed away.",
 [("Arberth", "Place"), ("Pwyll", "Person"), ("Narberth", "Place"), ("Dyfed", "Place"),
  ("Rhiannon", "Person"), ("Manawydan", "Person"), ("Gorsedd Arberth", "Place")],
 [("Arberth", "a magical fairy mound where people see visions"),
  ("Gorsedd Arberth", "the mound near the court, prone to strange events"),
  ("Arberth", "the royal seat of the old kingdom of Dyfed"),
  ("Rhiannon", "first appeared on the mound, riding a horse that could not be caught"),
  ("Manawydan", "a mist over the mound swept away the people of Dyfed")],
 {"objective": "Record Arberth, the fairy mound at the heart of the Mabinogi.",
  "key_results": ["Koch identifies the site with Narberth in Pembrokeshire.",
                  "The mound Gorsedd Arberth drew visions and strange events.",
                  "Rhiannon first appeared there, and a mist in the fourth branch swallowed Dyfed."],
  "evidence": "Monaghan 2003, s.v. Arberth; Koch 2006, s.v. 'Arberth'."})

# ---------- 6. Armorica ----------
blend("Armorica.json", "Koch 2006, s.v. 'Armorica'.",
 "Armorica is an ancient place-name. It names the coast of Gaul facing the Atlantic. "
 "The name means country facing the sea. "
 "In Roman usage the Tractus Armoricanus ran from the mouth of the Seine to the Loire. "
 "It covered the land lying west of the Belgae and reaching north of the Aquitani, the ground that later Normandy and Brittany share. "
 "Julius Caesar gives the earliest surviving examples of the name. "
 "He writes of the civitates Armoricae, the tribal states by the ocean. "
 "His list names the Curiosolites, the Redones, the Ambibarii, the Caletes, the Osismii, the Veneti, the Lemovices, and the Venelli. "
 "Caesar also records the Veneti as the strongest people of the coast and tells how Rome broke their sea power. "
 "Their name lives on in Breton Gwened, the town the French call Vannes. "
 "Modern works often use Armorica for the land later called Brittany. "
 "Koch also records the older spelling Aremorica.",
 [("Armorica", "Place"), ("Brittany", "Place"), ("Gaul", "Place"), ("Aremorica", "Place"),
  ("Caesar", "Person"), ("Seine", "Place"), ("Loire", "Place"), ("Veneti", "Group"),
  ("Belgae", "Group")],
 [("Armorica", "a coast of Gaul facing the Atlantic"),
  ("Brittany", "the later land assigned this name"),
  ("Armorica", "the Tractus Armoricanus ran from the Seine to the Loire"),
  ("Caesar", "listed its peoples as the civitates Armoricae"),
  ("Veneti", "the strongest coastal people, remembered in Breton Gwened")],
 {"objective": "Record Armorica, the old name of a Gaulish coast.",
  "key_results": ["The Tractus Armoricanus ran from the mouth of the Seine to the Loire.",
                  "Caesar named its peoples the civitates Armoricae and lists eight of them.",
                  "The Veneti were its strongest people, and their name survives in Breton Gwened.",
                  "Modern works use Armorica for the land later called Brittany."],
  "evidence": "Monaghan 2003, s.v. Armorica; Koch 2006, s.v. 'Armorica'."})

# ---------- 7. banshee ----------
blend("banshee.json", "Koch 2006, s.v. 'bean sí / banshee'.",
 "The banshee is an Irish spirit of death. The name means the woman of the fairy people. "
 "Long ago she ranked as a goddess of the land and of its sovereignty. "
 "Koch traces her to the territorial goddesses of early Irish literature, who guarded their rulers and could also appear as war goddesses under the name Badb. "
 "When her glory faded, her role narrowed to a single task. She now warns that death draws near. "
 "She favors the old families of Ireland. Their names often begin with O or Mac. "
 "She appears as a hag or as a young woman. She is most often an outdoor being in a white cloak, with her head bare. "
 "Red hair and white or green robes mark her as other. "
 "She wails, and she combs her hair with a comb of gold. "
 "In the east of Ireland she combs that hair, and in Galway she washes a garment in a stream. "
 "That deed matches the bean-nighe of Gaelic Scotland and the kannerezed noz of Brittany. "
 "An older layer of the same image shows the war goddess badhbh washing the clothes of men fated to fall in battle. "
 "A Galway tale places such a washer by the stream on the eve of Aughrim in 1691. "
 "The sovereignty goddess could also foretell a king's death. "
 "Aoibheall of Craglea foretold the fall of Brian Bóruma at Clontarf in 1014. "
 "In the eighth-century Táin Bó Fraích, the cries of Otherworld women, led by the hero's own mother Bé Find, sang Fraoch toward his end. "
 "Áine of north Munster appears as a weeping banshee and the ancestress of the FitzGeralds. "
 "She warns of death from any cause. The Washer at the Ford warns only of a death in battle. "
 "A banshee can follow her own people when they travel. "
 "The banshee of the O'Gradys family went with them to Canada.",
 [("banshee", "Being"), ("Washer at the Ford", "Being"), ("Aine", "Deity"),
  ("O'Gradys", "Group"), ("Canada", "Place"), ("Aoibheall", "Being"),
  ("Brian Bóruma", "Person"), ("bean-nighe", "Being"), ("Bé Find", "Being"),
  ("Badb", "Deity"), ("Táin Bó Fraích", "Title")],
 [("banshee", "Irish being whose name means woman of the fairy people"),
  ("banshee", "once a goddess of the land or of sovereignty"),
  ("banshee", "became a spirit who announced that death drew near"),
  ("banshee", "linked to goddesses such as Aine"),
  ("O'Gradys", "banshee followed the family to Canada"),
  ("banshee", "an outdoor being in a white cloak with her head bare"),
  ("bean-nighe", "the Scottish counterpart who washes clothes at a stream"),
  ("badhbh", "the war goddess who washed the clothes of men fated to fall"),
  ("Aoibheall", "foretold the death of Brian Bóruma at Clontarf in 1014"),
  ("Bé Find", "mother of Fraoch, whose cries sang her son toward his death")],
 {"objective": "Record the banshee as the fallen sovereignty goddess who warns of death.",
  "key_results": ["Her name means the woman of the fairy people, and she once held the role of a land goddess.",
                  "She wears a white cloak, combs her hair in the east, and washes clothes in Galway.",
                  "Her washing parallels the bean-nighe of Scotland and the kannerezed noz of Brittany.",
                  "Aoibheall foretold Brian Bóruma's fall, and Bé Find sang Fraoch toward his death."],
  "evidence": "Monaghan 2003, s.v. banshee; Koch 2006, s.v. 'bean sí / banshee'."})

# ---------- 8. Balor ----------
blend("Balor.json", "Koch 2006, s.v. 'Balor'.",
 "Balor is an Irish god. He is also called Balar, Bolar, and Balor of the Evil Eye. "
 "He reigned as king of the Fomorians, the monstrous race who held Ireland before the first invaders. "
 "His daughter was the fair Eithne. A prophecy warned that a son born to Eithne would kill his grandfather. "
 "Balor locked Eithne in a tower so that no man might reach her. "
 "He hoped that this would spare his own life. "
 "Koch draws his fullest early picture from the battle tale Cath Maige Tuired. "
 "That tale was set down in the ninth or tenth century. "
 "There Balor leads the Fomoiri against his grandson Lug and the Tuath Dé. "
 "Balor's greed undid his plan. He stole the magical cow Glas Ghaibhleann from a smith. "
 "Lugh struck him down in that battle with a slingshot or a spear made by the smith god Goibniu. "
 "Lugh cut off Balor's head. Even in death, Balor's remaining eye could split boulders. "
 "The eye was his ruin from the start. Koch says Balor gained it as a boy when he watched the spells of his father's druids. "
 "Its heavy lid took four men to lift, and its gaze struck soldiers of the Tuath Dé helpless. "
 "When Lug's stone flew through it, the fatal power turned back on the Fomoiri. "
 "Monaghan sets the eye as a third one in the middle of Balor's forehead. It spat flames and destruction. "
 "Cethlion, his consort, also had poisonous powers, and her poison killed the god Dagda. "
 "In later folk-tales Balor loses his role as a war leader and becomes a monstrous villain. "
 "Some scholars read him as a sun god, and others as the quarrel of the old year with the new. "
 "The tale ties him to the Hebrides, and modern storytellers place his fortress on Tory Island. "
 "He is linked to Mizen Head in County Cork and to Land's End in Wales.",
 [("Balor", "Deity"), ("Eithne", "Person"), ("Lugh", "Deity"), ("Goibniu", "Deity"),
  ("Cethlion", "Being"), ("Dagda", "Deity"), ("Fomorians", "Group"),
  ("Glas Ghaibhleann", "Animal"), ("Mag Tuired", "Place"), ("Mizen Head", "Place"),
  ("Tuath Dé", "Group"), ("Cath Maige Tuired", "Title"), ("Tory Island", "Place")],
 [("Balor", "king of the Fomorians"),
  ("Balor", "father of Eithne"),
  ("Balor", "stole the magical cow Glas Ghaibhleann from a smith"),
  ("Balor", "evil eye could split boulders and had to be lifted by four men"),
  ("Cethlion", "consort whose poison killed the god Dagda"),
  ("Balor", "associated with Mizen Head and Land's End"),
  ("Balor", "gained the evil eye as a boy by watching his father's druids"),
  ("Balor", "leads the Fomoiri in the second battle of Mag Tuired"),
  ("Tuath Dé", "his basilisk gaze struck their soldiers helpless"),
  ("Balor", "read as a sun god or as the strife between the old year and the new")],
 {"objective": "Record Balor, the one-eyed Fomorian king felled by his grandson.",
  "key_results": ["The second battle of Mag Tuired gives his fullest early picture as leader of the Fomoiri.",
                  "He gained the evil eye as a boy by watching the magic of his father's druids.",
                  "Four men lifted its lid, and Lug's slingshot turned its fatal power on the Fomoiri.",
                  "Later tales make him a villain, read as a sun god or the strife of the old year and the new."],
  "evidence": "Monaghan 2003, s.v. Balor; Koch 2006, s.v. 'Balor'."})

# ---------- 9. Banba ----------
blend("Banba.json", "Koch 2006, s.v. 'Banba'.",
 "Banba is an Irish goddess. She is one of three earth goddesses, with Fódla and Ériu, who met the Milesians. "
 "The medieval lore of women and the Book of Invasions group the three as daughters of Fiachra or of Ernmas. "
 "The Milesians were the mythological invaders seen as the first Irish Celts. "
 "The Book of Invasions says Banba met them at Slieve Mis in County Kerry. "
 "Some sources place her on the plain from which the hill of Tara rises. "
 "Banba offered the Milesians happiness and wealth if the land bore her name. "
 "The Milesians instead gave precedence to Ériu, who made the same promise from the hill of Uisneach. "
 "Tradition names three gods or heroes as husbands of the three goddesses. "
 "Banba's husband was Mac Cuill, whose name means son of Hazel. "
 "People said the salmon of wisdom fed on those hazel nuts. "
 "Koch calls Mac Cuill a king of the Tuath Dé and a grandson of the Dagda. "
 "Geoffrey Keating, drawing on a lost Old Irish manuscript, tells another arrival tale. "
 "Banba and her sisters came as daughters of Cain, fifty women and three men among them. Every one of that company died in a plague. "
 "The name may join ban, woman, with ba, an old word for death, for gain, or for cow. "
 "That last sense echoes Bóand, the river Boyne, whose name means white as a cow. "
 "The pig is an emblem of Banba, and her name resembles the Irish word for piglet, banb. "
 "Banba told the Milesians that she had lived in Ireland before the biblical Noah. "
 "Some versions say the newcomers drove her out by singing spells against her. "
 "Her name survives today as a poetic name for Ireland.",
 [("Banba", "Deity"), ("Fódla", "Deity"), ("Ériu", "Deity"), ("Milesians", "Group"),
  ("Mac Cuill", "Person"), ("Slieve Mis", "Place"), ("Tara", "Place"),
  ("Uisneach", "Place"), ("Book of Invasions", "Title"), ("banshenchas", "Title"),
  ("Keating", "Person"), ("Dagda", "Deity"), ("Cín Dromma Snechtai", "Title")],
 [("Banba", "one of the three earth goddesses, with Fódla and Ériu"),
  ("Banba", "met the Milesians at Slieve Mis in County Kerry"),
  ("Banba", "promised happiness and wealth if the land bore her name"),
  ("Mac Cuill", "husband of Banba, his name meaning son of Hazel"),
  ("Banba", "name remains a poetic term for Ireland"),
  ("Banba", "grouped with her sisters as daughters of Fiachra or of Ernmas"),
  ("Mac Cuill", "a king of the Tuath Dé and a grandson of the Dagda"),
  ("Keating", "tells of an arrival under Cain that ended in a plague")],
 {"objective": "Record Banba, one of the three goddesses who personify Ireland.",
  "key_results": ["The lore of women and the Book of Invasions call her a daughter of Fiachra or of Ernmas.",
                  "She met the Milesians and promised happiness and wealth if the land bore her name.",
                  "Her husband Mac Cuill was a king of the Tuath Dé and a grandson of the Dagda.",
                  "Her name may join woman with death, gain, or cow, as in Bóand."],
  "evidence": "Monaghan 2003, s.v. Banba; Koch 2006, s.v. 'Banba'."})

# ---------- 10. Bath ----------
blend("Bath.json", "Koch 2006, s.v. 'Bath'.",
 "Bath is a British mythological site. "
 "It lies in the southwest of England, where the river Avon cuts through the limestone of the Cotswolds. "
 "Three hot springs rise within a short walk of one another. "
 "For at least two thousand years the waters have drawn the sick. "
 "Some think the spring was used before the Celts. "
 "Coins from the late Iron Age and the remains of a causeway have come to light beneath the later King's Bath. "
 "The records that survive date from Celtic times. "
 "The local goddess was Sulis, and the Romans named the town Aquae Sulis, the waters of Sulis. "
 "The Romans folded Sul into their goddess Minerva. "
 "They built colonnaded temples and interior bathing rooms. "
 "Koch dates the first sanctuary complex to the Flavian age, between ad 69 and 138. "
 "It held a Corinthian temple of four columns, a paved court, an altar, and a spring left open to the sky. "
 "A fort on the Fosse Way watched the river crossing in the first years of the conquest. "
 "After the army moved on, the town grew as a civil settlement around the crossing. "
 "These buildings stand today. "
 "Celtic custom showed itself at Bath. People threw coins into the water. "
 "They also wrote curses on sheets of lead. "
 "Excavators have found 16,000 coins at the site. They have found more than 50 cursing tablets as well.",
 [("Bath", "Place"), ("Sul", "Deity"), ("Sulis", "Deity"), ("Minerva", "Deity"),
  ("Aquae Sulis", "Place"), ("Celtic", "Group"), ("Avon", "Place")],
 [("Bath", "British mythological site with healing hot springs"),
  ("Bath", "Roman name Aquae Sulis"),
  ("Sul", "Celtic goddess of the site, merged with Minerva"),
  ("Bath", "site of the Celtic coin-throwing custom"),
  ("Bath", "source of 16,000 coins and more than 50 cursing tablets"),
  ("Avon", "the river whose bend frames the site in the Cotswolds"),
  ("Sulis", "the fuller name of the spring goddess, waters of Sulis")],
 {"objective": "Record Bath as a healing site of the goddess Sulis.",
  "key_results": ["Three hot springs rise close together where the Avon cuts the Cotswolds.",
                  "The Romans named the town Aquae Sulis and joined Sulis to Minerva.",
                  "The first sanctuary of the Flavian age held a Corinthian temple, a court, and an altar.",
                  "Iron Age coins and a causeway lie beneath the later King's Bath."],
  "evidence": "Monaghan 2003, s.v. Bath; Koch 2006, s.v. 'Bath'."})

# ---------- batch-A sources gains ----------
M["Badb.json"] = {"add_sources": ["Koch 2006, s.v. 'Bodb'."]}
M["boar.json"] = {"add_sources": ["Koch 2006, s.v. 'boar'."]}
M["aisling.json"] = {"add_sources": ["Koch 2006, s.v. 'Aisling'."]}

# final lint pass + dump
for fn, p in M.items():
    if "text" in p:
        lint(p["text"], fn)
        assert 2 <= len(p["okr"]["key_results"]) <= 4, fn + ": KR count"
        assert p["okr"]["objective"] and p["okr"]["evidence"], fn + ": okr fields"

json.dump(M, open(f"{REPO}/rewrite/patch/t81_koch_b.json", "w"), indent=1, ensure_ascii=False)
print("BUILT OK:", len(M), "entries")
for fn, p in M.items():
    kind = "blend" if "text" in p else "src-gain"
    extra = f" text={len(p.get('text',''))}c" if "text" in p else ""
    print(f"  {fn:16s} {kind}{extra}")
