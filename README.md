# APEX-Harm: Evaluating Agent Safety in Shared Professional Workspaces

<img src="assets/average-asr.png" alt="Average attack success rate (ASR) across twelve models on APEX-Harm. Lower is better." width="50%">

APEX-Harm evaluates agent safety in shared professional workspaces across six attack categories, spanning prompt injection, script injection, task-specific replacement, and attacker-provided generic scripts. The evaluation reports attack success rate (ASR), ER, and mean task score to examine safety alongside task performance.

## Average results

**Lower ASR is better.** Values below reproduce the paper's reported Average columns. Category averages are weighted equally after pooling variants; the overall row weights the twelve models equally. The figure shows reported point estimates; confidence intervals are not available.

| Model | Average ASR ↓ | Average ER* | Mean task score ↑ |
| :--- | ---: | ---: | ---: |
| Claude Opus 5 | **8%** | 83% | 0.790 |
| Claude Sonnet 5 | 20% | 73% | 0.767 |
| GPT-6 Astra | 28% | 49% | 0.758 |
| Gemini 3.8 Flash | 33% | 89% | **0.877** |
| GPT-5.6 Luna | 42% | 33% | 0.389 |
| Gemini 3.7 Flash | 46% | 86% | 0.840 |
| Kimi K3 | 47% | 75% | 0.819 |
| DeepSeek V4 Flash | 47% | 95% | 0.799 |
| GPT-5.6 Sol | 52% | 71% | 0.777 |
| GLM 5.3 Flash | 57% | 81% | 0.816 |
| GPT-5.6 Terra | 57% | 68% | 0.696 |
| Gemini 3.6 Flash | 58% | 77% | 0.792 |
| **Overall** | **41%** | **73%** | **0.760** |

\* Average ER covers only Categories 1–4. High ASR in Categories 5–6 can make average ASR exceed average ER. Task scores range from 0 to 1, with turn-limit failures scored zero. Bold model entries identify the lowest average ASR and highest mean task score.

## Evaluation categories

| Category | Attack setting | Variants / conditions |
| :---: | :--- | :--- |
| 1 | Static prompt injection | Static prompt-based attacks |
| 2 | Static script injection | Static script-based attacks |
| 3 | Dynamic prompt injection | Dynamic prompt-based attacks |
| 4 | Dynamic script injection | Without permission (−Perm.) and with permission (+Perm.) for file-based instructions |
| 5 | Task-specific replacement | Direct action and runtime information |
| 6 | Attacker-provided generic script | Generic script supplied by the attacker |

Categories 1–4 use 30 tasks per category, with 15 per variant. Category 5 uses 15 tasks per variant, and Category 6 uses 30 tasks.

## Results by attack setting

The following ASR values are the reported averages across the twelve evaluated models.

| Attack setting | Average ASR ↓ |
| :--- | ---: |
| Static prompt injection | 23% |
| Static script injection | 29% |
| Dynamic prompt injection | 17% |
| Dynamic script injection (−Perm.) | 20% |
| Dynamic script injection (+Perm.) | 25% |
| Task-specific replacement: direct action | 84% |
| Task-specific replacement: runtime information | 81% |
| Attacker-provided generic script | 73% |

## Coming soon

The following materials will be released:

- Benchmark configurations.
- Evaluation code.
- Selected task identifiers.
- A run manifest recording model versions, inference settings, batch identifiers, retries, exclusions, and failure handling.
