---
title: Context& Custom Solutions Presentation of the Event Modeling Conference in Munich October 2025
marp: true
theme: default
paginate: false
html: true
backgroundColor:
tags:
  - #
  - delegate
  - event-modeling
  - presentation
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 2rem;
  }
---
# Event Modeling Conference Munich 2025

**Martin Rosén-Lidholm, Context& Custom Solutions**
TaaS Day Aarhus | October 2025
🟦🟧🟩🪟⚙️
___

<style scoped>
h1 { font-size: 1.6em; margin-bottom: 0.3em; }
h2 { font-size: 1.2em; margin-bottom: 0.4em; margin-top: 0; }
h3 { font-size: 1em; margin-bottom: 0.3em; margin-top: 0.5em; }
p { font-size: 0.8em; margin: 0.2em 0; line-height: 1.3; }
li { font-size: 0.75em; line-height: 1.3; }
ul { margin: 0.2em 0; padding-left: 1.2em; }
ul ul { margin: 0.1em 0; }
strong { font-size: 1em; }

.upper-right-logo {
  position: absolute;
  top: 1rem;
  right: 1rem;
}
.upper-right-logo img {
  height: 130px;
  width: auto;
}
</style>

<div class="upper-right-logo">

![](../Files/event-modeling.jpg)

</div>

# Before We Begin…

<style scoped>
section {
  padding-top: 2rem;
}
h1 {
  margin-bottom: 0.5rem;
}
h3 {
  margin-top: 0.5rem;
  margin-bottom: 0.3rem;
}
p {
  margin-top: 0.2rem;
  margin-bottom: 0.5rem;
}
</style>

### Event Modeling (action)
The practice/methodology/workshop format/tooling that outputs event models.

### Event Model (artifact that can model, specify, and verify **any** information system 💡)

<div class="columns">
<div>

**5 elements**
- 🟦 command (future)
- 🟧 event (past)
- 🟩 read-model (present)
- 🪟 screen
- ⚙️ automation

**4 patterns**
- state-change
- state-view
- automation
- translation

</div>
<div>

**Structure**
- An event model is a series of slices on a timeline, i.e. storytelling
- A slice is one of the four patterns and as cohesive and decoupled from the others as possible (preferably fully)
- Swimlanes divide different users and systems

**Given-(When)-Then tests/verification**
- Given State, When Command, Then Event(s)
- Given Event(s), Then State

**No (kanban/scrum) Board Needed**

</div>
</div>

___
<style scoped>
.upper-right-photo {
  position: absolute;
  top: 1rem;
  right: 1rem;
}
.upper-right-photo img {
  height: 150px;
  width: auto;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}
</style>

<div class="upper-right-photo">

![](../Files/Adam-Dymitruk.jpg)

</div>

# Keynote
### Adam Dymitruk, Founder and CEO, Adaptech Group
![bg blur:3px opacity:.3](../Files/adam-keynote-event-modeling-munich.jpg)

## the state and future of event modeling

- Attaining the goal of DDD w/o doing DDD (& TDD, & ...)
- Ruts in the road (we've always done it this way)
- eventmodeling.com and certifications (will remain free and open, but avoid the Accentures of the world to claim it and do harm)
- The dependency on Miro will be addressed

> AI needs to have a good system to be in. It's wasted on the stupid right now!

<!--
the inventor of event modeling and founder and CEO of Adaptech Group
-->
---
<style scoped>
h1 { font-size: 1.5em; margin-bottom: 0.3em; }
h2 { font-size: 1.1em; margin-bottom: 0.4em; margin-top: 0; }
li { font-size: 0.75em; line-height: 1.3; }
ul { margin: 0.3em 0; padding-left: 1.2em; }
ul ul { margin: 0.15em 0; }

.with-photos {
  display: grid;
  grid-template-columns: 1fr 150px;
  gap: 2rem;
  align-items: start;
}
.photo-stack {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.photo-item {
  text-align: center;
}
.photo-item img {
  width: 100%;
  border-radius: 8px;
}
.photo-item p {
  margin-top: 0.5rem;
  font-size: 0.8em;
  font-style: italic;
}
</style>

<div class="with-photos">
<div>

# Keynote — Adam Dymitruk
## the business model of Adaptech Group

- 100% operational consultancy consistency
	- only event modeling and event sourcing
- fixed price event modeling workshops
- fixed price per slice: 2.500 CA$ (~ 11.500 DKK)
- engineers paid per slice
	- lowest monthly salary to date: 3k CA$ (~ 14k DKK)
	- highest monthly salary to date: 76k CA$ (~ 350k DKK) 

- ⅔ of the money goes to the employees, the other ⅓ the company
- free bug-fixes for life
- 12 years running and no attrition

</div>
<div class="photo-stack">

<div class="photo-item">

![](../Files/Dave-Thomas.jpeg)

Dave Thomas, Advisor

</div>

<div class="photo-item">

![](../Files/Mel-Conway.jpg)

Mel Conway, Advisor

</div>

</div>
</div>

___
![bg](../Files/event-modeling-conf-2025-image18.jpg)
# Beyond the Hype: Event Sourcing in the age of AI
### Allard Buijze, CTO and founder, Axoniq
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
### strain on systems (scalability needs)

___
![bg](../Files/event-modeling-conf-2025-image16.jpg)

<style scoped>
.bottom-emojis {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  font-size: 3.5em;
  display: flex;
  gap: 1.5rem;
}
.checkmarks {
  position: absolute;
  left: 9rem;
  top: 42%;
  transform: translateY(-50%);
  font-size: 3em;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
</style>

<div class="bottom-emojis">
🤖x👱‍♀️x🖥
</div>

<div class="checkmarks">
<div>✔</div>
<div>✔</div>
<div>✔</div>
</div>

___
![bg](../Files/event-modeling_flat-cost-curve.jpg)

<style scoped>
section {
  justify-content: flex-start;
  padding-top: 0rem;
  padding-left: 3rem;
}
h3 {
  margin-left: 2rem;
}
.bottom-emojis {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  font-size: 4em;
  display: flex;
  gap: 1.5rem;
}
</style>

### the flat cost curve of additional features<br/>with event modeling and event sourcing

___

# Spec-Driven Development with Axoniq and Event Modeling: 📋→ 🤖x👱‍♀️→🟦🟧🟩🪟⚙️→🤖x👱‍♀️→0️⃣1️⃣

<style scoped>
.content-with-image {
  display: grid;
  grid-template-columns: 300px auto 200px auto 300px;
  gap: 0.5rem;
  align-items: center;
}
.content-with-image img {
  width: 100%;
  border-radius: 8px;
}
.iteration-emoji {
  font-size: 4em;
  text-align: center;
}
</style>

<div class="content-with-image">

![](../Files/event-modeling-workshop-spec-munich.jpg)

<div class="iteration-emoji">
🔄
</div>

<div>

![](../Files/event-modeling-conf-2025-image15.jpg)

</div>

<div class="iteration-emoji">
🔄
</div>

<div>

![](../Files/software-namo-banana.png)

</div>

</div>

<!-- 
The spec was scanned using the phone from a workshop spec at the conference.

The event model is text in VSCode.

The event model removes the ambiguity. 

Allard: I don't like event modeling. I love event models.

Martin: "Martin, this is the future"
 -->
___
![bg](../Files/Farley-programming.jpg)

<style scoped>
h1 {
  color: white;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
}
.lower-left {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 50%;
  height: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}
.lower-left h2 {
  font-size: 1.5em;
  margin: 0;
  text-align: center;
  color: white;
}
.lower-left .emojis {
  font-size: 2em;
}
</style>

<div class="lower-left">

## a personal reflection:<br/>event modeling<br/>ticks all the boxes

<div class="emojis">1️⃣✅2️⃣✅3️⃣✅</div>

</div>

<!-- https://youtu.be/CoGO6s7bS3A?si=-78edKhlYcBCQ7gg -->

___

# Cratis: Event Sourcing and Event Modeling for .NET & C#

<style scoped>
h1 { font-size: 1.5em; margin-bottom: 0.5em; }
h2 { font-size: 1.2em; margin-bottom: 0.4em; margin-top: 0.5em; }
li { font-size: 0.8em; line-height: 1.4; }
ul { margin: 0.3em 0; padding-left: 1.5em; }
p { font-size: 0.85em; margin: 0.3em 0; }
</style>

<div class="columns">
<div>

**Architecture**
- Event sourcing database built on MongoDB
- Control-levels 
  - Orleans
  - .NET client SDK
  - ASP.NET Core
- Extensible for other data stores

**Enterprise Ready**
- Multi-tenancy support
- Compliance focused
- Microservice workloads
- Business critical data storage

</div>
<div>

**Developer Experience**
- "No complexity, just powerful tools"
- Declarative projections
- Parent-child relationships
- Advanced aggregations
- Cratis Workbench (management tool)

**CQRS & Application Model**
- Opinionated approach
- Built on ASP.NET Core
- Consistent application patterns suitable for event modeling

</div>
</div>

**License:** MIT | **Website:** [cratis.io](https://cratis.io) | **GitHub:** [github.com/Cratis/Chronicle](https://github.com/Cratis/Chronicle)

<!-- research the open source event sourcing and event modeling tool for .net  "cratis" and
create a slide about it. place the slide last in the slide deck. -->
---
![bg opacity:.3](../Files/event-modeling-conference-bier.jpg)

<style scoped>
h1 { font-size: 1.5em; margin-bottom: 0.5em; }
h2 { font-size: 1.2em; margin-bottom: 0.4em; margin-top: 0.5em; }
li { font-size: 0.8em; line-height: 1.4; }
ul { margin: 0.3em 0; padding-left: 1.5em; }
p { font-size: 0.85em; margin: 0.3em 0; }
</style>

# What Else?

<div class="columns">
<div>

## • Conference Dinners #hygge 🍻

## • Event Modeling Workshop&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📋→ 👨 👱‍♂️ 👨‍🦰 🧔 → 🟦🟧🟩🪟⚙️

## • The Future of SWE in the Age of AI, and how EM and ES fit 💯

</div>
<div>

## • Q&A / AMA ⁉️

## • Live Event Modeling&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; by Martin and Adam ✨

## • Real-world Customer Walkthrough from Adaptech (Crypto Exchange) 💶

</div>
</div>

---
# Questions/Discussion
> 🧠 AI needs to have a good system to be in. It's wasted on the stupid right now!

> ▢ No (kanban/scrum) board

> 📊 Estimation/forecasting super-easy (a matter of counting)

> 🌊 Event models are the proper medium to communicate software (survived clouds, serverless, …, will survive AI, …)

> 👌 The beauty of event models is design at the right level (more details than textual specs, less details than code)

> 🧩 Event models work, because they hinge on facts no-one can dispute

> 📐 We need the AutoCAD for SWE!

<!-- provocations, food for thought, idea generators, … -->
---
![bg fit](../Files/chatgpt-event-model-sun.png)

<style scoped>
section {
  background-color: #f6e4c2;
}
</style>
