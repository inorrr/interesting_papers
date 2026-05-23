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

