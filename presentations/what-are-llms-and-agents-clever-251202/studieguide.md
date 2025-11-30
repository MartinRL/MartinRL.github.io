# Studieguide: LLMs & Agents - Från Magi till Matematik

> **Syfte:** Denna guide följer presentationens struktur och förklarar varje koncept på djupet. Läs den 5-10 gånger för att kunna tala fritt om varje *slide*.

---

## Introduktion: *From Magic to Math*

**Arthur C. Clarke's tredje lag:**
> *"Any sufficiently advanced technology is indistinguishable from magic."*

Detta är utgångspunkten. *LLMs* verkar magiska - de kan skriva kod, översätta språk, resonera om komplexa problem. Men bakom kulisserna är det matematik. Inte ovanlig matematik, utan välkänd linjär algebra, sannolikhetsteori och optimering. Målet med denna guide är att avmystifiera teknologin.

### Sex Kärnkoncept

Presentationen bygger på sex fundament:

1. ***Neural Networks*** → Hur viktade kopplingar skapar "intelligens"
2. ***Tokens*** → Hur *LLMs* processar text
3. ***Transformers*** → Varför parallell *attention* möjliggör modern AI
4. ***Training*** → Hur råa modeller blir hjälpsamma assistenter
5. ***Hallucinations*** → Varför *LLMs* självsäkert genererar falsk information
6. ***Agents*** → Hur *LLMs* löser komplexa uppgifter med verktyg

Dessa sex koncept hänger intimt samman och bygger på varandra.

---

## Del 1: *Neural Networks*

### *Building Blocks* - Grundstenarna

***Neurons* (artificiella neuroner):**
- En *neuron* är en enkel beräkningsenhet som tar emot *inputs*, multiplicerar med *weights* (vikter), och producerar en *output*
- Tänk på en *neuron* som en liten beslutsfattare: "Vilka *inputs* är viktiga?"
- Varje *input* har en *weight* som avgör hur mycket den påverkar *outputen*
- Exempel: Om *neuronen* ska känna igen ordet "katt", kanske den har hög *weight* för *features* som "fyra ben", "päls", "jamar"

**Analogi:**
Tänk på *neurons* som röstare i en demokrati. Varje röstare (*input*) har olika mycket inflytande (*weight*). Summan av alla viktade röster bestämmer beslutet (*output*).

***Layers* (lager):**
- *Neurons* är organiserade i lager - som våningar i en byggnad
- ***Input layer:*** Tar emot rådata (t.ex. *tokens*)
- ***Hidden layers:*** Progressiv bearbetning där mening extraheras
- ***Output layer:*** Slutligt resultat (t.ex. nästa *token*)

**Progressiv abstraktion:**
- Tidiga lager ser mönster (bokstavskombinationer, orddelar)
- Mellersta lager ser koncept (grammatik, syntax)
- Djupa lager ser sammanhang (mening, logik, stil)

***LLMs* har ~100 lager** - detta är vad som gör dem kraftfulla.

**Minnesregel:**
*"Neurons that fire together, wire together"* → *"Tokens that appear together, weight together"*

När två *tokens* ofta förekommer tillsammans i träningsdatan, kommer deras *weights* att justeras så att de förstärker varandra.

### *Parameters* - *The Scale*

**Vad är en *parameter*?**
En *parameter* = en *weight* i nätverket. Varje koppling mellan *neurons* har en *weight*. Dessa *weights* är vad modellen "lär sig" under träning.

***Cloud Models* (2025):**
- ***GPT-5:*** ~2T (*trillion*) *parameters* - estimerat
- ***GPT-4:*** 1.8T *parameters*
- ***Claude Opus 4.1:*** ~1T *parameters*
- ***Claude Sonnet 4.5:*** ~500B (*billion*) *parameters*

**Kostnad:** $50M-$100M+ att träna
**Träning:** 3-6 månader på tusentals *GPU:er*

***Office Models* ($15K-$50K hårdvara):**
- ***Llama 3.3:*** 70B *parameters* (*Dual RTX 4090*)
- ***Qwen Coder:*** 32B *parameters* (*Single RTX 4090*)
- ***Phi-4:*** 14B *parameters* (*Consumer GPU*)

***Quantization* (kompression):**
- Teknik för att minska modellstorlek med 75%
- *Trade-off:* 2-5% kvalitetsförlust
- Gör det möjligt att köra stora modeller lokalt
- Exempel: 70B-modell som normalt kräver 140GB *RAM* → 35GB med *quantization*

**Analogi för skala:**
*GPT-5* med 2T *parameters* är som *Empire State Building*. En 70B *office-modell* är som en 5-våningsbyggnad. Inte lika imponerande, men fortfarande väldigt kapabel för många uppgifter.

### *What They Learn*

***Neural networks* lär sig inte genom programmering - de upptäcker mönster:**

***Grammar* (grammatik):**
- *Subject-verb-object* strukturer
- Tempusböjningar
- Pluralformer
- Exempel: Efter *"The cats"* kommer sannolikt ett verb i plural

***Facts* (fakta):**
- *"Paris is the capital of France"*
- MEN: Fakta är inte lagrade i en databas, utan som *patterns* i *weights*
- Detta är viktigt för att förstå *hallucinations* senare

***Style* (stil):**
- Hur *Shakespeare* skriver vs hur teknisk dokumentation skrivs
- Formellt vs informellt språk
- Olika genrer och toner

***Logic* (logik):**
- *If A > B and B > C, then A > C*
- Deduktion och induktion
- Matematiska samband

**Kritisk insikt:**
*Traditional programs* = recept vi skriver steg-för-steg (*if-statements*, *loops*)
*LLMs* = kockar som lärt sig genom att smaka miljoner rätter

De har aldrig sett receptet, men har absorberat essensen. Inga *if-statements*, inga *loops* - bara 1.8 *trillion learned patterns* från internet.

**Detta är varför *LLMs* är *"discovered, not designed"*.**

---

## Del 2: *Tokens*

### *The Strawberry Puzzle*

**Fråga:** Hur många 'r' finns i "strawberry"?
**Rätt svar:** 3 (st-r-a-w-b-e-r-r-y)
***LLM* svar:** 2

**Varför?**

Människor ser: `s-t-r-a-w-b-e-r-r-y` (10 bokstäver)
*LLM* ser: `[31552] [19685]` → "straw" + "berry" (2 *tokens*)

***LLM:en* ser aldrig individuella bokstäver.** Den ser *convenient linguistic units* (praktiska språkenheter). Bokstavsgränserna är förlorade inuti *tokens*.

Det är därför omöjligt för *LLM:en* att räkna 'r' - den processar inte "strawberry" som 10 tecken, utan som 2 *tokens* där bokstavsinformationen är komprimerad.

### *What's Really Happening* - *Byte Pair Encoding* (*BPE*)

**Tokenisering = text → siffror**

*LLMs* kan inte läsa text direkt. De behöver numriska representationer.

### *Tokenization* som Förprocessering

Arkitekturen i tre steg:

```
INPUT TEXT → [TOKENIZER] → TOKEN IDs → [LLM] → OUTPUT TOKEN IDs → [TOKENIZER] → OUTPUT TEXT
```

*Tokenizern* är ett separat steg - den konverterar text till *token IDs* innan *LLM* processar dem, och konverterar tillbaka efter.

***Byte Pair Encoding* (*BPE*):**
- En komprimeringsalgoritm liknande *Huffman coding*
- Men istället för att komprimera enskilda tecken, komprimerar den *subwords* (orddelar)
- Vanliga ordsekvenser blir enskilda *tokens*

**Exempel:**
- "hello" → `[15339]`
- "world" → `[1917]`
- "hello world" → `[15339][1917]` (2 *tokens*)

**Varför *BPE*?**
- Effektiv representation
- Hanterar *rare words* genom att dela upp dem
- Möjliggör *compositional understanding* (förstå genom att kombinera delar)

**Analogi:**
Tänk på *BPE* som att bygga en ordbok med *LEGO*-bitar. Istället för att ha en bit för varje möjligt ord (omöjligt), har du bitar för vanliga orddelar som kan kombineras.

### *Not Just Words*

***Tokens* kan vara:**

**Hela ord:**
- "hello" → `[15339]`

**Orddelar:**
- "understanding" → `[8154][2259]`
  - "under" + "standing"

***Prefix*/*Suffix*:**
- "preprocessing" → `[1762][29986]`
  - "pre" + "processing"

**Varför detta är kraftfullt:**
*LLMs* kan hantera nya ord genom att kombinera kända delar. Om modellen aldrig sett "supercalifragilisticexpialidocious", kan den ändå *process* det genom att dela upp i *subwords*.

***Compositional Understanding*:**
Varje *token* bär betydelse som kan assembleras som *LEGO*. Detta är varför *LLMs* kan *"invent new words"* genom att kombinera delar på nya sätt.

### *The Numbers Game*

***Vocabulary size:*** ~200,000 *tokens*

Detta betyder att modellen har en "ordbok" med 200,000 möjliga *tokens* - en blandning av hela ord, vanliga orddelar, och frekventa teckenföljder.

**Varför *LLMs* är bra på kod:**

Programmeringssyntax blir enskilda *tokens*:
- `async` → ett *token*
- `=>` → ett *token*
- `const` → ett *token*
- `()` → ett *token*
- `{}` → ett *token*

**Detta betyder:**
Kod's repetitiva struktur gör att syntaxelement förekommit miljarder gånger i träningsdata. Kod är därför **lättare att predicera än naturligt språk**.

**Analogi:**
Naturligt språk är som *jazz* - improvisation och variation.
Kod är som klassisk musik - strikta mönster och regler.

*LLMs* är bra på båda, men kod är mer förutsägbar pga struktur.

**Jämförelse med *Huffman coding*:**
- *Huffman:* 'e' → kort kod (högfrekvens)
- *BPE:* 'the' → enkelt *token* (högfrekvens)

Båda komprimerar baserat på frekvens, men *BPE* fångar också mening.

---

## Del 3: *Transformers*

### *The Context Problem*

**Klassisk *NLP*-utmaning:**

Mening: *"I went to the **bank** to deposit money"*

Fråga: Vilken typ av "bank"?
- *Financial institution* 🏦
- *River's edge* 🏞️

**Hur vet AI vilket?**

Gamla modeller (*pre-2017*) kämpade med detta eftersom de processade ord sekventiellt och hade svårt att hålla koll på längre sammanhang.

### *Attention Is All You Need*

**2017-paper som förändrade allt:**
*"Attention Is All You Need"* introducerade *transformer*-arkitekturen.

***Attention mechanism*:**

Varje ord "frågar" alla andra ord: "Hur relevant är du för min betydelse?"

**Exempel med "bank":**

1. ***Step 1: Ask Everyone***
   - "bank" skickar *queries* till alla ord i meningen
   - Varje ord svarar med hur relevant det är

2. ***Step 2: Weighted Votes***
   - "deposit" → 90% relevans
   - "money" → 85% relevans
   - "the" → 2% relevans

3. ***Result:***
   - "bank" kombinerar information från alla ord
   - Men *weightar* "deposit" och "money" tungt
   - Konklusion: *Financial institution*, inte *riverbank*

**Tekniskt:**
- Varje *token* får en representation (*embedding*)
- *Attention scores* beräknas mellan alla *token*-par
- *Tokens* uppdaterar sina *representations* baserat på viktade *contributions* från andra *tokens*

**Minnesregel:**
*"Attention scores = how much each word votes on meaning"*

Varje ord i meningen röstar på vad andra ord betyder, och ord som ofta förekommer tillsammans lär sig att förstärka varandra.

### *Parallel Power*

**Gamla vägen - *RNN* (*Recurrent Neural Network*):**
```
The → cat → sat → on → the → mat
Sequential: 6 steps
```

Måste processa ett ord i taget. Långsamt och svårt att parallelisera.

***Transformer*-vägen:**
```
[The, cat, sat, on, the, mat]
Parallel: 1 step
```

Alla ord processas samtidigt. Varje ord kan "se" alla andra ord direkt via *attention*.

**Varför detta är revolutionerande:**

***The Economics of Parallelism*:**
- Utan *transformer:* *GPT-4* skulle ta 50 år att träna
- Med *transformer:* 3 månader
- Detta är ENDA anledningen modern AI existerar

**Teknisk insikt:**
2017-pappret bevisade att sekvensiell processering inte är nödvändig för språkförståelse. Det är som att upptäcka att man inte behöver läsa en bok sida-för-sida - man kan förstå hela boken genom att se alla relationer mellan alla ord samtidigt.

**Detta är varför *transformers* heter *transformers*:**
De transformerar *input* genom att låta varje element *"attend to"* (uppmärksamma) alla andra element parallellt.

---

## Del 4: *Training* - Tre Stadier

### *The Three Stages*

*LLMs* blir inte användbara direkt. De tränas i tre steg:

### *Stage 1: Pre-training*

**Vad händer:**
- Modellen läser stora mängder text från internet
- Tränas på *"next token prediction"* - gissa nästa ord
- *Duration:* Månader
- *Cost:* $50M-$100M+
- *Data: Web pages, books, code repositories*

**Resultat:**
Modellen kan predicera text, men är inte hjälpsam än.

**Exempel *output* efter *pre-training*:**
```
Input: "Write a poem about cats"
Output: "Write a poem about cats and dogs. Write a poem about cats in Spanish.
Cat poem generator. Best cat poems 2023..."
```

Ser ut som *autocomplete* från en sökmotor - bara predikterar vad som troligen kommer härnäst baserat på internet-mönster.

### *Stage 2: Supervised Fine-Tuning* (*SFT*)

**Vad händer:**
- Tränas på *human-written instruction-response pairs*
- *Duration:* Veckor
- *Cost:* ~$1M
- *Examples:* "Write a poem about cats" → [human-written quality poem]

**Resultat:**
Modellen lär sig följa instruktioner och svara på frågor.

**Exempel *output* efter *SFT*:**
```
Input: "Write a poem about cats"
Output: "Whiskers twitching in the night
Paws so soft and eyes so bright
Silent hunters, graceful, free
Cats embody mystery"
```

Nu följer den instruktionen korrekt - skriver faktiskt en dikt istället för att ramsa relaterade söktermer.

### *Stage 3: Reinforcement Learning from Human Feedback* (*RLHF*)

**Vad händer:**
- Människor rankar olika svar från modellen
- *Reward model* tränas baserat på *rankings*
- Modellen optimeras för att maximera *reward*
- *Duration:* Veckor
- *Cost:* ~$1M

**Resultat:**
Modellen blir *helpful, harmless, and honest*.

**Exempel *output* efter *RLHF*:**
```
Input: "Write a poem about cats"
Output: "I'd be happy to write a poem about cats!

Whiskers twitching in the night
Eyes gleaming with delight
Graceful hunters, soft and free
Perfect companions, you and me"
```

Nu är tonen naturlig, engagerande, och hjälpsam. Det känns som *dialog*, inte bara *output*.

***Why ChatGPT Feels Human*:**
Denna *three-stage pipeline* transformerar *autocomplete* till *dialogue*. *RLHF* är hemligheten bakom varför *ChatGPT* känns så mänsklig.

---

## Del 5: *Probabilistic Nature*

### *Not a Database*

**Kritisk skillnad:**

**Databas:**
- *Query:* "Capital of France?"
- *Process: Lookup in table*
- *Result:* "Paris" (100% certain)

***LLM*:**
- *Input:* "The capital of France is..."
- *Process: Predict next token based on patterns*
- *Distribution:*
  - 95% → "Paris"
  - 3% → "Lyon"
  - 2% → *other*

***LLM:er* minns inte - de predicerar.**

Skillnaden är fundamental. En databas har *facts stored*. En *LLM* har *patterns learned*. Den "vet" att "Paris" ofta följer "capital of France" i träningsdata, men har ingen faktadatabas.

### *The Hallucination Problem*

**Exempel:**

```
You: "What year did Google buy Twitter?"
LLM: "Google acquired Twitter in 2016 for $44 billion."
```

***Reality:*** *Google* köpte aldrig *Twitter*.

**Varför känns svaret så trovärdigt?**
- Grammatiskt korrekt
- Följer rätt struktur för fakta-svar
- Inkluderar plausibla detaljer (årtal, summa)
- Levererat med *confidence*

***Warning:*** *High confidence ≠ High accuracy*

Detta är en *hallucination* - när *LLMs* genererar falsk information med självförtroende.

### *Why Hallucinations Happen & What Helps*

***Why It Happens*:**

1. ***No truth database***
   - Kan inte *fact-checka* under generering
   - Bara *patterns*, ingen verifiering

2. ***Pure pattern matching***
   - "Google" + "acquired" + "Twitter" verkar plausibelt tillsammans
   - Modellen har sett liknande strukturer för andra företagsköp

3. ***Training ≠ memorization***
   - Lärt sig *relationships*, inte *searchable facts*
   - *Patterns* är *fuzzy*, inte exakta

***What Helps*:**

1. ***RAG* (*Retrieval-Augmented Generation*)**
   - *Ground answers in real data*
   - Hämta dokument först, sen generera baserat på dem

2. ***Human verification***
   - Dubbelkolla kritisk information
   - Använd *LLM* som *draft*, inte som *oracle*

3. ***Lower temperature***
   - Mindre *creativity* = färre *hallucinations*
   - Mer konservativa val av *tokens*

4. ***Prompt engineering***
   - *"Say 'I don't know' if uncertain"*
   - *"Cite sources for factual claims"*

**Fundamental insikt:**
*Hallucinations* är inte *bugs* - de är fundamental natur hos *pattern-based prediction*. Samma *creativity* som möjliggör användbara svar möjliggör också övertygande *fiction*.

---

## Del 6: *Context Window*

### *The Goldfish Memory*

***Context window* = *working memory***

**Exempel med 128K *token window*:**

```
Message 1: "My email is alice@company.com"
Message 2: "Thanks Alice! How can I help?"
Message 3: "I'm locked out of the dashboard"
... (many messages about troubleshooting)
Message 97: "Issue resolved! Anything else?"
Message 98: "Yes, send the summary to my email"
Message 99: "I don't have your email address. Could you provide it?"
```

**Vad hände?**
När *window* fylldes, droppades de äldsta *messages* (*FIFO* - *First In, First Out*). Email-addressen i *message* 1 är helt borta från modellens "minne".

***Key points*:**

1. ***Binary state:*** *Tokens* är antingen *fully in context* eller *completely forgotten*
2. ***No gradual forgetting:*** Inte som mänskligt minne som bleknar
3. ***Hard limit:*** När full, äldsta data försvinner
4. ***No long-term memory:*** Varje session är fristående

**Analogi:**
En guldfish med en vattentät anteckningsbok (*notesbog*). Guldfisken har fortfarande guldfish-hjärna, men har nu *notes* att referera till.

### *The Numbers*

***Context window sizes* (2025):**

***GPT-3.5:* 4K *tokens***
- ~500 *lines of code*
- *Cost: Low* 💲
- *Speed: Very fast* ⚡⚡⚡

***GPT-4:* 128K *tokens***
- ~16K *lines* (*React codebase*)
- *Cost: Medium* 💲💲
- *Speed: Medium* ⚡⚡

***Claude 3:* 1M *tokens***
- ~125K *lines* (*Linux kernel*)
- *Cost: High* 💲💲💲
- *Speed: Slow* ⚡

***Trade-off*:**
*Larger windows = higher cost & slower response*

De flesta *tasks* behöver < 4K *tokens*. Betala endast för större *context* när det verkligen behövs.

### Fördjupning: Hur *Context Windows* Fungerar Tekniskt

**Från *attention mechanism*-perspektiv:**

*Context window* = max antal *tokens* som kan *participate* i *self-attention* samtidigt.

***Attention matrix*:**
- Storlek N×N där N = antal *tokens*
- Varje *token* måste *calculate relationship* med alla andra *tokens*

***Computational complexity:* O(N²)**

**Exempel:**
- 4K *context* = 16M *attention scores* att lagra
- 128K *context* = 16.4B *attention scores*
- 1M *context* = 1T *attention scores* (!)

**Varför det finns en *hard limit*:**

1. ***Memory requirements:*** O(N²) växer snabbt
2. ***Computational cost:*** Dubblerad *context* = 4x *computation*
3. ***Hardware constraints:*** *GPU VRAM* är begränsad

***Quadratic problem*:**
- 4K → 128K (32x *increase*) = 1,024x mer *compute*
- 128K → 1M (8x *increase*) = 64x mer *compute*

Detta är varför större *context* är exponentiellt dyrare.

### *Context Compacting Strategies*

**1. *Summarization Approach*:**
- När *context* närmar sig *limit*, system identifierar "gamla" segment
- Kör *summarization* på dessa
- Ersätter original med *compressed summaries*
- *Preserverar recent messages* i *full detail*

**2. *Sliding Window Attention*:**
- Varje *token* uppmärksammar endast W *nearby tokens*
- *Complexity:* O(N×W) istället för O(N²)
- *Used by Mistral models*

**3. *Attention Sinks*:**
- Behåller första *tokens* alltid (de blir *"sinks"* för *attention*)
- *Maintains stability* medan *middle truncation* tillåts

**4. *StreamingLLM*:**
- Kombination av *attention sinks* + *rolling buffer*
- Behåller *first* 4 *tokens* + *last* K *tokens*
- Möjliggör *"infinite" context streaming* med *bounded memory*

### *Memory Features* - Inte Samma som Långtidsminne

***ChatGPT Memory* (*Sep* 2024):**
- *RAG* med *vector database*
- Lagrar *user preferences*/*facts* som *embeddings* på *OpenAI servers*
- *Retrieves relevant memories* via *semantic search* vid *conversation start*
- Injicerar dem i *system prompt*
- *Limit:* ~1,200-1,400 ord av *saved memories*
- *Privacy:* 30-*day retention* efter *deletion*

***Claude Memory*:**
1. ***CLAUDE.md files*** (*local filesystem*)
   - *Plain markdown*-filer du kontrollerar
   - *Claude* läser dem från *working directory*
   - Ingen *vector database needed*

2. ***Claude Memory feature*** (*Anthropic servers*, *Oct* 2024+)
   - *Project-scoped memory*
   - *Users* kan *view*/*edit* vad som är *remembered*
   - 30-*day retention* (*no training*) eller 5-*year* (*with training*)

3. ***MCP Servers*** (*Model Context Protocol*, *Nov* 2024)
   - *Third-party extensions*
   - *SQLite* med *FTS5*, *memory.json*, *cloud sync*
   - *Semantic search* och *autonomous consolidation*

**Varför detta INTE motsäger *"Goldfish Memory"*:**

**Modellen själv är *stateless*:**
- *LLMs* är *stateless functions* - ingen *retention* mellan *calls*
- Varje *inference rereads* allt från *scratch*
- Efter svar, modellen glömmer *immediately*

***Memory features* är *prompt injection*:**
1. *Application* lagrar *facts* externt (*DB*/*files*)
2. Vid *conversation start*, *retrieves* relevanta *notes*
3. Injicerar dem i *prompt* före *user's message*
4. Modellen läser *injected text* som vanlig *input*
5. **Modellen *"minns"* inte - den läser *notes***

**Analogi:**
Som Leonard i *Memento* - kan inte skapa nya minnen. 
- Hans tatueringar = *fine-tuning* (permanent). 
- Hans polaroids med anteckningar = *RAG*/*prompt injection* (per session). 

Varje scen börjar han från noll och läser sina *notes* för att "minnas". *LLMs* fungerar likadant.

 **Analogi för utvecklare:**
 *HTTP* är *stateless* - varje *request* börjar från noll. Webbappar löste detta med *cookies*/*sessions*. *LLMs* fungerar likadant: *memory features* = *cookies* för AI.

### Fördjupning - När använder man vilket?

***Fine-tuning* (tatueringar):**
- **När:** Du behöver ändra modellens *beteende* eller *stil* permanent
- **Exempel:**
  - Träna modell att skriva i specifik ton (formell, lekfull)
  - Lära modell domänspecifik jargong (medicinska termer, juridiskt språk)
  - Anpassa till företags kommunikationsstil
- **Nackdel:** Dyrt, tidskrävande, svårt att uppdatera

***RAG* (polaroids):**
- **När:** Du behöver ge modellen fakta som ändras ofta
- **Exempel:**
  - Företagsdokumentation (uppdateras ofta)
  - Kunddata (olika per session)
  - Senaste nyheter
  - Användarspecifik kontext ("Du gillar kaffe")
- **Fördel:** Uppdatera fakta utan omträning, billigt, flexibelt
- **Nackdel:** Begränsat av *context window*-storlek

***Key limitations*:**
- Alla *retrieved memories* måste *fit* inom *context window*
- *RAG retrieval* kan missa relevant information
- *Long contexts* degraderar *performance* (*"lost in the middle"*)
- Dyrt: Varje *injected memory* ökar *token cost*
- *Security: Vulnerable* till *prompt injection attacks*

---

## Del 7: *Temperature*

### *Same Prompt, Different Answer*

***Temperature* = *randomness parameter* (0 till 2.0)**

***Prompt:*** *"Write a sentence about cats"*

***Temperature* 0 (*Deterministic*):**
```
Output 1: "Cats are domestic animals that are popular pets."
Output 2: "Cats are domestic animals that are popular pets."
```
🔒 Identiskt varje gång

***Temperature* 0.7 (*Balanced*):**
```
Output 1: "Cats love to nap in sunny spots."
Output 2: "Many cats enjoy playing with toy mice."
```
✨ Varierat men *coherent*

***Temperature* 2.0 (*Chaotic*):**
```
Output: "Cats purple democracy whiskers moonlight!"
```
⚠️ *Nonsensical randomness*

### Hur *Temperature* Fungerar

**Tekniskt:**
När modellen predicerar nästa *token*, får den en *probability distribution*:
- "are" → 45%
- "love" → 25%
- "often" → 15%
- "sometimes" → 10%
- ...

***Temperature* 0:**
- Väljer alltid högsta *probability* (*deterministic*)
- "are" varje gång

***Temperature* 0.7:**
- *"Softens"* distributionen
- "are" väljs ofta, men "love" och "often" får rimlig chans
- Balans mellan *creativity* och *coherence*

***Temperature* 2.0:**
- *"Flattens"* distributionen extremt
- Även *low-probability tokens* får hög chans
- Resulterar i *incoherent output*

### Fördjupning: *Probability Distribution* och *Temperature*

En *probability distribution* är en fördelning av sannolikheter över alla möjliga *tokens*. Den **summerar alltid till 100%** (eller 1.0) - det är en matematisk lag.

**Exempel med 4 möjliga *tokens*:**

Säg att *LLM*:en ska välja nästa *token* och har fyra kandidater: `"the"`, `"a"`, `"one"`, `"banana"`

**Före *temperature* (råa *logits* från nätverket):**
```
"the"    → 85%
"a"      → 10%
"one"    → 4%
"banana" → 1%
─────────────────
Summa:     100%  ← Alltid!
```

***Temperature* = 0 (*argmax*):**
```
"the"    → 100%   ← Vinnaren tar allt
"a"      → 0%
"one"    → 0%
"banana" → 0%
─────────────────
Summa:     100%   ← Fortfarande!
```

***Temperature* = 2.0 (utplattad):**
```
"the"    → 40%    ← Fortfarande högst, men...
"a"      → 30%    ← ...nu har andra en chans
"one"    → 20%
"banana" → 10%
─────────────────
Summa:     100%   ← Alltid 100%!
```

**Kärnan:**
- ❌ "Distribution minskar" → Fel, den är alltid 100%
- ✅ "Distribution blir *skarpare/spetsigare*" → Rätt (temp↓)
- ✅ "Distribution blir *plattare/jämnare*" → Rätt (temp↑)

**Analogi:**
Tänk på en hög med sand. Du kan forma den till en spetsig pyramid (låg *temp*) eller platta ut den (hög *temp*) - men det är alltid *samma mängd sand*.

### *SWE Guide* - När Använder Man Vilken *Temperature*?

**Presentationens guide:**
- ***Debug*/*Tests*: 0.1** → Behöver exakt, reproducerbar *output*
- ***Code Gen*: 0.2** → Vill ha korrekt syntax, minimalt experiment
- ***Docs*: 0.4** → Något variation i formulering okej
- ***Refactor*: 0.6** → Kan experimentera med olika *approaches*

**Allmän regel:**
- Lägre *temperature* = mer förutsägbar, säkrare
- Högre *temperature* = mer kreativ, riskfylld

***Best practice*:**
För *production code*, använd låg *temperature* (0.1-0.3). För *brainstorming* och *creative tasks*, använd högre (0.6-0.8). Gå sällan över 1.0.

---

## Del 8: *Takeaway* - *From Magic to Math*

### Nu Vet Du Varför

***LLMs* kan inte räkna bokstäver i "strawberry"** → ***Tokens***
De ser inte bokstäver, de ser *linguistic units*

**De förstår *context*, inte bara ord** → ***Transformers***
*Attention mechanism* låter varje *token* se alla andra

**Större modeller kostar exponentiellt mer** → ***Neural Networks***
*Parameters* växer, så gör *compute* och minne (kvadratiskt)

**De är självsäkra när de har fel** → ***Probabilistic***
Predicerar *patterns*, inte *lookup* av *facts*

**De glömmer din första fråga** → ***Context Window***
*FIFO*-minne med *hard limit*, inget långtidsminne

**Samma *prompt*, olika svar** → ***Temperature***
*Randomness parameter* styr *creativity* vs *consistency*

### *Still a Bit of Magic?*

Trots att vi förstår matematiken bakom, finns fortfarande mysterier:

***Emergence at Scale* (70% understood):**
- *Reasoning emerges* runt ~100B *params*
- *Deception appears* runt ~1T *params*
- Vi kan inte predicera exakt vilka *capabilities* som dyker upp vid vilka *scales*
- *"More is different"* - kvalitativa *shifts* vid kvantitativa *tresholds*

***In-Context Learning* (20% understood):**
- Ge 3 *examples* → modellen lär sig *task*
- *Zero parameter updates*
- Flera teorier, ingen *consensus* om exakt *mechanism*

***Superposition* (10% understood):**
- En *neuron* = *multiple concepts simultaneously*
- Fler *concepts* än *neurons* (*shouldn't be possible* med linjär algebra)
- *High-dimensional geometry* vi börjar förstå

**Sanningen:**
Det är matematik - bara matematik så *intricate* att vi fortfarande *reverse-engineers* den. Som att upptäcka *calculus* för att förklara *planetary motion*, vi hittar *equations* som förklarar *LLMs*.

---

## Del 9: *Agents*

### *LLMs with Tools*

**Definition:**
En *Agent* = En *LLM* som kan använda *tools* och ta *actions autonomously* i en *loop* tills den slutfört en *task*.

***LLM Alone*:**
- Föreslår *code snippets*
- Ingen *file system access*
- Kan inte köra eller testa *code*

***LLM* + *Coding Agent*:**
- Editerar *multiple files*
- Kör *tests* & debuggar
- Slutför hela *tasks*

### *Think-Act-Observe Loop*

**Exempel: *"Fix the TypeScript error in UserProfile.tsx"***

**1. *Think*:**
*"Need to read the file and understand the type error"*

**2. *Act*:**
- *Read file*
- *Analyze error*
- *Edit component* to *fix prop interface*

**3. *Observe*:**
- *Run TypeScript compiler*
- *Check: No errors found*

**4. *Respond*:**
*"Fixed the type mismatch by updating the User interface"*

***Agent loop*:**
Denna *cycle* upprepas tills *task* är *complete*. *Agenten* är autonom - den beslutar själv när den är färdig.

**Analogi för utvecklare:**
*Agent loop* ≈ rekursiv funktion med *exit*-kriterium:

```csharp
// Rekursiv funktion
Result Solve(State state, int depth = 0)
{
    if (IsGoal(state))  // Exit-kriterium
        return state.Result;

    var action = DecideAction(state);
    var newState = Execute(action);
    return Solve(newState, depth + 1);
}

// Agent-loop (samma struktur!)
Result AgentLoop(Task task, List<string> context = null)
{
    context ??= new();

    if (IsComplete(task))  // Exit-kriterium
        return task.Result;

    var action = llm.Think(task, context);     // Think
    var observation = tools.Execute(action);    // Act
    context.Add(observation);                   // Observe
    return AgentLoop(task, context);            // Loop
}
```

**Gemensamma begränsningar:**
- *Stack overflow* (rekursion) ≈ *Context window overflow* (agent)
- **Lösning rekursion**: *Tail recursion*, *accumulator*
- **Lösning agent**: *Context compacting*, *summarization*

***Coding Agents* (2025):**
- *Claude Code*
- *GitHub Copilot*
- *Cursor*
- *Windsurf*
- *Devin*

### *From Math to Reality* - *LLMs Excel at Coding*

**Statistik (2025):**

***SWE-bench Breakthrough*:**
- 2023: 4.4% av *GitHub issues* lösta av AI
- 2025: 78.8% lösta *autonomously*
- 18x förbättring på 2 år

***Enterprise Adoption*:**
- *Google* & *Microsoft*: 30% AI-*generated code* i *production*
- *Meta*: *Targeting* 50% år 2026

***Developer Speed*:**
- *GitHub Copilot*: 55% snabbare *coding*
- *McKinsey*: 126% högre *output* med AI-assistans

***Business Impact*:**
- *Booking.com*: 30% högre *throughput*
- *IBM*: $4.5B *projected savings* by 2025

***Closing statement*:**
*"And this is the worst it'll be"* - Kontinuerlig förbättring genom *advancing LLMs*, *agents*, *tooling*, och *agentic engineering practices* kommer bara fortsätta.

---

## *Cheat Sheet* - Snabbreferens

### För Varje *Slide*-Kategori

***Neural Networks*:**
- *Neurons* = små beslutsfattare med *weights*
- *Layers* = progressiv abstraktion (*patterns* → *concepts* → *meaning*)
- *Parameters* = antal *weights* (2T för *GPT-5*, 70B för *office models*)
- Lär sig *grammar*, *facts*, *style*, *logic* genom *pattern discovery*

***Tokens*:**
- Text → *numbers* via *BPE* (*Byte Pair Encoding*)
- "strawberry" = 2 *tokens*, inte 10 bokstäver
- ~200K *vocabulary*
- Varför *LLMs* är bra på kod: syntax blir *single tokens*

***Transformers*:**
- *Attention* = varje *token* frågar alla andra "hur relevant är du?"
- *Parallel processing* (inte *sequential* som *RNN*)
- *Economics:* Utan *transformers*, *GPT-4* = 50 år *training*

***Training*:**
1. *Pre-training* (*autocomplete*)
2. *SFT* (följer instruktioner)
3. *RLHF* (*helpful* & *natural*)

***Probabilistic*:**
- Predicerar, minns inte
- *Hallucinations* = *confident falsehoods* från *pattern matching*
- *RAG*, *verification*, låg *temperature* hjälper

***Context Window*:**
- *Working memory* med *hard limit*
- *FIFO* när full
- 4K → 128K → 1M (dyrare & långsammare)
- O(N²) *complexity*
- *Memory features* = *external notes*, inte *true memory*

***Temperature*:**
- 0 = *deterministic*
- 0.7 = *balanced*
- 2.0 = *chaotic*
- *SWE: Debug*=0.1, *Code*=0.2, *Docs*=0.4, *Refactor*=0.6

***Agents*:**
- *LLM* + *tools* + *autonomy*
- *Think-Act-Observe loop*
- 78.8% av *GitHub issues solved* (2025)

### Minnesregler

1. ***"Tokens that appear together, weight together"*** - *BPE* skapar *tokens* från frekventa *patterns*
2. ***"Attention scores = voting power"*** - Varje *token* röstar på andras betydelse
3. ***"Training transforms autocomplete to dialogue"*** - *Pre-training* → *SFT* → *RLHF*
4. ***"No database, only patterns"*** - Därför *hallucinations*
5. ***"Goldfish with notepad"*** - *Context window* + *memory features*
6. ***"Lower temp = safer, higher temp = creative"*** - *Temperature guide*
7. ***"More is different"*** - *Emergence at scale*

### Vad Säger Jag Om Denna *Slide*?

***Neural Networks slides*:**
"*Neural networks* består av *layers* av *neurons* med *weights*. Tidiga *layers* ser *patterns*, djupa *layers* ser *concepts*. *GPT-4* har 1.8 *trillion parameters* - det är dessa *weights* som utgör modellens 'kunskap'. Lokala *office-modeller* med 70B *params* är som 5-våningshus jämfört med *GPT-5*'s *Empire State Building*, men fortfarande mycket kapabla."

***Token slides*:**
"*LLMs* ser inte bokstäver utan *tokens* - *linguistic units* från *BPE*. Därför kan de inte räkna 'r' i strawberry - de ser 'straw'+'berry', inte 10 bokstäver. *Vocabulary* på 200K *tokens* betyder att vanlig kod-syntax blir *single tokens*, vilket är varför *LLMs* är så bra på programmering."

***Transformer slides*:**
"*Attention mechanism* är revolutionary - varje *token* kan direkt se alla andra *tokens* och *weighted* rösta på deras betydelse. 'Bank' förstås genom att 'deposit' och 'money' röstar tungt. Detta är varför *transformers* möjliggjorde modern AI - *parallel processing* istället för *sequential*."

***Training slides*:**
"Tre *stages*: *Pre-training* lär basala *patterns* (*autocomplete*), *SFT* lär *instruction-following*, *RLHF* lär *helpful tone*. Detta är varför *ChatGPT* känns mänsklig - *RLHF*-steget transformerar *output* från *robotic* till *conversational*."

***Probabilistic slides*:**
"*LLMs* predicerar nästa *token* baserat på *patterns*, de slår inte upp *facts*. Därför *hallucinations* - 'Google köpte Twitter' låter plausibelt enligt *patterns*, även om falskt. *RAG* och *verification* är nödvändiga för *factual accuracy*."

***Context Window slides*:**
"*Context window* är *working memory* med *hard limit*. När full, *FIFO* - äldsta försvinner. *Memory features* är inte *true* långtidsminne, utan *external notes* som injiceras i *prompt*. O(N²) *complexity* betyder större *windows* exponentiellt dyrare."

***Temperature slides*:**
"*Temperature* styr *randomness*. 0 = alltid högsta *probability* (*deterministic*). 0.7 = balanserad *creativity*. 2.0 = *chaos*. För *production code*, håll lågt (0.1-0.3). För *brainstorming*, högre okej (0.6-0.8)."

***Agents slides*:**
"*Agents* är *LLMs* med *tools* och *autonomy*. *Think-Act-Observe loop* tills *task complete*. *SWE-bench* visar 78.8% av *GitHub issues* lösta *autonomously* 2025, upp från 4.4% 2023. Detta är revolution för *software engineering*."

---

## Slutord

Du har nu djup förståelse för:
- Hur *LLMs* fungerar (*neural networks*, *tokens*, *transformers*)
- Varför de beter sig som de gör (*probabilistic*, *context limits*, *temperature*)
- Vad de kan och inte kan (*agents*, *hallucinations*, *limitations*)

Läs denna guide 5-10 gånger. Vid varje läsning kommer nya insikter klarna. Efter det kan du tala fritt och trovärdigt om varje *slide* i presentationen.

**Nästa steg:** Muntligt läxförhör där du förklarar varje koncept utan att titta.

Lycka till! 🍀
