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
