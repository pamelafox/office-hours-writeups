[00:00] Welcome to our weekly Python plus AI
[00:03] office hours. I had to postpone it to
[00:07] Wednesday this week. Usually we're on
[00:09] Tuesdays.
[00:10] Um
[00:12] but uh that's because yesterday I was at
[00:15] the cursor conference and that was
[00:20] quite quite interesting. Lots of very
[00:22] interesting talks there about how we
[00:24] build software in the age of identic
[00:27] coding and AI. Um, and of course you may
[00:31] have seen that yesterday SpaceX decided
[00:34] to acquire Cursor for 60 billions. So
[00:37] there were some very rich people on
[00:39] stage yesterday.
[00:42] Um, and uh, yeah, and cursor also had
[00:45] some launches there um, which are really
[00:47] like competitive with uh, Git and
[00:50] GitHub.
[00:51] Uh so that was an interesting conference
[00:54] uh and that's why I had to postpone this
[00:56] week's
[00:58] uh now uh today uh we are having a big
[01:03] launch for the GitHub co-pilot app. So
[01:06] this is yeah June 17th that is today. So
[01:09] the GitHub copilot app is now generally
[01:13] available and uh we're pretty excited
[01:16] about it. And the thing the things have
[01:19] been added since the launch is canvases
[01:21] which are like custom UIs that you can
[01:23] build for um you know for your agent
[01:26] like a like a to-do board or a
[01:29] deployment dashboard
[01:31] um you know however you want to you know
[01:35] um interact with the agent because you
[01:36] may not want to use a chat or just a
[01:38] list of issues you might want something
[01:40] more interesting uh so you can basically
[01:42] create a custom canvas uh then we have
[01:44] automations which are like cron jobs uh
[01:46] I've started Ed using those. I have a
[01:48] couple automations. Uh we call they're
[01:51] here. They're called workflows. I don't
[01:53] know if my thing is out of date, but um
[01:55] I have one that runs my I have two of
[01:57] them running. Uh there's one that runs
[01:59] my LinkedIn agent every day. So that um
[02:03] uh goes to LinkedIn and accepts the
[02:06] invites. Uh so that's really handy
[02:07] because then I don't have to um accept
[02:10] LinkedIn invites personally. And then I
[02:12] al have also one that triages issues uh
[02:15] each day for my main repo and um says
[02:19] what you know the highest priority one
[02:21] is. Uh so yeah these workflow
[02:24] automations they're quite they're quite
[02:26] helpful.
[02:28] Uh and then of course you can bring your
[02:30] own model which is important given that
[02:33] as we can see governments can just take
[02:36] away models like the US government took
[02:38] away Fable last week. That was an
[02:40] exciting exciting week and I think we
[02:44] still don't have Fable back. Um,
[02:48] yeah, I think we don't have it back yet.
[02:50] So, it is important to be able to change
[02:53] your models around. Uh, so definitely
[02:55] check out the GitHub Copilot app. Uh, I
[02:57] I use it for lots of like my like chores
[03:00] and little fixes um where I don't need
[03:03] to go deep into the code, like the stuff
[03:05] that I know that an app can do. Um I
[03:08] used it to generate our office hours uh
[03:13] slide here. Uh so it's just it's really
[03:16] helpful. All right. What else is going
[03:18] on? Uh there's this Postgress conference
[03:21] happening this week and I had a talk for
[03:25] that about building an MC for a
[03:27] Postgress database. Uh so if you're
[03:32] interested in MCP and Postgress,
[03:36] check out that talk. Uh there's also
[03:39] lots of other Postgress talks in the
[03:41] conference. So you can check out all of
[03:43] the talks um if you're a Postgress
[03:47] developer.
[03:48] Uh let's see what else. Um for the rag
[03:54] repo, I upgraded the default chat model
[03:57] to GBD 54 mini. Uh, this was actually
[03:59] kind of hard to make this upgrade
[04:01] because I, you know, I like to run
[04:03] evaluations to see, um, you know, to
[04:07] make sure that when we change models
[04:09] that we're not regressing. And as you
[04:11] can see from this table, it was like
[04:13] really hard to find a model that was
[04:17] better across the board on every metric.
[04:20] And also now with the new reasoning
[04:23] models, we can't set the seed anymore.
[04:25] So, the evaluations are actually very
[04:27] very variable. Uh, so I'm working on a
[04:30] follow-up PR right now. Uh, which one?
[04:34] So, I have a lot of stuff here. Yeah.
[04:36] So, I'm working on this follow-up PR
[04:37] that actually where it makes it easy for
[04:39] me to run the evals like three, four,
[04:42] five times and then calculate the
[04:45] average across those runs, the like um
[04:49] statistical deviations, right? So I can
[04:51] get an idea for like you know what's the
[04:53] range that we can expect to see um
[04:56] because that way I can you know evaluate
[04:59] um you know future changes to the prompt
[05:01] or the model and see and try to reason
[05:04] about it. Uh but generally it's like now
[05:06] that the models don't uh obey the seed
[05:09] parameter and the reasoning models
[05:11] they're like just way less deterministic
[05:14] and it does make evaluations a lot
[05:17] harder. So you need to have like a
[05:18] bigger data set uh so that there's less
[05:20] noise. Um this is only on 50 questions
[05:23] which is too low and you basically just
[05:26] have to run your evals multiple times.
[05:27] Um that seems to be the approach. Uh so
[05:33] yeah so evaluation is hard. You still do
[05:35] it because it's very helpful. You'll
[05:36] learn a lot. Um but uh yeah that's
[05:40] that's this release.
[05:43] Um, I've also been working a lot on, you
[05:46] know, once again talking about model
[05:47] choice, like being able to swap between
[05:49] multiple models. So, this one, this
[05:51] model swap workshop repo, this is still
[05:54] a work in progress because this is for
[05:56] an upcoming conference.
[05:59] Um, but um, here I'm swapping between a
[06:02] bunch of different models. Let me open
[06:04] it up. Model swap workshop. Okay. Um, so
[06:07] I'm actually swapping between um, all
[06:10] these models. So, we've got GBD55, Mr.
[06:12] large 3 Kimmy K2.6 six and deepseek v4
[06:16] flash and seeing you know what things I
[06:18] can do across the models right can I do
[06:20] structured outputs can I do function
[06:21] calling can I do agentic workflows
[06:24] um can I do rag right and uh it's been
[06:28] really really interesting to see so
[06:29] these are all deployed with foundry I
[06:32] also have um like anthropic comparisons
[06:35] here so here once again deployed with
[06:37] foundry I've got uh anthropic models um
[06:41] and uh yes I've been figuring out you
[06:43] know what uh you know what kind of the
[06:46] differences are across models and um
[06:49] doing these evaluations. So uh you can
[06:52] see you know how um you know how the
[06:56] models do with basic requests, how they
[06:58] do with rag requests. So for example
[07:00] like Kimmy K2 generally Kimmy K2.6 looks
[07:03] quite good. Um
[07:05] uh Deepseek kind of varies. Um
[07:12] uh mistral sometimes is good sometimes
[07:14] not. So that has been very interesting.
[07:18] Uh I see the question is any workshop
[07:20] for model evaluation? Um I mean we we
[07:25] talk about we always try to talk about
[07:27] evaluation in our you know in our
[07:32] live streams that we do. So the most
[07:33] recent one was oh why am I I never Okay.
[07:38] Uh let's see. Foundry hosted this one.
[07:44] Ms. Foundry hosted. Here we go. Okay.
[07:48] So, the most recent stream we did was
[07:49] about hosted agents and we talked about
[07:51] evaluations there and there you get to
[07:54] see like how um you can do evaluations
[07:57] with the new foundry portal and that way
[08:00] you can actually see the evaluations
[08:03] in the in the portal. Um for this repo I
[08:07] I'm using the older SDK for doing
[08:10] evaluation. So uh I'm just using my own
[08:14] CLI uh in order to to do them. Um
[08:20] uh but you know general like the general
[08:23] practices are the same. You can even
[08:24] like so you can use our SDKs and
[08:27] especially if you want to integration
[08:28] with Foundry and be able to see the
[08:30] evaluation runs in Foundry. And then
[08:32] there's this new Oh, actually I should I
[08:34] didn't link to that one. There's this
[08:35] new
[08:37] um way of doing evaluations. There we
[08:39] go. Here's the blog post about it. Um so
[08:43] this is based off research
[08:46] called assert.
[08:48] And um they're trying to make it like
[08:51] easier to do evaluations, but this is
[08:53] super new. So in Foundry it's called
[08:56] rubrics. I think that's what it's
[08:58] called. There we go. Rubric evaluators.
[09:00] Let's see.
[09:01] Um, generate a rubrical.
[09:07] Um, I think
[09:10] I think that this is it. The rubric
[09:12] evaluators.
[09:14] Let's see if we can actually get
[09:18] Let me see if I can get it in the
[09:19] Foundry UI. Um
[09:27] cuz I think basically what we're seeing
[09:28] is that people are not doing evaluation
[09:30] and we're trying to make it easier to do
[09:33] evaluation.
[09:36] So let's see.
[09:40] All right. Foundry experiments. That
[09:42] sounds like a good project. Evaluations.
[09:45] Yeah. So new custom rubric evaluators
[09:48] are here. So you can create evaluator
[09:52] um you know custom
[09:55] rubric evaluator.
[09:58] Oh okay.
[10:00] So what you're going to do is like
[10:02] describe your agent be like
[10:05] um you know this agent uh queries data
[10:10] from a company knowledge base and gives
[10:14] back
[10:16] answers. It must always give back
[10:20] citations. Okay.
[10:23] And then um so this works best if you
[10:26] have a target agent here, but let's see
[10:27] what happens if we don't. Autogenerate
[10:29] rubric. Um evaluator
[10:33] should assess that the answers
[10:37] are grounded and that they contain
[10:40] citations in square brackets. All right,
[10:44] let's just try this. grounded
[10:48] relevant
[10:50] also.
[10:52] Okay, let's just try that. Uh context uh
[10:56] adding context.
[10:58] Yeah, so you can actually What's nice
[11:00] about this is you can if you hook this
[11:01] up to an agent, you can point it at your
[11:04] application insights traces. So they're
[11:06] trying to make it easy to use with
[11:08] existing traces. I don't think I don't
[11:11] have an agent in this foundry right
[11:13] here. Um, but then you could also upload
[11:16] context files. So,
[11:18] uh, let me see if I can give it I don't
[11:21] know what it's going to accept for the
[11:22] context files if it's a certain format.
[11:26] Um,
[11:28] but let me try
[11:30] let's see what happens. I gave it this
[11:32] is like a knowledge graph of the of the
[11:35] data. All right. And then it can do
[11:37] multi-turn. It can do conversation.
[11:41] So let's see what it does here. Um so
[11:45] what it should do is come up with like
[11:47] multiple
[11:49] um basically like sub evaluations
[11:53] and give like a weight to each of those.
[11:55] So here you can see you know example
[11:56] rubric all right intent recognition
[11:58] weight tool usage accuracy weight um
[12:02] policy informant right so
[12:05] you know you get you get all these sub
[12:07] evaluators and that they have weights uh
[12:10] so that you can run them all at the same
[12:13] time. Okay. So, it says expected a
[12:16] string got Okay. All right. It didn't
[12:18] like my my context was too long. All
[12:21] right. That's fair. All right. Let's
[12:22] just try generating the rubric without
[12:23] the context.
[12:29] >> Let's see. JSON JSONL CSV or text. Let's
[12:32] see what the format is. Example rubric
[12:36] context. Context.
[12:42] Okay. So, here's for best results, add
[12:46] agent production traces on top.
[12:49] Um, oh, you could, you know, you could
[12:51] attach your agent system prompt
[12:53] reference files. So, you're trying to
[12:56] give it as much information
[13:01] as you can so it can determine
[13:04] cooking up the rubric.
[13:11] Checking for blind spots. Nice little
[13:14] progress thing here.
[13:16] Oh, adding a pinch of quality. Okay.
[13:23] Um, let's see if we can look at fun
[13:25] stuff from this blog post.
[13:28] It's a really good big blog post. Okay.
[13:31] Uh, so they did it on a multi- aent
[13:33] lingraph travel planner, right? And so
[13:35] there, you know, when they came up with
[13:38] the rubric, uh, it had things like, you
[13:41] know, does it, um, over refusal policy
[13:45] violation, right? So it comes up with
[13:47] things that are custom for for that
[13:50] agent.
[13:54] Okay, it's still going. It's still
[13:56] going. Um,
[13:59] what else can we say about this? Uh,
[14:04] there we go. All right. Wow, it came up
[14:06] with a lot. Um, okay. So, let's see what
[14:09] it came up with. So, the most important
[14:11] one was evidential grounding. Um,
[14:15] supported by, entailed by, or reasonably
[14:17] inferable. Wow, this is said in a really
[14:20] fancy way. Okay.
[14:23] I would never have written reasonably
[14:25] inferable
[14:26] myself, but maybe that's what LLMs want
[14:29] to see. Um,
[14:32] task requirement coverage.
[14:35] Um, irrelevance avoidance. That's that's
[14:38] good. Uh, you don't want to go off
[14:40] topic. Citation coverage and placement.
[14:43] Uh, that's nice. Citation traceability.
[14:47] Citation claim support uncertainty and
[14:49] limitations. I like that one. That's
[14:51] basically like when the visible evidence
[14:53] is missing, incomplete. The answer
[14:55] explicitly states relevant limitation.
[14:56] Now the thing is you're only going to
[14:58] see that on some questions where you
[14:59] don't have enough context for it. So I
[15:01] usually do like a separate test for that
[15:03] but uh but that is a good thing to check
[15:05] and then general quality always
[15:07] applicable. Okay. All right. So then you
[15:10] can save the evaluator
[15:13] and then um you know then you can run
[15:16] that um against an agent, a model or a
[15:22] data set. Um,
[15:26] so then you have to set that up. So I
[15:28] usually run, you can also do this
[15:29] programmatically, right? So um, you
[15:31] know, I I typically would do it
[15:33] programmatically from Python. Um, but
[15:35] you can set this all up here.
[15:38] So yeah, so that's worth trying out. um
[15:42] you know when a lot but also like you
[15:44] know you the important thing is to do
[15:46] some form of evaluation like for these
[15:48] ones you know I these are examples where
[15:50] I know exactly the right output because
[15:52] this is like tool calling or structured
[15:54] outputs so it's very easy to do evals
[15:57] for that because it's like well did you
[15:58] get the did you get it right or not
[16:00] right so if you're doing something like
[16:02] that where it's very structured then
[16:04] it's very easy to um you know just uh
[16:08] roll your own emails and just say like
[16:10] well did it you know did get the right
[16:12] answer, yes or no. Uh it's harder for
[16:14] something where it's just question
[16:16] answering where maybe there's not 100%
[16:19] the, you know, one right answer and
[16:21] there's a range of answers and so then
[16:23] you need these LM evaluators.
[16:27] All right, cool. So that's trying out
[16:29] the new rubric evaluation. I would I
[16:30] would have to spend a bit more time to
[16:32] really like hook it up to this um to
[16:34] this app and I'd probably use Python to
[16:36] do it.
[16:39] All right. So, what else is what else is
[16:42] happening? Um,
[16:44] yeah. So, we're trying to generally make
[16:46] it easier to use other models from
[16:48] Foundry so that you're not um you know,
[16:51] you're not dependent entirely on the
[16:52] OpenAI models. Uh, so we're working with
[16:55] Enthropic to try and add better support
[16:57] for the Enthropic messages API because
[16:59] Enthropic has their own API uh for doing
[17:03] things, right? Um, and that's the
[17:05] messages API and it's actually it's a
[17:07] very cool API. So for rag, they actually
[17:10] have a specific um support for citations
[17:13] where you when you send the request, you
[17:16] say, "Hey, here are the the documents
[17:17] you can site." And you give like an ID
[17:19] for each of them. Um, and then the LLM
[17:22] is trained to respond with citations in
[17:25] a structured format. So you actually get
[17:28] back a list of citations and then you
[17:31] can do whatever you want with them. So,
[17:32] this is like really nice because when
[17:34] I'm using the OpenAI models, I have to
[17:36] just tell it like, okay, well, please,
[17:38] please, please put the citations in
[17:40] square brackets, please. Um, you know,
[17:43] and I'm just hoping and praying I can
[17:45] extract it back out in some sort of
[17:47] structured way. But here, the LLM itself
[17:49] is trained to see, oh, okay, here are
[17:51] documents that I can site. Let me site
[17:53] them and then give back um, you know,
[17:56] give back that structured citation list.
[17:59] Uh so uh that's a really nice part of
[18:02] the enthropic messages API. Um but this
[18:04] is only only when you're doing messages.
[18:06] So only with the enthropic ones.
[18:11] Uh and yeah, so basically if you're
[18:13] going to use enthropic models, you do
[18:15] have to, you know, switch for all of
[18:17] them. But it's it's easier if you're
[18:18] doing something like agent framework
[18:20] because then you can just um you know,
[18:22] you can just have a single
[18:25] uh thing that swaps between them. I
[18:27] because I have another repo I did last
[18:29] week which swaps between Enthropic and
[18:34] OpenAI um just with like an if else at
[18:37] the top and this one's using uh keyless
[18:41] credentials. So if you just want to see
[18:43] like if your main two models are
[18:45] nothropic models or
[18:48] um OpenAI models then this repo has all
[18:51] the examples for how you could switch
[18:53] between them with different frameworks
[18:55] here.
[18:57] Uh, so Robbie said you're working with
[18:59] customers on model router. Yeah, I
[19:01] haven't used model router but I was told
[19:03] that now that increasingly you should be
[19:05] able to use
[19:08] um
[19:10] model router when you're setting up the
[19:12] evaluations. Um, let me see where did I
[19:16] see
[19:18] evaluator catalog.
[19:20] Um
[19:23] yeah, I was maybe this isn't available
[19:24] yet, but I was told that for evaluations
[19:27] we would soon be able to use the model
[19:29] router for the judges for the
[19:31] evaluations. Uh but I I have not used
[19:34] model router myself.
[19:36] Uh I think the question is when do you
[19:38] do the routing and I guess model router
[19:41] has a like smart routing in it to try
[19:44] and decide that.
[19:46] Um but if you are doing model routing
[19:48] like you want to make sure everything
[19:49] works across all the models. Um so you
[19:52] know with the with this it's like you
[19:54] know do you need image input? Do you
[19:56] need function calling? Do you need
[19:58] structured outputs? And that's where I
[20:00] see a lot of variability across the
[20:02] models. Um they all you know work fine
[20:06] with just I mean they work fine enough
[20:08] with a single LM call. Like they may not
[20:10] be as as accurate. Um but um but yeah,
[20:15] they there's definitely difference in
[20:17] the models when you start getting into
[20:18] the fancier features.
[20:23] Um let's see
[20:27] what else. Uh
[20:31] so more some more updates on the
[20:34] co-pilot side. Um better support for
[20:36] co-pilot and jet brains if you use jet
[20:38] brains. Um a good reminder that the
[20:41] copot sk and CLI work with any open
[20:43] source model not just openi so you can
[20:45] bring your own models to it. Um you nice
[20:49] blog post about get work trees because
[20:51] these are now that we're doing like a
[20:53] dentic coding uh a lot of the coding
[20:55] agents will use work trees so that you
[20:57] can quickly go between multiple branches
[21:00] and basically it's basically just
[21:02] another folder that it makes. So that's
[21:04] a nice little blog post here.
[21:11] Uh so Robbie says any workshop on LLM as
[21:15] judge for evaluation. Um
[21:19] uh yeah I mean so generally the you know
[21:22] when we talk about evaluation that's
[21:23] that's what we're usually talking about
[21:25] is using the LLM as a judge for
[21:27] evaluation. So that was uh you know the
[21:30] most recent one was from the the live
[21:33] stream series. I think I already linked
[21:34] to it. Yeah I did. Um
[21:39] and uh yeah besides that I think there
[21:42] were there were also some build sessions
[21:44] on evaluations too. So you could check
[21:46] the build catalog. I think we had some
[21:48] labs and some sessions. Uh
[21:52] well yeah let us I mean let us know what
[21:55] additional topics you're looking for
[21:59] and we can
[22:01] cover cover more things. Um I also
[22:04] always recommend just for general
[22:06] guidance on evaluation. I you know I
[22:09] always recommend Hamal Hussein
[22:12] and he's got good insights um just about
[22:16] best practices for using LMS for
[22:20] evaluation. That's his expertise. He's
[22:22] also you know he runs a course on it. it
[22:25] is he's not specific to Microsoft um but
[22:27] just generally
[22:29] good practices for using LMS as a judge
[22:33] and the kind of things you need to
[22:34] avoid.
[22:39] Uh
[22:40] uh let's see there's another good recap
[22:43] of build. So if you missed Microsoft
[22:46] build
[22:48] check out that blog post that was a good
[22:51] one. And then this is a really like
[22:53] nerdy blog post which I love um which is
[22:56] how GitHub Copilot improves token
[23:00] efficiency. So this gets into like the
[23:02] weeds of stuff like prompt caching
[23:05] um because prompt caching ends up being
[23:07] one of the most important things like
[23:08] when you're in GitHub copilot and you
[23:11] know you have all this thing when when
[23:13] you send a new message the majority of
[23:15] that prompt is cached and so it's not as
[23:17] expensive. But if I switch models
[23:19] halfway through, because sometimes I do
[23:21] switch models halfway through,
[23:22] especially if I start with auto. If I
[23:24] switch models halfway through a
[23:26] conversation, then then I lose my prompt
[23:30] cash entirely. Um, and so it's actually
[23:33] going to cost more money. Uh, so,
[23:38] uh, yeah, it's it's interesting. So they
[23:40] do anybody who works on coding agents
[23:42] spends a lot of time on prompt caching
[23:45] because that has basically the biggest
[23:46] effect on you know speed and token usage
[23:49] and cost. Uh so you want to be able to
[23:52] take advantage of the prompt cache. Uh
[23:55] but that also assumes that you're using
[23:57] the same model through a session. Uh, so
[23:59] I think that's something good to keep in
[24:00] mind is if you switch models halfway
[24:03] through the session,
[24:05] then you you're you know, you've lost
[24:07] your um lost your prompt cache.
[24:12] Um, now yeah, Enthropic is interesting
[24:15] because they actually have give you a
[24:16] lot more control over the prompt
[24:20] caching. And this is something also
[24:21] you'll see in their in their API if you
[24:23] use their messages API is that um they
[24:27] give you like you can actually like
[24:28] cache certain blocks and you can have
[24:30] like these cache break points and stuff
[24:32] like that. So they you know co-pilot
[24:35] specifically
[24:38] um sets particular break points like
[24:40] tool definition system prompts because
[24:43] those change the least and then they've
[24:46] got break points in the conversation.
[24:48] Um, so that's that's quite interesting
[24:50] and that's something to think about as
[24:52] well when you're developing your your
[24:53] own agents, especially when you start
[24:56] using other models.
[25:00] So that I thought that was quite
[25:02] interesting. Um,
[25:06] what else? See if we can get some
[25:08] questions in here.
[25:12] What else do I have working on?
[25:18] Oh yeah. Oh, sorry. I wanted to announce
[25:20] this. You can be the first to know we're
[25:22] having another another live stream
[25:25] series coming up uh at end of July. Fix
[25:29] this little cam. I got to duct tape this
[25:32] thing. It's ridiculous. Um
[25:35] lazy senior deb.
[25:43] Come on, stay. Okay. Uh, so let me get
[25:46] an actual link for this series so you
[25:48] can sign up for it. Um,
[25:53] let's see.
[25:55] Uh,
[25:58] we're just we're just working on
[26:02] the stuff for it. So, let me give you a
[26:04] link. I think this one works. Okay,
[26:06] there we go. All right. So,
[26:10] this is going to be the series
[26:14] So this will be on Microsoft IQ. So
[26:16] we'll start with Foundry IQ, then do
[26:18] work IQ and then do Fabric IQ
[26:21] and we'll have, you know, the live
[26:23] streams with the office hours after each
[26:25] session just like we do for every
[26:27] series. U my colleague AA is working on
[26:29] it. She's going to do the work IQ one
[26:31] because she's an expert on that. Uh so
[26:34] yeah, sign up for that series. Um if
[26:36] there's another series you think
[26:39] that we should do, uh let us know. Um,
[26:43] if everything I'm saying is going over
[26:45] your head, uh, you know, um, I'm going
[26:47] to give the link I always give, which
[26:49] is,
[26:52] um, the
[26:55] well, start with the this one,
[27:00] right? Like, if you're new to generative
[27:02] AI, we recommend starting with this
[27:04] series. Um, but you can also read my
[27:07] blog post about other ways that I learn
[27:09] about generative AI. Um, but uh this is
[27:13] a recommendation. We might do this
[27:15] series again too, but we're still
[27:18] deciding if we have the time to do it
[27:20] because it is a nine-part series. It's
[27:22] quite long. Um, so yeah, but we might do
[27:25] another one if there's enough interest
[27:27] for it. Let's see what Sylvester linked
[27:30] to. Makes your AI agent think like the
[27:33] laziest senior dev in the room.
[27:37] Oh my gosh.
[27:40] Um,
[27:48] nice.
[27:50] So, what does the prompt look? Okay, the
[27:52] I the agent stops at the first. Does
[27:54] this need to exist?
[28:00] I assume this is a skill. Yeah, it's
[28:02] like a skill.
[28:04] It's using plugins for everything. Um,
[28:08] let's see what the skills looks like.
[28:10] GitHub
[28:12] plugin
[28:14] marketplace
[28:16] skills. Okay, there we go. This is how
[28:18] we do it. Skills,
[28:22] ponytail audit, ponytail,
[28:25] just ponytail skill.
[28:30] Uh, you are a lazy senior development.
[28:32] Lazy means efficient, not careless. you.
[28:35] Okay. Active every response.
[28:44] All right.
[28:55] When not to be lazy.
[28:59] All right. Yeah, it sounds fun. Uh, you
[29:01] should try it out. Let me know.
[29:05] Um I have I don't know. I mean yeah I
[29:07] sometimes have this issue where it gets
[29:10] overly complex. Um
[29:14] but uh a lot of times it's just kind of
[29:16] code smells that it introduces right. Um
[29:20] so uh yeah let me know if you actually
[29:23] are using ponytail.
[29:28] Uh let's see
[29:30] what else.
[29:35] Um,
[29:38] talk about that one.
[29:42] Oh, I deployed OpenClaw. Remember we
[29:44] were talking about OpenClaw last time.
[29:47] Uh, so I did I did actually deploy it.
[29:50] Let me see if I can log in. I forgot
[29:52] about that. Here we go. Yeah, this is
[29:55] the first time deploying OpenClaw. So I
[29:57] did send some fixes for it. So this is
[29:59] claw
[30:01] dead.
[30:04] Let me see where the the actual repo is.
[30:07] Um,
[30:11] here we go.
[30:15] Um, because we had various questions
[30:17] about this repo last time. So, I was
[30:18] like, all right, I guess I should I
[30:20] should deploy it. So, this is if you
[30:23] want to deploy OpenClaw on Azure
[30:25] container apps. Um, and uh, I've fixed a
[30:30] few issues with doing it on Mac. So, if
[30:32] you do have a Mac, try it out now and
[30:34] see if it works for you. See if we need
[30:36] to make any other
[30:38] um, fixes and yeah, so it'll deploy
[30:42] OpenClaw. So, then I said hi.
[30:46] And OpenClaw has like all this memory
[30:48] and apparently it uses git for the
[30:50] memory, the file system, which I didn't
[30:52] realize. So I had to set up set up get
[30:56] there and then yeah and then I couldn't
[30:58] decide what to do with it.
[31:00] Um in build Microsoft came up with
[31:03] autopilot. Is that the same? Are we
[31:04] talking about scout? Um I think it build
[31:07] we called it scout. Um so scout is like
[31:11] a Microsoft specific version of
[31:15] openclaw.
[31:18] Um
[31:20] uh let me see if I have it. Okay, I have
[31:24] the previous version of it which had a
[31:26] different name, but um I still need to
[31:29] download the latest one. Um but it like
[31:33] looked like this, like a little desktop
[31:36] app with automations and like it had
[31:39] like really good um integrations, right?
[31:42] And that's what's really nice is like
[31:44] integrating with Microsoft 365 really
[31:46] nicely. So I haven't downloaded the the
[31:49] new Scout because I think we have to do
[31:51] it a special way at Microsoft. So I have
[31:53] to follow that steps. Uh but yeah, so
[31:57] Scout is uh basically
[32:00] Open Claw, but it has specific
[32:02] integration to make it work well with
[32:06] Microsoft 365 in particular.
[32:14] Uh but this one is just open claw just
[32:17] the the you know the bare version of
[32:20] openclaw just the you know the node repo
[32:23] deployed on container apps. Uh so it
[32:27] doesn't have access to anything until
[32:29] you'd have to explicitly set up access
[32:31] for it right because by default it's
[32:33] just in an isolated container app. So
[32:36] there'd be different use cases for it.
[32:41] Um,
[32:43] okay. Yeah. So, Pablo says, "Do the
[32:46] three IQs come with attack protection?"
[32:49] Um, so first, let's just recap what we
[32:53] talked about before and see if there's
[32:55] anything more to add to that. What do we
[33:02] Right. So, this is what we were talking
[33:03] about before.
[33:05] Um, so we talked about foundry guard
[33:08] rails. I'm trying to think if okay so if
[33:11] we talk about foundry guard rails
[33:13] we talked about AI red teaming and
[33:16] getting logs of events. Oh, and I did um
[33:19] thanks to this discussion, we did
[33:21] improve the
[33:23] um
[33:25] the docs about about this not on here
[33:28] but on
[33:30] uh opening our responses API this one.
[33:34] Um
[33:36] because after our chat uh where is it?
[33:42] There we go. Okay. So thanks to your
[33:45] question last week, we did at least add
[33:47] this documentation
[33:49] um to show you how to detect the things
[33:54] in responses API.
[33:57] So thanks for that. Um now we have
[34:00] better docs on that.
[34:04] Um but uh yeah. Okay. I'm thinking if we
[34:06] had any other updates to that
[34:08] discussion. Um,
[34:14] so I don't think we but other things I
[34:17] guess we didn't talk about purview
[34:19] because there is also talking about the
[34:20] IQs like Foundry IQ does have the um,
[34:27] let me see their launch blog. I think it
[34:29] was in their
[34:31] Yeah, I think it's in here. Great.
[34:34] Um,
[34:36] so this is in here because we we're been
[34:39] working on integrating more perview into
[34:42] Foundry IQ. Um so purview is like so you
[34:47] can like label your label your data and
[34:50] say hey this label this data is highly
[34:52] confidential this data is public
[34:54] whatever and um there's a repo
[35:00] I think two are there two repos let's
[35:03] see okay so this is this repo is
[35:07] basically our main repo if you know
[35:10] Azure search openi demo matt just added
[35:12] perview onto this one we haven't
[35:14] integrated into the main one yet
[35:17] and I don't remember why. I will ask
[35:19] Matt after um uh because I do think that
[35:24] the need for purview is probably
[35:25] becoming increasingly necessary because
[35:28] if especially if you're doing multi-
[35:29] aent scenarios like it would be good for
[35:32] the agents to know how the data was
[35:33] labeled. Um so let me link to that one.
[35:39] Um so that would be something to think
[35:43] about. There's also just a more basic
[35:44] example for for that.
[35:48] um
[35:50] very very
[35:53] I I don't think I have anything more on
[35:56] that note about the IQ's
[35:59] um
[36:01] because I don't know uh
[36:06] yeah I guess the question is what um
[36:08] what additional things are so you are is
[36:11] it that you don't want to use the
[36:13] foundry guard rails because you want
[36:14] more protection in the IQ's itself. Um,
[36:22] and like if if that's the case, then my
[36:24] question would be what specific kinds of
[36:26] attacks are you looking for in each IQ
[36:30] that you like want that additional
[36:33] protection for, right? So what do you
[36:34] need on top of uh you know the foundry
[36:38] guard rails,
[36:40] the red teaming, the um the purview
[36:46] uh you know what additional sort of
[36:48] protection are you looking for? What
[36:49] attacks are you concerned about? Then I
[36:52] can ask around and see
[36:58] defender. Oh, I mean defenders also
[37:00] defenders is looking for different kind
[37:02] of attacks though cuz purview depends
[37:05] what kind of like purview is about um
[37:09] you know like are people seeing data
[37:11] that they shouldn't be able to see. So
[37:12] that's in purview. Um defender is
[37:14] usually more like stuff like networking
[37:17] issues. I guess defender might also it's
[37:20] a good question. What does defender have
[37:21] in it now? Maybe defender does have
[37:24] more. Let's look at that build recap
[37:27] because I actually haven't really kept
[37:29] up to date
[37:31] defender.
[37:34] I don't see anything in security
[37:38] review. Oh, there's A365,
[37:41] too. I think A365 is supposed to do a
[37:44] lot around Microsoft A635.
[37:47] Um, I haven't dug into this, but I think
[37:50] one of its big things is supposed to be
[37:51] governance.
[37:53] Okay. Bam. Bam. by agent 365
[38:00] the control plane for agents
[38:04] blah blah blah let's get their real docs
[38:07] okay all right so this includes
[38:10] a lot of stuff right you got Entra
[38:12] defender purview in tune and the admin
[38:15] center um
[38:19] security posture
[38:22] so this should wrap up everything into
[38:24] one. But what I want to see is the docs,
[38:28] the actual docs. Sign in to get started.
[38:32] I am Oh, I got to like sign into portal.
[38:35] Okay. Let's try and find the real docs
[38:37] for it. Um
[38:45] okay.
[38:48] Uh, so this is like stuff like managing
[38:50] well a lot of this is managing just
[38:51] which agents are even allowed in the
[38:54] thing. Um,
[39:01] kind of want to see more about seeing
[39:04] the data that they have.
[39:06] A365 why doesn't it govern when
[39:09] established lightweight guard whales
[39:10] blah blah blah. I think a lot of this is
[39:12] about what platforms
[39:15] uh like what like when people are like
[39:17] publishing lots of agents with Microsoft
[39:19] co-pilot to your internal teams like you
[39:22] know being able to govern those. So uh
[39:25] let me ask I'll ask
[39:28] prevent data oversharing and leak secure
[39:30] AI agents at scale. Okay. Oh here we go.
[39:33] Protect AI agents with Microsoft
[39:35] offender. All right. I think this is
[39:37] what we want. Okay. secure AI agents,
[39:40] blah blah blah.
[39:42] Um,
[39:46] threat detection. So, you would need to
[39:47] like basically register these your
[39:49] agents so that it could be watching
[39:54] these things. Uh, so manage.
[39:59] Okay. What what are the threats?
[40:02] Unsafe AI agent actions.
[40:05] Okay. Defender integrates directly with
[40:08] work IQ MCP to evaluated tool
[40:11] invocations. If defender determines an
[40:13] action issue, it blocks the action. So
[40:15] this looks really really interesting. Um
[40:22] so you go to defender, you go to
[40:23] security for agents.
[40:26] Uh you have to connect your 8365
[40:30] and connect to co-pilot studio if you're
[40:33] doing that. Um, and if your agent is
[40:36] just running on like just a custom
[40:38] endpoint, then you need to register that
[40:40] specifically
[40:45] you need to send observability data.
[40:49] That makes sense. So maybe with open
[40:51] telemetry advanced hunting.
[40:55] Wow.
[40:57] Okay. Advanced hunting. Proactively hunt
[41:00] for threats.
[41:04] Um,
[41:06] okay.
[41:09] Well, that looks fun. Um, and then this
[41:12] also has Purview and Entra. So, okay.
[41:14] So, this is this is the this looks like
[41:16] the good docs for this one. Um, because
[41:19] this has the the deep dive
[41:22] into it. Uh, oh, so you're saying yeah,
[41:25] protection should start by detecting the
[41:27] source before they reach any agent. Um
[41:31] yeah there was I mean the question is so
[41:34] there you know you you can do red teams
[41:36] on your local agent before you even
[41:39] deploy it right um but if you're
[41:41] thinking about like analyzing the source
[41:42] code itself
[41:45] um I did just see where was that build
[41:47] recap
[41:49] uh security it said a skill maybe the
[41:52] skill security review skill
[41:58] let me see co-pilot but But I think
[42:00] security review skill would not be
[42:02] specific to
[42:08] um agent stuff
[42:11] because it kind of sounds like you want
[42:13] a you want something to look at look at
[42:18] your code itself and look for like
[42:21] security issues in the way you've set it
[42:23] up, right?
[42:25] Um,
[42:28] oh, or you want you wanted to audit the
[42:30] way that would be interesting is to
[42:32] audit the way you're using the IQ's like
[42:36] look at your code for that and see like
[42:38] are you using
[42:40] um you know are you using secure
[42:42] settings? Uh because a lot of times
[42:45] these these things you know like with
[42:46] work IQ it's got multiple tools. It's
[42:48] got like a read only tool and a write
[42:50] tool
[42:52] and you might be using it in a um
[42:55] you know uh you know the most secure way
[42:59] or not. Um
[43:05] yeah I think uh I'm trying to think what
[43:08] sort of thing be looking for.
[43:11] Yeah I mean so Garvey says you know task
[43:13] adherence guardrails etc. So all of
[43:15] those are like looking at the output. It
[43:18] kind of sounds like so definitely you
[43:20] should do that and that's why we have
[43:21] the guardrails and the red teaming. Um
[43:24] but it also sounds like uh Pablo's
[43:27] asking for more an analysis of the code
[43:30] and getting like recommendations
[43:33] um based on the code, right?
[43:42] so that you could like identify identify
[43:44] issues before
[43:46] before you even have to do red teaming.
[43:53] Um so kind of like I mean this security
[43:55] skill, right? This security skill is
[43:56] something that's looking through code.
[43:58] Um this one's generic. This is not about
[44:00] um you know agent security, IQ security,
[44:02] whatever. This is just a general
[44:05] uh you know a general one. Um, you could
[44:09] imagine something that was more specific
[44:12] to agent security.
[44:16] Let me see.
[44:19] Thinking who to ask. Let's see if
[44:21] there's anything like that.
[44:25] The thing that's tricky is that, you
[44:27] know, we can have all these best
[44:28] practices and the skill can definitely
[44:31] alert you about, you know, hey, you're
[44:34] not following the best practice. Um but
[44:36] ultimately it, you know, depends on the
[44:38] use case. Like for some some use cases
[44:40] you may want to be sacrificing, you
[44:43] know, some aspect of security. Um but
[44:46] that's why it's good to be collaborative
[44:47] with these things, right? It's like,
[44:48] okay, yeah, I'm, you know, I I'm
[44:50] comfortable with that security issue.
[44:52] I'm I'm going to go forward with it,
[44:54] right?
[44:58] M
[45:02] uh so I'll I'll ask around to see um you
[45:06] know see what additional things we might
[45:07] have for that
[45:10] uh so Honor says he's building an agent
[45:14] using agent framework how many tools
[45:16] should be in an agent should you use sub
[45:18] agents if there are too many tool is the
[45:21] limit based on the model um there was a
[45:24] really fun let me find there was a very
[45:26] fun website um about tool calling. Um
[45:31] let's see
[45:33] it was from
[45:35] here.
[45:38] Uh so certainly like every model sees
[45:43] sees tools a different way. So this is
[45:46] um I mean this is really nerdy but this
[45:47] is this is the actual like showing how
[45:51] tools are sent to models and that's this
[45:53] is part of why there's so much
[45:55] difference um you know in in how
[45:58] different models pull tools. Um but
[46:01] anyway, so uh you know uh I don't I
[46:05] don't think I can answer that um
[46:08] generically like this is something where
[46:10] I would be
[46:13] running evals for it and checking on
[46:16] tool selection. So
[46:18] um
[46:20] you know so the question is
[46:23] is your agent doing a good job? If your
[46:25] agent's like doing a good job with the
[46:27] amount of tools you give to it, then
[46:30] then great like you don't have to make a
[46:32] sub agent. So the question like is it
[46:34] doing a good job? Is it selecting the
[46:36] tools when it should select them? Um is
[46:40] it um using an context efficiently?
[46:43] Because sometimes the reasons we use
[46:44] context is because uh the reason why we
[46:48] use sub agents is to reduce the amount
[46:50] of context that's in the main agent. Um,
[46:53] so that would be a potential reason why
[46:55] you might want to use sub agents. Um,
[46:58] so yeah, so I don't I don't think
[47:01] there's a hard and fast
[47:03] uh, you know, hard and fast rule for
[47:05] that. Um, I I you know, I think you want
[47:08] to set up the evals and you want to look
[47:10] at latency. You want to look at cost.
[47:13] Uh, and the cost can be a little tricky
[47:15] to look at because, you know, there's
[47:17] stuff like caching and stuff. So you
[47:19] have to like
[47:21] uh I'm trying to figure I wish it was
[47:23] easier to check the cost. I think if you
[47:25] use the evals I was told if you use the
[47:28] eval in foundry then I think it does try
[47:31] to show you cost there but that might
[47:33] only work for like a hosted agent. Um
[47:35] but ideally you would look at cost. Uh
[47:38] you can certainly look at token usage
[47:39] that comes back from the APIs right and
[47:41] say like how much token usage something
[47:43] used over the whole thing.
[47:46] and um and yeah and then and just see
[47:49] like you know is it selecting the tools
[47:52] at the right time is it selecting too
[47:54] many tools and and then you have to
[47:58] decide I don't think I've seen a limit
[48:00] like in terms of the model like is there
[48:03] an exact tool limit on model I haven't
[48:05] like I haven't seen that I think that
[48:07] the the limits on the model is just how
[48:09] smart they are and how big their context
[48:12] windows are right um but I don't think
[48:15] there's like a hard limit on number of
[48:17] tools per model.
[48:20] Um but he's saying you can you know do
[48:23] let me see where I was doing tool
[48:24] calling
[48:26] results.
[48:29] Um yeah the variance in the models is
[48:32] also we know do they corre do they call
[48:34] the tools correctly and um do they have
[48:37] a hard time deciding which tool to call?
[48:43] Uh, so
[48:45] yeah, I don't think I've any I've seen
[48:47] anything that says, you know, you should
[48:48] definitely, you know, once you have like
[48:50] X number of tools, you should move to
[48:52] sub agents. I think it's going to depend
[48:54] on your models and what your agent is
[48:56] doing.
[49:03] So yeah, Pablo says risk is another good
[49:06] reason to separate agents.
[49:09] Yeah, that's a good point.
[49:15] Yeah, I think like it's is like the the
[49:18] reason that's nice to have lots of tools
[49:20] in one agent is that then you've
[49:21] empowered that one agent with all those
[49:23] tools. So that's really good if you need
[49:25] like a high degree of flexibility.
[49:26] That's why coding agents, we just like
[49:28] load in everything we possibly can,
[49:30] right? Because we have just so many
[49:32] different tasks that we're doing with
[49:34] coding agents. Um but once your tasks
[49:38] are more scoped then you don't need to
[49:41] have you know as many um you know as
[49:44] many possible tools right and then you
[49:47] can lower your risk make your evaluation
[49:50] more deterministic
[49:52] um I mean gosh like evals are so
[49:54] non-deterministic right now because for
[49:56] these rag evals that I'm doing that's
[49:58] not even with tool calls that's that's
[50:00] actually still you know just basic
[50:02] providing the context once you add in
[50:04] tool calls, you have even more
[50:06] variability because it's how many like
[50:08] what order does it call the tools, how
[50:10] many times does it call the tool? Um,
[50:13] you know, and how does it interpret that
[50:16] output, right? You just the amount of
[50:18] variability really increases as you move
[50:21] more and more um toward a full agent
[50:24] with lots of tools.
[50:27] Um, can tools have subtools?
[50:30] Um
[50:31] uh I mean there is something like
[50:33] deferred tool loading if if you're just
[50:35] trying to reduce the context of the tool
[50:37] definitions. Um I don't know if agent
[50:40] framework has support for that but
[50:42] GitHub copilot does it for example. I
[50:44] wonder if they would do it. Tiny
[50:46] packages.
[50:48] Um, what would they call it? Like tool
[50:52] delayed
[50:54] maybe
[50:57] tool execution, tool discovery.
[51:01] Uh
[51:07] h
[51:09] um so certainly coding agents use clever
[51:12] ways to try to reduce the tool context,
[51:14] right? Like so they like will like only
[51:17] you know load in um a top level tool
[51:19] group um or they'll like they'll bundle
[51:22] tools together and stuff. Um, but that's
[51:24] really just like
[51:26] it's it's not like in the end it's just
[51:28] gonna it's it's that's about tool
[51:30] discovery and kind of like delayed tool
[51:32] loading, but ultimately each tool is
[51:35] separate. Um, if a tool has a subtool
[51:37] then that's the same thing as an agent,
[51:39] right? Like that that at least the way
[51:40] you would structure it um would be uh as
[51:44] you know a tool calling uh another agent
[51:48] inside of it.
[51:51] Uh
[51:53] Can tools have or simple tone advice
[51:56] agent? Um
[52:05] yeah so I think in things think thinking
[52:08] about tools with subtools like you can
[52:10] bring in another LLM call in the tool
[52:12] and maybe that LLM call is not a whole
[52:14] agent right um maybe it's just
[52:17] structured outputs so maybe it's just
[52:19] something that says like hey you know
[52:20] based off this just do a simple
[52:23] structured output call right like we
[52:26] only need tools when there's multiple
[52:28] possible things that could happen. Um
[52:31] uh so you don't always have to reach for
[52:33] tools. Sometimes it's a single LLM call
[52:37] um with an output. It just just depends
[52:40] on the the flexibility.
[52:44] All right. Okay. Great questions
[52:47] everyone. Um, I'll dig around for any of
[52:51] the things we're still investigating
[52:56] and I will see you next week and
[53:01] register for the new series. All right,
[53:04] bye everyone.
