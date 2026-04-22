# Anon Acknowledgement Design

**Context**

The thesis template currently implements anonymous acknowledgement pages by switching the acknowledgement body text to white in `anon` mode. This hides the content visually, but the text still exists in the source and compiled PDF text layer.

**Goal**

Keep the acknowledgement page and its `致谢` heading in anonymous mode, but make the page body genuinely empty instead of rendering the acknowledgement text in white.

**Decision**

Implement the behavior in the template layer by changing the `ack` environment definition in `nudtpaper.cls`. The environment will still:

- create the `致谢` chapter heading
- add the chapter to the table of contents
- keep the existing font sizing and spacing

In `anon` mode, the environment will additionally ignore its body content so no acknowledgement text is typeset at all.

**Why This Approach**

- Centralizes `anon` behavior in the class option implementation instead of scattering conditionals into thesis content files.
- Preserves the existing author workflow: users can keep writing `\begin{ack}...\end{ack}` normally.
- Prevents hidden acknowledgement text from remaining in the output PDF text layer.

**Files Affected**

- `nudtpaper.cls`
- `nudtpaper.dtx`

**Verification**

Build the thesis in the current `anon` configuration and extract text from the resulting PDF. The verification passes when:

- `致谢` still appears in the PDF text
- acknowledgement body phrases from `data/ack.tex` no longer appear in the extracted text
