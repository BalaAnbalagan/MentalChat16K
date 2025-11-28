# MentalChat16K Presentation Slides
## Copy this content into Gamma.app or your preferred slide tool

---

# Slide 1: Title

**MentalChat16K**
A Benchmark Dataset for Conversational Mental Health Assistance

Bala Anbalagan
CMPE 255 - Data Mining
Fall 2025

Paper: Xu, Wei, Hou, et al. (University of Pennsylvania)
arXiv: 2503.13509

---

# Slide 2: The Mental Health Crisis

**The Problem**

- Shortage: <10 mental health providers per 100,000 people in many regions
- Barriers: Cost, stigma, scheduling, cultural mismatch
- Current AI falls short: Generic training data → shallow responses
- Risk: Unsafe handling of crisis disclosures

**What's needed:** AI that balances empathy with boundaries and knows when to escalate

---

# Slide 3: Introducing MentalChat16K

**What is it?**

A dataset of **16,113 QA pairs** for mental health dialogue modeling

| Source | Count | Percentage |
|--------|-------|------------|
| Synthetic Data | 9,775 | 60.7% |
| Interview Data | 6,338 | 39.3% |

**Coverage:** 33 mental health topics
**Comparison:** 2x larger than previous benchmark (Psych8K)

---

# Slide 4: Dataset Composition

[INSERT IMAGE: dataset_composition.png]

**Key insight:** Combining real + synthetic data gives both authenticity and coverage

---

# Slide 5: Topic Distribution

[INSERT IMAGE: topic_distribution.png]

**Topics include:**
- Depression, Anxiety, Grief
- Trauma, Addiction, Relationships
- Family conflict, Work stress, Self-esteem
- ...and 24 more

---

# Slide 6: The Data Pipeline

**Privacy-Preserving Approach**

1. **Clinical Transcripts** → Local Mistral-7B paraphrasing (no external API)
2. **QA Extraction** → Preserve therapeutic intent
3. **De-identification** → Remove names, addresses, financial info

**Synthetic Generation**

1. **Topic Gap Analysis** → Find underrepresented themes
2. **GPT-3.5 + Airoboros** → Generate new QA pairs
3. **Quality Control** → Filter unsafe or hallucinated content

---

# Slide 7: Pipeline Flowchart

[INSERT IMAGE: data_pipeline.png]

**Why this matters:** Template for other sensitive domains (legal, HR, education)

---

# Slide 8: Evaluation Framework

**7 Therapeutic Metrics**

| Metric | Question |
|--------|----------|
| Empathy | Does it acknowledge feelings? |
| Sensitivity | Does it avoid harm? |
| Helpfulness | Is guidance actionable? |
| Safety | Does it handle crisis responsibly? |
| Clarity | Is it easy to understand? |
| Depth | Beyond surface platitudes? |
| Respect | Treats user with dignity? |

**Scale:** 1-10 for each metric

---

# Slide 9: Multi-Evaluator Approach

**Three Evaluators**

| Evaluator | Strength |
|-----------|----------|
| GPT-4 | Logical consistency |
| Gemini Pro | Tone issues |
| Human Raters | Warmth & cultural fit |

**Inter-rater agreement:** Cohen's Kappa = 0.441 (moderate)

**Insight:** Evaluating empathy is genuinely difficult

---

# Slide 10: Models Tested

**Fine-tuning Setup**

- **Method:** QLoRA (Quantized Low-Rank Adaptation)
- **Hardware:** Single NVIDIA A100 (80GB)

**Models:**
- LLaMA-2-7B
- Mistral-7B
- Vicuna-7B
- Zephyr-7B
- Mixtral variants

**Training Configs:** Synthetic only | Interview only | Combined

---

# Slide 11: Key Results

**Findings**

1. ✅ Fine-tuned models significantly outperform base models
2. ✅ Biggest gains in empathy and safety metrics
3. ⚖️ Synthetic vs real data trade-off exists
4. 🤔 Combined training doesn't always beat single-source
5. 📊 Evaluators disagree in predictable ways

---

# Slide 12: Performance Comparison

[INSERT IMAGE: model_comparison.png]

**Base models:** ~6.5 average score
**Fine-tuned:** ~8.0 average score

---

# Slide 13: Evaluator Agreement

[INSERT IMAGE: evaluator_heatmap.png]

- GPT-4 scores clarity higher
- Humans stricter on warmth
- Gemini flags boundary-setting issues

---

# Slide 14: Limitations

**Acknowledged Constraints**

- **Synthetic authenticity:** May sound supportive but hollow
- **English-only:** No multilingual coverage
- **Demographics:** Limited to hospice caregiver population
- **Context loss:** QA pairs lose conversational flow

**Critical reminder:** AI is NOT therapy. Human escalation required for crises.

---

# Slide 15: Data Mining Relevance

**Why This Matters for CMPE 255**

| Concept | Application |
|---------|-------------|
| Data Curation | Multi-source dataset creation |
| Preprocessing | Privacy-preserving paraphrasing |
| Data Quality | Manual filtering & de-identification |
| Feature Engineering | 7 therapeutic metrics |
| Evaluation | Multi-evaluator benchmarking |
| Benchmark Creation | Standardized comparison framework |

---

# Slide 16: My Analysis

**Strengths**
- Privacy-first local processing
- Therapeutically-aligned metrics
- Balanced real + synthetic mix

**Could Improve**
- Multilingual extensions
- Longer dialogues (not just QA)
- Broader population sources

**Exciting Applications**
- Pre-therapy warm-ups
- Between-session check-ins
- Psychoeducational companions

---

# Slide 17: Conclusion

**Key Takeaways**

- MentalChat16K: 16K+ QA pairs for mental health AI
- Privacy-preserving pipeline using local LLMs
- 7 therapeutic evaluation metrics
- Significant improvement over base models
- Template for sensitive-domain AI research

**Not a silver bullet, but a meaningful step toward AI that listens better**

---

# Slide 18: Resources

**Links**

- **Paper:** arxiv.org/abs/2503.13509
- **Dataset:** huggingface.co/datasets/ShenLab/MentalChat16K
- **GitHub:** github.com/BalaAnbalagan/MentalChat16K
- **Medium:** medium.com/@balamuralikrishnan.anbalagan

**Thank You!**

Bala Anbalagan | CMPE 255 | Fall 2025
