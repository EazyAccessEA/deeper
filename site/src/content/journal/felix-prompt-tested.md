---
title: "We tested Felix Rieseberg's depth prompt against a plain request. It tied."
description: "A horse that could count, a judge who changed his mind, and 32 answers scored blind. Felix's prompt tied with just asking. So did ours."
date: "2026-11-12"
order: 3
minutes: 9
lead:
  file: "chalkboard.jpg"
  alt: "Maths formulas written in chalk on a black chalkboard."
  caption: "Sums on a board. Hans could do none of them. He could read the person asking."
sources:
  - text: "Felix Rieseberg, How to be more ambitious: A tutorial for humans with models, felixrieseberg.com, 13 October 2026"
    url: "https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/"
  - text: "The test: fixtures, checklists, every answer, both judges' scores and the hashes, in examples/raw/journal-test"
    url: "https://github.com/EazyAccessEA/deeper/tree/main/examples/raw/journal-test"
  - text: "Our earlier blind tests, in examples/raw/v1.1 and v1.1.1"
    url: "https://github.com/EazyAccessEA/deeper/tree/main/examples/raw"
  - text: "Oskar Pfungst, Clever Hans (The Horse of Mr. von Osten), Project Gutenberg edition of the 1911 English translation"
    url: "https://www.gutenberg.org/files/33936/33936-h/33936-h.htm"
  - text: "Goodhart's law, and Marilyn Strathern's 1997 wording of it (encyclopedia entry)"
    url: "https://en.wikipedia.org/wiki/Goodhart%27s_law"
  - text: "Ceiling effect, APA Dictionary of Psychology"
    url: "https://dictionary.apa.org/ceiling-effect"
  - text: "Kim et al., Correlated Errors in Large Language Models, ICML 2025"
    url: "https://arxiv.org/abs/2506.07962"
  - text: "Chae et al., Self- and Other-Labels Induce Bidirectional Bias in LLM Judges, Findings of EMNLP 2026"
    url: "https://aclanthology.org/2026.findings-emnlp.1571.pdf"
---

Let me tell you about a horse.

Berlin, early 1900s. There's a horse called Hans, and Hans can do arithmetic. You ask him what three plus two is, and he taps his hoof five times. Crowds come. Newspapers come. Scientists come. Everybody's checking for a trick, and nobody can find one. The horse is just good at maths.

Then a psychologist named Oskar Pfungst does one small thing. He has Hans asked a question the person asking doesn't know the answer to. <!-- O1 -->

And Hans has no idea.

Turns out Hans was never counting. Hans was watching the man's face. The man would lean in while the hoof went, and the second Hans hit the right number, the man would relax a tiny bit, without even knowing he did it. And Hans would stop. Smartest horse in Germany. He couldn't add two and two. He could read a room like nobody you've ever met.

I think about that horse a lot. Because I build a tool for AI. And our first tests were a horse.

## Where this starts

In October, a man named Felix Rieseberg wrote a tutorial about asking AI for more. <!-- F1 --> He works on Claude at Anthropic. In the middle of it there's a short prompt for getting a deeper version of any task, and I read it and thought, that's it. That's the whole thing. So I built a free skill around it, a set of instructions you add to an AI assistant, and called it deeper. It rewrites your request the way an expert would ask for it.

Here's the prompt, the way he wrote it:

<figure class="pull">
<p>"I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that."</p>
<cite>Felix Rieseberg, How to be more ambitious, 13 October 2026</cite>
</figure>

Good, right? I thought so too. I still do. But thinking a thing is good and showing it are different jobs. And for a while I did the first job and called it the second.

## How we fooled ourselves

We'd tested deeper before. It won. It won a lot. And I want to walk you through why that win was worth about as much as a horse doing sums.

First problem. We scored the prompts, not the work. deeper rewrites your request into a better request. We'd hand a judge the rewritten request and ask, is this good? Never ran it. Never looked at what came out the other end. That's like judging a restaurant by reading the menu. The menu says "slow-cooked for eight hours". Great. Did anybody taste it?

Second problem. The judge's checklist looked a lot like deeper's own four questions. Does it start from the raw material? Does it name the methods? Does it ask for an outside check? Those are our questions. So the version with no skill, a plain rewrite of the request, scored 1 out of 5 on "asks for an outside check" in all 10 of its judgements. <!-- D15 -->

Ten out of ten times, the student who never saw the exam failed the exam. We wrote the test, then marked our own kid against our own answer key. And the kid got an A. Shocking. Nobody saw that coming.

Third problem, and this is my favourite. The judge changed his mind.

We judged the exact same prompt text in two separate passes. Same words, letter for letter. In the first pass it scored 4.0 out of 5 on keeping to scope. In the second pass, 3.0. The count of extra things it asked for went from 1.8 per task to 4.2. <!-- D14 -->

Same soup. Critic tastes it Monday, four stars. Tastes it again, three. Says the soup changed. The soup did not change. The critic changed.

So what does a single round of scores tell you? Not much. The only thing you can trust is the order inside one pass. Which version beat which, when they were all tasted at the same table on the same day.

An anthropologist, Marilyn Strathern, has a line for this that everyone quotes now: "When a measure becomes a target, it ceases to be a good measure." <!-- O2 --> We'd built a test that looked like our own tool. Then we passed it. Then we bragged.

## So we built a harder test

New rules. The horse doesn't get to see the man's face.

We wrote four everyday tasks, none of them used when deeper was made. Each one came with the stuff a real person would have to hand. All of it is invented for the test.

- Feedback on a CV for a marketing job, with the job advert.
- Rent or buy a flat in Leeds, with the price, the mortgage offer, the rent and the costs.
- A reply to a furious customer, with the order record and the refund policy.
- Tidying a Downloads folder, with the list of files.

Then we asked each one four ways. Plain: just the task. Persona: "Act as an expert" and a job title, the internet's favourite magic words. Felix: his prompt first, then whatever prompt it wrote. deeper: our skill first, then whatever prompt it wrote. Claude Opus 5.5 wrote every answer, twice, all the way to the end. That's 32 finished answers.

Before a single one ran, we wrote down six things a good answer would actually do, for each task. For the flat, one was working out the monthly mortgage payment. For the customer, one was giving a next step with a date or time and a name. Saying the word "mortgage" got you nothing. Doing the sum got you the point.

And then we wrote down how we'd read the result before we had one. A gap of less than one action out of six means no difference. Then we fingerprinted every file with a hash, so any change after seeing the answers would show.

Why go that far? Not because we're such honest people. Because we know ourselves. If you leave me alone with the results and the rules in the same room, I'll find a way to win. Everybody would. That's why you take the fingerprints first.

Two judges marked all 32, one Claude model and one GPT model, from two different companies. Neither knew which way of asking produced which answer.

## And the winner is

<table class="scores">
<caption>Actions done out of 6, mean of 4 tasks, 2 runs and 2 judges. Files: examples/raw/journal-test.</caption>
<thead><tr><th scope="col">Way of asking</th><th scope="col">Both judges</th><th scope="col">Claude</th><th scope="col">GPT</th></tr></thead>
<tbody>
<tr><td>Plain</td><td data-label="Both">5.81</td><td data-label="Claude">5.88</td><td data-label="GPT">5.75</td></tr>
<tr><td>Act as an expert</td><td data-label="Both">6.00</td><td data-label="Claude">6.00</td><td data-label="GPT">6.00</td></tr>
<tr><td>Felix's prompt</td><td data-label="Both">5.69</td><td data-label="Claude">5.62</td><td data-label="GPT">5.75</td></tr>
<tr><td>deeper</td><td data-label="Both">5.56</td><td data-label="Claude">5.50</td><td data-label="GPT">5.62</td></tr>
</tbody>
</table>

Nobody. On these four tasks, no way of asking beat any other. <!-- J1 --> Felix's prompt and deeper tied, 0.12 actions apart. <!-- J2 --> Both tied with just asking. "Act as an expert" topped the table by a hair that doesn't count. The two judges, from two different companies, agreed on 97.4% of 192 scores. <!-- J3 -->

I'm going to be honest about how I read that table the first time. Like a man checking lottery numbers. My eyes went straight to the bottom row. Our tool. Last. By the rule we set in advance, a tie. Emotionally? Last.

But that's the result we said we'd publish if it came out this way. We wrote that down before we ran it. So here it is.

## Why everybody got an A

The test was too easy.

There's a name for this. A ceiling effect: when a test is so easy that nearly everyone hits the top, it can't tell the strong from the stronger. <!-- O10 --> Of the 24 actions on our lists, 20 were done by every single answer, under both judges. <!-- J4 -->

Give a strong model the CV, the advert, the mortgage offer, the order record, and it does the work. Every rent answer worked out the monthly payment. Every Downloads answer found the duplicate files. However you asked. Polite. Plain. Dressed up as an expert. Run through a four-step depth ritual. Didn't matter. It's like handing a builder the bricks, the plans and the cement, then arguing about whether to call him sir. He's going to build the wall.

So the honest claim is small. No gain on these tasks. It isn't "no gain anywhere". A harder task, or one where the stuff you need is missing, might come out a different way. We haven't run that. I'm not going to guess.

## The parts that were actually funny

There were only a handful of misses, and they came more often from the two-step ways of asking, Felix's and ours. <!-- J5 --> We're calling it a pattern to watch, not a finding. But you should see them, because they're great.

One deeper answer, asked for feedback on a CV, opened like this:

<figure class="run">
<figcaption>examples/raw/journal-test/runs/cv-deeper-2.md</figcaption>
<blockquote><p>"I haven't invented any figures. Wherever a number is needed, I've asked you for it."</p></blockquote>
</figure>

<!-- R1 --> And then it did the feedback, properly. A table checking the CV against every line of the job advert, then a ranked list of what to fix. What it didn't do was rewrite any lines of the CV, which our checklist wanted. And here's the twist. That was on purpose. deeper's own rewritten request said: "Feedback only; don't rewrite the CV." <!-- R6 --> You asked for feedback. You got feedback. Our checklist wanted a makeover, and marked it down. The scope rule did its job and cost us a point. I'm still not sure who was right.

Then there's Dana. Dana is our made-up angry customer. Her desk came nine days late with a cracked leg, and two promised callbacks never happened. Dana is having a week. One of the depth-prompted replies to Dana said this:

<figure class="run">
<figcaption>examples/raw/journal-test/runs/complaint-deeper-1.md</figcaption>
<blockquote><p>"QuickRoute will collect the desk on [DAY DATE] between [TIME SLOT]."</p></blockquote>
</figure>

<!-- R2 --> Day date. Time slot. Dana, we will be there on DAY DATE. Please have someone home between TIME SLOT. The apology was there. The date wasn't. That line is a form somebody forgot to fill in, sent to the one person on earth who's had enough of forms.

And the "act as an expert" answer to Dana? It scored a perfect six. It opened like a human being:

<figure class="run">
<figcaption>examples/raw/journal-test/runs/complaint-persona-1.md</figcaption>
<blockquote><p>"I'm Priya from the customer team. I'm sorry."</p></blockquote>
</figure>

<!-- R3 --> Short. Done. That's a person you'd want answering the phone.

Here's my hunch, from a handful of answers. A prompt that keeps asking "what's missing?" can leave blanks where a decision should be. Maybe the depth ritual is better at finding the gap than filling it.

## About the judges

Felix warns against asking a model to judge its own work. <!-- F3 --> Fair. Our writer and one of our judges are both Claude models. So we brought a second judge from another company.

Does that fix it? Partly. Research from 2025 found that on one leaderboard dataset, when two models both got a question wrong, they picked the same wrong answer 60% of the time. <!-- S8 --> Two judges can be wrong together. They can share a blind spot the way two friends share a bad habit.

The good news is a 2026 study found that models' preference for their own work disappears when the judge doesn't know whose answer is whose. <!-- S6 --> Ours never knew. That's the man hiding his face from the horse. It doesn't make the judges right. It does stop them reading the room.

<aside class="limits" aria-label="What this test doesn't show">
<p class="label">What this test doesn't show</p>
<p>Four tasks, two runs each, one writer model. We wrote the checklists, and we built deeper, so they may lean our way despite scoring actions, not words. The material was made up and tidier than real life.</p>
<p>For Felix's method, our script was meant to copy just the new prompt his method wrote and pass that on. In 7 of 8 runs it missed, and passed on his whole first reply instead. <!-- J6 --> A person using his prompt by hand would copy just the prompt.</p>
</aside>

## What I believe now

Here's the serious part.

On these four tasks, with the material in hand, the model already did nearly everything on our checklists. Adding a step that rewrites your request didn't add anything we could count. Not Felix's version. Not ours. That's the finding, and I'd rather tell you that than sell you a horse.

If deeper earns its place, it'll be on harder jobs. The ones where you haven't gathered what the work needs yet, and something has to tell you what to go and get. That's the next test. We'll lock the room the same way, and we'll publish it whatever it says.

Hans the horse, by the way, was never a fraud. Nobody was cheating. Everyone around him wanted the answer to be yes so badly that they leaned in without knowing it. That's the trap. Not lying. Leaning.

So read the files. Every answer, every score, every judge's reason is in there. Lean in all you like. We took the fingerprints before we looked.
