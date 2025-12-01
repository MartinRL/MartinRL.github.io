# Plan: Danske Talenoter til LLMs & Agents Præsentationen

## Formål
Skabe 1-2 korte, mundrette danske afsnit per slide som ankre til fri tale. Tonen er uformel og kollegial — som at snakke med udviklere over kaffe.

---

## Slide 1: Titel — LLMs & Agents

**Taletekst:**
> "I dag skal vi se på, hvad der egentlig sker under motorhjelmen på ChatGPT, Claude og de andre. Ikke fordi vi skal bygge vores egen LLM — det kræver 100 millioner dollars og et par måneder — men fordi det gør os til bedre brugere. Og fordi det faktisk er ret fedt at forstå, hvordan magi bliver til matematik."

---

## Slide 2: Purpose — From Magic to Math

**Taletekst:**
> "Arthur C. Clarke sagde det perfekt: Avanceret teknologi er umulig at skelne fra magi. Og det er præcis sådan det føles, når ChatGPT skriver kode for os. Men i dag trækker vi gardinet til side. Vi går fra 'det virker bare magisk' til 'ah, *det* er derfor den gør sådan'."

---

## Slide 3: Six Core Concepts

**Taletekst:**
> "Seks koncepter. Det er alt hvad I behøver for at forstå, hvordan de her ting virker. Og når vi er færdige, vil I vide præcis hvorfor en LLM ikke kan tælle bogstaver i 'strawberry', hvorfor den nogle gange lyver helt overbevisende, og hvorfor den glemmer hvad I sagde for 10 minutter siden. Lad os dykke ned."

---

## Slide 4: Neural Networks — Building Blocks

**Taletekst:**
> "Neurale netværk er inspireret af hjernen, men det er en løs inspiration. Tænk på det sådan her: en neuron er bare en lille funktion der tager nogle tal ind, ganger dem med vægte, og spytter et tal ud. Gange mange milliarder af dem sammen i lag, og pludselig kan de lære mønstre. 'Neurons that fire together, wire together' — eller i LLM-termer: tokens der optræder sammen, får stærkere forbindelser."

---

## Slide 5: Parameters — The Scale

**Taletekst:**
> "Skala er altafgørende. GPT-4 har 1.8 billioner parametre — det er 1.8 billioner små justerbare knapper der bestemmer, hvordan modellen reagerer. Det koster 50-100 millioner dollars bare at træne sådan en. Men det sjove er, at du kan køre en 70-milliard-parameter model på to gamer-grafikkort til 50.000 kr. Den er 25 gange mindre, men stadig overraskende god til det meste."

---

## Slide 6: What They Learn

**Taletekst:**
> "Det her er det vilde: Vi designer ikke reglerne. Der er ingen if-statements, ingen regex, ingen hardcodede grammatikregler. Modellen lærer grammatik, fakta, stil og logik bare ved at læse internettet. Det er som forskellen på at give nogen en kogebog versus at lade dem smage tusindvis af retter. De kan ikke forklare opskriften, men de ved hvad der smager rigtigt."

---

## Slide 7: Tokens — The Strawberry Puzzle

**Taletekst:**
> "Okay, her kommer den klassiske test: Hvor mange r'er er der i 'strawberry'? ChatGPT siger to. Det rigtige svar er tre. Hvorfor fejler den? Fordi den aldrig ser bogstaver. Den ser tokens."

---

## Slide 8: Tokens — What's Really Happening

**Taletekst:**
> "Når vi skriver 'strawberry', ser vi s-t-r-a-w-b-e-r-r-y. Modellen ser to tokens: 'straw' og 'berry'. Bogstaverne r forsvinder ind i tokens. Det er som at spørge en, der kun læser ord, om at tælle bogstaver — de skal tænke baglæns fra ord til bogstaver. Derfor fejler de ofte på den slags opgaver."

---

## Slide 9: Tokens — Not Just Words

**Taletekst:**
> "Tokens er ikke bare hele ord. 'Understanding' bliver til 'under' plus 'standing'. 'Preprocessing' bliver til 'pre' plus 'processing'. Det er faktisk smart — det betyder at modellen kan håndtere ord den aldrig har set før, ved at kombinere kendte dele. Som LEGO-klodser der kan sættes sammen på nye måder."

---

## Slide 10: Tokens — The Numbers Game

**Taletekst:**
> "Her er grunden til at LLM'er er overraskende gode til kode: Programmeringssprog har tokens som 'async', 'const', 'function', pil-notation, tuborgklammer. De dukker op milliarder af gange i træningsdata. Kode er mere forudsigeligt end naturligt sprog. Så på en måde er kode *nemmere* for en LLM end dansk prosa."

---

## Slide 11: Transformer — The Context Problem

**Taletekst:**
> "'Jeg gik ned til banken for at indsætte penge.' Hvilken bank? Finansiel institution eller flodbred? I ved det med det samme. Men hvordan? I bruger konteksten — 'indsætte' og 'penge' giver det væk. Transformere gør præcis det samme."

---

## Slide 12: Attention Is All You Need

**Taletekst:**
> "Attention er mekanismen der får det til at virke. Hvert ord spørger alle andre ord: 'Hvor relevant er du for min betydning?' Og så stemmer de. 'Deposit' og 'money' stemmer kraftigt for finansiel bank. 'The' stemmer næsten ikke. Det hele sker parallelt, for alle ord, på én gang. Det er vanvittigt effektivt."

---

## Slide 13: Parallel Power

**Taletekst:**
> "Før 2017 brugte vi RNN'er der læste sekventielt: 'The', så 'cat', så 'sat'... seks trin. Transformer-arkitekturen læser alt på én gang: et trin. Det er ikke bare hurtigere — det er den eneste grund til at moderne AI eksisterer. Uden parallelisering ville GPT-4 tage 50 år at træne i stedet for 3 måneder. Det ville være økonomisk umuligt."

---

## Slide 14: How LLMs Learn — Three Stages

**Taletekst:**
> "Tre trin: Først pre-training — læs internettet, lær mønstre. Det tager måneder og koster 50-100 millioner. Så supervised fine-tuning — vis modellen eksempler på gode svar. Til sidst RLHF — lad mennesker rangere svar og træn en belønningsmodel. Det er det der gør forskellen mellem 'autocomplete på steroider' og 'faktisk hjælpsom assistent'."

---

## Slide 15: Raw Model to Helpful Assistant

**Taletekst:**
> "Se forskellen: Bed en pre-trained model om at skrive et digt om katte, og den fortsætter bare med 'cat poems 2023, best cat poems...' — den prøver at autocomplete en Google-søgning. Efter SFT skriver den faktisk et digt. Efter RLHF siger den 'Jeg vil gerne hjælpe!' og skriver et endnu bedre digt. Den lærer at være hjælpsom, ikke bare præcis."

---

## Slide 16: Karpathy Textbook Slide

**Taletekst:**
> "Det her er fra Andrej Karpathy, tidligere Tesla AI-chef og OpenAI-grundlægger. Hans pointe: Vi er gået fra den klassiske 'Software 1.0' — hvor vi skriver eksplicitte regler — til 'Software 2.0' — hvor vi træner neurale netværk. Fremtiden er hybrid: nogle ting koder vi selv, andre ting lærer modellen."

---

## Slide 17: Probabilistic — Not a Database

**Taletekst:**
> "'Hvad er hovedstaden i Frankrig?' Modellen svarer Paris — men ikke fordi den slår op i en database. Den *forudsiger* at 'Paris' er det mest sandsynlige næste token. 95% sandsynlighed for Paris, 3% for Lyon, 2% for noget andet. Den husker ikke — den gætter uddannet."

---

## Slide 18: The Hallucination Problem

**Taletekst:**
> "'Hvornår købte Google Twitter?' Modellen svarer: 'Google købte Twitter i 2016 for 44 milliarder dollars.' Fuldstændig overbevisende. Og fuldstændig forkert — Google har aldrig købt Twitter. Det her kalder vi en hallucination. Og det er ikke en bug — det er en konsekvens af, hvordan systemet fundamentalt virker."

---

## Slide 19: Why Hallucinations Happen

**Taletekst:**
> "Hvorfor sker det? Fordi modellen ikke har en sandhedsdatabase. Den har kun mønstre. 'Google' plus 'acquired' plus 'Twitter' lyder plausibelt sammen — det *kunne* være sandt. Modellen kan ikke skelne mellem 'sandsynligt at se i træningsdata' og 'faktisk sandt'. Heldigvis kan vi hjælpe: RAG, lavere temperatur, og prompts der siger 'sig du ikke ved det, hvis du er usikker'."

---

## Slide 20: Context Window — Goldfish Memory

**Taletekst:**
> "128.000 tokens lyder af meget — det er cirka 100 siders tekst. Men når vinduet er fuldt, forsvinder de ældste beskeder. Ligesom en guldfisk. I starten af samtalen sagde du 'min email er alice@company.com'. 50 beskeder senere: 'Jeg har ikke din email. Kan du give den igen?' Den *glemte* det, fordi det gled ud af vinduet."

---

## Slide 21: Context Window — The Numbers

**Taletekst:**
> "Her er størrelserne: GPT-3.5 har 4K tokens — cirka 500 linjer kode. GPT-4 har 128K — en hel React-codebase. Claude 3 har en million tokens — det er hele Linux-kernen. Men større kontekst betyder langsommere og dyrere. De fleste opgaver klarer sig fint med under 4K."

---

## Slide 22: Temperature

**Taletekst:**
> "Temperatur styrer kreativitet. Ved 0 får I det samme svar hver gang — deterministisk. Ved 0.7 er det varieret men stadig sammenhængende. Ved 2.0 får I 'Cats purple democracy whiskers moonlight!' — totalt kaos. For kode: Brug lav temperatur til debugging og tests. Højere til brainstorming og refactoring."

---

## Slide 23: The Takeaway — From Magic to Math

**Taletekst:**
> "Nu ved I det: Strawberry-problemet? Tokens. Forstår kontekst? Transformere. Dyr at køre? Parametre. Overbevisende forkert? Probabilistisk. Glemmer hvad I sagde? Context window. Forskellige svar hver gang? Temperatur. Magien er stadig imponerende — men nu ved I, hvad den er lavet af."

---

## Slide 24: Still a Bit of Magic?

**Taletekst:**
> "Vi forstår omkring 70% af hvordan det virker. Men der er stadig mysterier. Emergent reasoning — hvorfor begynder de pludselig at ræsonnere ved 100 milliarder parametre? In-context learning — hvorfor kan de lære af tre eksempler uden at opdatere vægte? Superposition — hvorfor kan én neuron repræsentere flere koncepter? Vi er stadig ved at reverse-engineere det."

---

## Slide 25: Agents — LLMs with Tools

**Taletekst:**
> "En agent er en LLM med værktøjer. Alene kan ChatGPT foreslå kode — men den kan ikke køre den, teste den eller rette fejl. Med agent-arkitektur kan den: læse filer, køre tests, debugge, og iterere indtil opgaven er løst. Think-act-observe-loop. Det er forskellen på en rådgiver og en der faktisk gør arbejdet."

---

## Slide 26: LLMs Excel at Coding — Stats

**Taletekst:**
> "Tallene er vilde. SWE-bench — en benchmark for rigtige GitHub-issues — gik fra 4% løst i 2023 til 79% i 2025. Google og Microsoft siger at 30% af deres kode nu er AI-genereret. Meta sigter efter 50% i 2026. GitHub Copilot gør udviklere 55% hurtigere. Det her er ikke fremtiden — det er nu. Og det bliver kun bedre."

---

## Slide 27: Recommended Reading

**Taletekst:**
> "Tre bøger hvis I vil gå dybere: Stephen Wolfram forklarer den matematiske side. Django Beatty er mere filosofisk — hvad AI *ikke* er. Og 'Vibe Coding' fra Gene Kim og Steve Yegge handler om, hvordan vi som udviklere skal arbejde med AI. Alle tre er værd at læse."

---

## Slide 28: Claude Code Slide

**Taletekst:**
> "Og ja — den her præsentation er delvist lavet med Claude Code. Jeg sidder og snakker med den i terminalen, den redigerer slides, kører Marp, og vi itererer sammen. Det er et godt eksempel på, hvordan agenterne faktisk fungerer i praksis."

---

## Slide 29: Q&A

**Taletekst:**
> "Spørgsmål? Nu er det jeres tur."

---

## Tidsstyring

Med 45-50 minutter og 20+ slides:
- **Del 1** (Neural Networks, Tokens, Transformers): ~15 min
- **Del 2** (Training, Hallucinations, Context, Temperature): ~15 min
- **Del 3** (Takeaway, Agents, Stats): ~10 min
- **Q&A**: ~10 min

## Tips til Fremførelse

1. **Start stærkt** — Magisk vs matematisk hook fanger opmærksomheden
2. **Strawberry er din ven** — Brug det som running gag når I snakker om tokens
3. **Bank-eksemplet** — Bed publikum selv svare før du afslører
4. **Karpathy-slide** — Kort pause, lad billedet tale
5. **Stats-slide** — Lad tallene synke ind, gentag de vigtigste
