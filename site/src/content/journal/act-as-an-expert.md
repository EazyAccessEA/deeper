---
title: "Should you tell an AI it's an expert?"
description: "The internet's favourite magic words, a sculptor who didn't want to paint, three studies, and 32 answers. What \"act as an expert\" does, and what to say instead."
date: "2026-11-12"
order: 1
minutes: 8
lead:
  file: "chef-hat.jpg"
  alt: "A white chef's hat on a white background."
  caption: "The hat doesn't know when the oil is hot."
sources:
  - text: "Awesome ChatGPT Prompts (now prompts.chat), first README, 5 December 2022"
    url: "https://github.com/f/awesome-chatgpt-prompts/commit/25b78186b32c514273e5003fcb430c53629d934d"
  - text: "Zheng et al., Is 'A Helpful Assistant' the Best Role for Large Language Models?, Findings of EMNLP 2024"
    url: "https://arxiv.org/abs/2311.10054"
  - text: "Basil, Shapiro, Mollick et al., Prompting Science Report 4, Wharton Generative AI Labs, 2025"
    url: "https://arxiv.org/abs/2512.05858"
  - text: "Hu, Rostami and Thomason, Expert Personas Improve LLM Alignment but Damage Accuracy, preprint, March 2026"
    url: "https://arxiv.org/html/2603.18507"
  - text: "Felix Rieseberg, How to be more ambitious: A tutorial for humans with models, felixrieseberg.com, 13 October 2026"
    url: "https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/"
  - text: "George Dantzig's own account, quoted from Albers and Reid's 1986 interview (Snopes)"
    url: "https://www.snopes.com/fact-check/the-unsolvable-math-problem/"
  - text: "BBC On This Day, 6 May 1954: Bannister breaks four-minute mile"
    url: "http://news.bbc.co.uk/onthisday/hi/dates/stories/may/6/newsid_2511000/2511575.stm"
  - text: "The journal test, in examples/raw/journal-test"
    url: "https://github.com/EazyAccessEA/deeper/tree/main/examples/raw/journal-test"
---

There are some words people say to an AI the way you'd say a spell.

"Act as an expert."

You've seen it. "You are the best financial planner in the country, with thirty years of experience." "You are a senior recruiter at a top firm." "You are the greatest copywriter who ever lived." People type this with total confidence, like the machine was about to give them a rubbish answer and then heard the word "senior" and sat up straight.

I'm not laughing at anyone. I've done it. Everybody's done it. It feels right. If you want the good stuff, you ask for the good guy.

## Where the spell came from

In December 2022, somebody started a list on GitHub called Awesome ChatGPT Prompts. The very first prompt on that list was this: "Act as a Linux Terminal". That one makes the AI pretend to be the text screen programmers type commands into. <!-- O8 -->

That list caught on. As of today it has 176,948 stars, GitHub's version of a like, and a new name, prompts.chat. <!-- O8 --> "Act as" became the way you talk to these things. A whole generation of us learned to open with a costume.

So, does the costume work? Somebody went and checked. A few somebodies.

## What the studies found

A 2024 study tried 162 different roles across four families of AI models, on 2,410 questions. Lawyer, doctor, teacher, you name it. Adding a persona to the instructions a model gets before your question didn't improve accuracy compared with no persona at all. <!-- S1 --> Which role helped on which question looked close to random. Nobody could tell you in advance which costume would help.

A 2025 report from Wharton tried to be smarter about it. Match the expert to the subject. Physics expert for physics questions. On hard science questions, it made no significant difference to accuracy, except on one model. <!-- S2 --> That report isn't peer reviewed, and another paper disputes how it was run, so hold it loosely.

And a 2026 preprint found it could even cost you. On a standard knowledge test, an expert persona scored 68.0% against 71.6% for the same model with no persona. <!-- S3 --> Those were small models, 7 to 8 billion parameters, so don't run with that one too far. And here's the twist. The same paper found personas helped on writing and role-play.

So the fair summary is small and boring, which is how you know it's probably true. On accuracy in test questions, telling a model it's an expert doesn't reliably help. On writing, it might.

Turns out the spell mostly works on things that didn't need a spell.

## A sculptor, not a painter

Felix Rieseberg, who works on Claude at Anthropic, wrote a long tutorial about asking AI for more. Near the end he has a line I can't stop thinking about.

<figure class="pull">
<p>"Michelangelo famously didn't want to paint the Sistine Chapel - you see, he was a sculptor, not a painter."</p>
<cite>Felix Rieseberg, How to be more ambitious, 13 October 2026</cite>
</figure>

<!-- F7 --> Think about that. Michelangelo. The ceiling. And the man's first instinct was, that's not my job title. Then he painted the most famous ceiling on earth anyway.

Job titles are a box. They tell you what you're allowed to be good at. And when you put a job title on an AI, you're handing it a box too. "You are a financial planner." Fine. But a good answer to "should I rent or buy?" might need a bit of a planner, a bit of a surveyor, and a bit of somebody who's been burned by a leasehold. The title picks one room in a house and tells it to stay there.

## Do the job, don't wear the uniform

Felix makes a point about this, and it's the sharpest thing in the whole tutorial. When you ask a model to act like a professional, he says, it often changes its words without changing its methods. <!-- F2 --> You get the vocabulary. You don't get the work.

His fix is good. Use the job titles to find which kinds of expert matter. Then ask the model to do what those people actually do. He uses a short seller as the example. Writing like a short seller is one thing. Researching like one is another. <!-- F6 -->

It's the difference between a man who bought a chef's hat and a chef. The hat is easy. You can get the hat today. The hat doesn't know when the oil is hot.

Here's a real one. We ran a CV through deeper, which is our tool, built on Felix's questions. Instead of announcing that it was a senior recruiter, it went and did a recruiter's homework. The CV bragged about an email open rate going from 31% to 44%. And the answer said this:

<figure class="run">
<figcaption>examples/raw/journal-test/runs/cv-deeper-2.md</figcaption>
<blockquote><p>"Apple Mail Privacy Protection has inflated open rates since late 2021. A Hartwell interviewer may know this."</p></blockquote>
</figure>

Hartwell is the made-up company in the job advert. <!-- R5 --> Now that's an expert move. That's the kind of thing a real recruiter says to you over coffee, quietly, so you don't embarrass yourself in the interview. No costume. Just the knowledge. (That line is the model's claim, by the way, and not a fact we checked. But it's the right kind of question to ask.)

## So we tested the spell

We tried it ourselves. Four everyday tasks: feedback on a CV, rent or buy a flat, a reply to a furious customer, and tidying a Downloads folder. Each one came with the stuff a real person would have to hand. We asked each one four ways, and one of them was "act as an expert" plus a job title. Every answer was run all the way to the end and scored blind by two judges, one Claude model and one GPT model.

And the spell? Did fine. It scored 6.00 actions out of 6. The plain request got 5.81. Our own tool got 5.56. None of those gaps was big enough to count. <!-- J1 --> All four came out level. The persona just happened to land on top. On these tasks, "act as an expert" didn't hurt one bit.

I want to be honest about that, because it's not the story I expected to tell. I built a tool on the idea that the job title is the weak way to ask. And on our four tasks, the job title landed on top, by a margin too small to count.

Here's how one of those persona answers opened, replying to Dana, our made-up customer whose desk came late and broken:

<figure class="run">
<figcaption>examples/raw/journal-test/runs/complaint-persona-1.md</figcaption>
<blockquote><p>"I'm Priya from the customer team. I'm sorry."</p></blockquote>
</figure>

<!-- R3 --> Lovely. That's a person.

## What the spell was really doing

But look at what every answer had. Every single way of asking came with the full material. The CV and the job advert. The mortgage offer and the rent. The order record and the refund policy.

And every answer did nearly everything on the list. 20 of the 24 actions were done by every answer, whoever was asking and however. <!-- J4 --> Every one of them worked out the monthly mortgage payment, whatever the wording. <!-- J7 -->

So here's what I think was going on. The spell didn't do the work. The groceries did the work. Hand a good cook the groceries and they'll make dinner, whether you call them "chef" or "mate". We never tested what happens when you call them chef and hand them an empty bag. We should. We haven't.

<aside class="limits" aria-label="What this doesn't show">
<p class="label">What this doesn't show</p>
<p>Four tasks, two runs each, one writer model, and checklists we wrote ourselves. The studies above measured accuracy on test questions, mostly not everyday tasks like ours.</p>
</aside>

## Believing it's possible

Felix's tutorial ends somewhere you wouldn't expect from an engineer. It ends on belief. People do hard things, he says, when they believe they're possible, and when they've watched somebody else do them.

He tells the story of George Dantzig, a student who arrived late to a statistics class at Berkeley. In Dantzig's own words: "On the blackboard there were two problems that I assumed had been assigned for homework." <!-- O7 --> He solved them. They weren't homework. In Felix's telling: "They were two unsolved problems in statistics." <!-- F8 -->

And he tells the one about the mile. For years, four minutes was the wall. Then on 6 May 1954, Roger Bannister ran it in 3 minutes 59.4 seconds. <!-- O6 --> Forty-six days later, somebody else beat his time. <!-- O6 --> The wall was never in the legs. It was in the head.

I think that's the real reason "act as an expert" feels like it should work. It's a way of telling the machine it's allowed to be good. Like whispering "you've got this" before an exam. And maybe the person who needs to hear it isn't the machine.

Because here's the serious part. My guess is that what made every answer good in our test wasn't a magic word. It was somebody bothering to hand over the real stuff. The actual CV. The actual numbers. The actual angry email. Most of us skip that part. We describe the problem instead of showing it, then dress the AI up in a costume and hope.

## What to say instead

Use a job title if you like. It didn't hurt here. It may help with tone.

But spend your effort on two other things. First, hand over the material: the document, the numbers, the email you're answering. Then ask for the action you want, in plain words, the way you'd ask a colleague who's good at their job. "Work out the monthly payment and the break-even year." "Check my CV against each line of this job advert."

One of the prompts in our test, written by Felix's method for the flat in Leeds, put it better than I can:

<figure class="run">
<figcaption>examples/raw/journal-test/runs/rent-felix-1.md</figcaption>
<blockquote><p>"Build a transparent model, find what the answer depends on, and tell me what to check before I commit."</p></blockquote>
</figure>

<!-- R4 --> No costume in that. Just the job.

If you're not sure what a professional would start from or do, that's what the four questions are for. What would a top professional do here that I haven't asked for? What raw material would they start from? Which methods and tools would they use? And what, other than you or the AI, would show the answer is right? They work in any chat app, no install needed. There's a copy on the [Get started](/start/#chat) page. Take the hat off. Hand over the groceries. Ask for dinner.
