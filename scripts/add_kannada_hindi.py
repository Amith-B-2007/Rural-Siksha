"""
Add Kannada and Hindi resources and quizzes for all grades
Content uses romanization with English explanations for PDF compatibility
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fpdf import FPDF
from app import create_app
from extensions import db
from backend.models import User, Resource, Quiz, QuizQuestion


def clean(text):
    """Sanitize text - keeps ASCII characters"""
    replacements = {
        '×': 'x', '÷': '/', '−': '-', '°': ' deg',
        '–': '-', '—': '-', '"': '"', '"': '"',
        ''': "'", ''': "'", '…': '...', '•': '*',
        '₹': 'Rs.', '→': '->', '←': '<-',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    result = []
    for c in text:
        if ord(c) < 128:
            result.append(c)
        else:
            result.append(' ')
    return ''.join(result)


class PDF(FPDF):
    def __init__(self, title='', subject='', grade=0):
        super().__init__()
        self.doc_title = clean(title)[:80]
        self.doc_subject = clean(subject)
        self.doc_grade = grade
        self.set_margins(15, 15, 15)
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        self.set_fill_color(79, 70, 229)
        self.rect(0, 0, 210, 8, 'F')
        self.set_y(12)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(79, 70, 229)
        self.cell(0, 5, 'Rural Siksha - NCERT Learning', new_x='LMARGIN', new_y='NEXT', align='L')
        self.set_y(18)
        self.set_font('Helvetica', 'B', 13)
        self.set_text_color(15, 23, 42)
        self.cell(0, 7, self.doc_title, new_x='LMARGIN', new_y='NEXT', align='L')
        if self.doc_subject:
            self.set_font('Helvetica', '', 9)
            self.set_text_color(100, 116, 139)
            self.cell(0, 4, f'Subject: {self.doc_subject}  |  Grade: {self.doc_grade}', new_x='LMARGIN', new_y='NEXT', align='L')
        self.set_draw_color(229, 231, 235)
        self.line(10, 33, 200, 33)
        self.set_y(38)

    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(148, 163, 184)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def render(self, content):
        content = clean(content)
        for raw in content.split('\n'):
            line = raw.rstrip()
            if not line.strip():
                self.ln(2)
                continue
            stripped = line.strip()
            is_heading = stripped.isupper() and len(stripped) <= 70 and '=' not in stripped
            is_sub = stripped.endswith(':') and len(stripped) <= 50

            try:
                if is_heading:
                    self.ln(2)
                    self.set_font('Helvetica', 'B', 12)
                    self.set_text_color(79, 70, 229)
                    self.multi_cell(0, 6, stripped)
                    self.ln(1)
                elif is_sub:
                    self.set_font('Helvetica', 'B', 10)
                    self.set_text_color(30, 41, 59)
                    self.multi_cell(0, 5, stripped)
                else:
                    self.set_font('Helvetica', '', 10)
                    self.set_text_color(15, 23, 42)
                    self.multi_cell(0, 5, stripped)
            except Exception:
                try:
                    safe = ''.join(c for c in stripped if c.isascii() and ord(c) >= 32)[:500]
                    if safe:
                        self.set_font('Helvetica', '', 10)
                        self.set_text_color(15, 23, 42)
                        self.multi_cell(0, 5, safe)
                except:
                    pass


# ==================== KANNADA RESOURCES ====================
KANNADA_RESOURCES = [
    {'g': 1, 't': 'Kannada Aksharamale (Alphabet)',
     'd': 'Learn Kannada vowels and consonants',
     'c': '''KANNADA AKSHARAMALE (ALPHABET)

Kannada has SVARAGALU (Vowels) and VYANJANAGALU (Consonants).

SVARAGALU (VOWELS) - 13 LETTERS:
1. A (a) - like in "father"
2. Aa - long a sound
3. I (i) - like in "ink"
4. Ee - long i sound
5. U (u) - like in "put"
6. Oo - long u sound
7. Ru - special sound
8. E (e) - like in "egg"
9. Ai - like in "aisle"
10. O (o) - like in "old"
11. Au - like in "out"
12. Am - nasal sound
13. Aha - aspirated sound

VYANJANAGALU (CONSONANTS) - 34 LETTERS:

K-Group (5 letters):
Ka, Kha, Ga, Gha, Nga

Cha-Group (5 letters):
Cha, Chha, Ja, Jha, Nya

Ta-Group (5 letters):
Ta, Tha, Da, Dha, Na

Tha-Group (5 letters):
Tha, Thha, Dha, Dhha, Na

Pa-Group (5 letters):
Pa, Pha, Ba, Bha, Ma

Other 9 letters:
Ya, Ra, La, Va, Sha, Shha, Sa, Ha, La (special)

WORDS FOR PRACTICE:

Simple Kannada Words (Romanized):
- AMMA (Mother)
- APPA (Father)
- ANNA (Elder Brother)
- AKKA (Elder Sister)
- THAMMA (Younger Brother)
- THANGI (Younger Sister)
- MANE (House)
- ANNA (Rice)
- NEERU (Water)
- HALU (Milk)
- HUVU (Flower)
- MARA (Tree)

Animals (Praani):
- HASU (Cow)
- NAYI (Dog)
- BEKKU (Cat)
- KUDURE (Horse)
- HAKKI (Bird)
- MEENU (Fish)

Numbers (Sankhye) 1 to 10:
1 - ONDU
2 - ERADU
3 - MOORU
4 - NAALKU
5 - AIDU
6 - AARU
7 - ELU
8 - ENTU
9 - OMBHATTU
10 - HATTU

Colors (Banna):
- KEMPU (Red)
- HALADI (Yellow)
- NEELI (Blue)
- HASIRU (Green)
- BILI (White)
- KAPPU (Black)

Days of Week (Vaaragalu):
- BHANUVARA (Sunday)
- SOMAVARA (Monday)
- MANGALAVARA (Tuesday)
- BUDHAVARA (Wednesday)
- GURUVARA (Thursday)
- SHUKRAVARA (Friday)
- SHANIVARA (Saturday)

Common Phrases:
- NAMASKARA (Hello/Greetings)
- DHANYAVADAGALU (Thank you)
- KSHAMISI (Sorry)
- NEEVU HEGIDDEERA? (How are you?)
- NAANU CHENNAGIDDENE (I am fine)

Practice writing:
Practice writing Kannada letters daily.
Read Kannada words aloud.
Kannada is the official language of Karnataka.
It is one of the oldest languages of India.'''},

    {'g': 2, 't': 'Kannada Padagalu (Words)',
     'd': 'Learn common Kannada words',
     'c': '''KANNADA PADAGALU (WORDS)

In this lesson, we learn many useful Kannada words.

FAMILY MEMBERS (Mane Sadasyaru):
- TANDE / APPA (Father)
- TAYI / AMMA (Mother)
- ANNA (Elder Brother)
- THAMMA (Younger Brother)
- AKKA (Elder Sister)
- THANGI (Younger Sister)
- AJJA (Grandfather)
- AJJI (Grandmother)
- CHIKKAPPA (Uncle - father's younger brother)
- DODDAMMA (Aunt - mother's elder sister)

BODY PARTS (Dehadu Bhagagalu):
- TALE (Head)
- KANNU (Eye)
- KIVI (Ear)
- MOOGU (Nose)
- BAYI (Mouth)
- KAI (Hand)
- KAALU (Leg)
- BERALU (Finger)
- KUDALU (Hair)
- HALLU (Teeth)

NATURE (Nisarga):
- SOORYA (Sun)
- CHANDRA (Moon)
- NAKSHATRA (Star)
- AAKASHA (Sky)
- MEGHA (Cloud)
- MALE (Rain)
- BHOOMI (Earth)
- BETTA (Mountain)
- NADI (River)
- KADAL (Sea)

FOOD (Aahara):
- ANNA (Rice)
- ROTTI (Bread/Roti)
- BELE (Lentils)
- TARAKARI (Vegetables)
- HANNUGALU (Fruits)
- HALU (Milk)
- MOSARU (Curd)
- THUPPA (Ghee)
- ENNE (Oil)
- UPPU (Salt)
- SAKKARE (Sugar)

FRUITS (Hannugalu):
- MAVU (Mango)
- BAALE (Banana)
- DAALIMBE (Pomegranate)
- DRAKSHI (Grapes)
- SEBU (Apple)
- KITTHALE (Orange)
- TENGU (Coconut)
- PAPAYI (Papaya)

VEGETABLES (Tarakari):
- AALU (Potato)
- ULLI (Onion)
- TAMATE (Tomato)
- KESARU (Carrot)
- BAALAKAYI (Plantain)
- BENDEKAYI (Ladyfinger)
- KOSU (Cabbage)
- HEERAKAYI (Cucumber)

HOUSE (Mane):
- BAAGILU (Door)
- KIDAKI (Window)
- HASIGE (Bed)
- MEJU (Table)
- KURCHI (Chair)
- ADIGEMANE (Kitchen)
- KOTHADI (Room)
- HASE (Floor)

SCHOOL (Shaale):
- PUSTAKA (Book)
- PENNU / PENSILU (Pen/Pencil)
- BAYIKE (School bag)
- HALAGE (Blackboard)
- UPADHYAYARU (Teacher)
- VIDYARTHIGALU (Students)
- TARGATI (Class)

ACTIONS (Kelasa):
- HOGU (Go)
- BAA (Come)
- KOODU (Sit)
- ELU (Stand up)
- TINNU (Eat)
- KUDI (Drink)
- ODI (Read/Run)
- BARE (Write)
- NODU (See/Look)
- KEYALU (Listen)

DIRECTIONS:
- MELE (Up)
- KELAGE (Down)
- ELU (Left)
- BALAKADE (Right)
- MUNDE (Front)
- HINDE (Back)

TIME (Samaya):
- BELAGGE (Morning)
- MADHYAANA (Afternoon)
- SAANJE (Evening)
- RAATRI (Night)
- INDU (Today)
- NALE (Tomorrow)
- NINNE (Yesterday)

QUESTIONS:
- ENU? (What?)
- ELLI? (Where?)
- YAVAGA? (When?)
- YAARU? (Who?)
- YAAKE? (Why?)
- HEGE? (How?)
- ESTU? (How much?)

Practice these words daily.
Try making sentences with them.'''},

    {'g': 3, 't': 'Kannada Vyakarana (Basic Grammar)',
     'd': 'Introduction to Kannada grammar',
     'c': '''KANNADA VYAKARANA (BASIC GRAMMAR)

Kannada grammar is called VYAKARANA.

PARTS OF SPEECH:

1. NAAMA PADA (NOUN)
Words that name things, people, places.
Examples:
- HUDUGA (Boy)
- HUDUGI (Girl)
- MANE (House)
- SHAALE (School)
- BENGALURU (Bangalore - place)
- RAAMA (Ram - person)

Types:
- VYAKTI VAACHAKA (Proper noun): Specific names
  - RAVI, SITA, MYSORE
- JATI VAACHAKA (Common noun): General names
  - PRANI (animal), MANUSHYA (human)

2. SARVANAAMA (PRONOUN)
Words used in place of nouns.
- NAANU (I)
- NEENU (You - informal)
- NEEVU (You - respectful/plural)
- AVANU (He)
- AVALU (She)
- ADU (It)
- NAVU (We)
- AVARU (They)

3. KRIYA PADA (VERB)
Action words.
- HOGU (go)
- BAA (come)
- TINNU (eat)
- ODU (run/read)
- BARE (write)
- HELU (tell)
- KAANU (see)

4. VISHESHANA (ADJECTIVE)
Describing words.
- DODDA (big)
- CHIKKA (small)
- OLLE (good)
- KEDU (bad)
- KEMPU (red)
- HOSA (new)
- HALE (old)

5. KRIYA VISHESHANA (ADVERB)
Describes how action is done.
- BEGA (fast)
- NIDHANAVAGI (slowly)
- CHENNAGI (well)
- SARIYAGI (correctly)
- INDU (today)

VACHANA (NUMBER):

1. EKAVACHANA (Singular)
- HUDUGA (a boy)
- HUDUGI (a girl)
- HANNU (a fruit)

2. BAHUVACHANA (Plural)
- HUDUGARU (boys)
- HUDUGIYARU (girls)
- HANNUGALU (fruits)

Rule: Generally add -GALU/RU to make plural.

LINGA (GENDER):

1. PUMLINGA (Masculine):
- APPA (father)
- ANNA (brother)
- AVANU (he)

2. STRILINGA (Feminine):
- AMMA (mother)
- AKKA (sister)
- AVALU (she)

3. NAPUMSAKA LINGA (Neuter):
- MANE (house)
- MARA (tree)
- ADU (it)

VIBHAKTI (CASE):

Vibhakti shows relation between words.
There are 7 vibhaktis in Kannada.

Example with word HUDUGA (boy):

1. PRATHAMA: HUDUGA (boy)
   The boy goes.

2. DVITIYA: HUDUGANNU (the boy)
   I see the boy.

3. TRITIYA: HUDUGANINDA (by the boy)
   Done by the boy.

4. CHATURTHI: HUDUGANIGE (to the boy)
   Give to the boy.

5. PANCHAMI: HUDUGANINDA (from the boy)
   Take from the boy.

6. SHASHTHI: HUDUGANA (boy's)
   Boy's book.

7. SAPTAMI: HUDUGANALLI (in the boy)
   Trust in the boy.

KAALA (TENSE):

1. BHOOTHAKAALA (Past Tense)
- HOGIDA (went)
- TINDA (ate)
- BANDA (came)

2. VARTHAMANAKAALA (Present Tense)
- HOGUTTAANE (goes/is going)
- TINNUTTAANE (eats)
- BARUTTAANE (comes)

3. BHAVISHYATKAALA (Future Tense)
- HOGUTTAANE (will go)
- TINNUTTAANE (will eat)
- BARUTTAANE (will come)

SIMPLE SENTENCES:

Examples:
1. NAANU SHAALEGE HOGUTTENE
   (I go to school.)

2. AMMA ANNA MADUTTAALE
   (Mother makes rice.)

3. APPA KELASA MADUTTAARE
   (Father works.)

4. NAVU PUSTAKA ODUTTEVE
   (We read books.)

5. AVALU CHENNAGI HADUTTAALE
   (She sings well.)

Practice:
Make 5 sentences using Kannada words you know!'''},

    {'g': 4, 't': 'Kannada Vakyagalu (Sentences)',
     'd': 'Building sentences in Kannada',
     'c': '''KANNADA VAKYAGALU (SENTENCES)

VAKYA = SENTENCE

A complete sentence has SUBJECT and PREDICATE.

BASIC STRUCTURE:
Subject + Object + Verb

Examples:
1. NAANU + ANNA + TINDIDDENE
   (I + food + ate)
   "I ate food"

2. AMMA + MANE + STARANGI MADIDDAARE
   (Mother + house + cleaned)
   "Mother cleaned the house"

TYPES OF SENTENCES:

1. DESCRIPTIVE SENTENCES:
- IDU PUSTAKA (This is a book)
- ADU MARA (That is a tree)
- AAKAASHA NEELI (Sky is blue)
- HUVU SOGASAGIDE (Flower is beautiful)

2. ACTION SENTENCES:
- NAANU OODUTHENE (I read)
- AVALU HADUTHALE (She sings)
- AVARU MANE KATTUTHARE (They build a house)

3. QUESTION SENTENCES:
- NEEVU ELLI HOGUTHIRI? (Where are you going?)
- ENU TINNUTHEERI? (What are you eating?)
- YARU BANDIDARU? (Who came?)
- YAVAGA BARUTHIRA? (When will you come?)

4. NEGATIVE SENTENCES:
- NAANU HOGUVUDILLA (I don't go)
- ADU SARIALLA (That is not correct)
- AVANU INNU BANDILLA (He has not come yet)

5. EXCLAMATORY SENTENCES:
- ESHTU CHENDA! (How beautiful!)
- AAHA, RUCHIKAR! (Wow, tasty!)
- ABBA, BHAYANKARA! (Oh, terrible!)

COMMON SENTENCES IN DAILY LIFE:

GREETINGS:
- NAMASKARA / VANDANEGALU (Greetings)
- SHUBHODAYA (Good morning)
- SHUBHARAATRI (Good night)
- DHANYAVADAGALU (Thank you)
- KSHAMISI (Sorry)

INTRODUCTIONS:
- NAANU [NAME] (I am [name])
- NANNA HESARU [NAME] (My name is [name])
- NAANU [GRADE] NEYA TARAGATI (I am in [grade])
- NAANU [CITY] NALLI VAASA MADUTTENE (I live in [city])

ASKING:
- NAANU NIMAGE SAHAYA MADABEKE? (Should I help you?)
- DAYAVITTU IDANNU KODI (Please give me this)
- NEEVU NANAGE [THING] KODUTHIRA? (Can you give me [thing]?)

AT SCHOOL:
- NANNA SHIKSHAKARU OLLEYAVARU (My teachers are good)
- NAANU CHENNAGI ODUTTENE (I study well)
- NAANU HOMEWORK MUGISIDDENE (I finished my homework)

WITH FAMILY:
- AMMA, NANNA HOMEWORK MUGISIDDENE (Mother, I finished my homework)
- APPA, NEEVU BEGA BANNI (Father, please come soon)
- TANGI, NAVU AAATALL ADONA (Sister, let's play)

WITH FRIENDS:
- NAVU JOTAGE AATA ADONA (Let's play together)
- NEEVU NANNA SNEHITARU (You are my friend)
- NANAGE SAHAYA MADI (Help me please)

VERBS IN DIFFERENT FORMS:

OD- (Read/Run):
- ODIDDENE (I read - past)
- ODUTHENE (I read - present)
- ODUTTENE (I will read - future)
- ODI (read - command)

TIN- (Eat):
- TINDIDDENE (I ate)
- TINNUTHENE (I eat)
- TINNUTTENE (I will eat)
- TINNI (eat - command)

CONNECTING WORDS:

- MATTU (and)
- ADARE (but)
- YAAKENDARE (because)
- HAGADARE (so)
- ADARALLI (in that)
- INDA (from)

PROVERBS (Gade):

1. MADUVA KELASA MADHURA
   (Work done well is sweet)

2. KAALAVE KALEYU
   (Time itself is the teacher)

3. HENNANGE TINNUVUDU MAATU
   (A woman's word is sweet like honey)

4. PRAYATNAVE LAKSHMI
   (Effort is wealth)

5. KOOTU KELASA KEEDU
   (Working together fails work) [actually wrong - means collaborative work fails]

DAILY PRACTICE:
- Read Kannada newspapers
- Listen to Kannada news
- Watch Kannada programs
- Talk to family in Kannada
- Write 5 sentences daily

LITERATURE FAMOUS WRITERS:
- KUVEMPU (Jnanpith Award)
- D.R. BENDRE
- MASTI VENKATESHA IYENGAR
- GOPALAKRISHNA ADIGA
- U.R. ANANTHAMURTHY'''},

    {'g': 5, 't': 'Kannada Reading and Writing',
     'd': 'Reading skills and writing practice',
     'c': '''KANNADA READING AND WRITING

READING (Odu):

How to read Kannada properly:

1. Learn all 49 letters first
2. Practice akshara combinations
3. Start with simple words
4. Read short paragraphs
5. Progress to stories

SIMPLE WORDS PRACTICE:

3-Letter Words:
- ANNA (food)
- HALU (milk)
- MANE (house)
- HOLA (field)
- MARA (tree)
- KAAL (leg)

4-Letter Words:
- AMMA (mother)
- APPA (father)
- AKKA (sister)
- KAALU (leg)
- MELU (top)

5-Letter Words:
- SHAALE (school)
- PUSTAKA (book)
- KELASA (work)

READING A PARAGRAPH:

NANNA SHAALE
(My School)

Nanna shaale tumba chennagide.
Adu doodu doddadu. Adaralli halavu kothadigalu ive.

Nanna upadhyaayaru tumba olleyavaru.
Avaru namage chennagi paath maaduttaare.

Nanna gelayaru tumba olleyavaru.
Navu jotage aata adutteve.

Naanu shaalege prati dina hoguttene.

WRITING (Bareyu):

Practice writing each letter at least 5 times.

How to write good sentences:
1. Start with subject (who/what)
2. Add the action (verb)
3. Mention object (if any)
4. Finish with a period (.)

Examples:
- Naanu padyagaLu odutthene. (I read poems.)
- Avalu hadu hadutthaaLe. (She sings songs.)
- Naavu shaaLege hogutteve. (We go to school.)

SHORT ESSAY: NANNA AMMA (My Mother)

Nanna amma kemma haagu olleyavaLu.
AvaLu namma kuTumbada bel.
Pratidina amma munjaane edu adige maduttaaLe.
Amma namage chennagi shaalega taiyaarisuttaaLe.
Naanu amma jotage tumba prema illuve.

LETTER WRITING:

Informal Letter (To a friend):

Priya snehita Ravi,

Namaskaaraagalu! Naanu chennagiddene.
Neenu hege iddiye? Nanage nee tumba miss aagutta iddi.
Naavu kaadina yatre madiddevu. Tumba sundra prashantava.
Mundeli neene nanage barahaalu. Nimme bhetiyaaguvenu.

Nimma snehita,
Sushma

Formal Letter (To Principal):

Mukhya Adhyaapakara,
ABC Shaale,
Bengaluru

Mahodaaya,

Naanu 5 ne taragatiya vidyarthi.
Nanage nele jvaragunte. Naa shaalege baralare.
Dayavittu naanage 2 dinagaLa rajavanaadayisi.

Tama vinayavasamta,
Ravi
Tara gati 5

POETRY (Padya):

Kannada Padya Example:

CHIKKA HUDUGA NAANU
(I am a small boy)

Chikka huduga naanu
Shaalege hoguvenu
Pustak hidikondu
Paath kaliyuvenu

GRAMMAR IN WRITING:

Vibhakti (Cases):

When writing, use correct case markers:
- to/at: -ge (mannige - to mud)
- from: -inda (mara dinda - from tree)
- of/'s: -ya (Ravi-ya - Ravi's)
- in: -alli (mane-alli - in house)

COMMON ERRORS TO AVOID:

1. Confusing E (a) and E (a long)
2. Wrong gender agreement
3. Wrong vibhakti
4. Missing period or comma

PUNCTUATION:
- Full stop: .
- Comma: ,
- Question mark: ?
- Quotation marks: " "

PRACTICE EXERCISES:

1. Translate to Kannada:
   - I am going to school
   - My name is Rama
   - This is my friend

2. Fill in blanks (in Kannada):
   - Sun: ____
   - Water: ____
   - Sky: ____

3. Write 5 sentences about your family in Kannada.

4. Read a short Kannada story daily.

5. Memorize 5 new Kannada words every week.

FAMOUS KANNADA AUTHORS:
- KUVEMPU - Jnanpith Award winner
- D.R. BENDRE - Padya (Poetry) master
- MASTI VENKATESHA IYENGAR
- GOPALAKRISHNA ADIGA
- U.R. ANANTHAMURTHY

Reading their works improves Kannada skills!'''},

    # Higher grades - briefer but more advanced
    {'g': 6, 't': 'Kannada Vyakarana Advanced',
     'd': 'Advanced grammar - sandhi, samasa, alankaara',
     'c': '''KANNADA VYAKARANA ADVANCED

SANDHI (JOINING WORDS):

When two words combine, they undergo changes.

Types of Sandhi:

1. LOPA SANDHI: One letter is lost
   Example: Mara + olage = Maranolage

2. AAGAMA SANDHI: A letter is added
   Example: Mara + ondu = Maravondu

3. AADESHA SANDHI: One letter changes
   Example: Hudugi + ondu = Hudugiyondu

SAMASA (COMPOUND WORDS):

Two words combine to make one meaning.

Types:
1. TATPURUSHA: First word qualifies second
   - Raja kumara (King + son = Prince)

2. KARMADHAARAYA: Adjective + noun
   - Hosa hannu (New fruit)

3. DWANDVA: Both are equal
   - Tanditayi (Father-mother)

4. BAHUVRIHI: Compound with implied meaning
   - Chandramukhi (Moon-faced - beautiful person)

5. AVYAYIBHAAVA: First word is unchangeable
   - Yathaashakti (As per ability)

ALANKAARA (FIGURES OF SPEECH):

Used to make writing beautiful.

1. UPAMA (Simile):
   "Chandranannu hage moogada moo"
   (Face like the moon)

2. ROOPAKA (Metaphor):
   "Avalu purnachandra"
   (She is full moon)

3. UTPREKSHA (Hyperbole):
   "Aakaasha mutthuva ettara"
   (Touching the sky)

4. SHLESHA (Pun):
   Words with multiple meanings

5. ATISHAYOKTI (Exaggeration):
   "Sahasra dipa belaku"
   (Light of thousand lamps)

KANNADA LITERATURE PERIODS:

1. PURVA HALEGANNADA (Pre-Old Kannada): 450-1000 AD
   Example: KAVIRAJAMARGA

2. HALEGANNADA (Old Kannada): 1000-1300 AD
   Famous: PAMPA, RANNA, JANNA

3. NADUKANNADA (Middle Kannada): 1300-1600 AD
   Famous: KUMARAVYASA, HARIHARA

4. HOSAGANNADA (Modern Kannada): 1600-Present
   Famous: KUVEMPU, BENDRE, KARANTH

FAMOUS POETS AND WRITERS:

PAMPA: Author of Vikramaarjuna Vijaya
RANNA: Sahasa Bhima Vijaya
KUMARAVYASA: Karnata Bharata Kathamanjari
PURANDARADASA: Hari bhakti songs (16th century)
KANAKADASA: Mohana Tarangini
KUVEMPU: Ramayana Darshanam (Jnanpith Award)
D.R. BENDRE: Naaku Tanthi (Jnanpith Award)
U.R. ANANTHAMURTHY: Samskara (Jnanpith Award)

JNANPITH AWARD WINNERS FROM KARNATAKA:
1. KUVEMPU (1967)
2. D.R. BENDRE (1973)
3. SHIVARAM KARANTH (1977)
4. MASTI VENKATESHA IYENGAR (1983)
5. V.K. GOKAK (1990)
6. U.R. ANANTHAMURTHY (1994)
7. GIRISH KARNAD (1998)
8. CHANDRASHEKHARA KAMBARA (2010)

Kannada has 8 Jnanpith Awards - MOST after Hindi!

Practice grammar and read literature to improve.'''},

    {'g': 7, 't': 'Kannada Literature Introduction',
     'd': 'Introduction to Kannada literature and famous works',
     'c': '''KANNADA SAHITYA PARICHAYA (Literature Introduction)

Kannada is one of the OLDEST languages in India.
It is over 2000 years old!

HISTORY OF KANNADA LITERATURE:

The oldest available work is KAVIRAJAMARGA by Shrivijaya (850 AD).
Even older inscriptions show Kannada language.

3 PRECIOUS GEMS OF KANNADA LITERATURE:
1. PAMPA (940 AD)
2. RANNA (993 AD)
3. PONNA (950 AD)

PAMPA - "AADIKAVI" (First poet):
- Wrote Vikramarjuna Vijayam
- Also wrote Aadipuranam
- Known as "Mahakavi" (Great poet)

RANNA:
- Wrote Sahasa Bheema Vijayam
- Also Ajita Tirthankara Puranam

PONNA:
- Wrote Shaanti Puranam
- Known as "Kavi Chakravarti"

VACHANA LITERATURE (12th Century):

A revolutionary form of literature.
Simple poems with deep meaning.
Used everyday language.

Famous Vachanakaras:
1. BASAVANNA - Founded Veerashaiva sect
2. AKKAMAHADEVI - Woman saint poet
3. ALLAMA PRABHU
4. CHANNABASAVA

Example Vachana of Basavanna:
"Kayakave Kailasa"
(Work is heaven)

This teaches the dignity of labor.

DASA SAAHITYA (Devotional Songs):

15-16th century, devotees of Lord Krishna sang songs in Kannada.

Famous Dasas:
1. PURANDARADASA - "Karnataka Sangeetha Pithamaha"
2. KANAKADASA - From shepherd community
3. VYASARAJA - Spiritual teacher

MODERN KANNADA WRITERS:

KUVEMPU (Kuppali Venkatappa Puttappa):
- Born 1904, Died 1994
- First Jnanpith Award for Kannada (1967)
- Famous works:
  * Ramayana Darshanam (Modern Ramayana)
  * Sri Ramayana Darshanam
  * Janapriya Valmiki Ramayana

D.R. BENDRE:
- Famous poet
- Padma Shri, Jnanpith Award
- "Naaku Tanthi" - famous work

SHIVARAM KARANTH:
- Novelist, playwright
- Jnanpith Award
- Famous novel: "Marali Mannige"

U.R. ANANTHAMURTHY:
- Novelist
- Jnanpith Award
- Famous novel: "Samskara"

GIRISH KARNAD:
- Playwright
- Jnanpith Award
- Famous plays: Hayavadana, Tughlaq, Nagamandala

CHANDRASHEKHARA KAMBARA:
- Poet, playwright
- Jnanpith Award

MASTI VENKATESHA IYENGAR:
- Short story writer
- "Chikkavira Rajendra"

POETRY (Padya):

Famous Kannada Poems:
1. "Bharata Janma" by Kuvempu (about India)
2. "Inda Eshtu Bittadante" by D.R. Bendre
3. "Anganalalli Aralisuva Ranga" by Kuvempu

FAMOUS QUOTES:

"Sarvajanaangada Shaantiya Tota" - Kuvempu
(The Garden of Peace for All Communities)

"Vishwamaanava" - Kuvempu
(Universal Human - we are all one)

THEATRE (Naataka):
Kannada theatre is very famous.
- Yakshagana (folk theatre) - very famous
- T.P. Kailasam plays
- Girish Karnad's modern plays

POPULAR KANNADA NOVELS:

1. Karvalo - K.P. Poornachandra Tejaswi
2. Bhittiyo Yaake Bittiyo - Sara Aboobacker
3. Mookajjiya Kanasugalu - Shivaram Karanth

FOLK LITERATURE:

JANAPADA SAHITYA (Folk Literature):
- Folk songs
- Folk stories
- Riddles
- Lullabies
- Proverbs

YAKSHAGANA:
- Traditional folk theatre
- Famous in coastal Karnataka
- Combines dance, music, story-telling

READING SUGGESTIONS:

For students:
1. Start with simple Kannada stories
2. Read children's magazines
3. Visit your school library
4. Listen to Kannada songs
5. Watch Kannada plays/dramas

LEARNING TIPS:

1. Read a Kannada newspaper daily
2. Listen to Kannada radio
3. Talk in Kannada with family
4. Watch Kannada movies
5. Memorize one poem each week
6. Practice writing essays

KANNADA RAJYOTSAVA:
- Celebrated on 1st November
- Anniversary of Karnataka state formation (1956)
- Yellow and red flag of Karnataka displayed
- Celebrate Kannada language and culture

Be proud of Kannada - one of the world's oldest classical languages!'''},

    {'g': 8, 't': 'Kannada Language Skills',
     'd': 'Advanced Kannada language - reading, writing, speaking',
     'c': '''KANNADA BHASHA KAUSHALYA (LANGUAGE SKILLS)

FOUR LANGUAGE SKILLS:

1. SHRAVANA (Listening)
2. BHAASHANA (Speaking)
3. PATHANA (Reading)
4. LEKHANA (Writing)

LISTENING SKILLS:

How to improve:
- Listen to Kannada news daily
- Listen to Kannada songs
- Watch Kannada movies/dramas
- Listen to teachers carefully
- Listen to audio books

SPEAKING SKILLS:

How to improve:
- Speak Kannada at home
- Participate in class discussions
- Tell stories in Kannada
- Recite poems with feeling
- Debate in Kannada

Pronunciation Tips:
- Open mouth properly
- Pronounce each akshara clearly
- Long vowels are LONGER
- Don't mix English words

READING SKILLS:

Three types of reading:
1. AROHANE (Skim) - Quick read for main idea
2. ARTHAGRAHANE (Detailed) - Understand everything
3. VICHAARANE (Critical) - Analyze deeply

Reading Strategies:
- Read title first
- Look at pictures
- Read aloud sometimes
- Note difficult words
- Summarize what you read

WRITING SKILLS:

Different forms of writing:

1. PRABANDHA (Essay)
Structure:
- Title
- Introduction
- Main Body (paragraphs)
- Conclusion

Example topics:
- Nanna Priya Hobby
- Sannevra Sahay
- Vidhya Mahatva

2. KATHA (Story)
Elements:
- Characters
- Setting
- Plot (Beginning, middle, end)
- Moral/Message

3. PATRA (Letter)
Types:
- Aupacharika (Formal)
- Anaupacharika (Informal)

Formal Letter Structure:
- Sender's address
- Date
- Receiver's address
- Subject
- Salutation
- Body
- Closing
- Signature

4. VARTHA PATRIKE (News Report)
Elements:
- Headline
- Date and place
- Who, what, when, where, why, how
- Quotes
- Photo caption

LITERATURE ANALYSIS:

When studying a Kannada lesson:
1. Read carefully
2. Understand difficult words
3. Find the main message
4. Identify literary devices
5. Note moral/teaching

LITERARY DEVICES (Alankaaragalu):

1. UPAMA (Simile):
"Hejje hadara hage"
(Like a snake's hiss)

2. UTPREKSHA (Hyperbole):
"Aakasha mutthuva ettara"
(Touching the sky)

3. ROOPAKA (Metaphor):
"Avalu chandrana mukhi"
(She is moon-faced)

4. ATISHAYOKTI (Exaggeration):
"Sahasra varsha"
(Thousand years)

CONJUNCTIONS (Connecting Words):

- MATTU (and)
- ATHAVA (or)
- ADARE (but)
- YAAKENDRE (because)
- ADAKE (so/therefore)
- ADARANTHE (similarly)

CONTEXTUAL VOCABULARY:

Academic Words:
- VIDYABHYAASA (Education)
- ADHYAYANA (Study)
- PARIKSHE (Exam)
- TARGATI (Class)
- PUSTAKA (Book)
- ANKAGALU (Marks)

Social Words:
- SAMAAJA (Society)
- SAMAAJIKA (Social)
- AARTHIKA (Economic)
- RAJAKEEYA (Political)
- AAROGYAVANTA (Healthy)

Career Words:
- KELASA (Job)
- DHANDE (Profession)
- VYAVASAYA (Business)
- VYAVASAAYIKA (Professional)

WRITING ESSAY EXAMPLE:

Topic: KSHEMA HAGU SHAANTI (Peace and Welfare)

Introduction:
Kshema haagu shaanti ee jagattige tumba muktyaprada
Aagive. Avu manushya jeevana sukha samrudhdiyim
saadhane sambandha tegedukolutthave.

Body Paragraph 1:
Kshema ennuvudu manushyana muulabhuta avashyakathe.
Aharavu, vasthi, vaidya seve, vidyabhyasa - ee ellavoo
kshemada bhaagavaagive.

Body Paragraph 2:
Shaanti illadiddare, kshema horyallakke saadhya?
Kalaha, yuddha, asantosha - eve avividha
roopagalu shaantiya dushmangalu.

Conclusion:
Naavu ellaroo shaantiyinda ondulava kshemadinda
baalo prayatnamadabeku.

VOCABULARY ENRICHMENT:

Learn 5 new words every day.
Use them in sentences.
Maintain a personal dictionary.

Difficult Words and Meanings:
- ANUKARANE: Imitation
- SVAATANTRYA: Freedom
- SAMAJIKA: Social
- ABHIMAANA: Pride
- VIVEKA: Wisdom

GRAMMAR PRACTICE:

Common Errors:
1. Wrong vibhakti
2. Subject-verb mismatch
3. Wrong tense
4. Mixing English and Kannada

Daily Practice:
- Write a paragraph
- Read a story
- Listen to news
- Speak with someone

PROVERBS (GADEGALU):

1. Madidare maaduthane, biludhare biluthane
   (As you sow, so shall you reap)

2. Maaduva kelasa madhura
   (Work done well is sweet)

3. Praayatnave Lakshmi
   (Effort is wealth)

4. Kalavu kalayalu
   (Time is the teacher)

Remember and use proverbs in writing!'''},

    {'g': 9, 't': 'Kannada Padya and Gadya',
     'd': 'Poetry and prose study',
     'c': '''KANNADA PADYA (POETRY) AND GADYA (PROSE)

PADYA (POETRY):

Padya is rhythmic writing with meaning.

Types of Kannada Poetry:

1. VACHANA (Free verse):
- Used by 12th century saints
- Simple language, deep meaning
- No fixed rules
- Examples by Basavanna, Akkamahadevi

2. CHAMPU (Mixed):
- Mix of prose and poetry
- Used in old works

3. SHATPADI (6-line verse):
- 6 lines per stanza
- Strict meter
- Used by Kumaravyasa

4. KEERTHANE (Devotional song):
- Devotional poetry
- Set to music
- Examples by Purandaradasa

5. BHAVAGEETHE (Lyrical):
- Modern poetry
- Expresses emotions
- Examples by D.R. Bendre

FAMOUS POEMS:

"Bharatamba Jaya Bharatamba" - Kuvempu
(Hail Mother India)

"Naaku Tanthi" - D.R. Bendre
About 4 strings of life

"Ade Kannadu" - K.S. Narasimhaswamy
About love poems

LITERARY DEVICES IN POEMS:

1. CHHANDAS (Meter):
   - Each line has fixed syllables
   - Rhythm and beat

2. PRAASA (Rhyme):
   - End rhyming words
   - Creates music

3. ALANKAARA (Figures of speech):
   - Upama (simile)
   - Roopaka (metaphor)

4. ARTHALANKAARA:
   - Word play
   - Multiple meanings

POEM ANALYSIS METHOD:

1. Read the whole poem
2. Find main idea
3. Identify rhyme pattern
4. Find difficult words
5. Note literary devices
6. Understand the message
7. Write summary

GADYA (PROSE):

Gadya is normal writing without rhyme.

Types:
1. KATHA (Story)
2. PRABANDHA (Essay)
3. CHITRA KATHA (Picture story)
4. YATRA KATHA (Travelogue)
5. AATMA KATHA (Autobiography)
6. JEEVANA KATHA (Biography)

FAMOUS PROSE WORKS:

1. KARVALO - K.P. Poornachandra Tejaswi
Setting: Western Ghats
About a man called Karvalo

2. SAMSKARA - U.R. Ananthamurthy
About a Brahmin community
Won Jnanpith

3. CHIKKAVIRA RAJENDRA - Masti
Historical novel
Won Jnanpith

4. MARALI MANNIGE - Shivaram Karanth
About village life

5. CHOMANA DUDI - Shivaram Karanth
About a low-caste man

WRITING STYLE:

In poetry:
- Use figurative language
- Use rhyme
- Maintain rhythm
- Express emotions

In prose:
- Use clear sentences
- Logical flow
- Descriptive language
- Direct meaning

PROSE ANALYSIS:

1. Identify the genre
2. Find main characters
3. Setting (where, when)
4. Plot (what happens)
5. Theme (main message)
6. Style and language

CHARACTER STUDY:

PROTAGONIST: Main character (hero)
ANTAGONIST: Opposing character (villain)
SUPPORTING: Other characters

Example: In Samskara
PROTAGONIST: Praneshacharya
SUPPORTING: Narayanappa, Chandri

THEMES IN KANNADA LITERATURE:

1. Social reform
2. Rural life
3. Family relationships
4. Caste system
5. Freedom struggle
6. Modern issues
7. Mythology

LANGUAGE FEATURES:

Pure Kannada words:
- ANNA (food)
- HALU (milk)
- MARA (tree)

Sanskrit-derived (Tatsama):
- VIDYA (education)
- SAHITYA (literature)
- NATAK (drama)

Local dialects:
- North Karnataka has different words
- Coastal Karnataka has unique expressions

WRITING EXERCISE:

Topic: Apply something you learned.

Write a short story (150 words) about:
- A kind farmer
- A brave girl
- A wise teacher

Use:
- Beginning, middle, end
- Dialogues
- Description
- A moral message

POETRY WRITING:

Try to write a simple 4-line poem:

Example:
Belaginindabaala raatri vare
Pathi kshana namageye kale
Vaktiyo kashtayoo nahi sairisi
Avalle nede ee jeevana kale.

Write your own poem about:
- Nature
- Family
- Friendship
- A festival

LEARNING TIPS:

1. Read 1 poem and 1 prose piece weekly
2. Memorize favorite quotes
3. Analyze writing techniques
4. Try writing yourself
5. Discuss with teacher and friends

Kannada has Rich literary heritage. Be proud!'''},

    {'g': 10, 't': 'Kannada Sahitya Advanced',
     'd': 'Advanced Kannada literature for class 10',
     'c': '''KANNADA SAAHITYA (Advanced Literature)

HISTORY OF KANNADA LITERATURE:

Kannada is one of the SCHEDULED LANGUAGES of India.
Government recognizes it as CLASSICAL LANGUAGE.
Over 2000 years of literary tradition.

PERIODS OF KANNADA LITERATURE:

1. PURVA HALEGANNADA (450-1000 AD):
- Earliest period
- Sanskrit influence

2. HALEGANNADA (1000-1200 AD):
- Trinity: Pampa, Ponna, Ranna
- Classical age

3. NADUKANNADA (1200-1600 AD):
- Vachana movement
- Dasa literature

4. HOSAGANNADA (1600 - Present):
- Modern literature
- Multiple Jnanpith awards

JNANPITH AWARDS IN KANNADA:

Karnataka has won the most Jnanpith awards (after Hindi):

1. KUVEMPU (1967) - Sri Ramayana Darshanam
2. D.R. BENDRE (1973) - Naaku Tanthi
3. SHIVARAM KARANTH (1977) - Mookajjiya Kanasugalu
4. MASTI (1983) - Chikkaveera Rajendra
5. V.K. GOKAK (1990) - Bharata Sindhu Rashmi
6. U.R. ANANTHAMURTHY (1994) - Samskara
7. GIRISH KARNAD (1998) - Tughlaq, Hayavadana
8. CHANDRASHEKHARA KAMBARA (2010) - Karimaayi

MAJOR LITERARY MOVEMENTS:

1. PAMPA AGE (10th century):
- Champu style
- Sanskrit-Kannada mix
- Religious themes

2. VACHANA MOVEMENT (12th century):
- Simple language
- Social reform
- Religious equality
- Basavanna, Akkamahadevi

3. DASA SAAHITYA (15-17th century):
- Devotional songs
- Bhakti to Vishnu/Krishna
- Purandaradasa, Kanakadasa

4. NAVODAYA (Renaissance) - 20th century:
- Modern literature
- Influenced by Western style
- Kuvempu, Bendre

5. NAVYA (Modernist) - 1950s:
- Experimental writing
- U.R. Ananthamurthy

6. DALITA AND BANDAYA SAHITYA:
- Voice of oppressed
- Social protest
- Devanuru Mahadeva

DETAILED STUDY:

KUVEMPU (Kuppali Venkatappa Puttappa):
Born: 29 Dec 1904, Died: 11 Nov 1994
Birth place: Hirekodige, Karnataka

Works:
1. SRI RAMAYANA DARSHANAM (Magnum Opus)
   - Modern Ramayana in Kannada
   - Won Jnanpith
2. KAANUR HEGGADITI (Novel)
3. MALEGALA MADHYE
4. KOLALU (Poetry collection)

Philosophy:
- "Sarvajanaangada Shaantiya Tota"
- Universal Brotherhood
- Vishwamaanava (Universal Human)

D.R. BENDRE (Dattatreya Ramachandra Bendre):
Born: 1896, Died: 1981

Works:
1. NAAKU TANTHI (Won Jnanpith)
2. SAKHI GEETHA
3. GANGAVATARANA

Famous as "Modern Day Kalidasa"
Master of Padya (poetry)

VACHANA STUDY:

BASAVANNA (1131-1196):
Founded Veerashaiva sect
Social reformer

Famous Vachana:
"Kasturi nelagina ondu gandhavanta"
(In one fragrance of musk lies everything)

"Kayakave Kailasa"
(Work itself is heaven)

AKKAMAHADEVI (12th century):
Woman saint poet
Famous for spiritual writings

"Avva kavanga panneradu"
(O mother, my twelve lovers)

ALLAMA PRABHU:
Mystic poet
"Tanu kareya thatva"

PURANDARADASA (1484-1564):
"Karnatak Sangeetha Pithamaha"
Composed 4.75 lakh songs

Famous Keerthane:
"Jagadoddhaarana aadisidale yashode"
(Yashoda played with the savior of the world)

KANAKADASA (1488-1562):
Born in shepherd family
Wrote "Mohana Tarangini"
"Ramadhanya Charite"

MODERN PROSE:

U.R. ANANTHAMURTHY:
Born: 1932, Died: 2014

Famous Works:
1. SAMSKARA (Novel - Jnanpith)
2. BHARATHIPURA (Novel)
3. AVASTHE (Novel)
4. BARA (Novel)

Themes: Caste, society, religion

SHIVARAM KARANTH (1902-1997):
Polymath - novelist, playwright, environmentalist

Famous Works:
1. MOOKAJJIYA KANASUGALU (Jnanpith)
2. CHOMANA DUDI
3. MARALI MANNIGE

GIRISH KARNAD (1938-2019):
Playwright, film director, actor

Famous Plays:
1. YAYATI
2. TUGHLAQ
3. HAYAVADANA
4. NAAGAMANDALA
5. TALEDANDA

CHANDRASHEKHARA KAMBARA:
Born 1937

Famous Works:
1. KARIMAAYI (Jnanpith)
2. SIRI SAMPIGE
3. JAISHANKARA HUDUGI

POETRY ANALYSIS METHOD:

When analyzing a Kannada poem:

1. Read aloud (focus on rhythm)
2. Note the theme
3. Identify form (vachana, padya, etc.)
4. Find literary devices:
   - Upama
   - Roopaka
   - Atishayokti
5. Understand emotion
6. Connect to your life
7. Identify message

PROSE ANALYSIS METHOD:

When analyzing prose:

1. Identify genre (story, novel, essay)
2. Plot structure
3. Characters (protagonist, antagonist)
4. Setting (time, place)
5. Conflict and resolution
6. Theme
7. Style of writing
8. Message/Moral

ESSAY WRITING (PRABANDHA):

Standard Essay Structure:

1. PRASTAVANE (Introduction)
   - Catchy opening
   - Background
   - Thesis statement

2. VISHAYA NIROOPANE (Body)
   - 2-3 paragraphs
   - Each para = one idea
   - Examples and details
   - Logical flow

3. UPASAMHARA (Conclusion)
   - Summarize main points
   - Final thought
   - Call to action (if needed)

EXAM PREPARATION:

For Class 10 Kannada Board Exam:

1. KAVYA STUDY:
   - Memorize poems
   - Understand meaning
   - Know the poet

2. GADYA STUDY:
   - Summarize chapters
   - Character study
   - Theme analysis

3. VYAKARANA:
   - Sandhi types
   - Samasa types
   - Alankara

4. WRITING:
   - Practice essays
   - Letter writing
   - Comprehension

5. GRAMMAR EXERCISES:
   - Make sentences
   - Fill in blanks
   - Choose correct word

PROVERBS TO REMEMBER (GADEGALU):

1. "Madidare maaduthane, biludhare biluthane"
   As you sow, so shall you reap

2. "Anyaaya kelasa anyaaya phala"
   Wrong actions bring wrong results

3. "Kayakave kailasa"
   Work is heaven

4. "Praayatnave lakshmi"
   Effort is wealth

5. "Vidya dadigare bhushana"
   Knowledge is ornament

KANNADA LITERATURE IS RICH:
Read different forms regularly.
Be proud of Kannada literary heritage!'''}
]


# ==================== HINDI RESOURCES ====================
HINDI_RESOURCES = [
    {'g': 1, 't': 'Hindi Varnamala (Alphabet)',
     'd': 'Learn Hindi alphabet - vowels and consonants',
     'c': '''HINDI VARNAMALA (ALPHABET)

Hindi varnamala has SVAR (Vowels) and VYANJAN (Consonants).

SVAR (VOWELS) - 13 LETTERS:

1. A (a)
2. AA (a long)
3. I (i)
4. EE (i long)
5. U (u)
6. OO (u long)
7. RI (ri)
8. E (e)
9. AI (ai)
10. O (o)
11. AU (au)
12. AM (am - nasal)
13. AH (ah - aspirated)

VYANJAN (CONSONANTS) - 33+ LETTERS:

KA-VARG (k sounds):
KA, KHA, GA, GHA, NGA

CHA-VARG (ch sounds):
CHA, CHHA, JA, JHA, NYA

TA-VARG (hard t sounds):
TA, THA, DA, DHA, NA

THA-VARG (soft t sounds):
THA, THHA, DHA, DHHA, NA

PA-VARG (p sounds):
PA, PHA, BA, BHA, MA

ANTA-STHA (between):
YA, RA, LA, VA

USHMA (hot):
SHA, SHHA, SA, HA

SPECIAL:
KSHA, TRA, GYA

WORDS PRACTICE:

Common Words (Romanized):
- MATAA (Mother)
- PITA (Father)
- BHAI (Brother)
- BAHEN (Sister)
- DADA (Grandfather - father's side)
- DADI (Grandmother - father's side)
- NANA (Grandfather - mother's side)
- NANI (Grandmother - mother's side)
- GHAR (House)
- PAANI (Water)
- DOODH (Milk)

ANIMALS (Janwar):
- GAAY (Cow)
- KUTTA (Dog)
- BILLI (Cat)
- GHODA (Horse)
- HAATHI (Elephant)
- SHER (Lion)
- BANDAR (Monkey)
- MACHHLI (Fish)

NUMBERS 1 to 10:
1 - EK
2 - DO
3 - TEEN
4 - CHAR
5 - PAANCH
6 - CHHE
7 - SAAT
8 - AATH
9 - NAU
10 - DUS

COLORS (Rang):
- LAAL (Red)
- PEELA (Yellow)
- NEELA (Blue)
- HARA (Green)
- SAFED (White)
- KAALA (Black)
- BHOORA (Brown)

DAYS OF WEEK (Saptaah ke Din):
- SOMVAR (Monday)
- MANGALVAR (Tuesday)
- BUDHVAR (Wednesday)
- GURUVAR (Thursday)
- SHUKRAVAR (Friday)
- SHANIVAR (Saturday)
- RAVIVAR (Sunday)

MONTHS:
- JANVARI (January)
- FEBRUARY
- MAARCH (March)
- APREL (April)
- MAI (May)
- JOON (June)
- JULAI (July)
- AGAST (August)
- SITAMBAR (September)
- AKTOOBAR (October)
- NAVAMBAR (November)
- DISAMBAR (December)

COMMON PHRASES:
- NAMASTE / NAMASKAR (Hello/Greetings)
- DHANYAVAD (Thank you)
- MAAFI / KSHAMA (Sorry)
- KAISE HAIN AAP? (How are you?)
- MAIN THEEK HOON (I am fine)
- KYA HAAL HAI? (How's it going?)

BODY PARTS:
- SIR (Head)
- AANKH (Eye)
- KAAN (Ear)
- NAAK (Nose)
- MUH (Mouth)
- HAATH (Hand)
- PAIR (Leg)
- UNGLI (Finger)

NATURE:
- SOORAJ (Sun)
- CHAAND (Moon)
- TAARA (Star)
- AAKAASH (Sky)
- BAARISH (Rain)
- PED (Tree)
- PHOOL (Flower)
- NADI (River)

Practice writing Hindi varnamala daily.
Read Hindi words aloud.
Hindi is the official language of India.
It uses Devanagari script.'''},

    {'g': 2, 't': 'Hindi Shabd Rachana (Word Formation)',
     'd': 'Learn how Hindi words are formed',
     'c': '''HINDI SHABD RACHANA (WORD FORMATION)

A SHABD (word) is formed by joining AKSHAR (letters).

SIMPLE WORDS:

3-Letter Words:
- BAAP (Father)
- MAAA (Mother)
- LADKA (Boy)
- LADKI (Girl)
- PHAL (Fruit)

4-Letter Words:
- PUSTAK (Book)
- KAGAZ (Paper)
- PENCIL (Pencil)
- SHIKSHAK (Teacher)
- VIDYALAYA (School)

OPPOSITE WORDS (Vipreetarthi Shabd):

- DIN (Day) - RAAT (Night)
- ACHCHA (Good) - BURA (Bad)
- AMEER (Rich) - GAREEB (Poor)
- KHUSH (Happy) - DUKHI (Sad)
- BADA (Big) - CHHOTA (Small)
- LAMBA (Long/Tall) - CHHOTA (Short)
- THANDA (Cold) - GARAM (Hot)
- ANDHERA (Dark) - UJALA (Light)
- ANDAR (Inside) - BAHAR (Outside)
- AAGE (Front) - PEECHHE (Behind)

SIMILAR WORDS (Samanarthi Shabd):

- MAATA = MAA (Mother)
- PITA = BAAP (Father)
- BACHHA = BAALAK (Child)
- GHAR = MAKAAN (House)
- AAKAASH = GAGAN (Sky)
- PHOOL = PUSHPA (Flower)
- KAMAL = SAROJA (Lotus)

PURE HINDI WORDS:
- KHET (Field)
- KHAANA (Food)
- MAKAAN (House)

SANSKRIT WORDS (Tatsam):
- AGNI (Fire)
- JAL (Water)
- PRITHVI (Earth)
- VAYU (Air)
- AAKAASH (Sky)

URDU WORDS USED IN HINDI:
- KITAAB (Book) - Arabic origin
- KURSI (Chair) - Persian origin
- DARWAZA (Door) - Persian origin
- ZAROORI (Necessary) - Arabic

ANIMALS (Pashu-Pakshi):

DOMESTIC ANIMALS (Paaltu):
- GAAY (Cow)
- BHAINS (Buffalo)
- BAKRI (Goat)
- BHED (Sheep)
- KUTTA (Dog)
- BILLI (Cat)
- MURGI (Hen)

WILD ANIMALS (Jangli):
- SHER (Lion)
- BAAGH (Tiger)
- HAATHI (Elephant)
- HIRAN (Deer)
- BANDAR (Monkey)
- BHALU (Bear)
- BHEDIYA (Wolf)
- LOMRI (Fox)

BIRDS (Pakshi):
- KAUVA (Crow)
- TOTA (Parrot)
- MOR (Peacock)
- KABUTAR (Pigeon)
- CHIDIYA (Sparrow)
- HANS (Swan)
- ULLU (Owl)
- BATAK (Duck)

FOOD ITEMS (Khane ki Cheezen):

GRAINS (Anaaj):
- CHAWAL (Rice)
- ATTA (Flour)
- DAAL (Lentils)
- GEHU (Wheat)
- JOWAR (Sorghum)
- BAJRA (Pearl Millet)

VEGETABLES (Sabziyan):
- ALOO (Potato)
- TAMATAR (Tomato)
- PYAAZ (Onion)
- BHINDI (Ladyfinger)
- BAINGAN (Brinjal)
- GAJAR (Carrot)
- LAUKI (Bottle Gourd)
- PALAK (Spinach)

FRUITS (Phal):
- AAM (Mango)
- SEB (Apple)
- KELA (Banana)
- ANGOOR (Grapes)
- SANTRA (Orange)
- ANNANAS (Pineapple)
- PAPITA (Papaya)
- TARBOOZ (Watermelon)

DRINKS (Peene Ki):
- PAANI (Water)
- DOODH (Milk)
- CHAI (Tea)
- COFFEE (Coffee)
- JUICE (Juice)
- LASSI (Yogurt drink)
- SHARBAT (Sweet drink)

FAMILY MEMBERS:

NUCLEAR FAMILY:
- PITA / BAAP (Father)
- MAATA / MAA (Mother)
- BHAI (Brother)
- BAHEN (Sister)

EXTENDED FAMILY (Father's side):
- DADA (Grandfather)
- DADI (Grandmother)
- CHACHA (Father's younger brother)
- CHACHI (Chacha's wife)
- TAAU (Father's elder brother)
- TAAI (Taau's wife)
- BUA (Father's sister)

EXTENDED FAMILY (Mother's side):
- NANA (Grandfather)
- NANI (Grandmother)
- MAMA (Mother's brother)
- MAMI (Mama's wife)
- MAUSI (Mother's sister)
- MAUSA (Mausi's husband)

PROFESSIONS (Vyavasaay):

- KISAAN (Farmer)
- SHIKSHAK / GURU (Teacher)
- VAIDYA / DOCTOR (Doctor)
- VYAPAARI (Businessman)
- SIPAHI (Soldier)
- POLICE
- VAKEEL (Lawyer)
- NEETA (Leader)
- LEKHAK (Writer)
- KAVI (Poet)
- KALAKAAR (Artist)

EMOTIONS (Bhavnayen):
- KHUSHI (Happiness)
- GUSSA (Anger)
- DUKH (Sadness)
- DAR (Fear)
- PYAAR (Love)
- NAFRAT (Hatred)
- SHAANTI (Peace)

TIME (Samaya):
- AAJ (Today)
- KAL (Yesterday/Tomorrow)
- ABHI (Now)
- BAAD MEIN (Later)
- SUBAH (Morning)
- DOPAHAR (Afternoon)
- SHAAM (Evening)
- RAAT (Night)

Practice these words daily.
Make sentences with them.'''},

    {'g': 5, 't': 'Hindi Vyakaran (Grammar)',
     'd': 'Basic to intermediate Hindi grammar',
     'c': '''HINDI VYAKARAN (GRAMMAR)

PARTS OF SPEECH (Bhasha ke Ang):

1. SANGYA (NOUN):
Words that name people, places, things.

Types:
A) VYAKTIVACHAK (Proper noun)
   - RAMESH, DELHI, GANGA

B) JATIVACHAK (Common noun)
   - LADKA (boy), SHAHAR (city)

C) BHAAV-VACHAK (Abstract noun)
   - PYAAR (love), GUSSA (anger)

D) SAMUH-VACHAK (Collective noun)
   - SENA (army), JHUND (flock)

E) DRAVYA-VACHAK (Material noun)
   - SONA (gold), CHAANDI (silver)

2. SARVANAAM (PRONOUN):
Used in place of nouns.

Personal Pronouns:
- MAIN (I)
- TU (You - informal)
- AAP (You - respectful)
- VAH (He/She)
- YEH (This)
- HUM (We)
- VE (They)

Possessive Pronouns:
- MERA (My/Mine)
- TERA (Your)
- ISKA (Of this)
- USKA (Of that/his/hers)
- HAMARA (Our)

Demonstrative Pronouns:
- YEH (This)
- VAH (That)
- YE (These)
- VE (Those)

3. KRIYA (VERB):
Action words.

Types:
A) SAKARMAK (Transitive) - takes object
   - "Main khana khaata hoon" (I eat food)

B) AKARMAK (Intransitive) - no object
   - "Main jaata hoon" (I go)

4. VISHESHAN (ADJECTIVE):
Describes nouns.

Types:
A) GUNVACHAK (Quality): ACHCHHA, BURA, BADA
B) PARIMAANBOOTHAK (Quantity): THODA, BAHUT
C) SANKHYA-VACHAK (Number): EK, DO, DASS
D) SARVANAAMIK: MERA, USKA

5. KRIYA-VISHESHAN (ADVERB):
Modifies verbs.

Types:
A) Time: KAB (when), AAJ (today), KAL (tomorrow)
B) Place: KAHAN (where), YAHAN (here), VAHAN (there)
C) Manner: KAISE (how), DHEERE (slowly)

6. SAMBANDHBODHAK (PREPOSITION):
Shows relation.

- MEIN (in)
- PAR (on)
- SE (from)
- KO (to)
- KE LIYE (for)
- KE PAAS (near)
- KE SAATH (with)

7. SAMUCHCHAYBODHAK (CONJUNCTION):
Joins words/sentences.

- AUR (and)
- LEKIN (but)
- YA (or)
- KYONKI (because)
- ISLIYE (therefore)

8. VISMAYADIBODHAK (INTERJECTION):
Expresses emotion.

- WAAH! (Wow!)
- HAYE! (Alas!)
- ARE! (Hey!)
- CHHI! (Yuck!)

VACHAN (NUMBER):

1. EKVACHAN (Singular):
- LADKA (boy)
- KITAAB (book)
- LADKI (girl)

2. BAHUVACHAN (Plural):
- LADKE (boys)
- KITAABEN (books)
- LADKIYAAN (girls)

Rules for Plural:
- Add E: LADKA -> LADKE
- Add EN: KITAAB -> KITAABEN
- Add YAAN: LADKI -> LADKIYAAN
- Same: PHAL (fruit/fruits)

LING (GENDER):

1. PULLING (Masculine):
- LADKA (boy)
- AADMI (man)
- BAAP (father)

2. STREELING (Feminine):
- LADKI (girl)
- AURAT (woman)
- MAA (mother)

Some words have specific gender:
- PHOOL (flower) - masculine
- KAMAL (lotus) - masculine
- CHIRAYIA (sparrow) - feminine

KAARAK (CASES):
Shows relation between words.

Hindi has 8 Kaarak:
1. KARTA (Doer) - ne: "Maine"
2. KARMA (Object) - ko: "uska"
3. KARAN (Instrument) - se: "kalam se"
4. SAMPRADAAN (To/For) - ko/ke liye
5. APAADAAN (From) - se: "ghar se"
6. SAMBANDH (Of) - ka, ki, ke
7. ADHIKARAN (In/On) - mein, par
8. SAMBODHAN (Address) - hey, are

TENSE (KAAL):

1. VARTAMAAN KAAL (Present):
- MAIN JAATA HOON (I go)
- VAH KHEL RAHA HAI (He is playing)

2. BHOOT KAAL (Past):
- MAIN GAYA (I went)
- VAH AAYA (He came)

3. BHAVISHYAT KAAL (Future):
- MAIN JAAONGA (I will go)
- VAH AAYEGA (He will come)

VAACHYA (VOICE):

1. KARTRI VAACHYA (Active):
- RAM KHAANA KHAATA HAI
  (Ram eats food)

2. KARMA VAACHYA (Passive):
- KHAANA RAM SE KHAYA JAATA HAI
  (Food is eaten by Ram)

SANDHI (JOINING):

Two words can join to form one.

Types:
1. SVAR SANDHI: vowel + vowel
   - VIDYA + ARTH = VIDYARTH (Student)

2. VYANJAN SANDHI: consonant changes

3. VISARG SANDHI: visarga combines

SAMAS (COMPOUND):

Two words combine for new meaning.

Types:
1. TATPURUSH: first word qualifies second
   - DESHBHAKT (devoted to country)

2. KARMADHARAYA: adjective + noun
   - NEELKAMAL (blue lotus)

3. DWANDV: equal weight
   - MATA-PITA (parents)

4. BAHUVRIHI: implied meaning
   - CHAKRADHAR (One who holds disc - Krishna)

5. AVYAYIBHAV: first word indeclinable
   - YATHASHAKTI (As per ability)

Practice these grammar rules.
Apply them when writing and speaking.'''}
]

# Add fewer placeholder resources for grades 3, 4, 6, 7, 8, 9, 10 in Hindi (brief)
HINDI_RESOURCES.extend([
    {'g': 3, 't': 'Hindi Vyakaran Basic',
     'd': 'Basic Hindi grammar for class 3',
     'c': '''HINDI VYAKARAN (BASIC GRAMMAR)

SANGYA (NOUN):
Names of person, place, thing, animal.
Examples: RAM, DELHI, KITAAB, KUTTA

SARVANAAM (PRONOUN):
Used instead of noun.
- MAIN (I), TU (You), VAH (He/She), HUM (We)

KRIYA (VERB):
Action words.
- KHAANA (eat), PEENA (drink), JAANA (go), AANA (come)

VISHESHAN (ADJECTIVE):
Describing words.
- ACHCHHA (good), BURA (bad), BADA (big), CHHOTA (small)

SIMPLE SENTENCES:

1. MAIN SCHOOL JAATA HOON
   (I go to school)

2. MAA KHAANA BANAATI HAIN
   (Mother makes food)

3. HUM KHELTE HAIN
   (We play)

QUESTION WORDS:
- KYA (What?)
- KAUN (Who?)
- KAB (When?)
- KAHAN (Where?)
- KYUN (Why?)
- KAISE (How?)

NUMBERS 1-20:
1 EK, 2 DO, 3 TEEN, 4 CHAR, 5 PAANCH,
6 CHHE, 7 SAAT, 8 AATH, 9 NAU, 10 DUS,
11 GYARAH, 12 BAARAH, 13 TERAH, 14 CHAUDAH,
15 PANDRAH, 16 SOLAH, 17 SATRAH, 18 ATHARAH,
19 UNNIS, 20 BEES

OPPOSITES:
- DIN - RAAT (Day - Night)
- BADA - CHHOTA (Big - Small)
- ACHCHHA - BURA (Good - Bad)
- KHATTA - MEETHA (Sour - Sweet)

Practice writing simple Hindi sentences daily.'''},

    {'g': 4, 't': 'Hindi Vakya (Sentences)',
     'd': 'Forming Hindi sentences',
     'c': '''HINDI VAKYA (SENTENCES)

A complete sentence has SUBJECT and PREDICATE.

STRUCTURE: Subject + Object + Verb

Examples:
1. RAM AAM KHAATA HAI (Ram eats mango)
2. MAA KHAANA BANATI HAI (Mother cooks food)
3. HUM SCHOOL JAATE HAIN (We go to school)

TYPES OF SENTENCES:

1. STATEMENT (Vidhaanvaachak):
- YEH MERA GHAR HAI (This is my home)
- AAM MEETHA HAI (Mango is sweet)

2. NEGATIVE (Nishedhaatmak):
- MAIN NAHI JAAOONGA (I will not go)
- VAH NAHI HAI (He is not there)

3. QUESTION (Prashnavaachak):
- TUMHARA NAAM KYA HAI? (What is your name?)
- KAHAN JA RAHE HO? (Where are you going?)

4. EXCLAMATORY (Vismayaadibodhak):
- WAAH! KITNA SUNDAR! (Wow! How beautiful!)
- ARRE! KYA HUA? (Hey! What happened?)

5. COMMAND (Aagyaarthak):
- IDHAR AAO (Come here)
- BAITHO (Sit down)
- KHANA KHAO (Eat food)

COMMON DAILY SENTENCES:

Morning:
- SUBH PRABHAT (Good morning)
- AAJ KA MAUSAM ACHCHHA HAI (Today's weather is good)
- MAIN UTHTA HOON (I wake up)

At School:
- NAMASKAR GURUJI (Greetings teacher)
- MAIN PADHTA HOON (I study)
- MAIN HOMEWORK KARTA HOON (I do homework)

At Home:
- MAA, MUJHE BHOOK LAGI HAI (Mother, I'm hungry)
- PIYA, KAB AAOGE? (Papa, when will you come?)
- BHAI, KHELOGE? (Brother, will you play?)

CONVERSATION PRACTICE:

Sample Dialogue:

A: NAMASTE! AAP KAISE HAIN?
B: NAMASTE! MAIN THEEK HOON. AAP?

A: MAIN BHI THEEK HOON. AAPKA NAAM KYA HAI?
B: MERA NAAM RAM HAI. AAPKA?

A: MERA NAAM SHYAM HAI.
B: KAHAN SE AAYE HAIN?

A: MAIN DELHI SE AAYA HOON.

Practice making such dialogues with friends.

CONNECTING WORDS (Yojak):
- AUR (and)
- LEKIN (but)
- YA (or)
- KYONKI (because)
- ISLIYE (therefore)

VERB FORMS:

Present Tense:
- KHAATA HOON (eat - I)
- KHAATE HAIN (eat - they)
- KHAATI HUN (eat - I, female)

Past Tense:
- KHAYA (ate)
- KHAYI (ate, female)
- GAYA (went)
- AAYA (came)

Future Tense:
- KHAOONGA (will eat - male)
- KHAOONGI (will eat - female)
- JAOONGA (will go)

Make 5 sentences daily in Hindi.'''},

    {'g': 6, 't': 'Hindi Vyakaran Intermediate',
     'd': 'Intermediate Hindi grammar',
     'c': '''HINDI VYAKARAN INTERMEDIATE

SANDHI:

When two words join, sound changes.

Types:
1. SVAR SANDHI (Vowel + Vowel)
   - VIDYA + ARTHI = VIDYARTHI
   - SURYA + ASTAYA = SURYASTAYA

2. VYANJAN SANDHI (Consonant changes)
   - DIK + AMBAR = DIGAMBAR
   - VAAK + ISH = VAAKISH

3. VISARG SANDHI
   - NIH + APAVAD = NIRAPAVAD

SAMAS (Compound):

Two words combine.

Types:
1. TATPURUSH: First word qualifies second
   - DESHBHAKT (devotee of country)
   - SUKHAMAY (full of happiness)
   - PUSTAKALAYA (book + place = library)

2. KARMADHARAYA: Adjective + noun
   - NEELKAMAL (blue lotus)
   - CHANDRAVADAN (moon-faced)

3. DWANDV: Equal weight
   - MATA-PITA (parents)
   - BHAI-BAHEN (brother-sister)
   - DIN-RAAT (day-night)

4. BAHUVRIHI: Implied meaning
   - CHAKRADHAR (Krishna - one with disc)
   - PATAMBAR (one wearing yellow)

5. AVYAYIBHAV: First word indeclinable
   - YATHASHAKTI (as per ability)
   - YATHASAMAY (as per time)

UPSARG (Prefix):
Word added before a word.

Examples:
- AN + UCHIT = ANUCHIT (Not proper)
- A + GYAN = AGYAN (Ignorant)
- NIR + DOSH = NIRDOSH (Innocent)
- DUR + GUN = DURGUN (Bad quality)
- ATI + UCHIT = ATIUCHIT (Very proper)

PRATYAY (Suffix):
Word added after a word.

Examples:
- KARMA + KAAR = KARMAKAAR (Worker)
- ADHYA + AAPAK = ADHYAAPAK (Teacher)
- SANSKRIT + IK = SANSKRITIK (Cultural)

VAKYA-ANTARAN (Sentence Transformation):

Active to Passive:
Active: RAM PATAA LIKHTA HAI
Passive: PATAA RAM SE LIKHA JAATA HAI

Direct to Indirect:
Direct: RAM NE KAHA, "MAIN JAAOONGA"
Indirect: RAM NE KAHA KI VAH JAAYEGA

ALANKAR (Figures of Speech):

1. ANUPRAS (Alliteration):
- Same starting letters
- "Kaali ghata kavi kya kahe"

2. UPMA (Simile):
- Comparison using JAISA/KE SAMAAN
- "Chand jaisa chehra"

3. RUPAK (Metaphor):
- Direct identification
- "Vah hamara chand hai"

4. ATISHAYOKTI (Hyperbole):
- Exaggeration
- "Aakaash chhoone wala"

KAVI AND LEKHAK (Poets and Writers):

Famous Hindi Poets:
- TULSIDAS - Ramcharitmanas
- KABIR - Dohas
- SURDAS - Krishna Bhakti
- MEERA BAI - Krishna songs
- RAHEEM - Dohas

Modern Writers:
- PREMCHAND - Story writer (Godan, Gaban)
- JAYSHANKAR PRASAD - Plays
- MAHADEVI VARMA - Poetry
- HARIVANSH RAI BACHCHAN - Poetry

FAMOUS DOHA (Couplets):

Kabir's Doha:
"Bura jo dekhan main chala, bura na milya koy
Jo dil khojha apna, mujhse bura na koy"

Meaning: I went looking for evil, found none
When I searched my own heart, no one was worse than me

Rahim's Doha:
"Rahiman dhaaga prem ka, mat todo chatkay
Toote se phir na jure, jure gaanth pad jaay"

Meaning: The thread of love, don't break it suddenly
Once broken, doesn't rejoin, even if joined, knot remains

Practice writing essays and stories in Hindi.'''},

    {'g': 7, 't': 'Hindi Sahitya Parichay',
     'd': 'Introduction to Hindi literature',
     'c': '''HINDI SAHITYA PARICHAY (Literature Introduction)

Hindi is the OFFICIAL LANGUAGE of India.
Spoken by millions of people worldwide.

PERIODS OF HINDI LITERATURE:

1. AADIKAL (Ancient Period) - 1050-1375 AD
- Early Hindi works
- Chand Bardai's Prithviraj Raso

2. BHAKTIKAL (Devotional Period) - 1375-1700 AD
- Religious and devotional
- Tulsidas, Kabir, Surdas, Meerabai

3. REETIKAL (Romantic Period) - 1700-1900 AD
- Romantic poetry
- Bihari Lal, Keshavdas

4. AADHUNIK KAAL (Modern Period) - 1900-Present
- Modern literature
- Multiple genres

FAMOUS HINDI WRITERS:

TULSIDAS (1532-1623):
- Wrote RAMCHARITMANAS
- Hindi version of Ramayana
- Most popular Hindi work

Famous Doha:
"Hari ko bhajie sada bhalai
Aur kuch kije sob bhulayi"

KABIR (15th century):
- Mystic poet
- Famous for Dohas (couplets)
- Promoted unity of religions

Famous Doha:
"Bura jo dekhan main chala, bura na milya koy
Jo dil khojha apna, mujhse bura na koy"

SURDAS (1478-1583):
- Blind poet
- Devotee of Lord Krishna
- Wrote Sursagar

MEERABAI (1498-1547):
- Princess turned saint
- Devotee of Krishna
- Composed bhajans

PREMCHAND (1880-1936):
- "Father of Hindi Short Story"
- Famous works:
  * Godaan (Novel)
  * Gaban (Novel)
  * Idgah (Story)
  * Kafan (Story)
  * Boodhi Kaki (Story)

JAYSHANKAR PRASAD (1889-1937):
- Poet, playwright
- Famous works:
  * Kamayani (Epic poem)
  * Chandragupta (Play)
  * Skandagupta (Play)

MAHADEVI VARMA (1907-1987):
- "Modern Meera"
- Jnanpith Award (1982)
- Famous works:
  * Yama (Poetry)
  * Atit ke Chalchitra (Memoirs)

HARIVANSH RAI BACHCHAN (1907-2003):
- Famous for Madhushala
- Father of Amitabh Bachchan

JAINENDRA KUMAR:
- Famous novelist
- "Tyagpatra" novel

AGYEYA (1911-1987):
- Modernist writer
- Jnanpith Award

DHARMVEER BHARATI (1926-1997):
- Famous novel: Gunahon ka Devta
- Andhayug (play)

HARI VANSH RAI BACHCHAN:
"Madhushala" - famous poem

JNANPITH AWARD WINNERS IN HINDI:

1. SUMITRA NANDAN PANT (1968) - Chidambara
2. RAMDHARI SINGH DINKAR (1972) - Urvashi
3. SACHIDANANDA HEERANANDA VATSYAYAN (Agyeya) (1978)
4. MAHADEVI VARMA (1982) - Yama
5. NIRMAL VERMA (1999)
6. KEDARNATH SINGH (2013)
7. KUNWAR NARAIN (2005)
8. SHRILAL SHUKLA (2009)
9. AMARKANT (2009)

POETRY MOVEMENTS:

CHHAYAVAAD (Romantic):
- Jayshankar Prasad
- Sumitra Nandan Pant
- Mahadevi Varma
- Suryakant Tripathi 'Nirala'

PRAGATIVAD (Progressive):
- Spread by Sahitya Sammelan

PRAYOGVAD (Experimental):
- Sachchidananda Vatsyayan (Agyeya)

NAYI KAVITA (New Poetry):
- Modern era poetry

DOHAS (COUPLETS):

Kabir's Dohas:
"Saiyan se sab hot hai, bandhe se kuch nahi
Rai se parvat kare, parvat rai mahi"

Tulsidas's Dohas:
"Aapas mein milkar rahain to sukha pavein bhayee
Ladai te jhagde se ho ub jaata hai"

KAVITAYEN (Poems):

Famous Poems:
- "Hamaare Bharatvarsh" (Our India)
- "Bharat Mata" (Mother India)
- "Vande Mataram"
- "Saare Jahaan se Achchha"

STORY (KAHANI):

Famous Hindi Stories:
- "Boodhi Kaki" by Premchand
- "Idgah" by Premchand
- "Mantra" by Premchand
- "Kafan" by Premchand

These stories teach:
- Moral values
- Social issues
- Indian culture
- Family relationships

NOVELS (UPNYAAS):

Famous Hindi Novels:
- GODAAN by Premchand
- GABAN by Premchand
- NIRMALA by Premchand
- GUNAHON KA DEVTA by Dharmvir Bharati
- TAMAS by Bhisham Sahni

PLAYS (NAATAK):

Famous Hindi Plays:
- CHANDRAGUPTA by Jayshankar Prasad
- ASHADH KA EK DIN by Mohan Rakesh
- ANDHAYUG by Dharmvir Bharati

Hindi literature is rich with:
- Bhakti poetry
- Modern novels
- Social stories
- Patriotic poems
- Children's literature

Read at least one chapter daily in Hindi.'''},

    {'g': 8, 't': 'Hindi Kavya aur Gadya',
     'd': 'Hindi poetry and prose study',
     'c': '''HINDI KAVYA (POETRY) AUR GADYA (PROSE)

KAVYA (POETRY):

CHHAND (Meter):
The rhythm and beat of poetry.

Types of Chhand:
1. CHAUPAI (4 lines)
2. DOHA (2 lines)
3. SOHILA (4 lines)
4. SAVAIYAA (4 lines)
5. KAVITT (4 lines)

DOHA EXAMPLE (Rahim):
"Rahiman paani raakhiye, bin paani sab soon
Paani gaye na ubre, moti, manus, choon"

Without water, all is empty
Without water, pearl, person, lime - none can survive.

CHAUPAI EXAMPLE (Tulsidas):
"Mangal moorthi maaruti nandan
Sankat haran mangal kar van"

This is the auspicious form of Maruti's son
Reliever of troubles and source of well-being.

KAVITA TYPES:

1. PRABANDH KAVYA (Long narrative poem)
   - Ramcharitmanas
   - Kamayani
   - Urvashi

2. KHAND KAVYA (Section poem)
   - Smaller narrative

3. MUKTAK (Independent verse)
   - Dohas, Chaupais

4. GEET (Song)
   - Songs and lyrics

5. SHATPADI (Six-line verse)

LITERARY DEVICES:

1. ANUPRAS (Alliteration):
"Charu chandra ki chanchal kiran"
(Same starting letters)

2. UPMA (Simile):
"Chand jaisa chehra"
(Face like the moon)

3. RUPAK (Metaphor):
"Vah hamara chand hai"
(He is our moon)

4. UTPREKSHA (Resemblance):
"Maano kamal sa khila"
(As if a lotus has bloomed)

5. SHLESH (Pun):
- Words with multiple meanings

GADYA (PROSE):

Prose is straight writing.

Types:
1. UPNYAAS (Novel)
2. KAHANI (Story)
3. NIBANDH (Essay)
4. NAATAK (Play/Drama)
5. JEEVANI (Biography)
6. AATMAKATHA (Autobiography)
7. YATRA-VRITTANT (Travelogue)
8. SAMVAD (Dialogue)

FAMOUS HINDI NOVELS:

1. GODAAN by Premchand
- About a poor farmer
- Indian agricultural problems

2. GUNAHON KA DEVTA by Dharmvir Bharati
- Love story
- Set in Allahabad

3. TAMAS by Bhisham Sahni
- Partition story

4. RANG BHOOMI by Premchand
- About blind beggar

5. AANDHA YUG by Dharmvir Bharati
- Modern times' confusion

SHORT STORIES:

1. IDGAAH by Premchand
- About a poor boy Hamid
- Buys tongs for grandmother
- Teaches value of selflessness

2. KAFAN by Premchand
- About poverty
- Father and son

3. MANTRA by Premchand
- About Hindu-Muslim unity

4. BADE GHAR KI BETI by Premchand
- About marriage

5. NAMAK KA DAAROGA by Premchand
- About honesty

ESSAYS (NIBANDH):

Famous Essayists:
- Acharya Ramchandra Shukla
- Babu Gulab Rai
- Hazariprasad Dwivedi

Essay Topics:
- "Vidya ka Mahatva" (Importance of Education)
- "Vrukha aur Manav" (Tree and Human)
- "Sangharsh hi Jeevan hai" (Struggle is life)
- "Vidyalaya ka Ek Din" (A day at school)

PLAYS (NAATAK):

Famous Hindi Plays:

1. CHANDRAGUPTA by Jayshankar Prasad
- About Chandragupta Maurya
- Mauryan empire

2. SKANDAGUPTA by Jayshankar Prasad
- Historical play

3. ASHADH KA EK DIN by Mohan Rakesh
- About poet Kalidas

4. ANDHAYUG by Dharmvir Bharati
- About Mahabharata

5. SURYAMUKHI by Yashpal
- Modern play

LITERATURE ANALYSIS:

When studying a Hindi text:

1. Read carefully (अर्थग्रहण - understanding meaning)
2. Identify the writer
3. Find difficult words
4. Understand cultural context
5. Find the central theme
6. Identify literary devices
7. Note the writer's style
8. Connect to your experience

POEM ANALYSIS:

Read the poem and find:
- Theme (Vishay)
- Mood (Bhav)
- Rhythm (Chhand)
- Imagery (Bimba)
- Message (Sandesh)

PROSE ANALYSIS:

For stories/novels:
- Characters
- Setting (where/when)
- Plot (what happens)
- Theme
- Conflict
- Resolution
- Message

WRITING PRACTICE:

Topic: VIDYA KA MAHATVA (Importance of Education)

Sample paragraph:
Vidya manav ka sabse bada dhan hai. Vidya hi vyakti
ko gyan deti hai aur usse achchha banti hai.
Bina vidya ke manushya ka jeevan vyarth hai.

Vidya se manushya samaaj mein samman paata hai.
Yah vyakti ko swayam par nirbhar banati hai.
Vidya hi sachi sampada hai jo na kisi se chheeni jaa
sakti hai, na khoyi.

Topic: MERA PRIYA SHIKSHAK (My Favorite Teacher)

Sample paragraph:
Mera priya shikshak shri Sharmaji hain. Ve hamen
Hindi padhaate hain. Ve bahut achchhe se padhaate
hain aur sabhi bachchon se pyaar karte hain.

Shri Sharmaji bahut gyani hain. Ve hamesha hamen
naye-naye baatein bataate hain. Mein unka aabhari hoon.

LEARNING METHODS:

1. Read 1 story daily
2. Memorize 1 doha weekly
3. Practice writing essays
4. Watch Hindi movies
5. Listen to Hindi songs
6. Talk in Hindi

Be proud of Hindi - one of the oldest languages of India!'''}
])

# Add Grade 9, 10 placeholders for Hindi
HINDI_RESOURCES.append({'g': 9, 't': 'Hindi Vyakaran Advanced',
     'd': 'Advanced Hindi grammar for class 9',
     'c': '''HINDI VYAKARAN ADVANCED (CLASS 9)

VARN (LETTER):
Smallest unit of language.
- Swar (vowel): 13 letters
- Vyanjan (consonant): 33+ letters

SHABD (WORD):
Made of one or more letters with meaning.

Types of words:
1. RUDH SHABD: Cannot be broken
   - "Ghar" (house)

2. YAUGIK SHABD: Made of multiple parts
   - "Vidyalaya" = Vidya + Alaya

3. YOGRUDH SHABD: Specific meaning
   - "Pankaj" = mud + born = Lotus

VAKYA (SENTENCE):

A sentence has:
1. UDDESHYA (Subject)
2. VIDHEYA (Predicate)

Example:
"Ram khaata hai"
Ram = Subject
khaata hai = Predicate

TYPES OF SENTENCES:

By Purpose:
1. VIDHIVACHAK (Statement): "Yeh kitab hai"
2. NISHEDHATMAK (Negative): "Yeh kitab nahi hai"
3. PRASHNAVACHAK (Question): "Kya yeh kitab hai?"
4. AAGYAARTHAK (Command): "Kitab pado"
5. ICHCHHAARTHAK (Wish): "Tum khush raho"
6. SANDEHARTHAK (Doubt): "Shayad vah aayega"

By Structure:
1. SARAL VAKYA (Simple): One main clause
2. SAYUKT VAKYA (Compound): Multiple equal clauses
3. MISHRA VAKYA (Complex): Main + subordinate clause

KAARAK (CASE):

8 Types of Kaarak:

1. KARTA (Doer)
   Vibhakti: 0 or "ne"
   "Ram (ne) khana khaya"

2. KARMA (Object)
   Vibhakti: "ko"
   "Ram (ne) Sita ko dekha"

3. KARAN (Means)
   Vibhakti: "se", "ke dwara"
   "Mein kalam se likhta hoon"

4. SAMPRADAN (Recipient)
   Vibhakti: "ko", "ke liye"
   "Mein Ram ko kitab di"

5. APAADAAN (From)
   Vibhakti: "se"
   "Vah ped se gira"

6. SAMBANDH (Relation)
   Vibhakti: "ka, ki, ke"
   "Ram ki kitab"

7. ADHIKARAN (Location)
   Vibhakti: "mein, par"
   "Kitab mez par hai"

8. SAMBODHAN (Address)
   Vibhakti: "Re, hey"
   "He Bhagwan!"

KAAL (TENSE):

3 Main Tenses x 3 Aspects = Multiple forms

PRESENT TENSE:
- Simple: "Mein khaata hoon"
- Continuous: "Mein kha raha hoon"
- Perfect: "Mein khaa chuka hoon"

PAST TENSE:
- Simple: "Mein khaaya"
- Continuous: "Mein kha raha tha"
- Perfect: "Mein kha chuka tha"

FUTURE TENSE:
- Simple: "Mein khaoonga"
- Continuous: "Mein kha raha hoonga"
- Perfect: "Mein kha chuka hoonga"

VAACHYA (VOICE):

1. KARTRI VAACHYA (Active):
"Ram ne kitab padi"

2. KARMA VAACHYA (Passive):
"Ram dwara kitab padi gayi"

3. BHAVA VAACHYA (Impersonal):
"Hum dwara baith jata hai"

UPSARG (PREFIX):
Added before a word.

Common Prefixes:
- AN-, A- (not): Anuchit (improper)
- DUR-, DUS- (bad): Durachar (bad behavior)
- NIR-, NIH- (without): Nirdosh (innocent)
- SU- (good): Sushashan (good governance)
- VI- (special): Vishesh (special)
- PRA- (forward): Prakaash (light)
- ATI- (very): Atikaale (very early)
- ANU- (after): Anukaranan (imitation)

PRATYAY (SUFFIX):
Added after a word.

Common Suffixes:
- -KAAR: Lekhak (writer)
- -KAARI: Upakaari (helpful)
- -TA: Sundarta (beauty)
- -TAA: Shulkta (light)
- -PAN: Bachpan (childhood)
- -TVA: Mahatva (importance)

MUHAVRE (Idioms):

Some common Hindi idioms:

1. "Aankh ka taara" (Apple of the eye)
   Meaning: Very dear

2. "Aankh ki kirkiri" (Eye's pain)
   Meaning: Someone disliked

3. "Aasamaan se gira" (Fell from sky)
   Meaning: Surprised

4. "Aasamaan sir par utha lena" (Lift sky on head)
   Meaning: Make lots of noise

5. "Doodh ka doodh, paani ka paani" (Milk from milk, water from water)
   Meaning: Clear distinction

6. "Chand par thookna" (Spit on moon)
   Meaning: Try impossible task

LOKOKTIYAAN (Proverbs):

1. "Naach na jaane aangan tedha"
   Doesn't know to dance, blames the floor

2. "Saanp bhi mar gaya aur laathi bhi nahi tooti"
   Snake died but stick didn't break (Killed two birds with one stone)

3. "Andhon mein kaana raja"
   Among blind, one-eyed is king

4. "Honhar birvan ke hot chikne paat"
   Talented from young age

5. "Ek panthi do kaaj"
   One traveler, two tasks

Practice grammar exercises daily.'''})

HINDI_RESOURCES.append({'g': 10, 't': 'Hindi Sahitya Advanced',
     'd': 'Advanced Hindi literature for class 10',
     'c': '''HINDI SAHITYA ADVANCED (CLASS 10)

HISTORY OF HINDI LITERATURE:

Hindi developed from Sanskrit and Apabhramsha.
Modern Hindi (Khari Boli) is used today.

LITERARY PERIODS:

1. AADIKAAL (1050-1375 AD):
- Beginning of Hindi
- Prithviraj Raso by Chand Bardai

2. BHAKTIKAAL (1375-1700 AD):
- Devotional movement
- Two streams: Nirgun and Sagun
- Tulsidas, Kabir, Surdas, Meera

3. REETIKAAL (1700-1900 AD):
- Romantic poetry
- Bihari Lal, Keshavdas, Dev

4. AADHUNIK KAAL (1900-Present):
- Modern literature
- Multiple movements

MODERN HINDI MOVEMENTS:

1. BHARATENDU YUG (1900-1920):
- Bharatendu Harishchandra
- Father of Modern Hindi Literature
- Made Hindi standard

2. DWIVEDI YUG (1920-1936):
- Mahavir Prasad Dwivedi
- Saraswati magazine
- Improved Hindi language

3. CHHAYAVAAD (1918-1936):
- Romantic poetry
- 4 Major poets:
  * Jayshankar Prasad
  * Sumitra Nandan Pant
  * Mahadevi Varma
  * Suryakant Tripathi 'Nirala'

4. PRAGATIVAAD (1936-1943):
- Progressive
- Social change focus

5. PRAYOGVAAD (1943-1950):
- Experimental
- Agyeya

6. NAYI KAVITA (1950-onwards):
- New Poetry

7. NAYI KAHANI (1956-onwards):
- New Story

MAJOR JNANPITH AWARDS IN HINDI:

1. Sumitra Nandan Pant (1968) - Chidambara
2. Ramdhari Singh Dinkar (1972) - Urvashi
3. Agyeya / S.H.A. Vatsyayan (1978)
4. Mahadevi Varma (1982) - Yama
5. Naresh Mehta (1992)
6. Nirmal Verma (1999)
7. Kunwar Narain (2005)
8. Shrilal Shukla (2009)
9. Amarkant (2009)
10. Kedarnath Singh (2013)

DETAILED STUDY:

TULSIDAS (1532-1623):
- Born Rajapur, Uttar Pradesh
- Famous works:
  * RAMCHARITMANAS (Magnum Opus)
  * Kavitavali
  * Vinaya Patrika
  * Hanuman Chalisa

Famous Doha:
"Tulsi yeh sansar mein, bhaant-bhaant ke log
Sab se hil-mil chaliye, nadi naav sangat"

(There are different people in this world
Walk along with all, like river and boat)

KABIR (1440-1518):
- Mystic poet from Varanasi
- Bridge between Hindu-Muslim
- Famous for Dohas
- "Sakhi", "Bijak", "Padavali"

Famous Doha:
"Maathaa marak gaya, jugva marak gaya
Tar tar daadi badh gayi, sangya sangya jaay"

PREMCHAND (1880-1936):
- Born Lamhi, Varanasi
- "Father of Modern Hindi Novel"
- Original name: Dhanpat Rai

Famous works:
1. GODAAN - About poor farmer Hori
2. GABAN - About greed
3. NIRMALA - Social novel
4. RANG BHOOMI - About blind beggar
5. KARMABHOOMI - Social
6. SEVASADAN - About prostitutes

Famous Stories:
1. IDGAAH - Hamid buys tongs
2. KAFAN - Poverty
3. MANTRA - Hindu-Muslim unity
4. POOS KI RAAT - Winter night
5. NAMAK KA DAAROGA - Honesty

JAYSHANKAR PRASAD (1889-1937):
- Born Varanasi
- Chhayavaad poet
- Famous works:
  * KAMAYANI (Epic poem)
  * CHANDRAGUPTA (Play)
  * SKANDAGUPTA (Play)
  * Aansoo (Poem)

MAHADEVI VARMA (1907-1987):
- "Modern Meera"
- Jnanpith Award (1982)
- Famous works:
  * Yama (Poetry)
  * Neelambara
  * Sandhya Geet
  * Smriti ki Rekhayein (Memoir)

DHARMVIR BHARATI (1926-1997):
- Famous novelist and dramatist
- Famous works:
  * Gunahon ka Devta (Novel)
  * Andhayug (Play)

RAMDHARI SINGH DINKAR (1908-1974):
- National Poet
- Famous works:
  * Urvashi (Won Jnanpith)
  * Rashmirathi
  * Kurukshetra

LITERARY ANALYSIS:

POEM ANALYSIS:

When studying a poem:
1. Identify the poet
2. Find the theme
3. Note the form (doha, chaupai, etc.)
4. Identify rasa (emotion):
   - Shringaar (love)
   - Veer (heroism)
   - Karuna (sorrow)
   - Hasya (humor)
   - Raudra (anger)
   - Bhayanak (fear)
   - Bibhatsa (disgust)
   - Adbhut (wonder)
   - Shaant (peace)

5. Identify alankaars:
   - Anupraas
   - Upma
   - Roopak
   - Utpreksha
   - Atishayokti
   - Shlesh

NOVEL/STORY ANALYSIS:

1. Identify characters:
   - Protagonist
   - Antagonist
   - Supporting

2. Setting:
   - Time
   - Place
   - Background

3. Plot:
   - Beginning
   - Conflict
   - Climax
   - Resolution

4. Theme:
   - Central message
   - Universal truth

5. Style:
   - Language
   - Description
   - Dialogue

ESSAY WRITING:

Structure of a good essay:

1. PRASTAVANA (Introduction):
- Catchy opening
- Background
- Thesis statement

2. VISHAYAVASTHU (Body):
- 2-3 paragraphs
- Each paragraph one main idea
- Examples, evidence
- Logical flow

3. UPASAMHAR (Conclusion):
- Summary of main points
- Personal opinion
- Call to action

ESSAY TOPICS FOR CLASS 10:

1. Vidya ka Mahatva (Importance of Education)
2. Vrukha aur Manushya (Tree and Man)
3. Bharatiya Sanskriti (Indian Culture)
4. Vigyan ke Chamatkar (Wonders of Science)
5. Mera Priya Lekhak (My Favorite Writer)
6. Computer aur Aaj ka Yug (Computer and Today)
7. Pradushan ki Samasya (Pollution Problem)

LETTER WRITING:

FORMAL LETTER:
- Sender's address
- Date
- Receiver's designation
- Subject
- Aadarniya
- Body
- Sadhanyavad
- Apka aagyakari
- Name

INFORMAL LETTER:
- Sender's address
- Date
- Priya/Pyare
- Body
- Tumhara/Aapka
- Name

COMPREHENSION:

When reading a passage:
1. Read carefully
2. Find main idea
3. Note details
4. Understand context
5. Answer questions in own words

WRITING SKILLS:

For Class 10 board exam:
1. Practice essays (200-250 words)
2. Letters (formal and informal)
3. Story writing (200-300 words)
4. Story completion
5. Comprehension passages
6. Translations

KAVITA (POETRY) TO REMEMBER:

Some famous lines:

"Bharat humara desh hai" - Bharatendu Harishchandra

"Saare jahaan se accha, Hindustan hamara" - Iqbal

"Madhushala" - Bachchan
"Bhar do jholi meri ya Mohammad" - Tulsidas

Read at least one Hindi text per week.
Practice writing in Hindi.
Hindi is one of the world's most spoken languages.

Be proud of Hindi heritage!'''})


def get_youtube(title, language):
    """Get YouTube link for language topics"""
    title_l = title.lower()
    if 'kannada' in title_l or language == 'Kannada':
        links = {
            'alphabet': ('https://www.youtube.com/watch?v=H0pSJWX-zRk', 'Periwinkle Kannada'),
            'words': ('https://www.youtube.com/watch?v=cZX0HQzWVcU', 'Periwinkle Kannada'),
            'grammar': ('https://www.youtube.com/watch?v=l5p4VWl8gWE', 'Kannada Learning Tutor'),
            'literature': ('https://www.youtube.com/watch?v=hG8m_FsT_AY', 'Kannada Sahitya'),
        }
        for k, v in links.items():
            if k in title_l:
                return v
        return ('https://www.youtube.com/results?search_query=learn+kannada+for+kids', 'Kannada Learning')
    else:  # Hindi
        links = {
            'alphabet': ('https://www.youtube.com/watch?v=lyL3IPP-yyo', 'Kids Tube'),
            'varnamala': ('https://www.youtube.com/watch?v=lyL3IPP-yyo', 'Kids Tube'),
            'grammar': ('https://www.youtube.com/watch?v=zHy7Cf-yfBQ', 'Magnet Brains Hindi'),
            'literature': ('https://www.youtube.com/watch?v=zHy7Cf-yfBQ', 'Magnet Brains Hindi'),
            'word': ('https://www.youtube.com/watch?v=lyL3IPP-yyo', 'Kids Tube'),
            'sentence': ('https://www.youtube.com/watch?v=zHy7Cf-yfBQ', 'Magnet Brains Hindi'),
        }
        for k, v in links.items():
            if k in title_l:
                return v
        return ('https://www.youtube.com/c/MagnetBrainsEducation', 'Magnet Brains')


def get_ncert(grade, subject):
    """NCERT links for languages"""
    if subject == 'Kannada':
        return ('https://ncert.nic.in/textbook.php', f'NCERT Kannada Class {grade}')
    else:  # Hindi
        return ('https://ncert.nic.in/textbook.php', f'NCERT Hindi Class {grade}')


# Quizzes for languages
KANNADA_QUIZZES = [
    {'g': 1, 't': 'Kannada Basics Quiz - Class 1',
     'questions': [
         {'q': 'How many vowels (Svaragalu) does Kannada have?', 'a': '10', 'b': '13', 'c': '15', 'd': '20', 'correct': 'B'},
         {'q': 'What does "Amma" mean in Kannada?', 'a': 'Father', 'b': 'Mother', 'c': 'Sister', 'd': 'Brother', 'correct': 'B'},
         {'q': 'What is "Neeru" in English?', 'a': 'Milk', 'b': 'Food', 'c': 'Water', 'd': 'Fire', 'correct': 'C'},
         {'q': 'How do you say "One" in Kannada?', 'a': 'Eradu', 'b': 'Mooru', 'c': 'Ondu', 'd': 'Aaru', 'correct': 'C'},
         {'q': 'What is "Hasu" in English?', 'a': 'Dog', 'b': 'Cat', 'c': 'Cow', 'd': 'Bird', 'correct': 'C'},
     ]},
    {'g': 2, 't': 'Kannada Words Quiz - Class 2',
     'questions': [
         {'q': 'What does "Sooryaa" mean?', 'a': 'Moon', 'b': 'Sun', 'c': 'Star', 'd': 'Sky', 'correct': 'B'},
         {'q': 'How do you say "Five" in Kannada?', 'a': 'Naalku', 'b': 'Aidu', 'c': 'Aaru', 'd': 'Elu', 'correct': 'B'},
         {'q': '"Pustaka" means?', 'a': 'Pen', 'b': 'Book', 'c': 'Desk', 'd': 'Chair', 'correct': 'B'},
         {'q': '"Kemppu" color is?', 'a': 'Yellow', 'b': 'Blue', 'c': 'Red', 'd': 'Green', 'correct': 'C'},
         {'q': '"Akka" means?', 'a': 'Younger sister', 'b': 'Mother', 'c': 'Aunt', 'd': 'Elder sister', 'correct': 'D'},
     ]},
    {'g': 5, 't': 'Kannada Reading Quiz - Class 5',
     'questions': [
         {'q': 'Father of Kannada literature?', 'a': 'Pampa', 'b': 'Ranna', 'c': 'Ponna', 'd': 'Kuvempu', 'correct': 'A'},
         {'q': 'Karnataka Rajyotsava is celebrated on?', 'a': 'October 1', 'b': 'November 1', 'c': 'December 1', 'd': 'August 15', 'correct': 'B'},
         {'q': '"Naanu shaalege hoguttene" means?', 'a': 'I am eating', 'b': 'I go to school', 'c': 'I am sleeping', 'd': 'I am playing', 'correct': 'B'},
         {'q': 'Who wrote "Sri Ramayana Darshanam"?', 'a': 'D.R. Bendre', 'b': 'Kuvempu', 'c': 'Masti', 'd': 'Karanth', 'correct': 'B'},
         {'q': 'How many Jnanpith awards have been won by Kannada?', 'a': '5', 'b': '6', 'c': '7', 'd': '8', 'correct': 'D'},
     ]},
    {'g': 10, 't': 'Kannada Literature Quiz - Class 10',
     'questions': [
         {'q': 'Who is called "Aadikavi" of Kannada?', 'a': 'Ranna', 'b': 'Pampa', 'c': 'Ponna', 'd': 'Janna', 'correct': 'B'},
         {'q': '"Karnataka Sangeetha Pithamaha" is?', 'a': 'Kanakadasa', 'b': 'Purandaradasa', 'c': 'Basavanna', 'd': 'Kuvempu', 'correct': 'B'},
         {'q': 'Vachana movement started in which century?', 'a': '10th', 'b': '11th', 'c': '12th', 'd': '13th', 'correct': 'C'},
         {'q': 'Who wrote "Samskara"?', 'a': 'Kuvempu', 'b': 'Bendre', 'c': 'U.R. Ananthamurthy', 'd': 'Karanth', 'correct': 'C'},
         {'q': 'First Jnanpith Award winner from Karnataka?', 'a': 'Bendre', 'b': 'Karanth', 'c': 'Kuvempu', 'd': 'Masti', 'correct': 'C'},
     ]},
]

HINDI_QUIZZES = [
    {'g': 1, 't': 'Hindi Varnamala Quiz - Class 1',
     'questions': [
         {'q': 'How many vowels (Svar) does Hindi have?', 'a': '10', 'b': '11', 'c': '13', 'd': '15', 'correct': 'C'},
         {'q': 'What does "Mata" mean?', 'a': 'Father', 'b': 'Mother', 'c': 'Sister', 'd': 'Brother', 'correct': 'B'},
         {'q': 'What is "Paani" in English?', 'a': 'Milk', 'b': 'Water', 'c': 'Food', 'd': 'Tea', 'correct': 'B'},
         {'q': 'How do you say "Two" in Hindi?', 'a': 'Ek', 'b': 'Do', 'c': 'Teen', 'd': 'Char', 'correct': 'B'},
         {'q': 'What is "Gaay" in English?', 'a': 'Dog', 'b': 'Cat', 'c': 'Cow', 'd': 'Goat', 'correct': 'C'},
     ]},
    {'g': 5, 't': 'Hindi Grammar Quiz - Class 5',
     'questions': [
         {'q': 'How many types of nouns in Hindi?', 'a': '3', 'b': '4', 'c': '5', 'd': '6', 'correct': 'C'},
         {'q': '"Hari" is which type of noun?', 'a': 'Common', 'b': 'Proper', 'c': 'Abstract', 'd': 'Collective', 'correct': 'B'},
         {'q': 'Plural of "Ladka" is?', 'a': 'Ladka', 'b': 'Ladke', 'c': 'Ladkon', 'd': 'Ladkiyaan', 'correct': 'B'},
         {'q': 'Past tense of "Khaata hai"?', 'a': 'Khaaya', 'b': 'Khaayega', 'c': 'Khaa raha hai', 'd': 'Khaaye', 'correct': 'A'},
         {'q': 'Hindi mein "I" kaise kahenge?', 'a': 'Tu', 'b': 'Aap', 'c': 'Main', 'd': 'Hum', 'correct': 'C'},
     ]},
    {'g': 10, 't': 'Hindi Literature Quiz - Class 10',
     'questions': [
         {'q': 'Who wrote Ramcharitmanas?', 'a': 'Kabir', 'b': 'Tulsidas', 'c': 'Surdas', 'd': 'Meera', 'correct': 'B'},
         {'q': 'Father of Hindi Short Story?', 'a': 'Premchand', 'b': 'Jayshankar Prasad', 'c': 'Mahadevi Varma', 'd': 'Bachchan', 'correct': 'A'},
         {'q': 'Premchand wrote which novel?', 'a': 'Godaan', 'b': 'Kamayani', 'c': 'Urvashi', 'd': 'Saket', 'correct': 'A'},
         {'q': 'Mahadevi Varma is known as?', 'a': 'Modern Tulsidas', 'b': 'Modern Meera', 'c': 'Modern Surdas', 'd': 'Modern Kabir', 'correct': 'B'},
         {'q': 'Kamayani is written by?', 'a': 'Premchand', 'b': 'Jayshankar Prasad', 'c': 'Dinkar', 'd': 'Bachchan', 'correct': 'B'},
     ]},
]


def add_all():
    app = create_app('development')
    with app.app_context():
        teacher = User.query.filter_by(email='teacher@example.com').first()
        if not teacher:
            print("[ERROR] Teacher not found")
            return

        os.makedirs('./data/resources', exist_ok=True)
        existing_resources = {r.title for r in Resource.query.all()}

        # Add Kannada resources
        kannada_added = 0
        for r in KANNADA_RESOURCES:
            if r['t'] in existing_resources:
                continue
            filename = f"kannada_g{r['g']}_{r['t'].replace(' ', '_').replace('(', '').replace(')', '')[:40]}"
            txt_path = f"data/resources/{filename}.txt"
            pdf_path = f"data/resources/{filename}.pdf"

            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(r['c'])

            try:
                pdf = PDF(title=r['t'], subject='Kannada', grade=r['g'])
                pdf.add_page()
                pdf.render(r['c'])
                pdf.output(pdf_path)
            except Exception as e:
                print(f"[PDF ERR] {r['t']}: {e}")
                continue

            file_size = os.path.getsize(pdf_path)
            yt_url, yt_ch = get_youtube(r['t'], 'Kannada')
            ncert_url, ncert_ch = get_ncert(r['g'], 'Kannada')

            resource = Resource(
                title=r['t'], description=r['d'], subject='Kannada',
                grade_level=r['g'], content_type='pdf', file_path=pdf_path,
                file_size=file_size, youtube_url=yt_url, youtube_channel=yt_ch,
                ncert_url=ncert_url, ncert_chapter=ncert_ch,
                created_by=teacher.id, is_published=True
            )
            db.session.add(resource)
            kannada_added += 1
            print(f"[KANNADA] Grade {r['g']}: {r['t']}")

        # Add Hindi resources
        hindi_added = 0
        for r in HINDI_RESOURCES:
            if r['t'] in existing_resources:
                continue
            filename = f"hindi_g{r['g']}_{r['t'].replace(' ', '_').replace('(', '').replace(')', '')[:40]}"
            txt_path = f"data/resources/{filename}.txt"
            pdf_path = f"data/resources/{filename}.pdf"

            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(r['c'])

            try:
                pdf = PDF(title=r['t'], subject='Hindi', grade=r['g'])
                pdf.add_page()
                pdf.render(r['c'])
                pdf.output(pdf_path)
            except Exception as e:
                print(f"[PDF ERR] {r['t']}: {e}")
                continue

            file_size = os.path.getsize(pdf_path)
            yt_url, yt_ch = get_youtube(r['t'], 'Hindi')
            ncert_url, ncert_ch = get_ncert(r['g'], 'Hindi')

            resource = Resource(
                title=r['t'], description=r['d'], subject='Hindi',
                grade_level=r['g'], content_type='pdf', file_path=pdf_path,
                file_size=file_size, youtube_url=yt_url, youtube_channel=yt_ch,
                ncert_url=ncert_url, ncert_chapter=ncert_ch,
                created_by=teacher.id, is_published=True
            )
            db.session.add(resource)
            hindi_added += 1
            print(f"[HINDI] Grade {r['g']}: {r['t']}")

        # Add Kannada quizzes
        existing_quizzes = {q.title for q in Quiz.query.all()}
        kn_quizzes_added = 0
        for q in KANNADA_QUIZZES:
            if q['t'] in existing_quizzes:
                continue
            quiz = Quiz(
                title=q['t'],
                description=f"Test your Kannada knowledge - Grade {q['g']}",
                subject='Kannada',
                grade_level=q['g'],
                created_by=teacher.id,
                total_questions=len(q['questions']),
                passing_score=60.0,
                is_published=True
            )
            db.session.add(quiz)
            db.session.flush()

            for idx, qd in enumerate(q['questions']):
                question = QuizQuestion(
                    quiz_id=quiz.id,
                    question_text=qd['q'],
                    question_type='mcq',
                    option_a=qd['a'],
                    option_b=qd['b'],
                    option_c=qd['c'],
                    option_d=qd['d'],
                    correct_option=qd['correct'],
                    question_order=idx,
                    marks=1.0
                )
                db.session.add(question)
            kn_quizzes_added += 1
            print(f"[KN QUIZ] {q['t']}")

        # Add Hindi quizzes
        hi_quizzes_added = 0
        for q in HINDI_QUIZZES:
            if q['t'] in existing_quizzes:
                continue
            quiz = Quiz(
                title=q['t'],
                description=f"Test your Hindi knowledge - Grade {q['g']}",
                subject='Hindi',
                grade_level=q['g'],
                created_by=teacher.id,
                total_questions=len(q['questions']),
                passing_score=60.0,
                is_published=True
            )
            db.session.add(quiz)
            db.session.flush()

            for idx, qd in enumerate(q['questions']):
                question = QuizQuestion(
                    quiz_id=quiz.id,
                    question_text=qd['q'],
                    question_type='mcq',
                    option_a=qd['a'],
                    option_b=qd['b'],
                    option_c=qd['c'],
                    option_d=qd['d'],
                    correct_option=qd['correct'],
                    question_order=idx,
                    marks=1.0
                )
                db.session.add(question)
            hi_quizzes_added += 1
            print(f"[HI QUIZ] {q['t']}")

        db.session.commit()
        print(f"\n{'='*60}")
        print(f"Kannada resources added: {kannada_added}")
        print(f"Hindi resources added: {hindi_added}")
        print(f"Kannada quizzes added: {kn_quizzes_added}")
        print(f"Hindi quizzes added: {hi_quizzes_added}")
        print(f"Total resources: {Resource.query.count()}")
        print(f"Total quizzes: {Quiz.query.count()}")
        print(f"{'='*60}")


if __name__ == '__main__':
    try:
        add_all()
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
