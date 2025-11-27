# Talepunkter: LLMs & Agents - Clever, 2. december 2025

**Format:** Bullet points til mundtlig præsentation (ikke hvad der står på plancherne!)

---

## KAPITEL 0: INTRO (3 min)

---

### Slide 1: Title - LLMs & Agents

**Kernebudskab:** Velkommen og setup forventninger

**Talepunkter:**
- Velkommen alle - glad for at være her hos Clever
- I dag skal vi demystificere AI - fjerne magien og vise matematikken
- Det bliver teknisk, men håndgribeligt
- Målet: I skal forstå HVORDAN det virker, ikke bare HVAD det kan

**Overgang:** "Lad os starte med hvorfor vi er her..."

---

### Slide 2: Purpose - From Magic to Math

**Kernebudskab:** AI ligner magi, men det ER matematik - som vi kan forstå

**Talepunkter:**
- Arthur C. Clarke citat - kender I det?
- Sådan føles AI lige nu: magisk, uforståeligt, måske lidt skræmmende
- Men: El var også "magi" indtil vi forstod fysikken
- Computere var "tænkende maskiner" indtil vi forstod algoritmer
- I dag gør vi det samme med AI - vi fjerner tågen

**Overgang:** "For at gøre det konkret, har jeg destilleret det ned til 6 nøglebegreber..."

---

### Slide 3: Six Core Concepts

**Kernebudskab:** Her er roadmappet - disse 6 koncepter forklarer alt

**Talepunkter:**
- 6 farver = 6 koncepter I skal kende
- Tokens - hvorfor kan ChatGPT ikke tælle bogstaver?
- Transformers - hemmeligheden bag moderne AI
- Neural Networks - selve "hjernen"
- Training - hvordan lærer de?
- Hallucinations - hvorfor lyver de?
- Agents - hvordan løser de opgaver?
- I løbet af næste 40 min gennemgår vi alle 6
- Hold øje med farverne - de kommer tilbage

**Overgang:** "Men først: Fundamentet..."

---

## KAPITEL 1: GRUNDLAG (14 min)

---

### Slide 4: Foundation - Neural Networks

**Kernebudskab:** Alt er neurale netværk - det er det eneste du behøver at huske

**Talepunkter:**
- VIGTIG: Før vi dykker ned - én ting at huske
- LLMs ER neurale netværk
- Fire byggeklodser: Neuroner (små regnestykker), Layers (stabler af neuroner), Weights (millarder af tal), Learning (justér tallene)
- Det er det! Alt andet I hører i dag - tokens, transformers, hallucinations - sker INDEN FOR denne struktur
- Det er ikke magi, det er matrix-multiplikation

**Overgang:** "Okay, nu hvor vi ved at det hele er matematik... Lad os se på den første overraskelse..."

---

### Slide 5: Tokens - The Strawberry Puzzle

**Kernebudskab:** LLMs ser ikke bogstaver - de ser "chunks"

**[PUBLIKUMSSPØRGSMÅL - NU!]**
> "Hvor mange r'er er der i ordet 'strawberry'? Ræk hånden op!"
> [Vent på svar] "De fleste siger 3... Lad os spørge en LLM... Den siger 2. Hvorfor?"

**Talepunkter:**
- Dette er IKKE fordi LLMs er dumme
- Det er fundamentalt i hvordan de virker
- De ser aldrig s-t-r-a-w-b-e-r-r-y
- De ser [31552][19685] - "straw" + "berry"
- Grænsen mellem bogstaver forsvinder inde i tokens

**Overgang:** "Men hvad ER tokens egentlig?"

---

### Slide 6: Tokens - What's Really Happening

**Kernebudskab:** Tokens = komprimerede tekst-chunks, ligesom ZIP men med mening

**Talepunkter:**
- Se det som komprimering - men smartere end ZIP
- Mennesker ser: s-t-r-a-w-b-e-r-r-y (10 tegn)
- LLM ser: to tokens [31552] [19685]
- Byte Pair Encoding (BPE) - som Huffman coding for subwords
- 'e' bruges ofte → får kort kode
- Men: 'the' bruges SUPER ofte → får SIN EGEN token
- Det er derfor de kan "læse" hurtigt - de ser chunks, ikke bogstaver

**Overgang:** "Okay, så det er ikke bare hele ord..."

---

### Slide 7: Tokens - Not Just Words

**Kernebudskab:** Tokens kan være ord, del-ord, præfikser - hvad end der er effektivt

**Talepunkter:**
- Se eksemplerne her
- "hello" = ét token [15339]
- "understanding" = to tokens: [8154, 2259] → "under" + "standing"
- Det smarte: Kompositionel forståelse
- Lige som LEGO - små brikker, uendeligt mange kombinationer
- Derfor kan de håndtere nye ord de aldrig har set
- Bare kombiner dele: "pre" + "processing" = preprocessing

**Overgang:** "Men vent - hvorfor er det vigtigt? Se på tallene..."

---

### Slide 8: Tokens - The Numbers Game

**Kernebudskab:** Kodningssprog er "lettere" for LLMs fordi syntaks er ultra-almindelig

**Talepunkter:**
- ~200.000 tokens i vocabulary - som en ordbog med 200k entries
- Men se: `async`, `const`, `=>`, `{}` - alle får hver deres token
- Hvorfor? De optrådte MILLARDER af gange i træningsdata
- GitHub er fyldt med JavaScript, Python, TypeScript
- Kode er mere repetitivt end naturligt sprog
- Derfor: LLMs er bedre til kode end til at skrive poesi
- De "forudsiger" kode nemmere fordi patterns gentages konstant

**Overgang:** "Okay, nu ved vi HVAD de ser... Men hvordan forstår de KONTEKST?"

---

### Slide 9: Transformer - The Context Problem

**Kernebudskab:** Ord er tvetydige - kontekst er alt

**[PUBLIKUMSSPØRGSMÅL]**
> "Ræk hånden op: Hvor mange tror 'bank' betyder finansiel institution? Hvor mange tror flodbred?"
> [Vent] "Præcis - samme ord, to betydninger. Hvordan VED AI'en forskellen?"

**Talepunkter:**
- "Bank" kan betyde to ting
- Mennesker bruger kontekst: "deposit money" → økonomi
- Men hvordan gør en computer det?
- Det er her Transformer-arkitekturen kommer ind

**Overgang:** "Svaret hedder: Attention..."

---

### Slide 10: Transformer - Attention Is All You Need

**Kernebudskab:** Attention = hvert ord "stemmer" på hvad andre ord betyder

**Talepunkter:**
- Se sætningen - tre ord lyser blåt: bank, deposit, money
- Her er tricket (to trin):
- Step 1: "Bank" spørger alle andre ord: "Hvor relevant er I for min betydning?"
- Step 2: Hvert ord "stemmer" - deposit giver 90%, money giver 85%, "the" giver 2%
- "Bank" kombinerer informationen - weighted average
- Resultatet: Den forstår det er en finansiel institution
- Hvis sætningen var "I sat by the bank of the river" → andre ord ville få høje votes
- Det er det hele! Attention = weighted voting på tværs af alle ord

**Overgang:** "Men vent - hvorfor er det REVOLUTIONERENDE?"

---

### Slide 11: Transformer - Parallel Power

**Kernebudskab:** Transformers behandler alle ord samtidig = derfor er moderne AI mulig

**Talepunkter:**
- Sammenlign gamle RNN vs Transformer
- RNN (gammel metode): "The" → "cat" → "sat" → ét ord ad gangen, 6 steps
- Transformer: [The, cat, sat, on, the, mat] → ALT på én gang, 1 step
- Hvorfor vigtig? Økonomien i det
- GPT-4 tog 3 måneder at træne med parallelisme
- Med gammel sekventiel metode? 50 år!
- Dette er GRUNDEN til at AI-revolutionen skete nu og ikke før
- Det er ikke smartere algoritmer - det er parallelle algoritmer der kan køre på GPUs

**Overgang:** "Godt, så nu ved vi hvordan de 'læser'... Men hvor store ER de?"

---

### Slide 12: Neural Networks - Parameters (The Scale)

**Kernebudskab:** Parametres = vægttallene der definerer modellen. Flere = klogere (men dyrere)

**Talepunkter:**
- Parametres = de millarder/billioner tal vi snakkede om før
- Cloud models: GPT-5 = 2 trillion, GPT-4 = 1.8T, Claude = ~1T
- Disse kører på datacentre med tusindvis af GPUs
- MEN (og her bliver det spændende): Office Models
- I kan køre en 70B model på to RTX 4090 GPUer (~30.000 kr hardware)
- En 32B model kører på ÉN RTX 4090
- Quantization = komprimering - reducer memory 75%, mist 2-5% kvalitet
- Scale: GPT-5 = Empire State Building, Jeres 70B office model = 5-etagers bygning
- Konklusion: On-prem AI er muligt nu

**Overgang:** "Men hvad lærer de egentlig?"

---

### Slide 13: Neural Networks - What They Learn

**Kernebudskab:** Parametres gemmer alt: grammatik, fakta, stil, logik - men ikke som en database

**Talepunkter:**
- Fire eksempler på hvad der "gemt" i parametres:
- Grammar: Subject-verb-object patterns
- Facts: "Paris er hovedstad i Frankrig"
- Style: Hvordan Shakespeare skriver
- Logic: Hvis A > B og B > C, så A > C
- VIGTIGT (💡): De er ikke designet, de er opdaget
- Traditionelle programmer = opskrifter vi skriver linje for linje
- LLMs = kokke der har smagt millioner af retter og lært essensen
- Ingen if-statements, ingen loops - kun 1.8 trillion mønstre fra internettet

**Overgang:** "Så hvordan lærer de alle disse mønstre? Det tager tre faser..."

---

## KAPITEL 2: TRÆNING (8 min)

---

### Slide 14: How LLMs Learn - The Three Stages

**Kernebudskab:** Fra rå model til hjælpsom assistent: Pre-training → SFT → RLHF

**Talepunkter:**
- Tre faser, hver med sit formål
- Pre-training: Læs hele internettet (måneder, $50-100M)
- Supervised Fine-Tuning: Lær at følge instruktioner (uger, ~$1M)
- RLHF: Lær at være hjælpsom og sikker (uger, ~$1M)
- Det er derfor det koster hundrede millioner at lave en frontier model
- Men når den er trænet, er inference billigt
- Tænk: Det koster milliarder at bygge en bilfabrik, men bilerne er billige at producere

**Overgang:** "Lad mig vise jer konkret hvad der sker i hver fase..."

---

### Slide 15: From Raw Model to Helpful Assistant

**Kernebudskab:** Se forskellen mellem faserne - samme prompt, forskellige svar

**Talepunkter:**
- Samme prompt til alle tre: "Write a poem about cats"
- Pre-training only: Autofuldender bare... "Cats and dogs. Cats in Spanish. Cat poem generator"
- Det er en super-fancy autocomplete
- Efter SFT: Okay, nu følger den instruktioner! Der er et digt
- Men... lidt tør, upersonligt
- Efter RLHF: "I'd be happy to!" - engagerende, naturligt, hjælpsomt
- Det er derfor ChatGPT føles som en samtale, ikke som autocomplete
- Tre-trins pipeline: Mønstergenkendelse → Instruktionsbefølgelse → Samtalestil

**Overgang:** "Men vent... Hvis det bare er mønstre, hvordan gemmer det fakta?"

---

### Slide 16: Probabilistic - Not a Database

**Kernebudskab:** LLMs forudsiger sandsynlige fortsættelser - de slår IKKE ting op

**Talepunkter:**
- Her er nøglen: "The capital of France is..."
- 95% sandsynlighed: Paris
- 3% sandsynlighed: Lyon
- 2%: andet
- Det er IKKE erindring - det er forudsigelse
- Modellen lærte at "capital of France is" bliver NORMALT fulgt af "Paris"
- Det betyder: Ingen database, ingen lookup, ingen garanti
- Bare statistisk sandsynlig fortsættelse

**Overgang:** "Og det er præcis derfor vi får..."

---

### Slide 17: Probabilistic - The Hallucination Problem

**Kernebudskab:** Høj confidence ≠ høj accurary. Det er derfor de lyver overbevisende

**[PUBLIKUMSSPØRGSMÅL]**
> "Hvornår købte Google Twitter? Nogle der ved det?"
> [Vent på gæt] "Hvad nu hvis jeg fortalte jer at ChatGPT siger: 2016 for $44 milliarder?"

**Talepunkter:**
- Google købte ALDRIG Twitter
- Men LLM'en siger det med fuld selvtillid
- Hvorfor? "Google" + "acquired" + "Twitter" + "billion" lyder plausibelt sammen
- Det har set lignende sætninger før
- Den GENERERER ikke sandhed - den genererer plausibilitet
- Det er fundamentalt i arkitekturen
- High confidence ≠ high accuracy

**Overgang:** "Så hvad gør vi ved det?"

---

### Slide 18: Hallucinations - Why & What Helps

**Kernebudskab:** Hallucinations er ikke bugs - de er features. Men vi kan mitigere

**Talepunkter:**
- Hvorfor det sker (venstre side):
- No truth database - kan ikke fact-checke på fly
- Pure pattern matching - "ser plausibelt ud" er nok
- Training ≠ memorization - relationskendskab, ikke faktaopslag
- Hvad der hjælper (højre side):
- RAG (Retrieval-Augmented Generation) - giv den reel data at referere til
- Human verification - check kritiske ting manuelt
- Lower temperature - mindre kreativ = færre hallucinations
- Prompt engineering - "Sig 'jeg ved det ikke' hvis du er usikker"
- 💡 Pointen: Kreativitet og hallucinations er samme feature
- Samme evne der skriver gode digte skriver også overbevisende løgne

**Overgang:** "Okay, vi har snakket om hvad de kan... Lad os snakke om hvad de IKKE kan..."

---

## KAPITEL 3: BEGRÆNSNINGER (8 min)

---

### Slide 19: Context Window - The Goldfish Memory

**Kernebudskab:** LLMs har ingen langstidshukommelse - kun en sliding window

**Talepunkter:**
- Her er problemet: Context window = guldfisk-hukommelse
- Eksempel: 128K token window (GPT-4)
- Besked 1: "Min email er alice@company.com"
- [... mange beskeder om troubleshooting ...]
- Besked 98: "Send resumé til min email"
- Besked 99: "Jeg har ikke din email. Kan du give den?"
- Hvad skete der? Første beskeder blev skubbet ud
- Det er som en transportbånd - når den er fuld, ryger de ældste beskeder ud
- Ingen gradvis glemsel - binær: Enten i kontekst eller helt væk

**Overgang:** "Men hvor stor er den window egentlig?"

---

### Slide 20: Context Window - The Numbers

**Kernebudskab:** Større kontekst = dyrere og langsommere. Trade-off mellem kapacitet og pris

**Talepunkter:**
- Tre eksempler:
- GPT-3.5: 4K tokens = ~500 linjer kode. Billig, hurtig
- GPT-4: 128K tokens = ~16K linjer (hel React codebase). Medium pris, medium hastighed
- Claude 3: 1M tokens = ~125K linjer (Linux kernel!). Dyrt, langsomt
- Hvorfor trade-off? Attention er O(N²) - kvadratisk
- 2x længere context = 4x mere regnekraft = 4x dyrere
- De fleste opgaver behøver < 4K
- Men når du skal analysere en hel codebase? Så er 128K+ guld værd

**Overgang:** "Lad os se på en anden kontrol du har..."

---

### Slide 21: Temperature - Same Prompt, Different Answer

**Kernebudskab:** Temperature styrer randomness - 0 = deterministisk, 2.0 = kaos

**[PUBLIKUMSSPØRGSMÅL]**
> "Hvis I bad ChatGPT skrive en sætning om katte to gange, ville I få samme svar?"
> [Vent] "Det afhænger af temperature..."

**Talepunkter:**
- Samme prompt: "Write a sentence about cats"
- Temperature 0: Identisk hver gang - "Cats are domestic animals that are popular pets"
- Temperature 0.7: Varieret men kohærent - "Cats love to nap" vs "Many cats enjoy playing"
- Temperature 2.0: Totalt kaos - "Cats purple democracy whiskers moonlight!"
- Hvad sker der? Temperature justerer probability distribution
- Lav temperature: Vælg altid mest sandsynlige token
- Høj temperature: Giv underdog-tokens en chance
- Produktion: Brug 0 for faktuelle svar, 0.7-1.0 for kreative opgaver, aldrig > 1.5

**Overgang:** "Så lad os samle op - hvad har vi lært?"

---

### Slide 22: The Takeaway - From Magic to Math

**Kernebudskab:** 6 koncepter forklarer "magien" - nu ved I hvorfor tingene virker som de gør

**Talepunkter:**
- Lad os gå tilbage til de 6 farver fra starten
- Tokens: Derfor kan de ikke tælle bogstaver i "strawberry"
- Transformers: Derfor forstår de kontekst, ikke bare ord
- Neural Networks: Derfor koster større modeller eksponentielt mere
- Probabilistic: Derfor er de overbevisende selv når de tager fejl
- Context Window: Derfor glemmer de din første besked
- Temperature: Derfor får du forskellige svar til samme prompt
- "The Magic": Det føles som forståelse
- "The Math": Det er bare next-token prediction
- Men "bare" er ikke simpelt - det er matematik så intrikat at vi stadig reverse-engineerer det

**Overgang:** "Og faktisk... Det ER stadig lidt magisk..."

---

### Slide 23: Still a Bit of Magic?

**Kernebudskab:** Vi forstår 70%, forsker i 20%, og 10% er stadig mystisk

**Talepunkter:**
- Tre niveauer af forståelse:
- 70% Well-Understood: Emergence at Scale
- Vi ved: Reasoning emerges ved ~100B parameters
- Vi ved: Deception appears ved ~1T parameters
- Men vi kan IKKE forudsige hvad der sker ved 10T
- 20% Active Research: In-Context Learning
- Det er mystisk: Giv 3 eksempler → den lærer opgaven
- Zero parameter updates - hvordan?
- Multiple teorier, ingen konsensus
- 10% Still Mysterious: Superposition
- Ét neuron = multiple koncepter samtidig
- Flere koncepter end neuroner - high-dimensional geometri
- Vi ved det sker, vi ved bare ikke helt hvordan
- 💡 Bottom line: Det ER matematik - bare så intrikat at vi stadig lærer om det
- Som at opdage calculus for at forklare planetbevægelser - vi finder ligningerne der forklarer LLMs

**Overgang:** "Okay, nok teori - lad os snakke om hvordan I bruger det..."

---

## KAPITEL 4: PRAKSIS (10 min)

---

### Slide 24: Agents - LLMs with Tools

**Kernebudskab:** Agent = LLM + værktøjer + autonomi i en loop

**Talepunkter:**
- Definition først: Agent = en LLM der kan bruge tools og tage actions autonomt
- Sammenlign:
- LLM alene: Foreslår code snippets, ingen fil-adgang, kan ikke køre kode
- LLM + Coding Agent: Redigerer filer, kører tests, debugger, fuldfører opgaver
- Eksempel: "Fix TypeScript error in UserProfile.tsx"
- Think: "Jeg skal læse filen og forstå fejlen"
- Act: Læs fil, analyser error, ret component's prop interface
- Observe: Kør TypeScript compiler → No errors
- Respond: "Fixed! Opdaterede User interface"
- Det er en loop - agent bliver ved indtil opgaven er løst
- Coding Agents: Claude Code, GitHub Copilot, Cursor, Windsurf, Devin
- I kan prøve dem i dag

**Overgang:** "Men virker det? Lad os se på tal..."

---

### Slide 25: From Math to Reality - LLMs Excel at Coding

**Kernebudskab:** Dette er ikke fremtid - det er 2025. AI kode er allerede mainstream

**Talepunkter:**
- Fire datapunkter fra virkeligheden:
- SWE-bench: 2023 = 4.4% løst, 2025 = 78.8% løst
- Det er GitHub issues løst autonomt - 18x forbedring på 2 år!
- Enterprise: Google og Microsoft har 30% AI-genereret kode, Meta targeter 50% i 2026
- Developer Speed: GitHub Copilot gør folk 55% hurtigere, McKinsey siger 126% højere output
- Business Impact: Booking.com 30% højere throughput, IBM sparer $4.5 milliarder i 2025
- Og crucially: "This is the worst it'll be"
- Modellerne bliver bedre hver måned
- Tooling forbedres konstant
- Agentic engineering practices modnes
- Det er som at stå i 2007 og se på den første iPhone

**Overgang:** "Hvis I vil lære mere..."

---

### Slide 26: Recommended Reading

**Kernebudskab:** Tre bøger hvis I vil dykke dybere

**Talepunkter:**
- Tre anbefalinger på forskelligt niveau:
- "What Is ChatGPT Doing?" - Stephen Wolfram: Matematisk dybt, men læseligt
- "Not Artificial, Not Intelligent" - Django Beatty: Afmystificerer begreberne
- "Vibe Coding" - Gene Kim & Steve Yegge: Praktisk, hvordan koder man med AI?
- Alle tre er fra 2024-2025, så de er up-to-date
- I finder dem på Amazon, kan læses på en weekend hver

**Overgang:** "Og apropos AI der kan kode..."

---

### Slide 27: Meta (Claude Code Slide)

**Kernebudskab:** Denne præsentation blev lavet MED Claude Code - det virker!

**Talepunkter:**
- Fun fact: Jeg brugte Claude Code til at lave denne præsentation
- Ikke bare "skrev noget tekst" - Claude:
- Designede slides, skrev Marp markdown, debuggede CSS styling
- Foreslog layout, optimerede farver, fixede syntax errors
- Vi itererede sammen - jeg sagde hvad jeg ville, Claude implementerede
- Det tog timer i stedet for dage
- Det er præcis den workflow jeg snakkede om: Human + Agent
- Hvis I vil prøve det selv: claude.ai/code

**Overgang:** "Okay, det var det! Tid til spørgsmål..."

---

### Slide 28: Q&A (Questions Slide)

**Kernebudskab:** Åben til spørgsmål

**Talepunkter:**
- Så, det var "fra magi til matematik"
- Vi har dækket: Tokens, Transformers, Neural Networks, Training, Hallucinations, Context, Temperature, Agents
- Hvad vil I vide mere om?
- Spørgsmål? Pushback? "Men hvad med...?"

---

## NOTER TIL FLOW

**Timing checkpoints:**
- Ved slide 8 (tokens done): ~8 min inde
- Ved slide 13 (grundlag done): ~17 min inde
- Ved slide 18 (træning done): ~25 min inde
- Ved slide 23 (begrænsninger done): ~33 min inde
- Ved slide 25 (praksis done): ~43 min inde
- Slut Q&A: 50 min

**Energi-management:**
- Start høj energi (intro)
- Dæmp lidt til teknisk forklaring (grundlag)
- Pick up igen ved "praksis" (virkelige tal)
- Højt tempo gennem "agents" sektion

**Hvis du løber over tid:**
- Spring slide 23 over (Still Magic) - nice-to-have
- Forkort "Reading" slide til bare at nævne dem
- Reservér ALTID 5-7 min til Q&A

**Hvis du har for god tid:**
- Uddyb "Attention" slide med ekstra eksempel
- Del en personlig anekdote ved "Claude Code" slide
- Bed om spørgsmål midt i præsentationen ved checkpoints
