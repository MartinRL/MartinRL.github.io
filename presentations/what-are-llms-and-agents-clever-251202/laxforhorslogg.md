# Läxförhörslogg: LLMs & Agents

## Session 2025-11-28

### Fråga 1 (Nivå 2) - 2025-11-28 15:30
**Fråga:** Varför kan en LLM inte räkna hur många gånger bokstaven "r" förekommer i ordet "strawberry"?

**Svar:** En llm "tänker" inte i termen ord, utan är helt baserad på tokens. i fallet strawberry är straw och berry två olika tokens och antalet r har i detta fall tagits från andra token berry.

**Bedömning:** ✅ Korrekt (grund)
- ✅ Förstår att LLMs arbetar med tokens, inte bokstäver
- ✅ Förstår att "strawberry" delas upp i flera tokens
- ⚠️ Kunde fördjupat med: BPE-algoritmen, att tokenization sker före modellen, att modellen ser numeriska IDs

**Fördjupning given:**
- Tokenizern är separat från LLM:en och körs före/efter
- LLM:en ser endast numeriska token-IDs, aldrig råtext
- BPE-algoritmen skapar vocabulary, sedan frusen
- Analogi: Som att läsa kinesiska tecken översatta till siffror

---

### Fråga 2 (Nivå 1) - 2025-11-28 15:35
**Fråga:** Vad är skillnaden mellan *pre-training*, *SFT* och *RLHF* i träningsprocessen?

**Svar:** pre-training: typ hela internet, bibliotek, och övr. tillgänglig text. tar lång tid (månader) och kostar mkt (upp emot 100 M US$). ger en "rå" opersonlig deterministisk llm som svarar likadant på samma input. SFT: supervised fine-tuning, tar veckor och bygger på mänskliga exempel. nu får modellen ett mer mänskligt beteende och är inte längre deterministisk. RLHF: re-enforced learning with human feedback. tar veckor och bygger på feedback från människor eller en reward model människor har skapat. nu skapas weights djupare nede i lagren i det neurala nätverket och llm:en kan svara i princip mänskligt.

**Bedömning:** ⚠️ Delvis korrekt
- ✅ Pre-training: Korrekt (datamängd, tid, kostnad)
- ❌ SFT: Fel koppling mellan determinism och träningssteg. Determinism styrs av *temperature*, inte träningssteg. *SFT* ger fråga-svar-format, inte determinism.
- ❌ RLHF: "Weights djupare nede i lagren" är felaktigt. Alla tre steg justerar *weights* genom hela nätverket. Skillnaden är målfunktionen (*reward maximization* vs *prediction error* vs *imitation*).

**Korrekt svar:**
- *Pre-training*: Internet-skala data → "autocomplete-papegoja" (kan språk, saknar fråga-svar-format)
- *SFT*: Mänskliga exempel → fråga-svar-format (hjälpsam assistent)
- *RLHF*: Reward-signal från människor → preferenser (säker, trevlig)
- **Minnesregel:** "Raw → Helpful → Safe"
- **Viktigt:** Determinism styrs av *temperature* (0 = deterministisk, >0 = slumpmässig), inte av träningssteg

---

### Fråga 3 (Nivå 2) - 2025-11-28 15:45
**Fråga:** Varför kostar längre *context windows* kvadratiskt mer att beräkna? Vad är det i *transformer*-arkitekturen som orsakar O(N²)?

**Svar:** O(N²) orsakas av att "attention" kräver att tokens frågar tokens, alltså ökar mängden kvadratiskt

**Bedömning:** ✅ Korrekt (kärnkonceptet)
- ✅ *Attention* är orsaken till O(N²)
- ✅ Tokens måste jämföras med varandra (*"tokens frågar tokens"*)
- ✅ Detta skapar kvadratisk komplexitet

**Fördjupning given:**
- **Exakt mekanism**: Varje token beräknar en *attention score* mot **alla andra tokens** i *context window*
- **Matematiken**:
  - 10 tokens → 10 × 10 = 100 jämförelser
  - 100 tokens → 100 × 100 = 10,000 jämförelser (100× mer arbete för 10× fler tokens)
  - 1000 tokens → 1,000,000 jämförelser
- **Varför nödvändigt**: *Self-attention* behöver se hela kontexten för att förstå samband (t.ex. "bank" = pengar eller flod?)
- **Konsekvens**: Dubblera *context window* → 4× beräkningskostnad
- **Minnesregel**: "Varje ny token måste 'fråga' alla tidigare tokens: Dubbla längden = fyra gånger kostnaden"

---

### Fråga 4 (Nivå 3) - 2025-11-28 16:41
**Fråga:** Förklara *hallucinations* med *Memento*-analogin. Varför "hittar" LLMs på fakta, och hur relaterar det till att de är probabilistiska modeller?

**Svar:** Jag förstår inte hallucinations med Memento-analogin. Den handlar ju om att minnet försvinner när kontextfönstret försvinner. Eftersom en LLM förutser nästa token, med eller utan SFT och/eller RLHF, så kan den begå fel då det neurala nätverket och dets vikter och temperatur väljer nästa token utifrån tidigare. Det handlar helt enkelt om sannolikheter inte sanningar.

**Bedömning:** ✅ Korrekt (utmärkt förståelse + ifrågasatte felaktig frågeställning!)
- ✅ Identifierade att *Memento*-analogin handlar om *context window*, inte *hallucinations*
- ✅ Förstår att *hallucinations* orsakas av probabilistisk token-förutsägelse
- ✅ "Sannolikheter, inte sanningar" - perfekt sammanfattning
- ✅ Förstår att *weights* och *temperature* styr valet, inte faktakontroll
- ✅ Kritiskt tänkande - ifrågasatte en dåligt formulerad fråga

**Kommentar:**
Frågan var felaktigt formulerad. *Memento*-analogin illustrerar *context window* / *memory features*, inte *hallucinations*.

**Korrekt förklaring av hallucinations:**
- LLM:en "vet" inte vad som är sant - den har lärt sig **mönster**
- Vid varje steg: "Vilket token är mest sannolikt härnäst?"
- Om träningsdata har felaktiga mönster → självsäker hallucination
- **Bättre analogi**: Expert improvisatör som läst tusentals manus. Fråga om en film hen aldrig sett → skapar trovärdigt svar från liknande mönster. Låter rätt, men är påhittat.

---

### Fråga 5 (Nivå 2) - 2025-11-28 16:48
**Fråga:** Vad är skillnaden mellan *RAG* (*Retrieval-Augmented Generation*) och *fine-tuning*? När skulle du använda det ena över det andra?

**Svar:** fine-tuning sker som en del av processen att skapa en färdig LLM och är där för evigt (tatuering) medan RAG är ekstern information/dokumentation som används för berika kontexten efter behov (titta på ett foto)

**Bedömning:** ✅ Korrekt (kärnkonceptet + analogi!)
- ✅ *Fine-tuning* är permanent (*"där för evigt"*) = tatueringar
- ✅ *RAG* är extern information som injiceras vid behov = polaroids
- ✅ *Fine-tuning* modifierar *weights* under träning
- ✅ *RAG* berikar kontext dynamiskt per session

**Fördjupning - När använder man vilket?**

**Fine-tuning (tatueringar):**
- **När**: Ändra modellens *beteende* eller *stil* permanent
- **Exempel**: Träna specifik ton, domänjargong, företagsstil
- **Nackdel**: Dyrt, tidskrävande, svårt att uppdatera

**RAG (polaroids):**
- **När**: Ge modellen *fakta* som ändras ofta
- **Exempel**: Dokumentation, kunddata, senaste nyheter, användarkontext
- **Fördel**: Uppdatera utan omträning, billigt, flexibelt
- **Nackdel**: Begränsat av *context window*

**Minnesregel:**
- *Fine-tuning* = ändra modellens DNA (permanent)
- *RAG* = ge modellen en faktabok att titta i (tillfällig)
- **Hybrid**: Ofta båda! *Fine-tune* för stil, *RAG* för fakta

---

### Fråga 6 (Nivå 1) - 2025-11-28 16:55
**Fråga:** Vad är en *agent* i AI-sammanhang? Hur skiljer sig en agent från en vanlig LLM?

**Svar:** en llm tar input och ger output. en agent är en llm med verktyg i en loop. är du enig i att en agent kan jämföras med en rekursiv funktion med exit-kriterium som första koll? vidare har en rekursiv det problem att stacken kan fyllas upp, liksom ett kontekstfönster (båda kan undvikas med trix som en tillståndsparameter till funktionen och compacting av kontextföstret)

**Bedömning:** ✅ Korrekt (utmärkt analogi + djupförståelse!)
- ✅ LLM = input → output (stateless funktion)
- ✅ Agent = LLM + verktyg i loop (*Think-Act-Observe*)
- ✅ **Briljant analogi**: Agent ≈ rekursiv funktion med exit-kriterium
- ✅ Identifierade gemensamma begränsningar:
  - Rekursion: Stack overflow-risk
  - Agent: *Context window* overflow-risk
- ✅ Lösningar parallellt:
  - Rekursion: Tillståndsparameter (tail recursion, accumulator)
  - Agent: *Context compacting* / *summarization*

**Fördjupning - Rekursionsanalogin:**
```python
# Rekursiv funktion
def solve(state, depth=0):
    if is_goal(state):  # Exit-kriterium
        return state
    action = decide_action(state)
    new_state = execute(action)
    return solve(new_state, depth+1)

# Agent-loop (samma struktur!)
def agent_loop(task, context=[]):
    if is_complete(task):  # Exit-kriterium
        return result
    action = llm.think(task, context)  # Think
    observation = tools.execute(action)  # Act
    context.append(observation)  # Observe
    return agent_loop(task, context)  # Loop
```

**Exit-kriterier för agenter:**
- Uppgiften klar
- Max iterationer nådd (säkerhetsnät)
- *Context window* full
- Fel uppstår

**Minnesregel:**
- **LLM**: Enkel funktion - kalla, få svar
- **Agent**: Rekursiv loop - tänk, agera, observera, repeat

**Kommentar:** Exceptionell förståelse genom att koppla AI-koncept till datastrukturer och algoritmik!

---

### Fråga 7 (Nivå 2) - 2025-11-30
**Fråga:** Förklara vad *temperature* gör tekniskt. Om du ställer in temperature=0, temperature=0.7 och temperature=2.0 - vad händer med *probability distribution* över nästa token i varje fall?

**Första svar:** "*probability distribution* minskar ju lägre tempen sätts. sätt den exempelvis till lägre för att skapa programkod än romanskrivande"

**Bedömning första svar:** ⚠️ Delvis korrekt
- ✅ Rätt intuition: Lägre temperature → mer förutsägbar output
- ✅ Rätt tillämpning: Kod kräver lägre temp än kreativt skrivande
- ❌ **Tekniskt oprecist**: "Probability distribution minskar" är inte korrekt formulering. Distributionen finns alltid och summerar till 100% - det är *formen* som ändras.

**Fördjupning given:**
- *Probability distribution* summerar **alltid** till 100%
- temp=0: Kollapsar till *argmax* - högsta sannolikheten får 100%, övriga 0%
- temp=0.7: Skärper distributionen - topptokens får högre relativ sannolikhet
- temp=2.0: Plattar ut distributionen - alla tokens får mer lika sannolikhet
- **Analogi**: Sandhög - kan formas till pyramid (låg temp) eller plattas ut (hög temp), men samma mängd sand

**Uppföljningsfråga:** Varför ger temp=0 *deterministisk* output medan temp>0 ger *non-deterministic*?

**Uppföljningssvar:** "summan av sannolikhetsdistributionen är alltid 100%, men vid temp. 0 sätts värdet till 100% till den mest sannolika token, således får övriga 0% och samma resultat ges varje gång."

**Bedömning uppföljning:** ✅ Korrekt!
- ✅ Summan är alltid 100% - förstått
- ✅ temp=0 → *argmax* → högsta sannolikhet får 100%, övriga 0%
- ✅ Därför: samma input → samma output = **deterministisk**

**Kommentar:** Detta korrigerar missförståndet från fråga 2 där determinism felaktigt kopplades till träningssteg (*SFT*). Nu korrekt förståelse: **Determinism styrs av *temperature*, inte träningssteg.**

---

### Fråga 8 (Nivå 2) - 2025-11-30
**Fråga:** Vad är skillnaden mellan *neurons*, *layers*, *weights* och *parameters*? Hur hänger de ihop?

**Svar:** "en neuron tar input och ger output. jag är inte säker på hur och behöver din hjälp för att bättre förstå det. layers är som nyanser och varje token prediction går igenom samtliga lager, runt 100 stycken för en frontier model. kan tillföra nyanser som smak och humör. jag är osäker på skillnaden mellan weights och parameters. hjälp mig bättre förstå den! hjälp mig även förstå exakt hur en modell/llm tränas för att skapa dessa!"

**Bedömning:** ⚠️ Delvis korrekt
- ✅ Neuron: Rätt att den tar input och ger output
- ✅ Layers: Rätt att ~100 lager för frontier models, rätt intuition om "nyanser"
- ❌ Saknas: Hur neurons faktiskt fungerar (weights, summering, activation)
- ❌ Osäker på weights vs parameters

**Fördjupning given:**

**1. Hur en neuron fungerar:**
```
Inputs × Weights → Summering + bias → Activation function → Output
```
Analogi: Domare som viktar olika prestationer och ger totalpoäng.

**2. Weights = Parameters:**
- De är samma sak!
- *Weight* = enskild siffra som multipliceras med input
- *Parameter* = samlingsnamn för alla justerbara värden (weights + biases)
- 1.8T parameters = 1.8T justerbara siffror som ÄR modellens "kunskap"

**3. Hur weights tränas:**
1. *Forward pass*: Skicka in text, få prediction
2. Beräkna fel mot faktiskt nästa token
3. *Backpropagation*: Räkna ut varje weights bidrag till felet
4. Uppdatera weights med *gradient descent*
5. Repeat miljarder gånger

Formel: `ny_weight = gammal_weight - (learning_rate × gradient)`

Analogi: Mixer med 1.8T rattar - smaka, justera, repeat.

---

### Uppföljning Fråga 2 (Nivå 2) - 2025-11-30
**Fråga:** Förklara nu korrekt: Vad gör varje träningssteg (*pre-training*, *SFT*, *RLHF*) med modellen - och vad styr determinism?

**Svar:** "pre-training: som att läsa all fakta i en lärobok (men i detta fall hela internet, samtliga läropböcker, etc). SFT (supervised fine-tuning): mänskliga 'lablers' går igenom otaliga exempel på fråga och rimligt svar/assistans. som exemplena i en lärobok. RLHF (re-enforced learning with human feedback): kräver kanske 1 miljard exempel, så en reward-modell skapas som regel. som att iterara på problem i en lärobok (dock stor skillnad på RLHF för problem med känd lösning som schack eller go och exempelvis humor och hur bra ett skämt är)"

**Bedömning första del:** ✅ Korrekt
- ✅ Pre-training: Rätt - läsa all fakta (hela internet, böcker, kod)
- ✅ SFT: Rätt - mänskliga exempel på fråga→svar-par
- ✅ RLHF: Rätt - reward model pga skala, bra insikt om skillnad mellan objektiva (schack/go) och subjektiva (humor) domäner
- ❌ Missade att besvara: Vad styr determinism?

**Följdfråga:** Vad styr determinism - träningssteg eller något annat?

**Svar:** "temperatur"

**Bedömning följdfråga:** ✅ Korrekt!

**Kommentar:** Missförståndet från fråga 2 är nu helt korrigerat. Användaren förstår att:
- Träningsstegen (pre-training → SFT → RLHF) påverkar modellens *beteende* och *kvalitet*
- **Temperature** styr *determinism* (0 = deterministisk, >0 = stokastisk)

---

### Uppföljning Fråga 8 (Nivå 2) - 2025-11-30
**Fråga:** Förklara med egna ord: 1) Vad händer inuti en neuron? 2) Vad är skillnaden mellan *weight* och *parameter*?

**Svar:** "1. den tar input och alla sina vikter och ger utifrån dem output. som att en domare bedömer en prestation. 2. en vikt är en parameter. en bias är också en parameter. i ett OO-språk hade parameter varit superklass till de nedärvda klasserna vikt och bias."

**Bedömning:** ✅ Korrekt!
- ✅ Neuron: Input + weights → output, domaranalogin fungerar
- ⚠️ Kunde nämnt de 3 explicita stegen (summering → bias → activation), men kärnförståelsen finns
- ✅ **Weights vs Parameters**: Perfekt! Weight är en parameter, bias är också en parameter
- ✅ **OO-analogin utmärkt**: `Parameter` som basklass, `Weight` och `Bias` som subklasser

**Kommentar:** Gapet från fråga 8 är nu stängt. Användaren förstår relationen mellan weight/bias/parameter.

---
