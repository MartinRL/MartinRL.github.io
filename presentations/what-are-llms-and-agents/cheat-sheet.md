# 🎯 CHEAT SHEET - LLMs & Agents Præsentation

**Udskriv dette og hav ved computeren under præsentationen!**

---

## ⏱️ TIMING CHECKPOINTS

| Slide | Tid | On Track Hvis... |
|-------|-----|------------------|
| 3 (Six Concepts) | 3 min | < 4 min |
| 8 (Numbers Game) | 8 min | < 10 min |
| 13 (What They Learn) | 17 min | < 19 min |
| 18 (Hallucinations) | 25 min | < 27 min |
| 23 (Still Magic) | 33 min | < 35 min |
| 25 (Excel at Coding) | 43 min | < 45 min |

**Total: 43 min præsentation + 7 min Q&A = 50 min**

---

## 🎤 DE 4 PUBLIKUMSSPØRGSMÅL

### 1️⃣ Før Slide 5 (Strawberry):
> "Hvor mange r'er er der i 'strawberry'? Ræk hånden op!"
> [Vent] "De fleste siger 3... LLM siger 2. Hvorfor?"

### 2️⃣ Før Slide 9 (Bank):
> "Se denne sætning... Hvilken 'bank'?"
> "Ræk hånden op for finansiel... for flodbred..."
> [Vent] "Hvordan VED AI'en forskellen?"

### 3️⃣ Før Slide 17 (Hallucination):
> "Hvornår købte Google Twitter? Nogen der ved det?"
> [Vent på gæt] "ChatGPT siger: 2016 for $44 milliarder."
> [Pause] "Google købte ALDRIG Twitter."

### 4️⃣ Før Slide 21 (Temperature):
> "Hvis I bad ChatGPT skrive en sætning om katte to gange..."
> "...ville I få samme svar?"
> [Vent] "Det afhænger af temperature..."

---

## 📊 KERNEBUDSKABER (1 per slide)

### INTRO (Slides 1-3)
1. Velkommen og setup
2. AI = matematik, ikke magi
3. **6 koncepter** forklarer alt

### KAPITEL 1: GRUNDLAG (Slides 4-13)
4. Alt er **neurale netværk**
5. LLMs ser ikke bogstaver - de ser **tokens**
6. Tokens = komprimerede chunks
7. Kompositionel forståelse (LEGO)
8. Kode er lettere end tekst (repetition)
9. Ord er tvetydige - kontekst er alt
10. **Attention** = weighted voting
11. Parallelisme gør AI mulig (ikke smartere algoritmer)
12. Flere parametres = klogere (men dyrere)
13. Parametres gemmer mønstre, ikke facts

### KAPITEL 2: TRÆNING (Slides 14-18)
14. **3 faser**: Pre-training → SFT → RLHF
15. Se forskellen mellem faserne
16. LLMs **forudsiger**, de slår ikke op
17. Høj confidence ≠ høj accuracy
18. Hallucinations er features, ikke bugs

### KAPITEL 3: BEGRÆNSNINGER (Slides 19-23)
19. Context = **guldfisk-hukommelse**
20. Større window = dyrere (O(N²))
21. **Temperature** styrer randomness
22. 6 koncepter forklarer "magien"
23. Vi forstår 70%, forsker i 20%, 10% mystisk

### KAPITEL 4: PRAKSIS (Slides 24-28)
24. **Agent** = LLM + tools + loop
25. 2025: 78.8% GitHub issues løst (vs 4.4% i 2023)
26. Tre bøger at læse
27. Denne præsentation lavet med Claude Code
28. Åben til spørgsmål

---

## 🎨 DE 6 FARVER/KONCEPTER

**Husk akronym: TTNHCA**

- **T**okens (lilla) → Hvorfor ikke tælle bogstaver
- **T**ransformers (blå) → Hvorfor forstå kontekst
- **N**eural Networks (grøn) → Hvorfor koster større modeller mere
- **H**allucinations (orange) → Hvorfor overbevisende når forkert
- **C**ontext (mørkeblå) → Hvorfor glemmer første besked
- **A**gents (grå) → Hvordan løser opgaver

---

## 🔑 NØGLETAL (til at huske)

### Tokens:
- ~200.000 tokens i vocabulary
- "strawberry" = [31552][19685]

### Transformers:
- Attention votes: deposit 90%, money 85%, "the" 2%
- GPT-4: 3 måneder træning vs 50 år uden parallelisme

### Parameters:
- GPT-4: 1.8T, Claude: ~1T, Office: 70B
- Empire State vs 5-etagers bygning

### Training:
- Pre-training: $50-100M
- SFT + RLHF: ~$1M hver

### Context:
- GPT-3.5: 4K tokens (~500 linjer)
- GPT-4: 128K (~16K linjer)
- Claude: 1M (~125K linjer)

### Coding:
- SWE-bench: 4.4% (2023) → 78.8% (2025)
- Google/Microsoft: 30% AI-kode
- Meta target: 50% i 2026

---

## 💡 OVERGANGE MELLEM KAPITLER

**Intro → Grundlag:**
> "Men først: Fundamentet..."

**Grundlag → Træning:**
> "Så hvordan lærer de alle disse mønstre?"

**Træning → Begrænsninger:**
> "Vi har snakket om hvad de kan... Lad os snakke om hvad de IKKE kan..."

**Begrænsninger → Praksis:**
> "Okay, nok teori - lad os snakke om hvordan I bruger det..."

---

## 🚨 HVIS DU FUMLER

### Glemmer næste punkt?
→ Kig på slide, der er hints

### Fumler et ord?
→ Ignorér, fortsæt (ingen lægger mærke til det)

### Mister tråden?
→ "Lad mig gentage kernebudskabet..." [recap]

### Går helt blank?
→ "Spændende spørgsmål! Nogen fra publikum der har tanker?" [køb tid]

### Løber over tid?
→ Spring slide 23 (Still Magic) over
→ Forkort slide 26 (Reading) til bare at nævne dem

### Har for god tid?
→ Uddyb Attention-eksemplet (slide 10)
→ Del personlig anekdote ved Claude Code slide
→ Invitér til spørgsmål midt i præsentationen

---

## 🎯 DE 3 VIGTIGSTE SLIDES

Hvis du kun husker TRE slides perfekt, lad det være disse:

1. **Slide 3 (Six Concepts)** - Roadmappet for hele præsentationen
2. **Slide 10 (Attention)** - Kernen i hvordan AI virker
3. **Slide 25 (Excel at Coding)** - Hvorfor det er vigtigt NU

---

## 💪 ENERGI-MANAGEMENT

### Start (Slides 1-3):
- **HØJ energi**, smil, velkommen
- "Glad for at være her!"

### Grundlag (Slides 4-13):
- **Moderat tempo**, teknisk men håndgribeligt
- Brug publikumsspørgsmål til at holde dem vågen

### Træning (Slides 14-18):
- **Pick up**, spændende afsløringer (hallucinations!)
- Energi op ved publikumsspørgsmål #3

### Begrænsninger (Slides 19-23):
- **Steady**, kan falde her - hold energien oppe
- Slide 22 (Takeaway) er recap - brug til at samle op

### Praksis (Slides 24-28):
- **HØJESTE ENERGI**, virkelige tal, inspiration
- "This is the worst it'll be" = peak momentum
- Slut på en høj note

---

## 📱 TECH CHECKLIST (lige før)

- [ ] Laptop opladet + oplader med
- [ ] Slides åbnet og testet (presentation mode)
- [ ] Fjernbetjening virker (hvis du bruger en)
- [ ] Backup på USB-stick
- [ ] Vand til undervejs
- [ ] Mobil på lydløs
- [ ] Denne cheat sheet printet og ved computeren

---

## 🧘 LIGE FØR DU GÅR PÅ

### 3-4-6 Vejrtrækning (3 gange):
1. Ind gennem næsen: 4 sekunder
2. Hold: 4 sekunder
3. Ud gennem munden: 6 sekunder

### Husk:
✅ Du har øvet det 20+ gange
✅ Du ved mere end publikum
✅ De er her for at lære
✅ Første 3 minutter er nøglen - derefter flyder det

---

## 🎬 DE FØRSTE 30 SEKUNDER (VIGTIGST!)

**Når du går på:**

1. **Smil** (selvom du er nervøs)
2. **Pause** (1-2 sek, lad dem se dig)
3. **"Velkommen alle - jeg er glad for at være her hos Clever"**
4. **"I dag skal vi demystificere AI"**
5. **Klik videre til slide 2**

**Når du har overlevet de første 30 sek, er resten nemt.**

---

## 🏁 AFSLUTNING (Slide 28)

### Når du kommer til Q&A:

"Så, det var 'fra magi til matematik'."

[Pause]

"Vi har dækket: Tokens, Transformers, Neural Networks, Training, Hallucinations, Context, Temperature, Agents."

[Pause]

"Hvad vil I vide mere om? Spørgsmål? Pushback?"

[Åben til publikum]

---

## 🎉 SUCCESS = HVIS 3/4 ER JA:

1. ✅ Kunne de svare: "Hvad er forskel på LLM og agent?"
2. ✅ Nævnte nogen at de vil prøve Claude Code/Cursor?
3. ✅ Fik du spørgsmål der viste de lyttede?
4. ✅ Følte du dig selv tryg (ikke perfekt, bare tryg)?

---

## 💬 HVIS PUBLIKUM STILLER SVÆRE SPØRGSMÅL

### "Hvad med [avanceret teknisk ting]?"
→ "Rigtig godt spørgsmål! Det er [kort svar]. Hvis du vil vide mere, kan vi tage det efter præsentationen."

### "Jeg er ikke enig i..."
→ "Interessant perspektiv! Hvad ville du sige i stedet?" [åben dialog]

### "Hvad er forskellen mellem [X] og [Y]?"
→ Hvis du ved det: Svar kort
→ Hvis du ikke ved det: "God distinktion at kigge på - lad mig ikke spekulere, men jeg sender dig et link efter mødet"

**Husk:** Det er OK at sige "Jeg ved det ikke" eller "Lad os tage det efter præsentationen"

---

## 🚀 FINAL PEP TALK

Du har:
- ✅ 28 slides
- ✅ 6 koncepter
- ✅ 4 publikumsspørgsmål
- ✅ 50 minutter
- ✅ Denne cheat sheet

**Ingen forventer perfektion.**
**De forventer indsigt.**
**Du har indsigten.**
**Bare del den.**

**GO GET THEM! 🎯🔥**
