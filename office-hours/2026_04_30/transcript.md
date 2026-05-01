[00:02] Welcome to our office hours for today's
[00:05] session from the hoster agents on
[00:08] foundry series. Today we talked about
[00:12] quality and safety evaluations.
[00:15] And so if you have any follow-up
[00:19] questions
[00:21] uh and I see we already have questions
[00:23] great from Gwen. Uh so yeah, post any of
[00:26] your questions in the chat and we'll
[00:28] answer whatever we can. And a lot of
[00:30] times we I may not have a direct answer
[00:33] for your question, but I will go and
[00:36] like you know talk to the product team
[00:38] afterwards and uh so sometimes you can
[00:41] just ask me the day after like hey did
[00:42] you get an answer to that question like
[00:44] and then I also I put all the questions
[00:46] in um in in this uh resources thread
[00:51] too.
[00:53] Okay, so we have qu So Gwen was saying,
[00:56] are there evals that will score on cost
[00:58] and token efficiency? Um, so you can
[01:02] always like write your own custom evals.
[01:04] So like when I do evals, I always look
[01:06] at latency for example. So that's always
[01:09] um like a you know something that I
[01:12] measure. Um
[01:16] uh I haven't tried setting up custom
[01:18] evals in the new version of Foundry just
[01:20] I so I'm not sure exactly what the code
[01:22] would look like for that. Um but um yeah
[01:26] I would say
[01:28] I think we let me see how how do we do
[01:30] custom evaluations?
[01:33] Uh custom
[01:36] let's find the docs for it. Um but yeah
[01:39] so I would generally say so you can uh
[01:42] you know latency is easy to measure
[01:43] because it's just the amount of time
[01:44] that elaps but the other thing is for
[01:46] token usage that is usually something
[01:47] that comes back in the response
[01:49] depending on um you know which API is
[01:52] being used. So
[01:55] you should in theory be able to do a
[01:57] custom evaluator that looks at that
[01:58] token usage. Uh
[02:03] uh I just haven't written the code for
[02:05] it exactly in with this one, but let's
[02:08] see
[02:10] if I can get a feel for how to do it.
[02:13] It's a good question. I I think it's a
[02:15] good idea to look at that like when I
[02:17] did my um
[02:20] yeah, pan Foxy AI MCP tool schemas.
[02:28] Uh
[02:30] dot okay
[02:34] where's so usually I do look at where's
[02:37] my token usage oh yeah yeah so like this
[02:40] one right so like when I'm doing this
[02:42] was a different kind of evaluation I did
[02:44] but I I looked at the the latency as
[02:47] well as like the size of the tokens for
[02:49] something so let's see um custom
[02:53] custom evaluators okay
[02:56] custom evaluators
[02:58] How do we do it? Returns. Okay. So, you
[03:02] write a Python function and you can use
[03:05] Oh, cool. You can use like these
[03:06] built-in packages. Interesting. All
[03:07] right. So, it's actually running the
[03:08] code in the cloud then. Um, so you would
[03:12] want to do it with a codebased
[03:14] evaluator.
[03:16] So the question is what like as long as
[03:19] this evaluator
[03:21] received information that had the token
[03:23] usage in it then it should work. Now I
[03:28] think the big question is whether we
[03:31] would like from the sample is token
[03:34] usage in the sample? Um so you have to
[03:36] really look at the output from the API
[03:38] and see whether the token usage is in
[03:40] there. Generally with the responses API,
[03:43] it usually does include token usage, but
[03:46] I you know we we'd have to really check
[03:48] and and see. Um so that would be the
[03:50] idea is that you you you write this
[03:52] custom evaluator. Um and uh hopefully it
[03:56] has that token usage. If this doesn't
[03:58] work, then you know um token usage
[04:00] should also be in should be in open
[04:04] telemetry traces too. So that would be
[04:05] another way of evaluating. Um, but I
[04:08] would I would try to do it with this way
[04:10] first. Link to this one. Uh, yeah, I
[04:13] mean that's a to-do as well. Like we
[04:15] need I need to do some examples of
[04:17] custom evaluators because we didn't show
[04:18] any in today's um because you can do
[04:21] codebased evaluators and prompt based
[04:22] evaluators like you know that's LM as a
[04:24] judge and then you can set them up with
[04:28] the same SDK that we were using today.
[04:32] Uh, okay good question. Are there any
[04:34] built-in evaluators which do not depend
[04:36] on the leng as a judge approach? There
[04:38] are some I wouldn't recommend most of
[04:41] them but we can look at them. Um uh
[04:45] these ones right so there's all these
[04:46] textual similarity evaluators. These are
[04:48] using
[04:50] pretty like old school means of doing
[04:52] similarity. Um this one uses LM but the
[04:55] rest of these are all using these
[04:56] different kinds of similarity metrics.
[04:58] And usually for agents that are doing
[05:01] like full text responses, these just are
[05:03] not useful. Um I have to find Okay, so
[05:07] Hamill who's saying he's like this
[05:09] expert on um evals and he's got these
[05:12] evals memes. So whenever you're like
[05:15] talking about evals and you need a meme,
[05:18] you can check his his meme images and he
[05:21] meme images and he has one. Let me see
[05:24] if I can find the one
[05:26] um about the F1 score. Uh
[05:35] I don't see the one, but I I do just
[05:39] crack up whenever I look at the stuff.
[05:40] Uh so yeah, so generally um I haven't
[05:44] found any use for these old school old
[05:47] similarity scores anymore, but maybe
[05:49] depending on what you're doing, they
[05:51] might be useful for you. So that they
[05:52] are available. Um they're, you know,
[05:55] they're from the NLP research space. So
[05:57] those are available. They don't use
[05:58] LLMs. Um these ones all use
[06:02] LLM.
[06:05] Um
[06:08] I think these all
[06:12] model score. I I think that all the rest
[06:15] of those ones do use
[06:18] um LLMs for a thing, but saying as we
[06:23] just saw, you can do custom evaluators.
[06:24] And so some custom evaluators can be
[06:26] really helpful without using LMS. So for
[06:29] example, I have a like a codebased
[06:33] evaluation that I use for my rag
[06:35] application uh to compare answers to
[06:38] ground truth and it just does a regular
[06:40] expression to check that the citations
[06:42] are correct. Right? So it says, "Hey,
[06:44] for the answer we got, do we see the
[06:47] same citations as we saw in the ground
[06:49] truth?" And that's actually one of my
[06:51] most useful evaluators. And that's just
[06:53] doing a reax. Um, so there certainly
[06:55] are, you know, evaluations that you
[06:58] could write that can be useful that
[07:02] don't use an LLM. Um, so these codebased
[07:06] evaluators, uh, it's and it's useful to
[07:08] measure just stuff like token usage,
[07:09] latency. Um, so there are a few things
[07:12] like that. Um, but for evaluating like
[07:16] what the like free flowing text looks
[07:18] like, then we're usually going to use an
[07:19] LLM.
[07:23] So Pablo says, "For each quality
[07:26] evaluator, the context of the agent is
[07:28] more than the query. Um, how can we take
[07:31] that into account?" Yeah. So something I
[07:34] kind of glazed over
[07:36] um is that uh let's see, let me do here.
[07:40] um quality eval. All right. So here,
[07:43] remember when we were setting these up,
[07:45] response says output items. The output
[07:49] items is not just the final output. It
[07:52] does actually have all the tool calls in
[07:54] it. So even though some of these like
[07:57] you know I said intent resolution was
[07:58] just an ET to E one just looking at
[08:00] query response, it does actually look at
[08:02] everything along the way. So um because
[08:05] if you're doing memory a lot of times
[08:06] memory it depends how memory was
[08:08] implemented but if the memory is like a
[08:10] tool call that's going to be an output
[08:12] items. Um
[08:14] so yeah I guess it depends how you've
[08:17] implemented memory but if it's somewhere
[08:20] in the you know in the in that
[08:23] conversation thing you might find that
[08:25] you do end up seeing that memory in
[08:27] output items. Uh now if you don't then
[08:30] you know maybe it's something you can
[08:32] add to to it. Um
[08:38] I but now we're using hosted agent so we
[08:40] have to somehow like you'd have to
[08:41] somehow stuff it into the responses API.
[08:45] Um, so I think we really have to like
[08:46] look and see what what does the output
[08:49] of the API look like when you're using
[08:52] that agent with memory and does it
[08:54] already include
[08:57] what you're thinking of as memory or is
[08:59] there some way to inject it in there um
[09:02] so that it can be accessed right because
[09:04] basically it needs to you know because
[09:06] this is just doing an API call so it
[09:08] needs to be somewhere in that API
[09:11] response so that we can pull it out in
[09:13] order to do an evaluation.
[09:15] Um, now I think the thing that's a
[09:17] little tricky is that if when we're
[09:19] using Foundry hosted agents, we're
[09:21] adhering to the responses API and using
[09:22] the responses API adapter. So, we can't
[09:25] necessarily just stuff every
[09:29] um or I I'm not sure if we can is a good
[09:32] question. Uh, if you're doing you can
[09:34] also use these evaluations like on your
[09:37] you know on other targets, not just
[09:39] founder agents. Um and there you you
[09:43] will have like if you have more control
[09:44] over it then you can you can output your
[09:47] API in any shape. In this case we are
[09:50] outputting from the responses API. So
[09:51] yeah we just need to look at and see uh
[09:54] you know what is actually in that
[09:56] response from the API and if we can get
[09:58] it to be in that API response then we
[10:01] can pass it to the evaluation. Um but if
[10:03] it's not in the API response, if it's
[10:06] hidden, uh then you know it's not able
[10:09] to evaluate it, right? Because how how
[10:11] would it get access to it? It either has
[10:12] to be in the uploaded data set um or it
[10:16] has to be in that API response
[10:17] somewhere.
[10:22] Oh yeah, good question. Okay.
[10:25] In a multi- aent environment, should we
[10:27] have a vows for each agent versus the
[10:29] final response? Yeah, I mean I think
[10:31] that I I would say yes because that each
[10:34] agent is it's just going to give you
[10:36] more information, right? So that you
[10:38] know the end toend test, you know,
[10:39] that's good. Um you start off with this
[10:42] end to end t you know test to give you
[10:44] an idea of overall. Um but if you you if
[10:47] you however you can break it down the
[10:48] better because that's going to like show
[10:50] you like okay end to end I'm getting a
[10:52] failure. Why am I getting a failure? Oh
[10:54] it's all because of this one agent.
[10:56] Right now I don't think we have a like a
[10:58] built-in multi-agent now but it depends
[11:01] on how you've implemented your
[11:02] multi-agent because sometimes when we
[11:03] implement multi-agent we actually are
[11:05] implementing using the agents as tools
[11:08] architecture. So if you're implementing
[11:10] using the agents as tool architecture
[11:11] then you basically can just use you know
[11:15] any of these tool ones because each of
[11:17] your sub agents is itself a tool and
[11:20] you're just figuring out okay did it
[11:21] call this tool correctly and you know
[11:24] what's the response from um but you also
[11:27] might want to I guess that's a bit
[11:29] different because you also maybe you you
[11:31] could also isolate each of those agents
[11:33] and try and call them separately. Uh, in
[11:35] order to do that, you would need them
[11:36] each to be to to have a way of calling
[11:40] them separately. Um, that might be
[11:42] tricky. So, you may want to just do a
[11:44] custom evaluator in that case, right?
[11:46] That might be because right now I I
[11:48] think you'd either need a separate
[11:49] endpoint for them or you would want to
[11:52] do
[11:54] um you'd want to do a custom evaluator
[11:57] that says, "Okay, for this sub agent,
[11:58] how is it doing? For this sub agent, how
[12:00] is this doing?" Uh so yeah, it just
[12:02] depends on how you've orchestrated those
[12:04] multi- aents. Um so if they are agents
[12:08] as tools, some of these might be
[12:09] helpful, but you could also set up a
[12:11] custom evaluator as well.
[12:17] Uh so Pablo says, uh you read that an
[12:21] option could be used in SOM to
[12:22] pre-process traces and feed each of them
[12:24] into a knowledge graph to extract
[12:26] entities and relationships. This would
[12:28] help reduce LM costs instead of
[12:31] evaluating traces using an LLM from
[12:33] text.
[12:35] Um
[12:38] let's see. I'm trying to understand that
[12:40] approach there. So
[12:43] um yeah well oh I oh one thing I forgot
[12:47] to show was the cluster evaluation.
[12:49] Let's see where is it? Okay. So that
[12:51] reminds me of this. Um there is this
[12:54] like that's this isn't the same thing,
[12:56] but uh there is this button here to
[12:58] analyze results and this does a cluster
[13:00] analysis
[13:02] and like this one. Oh, this one had like
[13:04] 178 samples. This actually probably be a
[13:06] pretty interesting one to do. Let's see
[13:07] if we can do it. Um so it's going to
[13:08] take 2 minutes and 10,000 tokens. Uh so
[13:12] this is going to look at because it's
[13:14] kind of overwhelming to look at a lot a
[13:16] lot of data, right? Uh, and so it's
[13:17] helpful to,
[13:19] you know, pass that into here. Uh, let's
[13:21] see if it's it'll if my foundry is
[13:24] logged in. I think it looks like it's
[13:25] working. Um, anyway, so that just
[13:27] reminded me of that. So, whenever you
[13:29] run an evaluation, you'll find this
[13:31] little analyze results button on it and
[13:33] it'll do a cluster analysis and try to
[13:36] like find different kinds of failure and
[13:38] and make little clusters for the
[13:40] different kinds of failures. Um, so then
[13:42] you can dig in because this is the kind
[13:44] of thing you'd want to do. This is kind
[13:46] of a data science thing. This is the
[13:47] kind of thing you'd want to do when you
[13:48] were if you were manually looking at
[13:50] data. Um, so the idea here is just to
[13:51] make it a lot faster to cluster the
[13:54] different kinds of failures.
[13:57] Um, so yeah, so I so probably yeah, I
[13:59] haven't read particularly about that
[14:01] approach. Uh, I guess it depends like
[14:04] yeah, what your LM costs are if it's
[14:07] taking too long too too much money to
[14:09] evaluate with the um evaluators. Oh, so
[14:12] this is cool. So, it found Okay, so it
[14:14] said 73 samples had a hallucinated
[14:16] response. Okay, so that's not good. Um,
[14:19] so then I could like Yeah. And so then
[14:22] we have Oh, and then it's got
[14:23] suggestions. Oh, this is so cool. Okay,
[14:26] so uh then so it has 73 samples that it
[14:30] found for this. Um, and then Oh, and
[14:33] then there's also required rule
[14:35] unavailable. Oh, that's really cool.
[14:38] Abrupt refusal.
[14:41] And then
[14:43] do we get to like look at the samples?
[14:46] Uh this object let me report this as a
[14:49] there's this like object object that
[14:50] shows up. I got to report that. Um
[14:54] oh but here we can see there's the
[14:55] actual sample there.
[14:59] Okay. So this could be this could be
[15:01] helpful.
[15:02] Uh let's see. LPK said could you expand
[15:04] a bit? Um oh wait there's a question on
[15:07] cluster. Does the cluster evaluation
[15:09] operate similar to theme analysis for
[15:12] conversational agents?
[15:15] Um,
[15:17] it's a good question. Uh, let's see.
[15:19] Filters, advanced filtering parameter
[15:23] past.
[15:25] So, the thing is I'm guessing that it's
[15:27] really focusing on the failures. Um, so
[15:31] that might be different than theme
[15:33] analysis, right? because theme analysis
[15:34] sounds like like it's just generally
[15:36] looking for different kinds of themes.
[15:38] Um but if you do past equal what if we
[15:41] say past equals true
[15:44] uh then we just get we get the actual
[15:48] Yeah, it's really it only looked at I I
[15:51] think that it's really focusing on the
[15:54] um
[15:57] on the failed samples because if we also
[16:00] look at all these suggestions, they're
[16:01] all for the failures. Uh so I think
[16:04] that's how it's different. It's like
[16:05] really trying to help you understand the
[16:07] failures and how you could improve.
[16:13] Okay. Uh so LPK says, "Could you expand
[16:16] a bit on any approaches you take for
[16:18] streaming and online eval together?"
[16:23] Good questions. Um
[16:26] so that's the thing. If you were
[16:27] streaming uh streaming an evaluation, if
[16:31] you're streaming a response,
[16:34] it's you can't really like you can't do
[16:36] an evaluation or at least I don't I
[16:39] don't have a clever way of doing an
[16:40] evaluation as something is streaming
[16:42] because
[16:44] I guess like in theory, could you pass a
[16:46] token token by token? I haven't set up
[16:49] something like that where you'd pass
[16:50] like token by token to another LLM for
[16:52] evaluation. Um, one thing you could do
[16:55] is that you could ask the LM to evaluate
[16:58] itself in its streamed response. You
[17:00] could say, "Hey, you're going to start
[17:01] off each stream with your confidence
[17:04] level, right?" And you could kind of
[17:06] like you could reax that out of the
[17:08] output. So, it's kind of like asking it
[17:10] to answer while doing its own evaluation
[17:14] at the same time. That would be one
[17:17] option. you know, it's usually not as
[17:20] effective when you're using the you
[17:22] know, when you're doing that in the same
[17:24] generation, but that does mean that um
[17:26] you could you could get it from the
[17:28] stream, right? So, you could either have
[17:29] it start it stream with its like
[17:31] confidence level or like end it stream
[17:32] with a confidence level and then you
[17:34] could like pull that out and and render
[17:36] that a particular way. Um as long as
[17:38] it's just always formatted a certain
[17:39] way. So, that would be kind of
[17:41] interesting. Um, and then maybe like if
[17:43] the confidence level was low, then that
[17:47] might be when you do like a second
[17:48] evaluation, right? Um, this gives me an
[17:51] excuse to to bring up the hacks toolkit
[17:54] from Microsoft. um which is this idea
[17:58] about human
[18:00] AI interaction and what sort of things
[18:03] you should do in your UI in order to
[18:07] uh make the system you know more human
[18:10] friendly and and also be be safer. Uh so
[18:13] I love looking at the examples
[18:16] here. Um
[18:20] uh so for example we have like uh I like
[18:24] the one where it's like okay make clear
[18:25] what the system can do. Um there's ones
[18:28] it's like there match the level of
[18:31] precision in UI with the system
[18:32] performance right so if you have a way
[18:35] of doing like
[18:37] confidence um then then that's like
[18:41] really nice to actually show it like oh
[18:43] here um detect blah uh I don't there's
[18:48] like all these examples
[18:50] that they try to show make clear how
[18:52] well the system can do
[18:54] um okay so this one from Gemini. Oh,
[19:00] nope. High demand. Okay. Um,
[19:03] highlighting confidence. Oh, there this
[19:05] is the one I was looking for. Okay.
[19:08] Uh, so this one is actually like
[19:10] highlighted. It's low confidence tokens.
[19:13] That's getting really fancy. But you can
[19:14] imagine like streaming the response and
[19:16] asking it to to include its confidence
[19:18] level and then you could show that in
[19:20] the stream response like in the UI with
[19:22] a particular thing. And then maybe if
[19:24] you know then you do like a second check
[19:27] um once you've seen that it's like on a
[19:31] certain threshold. And so there you're
[19:33] communicating to us like hey you know I
[19:34] got you the response but I'm not feeling
[19:36] that good about the response. This
[19:38] response probably needs a
[19:39] double-checking and you could put in the
[19:41] UI like you know u you know running
[19:43] iterative reflection or something like
[19:45] that. Um so the the user had more of an
[19:48] idea what going on because some of this
[19:49] is just you know this is like user
[19:51] experience like okay how do we convey to
[19:53] the user that this you know that this
[19:57] response is not perfect right um and
[19:59] that we need to do more work on it uh so
[20:01] if you're doing this kind of streaming
[20:03] experience you know you could be just
[20:05] you're giving progress updates you're
[20:07] saying all right I've done the search
[20:09] I'm generating the answer right that's
[20:10] the other thing if you want to do online
[20:12] eval like at least give progress updates
[20:13] like show the tools that are being call
[20:16] the search you're doing the that you got
[20:17] the results. Okay, now you're generating
[20:19] the candidate response. You're
[20:21] evaluating the candidate response. Like
[20:22] let the user know where you're at in the
[20:24] process so that they know something is
[20:26] happening, right? Because the worst
[20:27] thing is just watching a loading
[20:28] indicator for, you know, hours on end,
[20:31] not knowing that there's some progress
[20:33] happening. Um, so I think that's the
[20:34] other thing you can do is that if you
[20:35] are going to do online evals, just
[20:38] stream the updates like let the user
[20:40] know that's what's happening. Um, so
[20:43] that they can they can wait for it.
[20:46] So, those are my ideas there. Um,
[20:50] all right. So, Kalian said, "What is the
[20:53] recommended practice after the app is
[20:55] live? Should we schedule evals
[20:58] frequently?" Yeah. So, I think like our
[21:01] documentation defaults to daily for the
[21:06] scheduled evals. I changed mine to
[21:07] hourly just because it was easier to
[21:09] demo and debug. Um, uh, but you could do
[21:13] you could do evals. I mean it it just
[21:16] for scheduled evals,
[21:19] you know, it depends. Yeah, it just
[21:21] depends how often because with scheduled
[21:24] evals also you could do like a couple of
[21:25] them where you had like one of them that
[21:26] was just doing like because similar to
[21:29] like GitHub CI, right? So you could have
[21:30] a scheduled eval like maybe every day
[21:32] you test like 50 queries. Um but you
[21:35] could also just on an hourly basis just
[21:36] test like five queries, right? It's like
[21:38] a smoke test. It's just like is there
[21:41] anything like horribly, you know, has
[21:43] anything gone horribly wrong? Right. Um,
[21:46] so that like you you can kind of you
[21:48] should be able to do multiple schedules
[21:50] as long as I think they have different
[21:51] names. You can set up multiple
[21:52] schedules. So you can have, you know, a
[21:54] daily one that does a larger test, an
[21:56] hourly one that does a shorter test, a
[21:59] weekly one that does even larger, right?
[22:01] Uh because you wouldn't really be
[22:02] spending that much money. Like if you're
[22:04] only testing like five five questions
[22:06] once an hour, like that's nothing,
[22:08] right?
[22:10] Um so so yeah, I I I don't I don't know
[22:14] like generally like what people are
[22:16] doing in the industry. That's a good
[22:17] question. See if we have some data on
[22:19] that. Um but I would consider doing a
[22:20] mix of schedules with um you know
[22:24] different amounts um to give you
[22:27] confidence.
[22:30] Uh similarly you asked are there any
[22:32] benchmarks we can refer to to say an app
[22:34] is prod ready? I don't think so. I think
[22:37] it's it's I because here's the thing
[22:39] even if you get like let's say you get
[22:40] like a 100%. Even if I get a 100% on an
[22:44] evaluation,
[22:46] I don't necessarily think that my app is
[22:47] perfect because these are LM based apps
[22:50] and LM judges and like you know we don't
[22:55] you don't know um when um you know when
[22:58] when um what kind of things the users
[23:01] will send to them. So yeah, I don't I
[23:03] don't I don't I don't want to give you
[23:04] like an exact cut off. Um it's a good
[23:08] question. I I get quite like what people
[23:10] are doing in industry. How are they
[23:11] deciding that it is, you know, good
[23:15] enough? Like you don't want anything
[23:16] like egregious, anything like really
[23:18] really low quality, right? Um, and the
[23:21] other thing is like maybe it comes down
[23:23] to the UI, right? Like if you're
[23:24] messaging in the UI, like hey, this is
[23:26] a, you know, we're trying this out. This
[23:28] is all AI generated. Um, you know,
[23:30] please thumbs down or give us feedback
[23:32] if something's, you know, not doing
[23:34] well, right? So I I think that's
[23:36] probably what more people are doing is
[23:37] like, all right, we're going to put it
[23:38] out there.
[23:40] uh we because we've done you know we've
[23:42] done our best effort like I think um
[23:44] internally I think people often will
[23:46] like run like a thousand eval like
[23:48] evaluations on like a maybe a data set
[23:50] of like a thousand questions and then
[23:52] look at the results of that um and I
[23:54] don't know what cutoff they use for that
[23:56] um but you do want to evaluate a fair
[23:58] number of um you know questions
[24:03] uh before you do your first deploy of a
[24:05] system right I was saying like minimum
[24:06] 200 but I think internally we usually do
[24:08] like between 800 and a thousand
[24:10] But I don't know what percentages we
[24:12] use. It's a good question.
[24:15] Uh
[24:17] yeah, I saw this question in the chat
[24:18] too from Pablo. Could we directly feed
[24:22] images and audios to the agent in
[24:24] foundry safety evaluation? So the whole
[24:27] question about multimodal evaluations.
[24:31] Um
[24:33] this is trickier. I
[24:36] feel like it's not supported yet.
[24:41] Um,
[24:44] you might I wonder if you'd be able to
[24:45] do a custom evaluator.
[24:51] Um, I don't I don't think there's
[24:53] because you asked also about safety
[24:58] because you need it needs to be a
[24:59] different model for it um generally. So
[25:03] I
[25:04] I don't know if we've added it
[25:07] externally yet. Um
[25:11] hiring blah blah blah
[25:14] asky art.
[25:17] Um let's see image
[25:20] imagery. Nope.
[25:23] Multimodal.
[25:24] Yeah, I don't think we have anything
[25:27] live for this. Um because it because you
[25:31] would need an an multi you'd need a
[25:33] multimodal you need an image model and
[25:36] an audio model and they
[25:40] um they would have to have their guard
[25:42] rails off in order to be able to look at
[25:44] it and decide whether it was safe or
[25:46] unsafe. Um and we might we we may very
[25:50] well have that model, but I don't think
[25:53] we I don't think it's available yet. Um
[25:56] it's just a little bit harder to set up.
[25:59] Uh so I'll ask the team about it. Um I I
[26:03] yeah I don't see anything publicly
[26:06] documented.
[26:09] Uh
[26:12] oh so y says you almost never get the
[26:16] analyze results to show results. Your
[26:18] val may read 100% and analyze results
[26:20] show zero. Wait, so are you using are
[26:22] you talking about this one? Oh, so
[26:23] you're already using analyze results. I
[26:25] only noticed this yesterday. I was
[26:26] excited about it. Um, interesting. Uh,
[26:32] so it's so are you are you saying you're
[26:34] using this one and not getting results?
[26:37] Fascinating. Um
[26:40] yeah, I don't that just might be a bug
[26:42] with the system. If you have any like if
[26:44] you have like explicit like let's see
[26:46] was there like an ID for this cluster
[26:49] analysis evaluation run analyze insight
[26:53] um you know so if it looks like a bug
[26:55] then uh may be able to report it to the
[26:59] team with enough information
[27:01] about it. It looks like there's like a
[27:03] lot of information in the URL there. um
[27:07] or it could just be the way it's
[27:09] working. But if you can provide more
[27:10] information, um then we might be able to
[27:13] ask the team for more information about
[27:15] it and see whether it's just the way
[27:19] it's working or if we're like not using
[27:20] it the right way. Uh I I'm surprised
[27:24] you're already using I didn't know we
[27:25] even had this. Maybe we've had this for
[27:27] a while. Oh, and download that looks
[27:28] fun, too.
[27:30] Um yeah, so it might be that there's
[27:33] just a like some issues with it.
[27:37] So Pablo says, "Would the interaction
[27:39] between agents need to be evaluated
[27:42] differently?" Um, I'm going to say like
[27:44] like once again, this isn't going to
[27:45] depend on how you set up your your agent
[27:50] ar your multi- aent architecture, right?
[27:52] So if you're doing um a supervisor agent
[27:57] that's using the agents as tools, then
[28:00] your agents are tools and then you can
[28:01] kind of treat them that way in
[28:04] evaluations. But if you have a more
[28:06] flexible architecture, then I feel like
[28:08] you're going to probably write like a
[28:10] custom evaluator that basically looks at
[28:12] agentto agent interaction and says like,
[28:14] hey, did my uh you know, did my mains,
[28:17] you know, you know, did the agents call
[28:19] each other at the right time, right? And
[28:22] you'll you kind of give criterias for
[28:24] it, you know, um if you're doing like a
[28:26] customer support agent like like okay
[28:28] the triage agent should you know
[28:31] evaluate whether the triage agent
[28:33] successfully passed over to the refund
[28:34] agent in the right scenarios, right? Um
[28:37] so you you could imagine having like a
[28:39] custom evaluator that was like an agent
[28:42] uh handoff evaluator that was checking
[28:46] to see like how they're going back and
[28:49] forth. That would be interesting. But I
[28:51] would only do that if that's like if if
[28:53] that's like the issue you're seeing. And
[28:54] I have actually to fair when we did do
[28:56] those multi- aent um demos that I
[28:58] definitely saw that when you have a high
[29:00] degree of flexibility in a multi- aent
[29:03] architecture like when we were using the
[29:04] handoff orchestration in an agent
[29:06] framework like sometimes those handoffs
[29:09] were like wild like not they were like
[29:12] out of control like um not what I
[29:15] expected right so um I could see it
[29:18] being worthwhile to to build like a a
[29:21] handoff evaluator uh I'll also check
[29:23] with the team to for specifically
[29:25] building things for multi-agent because
[29:26] I feel like this might be a common
[29:28] request and so maybe there'll be some
[29:30] built-in evaluators for multi- aent in
[29:32] the future. Um, but I think we'd have to
[29:35] see whether we have a generic enough way
[29:38] of because because people are building
[29:40] their multi- aent systems in different
[29:43] using different architectures. uh it
[29:46] might be hard to do a built-in evaluator
[29:48] because we don't know, you know, how
[29:50] those agents are set up.
[29:54] Okay, so Yadell
[29:56] posted total sample 0000.
[30:05] Oh, okay. Um well, if you can
[30:10] DM me. Uh oh, I just accepted your Let
[30:13] me accept your friend request. Okay, I
[30:15] just accepted your friend request. So if
[30:18] you DM me the um the URL, then I can ask
[30:22] the eval team about it. So just find So
[30:25] I think the URL has everything that they
[30:28] would need for it. It's a very long URL
[30:33] and I can show them the screenshots,
[30:34] too.
[30:38] Um, so Cen said, "If an answer is highly
[30:41] relevant but has a low groundness score,
[30:43] how should
[30:46] uh a developer just their retrieval
[30:48] strategy?" So the user ask question, LM
[30:50] responds with the answer relevant to the
[30:52] question, but the information is not in
[30:55] the actual document.
[30:58] Um, yeah, that's a good question. And so
[31:01] here I think it depends on what like so
[31:04] if you're equipping your application
[31:06] with web search then I feel like it
[31:09] becomes harder to measure like when
[31:11] you're round when you're measuring
[31:12] groundedness then the groundness
[31:15] it's harder to measure especially if
[31:17] you're using Bing web search because you
[31:19] don't actually get back the snippets
[31:21] when you're doing Bing web search you
[31:22] just get back like the actual answer.
[31:24] So, in fact, I tried doing the
[31:26] groundedness evaluator um this morning,
[31:28] but because I was using web search, it
[31:30] actually failed because the groundedness
[31:32] evaluator that we have um specifically
[31:36] doesn't work with web search enabled. Um
[31:42] uh let's see. And then groundedness
[31:44] where um yeah, so this I tried doing the
[31:47] roundedness ones, but I actually got it
[31:49] like an um an error. there's like, oh,
[31:52] it can't do this with with web search,
[31:54] and that's because it it can't get back
[31:56] the um this the snippets for it. Um,
[32:02] so yeah, so there's so there's that
[32:04] issue, um, which is how are if if you're
[32:06] using Bing web search, how do you even
[32:07] know what the results are? Because Bing
[32:09] web search that tool doesn't give you
[32:10] back the snippets. Um, but I think that
[32:12] so the other issue is
[32:15] um, you know, the information's
[32:17] not in the document. So that's why, you
[32:20] know, we um I think that was the the one
[32:23] I really liked was that um tool output
[32:26] utilization. Where was the tool output?
[32:30] Uh tool output utilization.
[32:33] Yeah. So see that groundness got 100%
[32:34] but tool output utilization got 50%. I
[32:38] think this is like a better version of
[32:40] groundedness because this really caught
[32:44] a lot of the groundedness issues, right?
[32:46] like where it was like, oh, it
[32:48] fabricated. Um, so I think you just I
[32:51] like I, you know, I think this is just a
[32:53] kind of to me this is like a better
[32:54] version of of groundedness where it just
[32:58] was really trying to specifically look
[32:59] and see um whether it was matching
[33:03] exactly like what was in those results.
[33:08] Um,
[33:11] so but if the information Yeah. So I'm
[33:13] not sure if you're asking for retrieval
[33:15] strategy. So sometimes your retrieval
[33:17] strategy is that you're retrieving
[33:18] you're not retrieving enough and
[33:20] sometimes your retrieval strategy is
[33:22] that you're retrieving too much. Um if
[33:25] you're not retrieving enough then you
[33:26] you can you know increase the number of
[33:29] results or change your um search score
[33:32] threshold. U but I don't know if I'm
[33:33] following exactly
[33:36] what the failure situation is that
[33:37] you're describing.
[33:40] Uh let's see but you maybe share share
[33:44] some more information. So Pablo says
[33:47] Azure you mentioned that Azure AI search
[33:50] retrieval is better than work IQ. Um
[33:52] this depends on the data in work IQ. Um
[33:55] it might make sense to evaluate work IQ
[33:57] retrieval. How can we do that and even
[33:59] detect how to improve it? Um yeah it's a
[34:02] good question. So with work IQ do I have
[34:05] work IQ ask working right now? Um right.
[34:10] So let's say you're you're asking um
[34:14] find me my presentations about quality
[34:19] and safety.
[34:23] So work IQ is itself um oh I have to do
[34:26] work IQ- ask-q. Okay. Um work IQ is an
[34:31] is an agent that wraps different
[34:34] retrieval mechanisms and that's what's
[34:36] tricky. Oh I don't know if it's going to
[34:37] let me find out. Uh, no. Dang it. Okay,
[34:42] so it's not going to work because of my
[34:45] login issues, but um, work IQ is an
[34:48] agent that wraps retrieval strategies
[34:51] behind it. Um, so if you wanted to
[34:53] evaluate it, then you know, you could
[34:55] versus Azure AI search. Um, then I would
[34:58] say you you know you you do a bunch of
[35:00] queries, figure out what queries you'd
[35:01] be sending to to work IQ, like maybe
[35:04] it's something like this and do the same
[35:07] queries in in AI search. Um, and then
[35:11] you can you can see, but then you have
[35:13] to have AI search presumably then you're
[35:16] either using AI search with the remote
[35:21] uh are using it with the index
[35:22] shareepoint then like what do are you
[35:24] trying to compare it on the same data
[35:25] because then you have to set up your AI
[35:26] search to be pointing at SharePoint and
[35:28] there you're either pointing at the um
[35:33] an index SharePoint or at a remote
[35:36] SharePoint but if you're pointing at a
[35:37] remote SharePoint then I think that's
[35:38] basically work IQ at this point. Um, so
[35:41] maybe you're comparing work IQ retrieval
[35:44] versus Azure AI search with an index
[35:46] shareepoint. Is that maybe what you're
[35:48] comparing? And in that case, you could
[35:49] you could do different queries comparing
[35:51] them. Um, but you know, it's going to
[35:53] depend on what your users are asking
[35:55] because for some things like maybe the
[35:57] work IQ does actually do a decent job.
[35:59] Um, the thing is that it wraps so many
[36:02] different kinds of documents because
[36:03] work IQ it's searching your SharePoint,
[36:05] searching your emails, it's searching
[36:06] your chats and um, you know, I think it
[36:10] actually probably does do it for me it
[36:12] does a good job on my SharePoint but not
[36:15] a good job on my chats.
[36:21] Um, oh yeah, sorry. And the evaluators
[36:23] page that we were looking at was well,
[36:27] we were looking at a lot of them, but
[36:28] they're all it's all pretty much linked
[36:30] off of um linked away linked from this
[36:34] area here.
[36:37] Um okay, so following up on Okay, some
[36:40] some follow-up questions on the the work
[36:43] IQ question. I see.
[36:48] Um,
[36:50] so
[36:52] okay. So, Foundry IQ,
[36:55] Foundry IQ is as your AI search. Um, it
[36:58] is a another name for it because PE some
[37:03] people wanted another name for it and
[37:07] I'm annoyed at the team because it's so
[37:09] confusing. Um but Foundry IQ is AI
[37:13] search um using the new agentic
[37:15] knowledgebased feature and when you're
[37:18] using in Foundry you're generally using
[37:20] it with the the MCP endpoint for that
[37:23] agentic knowledgebased feature. Um but
[37:26] Foundry IQ is just another way of
[37:28] talking about the AI search agentic
[37:30] knowledgebased feature. Uh that was I
[37:33] guess that's how I would
[37:36] describe it. Um they're still trying to
[37:38] decide what the final name is for all
[37:40] these things. So it's like yesterday
[37:42] they were like, "Oh, should we be
[37:43] foundry IQ search?" I don't know. Just
[37:45] pick a name. Just pick a name and stick
[37:46] with it. It's so I'm sorry. I'm so
[37:49] annoyed at different names because it's
[37:51] so hard for us as developers. Like okay,
[37:53] what is this thing? You just renamed it.
[37:55] So here you can see it's called Foundry
[37:57] Azure Search. Um but this agentic
[37:59] retrieval here uh this is this the you
[38:02] know what we're what we uh this MS
[38:04] endpoint that's what we use when we are
[38:07] using foundry IQ
[38:10] um so yeah so the agentic knowledge base
[38:14] can wrap uh on top of a bunch of sources
[38:17] some of those sources are search index
[38:19] you could have an index shareepoint in
[38:21] there some of them are remote sources
[38:23] like remote shareepoint and I believe
[38:25] that currently basically uses the same
[38:27] retrieval does work IQ. So I think that
[38:29] would be similar results. Um so that's
[38:34] what we're talking about when we're
[38:35] talking about you know um AI search and
[38:38] searching.
[38:40] Um
[38:45] yeah. So let me and let me just bring up
[38:47] a slide that makes it clearer than than
[38:50] that. Um
[39:01] boundary
[39:04] maybe this one. Yeah, this was our
[39:07] ignite talk.
[39:10] Um, okay, here we go. Right. Uh so yeah
[39:15] this is the
[39:17] agentic retrieval which can
[39:21] you know do parallel execution of your
[39:26] um search queries to all the different
[39:27] knowledge sources um which could be
[39:30] search index or shareepoint and so yeah
[39:32] so for shareepoint we either can do
[39:34] remote shareepoint knowledge and that's
[39:36] using
[39:38] um a similar retrieval mechanism as work
[39:40] IQ I'm don't know exactly right now
[39:43] which mechanism it's using. It might be
[39:45] slightly different. Um, but it's not
[39:46] using AI searches search engine is the
[39:49] point. It is using an API that's
[39:52] maintained by like the M365 team. The
[39:56] other option for SharePoint is index
[39:58] SharePoint knowledge where you just
[40:00] point an indexer at a SharePoint
[40:02] document library. You run your ingestion
[40:04] on it and then it just becomes, you
[40:06] know, chunks in your search index,
[40:09] right? Um,
[40:11] and that way you get to use the Azure AI
[40:15] search like state-of-the-art retrieval
[40:17] with the hybrid search and semantic
[40:20] ranking. All of that would um be used
[40:23] when searching that. So those are your
[40:24] two options for SharePoint
[40:27] uh inside Azure AI search also known as
[40:31] Foundry IQ. Um,
[40:34] but you could also use work IQ
[40:36] separately. now uh in in in theory and
[40:39] and so that you might want to also
[40:41] compare that.
[40:46] Yeah, I don't I I cannot promise what
[40:49] the names of products will be by by
[40:52] build, you know, because sometimes
[40:54] products get named like the night
[40:56] before. Uh I learned about one of those
[40:59] this morning. So, you know, if it was up
[41:02] to me, we would just never rename
[41:04] products because I find it really
[41:07] annoying to have to change my brain and
[41:10] all my code and my environment variables
[41:13] and all that stuff. Um, but uh, you
[41:16] know, there are people in the executive
[41:18] world that really enjoy naming products
[41:21] and we want them to be happy too, don't
[41:23] we?
[41:27] Okay, I think there was another
[41:29] question. Let me see. There's a lot of
[41:31] people typing now. Um, so there was a
[41:33] question about eval with CI/CD
[41:35] integration. That's a good question
[41:37] because I haven't done that with Foundry
[41:39] yet. Um, but I think that they said,
[41:42] let's see if there's something
[41:44] if we There we go. CI/CD evaluations.
[41:47] Okay. Yeah. So, this is something that's
[41:50] built in. So, we should figure that out.
[41:53] Um, I'm pretty new to the this new kind
[41:56] of ebouse. Um for a long time I was a
[41:58] long time I was using that old SDK which
[42:00] does things differently. So I have set
[42:03] up CI/CD with the like the old way of
[42:07] doing eval but not with the new one. And
[42:09] I think it's supposed to be easier now
[42:11] where you could just kind of set some
[42:13] stuff in the YAML, right? Um okay. So
[42:16] you have like your sample data file. We
[42:18] already have that. Oh, but here you also
[42:19] specify the evaluators. Okay. Um
[42:24] and there's some examples. Okay. AI
[42:27] evaluation workflow.
[42:30] do not run evaluation on every commit. I
[42:32] agree. Um, what you could do is a
[42:34] comment. So, I'll show you the one that
[42:36] I do have that's a very custom workflow,
[42:39] which is probably too much effort now.
[42:40] Like, I need to redo everything now that
[42:42] we have easier ways of doing eval. But,
[42:44] I'll show you the the trigger anyway
[42:46] because I think that's interesting
[42:48] because you don't want to run it on
[42:49] every commit. So, for this one, I only
[42:53] run it if you say slashevaluate.
[42:57] And you also have to be owner,
[42:59] contributor, collaborator, member of the
[43:02] of the repo because I don't also just
[43:05] don't want people willywilly pressing
[43:06] evaluate. Um, so this is one way of
[43:09] doing it, right? Because you don't want
[43:10] to run it on every commit. Um, or you
[43:12] could like try and like use an LM to
[43:14] decide like to actually like you know
[43:17] look at a PR and say hey is this a PR
[43:20] where you think we should be doing
[43:21] evaluation. That would be an interesting
[43:22] thing too because now it's we have this
[43:24] like aentic devops. Now it's easier to
[43:26] bring LMS into your workflows. Um that
[43:30] would be another option to think about
[43:31] because yeah, you need to think about
[43:32] the trigger because you do not want to
[43:34] run evaluation on every commit for sure.
[43:38] Uh so then what can we do? Okay, we got
[43:40] to log in and then we run the
[43:42] evaluation. Boom. Nice. H
[43:47] I want to do this. Okay, this is so much
[43:50] easier. I had to like run my I had to
[43:52] write a lot of custom code
[43:55] to do all this because this is with also
[43:56] a custom application, right? So I don't
[43:58] have like a deployed agent, but if you
[43:59] have a deployed agent presumably, yeah,
[44:02] agent ids um we should double check that
[44:06] this works with Foundry hosted agents.
[44:08] That's a good question. I can ask the
[44:10] product team afterwards um
[44:14] whether this works for hosted agents
[44:16] yet. This this was probably built with
[44:18] prompt agents originally. So, some of
[44:20] the things when you see agent IDs,
[44:21] they're referring to prompt agents and
[44:22] they may not work with hosted agents
[44:24] yet. So, we do need to double check
[44:26] that. Um, but I'll I'll look through my
[44:30] um my notes afterwards and and ask. Uh,
[44:34] so then you can see the output. This is
[44:37] nice. This is real nice. Cool. Cool.
[44:41] Well, I'm excited.
[44:43] Uh so as long as I I just have to double
[44:46] check whether this is um this can
[44:48] support hosted. Um but if it can then
[44:50] that's really great.
[44:53] Let's see. Um so the question was
[44:58] uh
[45:06] uh let's see. Okay.
[45:10] Works better.
[45:14] All right. Many of the great Foundry
[45:16] features are in preview. Any roadmap for
[45:18] GA?
[45:20] Uh, that's a good question. Um,
[45:26] well, like hopefully everything
[45:28] eventually goes GA. Um, I don't know if
[45:30] I know. Also, if I didn't know the
[45:32] timeline off hand, I probably wouldn't.
[45:34] Sometimes we can say like with agent
[45:36] framework, we kind of knew when it was
[45:37] going GA and we were talking about that.
[45:40] Uh I don't I don't know offhand when
[45:43] these things are going GA. Um obviously
[45:46] build is a is a potential time when
[45:49] things go GA because people love to
[45:51] announce things then. Um but you know
[45:54] that's only a month from now at this
[45:55] point and
[45:57] I I guess I personally would want it to
[45:59] have a like for hosted agents I would
[46:01] want it to have a longer baking period
[46:02] because it is a a tricky feature um to
[46:06] to get right. So yeah I don't I don't
[46:08] know. I mean generally we're always
[46:09] aiming for thing for things to go GA.
[46:11] There is a lot of interest in
[46:14] um in a lot of these a lot of these
[46:16] features and in hosted agents. So I feel
[46:19] like they're on a good path for it but
[46:21] who knows like um yeah I think we have
[46:23] to get more product feedback and see. Uh
[46:26] so I don't know. I I'm kind of just
[46:28] speculating here. So I I do not actually
[46:30] know. Um obviously check at build to see
[46:33] if anything goes GA then. Um,
[46:36] and uh, yeah, we'll just we'll just hope
[46:39] I'll I'll look out for it as well.
[46:51] It would so Pablo says it would be good
[46:53] if Microsoft could offer a pay for
[46:55] execution service to evaluate retrieval
[46:57] quality from work IQ for specific user
[46:59] teams section. Um, oh, make an analysis
[47:03] to recommend changes. They decide rules
[47:05] that can be changed to affect
[47:06] retrievable performance.
[47:09] Um, yeah, that's good. That's good
[47:12] feedback. Um,
[47:14] well, we're also like, uh, so for build,
[47:17] let me find the lab that we're doing for
[47:20] build because we're going to try to use
[47:23] work IQ in our foundry IQ lab because
[47:26] we're just trying to use all the IQs we
[47:28] can. Um,
[47:31] let's see.
[47:33] Should be only one Pamela. Good.
[47:36] All right.
[47:38] Um,
[47:41] okay. So, here we only mentioned Foundry
[47:43] IQ. Uh, but we are for this lab, I'll
[47:48] let you know, we are trying to use as
[47:50] many IQs as possible. So, we're going to
[47:51] try to use Fabric IQ and work IQ. Um, so
[47:56] that's that's the other option is that
[47:59] Boundary IQ could um, you know, could
[48:02] pass through to work IQ. I do think
[48:04] there's some latency issues there
[48:06] because now we've got LMS on top of LMS.
[48:09] Um, because work IQ is saying work IQ is
[48:12] currently implemented as like an LLM on
[48:14] top of retrieval services. So if you're
[48:17] doing, you know, the more models you add
[48:19] into a retrieval pipeline, the slower
[48:21] it's going to go. Um, so I think that's
[48:25] that's the kind of a bit bit of an
[48:28] issue, right? Like do you want good
[48:30] retrieval or do you want good and like
[48:33] getting both good and fast retrieval
[48:36] across all of these enterprise knowledge
[48:39] sources that is going to be hard. Um but
[48:42] yeah, so I I know like in terms of work
[48:45] IQ, one option would be to use it from
[48:47] Foundry IQ because then you you would
[48:49] get some of the the you know AI search
[48:52] retrieval technology layered on top of
[48:54] it. Um like like maybe semantic ranking
[48:57] or um the new semantic classification
[48:59] model.
[49:11] All right. Uh Kayen said, "Any
[49:14] hackathons planned in the near
[49:17] future?" Um
[49:20] I don't we don't have any uh yeah, no
[49:23] virtual ones planned. I kind of we had
[49:25] the agents league one recently and the
[49:28] JS Buildathon. Those were the two most
[49:30] recent ones that my colleagues did. I'm
[49:32] not doing hackathons as much anymore
[49:33] because the judging process was just I
[49:36] don't know. It was it was hard.
[49:39] I ended up doing a lot of the judging
[49:41] myself. Um, I read through a lot of
[49:44] people's code repos and I haven't even
[49:45] like now that we're in the age of coding
[49:47] agents like like I would assume the
[49:50] submissions are like huge and like
[49:52] looking through the code for them would
[49:53] that that'd be even more overwhelming.
[49:55] So, um, I haven't done one recently
[49:57] because the judging is just so hard. I
[50:00] do love like I love seeing what people
[50:02] make. It's so fun to see what people
[50:03] make. Like I like I like showand tells.
[50:06] I love seeing what people make and just
[50:08] being impressed by all the different
[50:10] ideas people have. I just don't like the
[50:12] competition aspect and the judging
[50:14] aspect. So, I personally have not
[50:16] attempted to organize any hackathons. Um
[50:20] uh so we'll see if my colleagues have
[50:21] any planned. Uh we don't have any
[50:23] planned on our team. We we're doing
[50:25] we've been doing the live stream series
[50:26] more because they're they're um more
[50:30] sustainable for us to put on um where we
[50:33] don't have to worry about the judging
[50:36] aspect and prizes and all that stuff. Um
[50:39] so, you know, we'll probably do more
[50:42] live stream series in the future. People
[50:44] seem to like them. Like we might do
[50:47] like, you know, redeliver some of our
[50:50] old series but updated. Um, but if you
[50:52] have other ideas for what like, you
[50:54] know, future live stream series that you
[50:57] want to see, uh, let us know. This one
[50:59] was probably our more most advanced
[51:01] series. Uh, so we we had less watchers
[51:04] for this series, but everybody seems
[51:06] pretty engaged who is watching, which is
[51:08] good. Um, so this one, you know, because
[51:11] this is about, you know, how to deploy
[51:13] like so this is moving into more
[51:15] production stuff. Uh, so that's a
[51:17] smaller audience, but uh, looks like a
[51:20] good audience. So that's cool. Uh but
[51:22] yeah, these are generally the events
[51:23] that are coming up on my end. Uh build
[51:27] will have a hackathon in person. Um but
[51:29] yeah, I don't know about virtual ones.
[51:31] Uh let's see.
[51:35] Uh oh, you got an award in the
[51:36] buildathon. Okay, cool. Great. Yeah, I
[51:40] think Julia organized that one. So my
[51:42] colleagues, I still have colleagues that
[51:44] are excited about putting on hackathons.
[51:46] Um
[51:47] so maybe we'll have some in the future.
[51:52] As long as as somebody else does the
[51:54] judging that is not me.
[51:58] Uh
[52:01] yeah. Um
[52:04] so Yadell, you ran into content safety
[52:06] filter. Usually if you're when you're if
[52:09] you're do if you're giving unsafe input,
[52:11] you should give this get this content
[52:13] safety filter result. Um or here I'll
[52:15] I'll link to the more uh safety safety.
[52:19] Okay. Um the more basic demo with like
[52:22] the openi SDK
[52:25] um
[52:26] content filter. Okay. Right. Um so here
[52:30] with the openi SDK where we see like oh
[52:33] the error code is content filter. Right.
[52:36] Um, so at least from the API, if if it's
[52:40] a content filter error, it should get it
[52:44] should get sent as an actual error um
[52:47] using the JSON
[52:51] uh I showed here and then like different
[52:53] SDKs will you know turn that into
[52:57] different sorts of error types. So, in
[52:59] the OpenAI SDK, we, you know, it's like
[53:01] this in the agent framework SDK. Um,
[53:05] this is how I did it. Uh, but yeah, if
[53:07] you don't, if you don't have handling
[53:09] yet in your agents or your LLM code for
[53:14] content safety filter errors, I do
[53:17] recommend adding handling because your
[53:20] users are going to run into it. Um, uh,
[53:23] I I run into it all the time when I'm
[53:25] using the like GPD models.
[53:28] especially when I ask medical questions.
[53:30] That's what I run into the most. So, you
[53:32] you want to have some sort of handling
[53:33] like just decide what you want to do.
[53:38] Uh oh, we can use an LM as a judge.
[53:40] Yeah, I suppose we can use an LM as a
[53:42] judge now for hackathons, can't we?
[53:44] Yeah.
[53:46] Yeah, that's probably what we're doing
[53:47] now. I is Yeah. Yeah.
[53:52] I would just I wanted to be a really
[53:54] well-c calibrated judge that actually
[53:56] like looks at the code.
[53:59] Um because last time I had like some of
[54:01] the judges like only looked at the
[54:02] readme and then I like looked in the
[54:03] code and I was like no this code doesn't
[54:06] do what the readme says, right? But
[54:08] yeah, now you're right like the judges
[54:10] like the LMS could actually look through
[54:11] the code. So I I think um yeah certainly
[54:15] if we were doing like a lot of
[54:16] hackathons or like a big hackathon, it
[54:19] would definitely be worth it to really
[54:21] calibrate an LLM as a judge and and give
[54:23] it all the criteria that I use. So
[54:25] you're right. Um
[54:27] uh the last time I did a hackathon, our
[54:30] LLMs weren't as good, but yeah,
[54:31] currently you're right. We would just do
[54:33] an LM as a judge and we would just have
[54:35] to calibrate it really well.
[54:39] Um let's see. So Pablo And so you want
[54:43] an agent that could analyze your agent,
[54:46] interact, use, assess, and create
[54:48] evaluations. Oh yeah, actually this
[54:50] reminds me of something I didn't show.
[54:52] Um, but that is kind of similar. There
[54:55] is this skill
[54:58] um that tries to help you make
[55:00] evaluations. Like when I looked at it,
[55:02] it felt like it was specific to people
[55:03] using the Foundry toolkit extension. Um,
[55:07] there's also, by the way, in App
[55:09] Insights, there's something called the
[55:10] observability agent. So there is at
[55:11] build Nicha is working on
[55:15] um
[55:18] uh uh let's see Nicha is doing this this
[55:22] one observe optimize and protect. So
[55:23] she's doing this lab um where
[55:28] they're going to be like using skills
[55:31] and agents and stuff like that to help
[55:33] build better evaluations.
[55:35] Um, so, uh, and she pointed me to the
[55:38] this this skill here. So, I looked at it
[55:42] and I didn't end up using it for mine
[55:44] because I felt like it was like more
[55:45] specific to people using the foundry
[55:47] toolkit. Um, but I feel like this is
[55:51] kind of along the idea of what you were
[55:52] thinking. Also related to Haml that Haml
[55:55] Hussein, he's got um these uh skills,
[55:59] EBA skills. Yeah. Uh, these are like
[56:02] really generic. It would be interesting
[56:03] to to try them on
[56:07] um you know on a like on the repo I just
[56:10] made and see what it says like um it's
[56:13] even fun just but the skills are great
[56:15] like there's one um eval audit right and
[56:19] uh you can see here it checks to see
[56:21] stuff like this our evaluator was binary
[56:24] pass fail right because it's saying like
[56:27] he he hates one to five so he says like
[56:31] okay you got to make sure they're binary
[56:33] So that's something like if I ran this
[56:34] skill um on the repo, it would, you
[56:37] know, maybe criticize any of the ones uh
[56:40] that were one to five. Um now it's a
[56:42] little tricky because we're using the
[56:43] built-in evaluators here. So it would
[56:45] have to go and look. But oh yeah, are
[56:46] similar metrics uses primary evaluation.
[56:49] These metrics. Yeah. Yeah. So this is I
[56:52] love looking through his skills because
[56:54] even if you don't use it as a skill,
[56:56] like it still gives you a good idea for
[56:58] best practices in industry. Um, so yeah,
[57:01] I think it'd be good to have a maybe try
[57:05] this out and maybe have it more more
[57:07] foundry specific. So yeah, we've got
[57:09] some skills. Um, it's, you know, the
[57:11] hard thing with skills like will it
[57:13] apply to your setup, right? Will it work
[57:17] with your setup? Does it understand
[57:19] enough? Um, there is a bunch of skills
[57:22] here. Eval data sets. So was that the
[57:23] one we were just in? Observe. So this
[57:26] one's observe. There's also eval data
[57:29] sets. Interesting.
[57:31] Um,
[57:33] when to use this skill.
[57:37] Okay. Yeah. So, check out there's even
[57:39] more skills here
[57:43] than that one. Create
[57:47] new hosted. Oh, that's creating a hosted
[57:49] agent. Interesting. All right. Oh,
[57:52] Sylvester has interesting paper. And now
[57:53] we are over time now. But, uh, let's
[57:55] see.
[57:57] Extern unified view of memory skills
[57:59] protocol. Where are they from? Okay.
[58:02] All right. I haven't seen this one
[58:03] again. Uh before. Sorry.
[58:10] Nice. Yeah, externalization, right? How
[58:12] do you externalize stuff? Um some people
[58:15] use the file system like Langchain deep
[58:17] agents uses the file system as kind of
[58:20] this external storage system when it's
[58:23] doing research.
[58:25] All right. Okay. Thank you everyone. We
[58:28] are at or over time now. Uh these are
[58:31] all great questions. So I will um I will
[58:35] upload the office hour recording and all
[58:38] the questions to the resources thread
[58:42] later. Um and for anything where we
[58:45] didn't have a question, I will ask the
[58:48] friendly product team. So sometimes I'll
[58:51] like update the answers. So you should
[58:53] also check like for yesterday I did get
[58:55] some better I think this was Pablo's
[58:57] question about POS cosmos DB uh so I did
[59:00] update this question here because um I
[59:03] got some updates on there there's this
[59:05] new like checkpointer so if you're doing
[59:07] lang graph flows you can use the
[59:08] checkpointer so sometimes I I try to um
[59:12] update the questions afterwards after I
[59:14] talk to the product team.
[59:17] All right. Thank you everyone.
[59:20] Um, I'll see you when I see you. Oh,
[59:25] next Tuesday we have our weekly office
[59:28] hours. So, uh, come to the Python and I
[59:31] weekly office hours and I'll be here in
[59:33] the foundry. All right. Bye, everyone.
