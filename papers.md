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
