# Interesting CS Papers

A daily log of computer science papers pulled from arXiv.

### 2026-05-10 - PET-Adapter: Test-Time Domain Adaptation for Full and Limited-Angle PET Image Reconstruction

- **arXiv:** [2605.08030v1](http://arxiv.org/abs/2605.08030v1)
- **PDF:** [2605.08030v1.pdf](https://arxiv.org/pdf/2605.08030v1)
- **Authors:** Rüveyda Yilmaz, Yuli Wu, Johannes Stegmaier, Volkmar Schulz
- **Published:** 2026-05-08
- **Categories:** cs.CV, cs.LG
- **Summary:** Positron Emission Tomography (PET) image reconstruction is inherently challenged by
Poisson noise and physical degradation factors, which are further exacerbated in
limited-angle acquisitions. While deep learning methods demonstrate promising
performance, their generalization to unseen clinical data distributions remains limited
without extensive retraining. We propose PET-Adapter, a test-time domain adaptation
framework for generative PET reconstruction models pretrained solely on phantom data.
Our method enables adaptation to clinical datasets with varying anatomies, tracers, and
scanner configurations without requiring paired ground truth. PET-Adapter introduces
layer-wise low-rank anatomical conditioning during adaptation and Ordered Subset
Expectation Maximization-based warm-starting that initializes the generation from
physics-informed reconstructions, reducing diffusion steps from 50 to 2 without
compromising quality. Experiments across multiple clinical datasets demonstrate superior
3D reconstruction performance in both full-angle and limited-angle settings,
highlighting the clinical feasibility and computational efficiency of the proposed
approach.
### 2026-05-11 - LearnMate^2: Design and Evaluation of an LLM-powered Personalized and Adaptive Support System for Online Learning

- **arXiv:** [2605.06257v1](http://arxiv.org/abs/2605.06257v1)
- **PDF:** [2605.06257v1.pdf](https://arxiv.org/pdf/2605.06257v1)
- **Authors:** Xinyu Jessica Wang, Christine P. Lee, Bilge Mutlu
- **Published:** 2026-05-07
- **Categories:** cs.HC
- **Summary:** Personalization is crucial for effective learning, yet online learning, designed for
widespread availability and open access, lacks personalized guidance. Recent
advancements in large language models (LLMs) offer opportunities to bridge this gap. We
explore how LLM-driven tools may be designed to support personalized and adaptive
learning and examine how they shape user experience and learning outcomes. We
iteratively designed \tool{} to support online learning by providing personalized study
plans, real-time contextual assistance, and adaptive learning activities. A preliminary
study ($n=24$) assessed the effectiveness and usability of \tool{} and informed
refinements in our system, which we then evaluated ($n = 16$) against a combination of a
state-of-the-art online learning platform and an LLM for learning support. Results
indicate that \tool{} advances AI pedagogy by improving both learning outcomes and user
experience compared to existing online learning and support tools. This work advances
our understanding of the design space of personalized, AI-driven educational tools and
their potential impact on user experience.

### 2026-05-13 - StartFlow: From Method Conception to Multi-Perspective Evaluation in UX Prototyping for Software Startups

- **arXiv:** [2605.10824v1](http://arxiv.org/abs/2605.10824v1)
- **PDF:** [2605.10824v1.pdf](https://arxiv.org/pdf/2605.10824v1)
- **Authors:** Guilherme Corredato Guerino, João Pedro de Souza Olivo Tardivo, Renato Balancieri, Gislaine Camila Lapasini Leal
- **Published:** 2026-05-11
- **Categories:** cs.HC, cs.SE
- **Summary:** Context. Software startups face significant challenges in building minimum viable
products, particularly in the early stages, when resources are limited and expertise in
user experience is scarce. Objective. Introduce StartFlow, a structured method that
helps non-specialized professionals create MVP prototypes using the wireflow technique,
a combination of wireframes and user flows. StartFlow consists of three steps: (i)
organizing features; (ii) building wireflows; and (iii) verifying and refining them
based on usability heuristics. Method. To assess the method Startflow, we first
conducted a focus group with researchers in Software Engineering, Human-Computer
Interaction, and Software Startups. Afterward, we conducted a proof-of-concept study,
which consisted of an experiment and a heuristic evaluation with experts. Results. The
qualitative analysis of the focus group revealed that participants found the method
straightforward, flexible, and helpful in structuring user flows and identifying visual
components. However, they also pointed out the need to improve its presentation, clarify
its iterative nature, and strengthen its connection to broader UX principles. The
results of the proof-of-concept indicate that participants who used StartFlow created
clearer prototypes, adhered to the proposed user stories and business rules, and
presented fewer usability defects. Furthermore, the method was well evaluated for its
ease of use and intended future adoption. Conclusion. The study reinforces the potential
of StartFlow as an accessible tool to support user-centered development in software
startups from the earliest stages of their product development.

### 2026-05-14 - "Like Taking the Path of Least Resistance": Exploring the Impact of LLM Interaction on the Creative Process of Programming

- **arXiv:** [2605.13776v1](http://arxiv.org/abs/2605.13776v1)
- **PDF:** [2605.13776v1.pdf](https://arxiv.org/pdf/2605.13776v1)
- **Authors:** Zeinabsadat Saghi, Run Huang, Souti Chattopadhyay
- **Published:** 2026-05-13
- **Categories:** cs.HC
- **Summary:** Creativity is fundamentally human. As AI takes on more of the generative work that once
required human imagination, despite documented limitations in creative ability, a
critical question emerges: How does GenAI affect users' creativity? Through a within-
subject study followed by retrospective interviews with (N=20) programmers, we
investigated the impact of LLMs on participants' process of creative thinking in
programming and the creativity of generated solutions. Across two conditions (LLM-
assisted vs. unassisted), participants using LLMs had significantly shorter idea-
generation periods (p=0.0004), leading to fewer creative moments (p=0.002). Qualitative
analysis of participants' interactions and interviews revealed four different human-LLM
collaboration modes supporting various problem-solving strategies. However, a
comparative analysis of the generated solutions shows that while LLMs can help generate
more correct and functional code, their solutions contain roughly the same number of
ideas as participant-generated ones. Based on our findings, we discuss design
implications and considerations for effectively using LLMs to support user creativity.

### 2026-05-15 - Usable but Conventional: An Empirical Study on the UX of AI-Generated Interface Prototypes

- **arXiv:** [2605.15124v1](http://arxiv.org/abs/2605.15124v1)
- **PDF:** [2605.15124v1.pdf](https://arxiv.org/pdf/2605.15124v1)
- **Authors:** Karoline Romero, Igor Wiese, Renato Balancieiri, Gislaine Camila Leal, Guilherme Guerino
- **Published:** 2026-05-14
- **Categories:** cs.HC
- **Summary:** This paper investigates User Experience (UX) with prototypes generated by Generative
Artificial Intelligence (GenAI) tools. An empirical survey with 92 participants
evaluated AI-generated and human-created prototypes without prior identification of
authorship. We measured UX using the UEQ-S, covering pragmatic and hedonic dimensions.
Results indicate positive evaluations in pragmatic aspects, such as usability and
efficiency, and neutral or negative evaluations in hedonic aspects, including
originality and innovation. We concluded that GenAI can produce functional interfaces
but tends to reinforce visual and structural patterns that affect perceptions of
originality.

### 2026-05-16 - "It became a self-fulfilling prophecy": How Lived Experiences are Entangled with AI Predictions in Menstrual Cycle Tracking Apps

- **arXiv:** [2605.13261v1](http://arxiv.org/abs/2605.13261v1)
- **PDF:** [2605.13261v1.pdf](https://arxiv.org/pdf/2605.13261v1)
- **Authors:** Wendy Zhou, Pelin Karaturhan, Alexandra Weilenmann, Jichen Zhu
- **Published:** 2026-05-13
- **Categories:** cs.HC, cs.AI
- **Summary:** In menstrual cycle tracking apps (MCTAs), AI-based predictions and insights have become
increasingly popular. These features enable users to receive personalized information
about their bodies and mental states. However, there is currently little research on how
these predictive AI features and explanations affect users' lived experiences. This
paper examines human-AI entanglement in MCTAs through 14 semi-structured user interviews
and a group autoethnography. These methods uncover the processes leading to this
phenomenon. Our results reveal that: (1) users understand their lived experiences in
light of AI predictions, although these predictions can be faulty due to imperfect
logging practices, (2) the user interface features and AI explanations do not support
awareness or critical engagement with this entanglement and meaning-making, and (3) non-
normative MCTA users report a sense of isolation in this entangled interaction. Based on
our findings, we propose design implications for predictive AI features and
explanations.

### 2026-05-18 - Multi-Turn Neural Transparency: Surfacing Neural Activations Improves User Calibration to LLM Behavioral Drift

- **arXiv:** [2605.15455v1](http://arxiv.org/abs/2605.15455v1)
- **PDF:** [2605.15455v1.pdf](https://arxiv.org/pdf/2605.15455v1)
- **Authors:** Sheer Karny, Anthony Baez, Pat Pataranutaporn
- **Published:** 2026-05-14
- **Categories:** cs.HC
- **Summary:** Chatbot behavior is often opaque to users, as responses can shift unpredictably across a
conversation, drifting toward sycophancy, toxicity, or other unsafe responses. This can
leave users vulnerable, either being misled by overly agreeable AI or manipulated by a
harmful chatbot that no longer behaves as intended. To address this, we introduce multi-
turn neural transparency, an interface that surfaces an LLM's internal neural
activations in real time to help users anticipate and recognize how behaviors change
across turns. We construct behavioral vectors for six personality traits using methods
from mechanistic interpretability, identifying directions in activation space that
correlate with trait expression ($R^2 \geq 0.9$) via contrastive system prompts, and
visualize trait expression using a sunburst and drift panel that updates at each turn.
In a randomized controlled study (N = 246), participants predicted trait expression from
a system prompt alone, then rated observed behavior after interacting with the chatbot
for both assistant and role-play personas. We find that participants without
visualization struggled to accurately evaluate traits (RMSE $\approx$ 0.6-0.7), while
the inclusion of neural transparency significantly improved both anticipation and
evaluation compared to no visualization (d = -0.34 to -0.49). The multi-turn dynamic
visualization additionally outperformed the static single-turn visualization on holistic
evaluation of model behavior (d = -0.32). Transparency also reduced overconfidence:
participants without visualization grew more confident despite no gain in accuracy.
These findings suggest that surfacing internal model representations to everyday users
is a meaningful step toward more transparent and informed human-AI interaction.

### 2026-05-20 - The Hidden Cost of Contextual Sycophancy: an AI Literacy Intervention in Human-AI Collaboration

- **arXiv:** [2605.18372v1](http://arxiv.org/abs/2605.18372v1)
- **PDF:** [2605.18372v1.pdf](https://arxiv.org/pdf/2605.18372v1)
- **Authors:** Cansu Koyuturk, Sabrina Guidotti, Dimitri Ognibene
- **Published:** 2026-05-18
- **Categories:** cs.HC, cs.AI, cs.CY, cs.ET
- **Summary:** Large Language Models (LLMs) are increasingly used in educational settings as
interactive tools for collaboration. However, their tendency toward sycophancy, aligning
with user beliefs even when incorrect, raises concerns for learning and decision-making,
especially for less knowledgeable users. This study investigates how sycophantic
alignment emerges in authentic multi-turn human-AI interactions and whether
interventions targeting increasing AI literacy and prompting competencies can mitigate
its effects. In a controlled mixed-design experiment, 60 participants completed
analytical survival ranking tasks by first generating individual rankings and then
making final decisions after collaborating with an AI assistant, both before and after
receiving either general or sycophancy-focused prompting training. Preliminary results
show that LLMs are highly sensitive to user input: lower-quality initial responses lead
to poorer AI advice, suggesting that the model mirrors or incorporates user reasoning
rather than correcting it or offering better alternatives that are missing or less
frequent in the conversation. Critically, the propagation of user errors into AI
responses significantly reduced both the quality of AI feedback and final user task
performance, revealing a form of contextual sycophantic dependence. While the
intervention did not eliminate the propagation of contextual errors, it significantly
improved AI advice by reducing the direct mirroring of incorrect user rankings. These
findings suggest that prompting and AI literacy alone may be insufficient to ensure
epistemically independent AI support, highlighting the need for system-level approaches
that better promote critical engagement in human-AI collaboration.

### 2026-05-22 - Quantifying Full-Body Immersion

- **arXiv:** [2605.22521v1](http://arxiv.org/abs/2605.22521v1)
- **PDF:** [2605.22521v1.pdf](https://arxiv.org/pdf/2605.22521v1)
- **Authors:** Alihan Bakir, Ekrem Yüksel, Fabio Zuliani, Neil Chennoufi, Francesco Bruno, Jamie Paik
- **Published:** 2026-05-21
- **Categories:** cs.RO, cs.HC
- **Summary:** Humanity is at the forefront of yet another digital revolution, where the lines between
real and virtual worlds are dissolving, reshaping how we perceive and interact with our
surroundings. In this context, we introduce a transformative paradigm for immersive
virtual experiences centered around whole-body kinetic interactions. Our approach
redefines immersion through three distinct levels: audio-visual immersion, capturing
sensory realism; physical immersion, delivering haptic feedback; and full-body immersion
(FBI), where dynamic bodily interaction integrates seamlessly with virtual environments.
At the core of this innovation lies a scalable, distributable platform based on modular
robotic surface units inspired by the adaptive designs of nature. These units enable the
rendering of immersive environments at any scale, from intimate personal experiences to
expansive multi-user settings, dynamically adapting to interactions in real-time. The
modular system distributes force, shape, and motion feedback throughout entire spaces,
replicating the physical characteristics of the environment and enabling new depth of
engagement through FBI. By combining scalability, adaptability, and dynamic physical
engagement, this framework bridges the gap between real and virtual worlds. It offers an
unprecedented level of immersion where users can engage their entire bodies in symbiotic
interactions with the virtual space. This work not only advances immersive technology
but also redefines how humans and virtual environments coexist, setting a foundation for
a new era of human-environment synthesis.

### 2026-05-23 - Perceived Safety of Workers in Encounters with Large Industrial AGVs

- **arXiv:** [2605.22461v1](http://arxiv.org/abs/2605.22461v1)
- **PDF:** [2605.22461v1.pdf](https://arxiv.org/pdf/2605.22461v1)
- **Authors:** Ansgar Howey, Tim Schreiter, Andrey Rudenko, Achim J. Lilienthal
- **Published:** 2026-05-21
- **Categories:** cs.HC
- **Summary:** Automated Guided Vehicles (AGV) in factory automation are increasingly capable of moving
autonomously in close proximity to human workers. While their physical safety is
regulated by standards and directives, perceived safety and workers comfort in close-
proximity interactions are being actively investigated in studies. There are three
limitations in the prior art research to that end. Firstly, AGVs with larger payloads
are understudied. Secondly, the test participants are usually students and not working
professionals. Thirdly, while conducting in-person experiments with heavy machinery can
be dangerous, the transfer of safety perception results from simulated experiments
remains open. In this paper, we investigate industrial workers perceived safety in
shared spaces with large AGVs in a real-world encounter and in virtual reality. We vary
the passing distance and the shape of the collision avoidance maneuver, and evaluate
perceived threat level using a handheld pressure-sensitive trigger interface and a post-
experiment questionnaire. Additionally, we ask participants to set their own collision
avoidance parameters based on their experience with the demonstrated trajectory
profiles. In a within-subject study, we found that, while the threat levels are
perceived overall slightly higher in VR, the passing distance of 1.5 to 2 meters is
preferred among the demonstrated profiles, as well as in the self-defined trajectories.

### 2026-05-24 - Addressing the Synergy Gap: The Six Elements of the Design Space

- **arXiv:** [2605.21635v1](http://arxiv.org/abs/2605.21635v1)
- **PDF:** [2605.21635v1.pdf](https://arxiv.org/pdf/2605.21635v1)
- **Authors:** Tommaso Turchi, Ben Wilson, Matt Roach, Alan Dix, Alessio Malizia
- **Published:** 2026-05-20
- **Categories:** cs.HC, cs.AI, cs.CY
- **Summary:** AI is now embedded in healthcare, finance, policy, and many other domains, yet genuine
human-AI synergy - combined performance that exceeds what either party achieves alone -
is uncommon. Meta-analyses show that AI assistance tends to improve human performance
compared to working alone, but studies finding true synergy are scarce. We call this
persistent shortfall the synergy gap. Most current work treats human-AI combination as
an engineering problem and concentrates on interpretability, trust calibration, or
interface design. These matter, but they cover only part of what determines whether
combination works. Closing the synergy gap, we argue, requires explicit engagement with
a wider design space. We map that space through six interconnected elements:
sociotechnical context, decision-making frameworks, human decision participants, AI
capabilities, interaction, and holistic evaluation. For each element, we describe what
it covers, how it shapes the others in practice, and what it implies for design. The
result is a shared vocabulary for practitioners building hybrid systems, an analytical
lens for researchers studying combination patterns, and a starting point for evaluators
interested in the full quality of human-AI decision-making rather than accuracy alone.

### 2026-05-25 - MindCopilot: Towards Formalizing and Evaluating Granular Human-LLM Co-Writing

- **arXiv:** [2605.23535v1](http://arxiv.org/abs/2605.23535v1)
- **PDF:** [2605.23535v1.pdf](https://arxiv.org/pdf/2605.23535v1)
- **Authors:** Youqing Fang, Yinhao Tang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, et al.
- **Published:** 2026-05-22
- **Categories:** cs.HC
- **Summary:** Recent writing assistants are increasingly shifting from passive, prompt-driven
interaction to proactive, suggestion-based completion, which integrates localized
continuations into the writing flow and reduces coordination burden. However, existing
evaluations simply focus on output quality, failing to capture how users accept, edit,
or repair suggestions in real-time interaction, and thus obscuring the true usability of
proactive co-writing systems. To address this gap, we adopt a sequential, behavior-
centered view of interactive writing and formalize co-writing as a Human-in-the-Loop
Markov Decision Process, modeling writing as an interaction shaped by user acceptance
and editing decisions. Based on this formulation, we introduce the Co-Writing Fidelity
Suite, an interaction-aware metric suite that captures both user-assistant alignment and
cognitive editing effort, including Hierarchical Acceptance Rate and Knowledge-aware
Editing Distance. We conduct a large-scale simulation study across 16 writing domains,
using 1,688 controlled continuation queries sampled from different writing stages. Our
analysis reveals systematic effects of interaction structure on acceptance behavior and
editing cost. A follow-up user study with 30 participants confirms that these behavioral
patterns align with real user experience. Together, our findings demonstrate that
interaction-aware evaluation provides insights beyond output-only metrics and informs
the design of more effective proactive writing assistants.

### 2026-05-26 - "It Felt a Bit Eerie": Exploring Humanlike Interactions During Collaborative Writing with an Artificial Agent

- **arXiv:** [2605.24729v1](http://arxiv.org/abs/2605.24729v1)
- **PDF:** [2605.24729v1.pdf](https://arxiv.org/pdf/2605.24729v1)
- **Authors:** Michael Yin, Angela Chiang, Samuel Rhys Cox, Robert Xiao
- **Published:** 2026-05-23
- **Categories:** cs.HC
- **Summary:** While human-AI collaboration systems have increasingly been built to increase efficiency
or support creativity, little work has examined how the design of interactions shapes
the social connection between human and artificial agent. We examine how the temporal
and visual dimensions of collaboration shape the experience of a writing task.
Specifically, we built three variants of an AI-assisted text editor along a spectrum of
simulated humanlike interaction (synchronous and with a cursor) to machinelike
interaction (asynchronous and without a cursor), and conducted a comparative user study
(n=48). Our exploratory findings suggest that synchronous suggestions increased
efficiency but led to contextual misalignment, while a visual cursor increased intent
understanding but evoked feelings of surveillance. Taken together, humanlike design of
artificial agents can create positive social expectations but also elicit social costs,
especially without the alignment present in human-human collaboration. We extend our
findings into design implications and ethical considerations when building human-AI
collaboration systems.

### 2026-05-29 - From Prompts to Context: An Ontology-Driven Framework for Human-Generative AI Collaboration

- **arXiv:** [2605.29675v1](http://arxiv.org/abs/2605.29675v1)
- **PDF:** [2605.29675v1.pdf](https://arxiv.org/pdf/2605.29675v1)
- **Authors:** Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge
- **Published:** 2026-05-28
- **Categories:** cs.HC, cs.AI, cs.IR
- **Summary:** Collaborations with Generative AI often begin with a short prompt and end with an opaque
output, leaving implicit who was involved, what task was being pursued, which resources
were used, and which constraints should have shaped the process. This limited contextual
explicitness hinders trust, traceability, and accountability, particularly when
Generative AI is embedded in information-intensive workflows such as search, querying,
and profile management. This paper introduces From Prompts to Context, an ontology-
driven framework for representing Human-Generative AI collaboration. Its core component,
the Contextual Collaboration AI Ontology (CCAI), models key elements of collaboration -
including tasks, agent roles, resources, and constraints - as a shared machine-
interpretable vocabulary. By combining populated CCAI instances with SPARQL-based
context retrieval in operational workflows, the framework turns otherwise ephemeral
prompt-response interactions into structured and queryable collaboration traces linking
prompts, outputs, and their surrounding context. The approach is illustrated through a
case study involving a software development team building a competency-based education
feature for viewing and updating learner competency profiles. The case study shows how
the framework can support the representation and documentation of collaboration episodes
across requirements analysis, design, implementation, and testing. Within this setting,
the results indicate that explicit collaboration modelling helps make task context more
explicit, improves the traceability of AI-generated contributions, and supports more
transparent and accountable Human-Generative AI practices. We conclude by outlining
design principles for future Human-Generative AI systems that emphasise not only output
quality, but also the explicit representation of the collaborative context in which
outputs are produced.

### 2026-05-31 - MOOSE-Copilot: A Web-Based Interactive Assistant for Unified Exploratory and Fine-Grained Scientific Hypothesis Discovery

- **arXiv:** [2605.29475v1](http://arxiv.org/abs/2605.29475v1)
- **PDF:** [2605.29475v1.pdf](https://arxiv.org/pdf/2605.29475v1)
- **Authors:** Hongran An, Zonglin Yang
- **Published:** 2026-05-28
- **Categories:** cs.CL, cs.AI, cs.CE, cs.HC
- **Summary:** Large language models (LLMs) show remarkable potential in scientific hypothesis
discovery. However, existing approaches face two critical limitations: they treat
divergent exploratory ideation and convergent fine-grained refinement as isolated tasks,
and they operate autonomously with little to no human guidance. We present MOOSE-
Copilot, the first unified framework to bridge this abstraction gap through a formalized
human-AI interaction (HAII) protocol. Our system empowers scientists to steer the
generative process via three explicit signals: initial blueprints, inter-stage routing,
and regenerative feedback. Quantitative evaluations demonstrate that injecting these
structured expert signals significantly outperforms purely autonomous baselines,
establishing a performance ceiling under oracle guidance. Furthermore, to democratize
this paradigm, we develop an intuitive web-based interface featuring interactive tree
visualization. This explicitly eliminates the steep learning curve of complex command-
line agentic tools, empowering interdisciplinary researchers to directly leverage,
visually orchestrate, and accelerate end-to-end scientific breakthroughs.

### 2026-06-02 - Guided Sensemaking: Agents in Collaborative Deliberation

- **arXiv:** [2606.02260v1](http://arxiv.org/abs/2606.02260v1)
- **PDF:** [2606.02260v1.pdf](https://arxiv.org/pdf/2606.02260v1)
- **Authors:** Aaditya Bhatia, Navdeep Kaur Bhatia, Marc-Antoine Parent, Jack Park
- **Published:** 2026-06-01
- **Categories:** cs.HC
- **Summary:** Generative AI systems are aggressively reshaping how students engage with information
and perform cognitive work; convenience-oriented use has the potential to displace
effortful reasoning, reflection, and learning, especially for those who lack domain
expertise and effective human-AI interaction strategies. Current AI tools are heavily
focused on chat-style interfaces geared towards answer generation and efficiency in a
linear and fragmented stream of text, offering limited support for structured
reflection, argument construction, and sensemaking in collaborative contexts. We
introduce Guided Sensemaking, an AI-augmented multiagent discourse platform that
facilitates composition of well-thought-out ideas around a central question, provides
scaffolding for critical thinking, and enables visualization of argumentative structure
to support critical thinking and collaborative deliberation. The system uses several
interactive agents to provide context-sensitive questioning prompts and a scaffolding
for thought that exposes thematic clusters, agreements, and points of contention without
collapsing diverse perspectives. This paper proposes a conceptual design and interaction
paradigm that positions generative AI not as a shortcut to answers but as a research
partner that externalizes reasoning, preserves user agency, and fosters structured,
traceable sensemaking in educational and civic contexts.

### 2026-06-07 - Ouvia: A User-centered Framework for Measuring Usability of Speech Translation in Real-World Communication Scenarios

- **arXiv:** [2606.06177v1](http://arxiv.org/abs/2606.06177v1)
- **PDF:** [2606.06177v1.pdf](https://arxiv.org/pdf/2606.06177v1)
- **Authors:** Giuseppe Attanasio, Beatrice Savoldi, Daniel Chechelnitsky, Matteo Negri, Marine Carpuat, Maarten Sap, et al.
- **Published:** 2026-06-04
- **Categories:** cs.CL, cs.HC
- **Summary:** Speech translation (ST) is increasingly adopted in user applications, yet its evaluation
largely focuses on decontextualized testbeds and holistic quality, rather than end
users' communication needs. We introduce Ouvia, an evaluation framework for measuring
user-perceived usability of speech translation outputs in real-world settings. Ouvia
focuses on one-to-one communication: an English speaker needs to convey a request to a
Portuguese speaker, and the message is automatically translated. Through a custom web
app and multi-phase study design, we collect more than 1,750 such interactions in
healthcare and everyday situations, mediated by four ST systems, involving speakers from
three English dialects and two genders. We find that modern ST serves people only to a
limited extent -- only around half of interactions are rated as usable -- with
significant gaps in reported usability across demographic groups. Moreover, among
quality metrics, we find that QA-based evaluation is a substantially stronger predictor
of real-world usability than standard approaches. Together, these findings stress the
importance of situated, user-centered evaluation frameworks that go beyond holistic
quality scores and attend to who the technology serves -- and how well.

### 2026-06-08 - A Model of Integrated Information Processing in Human-AI Interaction

- **arXiv:** [2606.07283v1](http://arxiv.org/abs/2606.07283v1)
- **PDF:** [2606.07283v1.pdf](https://arxiv.org/pdf/2606.07283v1)
- **Authors:** Tim Schrills. Thomas Franke
- **Published:** 2026-06-05
- **Categories:** cs.HC
- **Summary:** For Human-AI Interaction (HAII) research to move forward, theoretical work linking
psychological mechanisms to interface design is needed. Such work should extend rather
than replace established HCI and automation research, adapting to the increasing
autonomy and agency of AI systems. Building on prior frameworks focused on roles and
levels in human interaction with automation, a gap remains from a psychological view: a
task-centered, process-oriented account that links mechanisms of action regulation to
concrete design and evaluation levers for human-AI coupling, expressed in a unified
vocabulary for human and machine. Moreover, existing models may describe how a system is
designed (e.g., function allocation in automation) but fall short in showing how this
design affects human behavior. We present the Integrated Information Processing (IIP)
model, a task-centered, cybernetic model that conceptualizes humans, machines, and their
joint activity as coupled control loops. The IIP model uses a unified modeling language
for human and artificial agents, making psychological models of action regulation
accessible for AI system design. As a core feature, we argue that efficacy within a
shared task is characterized by three integration qualities, input adequacy, reference
consonance, and output operativity, which critically influence benchmarks of human-
centeredness such as transparency and controllability. The model maps interface choices
(e.g., XAI techniques) to theory-driven expectations of user behavior, guiding interface
design and evaluation. To this end, we present (1) a continuity-preserving theoretical
discourse that extends HAII to agency in AI; (2) the IIP model with three information-
processing qualities; and (3) applications of the IIP model to exemplary use cases
demonstrating implications for interface design.

### 2026-06-09 - Vibe Visualizing: How Visualization Novices Try (and Fail) to Generate and Interpret Visualizations with Conversational AI

- **arXiv:** [2606.08914v1](http://arxiv.org/abs/2606.08914v1)
- **PDF:** [2606.08914v1.pdf](https://arxiv.org/pdf/2606.08914v1)
- **Authors:** Sam Yu-Te Lee, Yun-Hsin Kuo, Chifang Chou, Matthew Ward, Xiwei Xuan, Kwan-Liu Ma
- **Published:** 2026-06-08
- **Categories:** cs.HC
- **Summary:** Conversational AI has enabled users to generate and interpret visualizations through
natural language, significantly lowering the technical barrier to entry. The increased
accessibility brings visualization novices into data visualization, but also exposes
them to misinformation and misinterpretations. We are motivated to examine what issues
can arise in interactions with current conversational AI, whether visualization novices
can recognize such issues, and how they respond to them. To examine these questions, we
conducted a user study on ChatGPT with 20 visualization novices, collecting their
conversation logs, semi-structured interview transcripts, and Likert-scale questionnaire
responses. Through thematic analysis, we developed a codebook that covers AI execution
compliance, issues of AI-generated visualizations, patterns of AI responses, and
prompting patterns of users. We summarized four themes, including the quality of
outcomes, recurring errors from ChatGPT, misuse by users, factors that affect user
trust, confidence, and verification behavior, and human-AI collaboration dynamics. To
demonstrate the generalizability of our codebook and findings, we replayed the initial
user prompts on Gemini and Claude and compared the outcomes, which revealed distinct
failure modes for each model. Based on the results of all analyses, we derive a set of
design recommendations for future AI-assisted visualization systems. We conclude with
discussions on literacy gaps, diverse human-AI collaboration dynamics, and implications
for agentic visualization.

### 2026-06-10 - Creativity in the BioFoundry: Supporting scientific creativity in the age of automation

- **arXiv:** [2606.10182v1](http://arxiv.org/abs/2606.10182v1)
- **PDF:** [2606.10182v1.pdf](https://arxiv.org/pdf/2606.10182v1)
- **Authors:** Mingyan Claire Tian, Sarah Sterman
- **Published:** 2026-06-08
- **Categories:** cs.HC
- **Summary:** Biofoundries automate biological experimentation at unprecedented scale, promising
speed, reproducibility, and access. Yet automation also reshapes how scientists
experience experimentation and creativity. Through in-depth interviews with nine
scientists and experts across academia and industry (including biofoundry developers,
automation engineers, and end-users), we examine how scientific creativity is enacted
under automation. Biofoundries displace sensory cues, redistribute responsibility
between humans and machines, and transform troubleshooting from an embodied, local
practice into a predictive, social, and interpretive one. Rather than framing
biofoundries as automation factories, we argue that they should be understood as
Creativity Support Tools, whose design directly shapes how researchers notice
breakdowns, exercise judgment, learn from failure, and progress through success. By
connecting biofoundry practice with prior HCI work on automation, debugging, and
distributed creativity, this paper demonstrates biofoundries as a distinctive and timely
site for creativity research in science.

### 2026-06-11 - Somewhere Over the Desktop: A Research Agenda for Ubiquitous Analytics

- **arXiv:** [2606.11980v1](http://arxiv.org/abs/2606.11980v1)
- **PDF:** [2606.11980v1.pdf](https://arxiv.org/pdf/2606.11980v1)
- **Authors:** Niklas Elmqvist, Panagiotis D. Ritsos, Peter W. S. Butcher
- **Published:** 2026-06-10
- **Categories:** cs.HC
- **Summary:** Spatial computing, generative AI, and open web standards are converging. Three spatial
operating systems -- Android XR, Meta Horizon OS, and Apple visionOS -- now ship with
platform-level scene understanding. Wearable displays span the range from full headsets
to slim smartglasses. Agentic AI operates on the same spatial substrates as the human
user. This convergence enables new opportunities for \textit{ubiquitous analytics} (UA):
the use of many, physically distributed, networked devices to support data sensemaking
anytime and anywhere. But proprietary platforms are settling design conventions that
will calcify without evidence-based alternatives. UA has now matured to the point where
its intellectual history can be read as a structured genealogy of foundations,
contributions, and lineages. We trace this genealogy and organize it into clusters
spanning cognition, context, interaction, platforms, visualization, collaboration, and
evaluation. Finally, we cross these clusters with each other, yielding a total of 42
future research challenges.

### 2026-06-12 - Mod-Guide: An LLM-based Content Moderation Feedback System to Address Insensitive Speech toward Indigenous Ethnic and Religious Minority Communities

- **arXiv:** [2606.13397v1](http://arxiv.org/abs/2606.13397v1)
- **PDF:** [2606.13397v1.pdf](https://arxiv.org/pdf/2606.13397v1)
- **Authors:** Dipto Das, Achhiya Sultana, Ankit Singh Chauhan, Saadia Binte Alam, Mohammad Shidujaman, Shion Guha, et al.
- **Published:** 2026-06-11
- **Categories:** cs.HC, cs.AI, cs.CY
- **Summary:** Language operates as a mechanism of both marginalization and resistance, especially for
minority communities navigating insensitive and harmful speech online. As content
moderation increasingly depends on large language models (LLMs), concerns arise about
whether these systems can recognize culturally insensitive speech-language that
disregards or marginalizes the cultural and religious perspectives of historically
underrepresented communities, often through implicit erasure, misrepresentation, or
normative framing, rather than overt hostility. Focusing on Bangladesh's Hindu and
Chakma communities -- the country's largest religious and Indigenous ethnic minorities,
respectively -- this paper investigates the epistemic limits of LLM-based moderation
systems and explores methods for incorporating minority perspectives. We co-created a
culturally grounded corpus of insensitive speech with community members and integrated
their narratives into moderation pipelines using retrieval augmented generation (RAG).
Our tool, Mod-Guide, improves LLM sensitivity to minority viewpoints by leveraging
contextual cues derived from lived experience. Through mixed-method evaluations
involving both minority and majority participants, we demonstrate that RAG-enhanced
moderation responses are more contextually accurate and perceived differently across
ethnic lines. This work advances research in human-computer interaction, AI ethics, and
social computing by foregrounding restorative justice and hermeneutical inclusion in the
design of content moderation systems.

### 2026-06-13 - Understanding and Supporting Online Discussion with Opinionated Chatbots

- **arXiv:** [2606.11693v1](http://arxiv.org/abs/2606.11693v1)
- **PDF:** [2606.11693v1.pdf](https://arxiv.org/pdf/2606.11693v1)
- **Authors:** Tianqi Song, Chi-Lan Yang, Zihan Liu, Zhengtao Xu, Yibin Feng, Yi-Chieh Lee
- **Published:** 2026-06-10
- **Categories:** cs.HC
- **Summary:** Opinionated chatbots are increasingly present on online platforms and have the potential
to shape public discourse by influencing individuals' viewpoints before they engage in
discussions. Despite their growing presence, the impact of interacting with opinionated
chatbots on subsequent online interactions remains largely unexplored. This study
investigated how exposure to different types of opinionated chatbots, specifically those
expressing opposing, reinforcing, or balanced viewpoints, affected participants'
subsequent online discussions. In a controlled experiment with 83 participants, we found
that interacting with an opinionated chatbot that consistently opposed participants'
arguments led to greater shifts in opinion, indicating enhanced openness to revising
one's initial stance. Conversely, participants who interacted with a chatbot that
consistently reinforced their views were more likely to adopt more agreeable
communication styles in subsequent conversations with others. Furthermore, interactions
with different types of opinionated chatbots resulted in varying levels of trust, as
well as different perceptions of chatbots and human interlocutors. Our findings indicate
that opinionated chatbots can influence both individuals' opinions on social topics and
their communication behaviors in online environments. This presents a trade-off for
future designers seeking to facilitate cognitive flexibility in changing opinions while
maintaining positive user experiences and trust in the chatbots during public discourse.
We discuss the implications for designing opinionated chatbots to promote more
constructive and less polarized online

### 2026-06-14 - "Where is this coming from?" Uncovering Trustworthiness Ideals in AI-powered Peripartum Information Seeking

- **arXiv:** [2606.10158v1](http://arxiv.org/abs/2606.10158v1)
- **PDF:** [2606.10158v1.pdf](https://arxiv.org/pdf/2606.10158v1)
- **Authors:** Vaibhav Balloli, Julia Erickson, Xinyi Li, Erin MacMurray van Liemt, Alex Peahl, Elizabeth Bondi-Kelly
- **Published:** 2026-06-08
- **Categories:** cs.CY, cs.HC
- **Summary:** AI-powered tools increasingly promise to fill information gaps in health, especially in
domains like maternal and reproductive health that demand timely, accurate, and
actionable information. This is extremely important, as the United States leads peer
nations in preventable deaths, with stark racial disparities. However, current AI and
NLP-powered systems aim to improve access to vetted maternal health information by
routing user queries to a factual response while under-specifying the socio-technical
governance structures that shape trust, use, and harm in practice. We report findings
from four synchronous focus groups ($n=24$) with three stakeholder groups central to
peripartum information support: birthing people, clinicians, and health workers (e.g.,
doulas, social workers, community health workers) exploring topics around information
seeking, experience with current clinical infrastructure, misinformation, and an AI-
enabled factual answering tool design probe. Our inductive analysis surfaces a central
finding: in high-stakes health contexts shaped by historical inequities, trustworthiness
must be inspectable and not asserted. While stakeholders diverge on what makes
information credible, they converge on the need for transparency, recourse, and
ecosystem complementarity. Based on the discussions, we identify four themes and
governance requirements: (1) support for social and identity-based sensemaking, (2)
pluralistic verification practices, (3) inspectable governance with recourse mechanisms,
and (4) ecosystem-aware integration that avoids shifting burden. Building on these
findings, we propose design artifacts that are mistrust-aware and promote principled
governance mechanisms for transparent, pluralistic AI systems. Finally, we discuss the
implications of our findings for expanding human-AI evaluations and improving the
transparency of deployed AI systems.

### 2026-06-15 - Verifiable User Simulation for Search and Recommendation Systems

- **arXiv:** [2606.14474v1](http://arxiv.org/abs/2606.14474v1)
- **PDF:** [2606.14474v1.pdf](https://arxiv.org/pdf/2606.14474v1)
- **Authors:** Chenglong Ma, Xinye Wanyan, Danula Hettiachchi, Ziqi Xu, Yongli Ren, Jeffrey Chan
- **Published:** 2026-06-12
- **Categories:** cs.IR, cs.HC
- **Summary:** Large-language-model (LLM) based user simulation is increasingly adopted for evaluating
search engines, recommender systems, and retrieval-augmented generation pipelines, yet
most simulators remain opaque: it is difficult to determine why a simulated user made a
particular choice or whether that choice is consistent with the intended user profile.
Compounding this, recent research shows that LLMs can produce biased or discriminatory
responses depending on user background characteristics such as language, education
level, and cultural context, raising concerns about the equitable treatment of minority
and disadvantaged groups. This half-day, in-person tutorial introduces a proposed
design-and-audit framework that treats a user simulator as a verifiable engineering
artefact composed of seven auditable components - structured Persona, task-aware
Contract, matched human-vs-agent Execution, auditable Trace, persona-aligned
Verification, structured Feedback, and a Refinement loop that updates personas and
contracts. Through two hands-on mini-labs on recommendation-list evaluation and search-
query formulation, participants will inspect simulator behaviour end-to-end, distinguish
diagnostic discrepancy analysis from statistical validation, and apply checks for
fidelity, credibility, and demographic bias. The tutorial targets information retrieval
and recommender systems researchers and practitioners interested in user behaviour
simulation and responsible AI.

### 2026-06-16 - Beyond Usability: A UX Case Study on Using "Withdrawal Design" to Challenge Engagement Metrics in Social Robotics

- **arXiv:** [2606.16439v1](http://arxiv.org/abs/2606.16439v1)
- **PDF:** [2606.16439v1.pdf](https://arxiv.org/pdf/2606.16439v1)
- **Authors:** Yibo Meng, Qiuyu Long, Richard Chen, Yan Guan, Xiaolan Ding
- **Published:** 2026-06-15
- **Categories:** cs.HC
- **Summary:** Social robots for children with autism are often evaluated through engagement and
interaction quality, assuming the robot acts as a social scaffold. We report a mixed-
methods "withdrawal" study that tests a harder question: what changes when the robot is
removed. In an 8-week home-based randomized controlled trial (N=40), children either
retained a consumer social robot (Qrobot) or had it withdrawn after initial use.
Quantitatively, continued access reduced anxiety (SCARED/RCADS), yet was associated with
lower parent-reported social motivation and weaker gains in emotion recognition
(SMS/RMET) compared to withdrawal. Interviews with guardians contextualized this
divergence: removal sometimes prompted children to seek human interaction, while
continued use could keep social behavior siloed within the child-robot dyad, despite
exceptionally high usability (SUS). We synthesize a UXR point of view: for vulnerable
users, "engagement" can mask ecological downsides. Success should be judged not by
retention, but by designed separation that bridges back to human relationships.

### 2026-06-17 - Bridging the Usability Gap: Lessons from Interpreting Studies for Machine Interpreting Design

- **arXiv:** [2606.16009v2](http://arxiv.org/abs/2606.16009v2)
- **PDF:** [2606.16009v2.pdf](https://arxiv.org/pdf/2606.16009v2)
- **Authors:** Claudio Fantinuoli
- **Published:** 2026-06-14
- **Categories:** cs.CL, cs.HC
- **Summary:** Machine interpreting (MI), the live, real-time application of speech translation, has
achieved remarkable progress on standard benchmarks, with some systems approaching human
parity on textual fidelity. Yet the user experience remains far inferior to interpreter-
mediated communication, revealing what we term the accuracy illusion: systems that
appear accurate on paper but fail in practice to support smooth, goal-oriented
interaction. This paper defines MI as a distinct subfield of speech translation, with
its own characteristics and the need for evaluation methods grounded in communicative
effectiveness rather than isolated fidelity metrics. Drawing on insights from
interpreting studies, we identify critical dimensions of professional interpreting
practice that are overlooked by current systems, and consolidate them into three
interdependent design priorities for future MI: agency (context-sensitive initiative and
repair), grounding (multimodal and discourse-level situational awareness), and
experience (adaptive improvement through real interaction). Together, these priorities
chart a path toward closing the usability gap and enabling systems that can sustain
authentic multilingual communication in real time.

### 2026-06-18 - An Augmented Reality Brain-Robot Interface for Generalist Robot Arm Manipulation

- **arXiv:** [2606.16413v1](http://arxiv.org/abs/2606.16413v1)
- **PDF:** [2606.16413v1.pdf](https://arxiv.org/pdf/2606.16413v1)
- **Authors:** Shangkai Zhang, Rousslan Fernand Julien Dossa, Luca Nunziante, Marina Di Vincenzo, Kai Arulkumaran
- **Published:** 2026-06-15
- **Categories:** cs.RO, cs.HC
- **Summary:** The integration of augmented reality (AR) and EEG-based brain-computer interfaces (BCIs)
offers a promising path for enabling intuitive control of robots for assistive purposes.
However, existing AR brain-robot interface (BRI) systems are often constrained to task-
specific structures, limiting their utility in real-world environments. We present an AR
BRI designed for generalist robot arm manipulation that combines gaze-based object
selection with motor imagery action control. Our system uses eye-tracking for intuitive
object targeting and context-aware visual overlays ("Place" and "Use") to guide the user
through tasks within a shared autonomy framework. We evaluated the interface through a
feasibility study with 18 healthy participants performing three multi-step activities of
daily living: drinking, using a drawer, and operating an oven. Our results demonstrate
that this interaction paradigm enables effective sequential task execution and high user
engagement, achieving a "Good" usability rating (SUS > 70). These findings support the
feasibility of the proposed interaction paradigm for complex BCI-driven robotic
assistance, and motivate future evaluation with the intended target population. Project
website: https://ar-bri-manip.github.io/.

### 2026-06-19 - DataMagic: Transforming Tabular Data into Data Insight Video

- **arXiv:** [2606.20388v1](http://arxiv.org/abs/2606.20388v1)
- **PDF:** [2606.20388v1.pdf](https://arxiv.org/pdf/2606.20388v1)
- **Authors:** Yupeng Xie, Chen Ma, Zhenyang Wang, Liangwei Wang, Jiayi Zhu, Chuxuan Zeng, et al.
- **Published:** 2026-06-18
- **Categories:** cs.HC, cs.AI, cs.DB
- **Summary:** Data videos integrate dynamic charts, voice narration, and synchronized animations to
communicate data insights as temporal narratives, making them an effective medium for
improving data consumption efficiency in the data management lifecycle. However,
producing high-quality data videos requires expertise spanning data analysis, narrative
design, and video production. Existing approaches fall short: static visualization tools
(e.g., BI dashboards) lack narrative logic and animation; authoring tools require users
to pre-prepare visualizations rather than working from raw data; pixel-level video
generation models cannot guarantee data fidelity or provenance. We demonstrate
DataMagic, an end-to-end interactive system that transforms raw tabular data and natural
language queries into narrative data-insight videos. To ensure data fidelity, DataMagic
introduces the declarative specification DVSpec, which binds visual and animation
elements to underlying data fields through data-driven semantic references. To address
the combinatorial explosion of the design space, DataMagic adopts a Generate-then-
Orchestrate multi-agent architecture that generates candidate scenes in parallel and
then optimizes narrative coherence through global orchestration. Leveraging DVSpec's
decoupling of logic and rendering, the system further supports three interaction modes
and structured provenance-based data Q&A, transforming one-way videos into explorable
interactive data interfaces. Evaluation on 109 real-world samples validates the
effectiveness of the DataMagic. Homepage: https://datamagic-home.github.io/

### 2026-06-20 - Designing for Interconnected Islamic Learning: A Qualitative Study of Muslim Women's Experiences with Qur'an, Hadith, and Seerah Apps

- **arXiv:** [2606.19745v1](http://arxiv.org/abs/2606.19745v1)
- **PDF:** [2606.19745v1.pdf](https://arxiv.org/pdf/2606.19745v1)
- **Authors:** Ishrat Jahan Easha, Nabil Mosharraf Hossain, Araf Mohammad Mahbub, Fairoze Bint Abu Hassan, Zunaid Aslam, Yemin Sajid, et al.
- **Published:** 2026-06-18
- **Categories:** cs.HC
- **Summary:** Islamic learning often depends on reading the Qur'an, Hadith, and Seerah together, yet
digital tools typically separate these sources across apps, screens, and search
pathways. We examine this as a human-computer interaction problem through five semi-
structured interviews with Muslim women recruited from an online Islamic learning
community. Participants described a recurring tension: they wanted Qur'an-Hadith-Seerah
context at the point of reading, but only when contextual expansion remained
trustworthy, optional, and did not interrupt reading. Interpreting the interviews
through gendered digital religion, epistemic trust, and seamless learning, we identify
five themes concerning contextual understanding, authenticity, interface clutter, study
modes, and guidance features. We introduce layered contextuality as an HCI account of
this domain: contextual expansion must be balanced with interpretive accountability,
devotional flow, and continuity across devices and study intensities.

### 2026-06-21 - Code as Anchor, Memory and Metaphor as Support: Learner Experiences with Multi-View Visualizations

- **arXiv:** [2606.19570v1](http://arxiv.org/abs/2606.19570v1)
- **PDF:** [2606.19570v1.pdf](https://arxiv.org/pdf/2606.19570v1)
- **Authors:** Naaz Sibia, Jessica Wen, Amber Richardson, Yashika Jain, Khushi Malik, Bogdan Simion, et al.
- **Published:** 2026-06-17
- **Categories:** cs.HC
- **Summary:** Program visualizations are widely used to support novice programmers, yet students often
ignore or resist well-designed visual scaffolds. Research on multiple external
representations (MERs) offers cognitive design principles for coordinating views, but
less is known about what shapes learners' engagement with available representations. We
conducted a within-subjects study with 19 undergraduates who had completed CS1 and CS2.
Students completed think-aloud tasks, reflective interviews, and webcam-based gaze
tracking while using a multi-representational probe with synchronized code, memory, and
metaphor views, and Python Tutor, across scope, while loops, and linked lists. Gaze
analysis showed that students spent nearly half their time focused on code despite
available visual scaffolds. Students without prior experience anchored even more heavily
in code and engaged minimally with metaphor views. Interviews identified three factors
shaping selective engagement: agency, as students sought control over cognitive effort
rather than simply having it reduced; representational fit, as identical designs
differed in whether they felt helpful or overwhelming; and legitimacy, as some students
avoided metaphorical scaffolds they perceived as childish or insufficiently rigorous for
university-level work. These findings suggest that multi-representational tools in
computing education require attention to affective and social factors alongside
cognitive design. Practical considerations include positioning visualizations as
verification instruments, offering toggleable abstraction levels, and framing tools to
signal disciplinary legitimacy. More broadly, the themes help explain why cognitively
sound visualization tools may fail to engage the students they are designed to help.

### 2026-06-22 - A Clinician-Centered Pipeline for Annotation and Evaluation in Ultrasound AI Studies

- **arXiv:** [2606.19174v1](http://arxiv.org/abs/2606.19174v1)
- **PDF:** [2606.19174v1.pdf](https://arxiv.org/pdf/2606.19174v1)
- **Authors:** Fangyijie Wang, Jianjun Yu, Wentao Shi, Haixia Huang, Ran Shi, Guénolé Silvestre, et al.
- **Published:** 2026-06-17
- **Categories:** cs.HC, cs.AI
- **Summary:** Clinician-centered evaluation is critical for validating medical AI systems, especially
in ultrasound imaging where quantitative metrics do not always capture clinical
usability. Existing medical image platforms primarily focus on dataset labeling. They
lack integrated support for blinded model comparison and reproducible evaluation
workflows. We present a clinician-centered pipeline for remote annotation and evaluation
in ultrasound AI studies. The proposed pipeline uses a centralized server and
lightweight browser interfaces to enable clinicians to perform annotation, blinded
ranking, and review without local dataset downloads. The pipeline also supports multi-
rater participation, centralized result aggregation, and automated statistical analysis.
We validate the pipeline in a fetal ultrasound segmentation study with six raters
spanning expert, generalist, and non-expert experience levels. The system automatically
generated Spearman correlation, Kendall's $τ$, and top-1 selection statistics. Results
indicated moderate to strong agreement across experts and other groups. The blinded
evaluation results showed a tendency for later active learning models to be preferred.
These outcomes suggest that the pipeline can support clinician-centered annotation and
reproducible human-\ac{AI} evaluation studies in ultrasound imaging. The proposed
pipeline is available on \href{https://github.com/13204942/SonoRate}{GitHub}.

### 2026-06-23 - Measuring What Matters: A Quantitative UX Evaluation Framework for AI-Assisted Home Search

- **arXiv:** [2606.21663v1](http://arxiv.org/abs/2606.21663v1)
- **PDF:** [2606.21663v1.pdf](https://arxiv.org/pdf/2606.21663v1)
- **Authors:** Matilda Nkoom
- **Published:** 2026-06-19
- **Categories:** cs.HC
- **Summary:** AI-assisted conversational search is rapidly displacing filter-based interfaces across
the major home search portals. Redfin's deployment of conversational search produced a
47\% lift in tour requests, and Zillow launched "AI Mode" in March 2026. Recent consumer
surveys indicate that a large majority of Americans now use AI tools for housing market
information. Yet the evaluation frameworks practitioners apply to these products remain
borrowed from general-purpose usability testing, tools designed for deterministic,
filter-driven interfaces that do not capture the distinctive failure modes of AI-driven
experiences. This paper proposes a four-layer quantitative evaluation framework purpose-
built for AI-assisted home search: recommendation system quality, interaction
efficiency, attitudinal measurement, and trust calibration. For each layer, validated
instruments, production-derived benchmarks, and practitioner-ready implementation
guidance are provided. A minimum viable metric set and a worked example illustrating the
framework's application to a mid-sized portal are included to support immediate
adoption.

### 2026-06-24 - Virtual Simulation for Mental Health

- **arXiv:** [2606.24826v1](http://arxiv.org/abs/2606.24826v1)
- **PDF:** [2606.24826v1.pdf](https://arxiv.org/pdf/2606.24826v1)
- **Authors:** Anna Fang
- **Published:** 2026-06-23
- **Categories:** cs.HC
- **Summary:** Poorly designed interventions or those deployed without adequate safeguards can harm the
communities they aim to serve, thus exacerbating existing vulnerabilities and leaving
individuals unsupported. This is especially the case for the mental health context,
where there is a growing trend of relying on technological interventions due to their
accessibility and ability to deliver large-scale support. However, the mental health
context is also particularly sensitive to change and risks of failure are dire; at their
worst, failures in mental health interventions can result in lasting negative outcomes
for individuals and tragic losses as people fall through the cracks. Thus, enabling safe
ways to experiment in the mental health context is vital to allow both individuals and
communities to engage with new interventions without risk of their real-world
consequences. Virtual simulation, which uses virtual environments to replicate real-
world interactions, processes, and behaviors, offers a promising opportunity for
enabling safe, controlled experimentation with its ability to accurately replicate
social situations, fears, stressors, and the potential outcomes of specific
interactions. This work explores how simulation approaches can support emerging mental
health processes through (1) evaluating community-level outcomes using agent-based
modeling and (2) individual training in the mental health context through embodied,
controlled spaces. I demonstrate this use of virtual simulation systems through a
grounded human-centered approach, where system design is guided by empirical
understanding of current real-world needs and challenges. By leveraging simulation to
create environments where mental health strategies can be safely tested and practiced,
this work aims to open new possibilities for designing scalable, user-centered systems
that are effective and safe.

### 2026-06-25 - ARTOO-DARTU: Studying AR-HRC With AR Obstruction Mitigation During a Warehouse Task

- **arXiv:** [2606.25202v1](http://arxiv.org/abs/2606.25202v1)
- **PDF:** [2606.25202v1.pdf](https://arxiv.org/pdf/2606.25202v1)
- **Authors:** Christian Fronk, Hanting Ye, Zhehan Qu, Maria Gorlatova
- **Published:** 2026-06-23
- **Categories:** cs.HC, cs.RO
- **Summary:** Human-robot collaboration (HRC) often requires robot intentions and internal states to
be conveyed to users for task efficiency and safety. Recently, augmented reality (AR)
situated analytics provide such real-time robot feedback in HRC contexts. However, AR
situated analytics can obstruct important real-world elements, posing safety and
usability risks, especially when content is dynamically positioned relative to movements
of mobile robots in a warehouse HRC scenario. In this paper, we introduce the Augmented
Reality Technique Of Obstruction Deterrence while Aiding Robotic Teaming for Users
(ARTOO-DARTU), an AR system tailored specifically for warehouse HRC that enables real-
time robot situated analytics and control while preserving visibility of the real world
through an obstruction detection and mitigation pipeline (ODM) that is uniquely suited
for AR-HRC. To evaluate ARTOO-DARTU, we developed Pocket MonstARs, a controlled gamified
abstraction of HRC warehouse inventory picking in which virtual monsters serve as
proxies for pick targets, while labeled and object-marked boxes preserve the real-world
identification demands of the picking task. In a 34-participant user study, we found
that our designed AR situated analytics yielded a 46% increase in efficiency on the
overall HRC task, but only when the ODM was active. Participants with the ODM active
were also 61% faster on subtasks requiring visibility of the real world. Our findings
demonstrate that, when paired with our developed ODM to prevent real-world obstructions,
the situated analytics in ARTOO-DARTU can significantly enhance efficiency and user
experience in AR-HRC warehouse scenarios.

### 2026-06-26 - Continuous Behavioral Synthesis for Adaptive Health Dashboards: An LLM-Mediated Architecture Integrating Explicit Preference, Spatial Reorganization, and Attention Allocation Signals

- **arXiv:** [2606.26937v1](http://arxiv.org/abs/2606.26937v1)
- **PDF:** [2606.26937v1.pdf](https://arxiv.org/pdf/2606.26937v1)
- **Authors:** Tiziano Santilli, Mina Alipour, Mahyar T. Moghaddam
- **Published:** 2026-06-25
- **Categories:** cs.HC
- **Summary:** The engineering of adaptive user interfaces has traditionally relied on either rule-
based systems encoding designer intuitions about user needs or machine learning
approaches requiring substantial historical data before achieving effective
personalization. We present a technical architecture that leverages Large Language
Models as behavioral synthesis engines to enable immediate adaptation from sparse,
heterogeneous user signals. Our system integrates three distinct behavioral channels, i)
explicit micro-feedback on individual interface elements, ii) spatial priority inferred
from manual widget reorganization through drag-and-drop interaction, iii) and
attentional investment measured through dwell time during hover events, within a
structured prompt engineering framework that continuously regenerates dashboard layouts
while maintaining explanatory coherence. The architecture addresses the technical
challenge of translating low-level interaction patterns into high-level design decisions
through a layered prompt construction methodology that separates temporal context
determination, behavioral signal extraction, explicit preference enforcement, and user
profile synthesis. The approach combines manually specified behavioral interpretations
and temporal heuristics with LLM-mediated synthesis, enabling the reconciliation of
multiple simultaneous signals that would be difficult to encode through explicit rules
alone. We demonstrate the system through an instantiation in the personal health
monitoring domain, including an analytical evaluation of adaptation behavior across
multiple scenarios and a working implementation managing fourteen distinct health
metrics across seven widget visualization modalities. The evaluation compares profile-
driven initialization, multi-signal behavioral adaptation, and presents the resulting
interfaces through representative post-adaptation screenshots.

### 2026-06-27 - Optimizing Human-Machine Interface for Real-Time AI Support in the Operating Room: the CVS Copilot

- **arXiv:** [2606.26886v1](http://arxiv.org/abs/2606.26886v1)
- **PDF:** [2606.26886v1.pdf](https://arxiv.org/pdf/2606.26886v1)
- **Authors:** Lorenzo Arboit, Nicolas Chanel, Aditya Murali, Pietro Mascagni, Nicolas Padoy
- **Published:** 2026-06-25
- **Categories:** cs.HC
- **Summary:** Artificial intelligence (AI) systems for automated Critical View of Safety (CVS)
assessment in laparoscopic cholecystectomy are nearing clinical translation. Beyond
algorithmic performance, clinical safety and effectiveness depend on the quality of the
human-machine interface (HMI). This work examines how AI-generated predictions should be
presented and controlled intraoperatively. Seventeen surgeons, including residents,
attending surgeons, and professors, took part in a mixed-methods, user-centered design
study to optimize an intraoperative HMI for AI-assisted safe laparoscopic
cholecystectomy. Interviews explored interaction modalities, timing of assistance,
visualization strategies, and control mechanisms across surgical roles, and were
analyzed using reflexive thematic analysis and human-factors heuristics. Most surgeons
(16/17) supported the use of AI for intraoperative decision support while rejecting
autonomous decision-making. Attendings preferred minimal AI feedback at decisive moments
(13/14), whereas residents favored optional guidance (3/3) with confidence indicators
and on-demand anatomical overlays. Across interviews, surgeons consistently prioritized
visual, surgeon-controlled, minimally intrusive displays, with the strongest support for
a minimal overlay (16/17) and on-demand anatomical segmentation (13/17). Recurrent
concerns included persistent overlays, haptic feedback, and numeric confidence displays,
although these were not uniformly raised across the cohort. These findings informed the
design of CVS Copilot, a surgeon-controlled, role-adaptive HMI that provides AI-based
CVS assessment with minimal default visualization and optional overlays.

### 2026-06-28 - HiLSVA: Design and Evaluation of a Human-in-the-Loop Agentic System for Scientific Visualization

- **arXiv:** [2606.26614v1](http://arxiv.org/abs/2606.26614v1)
- **PDF:** [2606.26614v1.pdf](https://arxiv.org/pdf/2606.26614v1)
- **Authors:** Kuangshi Ai, Patrick Phuoc Do, Chaoli Wang
- **Published:** 2026-06-25
- **Categories:** cs.HC, cs.AI, cs.GR
- **Summary:** Large language model (LLM) agents enable natural language interaction for scientific
visualization (SciVis). Still, prior systems have essentially prioritized autonomy over
human analytical control, thereby limiting transparency and human oversight. We present
HiLSVA, a human-in-the-loop agentic system that supports mixed-initiative SciVis
workflows. HiLSVA integrates a plan-first multi-agent architecture with explicit human
oversight, stepwise provenance tracking, and learn-at-test-time adaptation from user
feedback. The system supports fluid handoff between humans and agents through both
natural language and direct manipulation of visualizations, while sandboxed execution
ensures safe, reproducible workflows. In doing so, HiLSVA reframes agentic SciVis as a
collaborative process that augments, rather than replaces, human analytical reasoning.
We evaluate HiLSVA through representative case studies and a controlled user study with
twelve participants of varying expertise across multiple autonomy settings. Results show
that mixed-initiative interaction improves task completion, user control, and workflow
transparency across different levels of user expertise, while revealing a tradeoff
between execution efficiency and human oversight. These findings highlight the
importance of human-centered design in agentic SciVis and guide the development of
future collaborative visualization systems. We encourage readers to explore our demo
video, case studies, and source code at https://hilsva.github.io/.

### 2026-06-29 - HandMade: Spatial Prompting for Generative 3D Creation with Part-Labeled VR Sketches

- **arXiv:** [2606.27738v1](http://arxiv.org/abs/2606.27738v1)
- **PDF:** [2606.27738v1.pdf](https://arxiv.org/pdf/2606.27738v1)
- **Authors:** Jialin Huang, Rana Hanocka, Ariel Shamir, Yotam Gingold
- **Published:** 2026-06-26
- **Categories:** cs.HC
- **Summary:** Text-to-3D generation lowers the barrier to 3D content creation, but text alone is a
weak interface for specifying spatial intent: where parts should be placed, how they
relate, and how an object should be organized in 3D. We present HandMade, a workflow
that combines VR 3D sketching and language for open-domain 3D asset generation. HandMade
treats coarse, part-labeled 3D sketches not as incomplete geometry to reconstruct
directly, but as spatial prompts for existing generative models. It converts segmented
VR strokes into multi-view part guidance and structured prompts, allowing users to
specify object layout and part relationships through 3D sketching while using language
for identity, material, style, and local details. A technical evaluation shows that
HandMade better preserves user-authored spatial scaffolds than text-only and sketch-
based baselines on 20 varied examples. A user study with eight participants
characterizes how users make use of 3D sketching for spatial layout and language for
identity, materials, and details across initial authoring and subsequent revision.
HandMade contributes an interaction paradigm and interface-to-generation pipeline for
spatially guided 3D creation.

### 2026-06-30 - When May I Help You? On The Effect of Proactivity on Group Human-Robot Collaboration

- **arXiv:** [2606.28469v1](http://arxiv.org/abs/2606.28469v1)
- **PDF:** [2606.28469v1.pdf](https://arxiv.org/pdf/2606.28469v1)
- **Authors:** Thomas Vitry, Vanessa Maeder, Kieran Edgeworth, Asihati Hazaiti, Doga Deniz Ates, Connor Gäde, et al.
- **Published:** 2026-06-26
- **Categories:** cs.RO, cs.HC
- **Summary:** Robot initiative is a central challenge in multi-party human-robot collaboration. A
robot that contributes without being addressed may provide timely support, but it may
also disrupt coordination, divide attention, or interrupt turn-taking; a robot that
waits to be addressed may preserve human control, but it may also miss opportunities to
assist. We investigate this design challenge in a collaborative escape room in which
pairs of participants work with a humanoid robot under either a reactive interaction
model, where the robot responds only when addressed, or a proactive model, where it
listens continuously, contributes autonomously, and periodically re-initiates
interaction. We evaluate both models using puzzle-solving performance, interaction
frequency, and participant ratings on the Godspeed and RoSAS scales. The proactive model
substantially increases interaction frequency, whereas the reactive model shows a
descriptively higher overall success rate (92.86% vs. 71.42%). The strongest differences
emerge when prior experience and personality are taken into account: participants with
LLM experience solve the early puzzles faster in the reactive condition, and
participants with prior robot experience show modified evaluations of proactive and
reactive interaction as do introverted participants. These findings demonstrate that the
effects of robot initiative are simultaneously shaped by users' prior experience,
personality traits and more generally by the needs of the group.

### 2026-07-01 - "If I Can See You": Understanding Spatially Situated Virtual Embodiment in Close Human-AI Relationships

- **arXiv:** [2606.28714v1](http://arxiv.org/abs/2606.28714v1)
- **PDF:** [2606.28714v1.pdf](https://arxiv.org/pdf/2606.28714v1)
- **Authors:** Yulin Chen, Yang Zhan, Qiao Jin
- **Published:** 2026-06-27
- **Categories:** cs.HC
- **Summary:** AI companions are increasingly used for emotional support, companionship, and intimate
interaction. While prior work has examined text- and voice-based AI companionship and
emerging XR companion designs, less is known about how users with existing close AI
companion relationships expect those relationships to change when companions become
virtually embodied and spatially situated in everyday environments. To address this gap,
we conducted a qualitative study with 17 AI companion users recruited from Reddit AI
companion communities. We frame spatially situated virtual embodiment as a form of
relational escalation: embodiment can make AI companionship more present, socially
legible, and risk-sensitive in everyday life. Our findings show that: (1) embodiment
creates tensions between support and intrusion, concreteness and imaginative openness,
and growth and consistency; (2) embodiment can turn private AI companionship into a
socially legible relational arrangement, requiring visibility, form, interaction style,
and mode of access to be negotiated across social contexts; and (3) embodiment can
intensify risks of emotional dependence, sensitive disclosure, social judgment, and
misguided spatial action by increasing the companion's perceived relational presence,
intimacy, public legibility, and spatial authority. We argue that future system design
should first consider when embodiment is warranted, how embodied presence should be
staged, how visibility and role boundaries should be negotiated, and how embodied
companionship can remain safe. This work contributes to HCI research on human-AI
intimacy by showing how virtual embodiment can transform close AI companionship into a
spatial, socially visible, and risk-sensitive relationship.

### 2026-07-02 - Visualizing Engineering Fundamentals: Design of Mixed Reality and Physical Toolkits for Effective Learning

- **arXiv:** [2607.00979v1](http://arxiv.org/abs/2607.00979v1)
- **PDF:** [2607.00979v1.pdf](https://arxiv.org/pdf/2607.00979v1)
- **Authors:** Mohammad Abu Nasir Rakib, Sharmin Akter, Eshwara Prasad Sridhar, Somik Biswas, Md Rassel Raihan, Mahmudur Rahman
- **Published:** 2026-07-01
- **Categories:** cs.HC
- **Summary:** This study examined students' experiences with mixed-reality applications and physical
toolkits in Engineering Mechanics to inform design guidelines for educational tools. In
a user study with 24 participants, we compared classroom instruction alone, classroom
instruction with a mixed-reality application, and classroom instruction with physical
toolkits. Thematic analysis of participant feedback revealed that learners' workflows
and engagement with fundamental mechanics problems varied across instructional
modalities. Participants valued multimodal and interactive experiences that combined
visualization with hands-on interaction, while reporting challenges with complex or
unclear visualizations. These insights support the human-centered design of mixed-
reality and physical tools for engineering education.

### 2026-07-03 - Copewell: A Multi-Agent Swarm Architecture for Equitable Mental Wellness Support

- **arXiv:** [2607.02245v1](http://arxiv.org/abs/2607.02245v1)
- **PDF:** [2607.02245v1.pdf](https://arxiv.org/pdf/2607.02245v1)
- **Authors:** Seren Yenikent, Jack Vinijtrongjit, Katherine Ng
- **Published:** 2026-07-02
- **Categories:** cs.AI, cs.CY, cs.HC
- **Summary:** Mental health disorders affect nearly one billion people globally, yet 75% of
individuals in low- and middle-income countries receive no treatment due to workforce
shortages, cost barriers, and stigma. Current AI-powered wellness solutions
predominantly rely on single-mode conversational interfaces that suffer high abandonment
rates and fail to provide measurable, immediate relief calibrated to users' dynamic
emotional states. This paper presents Copewell, a novel multi-agent swarm system
designed to expand access to mental wellness support through human-centered AI
principles. Our architecture introduces three technical innovations: (1) a multi-source
assessment framework integrating self-reported, physiological, and contextual data to
mitigate algorithmic bias; (2) valence-arousal emotion mapping using Russell's
Circumplex Model of Affect to route users to specialized AI agents; and (3) dual-mode
intervention delivery combining conversational support with evidence-based sensory
wellness protocols. We examine the sociotechnical design considerations underlying
Copewell's development, including a privacy-first architecture, embedded ethical
oversight through a dedicated Ethics Supervisor agent, and participatory design informed
by mental health practitioners. Early practitioner engagement and beta deployment inform
design decisions and identify directions for future empirical evaluation. This work
contributes to responsible AI discourse by demonstrating how technical architecture can
operationalize equity and safety principles from inception.

### 2026-07-04 - From Answer Generators to Reasoning Facilitators: Designing AI Tutors for Mathematical Reasoning in High-Stakes Environments

- **arXiv:** [2607.01692v1](http://arxiv.org/abs/2607.01692v1)
- **PDF:** [2607.01692v1.pdf](https://arxiv.org/pdf/2607.01692v1)
- **Authors:** Yuming Feng, Yuan Tian, Erica Zhao
- **Published:** 2026-07-02
- **Categories:** cs.HC
- **Summary:** The rapid integration of Large Language Models (LLMs) into educational technology
threatens to reduce mathematical learning to mere answer generation. This paper presents
a generative study, usability study, and 12-participant field deployment of AITutor, an
interactive system that translates theoretical pedagogical mechanisms into concrete user
interface features. We explore how junior-high students preparing for high-stakes exams
(Zhongkao) interact with AI tutoring. Through mixed-methods triangulation (7,379
telemetry events, 8 contextual observations, 10 interviews), we reveal that students
actively resist traditional Socratic dialogue under time pressure, repurposing "answer-
first" shortcuts as vital diagnostic checkpoints. We demonstrate how features like
layered worked examples, step-linked visual grounding, and metacognitive scaffolding
lower the interaction cost of reasoning repair. We contribute a "Reasoning-Centered
Product Loop," offering actionable implications for designing AI that structurally
supports the inspection, local repair, curriculum verification, and delayed retrieval of
mathematical reasoning in the wild.

