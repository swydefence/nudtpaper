# 2026-04-09 chap02 introduction alignment design

## Goal
Revise the chapter introduction in `data/chap02.tex` so its logic is consistent with the abstract and `data/chap01.tex`, while also smoothing the transition into the first 1-2 overview paragraphs of the method section.

## Scope
In scope:
- `\section{引言}` in chapter 2
- The first 1-2 transition paragraphs at the start of `\subsection{方法概述}`

Out of scope:
- Technical details of CUT, CC-Loss, formulas, figures, citations, and later method subsections
- Rewriting the whole chapter
- Changing experimental claims or contribution boundaries

## Required alignment
The rewritten opening should match the thesis-wide logic already established in the abstract and chapter 1:
1. The overall goal is to use simulated SAR data to train a target recognition model.
2. There is domain shift between simulated SAR images and measured SAR images.
3. Domain adaptation offers a path for simulated-to-measured transfer.
4. Existing domain adaptation methods usually rely on a relatively large amount of unlabeled measured images during training.
5. Chapter 2 focuses on the scenario of training with simulated data plus a small amount of measured data, and aims to alleviate the dependence on large quantities of measured target-domain data.

## Recommended rewrite structure
### A. Introduction section
Use a four-step progression:
1. **Task scenario**: clearly define that this chapter studies the simulated + small-amount measured training scenario.
2. **Core problem**: explain that simulated and measured SAR images differ in clutter, speckle, texture detail, and statistical distribution, which causes domain shift.
3. **Gap in existing DA methods**: explain that although DA can support simulated-to-measured transfer, most existing methods assume sufficient unlabeled measured samples for stable alignment; this assumption weakens under limited measured data.
4. **Chapter solution**: introduce the chapter method as a way to improve alignment and recognition performance under limited measured samples.

### B. Method-overview transition
The opening of `方法概述` should answer "why this method" before expanding modules:
1. Restate the concrete pain point: under limited measured samples, target-domain information is insufficient and cross-domain alignment is unstable.
2. Then introduce the two-module solution boundary clearly:
   - CUT handles more stable pixel-level style translation under limited measured samples.
   - CC-Loss reduces dependence on large-sample target-domain distribution estimation and directly improves the target-domain decision boundary.

## Writing constraints
- Keep wording academic and consistent with current thesis tone.
- Preserve all citations, labels, formulas, and figure references unless an adjustment is strictly needed for coherence.
- Do not mirror the abstract sentence-by-sentence; chapter 2 should remain an expanded chapter-level introduction.
- Avoid exaggerated evaluation language.
- Avoid unnecessary quotation-mark emphasis.

## Expected outcome
After revision, the reader should be able to understand at the start of chapter 2:
- what scenario chapter 2 addresses,
- why ordinary simulated-to-measured transfer is difficult,
- why existing DA methods are insufficient in this scenario,
- and why the chapter uses the CUT + CC-Loss combination.

## Implementation note
When actual editing begins, concentrate changes in:
- `data/chap02.tex:3-31`
- the first 1-2 opening paragraphs under `data/chap02.tex:35-73`

Do not expand the edit radius unless a local sentence must be adjusted for continuity.
