[00:00] Welcome to our weekly office hours for
[00:03] Python AI. And uh in this office hours,
[00:07] you can ask any questions or post any
[00:10] cool news in the chat. Uh just just put
[00:12] it in the Discord chat and I'll be
[00:15] checking the chat throughout and uh
[00:18] yeah, we can talk about whatever is on
[00:21] people's mind. I also have you know
[00:24] gathered together the things that I
[00:26] found interesting in the last week and
[00:27] the things I'm working on and we can
[00:29] also talk about those.
[00:31] Uh so just starting we already have some
[00:34] questions in the stat chat. Um so where
[00:36] could you start uh learning? Um
[00:42] so you know usually it really depends on
[00:45] the way in which you learn but this is
[00:46] my you know blog post about how I
[00:50] learned generator but at the bottom of
[00:52] that um we have links to the past series
[00:58] we've done about
[01:00] um Python AI.
[01:03] Uh oh I need to share my other screen.
[01:05] All right. So, let's do Looks like it's
[01:08] sharing the wrong screen. Let's try this
[01:11] one. Here we go. Yeah, this computer has
[01:15] everything reversed. Okay.
[01:17] All right. Um
[01:21] yeah, so that's the that's the um you
[01:25] know, video series that we'd recommend
[01:27] for getting started uh that we've put
[01:29] out. But um but you can also just look
[01:32] through here to see how I personally
[01:34] have learned generative AI. There's lots
[01:36] of different approaches. Um you know,
[01:38] most important thing is to actually try
[01:40] it, you know, um actually get hands-on
[01:43] with stuff because that's the way you
[01:45] really learn is to try stuff out.
[01:48] Uh so Ramsay says, "You need to use
[01:51] Foundry. Do I have links for free as
[01:53] your credit credits?" Um, I don't like
[01:57] just like I don't just have like coupons
[01:59] if that's what you're asking for. Um,
[02:02] they they haven't given me those to give
[02:04] out. Uh, what we have is there's the
[02:07] Azure free trial, but I don't think the
[02:09] Azure free trial works for Foundry. So,
[02:11] as far as I know, we don't have any
[02:14] mechanism. Let's see.
[02:17] Oh, does Foundry have a free level now?
[02:20] It might actually have a Let's see.
[02:23] Okay. It's free to use and explore, but
[02:26] then as soon as you want to actually I
[02:28] don't even know what that means, use and
[02:29] explore.
[02:31] Maybe that means you can like poke
[02:32] around it, look at the leaderboard and
[02:34] stuff, but then as soon as you're going
[02:35] to start, you know, using models and
[02:37] whatnot, because I think you said you
[02:39] wanted uh Oh, I don't know what you want
[02:40] on Foundry, but um you know, so like
[02:44] models models don't usually have a free
[02:47] tier. Uh oh my gosh, so many levels of
[02:50] indirection just to get to the pricing.
[02:55] But generally we don't have free tiers
[02:58] uh for models. So yeah, so there's no
[03:03] there's no free tier there. So I think
[03:05] this is actually a little
[03:08] um misleading here. I'm just going to
[03:11] screenshot this
[03:13] um because
[03:15] yeah, I mean you can so I think you can
[03:17] go to ai.asure.com as your intercom and
[03:19] like poke around the leaderboard and
[03:20] stuff, but I don't think you're going to
[03:22] be actually able to do anything. Um,
[03:24] that being said, like the models, if
[03:26] you're just doing like a few a little
[03:28] like a few tests with them, it's not
[03:30] that expensive. Like I got a bill of a
[03:33] dollar for the tests I was doing with
[03:35] the anthropic models because I was just
[03:36] doing a few small tests just to make
[03:38] sure that I could like do an agent with
[03:41] them. Um, so, you know, it depending on
[03:45] what you're trying to do. Like if if
[03:46] you're just trying to run a few um, you
[03:49] know, calls and just see how something
[03:51] responds, you know, it's not that
[03:53] expensive. Um, but, you know, obviously
[03:55] if you're developing an app uh, or doing
[03:57] some sort of evaluation or anything that
[04:01] requires um, a lot of calls, then you
[04:05] want um, to actually set up some u way
[04:09] of paying for it.
[04:13] All right. Um, so what else is going on?
[04:16] So yeah, we had the we went to the code
[04:18] with Claude conference this week and um
[04:22] we uh we did a little workshop there
[04:25] where we used Foundry with the cloud
[04:30] models
[04:31] and uh and we made an agent using the
[04:34] cloud models,
[04:36] right? So um so you can actually deploy
[04:40] cloud models like sonnet haiku and opus
[04:43] from foundry
[04:45] and uh and then you can yeah you can
[04:47] build on them. So you can see here show
[04:51] the code
[04:54] right. So
[04:57] you know we said okay this is the name
[04:58] of our deployment. This is our API key.
[05:01] We used keys here instead of keyless.
[05:03] This is our endpoint. And then in this
[05:05] case we were using Microsoft agent
[05:06] framework. So we pointed Microsoft agent
[05:08] framework agent at that model. And then
[05:12] um we built a model that pointed at this
[05:15] cupcake store. and the cupcake store. Uh
[05:19] they could, you know, use the agent to
[05:21] order a cupcake from the cupcake store.
[05:25] Uh so that was fun to finally get to
[05:28] play around with enthropic models on
[05:30] Foundry. Uh we also made um here I'll
[05:34] share this this repo here. Is is this
[05:38] free? Oh yeah, the all of our video
[05:41] series are free to watch. Um they're all
[05:44] on YouTube.
[05:46] Uh what isn't always free is actually
[05:48] like running the code, right? So um you
[05:52] know we try to have all of our sample
[05:54] code be compatible with Olama, right? So
[05:58] I've got Olama running up here uh for
[06:00] local models. So you can try to run
[06:03] samples with local models. Um but then
[06:06] you do need to have uh a powerful enough
[06:09] machine to run a good agentic model.
[06:13] Let's see. So on the other so also
[06:16] related to claude we have this repo here
[06:20] which is a repo for getting started with
[06:26] claude on foundry and it's got some more
[06:29] sample code in it that shows different
[06:30] ways of doing things. It's also got
[06:32] infrastructure for bicep and terraform
[06:34] if you need infrastructure as code for
[06:36] deploying cloud on foundry. And then we
[06:39] have some examples just doing uh this
[06:42] one's using the enthropic SDK directly,
[06:44] right? And showing how you would do that
[06:47] both with keys and keyless.
[06:52] So there's some options for you if you
[06:54] want to use quad on Foundry.
[06:59] Um
[07:01] what else?
[07:03] Uh let's see. I think we've already
[07:05] talked about this GitHub co-pilot stuff.
[07:07] The co-pilot is going through
[07:10] really big um pricing changes right now
[07:14] uh for better sustainability. So that's
[07:17] gonna start affecting people. I think on
[07:20] June 1st is when the big changes happen
[07:23] where we go to usage based billing which
[07:26] I think is the more intuitive way of
[07:27] doing billing which is like based
[07:29] basically on the number of tokens you
[07:30] use. Um but uh it it is going to
[07:34] certainly affect the uh yeah that you
[07:38] know how much you can do with the same
[07:41] uh same plans I guess.
[07:44] Um
[07:48] yes if you know Python for so for for
[07:50] the Python AI series that is designed
[07:53] for somebody who knows some Python and
[07:55] doesn't yet know generative AI. That's
[07:57] what it's designed for. So yeah, if you
[08:00] know Python but haven't learned AI
[08:02] libraries, then um this should be a good
[08:04] one. We might do maybe we'll do another
[08:07] offering of this in the summer just to
[08:09] update it uh with you know latest and
[08:13] greatest models and slightly new ways of
[08:16] doing things, but it's still quite
[08:18] relevant
[08:19] today with what we covered before.
[08:25] Um all right, let's see.
[08:29] What else is going on? Uh,
[08:34] OpenAI said they're winding down
[08:36] fine-tuning. That's kind of interesting.
[08:38] Um, so if you were fine-tuning OpenAI
[08:41] models, I guess that you won't be doing
[08:43] it anymore. At least not on OpenAI. I
[08:46] don't know. I haven't found out if that
[08:47] also is I assume that would affect Azure
[08:51] fine tuning as well, but um
[08:56] I don't know for sure. Here we go.
[08:58] Deprecations.
[09:01] Uh,
[09:04] fine-tune update to open selfarnerence
[09:09] on fine-tune models.
[09:13] Let me ask creating. All right.
[09:18] So, I don't know if this affects as your
[09:20] openi. Let me check on this. Does the
[09:23] OpenAI fine-tune announcement
[09:27] connect Azure OpenAI?
[09:31] All right. So, I'm going to check on
[09:32] that. Um, but uh that's that's
[09:37] interesting.
[09:38] I don't personally know people that were
[09:40] fine-tuning OpenAI models. It's a lot of
[09:43] effort to fine-tune, a lot of money. Um,
[09:46] but you know, if it's worth it, it's
[09:48] worth it.
[09:51] Uh, let's see
[09:54] what else is going on. PYON is happening
[09:56] this week. That's why I'm a bit tired
[09:58] because I've been prepping for Pyon
[10:00] because I'm uh, as soon as the office
[10:02] hours is over, I'm going to hop on a
[10:03] plane and go to Pyon. Uh, so we'll have
[10:06] a lot happening at Pyon. Lots of
[10:08] tutorials and booth and workshops and
[10:11] all of that stuff. Um, so that will be
[10:14] fun. Uh then after that is Microsoft
[10:17] Build and we're going to run a lab there
[10:19] on Foundry IQ
[10:22] and
[10:24] yeah and I guess the other big thing was
[10:26] just that on my side that I got a new
[10:29] Mac and excited to try out the local
[10:31] models.
[10:34] Um Clippy. So, we're not going to have
[10:37] Clippy at I don't think at any of these
[10:40] events. We are going to have at Build
[10:41] there's going to be an openclaw party.
[10:43] And I asked if I could come as a giant
[10:45] lobster
[10:47] and they said no. Um,
[10:52] but I still have plans to be somewhat
[10:55] adorned in lobster, so we'll see. Uh,
[10:58] but yeah, we are going to have an
[10:59] OpenClaw party with Peter, the creator
[11:01] of OpenClaw. Uh, so that should be that
[11:04] should be fun.
[11:07] Yeah. So, Mecca says, "You use different
[11:09] AI models when you run out of tokens.
[11:10] This way you don't spend money." Uh,
[11:13] yeah. I think people find all sorts of
[11:14] creative ways to use the free levels.
[11:16] Like I met somebody yesterday who's
[11:18] using um Nvidia Nim.
[11:22] Um,
[11:23] and I have used NIM. Um, I've used this
[11:27] to like deploy to as your serverless
[11:29] GPUs. But, uh, the developer yesterday
[11:31] was saying that you um, you get a
[11:33] certain amount. Yeah, you can actually
[11:35] try. So, get free access to NIM API
[11:37] endpoints for unlimited prototyping.
[11:39] Really? Wow. Okay. Um, so this might be
[11:45] I'm surprised they say unlimited.
[11:46] There's got to be limits. There's always
[11:48] limits. Maybe it's like slower. I don't
[11:50] know. Um,
[11:52] but um but yeah, this this developer was
[11:55] able to
[11:57] use the nim free level. Um the other
[12:00] thing we have is the you know we have
[12:03] the GitHub models you know which is kind
[12:05] of similar but um the thing is there
[12:08] they haven't updated it with the most
[12:10] recent models and uh they don't support
[12:13] the um responses API and that's what I'm
[12:17] generally using these days. So
[12:20] um you know it's more limited but
[12:23] uh but still something so you know like
[12:25] free you know what are what are free
[12:28] options out there and then of course
[12:30] there's a llama right so a llama like
[12:33] let me actually download some llama
[12:34] models now so what a llama models do I
[12:36] have at the moment um let's see
[12:41] uh
[12:45] lama list.
[12:48] Let's make this big. Okay. Alama.
[12:52] So, I only have Gwen 3.5 and Gemma 4.
[12:57] Those are still
[12:59] those are both good ones. But I should
[13:01] be able to maybe I shouldn't download a
[13:04] model while I'm streaming. Actually,
[13:05] that's probably a bad idea.
[13:07] But I have gotten suggestions for some
[13:09] other models I might be able to try. Um,
[13:11] and I if I go to can I run.ai. This is a
[13:15] website that tries to predict um which
[13:18] models you can run on your machine,
[13:19] right? Oh, I could actually do GPD OS
[13:21] now. GBD is a nice one. Maybe I'll
[13:23] download GPD OS. Um 3.18B is not quite
[13:27] good enough for agent stuff, I would
[13:29] say. Um yeah, the Gwen model is good. I
[13:34] haven't really tried the 54 for aentic
[13:36] stuff. GPD O is pretty good for aentic
[13:38] stuff, so I'll probably download that.
[13:40] Uh haven't tried Mistral. Gemma 3 should
[13:43] be a good one. Um
[13:47] uh and then and then it's it starts to
[13:50] say I'm gonna get worse performance as
[13:51] we go on here. But 27 billion parameter
[13:54] that should be a pretty good one to be
[13:55] able to run. But I won't download this
[13:58] now since I am streaming on multiple
[14:00] platforms right now.
[14:03] Um so Mecca says, "Can you give advice
[14:06] to AI student graduates on what skills
[14:08] to pick up to get interviews lined up?"
[14:10] So, it really, you know, depends on what
[14:14] sort of job you're interviewing for. Um,
[14:17] I I guess I would say if you like, let's
[14:19] say you're interviewing for software
[14:20] engineering, uh, I I do think it
[14:23] benefits you to know how to use uh,
[14:25] Aentic coding tools, you know, like
[14:27] GitHub Copilot or Cloud Code or Codeex.
[14:31] Um because these days that's you know
[14:33] what developer what companies are
[14:37] uh expecting and the developers that
[14:39] aren't willing to use those tools are
[14:44] well I don't know how it's well it's
[14:46] going to work out for them.
[14:48] Uh so there's an expectation um and you
[14:52] know we don't know exactly what the
[14:53] productivity gains are for every single
[14:57] person but there's like like these
[14:58] agentic coding tools can definitely help
[15:00] you write code faster. Like you don't
[15:03] have to spend time with the like code
[15:05] you've written lots of times before. You
[15:07] can still spend a lot of time looking at
[15:08] your code and um improving it and all
[15:10] that stuff. But, you know, if you think
[15:12] like you can use it in the extreme, some
[15:14] people use it in the extreme, but even
[15:16] if you don't use an extreme, it's just
[15:17] like, you know, supercharged
[15:19] autocomplete,
[15:20] you're still going to be more
[15:22] productive. Like, you know, in my
[15:24] opinion, from what I've seen from the
[15:26] amount of um, you know, code I'm able to
[15:29] write with it. Um so I think across the
[15:32] board all software engineers um should
[15:37] uh or data engineers as well um you know
[15:40] should have the ability to work with uh
[15:43] a coding agents in order to speed up
[15:47] parts of your development cycle.
[15:50] Um I don't know if they're going to ask
[15:52] about that in interviews though. Uh you
[15:55] know they might ask like whether you're
[15:56] comfortable with that, whether you're
[15:57] okay with that. I don't know if they're
[15:58] going to ask you like tricky questions
[16:00] about that, right? Um interviews, if
[16:02] you're talking about prepping for
[16:03] interviews, then it like depends on your
[16:04] position, but you know, generally you're
[16:06] going to have like, you know, you have
[16:08] your algorithmic questions, your data
[16:10] structures questions. I assume people
[16:11] are still asking that sort of stuff. Um,
[16:14] but for a particular job, I mean, the
[16:16] best thing to do is just look at the job
[16:17] description and see what skills they're
[16:20] looking for. And then you know if if
[16:23] because if that's a job you want and you
[16:25] don't have those skills then you just
[16:26] work on those skills right so you say
[16:28] like okay like we find a job like we
[16:31] look and see um you know I'll just go to
[16:34] this random one right oh this is open AI
[16:37] okay
[16:38] let's say you wanted to work at openai
[16:40] um
[16:42] so you know I would look at this and see
[16:45] all right so it wants me to be
[16:47] proficient in backend languages right so
[16:50] I'd want to you know, I would just pick
[16:52] Python here and say that was what I was
[16:54] strongest at. Um, now this one actually
[16:56] doesn't have that's interesting. This
[16:58] one doesn't have a lot of like really
[16:59] specific tools listed on it. So they
[17:02] stuff like software engineering
[17:03] fundamentals, distributed systems, and
[17:05] API design. Um, so they're distributed
[17:09] systems like that would be something
[17:11] like there's entire books about
[17:12] distributed systems. I just read an ex
[17:14] excerpt from one last week, right? Um,
[17:17] and there might be like specific
[17:19] interview questions. You can also look
[17:20] up kind of interview questions like
[17:21] distributed systems interview questions,
[17:23] right? And of course, you can also look
[17:24] at glass door and you at Glass Door, you
[17:26] can see specific interview questions
[17:29] uh that you know that other people have
[17:32] done um at that thing. Um you know,
[17:36] usually
[17:38] job descriptions are a little more
[17:40] specific about what um you know, what
[17:45] role like skills they're looking for.
[17:46] And so then you can pick up those
[17:49] skills.
[17:51] Um, but I, you know, I think if you're
[17:53] software engineering, you want to know
[17:54] how to build with AI, meaning both be
[17:57] able to use coding agents and be able to
[17:59] incorporate an LLM into things you're
[18:02] building because imagine like it's like
[18:04] knowing regular expressions, right?
[18:05] Sometimes you need a regular expression.
[18:07] Now, sometimes you need an LLM, right?
[18:09] Like an LLM like red like reax in some
[18:12] way like in a lot of places redax is
[18:14] getting replaced by LLM, right? Like
[18:16] we'd used Reax before when there was
[18:17] like this kind of fuzzy thing and we
[18:19] needed to like fuzzy match it, right?
[18:21] And now we've got LLMs and so the LM can
[18:23] like fuzzy match, right? So just as you
[18:25] like should be able to um you know reach
[18:27] for a Reax if that was the right tool
[18:29] for the job, you should be able to reach
[18:31] for an uh an LLM and know how to
[18:34] incorporate that into a workflow. And
[18:37] it's harder because you have to write um
[18:40] you know different kinds of tests
[18:42] because now you've got non-determinism
[18:44] in there and you've got more risks and
[18:46] and all that stuff. Um but you also
[18:48] potentially have more benefits. So yeah.
[18:51] So that's I mean that's what I would
[18:52] suggest.
[18:56] Um
[18:59] can you be picky on which companies you
[19:01] want when you have no real experience
[19:02] though? Um well usually if you have no
[19:04] real experience then you do try to start
[19:06] off as like a internship level. That
[19:10] being said I didn't I did not start off
[19:12] as an intern because I was like busy
[19:14] doing research in my undergrad. Um so I
[19:18] went into full-time immediately but
[19:20] obviously on a more junior level. So if
[19:22] you have no experience and you're going
[19:24] to start off either as a junior level or
[19:25] at an intern level and you can look for
[19:28] those. Um,
[19:30] but you can still like you shouldn't you
[19:34] shouldn't work at a job if you hate it,
[19:36] I would say. Um, but also there's
[19:38] there's lots of it. For for some reason,
[19:41] LinkedIn is only showing me open eye and
[19:42] anthropic, which are probably two of the
[19:44] hardest companies to get into right now.
[19:47] Um, so I wouldn't necessarily go for go
[19:49] for those. Um, but there's tons of
[19:52] companies out there. Uh, and lots of
[19:55] them can be really interesting. So, you
[19:58] know, don't don't work somewhere if you
[20:01] hate it. Um, but uh, you know, do be
[20:04] open to working at lots of different
[20:07] places.
[20:15] All right. So, let's see. So, Pablo
[20:17] says,
[20:19] uh, I've reading about comparisons
[20:21] between different ways to add knowledge
[20:23] to agents. So carpothes idea ricky wiki
[20:27] vector rag knowledge graph um so
[20:29] depending on the amount of source in
[20:30] their type and depending on the type of
[20:31] query optimal retrieval should be
[20:32] different. So not always vector rag not
[20:34] always graph rag
[20:36] uh based on the query we should use one
[20:38] method or the other which means that for
[20:41] creating a reliable expert agent we need
[20:43] more than just hybrid agentic rag.
[20:48] Um
[20:52] yeah, I mean yeah the interesting thing
[20:53] is um I guess the question is how how
[20:57] you want to
[20:59] you know bring bring those things
[21:02] together um because with like Azure AI
[21:05] search it has that multissource rag and
[21:08] some of those a lot of those rag sources
[21:10] increasingly implement their own
[21:12] retrieval mechanism right so for example
[21:14] with Azure AI search um you'll soon be
[21:18] able to point it at fabric uh ontology
[21:22] and the fabric ontology like that is
[21:25] kind of like a graph more of a a graph
[21:27] approach or like kind of a writing a
[21:30] graph query on demand. Um and so then
[21:33] it'll it just like funnels through to
[21:35] that one. Um and then like work IQ has
[21:38] its own approach to to retrieval as
[21:41] well. So I yeah I do think we're
[21:43] increasingly seeing that you know
[21:45] there's like retrieval layers on top of
[21:47] certain kinds of data. Um, and so it it
[21:52] makes sense to use those retrieval
[21:54] layers, but you might then also, you
[21:56] know, have retrieval like, you know,
[21:58] with like Azure AI search, like you put
[22:00] it in front of those sources and then
[22:05] you can still merge the results across
[22:07] them because the the merging and like
[22:11] the ranking and merging across the
[22:12] results, I think that can be more
[22:17] source agnostic. Um I think the thing
[22:20] that's hard is like the retrieval. Um
[22:23] like but once you actually find matching
[22:26] information then you know looking at
[22:29] like 10 results across your three
[22:31] sources I think that you can you know
[22:34] use the same ranking in order to say
[22:38] okay for this query you know how do
[22:40] these how do these results stack up? Um,
[22:45] so yeah, I think I mean I think you're
[22:49] you're right is that the different kind
[22:51] of we do need different kind of
[22:53] retrieval for for different sources. Um
[22:58] and you know and if we can figure that
[23:00] out and be able to
[23:04] send queries
[23:06] in parallel to different sources that
[23:08] are all using you know customized
[23:10] retrieval mechanisms then then we could
[23:13] have good results.
[23:15] Um,
[23:18] yeah.
[23:21] I guess there's stuff like I mean idea
[23:24] wiki. The idea wiki is like I don't even
[23:27] know how he's searching his idea wiki. I
[23:29] think he's just loading it entirely into
[23:31] the context. I haven't set up my own
[23:34] idea idea wiki yet. Um, LLM wiki. I
[23:38] thought he was calling it idea wiki.
[23:41] Yeah, this is it. This is an idea file.
[23:45] This is the core idea.
[23:47] Uh, so you ingest it. The LM reads the
[23:50] source, writes a summary page,
[23:53] then query. The LM searches for relevant
[23:55] pages, insides, and answers. Okay, this
[23:58] one doesn't really say. So, when it says
[24:00] query, I think it assumes you're using a
[24:02] coding agent that's just going to GP.
[24:04] Um,
[24:06] oh, two special files help navigate the
[24:08] wiki. So, index.ibb has a page and then
[24:11] logged. MD has this. Okay. So, okay.
[24:15] Here we go. So, when answering a query,
[24:19] the LM reads the index first to find
[24:21] relevant pages.
[24:23] Um, then drills into them.
[24:28] Okay. So, it's like it's the index like
[24:30] a database. It's the index. Um, uh, so
[24:34] this is moderate scale, right? This is
[24:36] like
[24:38] Okay, so hundreds hundreds of pages. Um,
[24:42] so it works well like for this like
[24:45] which for for some uses this might be
[24:47] this must be fine, right? Um, 100
[24:49] sources, hundreds of pages
[24:51] and then we have a log
[24:55] um
[24:56] and then
[24:59] images
[25:04] generating slides. I have my own way of
[25:07] doing that. graph view. Best way to see
[25:10] the shape of your whippy wiki.
[25:15] Okay, it's a lot of obsidian. Um,
[25:22] all right. And then there's a huge
[25:25] number of comments on here. What you
[25:27] should do is point like co-pilot at the
[25:30] comments and say, "Hey, read the
[25:31] comments and summarize,
[25:34] you know, what to do." Gosh, are people
[25:36] just dropping there? Jeeez,
[25:40] there's just so many people are probably
[25:42] spamming this to smitherines. Look at
[25:44] this. Wow.
[25:48] Um, that's kind of fun. So this one's a
[25:51] knowledge base
[25:54] local first wiki CLI for AI agents
[25:57] hybrid semantic and keyword search
[26:02] and SQL light for semantic search
[26:05] uh local embeddings with BG base. Okay,
[26:08] haven't tried that one. Uh hybrid search
[26:11] with BM25 and RF. Very good. Um it
[26:15] doesn't have a reranking model but oh
[26:17] well you win some you lose some. Um,
[26:20] agent skill system,
[26:22] npm install.
[26:28] So, I imagine there's a bunch of these
[26:30] now. If you check, I mean, this was just
[26:31] for
[26:33] if you look through these comments,
[26:34] there's just billions of comments,
[26:36] right?
[26:42] Um, but that's I mean, he developed it
[26:44] for his like kind of research case,
[26:46] right? So, the question is whether
[26:49] uh you know it becomes
[26:52] something
[26:54] that you would put also use you know can
[26:57] it handle the scale of something that
[26:59] you want to put in production uh let's
[27:01] see wow there's so many people
[27:06] uh that have made
[27:09] different variations of it on that one
[27:11] you can do with anthropic
[27:18] That's fun. I think researchers are
[27:20] loving this, right? Like this must be
[27:22] just absolutely
[27:25] everything that the the research
[27:28] community wants. Um I don't know if
[27:31] people are using it for more like
[27:33] enterprise use cases. Um
[27:37] there's so many
[27:39] so many people have made repos based off
[27:42] this.
[27:45] Super interesting. Uh, oh yeah, and
[27:47] there's a request for my LinkedIn. So,
[27:49] all of my stuff is off pamelafox.org.
[27:53] And here is my LinkedIn.
[28:08] What you could do, you know, those of
[28:10] you who are practicing your interviews,
[28:11] make an LLM wiki based off of like your
[28:14] interview prep.
[28:16] And
[28:18] I don't know, it could be interesting.
[28:20] Like the thing is like for any of these
[28:21] things, you want to find a reason to try
[28:23] them out, right? And see how they work.
[28:25] So question is like, okay, LM wiki like
[28:28] um for me, you know, I would probably do
[28:30] something with parenting like, okay, I'm
[28:31] going to make an LM wiki based off all
[28:33] the summer camps. um which basically
[28:35] I've already done but I didn't have it
[28:38] called an LM wiki, right? But you know
[28:40] come up with a scenario where it's
[28:42] helpful to try one of these things out
[28:44] and come up with a scenario that like is
[28:46] actually like means something to you
[28:48] where like it would really benefit you,
[28:49] right? So what is something that you
[28:51] legitimately want to research? Is it you
[28:53] know academia? Is it recipes? Is it um
[28:58] you know your kids summer camps? like
[29:01] whatever it is that um is going to be
[29:03] something where you can really evaluate
[29:05] whether it's doing a good job um
[29:09] because uh it's it's really hard to
[29:10] evaluate these systems if you're
[29:12] evaluating it for domains that are
[29:14] outside of your expertise. So I
[29:16] recommend if you can to try building
[29:18] things that are in your domain of
[29:22] expertise so that you can really look at
[29:23] the results and say oh that's correct or
[29:25] that's not correct.
[29:29] Um
[29:33] yeah so Pablo is focusing on expert
[29:35] agent and expert sometimes need semantic
[29:38] sometimes all occurrences and sometimes
[29:40] specific parts of the information.
[29:44] Um, yeah. I mean, yeah, the hard thing
[29:47] with an expert is where you said all
[29:49] occurrences, right? Like here's the
[29:51] hardest thing is like completeness,
[29:52] right? How do you know that you've done
[29:56] a complete search for the information?
[29:58] And I almost I I feel like it's
[30:00] unknowable, right? Like the only way you
[30:01] really know if you've done a complete
[30:03] search of the um
[30:07] information is if you've looked at every
[30:09] single thing, right? Um otherwise
[30:11] everything we use is a heristic where
[30:13] we're like okay well we think you know
[30:15] we we think we got it right. Um
[30:19] so so that's the question is how do you
[30:21] know how do you know if you've done a
[30:24] complete retrieval for everything
[30:28] relevant.
[30:31] Um what you do know what you can reason
[30:34] about is whether you feel you've gotten
[30:37] enough information to answer the
[30:39] question. Like if there's you can you
[30:41] can notice like your expert like either
[30:44] your expert or an LLM that's judging it
[30:46] can say like oh you know what you know
[30:49] we found the answer to this part of the
[30:51] question but we didn't find the answer
[30:52] to this part of the question right um so
[30:54] like Azure AI search they have a new
[30:55] model the semantic classification model
[30:58] and it actually goes through each
[31:01] document and says like you know does
[31:03] this document answer the query and at
[31:06] the end like do we have like have we
[31:08] gotten enough documents to fully answer
[31:10] this query and if not we're going to do
[31:12] another search. Right? So that's
[31:14] something you can put in your your like
[31:17] agent code um which is like okay you're
[31:19] going to you're going to look at each of
[31:20] these. You're going to break the
[31:22] question down into what information
[31:25] needs are in the question. You're going
[31:27] to say you know which of those are
[31:29] covered by which of the results and then
[31:32] if there's still any remaining
[31:33] information needs then you need to keep
[31:35] going. But that still doesn't tell you
[31:38] like absolute completeness, right?
[31:40] Because you don't know what you don't
[31:43] know. Um,
[31:46] so
[31:48] I don't know. I'm Yeah, I'm just I'm
[31:50] thinking through like what I would do um
[31:52] to try and like really really get
[31:54] completeness. um
[31:56] you know like you might want to say
[31:58] something like
[32:00] um if you've identified this query as
[32:02] like a deep query um you know one that's
[32:05] need comprehensive um searching then
[32:08] you're going to use this other way of s
[32:10] you know searching that can that can go
[32:12] more comprehensively
[32:14] across uh or can go deeper or maybe
[32:17] you're just going to allow more tool
[32:19] calls and more retrieval calls in that
[32:21] case if you've identified it
[32:25] Um yeah, graph rag, right? Because with
[32:27] graph rag, um so yeah, because Pablo
[32:31] says graph rag is the best approach for
[32:32] completeness if the anttology is good
[32:34] and complete, right? Um so yeah, if
[32:37] you're confident that it is good and
[32:38] complete because then you're you're
[32:39] following nodes, right? And you can just
[32:41] keep following until you followed them
[32:43] all.
[32:45] Um
[32:47] yeah, but then graph rag is expensive.
[32:49] So that's saying like I think if you're
[32:51] thinking about having graph rag for
[32:52] completeness, you definitely would want
[32:54] some sort of decision layer or like
[32:56] routing layer where you say, "Hey, okay,
[32:59] um you know, it looks like this is a
[33:01] question that requires using our more
[33:04] expensive slow search." Um so you know,
[33:09] we're going to do that in this case. U
[33:10] you don't want to do it in most cases
[33:13] because it's it's you know, too slow,
[33:15] too expensive. Um but if you could
[33:18] identify it and then the question is can
[33:19] you fully identify it right? So maybe
[33:21] you build in um evaluator for that stage
[33:24] which is like um and could and this also
[33:26] could just be an agent with like you
[33:27] know tools. So you know the agent could
[33:29] have a tool like um you know do you know
[33:33] basic search and then have another tool
[33:35] which is like um do a deep search right
[33:38] and in the descriptions for those tools
[33:40] you're like okay you know um usually
[33:41] basic search can answer most questions
[33:44] um but use deep search if um you know
[33:47] the question requires
[33:50] like you know um going across multiple
[33:52] sources or um you know you can like
[33:55] describe it right so you could set up an
[33:58] agent that has those tools on it and
[34:01] then see whether it was making the right
[34:05] call um
[34:07] and um deciding on the tool.
[34:15] Uh I think Pablo has a lot of experience
[34:16] in this field. Pavle is like often in
[34:18] our office hours. He always has great
[34:20] questions.
[34:24] A pipeline. So Karpathi. Okay. So this
[34:26] says karpathy wiki with referencing the
[34:28] summaries pre-process detect entities
[34:30] and relationships and then feeding it
[34:34] into the graph. Yeah, I guess how would
[34:38] that compare to um
[34:41] the uh structured rag from Guido
[34:48] rag.
[34:50] Let me see if I can find it. Pi pie sh
[34:55] Oh, sorry. It's called um type
[35:00] type agent.
[35:02] Well, let me find it. Uh type agent.
[35:08] Um
[35:11] yes. Okay. Type agent py structured rag
[35:14] ingest index query.
[35:19] Yeah. I don't know. I don't know how
[35:21] active
[35:23] tune embedding models
[35:26] add benchmarking tools. Well, seems
[35:28] pretty active. Guido committed
[35:32] in the last week. Um,
[35:36] so I haven't tried
[35:39] this this out, but I feel like it's kind
[35:42] of it might um give you some inspiration
[35:45] because it has um the ability to pull
[35:47] out uh entities and
[35:50] relations. So tools um
[35:55] ingest email, right? So it tries to
[35:59] so it's kind of geared for certain sort
[36:00] of stuff. So it has ingest email, ingest
[36:02] podcast, ingest bttt.
[36:06] Um, so I guess they're really like
[36:07] testing it for specific ones examples.
[36:18] Yeah, I don't know how far along it is.
[36:20] Oh, I saw Okay, so there's Let me just
[36:22] link to things just for the record. Um
[36:30] yeah, and the graph rag that we were
[36:32] talking about is the Microsoft graph
[36:35] rag. Um
[36:39] but there's also the
[36:42] um there's some been some variants of
[36:44] it. I saw something really. So,
[36:45] hindsight
[36:47] is a memory package and I saw a talk
[36:50] about it last week
[36:52] and they were doing a similar things
[36:54] with like really using um
[36:58] lots of different
[37:01] like forms of retrieval.
[37:10] And oh, look at that. You could wrap
[37:12] just wrap openi. Nice.
[37:18] I'm trying to see if they have
[37:19] hindsight. Okay.
[37:23] Install prepare metadata. I mean, this
[37:26] one's specific to memories, but um but I
[37:29] thought it was interesting because it
[37:30] looked like it had
[37:32] they were kind of using different
[37:34] things. Yeah, they were using
[37:36] different kinds of structures behind the
[37:39] scenes. So
[37:41] um you know just you know different
[37:44] different retrieval mechanisms,
[37:48] entity links, temporal links, semantic
[37:50] links, causal links, right? So they're
[37:52] they're doing something like a graph
[37:54] with the memories.
[37:57] Oh, here we go. So this was input query.
[37:59] So the input query does a semantic
[38:01] search, a keyword search, a graph
[38:03] reversal, and a time series and then
[38:06] merges them all together. So this is
[38:08] similar what I was saying before is that
[38:11] you know it's it's good to be able to do
[38:13] queries in parallel and then um but then
[38:17] when you're merging them uh and this one
[38:19] includes the reranking model too the
[38:21] cross encoder ranking. So then when
[38:23] you're merging those in
[38:25] uh then um then you know then you can
[38:29] use the same merger across all of them.
[38:32] Um,
[38:35] I think this one like will always do all
[38:38] of these unless you, you know,
[38:40] explicitly turn them off. But, um, but
[38:42] you can imagine that, you know, you
[38:44] could also make these into tools that it
[38:46] could decide which of them it's going to
[38:48] call, uh, and do them in parallel or
[38:51] not.
[38:54] Um, and it has kind of a dreaming stage,
[38:57] a reflection.
[38:58] Uh,
[39:01] yeah. Anyway,
[39:03] that was that was interesting. It
[39:05] reminded me a bit of this conversation.
[39:12] What else?
[39:26] Any other
[39:31] thoughts, questions, ideas?
[39:39] I still haven't set up a graph rag for
[39:42] anything.
[39:44] Waiting for it to be easier to do.
[39:48] Um,
[39:55] yeah, I think you can try like I mean
[39:56] you can take the idea of graph rag and
[39:58] just make it cheaper, right? They they
[40:01] had a research paper about a lazy graph
[40:02] rag, but I don't um I don't think they
[40:05] put it out there. Let me see because
[40:06] I've heard alternate names for it. Graph
[40:08] rag zero.
[40:11] This one. Yeah, but they haven't done
[40:14] the code for it. But um but you can you
[40:16] know you can just invent your own lazy
[40:19] graph rag.
[40:22] You can just point C-pilot at this and
[40:25] then uh
[40:27] actually I don't know I haven't read
[40:28] this one to see if it has enough
[40:30] implementation details. Um
[40:33] but yeah you can you know you can
[40:35] experiment. Um
[40:38] there's
[40:40] you could like set up a a Ralph loop. I
[40:44] was chatting with the you know the Ralph
[40:45] loop the I met that creator this week as
[40:48] well. He came to last night's meetup. Um
[40:51] so Ralph loop a Ralph loop is just a
[40:54] very very persistent AI agent loop that
[40:57] just keeps working and working and
[40:59] working and working
[41:01] uh until it's finally complete. Um so
[41:03] even if it tries to exit, it doesn't let
[41:05] it exit.
[41:08] It'll just keep going. Um, so you could
[41:10] say like, "Listen, we want to like set
[41:12] up a a cheaper graph rag and maybe
[41:16] you're gonna experiment with it."
[41:19] It would probably help to have some
[41:21] emails on it. I also have not tried it
[41:24] tried doing a Ralph loop yet, but
[41:25] basically all of the different um all of
[41:28] the different coding agents have it now.
[41:30] So Codex has slashgo
[41:34] um and that is the same thing as a Ralph
[41:36] loop. And then let's see what is
[41:39] co-pilot CL like co-pilot C like man
[41:43] um
[41:48] let's see
[41:50] loop R
[41:53] goal
[41:56] uh let's see is it is it a plugin
[42:00] I'm just going to ask this
[42:06] Uh,
[42:08] okay. I'm just going to ask, does
[42:10] co-pilot have a Ralph flute
[42:19] when I control
[42:22] that? Or actually, let me just search
[42:24] Copilot
[42:26] CLI Ralph Floop.
[42:30] Oh, there's a plugin.
[42:33] Okay, there's definitely plugins. Um,
[42:36] oh, maybe it's fleet mode because Burke
[42:39] has a video here.
[42:42] I have heard of fleet mode.
[42:46] Fleet enable parallel.
[42:49] Yeah.
[42:52] Is fleet closest?
[42:55] All right. So, anyway, RAF loops are
[42:57] interesting. Um,
[42:59] I'll just link to those and I'll see we
[43:01] have some more questions
[43:03] and
[43:07] Okay, so we had other questions. Um,
[43:13] uh, let's see. Can I explain the
[43:15] different use cases like work IQ, fabric
[43:17] IQ, and Foundry IQ? It's a great
[43:19] question since we're working on the lab
[43:21] about it right now. Um,
[43:24] so Foundry IQ
[43:27] will be able to basically pass through
[43:29] to all of those sources. So, Foundry IQ,
[43:34] think of that as both something that can
[43:35] like set up search indexes and search
[43:38] those indexes, but it can also manage
[43:40] search at a higher level and connect to
[43:42] different sources, right? Um, so it's
[43:45] kind of got built-in connections. It can
[43:47] connect to any sort of MCP endpoint. So,
[43:49] it can it can be a higher level search
[43:51] that can handle sending queries to
[43:54] multiple sources in parallel and then
[43:57] getting back the results and merging
[43:59] them, right? So you know um uh using
[44:03] both uh reciprocal rank fusion and
[44:06] semantic ranking models in order to
[44:08] merge things together. Um so that's I
[44:11] would think of Foundry IQ as being the
[44:13] the higher level search uh mechanism
[44:18] um but also being able to you know
[44:20] create indexes itself if you if your
[44:22] data doesn't exist anywhere else yet.
[44:25] Fabric IQ uh is has both the ontologies
[44:29] and the data agents and both of those
[44:31] are things that you can query. So the
[44:33] ontology
[44:35] is h I'm still learning how it works but
[44:39] um
[44:41] the ontology is like
[44:44] uh yeah okay uh
[44:49] right so you can like query your
[44:51] anttologies I think it's you're you
[44:53] basically come up with the ontology and
[44:54] then fabric IQ you can like send these
[44:56] basic kind of graph-like queries on that
[44:58] ontology right because it is like a
[45:00] graph representation and then you can
[45:02] query on top of those graphs. So, it's
[45:04] like a way of doing, you know, like kind
[45:08] of like SQL queries on on top of your um
[45:13] your fabric data. Um it just uses its
[45:16] own terminology,
[45:19] but you can like pass in a a query that
[45:21] can go across um all the ontology, all
[45:26] the all the entities in that graph.
[45:30] Um
[45:31] and then they also have something called
[45:34] um where's data agents? Okay, so they
[45:36] also have data agent and
[45:40] what does this do? Okay, so this is more
[45:42] about insights. I haven't this one I'm
[45:44] completely new to but just brought it up
[45:46] today. Okay. Um oh, so this one actually
[45:50] data agent incorporates its own LLM.
[45:55] So it'll actually try to answer the
[45:57] questions itself.
[45:59] Um, so that's interesting. So that's
[46:01] like
[46:03] that's I would say that's seems like
[46:04] higher level than ontology, but I need
[46:06] to
[46:09] uh understand that a bit better.
[46:12] Um, but you have you have both those
[46:13] options. You have to like enable them on
[46:15] your fabric tenant at the tenant level.
[46:17] So your admin has to enable them or you
[46:19] if you're the admin. And then there's
[46:22] work IQ. So currently work IQ
[46:26] is you know uh basically a CLI and an
[46:30] MCP server and an agent. So it's like an
[46:33] MCP server in front of an agent. So it's
[46:36] actually most similar to the data agent,
[46:37] right? How the data agent has an LLM as
[46:39] part of it. Um work IQ is like that but
[46:43] for M365. So it can it can query your
[46:46] teams chats, it can query your emails,
[46:48] it can query your calendar events. It
[46:50] can't take any um actions. So it can't
[46:53] uh create, edit, delete right now. Um
[46:55] but it can query all those things and
[46:59] uh it can be easier to integrate with
[47:01] work IQ just from kind of a permissions
[47:03] perspective in terms of setting up the
[47:05] permissions for quering M365.
[47:09] Uh but you can think of it as being an
[47:12] agent on top of um your M365 readonly
[47:17] data
[47:20] and you can integrate it with the
[47:21] various ways because you can use it
[47:23] directly from the command line um or you
[47:25] can run the MCP server and then you can
[47:28] point anything that supports MCP at the
[47:30] MCP server right so coding agents
[47:33] programmatic agents etc. Um, but you do
[47:37] have to set up the O and they are
[47:39] currently like changing how the O works.
[47:42] So
[47:43] stay tuned for build because build is
[47:46] the point at which things often change.
[47:52] Um, let's see. Okay. Okay. There's a
[47:54] good question about math. So I'm gonna
[47:58] defer to
[48:00] the agent framework team on that one
[48:02] since we're getting to the end of our
[48:04] office hours. And I do have a plane
[48:06] catched uh plane flight to catch. Um but
[48:09] so math the Microsoft agent framework
[48:11] team they do have um they have their own
[48:15] office hours as well. Uh I haven't tried
[48:17] attending them yet but um I think that
[48:20] would be a good place but also they have
[48:23] they've enabled the discussions tab
[48:25] here. I don't know if you've tried
[48:27] uh asking here yet. I do see a lot of
[48:31] unanswered ones. So, uh, oh, but some of
[48:34] these I think they just haven't been
[48:35] marked because this is Evan. Evan's on
[48:37] the project. So, um, yeah, given we're
[48:41] out of time and I also don't I don't
[48:43] think I don't think I know your answer
[48:45] directly. Does maps accommodation
[48:46] checkpoints and session per agent?
[48:52] Um, the other thing to check out is we
[48:54] did have the uh wait
[49:03] Um,
[49:12] no. I want doing human loop. Yeah, I
[49:15] think that there's an example here.
[49:23] This one.
[49:32] So, this one might
[49:36] this one might have a combination of
[49:39] session and um checkpointing in it. I
[49:42] don't know if you've looked at it yet.
[49:45] Uh
[49:49] trying to remember where
[49:51] would be
[49:55] handoff orchestrator.
[49:58] Yeah. So it does this one uses
[50:00] checkpoint storage
[50:03] and
[50:06] and it also uses okay based off like the
[50:09] thread ID. Oh so you may want to check
[50:12] those out. Um this is from Davididmo.
[50:15] So he's I think done the most um
[50:18] experimentation with
[50:21] that like combination of features. Um,
[50:25] so he's
[50:27] also a good one um to ask. He was
[50:31] bringing up a lot of questions about
[50:32] workflow state uh with the agent
[50:35] framework team the other day. Uh so I
[50:37] would dig into that. Um but uh yeah, so
[50:41] check out the examples but post in their
[50:43] their forum if it's still unclear
[50:45] because I think probably needs more
[50:47] clarification if it's not clear yet.
[50:51] Okay. Okay, Pablo explained ontology
[50:53] that entology is the template of the
[50:55] types of nodes and okay and yeah and
[51:00] then we can query when we query the
[51:02] ontology we're quering the actual data
[51:05] um but using the ontology as like the
[51:10] um
[51:12] the kinds of things we're querying I
[51:13] guess
[51:16] um all right sweet okay
[51:21] See, thank you everyone
[51:24] for coming today.
[51:26] Sorry I'm a little sleepy. Um, but uh
[51:31] still fun to
[51:34] find out what everyone's working on. Uh,
[51:37] so yeah, I'm gonna go off to Pyon now
[51:42] and I'll be back next week for our next
[51:46] weekly office hours.
[51:50] All right.
[51:56] Ah, thank you. Thank you, Pablo.
[51:59] Should have Pablo do the fabric office
[52:01] hours.
[52:04] All right. Thanks, everyone. Bye.
