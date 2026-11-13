---
title: "Ask for depth, get size"
description: "I asked for one caption for a jar of honey and got a testing programme. On gold plating, a famous hobby, the fix that failed, and the judge who couldn't make up his mind."
date: "2026-11-12"
order: 2
minutes: 8
lead:
  file: "honey-jars.jpg"
  alt: "Jars of honey on a white background."
  caption: "The job: one caption for one jar."
figures:
  door:
    file: "forged-door.jpg"
    alt: "Close-up of an old, heavy forged door."
    caption: "You agreed to a door. Gold plating is everything that gets bolted on after."
sources:
  - text: "Felix Rieseberg, How to be more ambitious: A tutorial for humans with models, felixrieseberg.com, 13 October 2026"
    url: "https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/"
  - text: "deeper blind test for 1.1, round 2: every prompt and score, with the answer key, in examples/raw/v1.1"
    url: "https://github.com/EazyAccessEA/deeper/tree/main/examples/raw/v1.1"
  - text: "The second judging pass of the same 1.1 text, in examples/raw/v1.1.1"
    url: "https://github.com/EazyAccessEA/deeper/tree/main/examples/raw/v1.1.1"
  - text: "Parkinson's law, The Economist, 19 November 1955 (encyclopedia entry; the original is paywalled)"
    url: "https://en.wikipedia.org/wiki/Parkinson%27s_law"
  - text: "Gold plating (project management), encyclopedia entry"
    url: "https://en.wikipedia.org/wiki/Gold_plating_(project_management)"
  - text: "Ron Jeffries, You're NOT gonna need it!, 1998; and Martin Fowler, Yagni"
    url: "https://ronjeffries.com/xprog/articles/practices/pracnotneed/"
  - text: "Linus Torvalds, the first Linux announcement, comp.os.minix, 25 August 1991"
    url: "https://www.cs.cmu.edu/~awb/linux.history.html"
  - text: "Preventing overengineering and project bloat in Codex, OpenAI Developer Community, 2 November 2026"
    url: "https://community.openai.com/t/preventing-overengineering-and-project-bloat-in-codex/1411969"
  - text: "anthropics/claude-code issue 5645, GitHub, August 2025"
    url: "https://github.com/anthropics/claude-code/issues/5645"
  - text: "The journal test, in examples/raw/journal-test"
    url: "https://github.com/EazyAccessEA/deeper/tree/main/examples/raw/journal-test"
---

I asked an AI for a caption. One caption. For a jar of honey.

You know what a caption is. It's a sentence. Two, if the honey's having a good day. You post a photo of the jar, you write "Borage honey, pale and light, out now", and you go and make a cup of tea.

That is not what came back.

What came back was a plan. Write the caption. Then write a second version of the caption. Then post both. Then wait a week and see which one did better. <!-- D16 --> I asked for a caption and got a research programme. I asked for a sentence and got a quarterly review. Somewhere in a server farm, a jar of honey is being A/B tested, and I'm the reason.

## The line it was supposed to follow

Here's the funny part. The tool doing this was mine. It's called deeper. It rewrites your request the way an expert would ask for it, and it's built on a prompt by Felix Rieseberg, who works on Claude. His prompt starts with one line, and the line is about exactly this.

<figure class="pull">
<p>"I want a deeper version of this task, not a bigger one."</p>
<cite>Felix Rieseberg, How to be more ambitious, 13 October 2026</cite>
</figure>

<!-- F4 --> Deeper, not bigger. Clean. Wise. Easy to agree with. Like "eat less sugar". Everyone nods. And then there's the biscuit tin.

Because here's what kept happening when we asked a model what an expert would do. It didn't hand us what an expert would do. It handed us everything an expert might ever do, in every possible world, just in case. You ask for directions to the shop, it gives you the shop, the road, the history of the road, and a plan for the road's retirement.

It did the same with a messy Downloads folder. I asked it to tidy the folder. It came back with a retention policy. <!-- D17 --> A retention policy. For my Downloads. My Downloads doesn't have a policy. My Downloads has eleven copies of the same PDF and a file called "final final v2". It doesn't need governance. It needs a bin.

## How bad was it

Bad. I went back through 40 of my own early runs with deeper's first version. In 33 of them, the rewritten request asked for at least one thing the person never asked for. <!-- D6 --> I haven't published those 40 runs, so treat that as my own count. But I was there. It was a lot of honey.

Later we counted it properly, in a blind test where a judge listed every extra thing each version added to the job. In that judging pass, a plain rewrite with no skill at all added 3.2 extra things per task. deeper's first version added 3.6. <!-- D7 -->

So in that pass, deeper's first version added about as many extras as no skill at all, 3.6 against 3.2, a gap inside the noise. <!-- D7 --> The tool built to go deeper stayed no smaller than not using it. That's like hiring a personal trainer and weighing exactly the same. You'd want a word.

## This is an old problem with new clothes

People were overdoing work long before computers.

In 1955 a historian named C. Northcote Parkinson wrote a piece for The Economist with a line that's been quoted ever since: work expands so as to fill the time available for its completion. <!-- O3 --> Give a man a week to post a letter, and he'll spend the week posting it.

Project managers have a name for the version where the extras are shiny. Gold plating. You agreed to build a door, and the builder adds a brass knocker, a doorbell that plays a tune, and a little window with a stained-glass owl. <!-- O9 --> Nobody asked for the owl. Now you're paying for the owl. Now you have to clean the owl.

<!-- figure:door -->

Programmers have their own rule against it, and it's my favourite name for anything. YAGNI. You aren't gonna need it. It came out of Extreme Programming in the 1990s, from Kent Beck, and Ron Jeffries put it plainly: "Always implement things when you actually need them, never when you just foresee that you need them." <!-- O5 --> Somebody wrote that down as a principle, so it must have been a real problem. You don't write "don't put your hand in the fire" on the wall unless people kept putting their hands in the fire.

And it isn't just us. People who use coding assistants report the same thing right now. One Codex user wrote this, earlier this month:

<figure class="run">
<figcaption>OpenAI Developer Community, 2 November 2026</figcaption>
<blockquote><p>"Problems that could be solved with relatively simple implementations are sometimes turned into unnecessarily complicated modules, abstraction layers, or management mechanisms."</p></blockquote>
</figure>

<!-- S11 --> Management mechanisms. For a simple problem. That's my honey.

A Claude Code bug report from 2025 tells the same story the other way round. A one-line bug fix grew into a pile of features nobody requested. <!-- S12 --> One line in. A shopping centre out.

## The fix that failed

So we wrote a rule. Ask for the same things the person asked for. Nothing more.

Did it work? On scope, yes. In the same judging pass, that first rule kept closer to the task than any other version: 4.4 out of 5. <!-- D8 -->

Then we looked at what it threw away.

It threw away the good stuff too. Its method score dropped to 4.2 and its outside-check score to 3.4, against 5.0 and 4.8 for the version that replaced it. <!-- D9 --> It had started treating real checks as extras. Here's the example that got me. Somebody asks for help typesetting a book. A real professional prints a proof and looks at it on paper before the printer runs a thousand copies. That's not an extra. That's the job. The rule cut it anyway.

It's the diet where you cut the sugar, and the vegetables too, because they were both in the kitchen. Technically you're eating less. Technically you're also not well.

## The fix that held, sort of

The second version draws one line, and it's short enough to tattoo. Checks stay. Chores go.

A check that tests the thing you asked for stays in. However much work it takes. The proof of the book stays. Anything new you'd have to keep, look after or maintain goes out. It gets one line at the end, headed "Worth knowing, not in this task". You read it. You choose.

<table class="scores">
<caption>One judging pass, five tasks, scores out of 5. These score rewritten prompts, not finished work. File: examples/raw/v1.1/round2-judge.json.</caption>
<thead><tr><th scope="col">Version</th><th scope="col">Scope</th><th scope="col">Method</th><th scope="col">Check asked</th><th scope="col">Extras / task</th></tr></thead>
<tbody>
<tr><td>No skill</td><td data-label="Scope">2.2</td><td data-label="Method">2.6</td><td data-label="Check">1.0</td><td data-label="Extras">3.2</td></tr>
<tr><td>deeper 1.0</td><td data-label="Scope">2.8</td><td data-label="Method">4.6</td><td data-label="Check">3.8</td><td data-label="Extras">3.6</td></tr>
<tr><td>First 1.1 draft</td><td data-label="Scope">4.4</td><td data-label="Method">4.2</td><td data-label="Check">3.4</td><td data-label="Extras">0.6</td></tr>
<tr class="mark"><td>Final 1.1</td><td data-label="Scope">4.0</td><td data-label="Method">5.0</td><td data-label="Check">4.8</td><td data-label="Extras">1.8</td></tr>
</tbody>
</table>

Within that pass, the final version kept to scope better than no skill and better than our first version, and it kept its method. <!-- D8 --> It still added 1.8 things per task, by the judge's count. <!-- D7 --> Fewer. Not none. The owl got smaller. The owl is still there.

## The judge who couldn't make up his mind

Now here's where I'd love to stop. Fix found, table drawn, everyone go home.

Except we judged that same final text again. Same words, letter for letter, in a new pass with other versions sitting beside it. Scope came back 3.0, not 4.0. Extras came back 4.2 per task, not 1.8. <!-- D14 -->

Same words. Different day. Different number. It's like weighing yourself in the morning and again at night. The scale tells you a different story, and neither one is lying exactly. They just aren't telling you the same thing.

So the honest claim is narrow. Within one pass, the final wording ranked ahead on scope. Across passes, the numbers moved too much to say more than that. Extras and scope moved most between the two passes. Which makes sense if you think about it. Ask ten people whether an extra is an extra, and you'll get ten speeches.

<aside class="limits" aria-label="What this doesn't show">
<p class="label">What this doesn't show</p>
<p>Five tasks, one run each, scored by a model, and the scores are for prompts, not finished work. The 33 of 40 count is mine and unpublished. Nobody has judged these by hand.</p>
</aside>

## And then it held the line

You'd think a tool that grows tasks would only ever grow them. In our newest test, where every answer ran all the way to the end, the opposite showed up.

One deeper answer, asked for feedback on a CV, opened with this: "I haven't invented any figures. Wherever a number is needed, I've asked you for it." <!-- R1 --> Then it gave the feedback, properly. What it didn't do was rewrite any lines of the CV, which our checklist wanted. That was on purpose. Its own rewritten request said: "Feedback only; don't rewrite the CV." <!-- R6 -->

Asked for feedback. Got the feedback. Our checklist wanted a rewrite as well, and marked it down. The scope rule did its job, and we docked it a point for doing it.

That's a handful of answers, not a finding. <!-- J5 --> But it taught me that "deeper, not bigger" is a judgement call, even for the people writing the checklist.

## What small on purpose looks like

Here's the serious part.

Felix's post, in a passage about giving yourself permission to fail, mentions Linus Torvalds. I read the story as the opposite of gold plating. In August 1991, Torvalds, a student in Helsinki, posted about a little operating system he'd been working on. He called it "just a hobby, won't be big and professional". <!-- O4 --> That hobby became Linux.

He didn't plan the empire. He built the thing in front of him, and he built it properly. The bigness came later, from people who chose it, one piece at a time.

That's what "deeper, not bigger" means to me now. Do the job you were asked to do as well as the best person in the field would do it. Check it properly. And when you spot the owl, the brass knocker, the testing programme for the honey, don't build it. Write it down. Hand it over. Let the person decide.

## A habit you can steal

You don't need deeper for this part. Next time you ask any AI for depth, add one sentence:

"Keep to what I asked for, and put anything extra on one line at the end headed Worth knowing."

You'll still see every bright idea it has. You just won't have to live in them. And somewhere, a jar of honey gets its caption, and goes home early.
