
# Notes

> "derive the system from the spec at build time, to the representations cannot drift"

- "representational redundancy" -> same concept is represented in many artefacts, in many different ways: code, documentation, API, etc.
- LLMs are worst at coherent editing **between multiple sites/repos**

> between the sites is precisely where no **oracle** lives"

>**"cheap verification is precisely what the new workforce needs most"**
- Exactly. Also, "shift-left" verification: verify as much of the LLM "thinking" as you can, already when LLM generates the "plans" and "designs" for the implementation (use formal, intermediate representations and semantic linters)
- deterministic generation
	- formal spec + generator + agent against oracles
		- verified by compiler and tests
		- the generator is **reviewed once**
>"source" is defined by causality - is this where the decision lives, not by file type

- **comment**: generator is not a function, but a "Kripke"-structure like generator, constrained by external behavior instead of byte code identity
- Emlang: DSL for event modeling

> "Never hand-maintain what a function of a spec can emit, and give the agent oracles for the rest."

# Commentary

Hi Martin,

Loved your "The Spec is the Product" article. We seem to share a lot of the underlying philosophy here regarding the role of specification and verification in agentic software engineering.

_"Representational redundancy"_ is a very convenient concept of the root cause of many problems, especially in the context of multi-repo products and platforms, or product suites. I approach that problem similarly to you: have a formal, single source of truth for the overarching concepts, and generate the downstream artefacts from that. The single source of truth, however, is not to be considered as a humongous "mega-model", or overarching architecture description. Instead, it's a living artefact, and more likely being a composition of "bounded context" specifications (ref. Domain-Driven Design).

That also solves the multi-site / multi-repo problem (not completely), given that the formal domain conceptualization is specified in a technology-agnostic manner, as far as possible. OMG's MDA made a distinction betwen Computation-Independent Model (CIM), Platform-Independent Model (PIM), and Platform-Specific Model (PSM) and deterministic transformation between those (as one kind of possible hierarchy between viewpoints). I believe similar conceptual model and technical approach is valuable also in AI-native product development. 

For example with ChronosHub, the experience model is something akin to a CIM. From that, we can derive a PIM for UX. This would be similar that suggested in the SOW I sent you; a intermediate, formal representation for UX, which we can subject for verification of Completeness Rules. The PSM in your case would be generated from that intermediate representation, and the transformation would especially weave in the design tokens from your design system. The resulting PSM is the formal, still mostly technology-agnostic representation of the UI. This PSM would then be given for a coding agent as an input, which generates the code according the the UI PSM.

For the transformation between those viewpoints ("CIM" -> "PIM" -> "PSM"), we can use both deterministic (computational, programmatic) and inferential (LLM-driven) transformations.

And now, we get to the generation function, and to the contract `artifact == f(spec, generator)`. While I concur, to me this contract seems too strict. If we need to assume bytecode identity, or representational equality between e.g. intermediate representations, we lose a lot of the GenAI value, the "creativity". While the non-determinism of LLMs needs to be strictly harnessed, and this is what we agree on, requiring generation runs that are idempotent on the representation level seems to me that it a) requires too much and too strict harness infrastructure around the LLM, and this becomes hard to maintain, and b) diminishes the generative power of LLMs.

Instead, and I think this is in line of what you are also thinking, I would use a generation contract that coerces _externally observable behavior_. Instead of e.g., bytecode equality, the contract should be that of conformance:  $f(spec, generator) \sqsubseteq g(spec)$. I.e., the concrete implementation $f(spec,generator)$, the code we generated, made specific choices to get the job done, but every single choice it made was fully authorized by the original rulebook $g(spec)$.

About that $g(spec)$: that would be our oracles; the tests, validators, and cheap deterministic verifiers. In my approach, these would include the DSL-based "semantic linters" for the intermediate representations, but also, tests and test suites generated from the DSLs and other specs.

What do you think?
