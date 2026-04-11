# chap01 跨域SAR综述补文献与重写 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 为 `data/chap01.tex` 中“域适应SAR目标识别”和“域泛化SAR目标识别”两节补充具体、可核查的 SAR 文献，新增 BibTeX 到 `ref/refs.bib`，并按技术演进链重写逻辑，使其与后文仿真-实测迁移综述自然衔接。

**Architecture:** 先锁定现有小节的叙述边界与已存在引文，再分别为“域适应”和“域泛化”筛选 3–5 篇新增代表文献，优先利用 IEEE/Elsevier/SPIE 等正式来源核对题名、作者、年份和刊源。随后先补 `ref/refs.bib`，再重写 `data/chap01.tex` 中对应段落，并通过引用检索与 XeLaTeX/BibTeX 构建验证新增引用未破坏论文编译。

**Tech Stack:** LaTeX, BibTeX, `data/chap01.tex`, `ref/refs.bib`, WebSearch/WebFetch, XeLaTeX, BibTeX

---

## File Structure

- Modify: `data/chap01.tex`
  - 责任：重写 `\subsubsection{域适应SAR目标识别}` 与 `\subsubsection{域泛化SAR目标识别}` 的研究现状叙述。
- Modify: `ref/refs.bib`
  - 责任：新增或修正本次补文献所需的 BibTeX 条目，避免与现有 key 冲突。
- Read-only check: `docs/superpowers/specs/2026-04-10-chap01-sar-cross-domain-literature-design.md`
  - 责任：作为结构与约束依据。
- Verification target: `thesis.tex`
  - 责任：论文入口文件，用于最终引用与构建验证。

### Task 1: 锁定现有段落边界与已存在引文

**Files:**
- Read: `docs/superpowers/specs/2026-04-10-chap01-sar-cross-domain-literature-design.md`
- Read: `data/chap01.tex:281-343`
- Read: `ref/refs.bib:869-1038`

- [ ] **Step 1: 读取设计文档并确认不可违背的约束**

必须确认以下约束全部成立后再继续：

```text
1. 两节都按技术演进链重写；
2. 采用“经典文献 + 近5年进展”；
3. 每节新增 3–5 篇代表性文献；
4. 新增引用统一写入 ref/refs.bib；
5. 不虚构论文，不把非 SAR 直接相关工作强行写成代表文献。
```

- [ ] **Step 2: 读取待修改段落，记录当前可保留的引用键**

从 `data/chap01.tex:281-343` 提取当前已使用的 key，并记录为执行清单：

```text
域适应：kang2016sar, malmgren2017improving, girshick2014rich, huang2019and, shi2021unsupervised, chen2022pixel
域泛化：li2023hierarchical, xiong2024lightweight, yuan2024filling, li2025saratr
```

- [ ] **Step 3: 检查这些 key 是否已在参考文献文件中定义**

Run:
```bash
grep -nE "(kang2016sar|malmgren2017improving|girshick2014rich|huang2019and|shi2021unsupervised|chen2022pixel|li2023hierarchical|xiong2024lightweight|yuan2024filling|li2025saratr)" ref/refs.bib
```

Expected:
```text
输出对应 BibTeX 条目行号；不存在“not found”类结果。
```

- [ ] **Step 4: 形成最终待补空位表**

输出一个两列表，供后续执行时严格填充：

```text
域适应新增空位：3–5 篇
- 统计分布对齐 / MK-MMD 或同类方法：至少 1 篇
- 对抗式/多层对齐：至少 1 篇
- 像素级迁移 / 伪标签 / 联合优化：至少 1 篇

域泛化新增空位：3–5 篇
- 数据层扩展 / 域随机化 / 风格扰动：至少 1 篇
- 特征解耦 / 域不变表示：至少 1 篇
- 自监督 / 大规模预训练趋势：可补 1–2 篇（若确有直接相关 SAR 工作）
```

- [ ] **Step 5: 提交一次小提交**

```bash
git add docs/superpowers/plans/2026-04-10-chap01-sar-cross-domain-literature-plan.md
git commit -m "docs: add chap01 cross-domain SAR literature update plan"
```

### Task 2: 筛选域适应小节的新增代表文献

**Files:**
- Read: `ref/refs.bib:897-958`
- Modify later: `ref/refs.bib`
- Modify later: `data/chap01.tex:281-317`

- [ ] **Step 1: 为域适应建立候选文献池**

至少收集 6 篇候选，再从中选 3–5 篇。候选池必须优先覆盖以下方向：

```text
1. SAR 目标识别或检测中的分布对齐（MMD / MK-MMD / CORAL 等）；
2. SAR 任务中的对抗式域适应；
3. SAR 任务中的多层/多粒度对齐；
4. SAR 任务中的像素级风格迁移、伪标签或联合优化。
```

允许保留并强化的现有文献：

```text
huang2019and
shi2021unsupervised
chen2022pixel
zhang2023vsfa
shi2024unsupervised
```

- [ ] **Step 2: 对每篇候选文献做四项核查**

每篇候选都必须记录以下字段，任何一项拿不准都不能进入最终正文：

```text
title:
author:
venue:
year:
problem_fit: 是否直接服务“域适应SAR目标识别”
method_role: 属于“分布对齐 / 对抗适应 / 多粒度对齐 / 像素级迁移 / 伪标签”哪一类
why_keep: 它在技术演进链里承担什么角色
```

- [ ] **Step 3: 删除不适合写入绪论的候选**

剔除以下类型：

```text
- 只讲一般计算机视觉 DA，不是 SAR；
- 与分类/识别关系过远、无法自然服务本节主线；
- 与现有文献高度重复、只换了轻微实现细节；
- 无法核实正式题名、作者或刊源。
```

- [ ] **Step 4: 选出域适应最终新增文献清单**

最终输出应类似：

```text
新增（示例格式，不是固定名单）
- zhang2023vsfa — 用于“视觉特征+散射拓扑特征融合与对齐”
- shi2024unsupervised — 用于“域级/类级双粒度对齐与伪标签过滤”
- [再补 1–3 篇已核实文献]
```

要求：
- 最终 3–5 篇；
- 至少覆盖 3 类不同技术路线；
- 至少 2 篇为 2021–2025 的近年工作。

- [ ] **Step 5: 运行交叉去重检查**

Run:
```bash
grep -nE "@(article|inproceedings)\{(zhang2023vsfa|shi2024unsupervised|NEWKEY1|NEWKEY2|NEWKEY3)" ref/refs.bib
```

Expected:
```text
已存在的 key 只记录一次；若新 key 已存在，必须重命名后再写入计划外执行。
```

- [ ] **Step 6: 提交一次小提交**

```bash
git add docs/superpowers/plans/2026-04-10-chap01-sar-cross-domain-literature-plan.md
git commit -m "docs: refine domain adaptation literature selection plan"
```

### Task 3: 将域适应新增 BibTeX 写入参考文献文件

**Files:**
- Modify: `ref/refs.bib`
- Verification: `ref/refs.bib:897-1038`

- [ ] **Step 1: 在现有跨域 SAR 条目附近插入新条目**

插入位置：紧接 `ref/refs.bib:1038` 后，保持该区域同主题聚集。

新增条目模板必须完整填写，不允许留空：

```bibtex
@article{newkey202Xexample,
  title={Full Paper Title},
  author={Author1 and Author2 and Author3},
  journal={Full Venue Name},
  volume={XX},
  number={Y},
  pages={A--B},
  year={202X},
  doi={10.xxxx/xxxxx},
  publisher={IEEE}
}
```

如果是会议论文，使用：

```bibtex
@inproceedings{newkey202Xexample,
  title={Full Paper Title},
  author={Author1 and Author2},
  booktitle={Conference Name},
  pages={A--B},
  year={202X},
  organization={IEEE}
}
```

- [ ] **Step 2: 为每个新增条目做格式校验**

Run:
```bash
grep -nE "@(article|inproceedings)\{" ref/refs.bib | tail -n 20
```

Expected:
```text
新增条目语法完整，花括号配平，key 唯一，没有 title/author/year 缺失。
```

- [ ] **Step 3: 确认域适应正文会引用到每个新增 key**

先列出计划写入正文的引用键，例如：

```text
\cite{huang2019and,zhang2023vsfa,shi2021unsupervised,shi2024unsupervised,chen2022pixel}
```

要求：
- `ref/refs.bib` 中新增的域适应 key 不能成为死条目；
- 不引入不会在正文出现的新增 key。

- [ ] **Step 4: 提交一次小提交**

```bash
git add ref/refs.bib
git commit -m "bib: add SAR domain adaptation references for chap01"
```

### Task 4: 改写域适应SAR目标识别小节

**Files:**
- Modify: `data/chap01.tex:281-317`
- Verify against: `docs/superpowers/specs/2026-04-10-chap01-sar-cross-domain-literature-design.md`
- Verify refs in: `ref/refs.bib`

- [ ] **Step 1: 先写重写后的段落骨架，再填具体引文**

必须生成 5 段骨架：

```text
段1：预训练—微调起点
段2：负迁移与显式域对齐的必要性
段3：特征分布对齐与对抗适应
段4：像素级迁移、伪标签与联合优化
段5：阶段性总结（依赖目标域样本）
```

- [ ] **Step 2: 把每段压缩成绪论风格的篇幅**

执行时每段遵守如下长度上限：

```text
段1：6–8 行
段2：4–6 行
段3：6–8 行
段4：5–7 行
段5：3–4 行
```

禁止出现：

```text
- 一篇文献讲成一整段；
- 详细实验数值；
- 与后文“仿真-实测迁移”重复展开。
```

- [ ] **Step 3: 用具体句式替换现有泛写法**

执行时使用如下句式模板逐段落地：

```text
针对……问题，A等人\cite{key}通过……实现……，说明……。
进一步地，B等人\cite{key}将……与……结合，在……条件下缓解了……。
然而，这类方法仍……，因此研究进一步转向……。
```

- [ ] **Step 4: 检查过渡句是否把局限引向下一段**

Run:
```bash
grep -n "然而\|但\|因此\|进一步地\|总体来看" data/chap01.tex
```

Expected:
```text
在域适应小节对应段落中可以看到 4–6 个过渡词，且每个过渡词服务于“方法局限→下一类方法”的逻辑推进。
```

- [ ] **Step 5: 提交一次小提交**

```bash
git add data/chap01.tex
git commit -m "docs: rewrite SAR domain adaptation overview in chap01"
```

### Task 5: 筛选域泛化小节的新增代表文献

**Files:**
- Read: `ref/refs.bib:968-1038`
- Modify later: `ref/refs.bib`
- Modify later: `data/chap01.tex:321-343`

- [ ] **Step 1: 为域泛化建立候选文献池**

至少收集 6 篇候选，再从中选 3–5 篇。候选池优先覆盖：

```text
1. 数据层扩展：域随机化、风格扰动、风格混合；
2. 特征层机制：目标/背景解耦、域不变表示；
3. 新趋势：SAR 自监督、大规模联合预训练、基础模型。
```

允许保留并强化的现有文献：

```text
inkawhich2021bridging
kim2024soft
jang2025irasnet
yuan2024filling
li2025saratr
```

- [ ] **Step 2: 对每篇候选文献做与域泛化主线的适配性判定**

每篇都要写出一句判定理由：

```text
这篇文献之所以属于域泛化，而不是一般鲁棒识别/域适应，是因为……
```

若这句话写不出来，该文献不应进入最终正文。

- [ ] **Step 3: 选出域泛化最终新增文献清单**

最终新增清单要求：

```text
- 最终 3–5 篇
- 至少 1 篇落在数据层扩展
- 至少 1 篇落在特征层域不变表示
- 至少 1 篇能支撑“新趋势”段落（若没有直接相关工作，则保留 li2025saratr 并减少该段扩写）
```

- [ ] **Step 4: 标记需避免过度借用检测文献的位置**

如果保留 `yuan2024filling` 这类检测任务文献，必须在执行时注明其角色是“为识别任务提供借鉴”，不能写成“域泛化SAR目标识别的直接主干工作”。

- [ ] **Step 5: 运行交叉去重检查**

Run:
```bash
grep -nE "@(article|inproceedings)\{(inkawhich2021bridging|kim2024soft|jang2025irasnet|yuan2024filling|li2025saratr|NEWKEY4|NEWKEY5)" ref/refs.bib
```

Expected:
```text
已存在 key 可直接复用；新 key 必须唯一且已核实。
```

- [ ] **Step 6: 提交一次小提交**

```bash
git add docs/superpowers/plans/2026-04-10-chap01-sar-cross-domain-literature-plan.md
git commit -m "docs: refine domain generalization literature selection plan"
```

### Task 6: 将域泛化新增 BibTeX 写入参考文献文件

**Files:**
- Modify: `ref/refs.bib`
- Verification: `ref/refs.bib:983-1038`

- [ ] **Step 1: 追加域泛化新增条目，保持字段完整**

新增条目必须至少包含：

```bibtex
title
author
journal 或 booktitle
year
pages
```

若 DOI 可核实，则一并补齐：

```bibtex
doi={10.xxxx/...}
```

- [ ] **Step 2: 统一新条目的 key 命名风格**

执行时遵守：

```text
作者姓氏小写 + 年份 + 主题缩写
```

示例：

```text
zhang2024sarstyle
liu2023dgatr
```

不要使用：

```text
paper1
newref
sar2024
```

- [ ] **Step 3: 检查花括号、逗号和页码格式**

Run:
```bash
python - <<'PY'
from pathlib import Path
text = Path('ref/refs.bib').read_text(encoding='utf-8')
print(text.count('{'), text.count('}'))
PY
```

Expected:
```text
左右花括号计数相同。
```

- [ ] **Step 4: 提交一次小提交**

```bash
git add ref/refs.bib
git commit -m "bib: add SAR domain generalization references for chap01"
```

### Task 7: 改写域泛化SAR目标识别小节

**Files:**
- Modify: `data/chap01.tex:321-343`
- Verify against: `docs/superpowers/specs/2026-04-10-chap01-sar-cross-domain-literature-design.md`
- Verify refs in: `ref/refs.bib`

- [ ] **Step 1: 先写重写后的段落骨架，再填具体引文**

必须生成 5 段骨架：

```text
段1：从复杂条件鲁棒识别过渡到域泛化问题
段2：域随机化、风格扰动与源域分布扩展
段3：特征解耦与域不变表示学习
段4：自监督与基础模型预训练的新趋势
段5：阶段性总结（目标域不可见）
```

- [ ] **Step 2: 控制每篇文献的介绍粒度**

执行时每篇文献只允许 1.5–2 句，统一使用：

```text
针对……问题，A等人\cite{key}提出……；
该工作通过……提升了……，但仍……。
```

- [ ] **Step 3: 强化与后文“仿真-实测迁移”衔接的结尾**

小节最后一段必须显式落到以下语义：

```text
域泛化更符合目标域不可见的实际需求，但当仿真域与实测域存在更强成像机理差异时，现有方法仍有明显不足。
```

- [ ] **Step 4: 检查检测任务借鉴文献是否被谨慎表述**

Run:
```bash
grep -n "yuan2024filling" data/chap01.tex
```

Expected:
```text
若出现该 key，所在句子必须含有“提供借鉴”“也为相关识别任务提供启示”等限定表述。
```

- [ ] **Step 5: 提交一次小提交**

```bash
git add data/chap01.tex
git commit -m "docs: rewrite SAR domain generalization overview in chap01"
```

### Task 8: 做整段一致性检查并验证 LaTeX 引用

**Files:**
- Modify if needed: `data/chap01.tex`
- Modify if needed: `ref/refs.bib`
- Verify: `thesis.tex`

- [ ] **Step 1: 检查新增 key 是否都被正文实际引用**

Run:
```bash
python - <<'PY'
from pathlib import Path
import re
chap = Path('data/chap01.tex').read_text(encoding='utf-8')
refs = Path('ref/refs.bib').read_text(encoding='utf-8')
keys = sorted(set(re.findall(r'@\w+\{([^,]+),', refs)))
used = sorted(set(k for group in re.findall(r'\\cite\{([^}]+)\}', chap) for k in group.split(',')))
new_like = [k for k in used if any(tag in k for tag in ['2021','2022','2023','2024','2025'])]
print('used_recent_keys=', new_like)
print('unused_keys_count=', len([k for k in keys if k not in used]))
PY
```

Expected:
```text
能列出本节使用到的新增/近年 key；若发现本次新增 key 未被引用，返回上一任务修正。
```

- [ ] **Step 2: 检查逻辑过渡与两节结尾是否满足 spec**

人工逐条核对：

```text
- 域适应结尾是否明确“依赖目标域样本”；
- 域泛化结尾是否明确“目标域不可见但跨机理差异仍难处理”；
- 两节是否都避免“文献流水账”；
- 两节是否都服务后文仿真-实测迁移综述。
```

- [ ] **Step 3: 运行 BibTeX 构建验证引用**

Run:
```bash
xelatex -interaction=nonstopmode thesis.tex && bibtex thesis && xelatex -interaction=nonstopmode thesis.tex && xelatex -interaction=nonstopmode thesis.tex
```

Expected:
```text
生成 thesis.pdf；日志中不应出现新增 key 的 undefined citation。
```

- [ ] **Step 4: 若构建失败，先定位是引用问题还是模板问题**

按以下顺序检查：

```text
1. 是否有 BibTeX 条目语法错误；
2. 是否有 cite key 拼写不一致；
3. 是否是历史模板告警而非本次修改引起；
4. 仅修复与本次新增引用有关的问题。
```

- [ ] **Step 5: 提交最终小提交**

```bash
git add data/chap01.tex ref/refs.bib
git commit -m "docs: expand cross-domain SAR literature review in chap01"
```

## Self-Review

- **Spec coverage:**
  - 设计文档要求的三件核心工作——筛选具体 SAR 文献、写入 `ref/refs.bib`、重写 `data/chap01.tex` 两节——分别由 Task 2/5、Task 3/6、Task 4/7 覆盖。
  - 设计文档要求的逻辑衔接与最终验证，由 Task 8 覆盖。
- **Placeholder scan:**
  - 计划中未使用 “TBD/TODO/implement later” 等占位词。
  - `NEWKEY1` 等字样仅用于说明去重命令模板，执行前必须替换成已核实的真实 key，不得保留在实际命令中。
- **Type consistency:**
  - 所有文件路径统一为 `data/chap01.tex`、`ref/refs.bib`、`thesis.tex`。
  - 所有任务均围绕“域适应/域泛化/引用验证”三类动作展开，没有引入未定义的新文件职责。
