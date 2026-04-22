# Anon Acknowledgement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `anon` mode keep the acknowledgement heading while suppressing acknowledgement body content completely.

**Architecture:** Update the class-level `ack` environment so anonymous-mode behavior stays centralized in the template. Mirror the same logic in `nudtpaper.dtx`, then verify with a full thesis build and PDF text extraction.

**Tech Stack:** XeLaTeX, biber, PowerShell, `pdftotext`

---

### Task 1: Capture the current failing behavior

**Files:**
- Test: `thesis.tex`
- Read: `data/ack.tex`

- [ ] **Step 1: Extract PDF text from the current anonymous build**

Run: `pdftotext thesis.pdf -`

Expected: the extracted text still contains acknowledgement body phrases from `data/ack.tex`, proving the current anonymous-mode output is not truly empty.

- [ ] **Step 2: Search for a stable acknowledgement phrase**

Run: `pdftotext thesis.pdf - | Select-String -Pattern "感谢我的家人"`

Expected: a match is returned before the code change.

### Task 2: Change the template behavior

**Files:**
- Modify: `nudtpaper.cls`
- Modify: `nudtpaper.dtx`

- [ ] **Step 1: Replace white-text masking with body suppression in `nudtpaper.cls`**

Update the `ack` environment so it still emits the heading and TOC entry, but in `anon` mode discards the environment body before typesetting.

- [ ] **Step 2: Mirror the same implementation in `nudtpaper.dtx`**

Keep the documented source aligned with the generated class file so future regeneration preserves the behavior.

### Task 3: Verify the fix

**Files:**
- Test: `thesis.tex`

- [ ] **Step 1: Rebuild the thesis**

Run: `xelatex thesis && biber thesis && xelatex thesis && xelatex thesis`

Expected: all commands succeed.

- [ ] **Step 2: Re-extract PDF text and confirm the body is gone**

Run: `pdftotext thesis.pdf - | Select-String -Pattern "感谢我的家人|致谢"`

Expected: `致谢` still appears, while acknowledgement body phrases no longer appear.
