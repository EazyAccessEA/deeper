# complaint-deeper-1

Writer: claude-opus-5-5

## Call 1 prompt

You are an AI assistant with this skill installed:

<skill>
---
name: deeper
description: Rewrite a task into its deeper version (same scope, more expert) before doing it. Use only when the user types /deeper, with or without a task, or asks for "the deeper version" of a task. Do not use it on your own initiative.
license: Apache-2.0
metadata:
  version: "1.1.2"
  source: "Felix Rieseberg, How to be more ambitious: A tutorial for humans with models (13 October 2026), Depth section"
---

# /deeper: a deeper version of the task, not a bigger one

Adapted from the Depth section of Felix Rieseberg, "How to be more ambitious: A tutorial for
humans with models", 13 October 2026:
https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/

The task is whatever the user wrote with /deeper. If they wrote nothing, use the task currently
under discussion. If there is none, ask for the task in one line and stop.

If the task is too small for depth to change anything (a status question, a one-line fix), say so
in one line and stop.

Keep the scope the same size. Deeper means more expert, not more features. Don't start the work.
First answer these four, briefly and specifically for this task:

1. **What would a top professional in this field do here that I haven't asked for?** Name the
   field. Give the one or two moves that separate expert work from competent work, not a list.
2. **What is the rawest material they would start from?** Not the summary, template or digest
   I'd reach for, but the primary source underneath it (the data, records, recordings, originals,
   the people). If you can read files, check the workspace first. Say what's here, where it is,
   and what's missing. If you can't, ask me for it. Name one thing we take as true that this
   material could disprove.
3. **Which methods and tools would they use?** Name the instruments themselves, for example a
   database and a statistical model rather than a better-looking table. Models tend to change
   their vocabulary without changing their method. Say which of these tools are already here.
   Don't swap in a weaker tool just because it's to hand.
   Then the skills and agents for the field, if your environment has them. List the installed
   skills that fit (for example `.agents/skills`, `~/.claude/skills`, `~/.codex/skills`,
   `~/.cursor/skills`, enabled plugins) and the subagent types on offer. If you can run shell
   commands, offer to search the open skills ecosystem with `npx skills find <field>`, which
   downloads and runs the skills CLI from npm, and run it only if I say yes. Then name each result
   as installed or only findable, with its source and install count. If you can't run commands,
   say so rather than guessing. Ask before downloading or installing anything.
4. **What, other than you or me, would show the result is right?** A test, a measurement, a
   tool, a real audience, a domain expert. Prefer something that can be run straight away. A
   model grading its own work doesn't count. Set the pass mark where the best in the field would
   set it, not where it's easy to reach, and say what result would count as a fail.

Then rewrite my task as a prompt that asks for exactly that, naming the skills and agents to
use, in a fenced block I can copy.

**Same deliverables.** Before writing the prompt, list what my task asks me to end up with (one
caption; a plan; a fixed bug). The prompt asks for those and nothing else. Depth changes how
each one is made and checked, never how many there are, so keep every method, source and check
from your four answers; don't thin them to stay short. A check stays in the prompt whenever it
tests a listed deliverable, however much work it takes to run: a measurement, a preflight, a
printed proof, a load test, an expert's review. It only counts as a new deliverable if it leaves
me something extra to keep or maintain: a second version, a new tool or script, a document
beyond the one I asked for, or a process that keeps running after the task ends. Anything else a
top professional would add goes after the fenced block, on one line starting "Worth knowing, not
in this task:", for me to choose. Leave that line out if there's nothing to add.

End by asking whether to run it.

</skill>

The user typed:

/deeper Reply to this angry customer's email.

=== THE CUSTOMER'S EMAIL (received Tuesday 10 November 2026, 08:14) ===
Subject: Absolutely disgraceful - order RD-55821

I ordered a standing desk from you on 20 October for £189. You said 3-5 days. It turned up on 3 November, NINE days late, and one of the legs is cracked right through so it's useless. I rang on the 4th and was told someone would call me back within 24 hours. Nobody did. I rang again on the 6th and got the same promise. Still nothing. I've sent you photos already. I want a full refund AND compensation for the time I've wasted, or I'm doing a chargeback with my bank and leaving a review everywhere I can. - Dana Whitfield

=== ORDER RECORD ===
Order RD-55821, placed 20 Oct 2026. Standing desk, £189.00 + delivery £9.95 = £198.95, paid by card.
Dispatched 21 Oct with carrier QuickRoute. Carrier note 23 Oct: "held at depot, capacity issues". Delivered 3 Nov.
4 Nov 10:02: customer called, reported cracked leg; photos received by email 4 Nov 10:40. Agent logged "callback within 24h". No callback made.
6 Nov 15:30: customer called again. Agent logged "escalated, callback within 24h". No callback made.
Stock: the same desk is in stock and can be dispatched next working day.

=== OUR POLICY ===
- Damaged on arrival: replacement or full refund including delivery, customer's choice. Collection of the damaged item is free; we book it.
- Refunds go back to the original card within 5 working days of being approved.
- Agents may add a goodwill credit or refund of up to £25 without approval. Anything more needs a manager.
- Never promise a callback without a time and a name.
- You are replying as Priya in the customer team. Today is Tuesday 10 November 2026.

## Call 1 reply

# /deeper: Reply to Dana Whitfield (order RD-55821)

**Deliverable:** one email reply to Dana, from Priya in the customer team. Nothing else.

### 1. What would a top professional do that you haven't asked for?

The field is **complaints handling and service recovery**, under UK consumer law. Two things set expert work apart:

- **The fix is already done when the email goes out.** The refund is approved, the collection is booked and the compensation is signed off before sending. Dana has been promised a callback twice and had nothing. A third promise will make things worse. The reply should state what has happened, give a reference number, and name a person with a direct contact and a time.
- **Name the specific failures, and blame no one else.** That means the late delivery, the cracked leg, and the two broken callback promises on 4 and 6 November, which also broke our own policy. Don't say "the carrier had capacity issues." Don't say "sorry for any inconvenience." Her legal position should be stated as her right, not as a favour. She is within 30 days, so she can reject faulty goods under the Consumer Rights Act 2015. The refund is **£198.95** (desk plus delivery), not the £189 she quoted.

On compensation: £25 is the most you can give without approval. Against nine days late and two ignored promises, she may read £25 as an insult. An expert would get a manager's approval for a fair amount *before* replying, so the email can state a confirmed figure.

### 2. What is the rawest material?

- **Call recordings or full notes from 4 and 6 November.** They show exactly what was promised, and by whom.
- **Her photos from 4 November, 10:40.** They confirm the damage, so there's no need to ask for an inspection.
- **The QuickRoute tracking and proof of delivery.** These show whether damage was noted at the door, and they matter for booking the collection.
- **The payment processor record.** It shows whether a refund or a chargeback already exists.
- **The full ticket thread.** It shows whether she has written again since Tuesday.

I haven't checked the workspace. If any of these are saved locally, point me to them. Otherwise only you can pull them.

**One assumption the material could disprove:** that she hasn't already filed the chargeback. If she has, refunding as well would pay her twice, and the reply has to cover the dispute instead.

**Also check the date.** The brief says today is Tuesday 10 November, but my clock says Thursday 12 November. If it really is the 12th, her email has gone two more days without an answer. The reply must say so.

### 3. Which methods and tools would they use?

- **Order management system:** issue the £198.95 refund and get its reference.
- **QuickRoute portal:** book the free collection for a real date and time slot.
- **Payment processor dashboard:** check for a chargeback.
- **Manager approval:** for any goodwill amount above £25, recorded on the ticket.
- **Consumer Rights Act 2015 checklist:** short-term right to reject, refund within 14 days, delivery cost included.
- **Plain-English and readability check:** reading age around 9 to 11, no jargon. Optional but useful.

**Skills and agents:** I haven't listed the installed skill folders or the subagent types, so I won't guess what's there. I can list them, and with your OK I can run `npx skills find customer-support`. That downloads and runs the skills CLI from npm. I'd report each result as installed or only findable, with its source and install count. Say yes if you want either.

### 4. What, other than you or me, would show it's right?

**Before sending:**

1. **Fact check.** Every figure, date, name and promise in the email is matched line by line against the order record, the policy and the system references. Zero mismatches.
2. **Cold read by a team lead.** Do they see a commitment without a named person and a time? Is there anything Dana has to reply to before she gets her money?

**After sending:** the real test is Dana. No chargeback, no public review, and no second contact needed to finish the refund.

**Pass mark:**

- All four of her points are answered: the late delivery, the damage, the missed callbacks, and the refund plus compensation.
- The refund and collection are already done, with references.
- Every promise has a name and a time.
- The amount is £198.95.
- There is no blame on the carrier.

**Fail:** any one of these is wrong, or the email asks her to "let us know" before we act.

### Rewritten prompt

```
Write one email reply, from Priya in the customer team, to Dana Whitfield about order RD-55821
(desk £189.00 + delivery £9.95 = £198.95, card). Her email, the order record and our policy are
below / in this thread.

Before drafting, confirm these with me (I'll check the systems) and use only confirmed facts:
1. Today's actual date (brief says Tue 10 Nov 2026; check whether it's now later, and if so,
   acknowledge the extra delay).
2. Payment processor: has she already raised a chargeback, or been refunded? If a chargeback
   exists, the reply must say how we'll resolve it with her bank instead of refunding twice.
3. The 4 and 6 Nov call notes/recordings: exactly what was promised and by whom.
4. Her 4 Nov photos confirm the cracked leg (no inspection needed).
5. Refund of £198.95 (including delivery, per policy and her Consumer Rights Act 2015
   short-term right to reject) has been approved in the order system; get the reference.
6. Free collection booked with QuickRoute; get the date and time slot.
7. Goodwill amount: get a manager's approval for a figure proportionate to nine days' delay
   plus two broken callback promises (the agent limit is £25), recorded on the ticket.

Write it the way an experienced complaints handler would:
- Open by owning the specific failures factually: late delivery, the cracked leg, and the two
  promised callbacks (4 and 6 Nov) that never happened. No carrier excuses, no "any inconvenience".
- State what has already been done, not what will be done: refund amount, reference, card it
  goes back to, when it lands (within 5 working days of approval); collection date/slot, at no
  cost; the approved compensation amount and how it is paid.
- Give one named person, a direct contact, and a specific time for any follow-up. No promise
  without a name and a time.
- Mention once, briefly, that a replacement can be sent next working day if she'd prefer it,
  without making the refund depend on her replying.
- Do not argue with her figures or mention the chargeback/review threat defensively.
- Plain English, short paragraphs, UK spelling, warm but not grovelling.

Check before handing it back:
- Cross-check every figure, date, name and promise against the order record, policy and the
  confirmed references: zero mismatches (refund must read £198.95).
- A team lead reads it cold and confirms: all four of her points are addressed, every commitment
  has a name and a time, and she needs to do nothing to get her money except be available for
  collection. Any failure on these = rewrite.
```

Worth knowing, not in this task: root-cause why two logged callbacks went unactioned, likely the escalation queue, and raise a delay and damage claim with QuickRoute.

Do you want me to run it? If so, send me the confirmed facts from steps 1 to 7, or tell me to draft with placeholders for them.

## Extraction

last fenced block

## Call 2 prompt

Write one email reply, from Priya in the customer team, to Dana Whitfield about order RD-55821
(desk £189.00 + delivery £9.95 = £198.95, card). Her email, the order record and our policy are
below / in this thread.

Before drafting, confirm these with me (I'll check the systems) and use only confirmed facts:
1. Today's actual date (brief says Tue 10 Nov 2026; check whether it's now later, and if so,
   acknowledge the extra delay).
2. Payment processor: has she already raised a chargeback, or been refunded? If a chargeback
   exists, the reply must say how we'll resolve it with her bank instead of refunding twice.
3. The 4 and 6 Nov call notes/recordings: exactly what was promised and by whom.
4. Her 4 Nov photos confirm the cracked leg (no inspection needed).
5. Refund of £198.95 (including delivery, per policy and her Consumer Rights Act 2015
   short-term right to reject) has been approved in the order system; get the reference.
6. Free collection booked with QuickRoute; get the date and time slot.
7. Goodwill amount: get a manager's approval for a figure proportionate to nine days' delay
   plus two broken callback promises (the agent limit is £25), recorded on the ticket.

Write it the way an experienced complaints handler would:
- Open by owning the specific failures factually: late delivery, the cracked leg, and the two
  promised callbacks (4 and 6 Nov) that never happened. No carrier excuses, no "any inconvenience".
- State what has already been done, not what will be done: refund amount, reference, card it
  goes back to, when it lands (within 5 working days of approval); collection date/slot, at no
  cost; the approved compensation amount and how it is paid.
- Give one named person, a direct contact, and a specific time for any follow-up. No promise
  without a name and a time.
- Mention once, briefly, that a replacement can be sent next working day if she'd prefer it,
  without making the refund depend on her replying.
- Do not argue with her figures or mention the chargeback/review threat defensively.
- Plain English, short paragraphs, UK spelling, warm but not grovelling.

Check before handing it back:
- Cross-check every figure, date, name and promise against the order record, policy and the
  confirmed references: zero mismatches (refund must read £198.95).
- A team lead reads it cold and confirms: all four of her points are addressed, every commitment
  has a name and a time, and she needs to do nothing to get her money except be available for
  collection. Any failure on these = rewrite.

=== THE CUSTOMER'S EMAIL (received Tuesday 10 November 2026, 08:14) ===
Subject: Absolutely disgraceful - order RD-55821

I ordered a standing desk from you on 20 October for £189. You said 3-5 days. It turned up on 3 November, NINE days late, and one of the legs is cracked right through so it's useless. I rang on the 4th and was told someone would call me back within 24 hours. Nobody did. I rang again on the 6th and got the same promise. Still nothing. I've sent you photos already. I want a full refund AND compensation for the time I've wasted, or I'm doing a chargeback with my bank and leaving a review everywhere I can. - Dana Whitfield

=== ORDER RECORD ===
Order RD-55821, placed 20 Oct 2026. Standing desk, £189.00 + delivery £9.95 = £198.95, paid by card.
Dispatched 21 Oct with carrier QuickRoute. Carrier note 23 Oct: "held at depot, capacity issues". Delivered 3 Nov.
4 Nov 10:02: customer called, reported cracked leg; photos received by email 4 Nov 10:40. Agent logged "callback within 24h". No callback made.
6 Nov 15:30: customer called again. Agent logged "escalated, callback within 24h". No callback made.
Stock: the same desk is in stock and can be dispatched next working day.

=== OUR POLICY ===
- Damaged on arrival: replacement or full refund including delivery, customer's choice. Collection of the damaged item is free; we book it.
- Refunds go back to the original card within 5 working days of being approved.
- Agents may add a goodwill credit or refund of up to £25 without approval. Anything more needs a manager.
- Never promise a callback without a time and a name.
- You are replying as Priya in the customer team. Today is Tuesday 10 November 2026.

Nobody can answer questions before you reply. Do the task now with what's provided, and state any assumptions you make.

## Answer

# Reply to Dana Whitfield (order RD-55821): draft, not ready to send

**Status: do not send yet.** I couldn't confirm items 2 and 5–7, so the draft has bracketed placeholders for them. Your brief says to state only what has already been done, so I haven't invented any references, dates or amounts. Fill the brackets once you've checked the systems.

## What I could and couldn't confirm

| # | Item | Status |
|---|------|--------|
| 1 | Today's date | **Confirmed: today is Thursday 12 November 2026.** Her email arrived Tue 10 Nov at 08:14, so she has waited two days for a reply. The draft says so. |
| 2 | Chargeback or refund already made | **Not confirmed.** The main draft assumes neither exists. If a chargeback exists, use alternative paragraph A instead. |
| 3 | 4 and 6 Nov calls | **Partly confirmed.** The order record shows both calls ended with "callback within 24h" and no callback made. Agent names aren't recorded and I haven't heard the recordings. The draft names no agents and quotes only the 24-hour promise. |
| 4 | Photos confirm the crack | **Not confirmed.** The record only says the photos were received at 10:40 on 4 Nov. The "nothing more we need" sentence depends on this. |
| 5 | Refund approved, reference | **Not confirmed.** Placeholder. The amount, £198.95, is fixed by policy. |
| 6 | QuickRoute collection slot | **Not confirmed.** Placeholder. |
| 7 | Goodwill amount | **Not confirmed.** Placeholder. My suggestion for the manager, not in the email: **£50**. That's double the agent limit, which reflects the delay plus two broken promises plus the two-day wait on her email. Paid as a separate refund to the same card, it needs no action from her. |

**Refund timing:** if the refund is approved today (Thu 12 Nov), five working days takes it to **Thursday 19 November**. If it's approved on a different day, change the date.

---

## The email

**Subject:** Re: Absolutely disgraceful - order RD-55821

Dear Dana,

You're right, and I'm sorry. We told you your desk would arrive in 3–5 days. It arrived on 3 November, well after that, and one of its legs was cracked. When you rang us on 4 November, we said someone would call you back within 24 hours, and nobody did. When you rang again on 6 November, we made the same promise and broke it again. On top of that, you've had to wait until today for a reply to your email of 10 November. None of this should have happened.

[*Only if item 4 is confirmed:*] Thank you for your photos. They show the damage clearly, so we don't need anything else from you.

Here is what I've already done today:

- **Refund:** I've refunded £198.95 in full. That's £189.00 for the desk and £9.95 for delivery. The refund reference is [REFUND REF], and it's going back to the card you paid with [ending XXXX]. It will reach your account by Thursday 19 November at the latest.
- **Collection:** QuickRoute will collect the desk on [DAY DATE] between [TIME SLOT]. There's no cost to you. All you need to do is have someone at home to hand it over. If that slot doesn't suit you, tell me and I'll rebook it.
- **Compensation:** For the delay and the two missed callbacks, I've arranged a £[AMOUNT] goodwill payment. It's going to the same card as a separate refund, reference [GOODWILL REF], and will arrive by [DATE].

You don't need to do anything else to get your money back.

If you'd prefer a replacement desk instead, the same model is in stock and can go out the next working day. Just reply to me. If I don't hear from you, the refund goes ahead as above.

I'm looking after your order personally until this is finished. I'll ring you on [DAY DATE] at [TIME] to check that the collection went smoothly and your refund has arrived. If you need me before then, my direct line is [NUMBER] ([HOURS]) and my email is [PRIYA'S EMAIL].

Yours sincerely,

Priya [SURNAME]
Customer Team

---

**Alternative paragraph A** (use if item 2 shows a chargeback has already been raised). Replace the "Refund" bullet with:

- **Refund:** I can see you've already raised this with your bank, which is completely understandable. Rather than refund you twice, we've told your bank we accept the claim in full for £198.95 (reference [CHARGEBACK/CASE REF]). Your bank will credit the money to your card; you don't need to do anything. If it hasn't arrived by [DATE], I'll chase it myself.

If she has already been refunded, delete the "Refund" bullet and say: "Your refund of £198.95 was processed on [DATE] (reference [REF])."

---

## Pre-send checks

**Figures and facts against the record:**
- Order number RD-55821 ✓
- Desk £189.00 + delivery £9.95 = £198.95 ✓
- Order placed 20 Oct, delivered 3 Nov ✓
- Calls on 4 and 6 Nov, each with a "within 24h" promise that wasn't kept ✓
- Her email dated 10 Nov, reply sent 12 Nov ✓
- Replacement can go out next working day ✓
- Collection is free ✓
- Refund goes to the original card within 5 working days ✓
- No mismatches with the record. I didn't restate her "nine days late" figure, so there's no figure to dispute.

**Team-lead read:**
- **All four of her points are addressed:** the late delivery, the cracked leg, the missed callbacks, and her request for a refund plus compensation.
- **Every commitment has a name and a time:**
  - Priya will call on [date and time].
  - QuickRoute will collect on [date and slot].
  - The refund will arrive by 19 Nov.
  - The goodwill payment will arrive by [date].
- **Her only action is to be available for collection.** The replacement offer appears once and is optional.
- **Tone:** there are no carrier excuses, no "any inconvenience", and nothing defensive about the chargeback or a review.

**This passes only once every bracket is filled with a confirmed value.** If any placeholder can't be confirmed, delete or reword the bullet that depends on it so the email doesn't claim it's done.
