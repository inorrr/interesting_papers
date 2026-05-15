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

