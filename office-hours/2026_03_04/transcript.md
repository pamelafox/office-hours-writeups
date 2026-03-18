[00:01] All right.
[00:05] Okay, that
[00:07] looks good. Welcome to our office hours
[00:11] after our fifth session of the Python
[00:15] agents live stream series all about
[00:17] orchestrating advanced multi-agent
[00:20] workflows.
[00:22] What questions
[00:24] do we have from today's session?
[00:30] Okay, this is a kind of a big question.
[00:33] How to increase the performance of a
[00:35] multi- aent system? Can you be more
[00:37] specific when you say performance? If
[00:39] we're talking about quality, latency, uh
[00:43] time, time. Okay. Yeah, that's a good
[00:47] question. I mean, we were talking about
[00:48] today with like magentic, right? like
[00:50] magentic like really um increases the
[00:54] time because it does all this it does
[00:56] all this additional LLM calls. So I
[01:00] would say if you want if you're I mean
[01:01] generally if you're trying to optimize
[01:03] anything about a system you need a way
[01:05] of knowing that your uh of an LLM based
[01:08] system you need a way of knowing that
[01:09] your quality has remained the same. So
[01:12] the very first thing is you you need to
[01:14] set up evaluations, quality evaluations,
[01:17] right? Because then you can start
[01:20] changing things about the system and
[01:21] confirm that the quality doesn't go
[01:23] down. So that's really important is that
[01:25] you set up quality evaluations first,
[01:28] right? And that you have like a ground
[01:29] truth where you can say like, okay, we
[01:30] know this currently is high quality.
[01:33] Then you can start chopping away um you
[01:35] know, start trying different
[01:36] optimizations to um reduce the time,
[01:40] right? Um so so there you know you can
[01:44] try uh you can try smaller models that's
[01:47] what people often try is to you know try
[01:50] quicker models smaller models uh uh that
[01:53] don't you know take as much time uh if
[01:55] you're using a reasoning model you try
[01:57] turning the effort down to none right
[01:59] with GP5 uh point.2 two or and.3 you can
[02:03] set reasoning effort to none and that
[02:06] you know that saves a lot of time uh you
[02:09] can try reducing the uh the output um
[02:14] right like because one thing that takes
[02:15] time is just like LLMs generally are
[02:18] slower based off the number of tokens
[02:19] you're sending to them and the number of
[02:21] tokens that you are outputting right so
[02:24] um so first you want to send as few
[02:26] tokens as possible um so we talked about
[02:29] uh context management techniques in uh
[02:32] was it the second session last week? And
[02:35] so there you can use like sub agents to
[02:37] try and keep your context window small,
[02:39] right? So think you know you there might
[02:40] be ways of um setting up your system so
[02:43] that you can have a smaller context
[02:44] window that's uh context that's sent to
[02:46] each of them. Um and then there's your
[02:49] output, right? How much are you
[02:50] outputting? Right? So if you have it
[02:52] output a one sentence summary instead of
[02:55] a one paragraph summary that's going to
[02:57] be that's going to be um you know more
[03:00] efficient. So um you know those are some
[03:04] some general ideas but I would I'd say
[03:07] like the the first step is to set up
[03:09] some quality evaluations. So then you
[03:11] can say okay we made this change and um
[03:15] you know now we've we've rerun the
[03:17] evaluations we can see that latency has
[03:19] gone down and quality has stayed the
[03:22] same. Um and it's really important
[03:24] because I've done stuff like that and
[03:25] I've run evaluations and I've seen like
[03:27] wow latency you know actually sometimes
[03:30] I make changes to improve quality but
[03:32] then I see the latency went way up and
[03:34] I'm like oh well then it's not worth it
[03:36] right? So um you know you you definitely
[03:38] want those evaluations so that we you
[03:40] can reason about the whole latency
[03:42] quality trade-off.
[03:47] Um okay all right so let's see we have
[03:49] some additional questions. So Zaddy says
[03:51] how do you incorporate ATA protocols
[03:54] into model orchestrations to integrate
[03:56] other agents providers into the foundry
[03:58] orchestration.
[04:00] Um I have so I have not personally used
[04:03] ADA myself. I know we do have support
[04:05] for it built into
[04:08] um agent framework. Oh, and then also
[04:09] wait, let me there's another
[04:10] documentation I want to bring up about A
[04:12] to A just to see
[04:15] uh make sure I'm covering everything.
[04:17] Okay, so host your agent A to A
[04:19] protocol. Um let's see, go deeper.
[04:23] All right, so this one
[04:27] agent function app that's with
[04:30] functions.
[04:32] Uh okay, that's hosting on functions.
[04:34] All right, let's see. What do we link to
[04:35] here? A toa integration. All right, so
[04:39] this
[04:41] this is one of the
[04:44] pieces of documentation. I have I don't
[04:46] think I've read this one yet. Um but
[04:48] yeah, so there is a a like a package
[04:50] like a sub package specifically for A2A
[04:55] where you can say, "Oh, I want to
[04:57] connect to this ATA agent
[04:59] and um you know get back responses for
[05:03] it.
[05:05] Um,
[05:06] so that that is if you're trying to com,
[05:09] you know, communicate
[05:11] with an ATA agent, but that you might be
[05:14] looking for something. I I don't know if
[05:16] that's the kind of ATA you're looking
[05:18] for. Um, but that's what's currently
[05:20] built into
[05:22] uh built into agent framework.
[05:27] Uh, let's see. Can I reshare the repo
[05:29] for finance orchestration? Yep. Uh it is
[05:32] right here. Here you go.
[05:36] There's that repo. It's all linked from
[05:38] the slides as well. So remember you can
[05:41] get everything from this uh this link
[05:44] here.
[05:48] All right. Uh so Pablo asks are there
[05:51] limitations in workflows evaluation
[05:53] using Microsoft Foundry if you deploy
[05:56] our a if you deploy your agent as a
[05:59] hosted agent.
[06:02] Um
[06:05] uh I I don't know. It's a good question
[06:09] if anyone else knows. I haven't messed
[06:10] with I actually have not deployed an
[06:12] agent as a hosted agent yet. So I
[06:14] haven't I haven't tried it. Um, if if we
[06:17] do a follow-up series about hosting
[06:19] agents, then that will give me the
[06:21] excuse to to try it out. Um, but I
[06:25] haven't I haven't even done it myself.
[06:26] So, if anybody else has actually
[06:29] uh used hosted agents and let Pablo know
[06:33] otherwise I'll I'll also ask. Uh, but
[06:35] Pablo, have you tried like what kind of
[06:37] have you tried doing the foundry
[06:38] evaluations? Like are you running into
[06:40] limitations?
[06:42] Bernard says any recommendation for
[06:44] evaluation framework debal ragas others
[06:47] uh well we talked about evaluation in
[06:48] Thursday's session and there I showed
[06:50] the um
[06:53] the uh as your AI evaluation um I
[06:59] haven't tried them specifically for
[07:00] workflows and this a good question like
[07:02] for workflows how should you value
[07:04] workflows I I would say we'd want to
[07:05] probably do something kind of similar
[07:07] where you want to do like high level and
[07:08] lowle so here we talked about for agents
[07:11] you want to, you know, evaluate the
[07:13] agents at a whole and ideally evaluate
[07:16] them relative to ground truth, but then
[07:17] you also want to like break break down,
[07:19] you know, each of the steps. So, I would
[07:21] say for workflows, a workflows like
[07:23] composed of agents. So, once again, I
[07:26] think you'd want to have a um you know,
[07:30] uh evaluate the the final um output of
[07:33] the workflow and ideally compare it to a
[07:35] ground truth. Uh but then you you also
[07:39] want to evaluate each agent. So with
[07:41] each agent along the way, you you could
[07:42] just run, you know, set up these evals
[07:44] for each agent along the way and then
[07:46] just see, okay, when I, you know, when I
[07:48] put these things together, um, what is
[07:51] the response like? Uh, but yeah, I don't
[07:53] think we've like really, let's see, um,
[07:57] talked that much about evaluation of of
[08:00] workflows. I don't know if I Let's see
[08:03] samples
[08:07] evaluation. So, let's see if they have
[08:09] any self-reflection
[08:12] um groundedness evaluator.
[08:15] Yeah, I just want to see if they if
[08:17] they've done any examples
[08:20] specifically with workflow builder. I
[08:22] don't think so. Yeah. So, I don't
[08:24] actually think we've done we have not
[08:26] really done examples evaluating
[08:28] workflows. Um I I would say just the
[08:30] same principles apply where you want to
[08:34] evaluate on the whole but also you know
[08:36] evaluate the what's happening along the
[08:37] way. Um
[08:40] and I use Azure AI evaluation. Um it
[08:44] looks like we're moving towards
[08:48] uh using uh the open AI. So these were
[08:51] the list of packages, right? So I think
[08:53] the we are supposed to be moving towards
[08:56] using OpenAI evals. um for for this. So
[09:00] I need to try that out soon because we
[09:02] have a lot of documentation about how to
[09:03] do use open AI vows with foundry
[09:06] projects. Um so that would be another
[09:07] thing to try. I've done ragas but um I I
[09:12] kind of had mixed success with them. Um
[09:16] some performance issues and stuff. I
[09:18] don't know. And yeah, I haven't checked
[09:19] to see what Ragus is up to lately. I
[09:20] haven't used them in a in six months,
[09:23] which is you know a long time in this in
[09:25] this era. Um we do also agent framework
[09:29] does have um in its lab package it has a
[09:34] few other evaluation frameworks. So TA 2
[09:36] is specifically for customer service
[09:38] agents. So that could be interesting to
[09:40] try. It has all these benchmarks for
[09:42] customer service agents. Um and then
[09:45] there's also Gaia. I haven't tried that
[09:47] one. Oh, it says agents and workflows.
[09:52] That could be fun. Um I found very
[09:54] little documentation about it though.
[09:56] So, I don't I don't know um if that's
[09:59] going to work out or not, but certainly
[10:01] check out there's some interesting
[10:02] things in lab. Um but I would you know I
[10:05] I you know the basic idea is that you
[10:08] know either you're evaluating based off
[10:10] of an LLM as a judge and you know the
[10:13] LLM's going to output yes or no um or uh
[10:17] or like one to five uh with a reason and
[10:20] then you just need to do a batch
[10:22] evaluation, right? So you don't even
[10:24] necessarily have to use somebody else's
[10:26] evaluation framework. The nice thing
[10:27] about using Azure AI evaluation or um
[10:30] open AI evals with the foundry uh
[10:33] projects is that then you can see the
[10:35] evaluations in your foundry portal. So
[10:38] that's that's the that's the nice thing
[10:40] about uh using those.
[10:44] Uh let's see. Okay. All right.
[10:48] Um,
[10:50] so Gwen repeated a question.
[10:54] Um, all right. So,
[11:02] so, so this was a question about a
[11:04] middleware world layer that's saving it
[11:06] to the workflow shared state.
[11:09] Um, and the problem is the middleware
[11:12] doesn't have access to the workflow
[11:13] context and he's manually injecting
[11:15] them. Is there a more native way? Uh
[11:17] it's a good question. I think that let's
[11:19] see if there's do they have discussions
[11:21] enabled on this reboot. Yeah, I think
[11:23] that's such a that's such a age like
[11:26] that's such a deep question that I think
[11:28] it would be um best to ask it year um
[11:31] because I have noticed like that
[11:34] um you know we don't like the middleware
[11:37] I I wonder if like if there needs to be
[11:39] a better middleware story for uh
[11:42] workflow specifically. So, I think it
[11:45] would be best if um to post that there
[11:48] because offhand I'd have to like really
[11:50] try that out myself uh to see
[11:54] uh generally I've been finding a lot of
[11:56] issues and discussions in the agent
[11:58] framework repo and they've been really
[12:00] helpful.
[12:06] Okay, let's see.
[12:09] Yeah, so for evals we did talk about
[12:11] evals of agents. Um, I said more email
[12:14] questions. Okay. How does tracing,
[12:16] logging, etc. work with workflows? Yeah,
[12:18] it should be the same. Let's try it out
[12:20] though because I didn't enable it and I
[12:21] feel bad about that. So, let's go ahead
[12:23] and try that out. Um, so let's find our
[12:28] example that had open telemetry enabled.
[12:30] So, um,
[12:33] uh, from agent framework.
[12:36] Configure provider. So, let's try a um
[12:41] you know, let's just try
[12:44] bringing it into something here. So,
[12:46] we'll import that. And then we just need
[12:49] to call that.
[12:53] All right. And let's go ahead set that
[12:56] up.
[13:00] Okay. All right. And I'm just going to
[13:02] try it with DebUI because DebUI does
[13:06] show traces. So I ideally it's going to
[13:10] show us if it worked. Otherwise we can
[13:12] try it with Aspire or App Insights.
[13:16] But let's try this out with with Debi
[13:18] and see what kind of traces we see.
[13:31] H. Okay,
[13:33] I see some other juicy questions. All
[13:36] right, let's get this. Sometimes WI
[13:38] takes a second to start up.
[13:45] Oh, yeah. So, TLE Taf, you reported the
[13:47] WI issues yesterday, right? So, those um
[13:51] the that was an agent framework issue
[13:53] that was fixed five days ago, but our
[13:55] pin our pinned version is before five
[13:57] days ago. So I put a workaround in the
[13:59] repo instead. Uh but it just had to do
[14:01] there was an issue with agent framework
[14:03] and structured outputs with debi. So um
[14:06] that is resolved now. All right. So here
[14:08] let's look at the um traces. Okay. All
[14:12] right. So let's try right uh LinkedIn
[14:16] post about AI so hot right now. Okay.
[14:21] All right. So let's see if we see traces
[14:24] show up. Okay. I see one hotel spans
[14:30] one turn.
[14:31] I Oh, good, good, good. Great. All
[14:33] right, so this is awesome. Um, we can
[14:36] see the hotel
[14:38] traces
[14:40] in
[14:42] Debui. Uh, so these are all well these
[14:44] are all like spans, right? So, um, this
[14:48] is like, you know, the actual uh, chat
[14:50] completion call and you can see the
[14:52] attributes. You see those geni
[14:54] attributes. So there those are like the
[14:55] custom attributes that are getting sent.
[14:58] Uh message send edge group. Okay. So we
[15:01] can see here. Okay. So on
[15:05] the workflow level because these were
[15:06] ones that we saw before like with when
[15:09] we were tracing agents but now on the
[15:11] workflow level you can see that there's
[15:13] all these parent spans. So we have this
[15:15] parent span for this executive. Then we
[15:18] have a parent span for the edge the
[15:21] actual edge.
[15:23] And then we have a span for the
[15:26] reviewer.
[15:28] Then another um edge group edge group
[15:31] and then the editor.
[15:33] So so there you go. So um yeah work uh
[15:36] agent framework is outputting open
[15:39] telemetry spans for the workflows as
[15:41] well. And so all we had to do there was
[15:44] um you know we just had to say configure
[15:46] hotel providers. We should probably just
[15:48] do them in all do that in all the
[15:50] examples.
[15:52] Uh, it's nice to be able to see.
[15:56] All right. Um, I see there's
[15:59] recommendations
[16:01] of agent agent eval. This is a net
[16:05] evaluation.
[16:08] Uh, cool.
[16:10] Great. So, if you're working innet, um,
[16:12] then that might be that might be good
[16:17] for you. Um, I think like basically what
[16:20] do these frameworks have? A lot of them
[16:21] have like built-in evaluations that use
[16:23] LLM, built-in ways of like summing up
[16:26] the, you know, results that you get from
[16:28] it and like, you know, parsing it. Um, I
[16:31] like that it's also checking latency. I
[16:33] always check latency when I'm doing
[16:35] evaluations as well because sometimes
[16:36] your latency goes way up and it's not
[16:39] worth it, right? Uh, it's checking cost.
[16:42] Uh, so uh, so yeah, so you'll see. Oh,
[16:44] and this one has red teams built in,
[16:46] too. That's cool. Uh, so that's good.
[16:50] You could also like I mean the you I was
[16:53] saying like it's great if you find a
[16:56] framework that you like also feel free
[16:58] like we're in the age of coding agents
[17:00] you could ask GitHub copilot like to
[17:02] write up an make an eval framework for
[17:04] you like if you find that like you're
[17:06] fighting like the whole thing with
[17:07] frameworks is like use them if they work
[17:08] for you and then if they don't don't use
[17:10] them right so if you're if you're
[17:13] finding you want to do like really
[17:14] custom evaluations for your workflows
[17:16] like just just remember the principles
[17:18] of evaluation right are you you are you
[17:20] going to use an LM as a judge or you
[17:21] going to use some other heruristic and
[17:24] how are you going to um track those and
[17:26] then and surface those um I always have
[17:29] to re recommend Haml Hussein um for uh
[17:34] everything related to to eval
[17:37] fantastic blog and he has this u let me
[17:40] find his um his FAQ you can see I search
[17:44] it a lot um LM evolves everything you
[17:47] need to know but yeah subscribe to his
[17:49] blog
[17:50] just everything he writes is just
[17:51] fantastic.
[17:54] All right, so Bernard asks, "Will the
[17:57] Microsoft agent framework be submitted
[17:59] to the AI AI
[18:04] if
[18:05] um which is the new Aentic AI foundation
[18:09] which has MCP goose and agents.md.
[18:13] So, I don't do do things get submitted
[18:16] to this now or do they like how does one
[18:19] decide what's goes in here? Because
[18:21] look, they've got a whole darn protocol.
[18:23] They have an open- source AI agent and
[18:26] then they have a markdown file which is
[18:29] like a great markdown file. I'm very
[18:30] glad it's a standard, but it's like
[18:34] it's it's quite a range of different
[18:37] different um things uh that are part of
[18:40] this. And I don't know how they decide
[18:43] what else they're going to add to it and
[18:45] like whether, you know, something gets
[18:47] submitted to it or whatnot. So, uh I
[18:49] don't know. I really actually have no
[18:51] idea. Um I I think it's kind of
[18:53] fascinating to see um the current uh
[18:56] range of projects that they have. Uh I
[18:58] mean, I think it'd be it'd be most
[19:00] similar to Goose, right?
[19:02] and um you know may they they could I
[19:05] don't know if they I would I mean
[19:07] Microsoft agent framework still has very
[19:09] Microsoft specific and I think it would
[19:11] stay that way because it has so much
[19:14] integration into into Microsoft tools.
[19:16] It is also has a lot of agnosticism
[19:18] which is great. Um but it definitely has
[19:21] a lot of integration into
[19:24] Azure and Microsoft. So, so I don't
[19:28] know. I don't know. Who knows? Could
[19:31] happen. I haven't heard, but
[19:34] um Oh, common patterns.
[19:37] Uh yeah, common patterns for agent
[19:40] frameworks. Uh you know, yeah, stuff
[19:42] like handoff and stuff like that. I
[19:45] think what you'll see I my observation
[19:47] is that I don't think that Microsoft
[19:50] has really like I don't think most of
[19:53] the protocols have started with us like
[19:55] ATA that was what um Google right MCP
[19:59] was anthropic so I think that you know
[20:02] when patterns emerge it seems more
[20:05] likely that what we'll see instead is
[20:07] that agent framework would bring in that
[20:10] pattern right so I do expect agent
[20:12] framework to support big protocols and
[20:14] patterns that come out, you know, the
[20:16] things that everybody's talking about,
[20:18] right? So, we've got support to AD to
[20:19] AA, we've got support to AGUI.
[20:22] Um,
[20:24] I don't I don't know if we're going to
[20:26] see um terminology leak the other way
[20:29] from agent framework out to the
[20:31] industry. I haven't seen that happen yet
[20:33] with Microsoft stuff. So um because I
[20:37] think generally the protocols are coming
[20:39] from the uh the people that are
[20:41] developing the the LLM frontier models
[20:44] and we don't have uh we don't have any
[20:47] of our own like frontier models yet I
[20:50] would say um so
[20:53] yeah
[20:55] uh the protocols tend to be coming from
[20:58] Google Anthropic etc.
[21:05] Uh let's see. Um
[21:08] I think that generally like let's see
[21:10] what terms are a lot of these terms I
[21:12] think are similar like the middleware
[21:14] term is the same like across link chain
[21:18] um what terms are are different here uh
[21:24] the orchestrations right so concurrent I
[21:27] think concurrent that's a just standard
[21:28] programming term right handoff I don't
[21:32] know if handoff I yeah it's a good
[21:33] question whether handoff is that
[21:35] something that we see other frameworks
[21:38] talking about. I'm not sure. Magentic
[21:40] certainly came from Microsoft um and
[21:43] autogen right originally and I don't
[21:45] think other um you know frameworks have
[21:48] done like lingchain has their own you
[21:49] know take like they've got their own
[21:51] orchestrations basically like deep
[21:52] agents is you know uh you know a lingch
[21:55] chain specific orchestration right and
[21:59] um
[22:02] you know they they have their
[22:05] orchestration here
[22:07] um
[22:09] And it kind of it's kind of similar to
[22:10] like it's like a built almost like a
[22:12] built-in orchestration for Lchain,
[22:15] right? They do it as a separate package.
[22:19] So yeah, it would be nice if we all use
[22:21] similar terminology. Um but uh
[22:25] I don't know. It's hard like even
[22:27] terminology like agent harness like what
[22:29] is an agent harness? Like I finally now
[22:31] have my idea of what an agent harness is
[22:34] uh or what is context.
[22:36] It takes us a while to agree. Exactly.
[22:40] Uh Microsoft doesn't need their own
[22:42] Frontier models since we own 30% of the
[22:44] OpenI for profit entity. Well, I think
[22:47] it would be nice if we had some really
[22:50] good Frontier models that were entirely
[22:51] ours. Just in case we might disagree
[22:54] with things that Well, this is just me.
[22:56] When I say we, in case I disagree with
[23:00] things that Opening Eye does, uh, I like
[23:03] being able to move off of Opening Eye,
[23:06] but that's just me.
[23:10] Um, let's see.
[23:21] Let's see. So, Satcha also asked about
[23:23] versioning systems.
[23:25] Um yeah, when you're versioning your
[23:28] this this this is a discussion I had
[23:31] with folks um at a conference at Pyon
[23:34] last year, like prompt versioning,
[23:36] right? Like where do you put your
[23:37] prompts? That was back when everything
[23:39] was based off prompts. Here's the thing
[23:40] now is like you have your prompts, but
[23:43] you also have your tool descriptions.
[23:45] And your tool descriptions are usually
[23:48] going to be in the code. So inevitably
[23:50] some part of your prompt is in the code.
[23:52] So given that the tool descriptions are
[23:54] in the code, is it worth it to actually
[23:56] move the prompts into their own special
[23:58] versioning system? Because if you do
[23:59] that, are you also going to move your
[24:00] tool descriptions and your arguments in
[24:02] the code? Because all of those, you
[24:04] know, that like all of those go into the
[24:07] the LLM process, right? So now that we
[24:10] have natural language in our our actual
[24:14] um tool descriptions as well, can we
[24:17] actually,
[24:19] you know, version and store the prompts
[24:21] separately from the code? So I think at
[24:23] this point, no. Um, what you can do is,
[24:26] I mean, you could have the system
[24:27] prompts could be in their own files
[24:28] because your system prompts might be
[24:30] particularly long. So I often will put
[24:32] my prompt in a markdown file or in a
[24:34] ginger file if I need templating, right?
[24:37] Um, and then and then pull that in. So I
[24:39] do think it it makes sense to have those
[24:41] be in separate files, but probably just
[24:43] in your codebase. And then your
[24:44] versioning is just inside your codebase.
[24:47] And then you can run evaluations, you
[24:49] can tie evaluations to your PRs, right?
[24:51] like I have some workflow some um
[24:54] repository set up with evaluation you
[24:56] know workflows that I can trigger if I
[24:58] want to evaluate uh you know a
[25:00] particular um PR let's see I think it's
[25:03] this one evaluate right so so I think at
[25:07] this point that um you know your your
[25:10] prompts and your tools are just you're
[25:11] in your codebase and that's how they're
[25:13] being versioned and you can you know um
[25:17] try and have prompts being in separate
[25:20] files but I think ultimately it's
[25:21] easiest to put in the codebase. So here,
[25:23] yeah, if I ask to evaluate, then I set
[25:27] everything up. I run my evaluation on um
[25:31] just the this one's just running off the
[25:33] local app running inside the um GitHub
[25:36] runner. And then I tell it where to
[25:38] store the results in a folder for that
[25:40] PR. I can upload the evaluation results
[25:43] as an artifact. I can summarize results.
[25:45] That's just to give you an idea for um
[25:47] how you might do uh you know workflows
[25:51] for evaluation that you know you could
[25:53] set it up all kinds of ways.
[25:58] Um there are the fi models. I would love
[26:01] to know if anyone has managed to use the
[26:04] fi models in production for anything. Uh
[26:06] I did not find them useful for rag which
[26:09] is you know what I do most of my time
[26:13] usually is on rag. Um,
[26:17] let's see. So, Bernard also says, "Some
[26:19] we're talking about versioning, you have
[26:21] weights during training."
[26:23] Um, yeah, if you're do are you talking
[26:26] about doing like fine-tuning? If you're
[26:27] doing fine tuning,
[26:30] uh, then then you'll want to add a whole
[26:32] other system as well.
[26:44] All right. What other other
[26:47] questions? Let's see.
[26:51] LM Ops.
[26:54] All right. What else? I'll just flash
[26:56] the slides to
[26:58] remind you of things we talked about
[27:00] today. Okay. So, here we go.
[27:03] Concurrency. Concurrency. Aggregation.
[27:06] Some really fun aggregation. Uh, I want
[27:09] to do this but with like the copilot SDK
[27:11] agent. I think that'd be fun. So I can
[27:14] have it automatically uh start farming
[27:16] out my coding tasks. Do some aggregation
[27:22] uh conditional concurrency
[27:25] magentic
[27:29] and handoff.
[27:34] Uh yeah, so Bernard says to debug a
[27:36] workflow, we can also set break points
[27:39] in VS Code. That's a good question.
[27:42] Let's try this out. We haven't set up
[27:44] our We haven't really set up our Oh, we
[27:47] do have a launch.json. Okay. All right.
[27:50] Let's try this out and see.
[27:54] Um so we'll set some break points.
[27:59] Uh I'll just set it on the edges.
[28:02] Okay. The thing is that we don't really
[28:04] have like an agent like this agent has
[28:07] no it's just a class right so um if we
[28:12] wanted to break inside the agent it
[28:13] would have to be like in the actual
[28:16] you know like the event for the agent or
[28:19] we'd write middleware right so you might
[28:21] have like a debugging you could write a
[28:23] debugging middleware but let's just see
[28:24] if we can even do um do any of the
[28:27] agents okay so let's see
[28:30] uh debug
[28:34] default interpreter
[28:37] path. Okay, just want to make sure my
[28:40] Python environments have been a little
[28:42] odd. All right, so let's try using the
[28:44] debugger
[28:47] and so I've got some Okay, so it's
[28:49] running the debugger.
[28:52] Is it going to work with UV workspace
[28:56] VM bin Python?
[28:59] That's right.
[29:01] Okay. Uh, yeah. Okay. All right. Oh, I
[29:04] set the Okay, that was a silly place to
[29:06] set an end point, but that's promising
[29:08] that we got there. Um, I should set the
[29:11] end points that you should set the break
[29:12] points inside the functions. Um, not on
[29:16] the actual signature.
[29:18] Okay, we're just going to go play. All
[29:20] right. All right. I set the break points
[29:23] in silly places, so I'm going to stop
[29:25] that debugging session. Okay. No, the
[29:27] breakpoint should be Oh, that's weird.
[29:28] Oh, I did it on the dock string. All
[29:30] right. Apparently, you should not add a
[29:32] breakpoint to a dock string. All right.
[29:34] So, let's
[29:36] If you do a breakpoint on a dock string,
[29:38] it becomes a function signature. Okay.
[29:40] All right. So, do not add break points
[29:42] to dock strings. Do it to the actual
[29:44] first line of code. Okay. All right.
[29:47] Now, let's try it.
[29:52] Okay.
[29:58] This is fun actually. I I It's always
[30:01] really good when you actually can get
[30:02] the debugger um working on on whatever
[30:05] you're working on because then it's more
[30:07] helpful. Oh, we're seeing the um the
[30:12] those are the open telemetry events
[30:14] because I have in my EMV I have enable
[30:19] console exporter is true. So we're
[30:21] seeing like all this um these are just
[30:24] the hotel uh things getting sent out.
[30:27] Okay. Uh so now it did break. Great. So
[30:31] we can see on the agent executive
[30:33] response we can look at the actual agent
[30:35] response and we can see the text
[30:39] from there. Uh so yeah. Oh I should have
[30:43] done this the other day when I was
[30:45] debugging that that bug we had
[30:47] yesterday.
[30:48] Uh so you can you can do breakpoint
[30:52] debugging with your workflows uh as long
[30:55] as you have a place to put the
[30:56] breakpoint. Um so here I was able to
[30:59] place it in the edge functions. Um you
[31:03] know for agents
[31:05] you would I think you just have to write
[31:07] a middleware for debugging so that you
[31:10] had a place to break
[31:18] All right, cool. Good question.
[31:23] Let's see if there's any more questions.
[31:24] See, there's someone typing there. Let
[31:27] me turn off my hotel insights. They're a
[31:31] bit
[31:33] wordy.
[31:49] All right, I'm just gonna see if we have
[31:51] any more questions
[31:54] before we close it up for today.
[31:58] Um just as a reminder of you know
[32:00] middleware like if we want to do debug
[32:02] middleware
[32:05] you can even just tell copilot like add
[32:09] uh BS code debug middleware
[32:15] uh because remember like you know
[32:17] actually like copilot wrote a almost all
[32:19] of these examples with my heavy heavy
[32:23] influence. Um but uh you can see I saved
[32:26] my plan because people asked about this
[32:28] before like oh how do I do this right?
[32:30] So um when I was planning the
[32:33] presentation for tomorrow spoilers but
[32:36] um I gave it access to
[32:39] asky versions of the two previous
[32:41] slides. I gave it the description from
[32:42] reactor. I gave it the outline that I
[32:44] had come up with based off of um looking
[32:47] through the docs. Uh some open
[32:49] questions, some to-dos and then
[32:52] finalized plan. Right? So these are the
[32:54] samples uh and then implementation steps
[32:57] and then these were actual slides. Uh so
[32:59] that's spoilers but uh I ended up I did
[33:03] experiment with having to generate the
[33:05] PowerPoint based off of the slides. I
[33:08] didn't like the output. Uh it just
[33:12] wasn't well formatted. So I made the
[33:14] slides manually just looking at it what
[33:16] it thought should be in the slides. And
[33:20] uh I thought that was easier than trying
[33:24] to fix the formatting that it did.
[33:28] Um
[33:31] we have all the patterns. Do we have the
[33:33] problems that they solve
[33:34] architecturally?
[33:36] Uh
[33:38] do you mean like what you know what
[33:39] scenarios are we going to actually use
[33:41] them for? Right. Um, and I have to say
[33:45] it's it's, you know, I I can show you
[33:48] the patterns. I can't like give you the
[33:51] scenarios because there's only so many
[33:53] scenarios that I have currently in my
[33:55] life that I can try um, automating. So,
[33:59] um I will now that now that I like I
[34:01] didn't really know agent framework until
[34:03] like two weeks ago. But now that now
[34:05] that I know uh more about agent
[34:06] framework and how to do them, I will
[34:08] start trying to um automate more of my
[34:11] workflows using agent framework um
[34:14] possibly in conjunction with the copilot
[34:16] SDK because a lot of my tasks are are
[34:19] coding tasks and the copilot um you know
[34:22] agent is particularly good at that. So
[34:25] so yeah. So um you know I I can't really
[34:28] I can and I'm showing I'm you know we're
[34:30] showing like end toend applications that
[34:32] also show off some scenarios but um it's
[34:35] hard for me to say you know for sure
[34:37] what problems they're going to solve for
[34:40] you know for each organization
[34:42] uh you know because I'm I'm I only have
[34:45] my own job as an advocate that I can try
[34:48] to automate with workflows and I can
[34:51] hear from other people what they're
[34:52] doing. So if you are using workflows and
[34:54] agents in production in your
[34:56] organization, please do share how you're
[34:58] using it and what they're been useful
[34:59] for you for to give inspiration to other
[35:02] people and also share what they don't
[35:03] work for. Like I know I've talked to
[35:05] people that have tried to do things and
[35:06] they ended up finding like things that
[35:08] didn't work for them. So it's really
[35:10] helpful to both hear what works and also
[35:12] what what doesn't work, right? U but I
[35:15] think we're still early days. Like
[35:16] honestly like we know at this point that
[35:18] coding agents are incredible. All right,
[35:20] that they like it's just the perfect use
[35:23] case for LM's code is very structured.
[35:25] It it knows these coding languages
[35:27] better than we do at this point. It's
[35:29] seen so many patterns, right? So, we
[35:31] know that coding agents are really
[35:33] powerful. So, um you know, I think a lot
[35:35] of the stuff that um that the automation
[35:38] that that I do is going to be with with
[35:42] coding agents because that's you know,
[35:43] what what I'm dealing with the most. Um
[35:46] but yeah, I would love to hear more from
[35:50] where people are uh able to use
[35:53] workflows in production and um what's
[35:56] yeah, just what scenarios they're
[35:57] particularly good for. Um you know, for
[36:00] me, if I find scenarios before where I
[36:02] was using I've mentioned this before,
[36:03] like with like regular expressions,
[36:04] right? Like gosh, like LLMs can be much
[36:09] better at that fuzzy matching uh that um
[36:12] than regular expressions, right?
[36:15] Um, but there's other workflows that you
[36:18] know may not exist at all at this point
[36:20] that you could you could make new
[36:22] automation for because of having access
[36:25] to these.
[36:31] See Pablo's typing. I know Pablo has I
[36:33] think Pablo has some stuff that they're
[36:35] actually doing it for. So maybe he has
[36:37] some ideas to share. Oh, okay. Pablo's
[36:41] question. the OpenAI real time API with
[36:44] MS Asian framework. Oo, there was just a
[36:47] chat about the new real time because I
[36:50] know we just came out with new models.
[36:54] Um,
[36:56] let's see. I and I haven't played with
[36:58] the new
[37:00] models yet. Let's just see if there's
[37:03] any mention of real time.
[37:06] No, don't real model ID.
[37:14] What is it using it for? Let's see.
[37:17] Nowhere.
[37:20] Uh,
[37:23] somebody
[37:24] I don't Let me see if I can log into
[37:26] Slack. Can I log in and then move it to
[37:28] this
[37:30] side? Okay, I'm going to move it over
[37:32] here. See, I can't see it. Okay, close.
[37:37] All right. Uh, Uh
[37:44] okay. So let me just search because
[37:46] somebody mentioned at real time.
[37:50] Uh
[37:52] team
[37:56] okay there's a new GPT real time 1.5
[38:01] and let me see
[38:04] what things people chose.
[38:09] Uh,
[38:11] okay. So, Bruno Capuano.
[38:15] Um, okay.
[38:19] So, this is one
[38:21] this is.net real time audio.
[38:25] Oh, so this is using
[38:29] Microsoft Asian framework andnet.
[38:33] Um, I don't know how up to date
[38:36] looks fairly up to date. So I would chat
[38:38] with
[38:40] um Bruno
[38:43] uh who you probably know from other
[38:44] other stuff he's another advocate. So it
[38:47] looks like he has done some
[38:52] combination of real time API
[38:56] uh with with agent framework.
[39:00] Um,
[39:01] so we go
[39:04] LM chat where we have the real time.
[39:08] Well, I don't know if this is actually
[39:10] using the real time models. Yeah,
[39:12] because these are whisperers, speech
[39:14] text. These are text models. This is
[39:18] text to speech voice activity. Okay. So,
[39:24] I don't know if he's using the real-time
[39:26] models, but I think he wants to use
[39:27] them. I think that's what he said in our
[39:30] in our chat.
[39:33] Let me see.
[39:41] Okay. Oh, he said it does use the first
[39:43] um Oh, here we go. Real time audio. Oh,
[39:46] this is another one. All right. Here's
[39:47] another sample. So, this one is another
[39:51] net one. Real time audio.
[39:56] I don't think this one is using agent
[39:59] framework though because this was made
[40:00] this was made a while ago. Um but uh he
[40:05] says he wants to do some updates with
[40:08] that one too. So I would check out those
[40:12] and you know maybe just uh message him
[40:14] on LinkedIn um to see
[40:18] if he has any additional uh advice or
[40:20] samples.
[40:25] One question we get lots I know we
[40:28] always get requests for WhatsApp and now
[40:30] real-time audio. So I think we like we
[40:32] need to show all the overlap of agent
[40:34] framework with these uh different
[40:36] modalities of communication.
[40:41] All right. Do we have any other
[40:43] questions?
[40:50] Can we get the full stack code for the
[40:52] ai finance agent? Uh yeah. Yeah, that's
[40:56] uh I shared it earlier in the chat
[40:58] today. Um this is the investment. So as
[41:01] I mentioned, this one is
[41:04] um
[41:06] this one is using an old version of
[41:09] agent framework. So and I got to say
[41:12] they didn't did not pin. You always got
[41:15] to pin people. Pin pin pin. So if you
[41:17] look at the requirements, it does not
[41:20] say which version. Um, they did actually
[41:22] message me and tell me what version. And
[41:24] this is the only one without a pin too.
[41:25] Like please, you have to have to pin
[41:28] agent framework. Like I mean, you have
[41:29] to pin everything. Like you should never
[41:31] um, you know, have something without a
[41:33] version, but particularly you know the
[41:35] agent framework, but really for
[41:36] everything. I've been broken by every
[41:38] dependency. Um, so it's hard to run it
[41:41] right now because of the lack of the
[41:43] pin. Um, but he said like like in the
[41:45] next few weeks they should they should
[41:47] update it. And yeah, this has a front
[41:50] end. This is built in. I think it's
[41:52] React because they're using React Flow.
[41:54] You see that when it says React Flow,
[41:56] they're using that React Flow component.
[41:57] So, React
[41:59] Tailwind and then the back end is with
[42:04] uh fast API.
[42:08] Yeah. Let me see if I can get the
[42:12] um Oh, let me get the version number for
[42:15] that one so that you can
[42:19] uh you can run it because right now
[42:21] you'll you get all these errors if you
[42:23] try to run it. But he he Davidid he's
[42:26] the one working on it um along with some
[42:28] other folks. He did tell me what to use.
[42:33] He says oh he says next week they should
[42:34] have it updated. All right. So, it'll be
[42:37] updated really soon. Um, okay. So, he
[42:40] said
[42:44] it is
[42:48] that. So, you can try getting it running
[42:50] now with that version or just wait a
[42:52] week and it should be updated to the new
[42:55] map.
[42:58] All right. Okay. I think we It looks
[43:01] like we're um Do we have any other
[43:06] questions. All right, cool. All right,
[43:08] then I will call it here so I can
[43:13] uh start prep for
[43:16] our next sessions. Uh thank you so much
[43:19] for joining the live stream and for
[43:21] bringing your questions here. We'll see
[43:22] you tomorrow for the final session. Bye
[43:25] everyone.
