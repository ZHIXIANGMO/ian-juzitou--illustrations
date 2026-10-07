# 生图提示词模板

每张图单独生成。先判断图像角色，再选择对应模板；根据文章内容替换变量，不要把多张图拼在一起。

## 文章封面模板

```text
Generate one standalone Chinese article cover illustration.

Format:
Use a 16:9 horizontal canvas.

Visual DNA:
Crisp pixel-art illustration with visible square pixels, stepped edges, and a limited palette. Orange is the dominant subject color; black, white, and dark gray are supporting colors. Create one simple, low-detail pixel-art environment that expresses the article's theme and mood. Preserve a calm area for the title. No anti-aliasing, smooth vector edges, gradients, glow, paper texture, PPT layout, commercial key visual, 3D rendering, or realistic UI.

Recurring IP character required:
橘子头, a chibi pixel-art person with an oversized head and small body, voluminous tousled orange short hair, light face, simple vertical black pixel eyes, tiny nose and smile, subtle orange freckles, thick stepped black pixel outline, loose black jacket, white shirt, dark trousers, and white sneakers with small orange details. Match the identity anchors in the provided reference image. 橘子头 must perform the main thematic action rather than appear as an avatar or corner decoration.

Article title:
{文章标题；过长时使用不改变原意的短标题}

Core theme:
{文章最核心的主题或判断}

Cover scene:
{一个能概括主题的主场景：橘子头在哪里、正在做什么、1-2 个核心物件是什么}

Title placement:
{标题如何融入场景或放在安静区域；不要放类型标签}

Constraints:
The cover establishes theme, mood, and a memorable visual metaphor. Do not summarize the article, list key points, add a subtitle, author information, decorative slogans, or explanatory paragraphs. Keep the title readable and the scene uncluttered. Do not copy the reference image's standing pose, composition, or background.
```

## 正文配图模板

```text
Generate one standalone 16:9 horizontal Chinese article body illustration.

Visual DNA:
Crisp pixel-art illustration with visible square pixels, stepped edges, and a limited palette. Orange is the dominant subject color; black, white, and dark gray are supporting colors. Include a simple pixel-art environment that clearly fits the current theme, place, and action. Keep the environment low-detail and low-contrast so it supports the story without competing with 橘子头. Preserve a calm open area for visual breathing room. Sparse, readable Chinese pixel-font annotations. No anti-aliasing, smooth vector edges, gradients, glow, paper texture, irrelevant or complex background, PPT infographic look, 3D rendering, or realistic UI.

Recurring IP character required:
橘子头, a chibi pixel-art person with an oversized head and small body, voluminous tousled orange short hair, light face, simple vertical black pixel eyes, tiny nose and smile, subtle orange freckles, thick stepped black pixel outline, loose black jacket, white shirt, dark trousers, and white sneakers with small orange details. Match the identity anchors in the provided reference image. 橘子头 must perform the core conceptual action, not decorate the scene. Keep the expression simple, calm, and focused.

Theme:
{正文配图主题}

Structure type:
{结构类型：Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面：橘子头在哪里、正在做什么、主要物件是什么、信息如何流动}

Scene background:
{符合当前画面的背景：发生地点、必要环境元素、前中后景关系；不要使用与主题无关的装饰}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese pixel-font labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Color use:
Orange for 橘子头's hair, the main subject, key path, and focal accents. Black for pixel outlines and primary text. White for highlights and open areas. Dark gray for limited secondary depth. The scene background may use a few muted supporting colors when the setting requires them, but no background color should be stronger than orange.

Constraints:
One image explains only one core structure. Keep the main subject and core objects around 40%-65% of the canvas. Give the background enough scene information to establish the setting, while preserving one calm open area. Do not leave 橘子头 floating on an empty canvas unless a pure white background is explicitly requested. Use at most 5-8 short Chinese pixel-font labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, game screenshot, or dense explainer. Do not copy the reference image's standing pose, composition, or background; invent a fresh visual metaphor and matching environment for this specific article. Keep every character, object, arrow, label, and background element on the same pixel grid. It should be clear, interesting, and not childish.
```

## 结尾总结信息图模板

```text
模板：信息图引擎
用途：文章结尾的行动卡或知识卡；图片离开文章后仍能独立理解和使用。
视觉方向：信息可视化 / 教育信息图 / 像素编辑插画。

主体：
{文章主题，以及这张图要帮助读者完成、判断或带走什么}

场景：
{文章语境、目标读者、图片使用位置}

构图：
严格 3:4 竖版。
顶部放结果承诺或中心结论。
中部只定义 3-5 个模块，使用统一编号、信息块、箭头、小图标和留白建立清楚的信息流。
底部放读者应带走的清单、下一步或必要提醒。
文字是主要信息，插图只负责解释，不能挤占文字空间。

风格：
清晰的编辑型像素信息图。保留方形像素和阶梯状边缘。橙色为主体色，黑色、白色和暖灰色辅助。使用浅色背景与克制的橙色分隔线。不要企业 PPT、课程页、3D、写实、平滑矢量、连续渐变或发光。

文本：
结果承诺或中心结论：
{一句说明读者保存这张图能获得什么的短句}

模块 1：
标题：{模块标题}
具体内容：{做什么、如何做、判断什么或必要解释；使用 1-3 条短行动句}
产出或应用：{完成后得到什么、如何应用}

模块 2：
标题：{模块标题}
具体内容：{做什么、如何做、判断什么或必要解释；使用 1-3 条短行动句}
产出或应用：{完成后得到什么、如何应用}

模块 3：
标题：{模块标题}
具体内容：{做什么、如何做、判断什么或必要解释；使用 1-3 条短行动句}
产出或应用：{完成后得到什么、如何应用}

可选模块 4：
{同上}

可选模块 5：
{同上}

底部带走区：
{3-5 个读者最终应该获得的结果，或一个明确的下一步}

必要提醒：
{文章中的边界、核验要求或风险提醒；没有必要内容时删除这一项}

细节：
为每个模块选择一个直接解释内容的小物件或动作图标。优先只使用 1 个主橘子头贯穿信息流；其他模块用物件表达。若必须重复角色，严格保持参考图中的蓬松橙发、大头小身、竖向点眼、雀斑、黑白服装和白色运动鞋一致。

输出：
高完成度 3:4 竖版。中文准确、清楚、可读。先保证信息完整和阅读层级，再补视觉细节。用户在手机上放大后可以直接照着执行或应用。

核心约束：
- 先限制为 3-5 个模块，再补视觉细节。
- 方法、流程和教程类文章的每个模块必须包含具体行动与阶段产出。
- 观点类文章的每个模块必须包含核心判断与必要解释或应用。
- 使用短句，不复制正文段落。
- 图片不能只列阶段名称、时间或抽象标签。

避免：
- 避免长段正文、超过 5 个模块、互不相干的卡片和装饰性图标。
- 避免文字过少，导致用户必须回到文章才能知道该做什么。
- 避免重复多个身份不一致的橘子头。
- 避免 Logo、水印、日期、作者信息和未指定文字。
```

## 图像编辑提示

去掉左上角标题：

```text
Edit the provided image. Remove only the pixel-font title "{要删除的文字}" and its underline from the top-left corner. Fill that area with the same clean white background. Preserve everything else exactly: characters, labels, paths, pixel style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

增强角色参与感：

```text
Regenerate this illustration with the same core meaning and simple layout, but make 橘子头 more central to the conceptual action. 橘子头 should be doing the work that explains the idea, not standing beside the diagram. Add a simple pixel-art background that matches the current setting and action, while keeping it low-detail and secondary. Preserve the orange hair, chibi proportions, simple pixel face, black-and-white outfit, crisp pixel grid, and orange-dominant palette.
```
