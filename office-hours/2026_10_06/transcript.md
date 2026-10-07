[00:00] Okay, welcome everyone to our weekly
[00:04] Python plus AI office hours. As usuals,
[00:08] I've collected some of the news from the
[00:11] last two weeks since we didn't have
[00:13] office hours last week because I was at
[00:15] OpenAI Dev Day, which is where lots of
[00:18] the news comes from. So, collecting lots
[00:20] of news there. Um, so we can chat about
[00:23] some of the things announced at OpenAI
[00:25] Dev Day. um or just uh talk about
[00:30] whatever people uh want to talk about.
[00:33] So just if you have any questions or
[00:35] news to share, just post it in the chat
[00:37] and I'll be watching the chat the whole
[00:40] time.
[00:42] Uh so yeah, so OpenAI Dev Day, uh that
[00:46] was in San Francisco last week and um
[00:50] they you know they announced several
[00:54] several things here. So, probably the
[00:56] most efficient way of seeing what they
[00:59] announced. Um, they've got the recap,
[01:02] but also, let's see, um, which which is
[01:06] the most they announced quite a bit.
[01:09] Okay, so let's see. Um, they did sign in
[01:11] with JBT. So, that's, you know, like you
[01:13] have sign in with Google and and all
[01:15] that stuff. So, now you can sign into
[01:18] stuff like other coding agents. So, T3,
[01:21] Open Claw. Uh so really like OpenAI is
[01:24] trying to have people use their credits
[01:27] not just towards chat dbt and this is a
[01:30] really different approach than what um
[01:33] Enthropic is doing. Um GitHub copilot is
[01:37] kind of in the middle where obviously
[01:38] you can use GitHub copilot with lots of
[01:40] different models and across many
[01:42] different surfaces but it's not quite as
[01:44] going as far as like you know there is a
[01:46] sign in with GitHub but there's not a
[01:47] sign in with GitHub copilot. So this way
[01:49] if you sign up with chat GBT you're
[01:51] actually using your uh like kind of you
[01:54] know AI credits um your like token
[01:58] credits for
[02:00] uh you know for other other um you know
[02:04] other apps. So that's very interesting
[02:06] that they decided to open that up. Um
[02:10] uh so that's cool. Oh they added a
[02:13] really expensive tier because they added
[02:14] this ultraast model. So, the Ocean Fast
[02:16] model is like really fast, but also, you
[02:19] know, because it's so fast, it's more
[02:21] expensive. And so, they decided they had
[02:24] to add it add a new plan for that. So,
[02:27] that's I guess $500 a month feels like a
[02:31] lot. Uh, but, you know, maybe it is
[02:34] worth it, especially if you can get your
[02:35] company to play. Um,
[02:39] and yeah, and they did a lot with the
[02:40] plugins. So going to the plugins because
[02:42] we've talked a lot about chaty plugins
[02:45] here before. So chaty plugins are based
[02:49] off of MCP. So that's why I was
[02:51] interested in this. Uh so they've um you
[02:55] know they've extended plugins to have
[02:59] more ways of integrating with the
[03:00] sidebar and with the full view and
[03:02] they're actually using MCP apps. H so
[03:05] that's the ability to like basically
[03:06] iframe a website as part of an MCP
[03:08] server. So they're building on top of
[03:11] MCV apps. Let me see if I can find the
[03:14] uh here we go. So this is the way in
[03:17] which they've built on top of
[03:20] uh MC apps. So let me share this too. Uh
[03:23] so I chatted a lot with their MCP team
[03:25] there. Uh so uh they may upstream some
[03:29] of these know some of this might get
[03:32] suggested as improvements to MCP itself.
[03:35] So you can see this is the way in which
[03:36] they've extended MCP
[03:40] uh specifically in this spec.md here
[03:42] right and uh you know they've added
[03:46] things like these entry points like the
[03:48] fact that uh these apps can be invoked
[03:51] at particular entry point they also
[03:53] added file extension handling so you
[03:55] know if somebody's dealing with certain
[03:57] file it an MCP server knows that it can
[04:00] handle that file so that's quite
[04:01] interesting Um,
[04:05] so yeah, it'll be interesting to see if
[04:07] this gets added to MCP itself,
[04:10] uh, or if this stays as specific as only
[04:14] an OpenAI extension.
[04:17] Uh, but if you are building, you know,
[04:19] MCP servers and plugin for Gachibbt,
[04:22] then you definitely want to,
[04:25] uh, check this out.
[04:27] Uh they also added support for MCP
[04:29] events which is pretty cool because they
[04:31] are the first the first major client to
[04:35] support MP events and uh this is this is
[04:38] pretty cool because this is really like
[04:40] it's even you know not a full not fully
[04:43] in the MCP spec yet. Um but they decided
[04:46] to go ahead and add it for it because
[04:48] they wanted to have triggers and events
[04:51] and automations and all that stuff. So,
[04:53] that's another thing you can add.
[04:57] Uh, oh, and they also made it easier to
[04:59] discover plugins. So, when you're
[05:00] chatting in Chat GBT, it'll actually be
[05:03] like, "Oh, I see you're, you know,
[05:06] trying to book a hotel. Like, maybe
[05:08] check out this plugin." Uh, but they're
[05:09] only going to recommend plugins if they
[05:13] like clearly see that, you know, your
[05:15] plugin has really good usage, good
[05:17] ranking, like that people are truly
[05:19] using it, right? because they obviously
[05:20] they don't want to recommend, you know,
[05:23] plugins that aren't good, right? So, if
[05:25] you have a good plugin and it's
[05:27] appropriate, you know, it's well ranked,
[05:29] um, good usability, then it could get
[05:32] recommended to people who are chatting
[05:34] and chatting.
[05:37] That's cool. Uh, let's see. They
[05:40] introduce dots. Dots are basically a
[05:43] longunning agent with memory. Um,
[05:47] and they're, you know, building on top
[05:49] of ChachiBT. I think it's basically
[05:51] their equivalent to Grockbot and to
[05:54] Muse. Um, the closest thing we have at
[05:57] Microsoft is Autopilot.
[05:59] Um, which, you know, has its own
[06:01] identity and it's long running, but um,
[06:06] yeah, we'll see. I don't know if any of
[06:08] you are playing with your dots yet.
[06:10] Uh, let's see. We also had 61 soul. So
[06:13] this one is nice because it delivers
[06:16] near Astro Intelligence at fifth of its
[06:18] standard input and output token prices.
[06:20] Right? So the big story here is the
[06:22] cost. Um and you know if you weren't if
[06:26] you were thinking if you liked Astra
[06:29] but you didn't like the cost of it. Um
[06:31] you know now we've got this 61 soul.
[06:35] Uh so there we go. So that compares to
[06:39] Astra and and Soul. Uh, I'm still on
[06:42] Opus 5.5, but you know, if you like the
[06:46] GPD series, it could be a good one. We
[06:48] are updating all of our, you know, as
[06:50] your opening samples to use 61 soul now
[06:52] that it's out. Uh, so it's already
[06:55] available in Foundry, so you can you can
[06:58] use it in Foundry already and see if it
[07:02] works well for your scenarios.
[07:05] Okay. So, I think that was a lot. Oh,
[07:08] yeah. Yeah. also okay codeex has cloud
[07:10] you know that's similar to like you have
[07:12] copilot cloud um so making it easier to
[07:16] do things remotely um but relevant to
[07:19] developers we have the decisions API so
[07:22] what they so obviously Jeb has been
[07:24] taking the world from storm by storm the
[07:26] last three weeks was October first no
[07:29] Jeb came out when did Jeb come out but
[07:32] type safe Jeb I don't know if any of you
[07:33] got access to it yet um but you know
[07:36] it's what was called like a system one
[07:37] model uh you know it's a very fast model
[07:41] that can do that can make structured
[07:44] decisions that can classify things like
[07:46] pick a category pick a boolean etc. Um,
[07:49] so you can see like all it can do is
[07:50] make it choose an option from a list,
[07:53] give a score or say, you know, give a
[07:55] boolean true false, right? So that's all
[07:57] it can do. But in fact, when that's what
[07:59] you have, then you can do quite a bit.
[08:01] So everyone's been going crazy with Jeb
[08:04] because it's very fast. Uh, it seems to
[08:07] be very accurate and, you know, it can
[08:11] be a good replacement for a lot of
[08:12] situations where we're using structured
[08:14] outputs before. So um people are really
[08:17] excited about it and all the u model
[08:20] providers are trying to figure out how
[08:21] they can offer something equivalent
[08:23] because you know they want to they want
[08:25] to get in on this u so we're seeing lots
[08:28] of kind of equivalents of jab. So with
[08:30] openi what they announced was this
[08:32] decisions API. So the decisions API is
[08:34] they took Luna and they um added with
[08:39] constraint decoding to Luna to make it a
[08:42] lot faster
[08:44] and make it basically act kind of like
[08:48] Jev in terms of the API. So they built
[08:50] this new API called the decisions API on
[08:52] top of this constrained Luna
[08:55] and uh and yeah so that's like if you
[08:58] wanted to build on the OpenAI model
[08:59] ecosystem you know you don't have access
[09:01] to Jeb or you just want to keep working
[09:03] with OpenAI models the decisions API is
[09:06] there equivalent to Jev at this point
[09:10] right we'll see if they come up with
[09:11] like an actual thing because I saw some
[09:13] feedback you know from the Jev folks
[09:14] that's like okay well the constraint
[09:16] decoding reduces your accuracy right
[09:18] like that that approach approach is not
[09:20] a good approach to get this kind of
[09:22] model. Um, but it might work for you.
[09:24] So, um, now the thing is this API, they
[09:27] announced it, but it's not available
[09:28] yet. So, I'm still waiting to see, uh,
[09:32] when they actually release it. I think
[09:34] that it was a very last minute thing.
[09:37] Uh, and they haven't been able to fully
[09:39] release it yet. Oh, I see some feedback.
[09:42] So, Jeb is small, but the performance is
[09:44] bad in my experience. Sorry. All right.
[09:46] So when you say performance, are you
[09:47] talking about quality performance or
[09:49] latency performance? I'm curious um
[09:52] which kind of performance you're talking
[09:53] about there. Uh let's see. The other
[09:56] relevant thing is agents API. So agents
[09:59] API is that basically their managed uh
[10:03] like managed codeex harness in the cra
[10:05] in the cloud. Right now this is just on
[10:07] open AAI. I think there's a possibility
[10:09] it's going to make it to Azure in the
[10:11] future because it's kind of like the
[10:12] equivalent of the assistance API. Um,
[10:16] but you know, it does a lot more. So,
[10:18] that'll be interesting to see. Um, you
[10:21] know, because obviously if it makes it
[10:22] to Azure, then you know, we're going to
[10:23] have people trying that out on Azure.
[10:25] So, we'll see uh how that works because
[10:27] that would be an alternative to like
[10:29] Foundry Hosted agents, for example.
[10:32] Um,
[10:34] okay. So, I think those were the big
[10:37] things that were Oh, and there was also
[10:41] a new Oh, where did they mention? They
[10:42] didn't mention live. Um they did a lot
[10:45] with voice like you might have famously
[10:47] seen that their voice demos didn't uh
[10:49] that failed during the keynote um
[10:52] because they really were trying to show
[10:53] off the new GPD live model quite a bit.
[10:56] GPT live opening eye. Uh so they have
[11:00] this GD live model and they were trying
[11:04] to use it quite a bit. This says July
[11:06] but I wonder if they did something more
[11:07] recent uh because they were using this
[11:10] quite a bit or trying to use this during
[11:12] the keynote. it kept failing. Um, but
[11:14] they did also have a session about it
[11:16] and during the session people said it
[11:18] looked like it had gotten a lot better.
[11:20] So, I haven't I haven't messed around
[11:22] with it yet. Um, but it's probably worth
[11:28] seeing if GPD live uh works well for
[11:31] your real-time voice scenario. Um,
[11:35] because apparently people are saying
[11:37] it's pretty good.
[11:41] Um, we know funnels. Okay. All right.
[11:45] Hop says, "Latency is good. Blazing
[11:49] fast." Okay. So, the latency good. Um,
[11:52] but without any reasoning, it's not as
[11:54] good as what people are used to with
[11:55] LLMs. Um, so maybe for mass email spam.
[11:58] So, okay. So, you're saying the quality
[11:59] like the accuracy. So, that's good to
[12:01] know. So, maybe the decisions API, it'd
[12:03] be interesting to see if the decisions
[12:05] API works better for you. But that is
[12:07] decisions API like they turned reasoning
[12:09] off on Luna. So I think they turn
[12:11] reasoning off like reasoning none and
[12:13] then they add on this they use this
[12:15] thing called constraint decoding. I'm
[12:17] not an ML expert so I'm not sure exactly
[12:19] how that works. Um
[12:22] so um it you know be good to see once
[12:26] that comes out if that's going to give
[12:29] you better quality. Um you know that'd
[12:32] be good to know. Uh, okay. For for
[12:35] getting started with Python and AI, I'll
[12:39] just give you the normal
[12:41] um link that I send around, which is
[12:44] just our Python and AI series,
[12:48] um, which is a one way of getting
[12:51] started.
[12:54] Okay. All right. Uh, yeah. So, those are
[12:56] all the Open AI
[13:00] announcements.
[13:01] Um,
[13:03] related to that, you know, we do have
[13:04] GP61 soul now in GitHub Copilot. We also
[13:08] have it in Foundry, so you can try it
[13:10] out there. Um, oh, we did this big
[13:13] announcement for of Copilot Home. Uh, so
[13:19] Copilot at home, I don't even have it
[13:20] yet. I'm sorry, but I don't know. I
[13:23] because I think it's limited. I think
[13:25] it's still limited abil um rollout,
[13:28] but it's worth pointing out because this
[13:30] did get launched. Um, so I guess they
[13:33] just combined various apps into one. So
[13:36] this co-pilot has home, code, and
[13:39] autopilot.
[13:41] Um, code is literally the GitHub copilot
[13:43] app, but they like stripped out some
[13:45] features. I was chatting with the
[13:46] Copilot team about that. Um, because
[13:49] they basically realized like a lot of
[13:50] people are like using the GitHub Copilot
[13:52] app, but like maybe don't necessarily
[13:53] even have a GitHub, you know, a GitHub
[13:55] username. like because you see how many
[13:57] of my chats are actually just quick
[13:59] chats and already been tied to a um um a
[14:03] project. Um so yeah, so that's the code
[14:07] tab. So I know that the code app tab is
[14:09] basically you can see it looks like
[14:10] really similar. You got automations and
[14:13] stuff like that. So it's the GitHub
[14:15] copilot app but without having a
[14:17] dependency on GitHub repos. And then
[14:20] there's autopilot previously called
[14:23] Scout. So if you're using scout, this is
[14:25] now called autopilot. So an autopilot is
[14:27] an agent that has an identity. So this
[14:29] similar to, you know, Muse and Grockbot
[14:32] and stuff like this. Um,
[14:36] and uh, it's interesting called
[14:38] autopilot because you can also make your
[14:39] own autopilot agency agents because my
[14:42] colleague Aisha and I have been doing a
[14:44] lot of demos and presentations showing
[14:46] how to build your own autopilot. So I
[14:48] guess this is you know kind of your
[14:50] default autopilot but if you wanted to
[14:52] make custom autopilots for particular
[14:54] workflows you can you know make your own
[14:56] autopilot agents and register them with
[14:58] the directory.
[15:03] Uh let's see so Bernard is sharing Uber
[15:07] announce management platform.
[15:10] Um that makes sense. I think I saw a
[15:12] talk by them like two years ago. So did
[15:14] they
[15:16] um because they have so much they use so
[15:18] much MCP
[15:20] um oh uh that you know they like they
[15:23] just have like this whole dedicated
[15:26] um tooling internal tooling team that
[15:29] makes you know stuff like the MCP
[15:31] registry. Uh so yeah they had a very
[15:33] cool talk. So um I could see that. Um,
[15:37] oh, and there's he the so, um, J, this
[15:40] is JQ. He gave a talk about his thing
[15:43] for us last week. Um, so if you, you
[15:47] know, want to build yourself, of course,
[15:49] at, um, Azure, we have the APIM AI
[15:52] gateway as well. We also have Foundry
[15:53] Toolbox, which is basically an MC
[15:55] gateway. Uh, so yeah, there's definitely
[15:58] this trend toward MC gateways and
[16:02] multiple different approaches for it.
[16:06] Uh, I also saw that just reminds me that
[16:08] I saw Door Dash has MCP which amuses me
[16:12] quite a bit. Um, a gentic ordering a
[16:15] gentic ordering on Door Dash. Uh, which
[16:18] I think is really fun. So, if you need
[16:21] Door Dash CLI
[16:25] because I because you know it's too much
[16:28] effort to uh place your order in the
[16:31] thing, right? Uh, but it amuses me that
[16:34] there's like so much usage of Door Dash
[16:37] for, you know, on the event basis, which
[16:39] I like doesn't actually surprise me that
[16:40] much because I also use Door Dash for
[16:42] events. Um, but I I just think it's
[16:45] great. Like I I think it's great to see
[16:48] uh you know, MCP servers
[16:51] being used across the the industry. So
[16:55] the fact that Door Dash has MCP,
[16:59] you know, it's really it's really uh
[17:02] it's really becoming
[17:04] prevalent
[17:06] across, you know, across the industry
[17:09] then.
[17:11] Um,
[17:13] cool. Okay, let's see what else. All
[17:17] right, talk about this. Oh, GitHub
[17:19] Copilot. So, a few things for GitHub
[17:21] Copilot as well. Um, Copilot added
[17:25] something called dynamic workflows
[17:28] and these are workflows
[17:31] that like programmatically define how a
[17:34] task is carried out. Uh, so I've seen a
[17:38] talk about it. I haven't actually,
[17:42] you know, run set up a workflow
[17:46] myself. Um, let me see if we can find an
[17:48] example.
[17:54] Okay. So, here's like the creating a
[17:57] dynamic lo workflow. So, it probably has
[18:00] a built-in skill for it. Um,
[18:04] but I wanted to show the code for it.
[18:08] So, I saw some code.
[18:11] Let's see.
[18:18] I wanted to see the like JavaScript for
[18:20] it.
[18:21] Um,
[18:24] reusing and sharing
[18:29] sharing the results. I wonder if we have
[18:32] any on awesome co-pilot.
[18:35] Awesome co-pilot.
[18:37] Let's see. Do we have workflows here
[18:40] yet? No, we don't. Okay. All right.
[18:43] Well, um yeah, I so in the presentation
[18:46] that I saw of this
[18:48] um
[18:51] there was uh you know they were showing
[18:54] actual like JavaScript code that was
[18:56] orchestrating the workflow. All right, I
[18:59] guess we'll just tell it what to do. Um,
[19:03] so here uh
[19:07] um
[19:10] let's see
[19:13] that list us. Okay, so we're just going
[19:15] to tell it to make a dynamic workflow
[19:19] and see how that works out. Um it says
[19:23] it's available in both the CLI and the
[19:27] app. Uh for the CLI you have to enable
[19:30] experimental.
[19:32] Um, but I think it's just already
[19:34] >> Oh, sorry. I have a sound my If you hear
[19:39] my that sound, that's the sound of my
[19:41] child giggling. So, every time an agent
[19:43] stops working for me, I hear my child
[19:47] giggle. Uh, so that's a hook that I've
[19:49] set up. So, if you hear that, that's
[19:50] just that just means that the agent has
[19:53] completed.
[19:56] Uh, so let's see. So,
[19:58] >> oh, here we go. Okay. I should probably
[20:00] turn the sound off when streaming.
[20:01] somehow. Um,
[20:04] oh, I'll just turn my audio off on here.
[20:06] Okay, so you can see here it created a
[20:11] workflow.
[20:13] Um, and yeah, so this is what it does.
[20:16] It does use JavaScript, right? So, it's
[20:17] using this JavaScript here thing and um,
[20:20] you can see it has like phases, right?
[20:23] So, and then arguments and then it runs
[20:26] it. Uh I guess it really tries to hide
[20:28] the JavaScript for you and and really
[20:31] encourage you to use natural language
[20:32] but it is via this whole um this whole
[20:35] SDK here right uh and it like you know
[20:38] it can like spawn sub agents it can do
[20:40] things in parallel can do things in
[20:42] independent right so if you want to have
[20:44] like a lot of control over the you know
[20:47] the workflow for something um because
[20:51] some people were already like trying to
[20:53] do this and this gives you like a lot of
[20:55] control over it. So it made you know it
[20:58] made a workflow. I haven't run it. List
[21:00] changes.
[21:02] Uh
[21:04] summarize.
[21:06] Okay. Run it.
[21:10] Wait, how do we supposed to run it if
[21:12] you Okay. Running a dynamic workflow
[21:14] enter natural language. Okay. All right.
[21:16] So run.
[21:18] Okay. Run the review changed workflow.
[21:25] All right.
[21:26] Let's see.
[21:30] Yes, I have turned off the giggling. Um,
[21:33] it's really it's very helpful because a
[21:34] lot of times I'll like be doing
[21:36] something else or walk away from my
[21:37] computer and if I hear the giggle, that
[21:40] means I come back to my computer and see
[21:43] what my agent has done. And you know, I
[21:46] thought I would get tired of hearing my
[21:47] child giggle, but you know, turns out I
[21:50] don't, which is good. All right. So, you
[21:53] can see it is running the workflow in
[21:55] the background
[21:57] and um Oh, cool. So, you can actually
[21:59] see background activity. Oh, look at
[22:01] this. Oh, this is fun. This is new,
[22:03] actually. I've never seen this
[22:04] background activity tab. Um, wow. Oh
[22:08] gosh, I forgot how large this Oh, this
[22:11] is a really big branch. I forgot that
[22:13] this is a massive branch. So, it has now
[22:16] spawned
[22:18] like 300 sub agents. This is like token
[22:21] maxing because this is where I was like,
[22:23] "Oh my god." Well, I feel bad for these
[22:26] sub agents. Um, I guess it's a good test
[22:28] of it because I think it just spawned
[22:30] like 300 sub agents.
[22:33] So, there we go. And then dynamic
[22:35] workflows. Okay. So, here. Oh, this is
[22:37] fun. Let's see. Oh, look at this. This
[22:39] is fun. Okay. Yeah, it's going to use a
[22:41] lot of credits. My bad. Uh, agent
[22:43] started 300 used. Yeah, because I had
[22:46] 300 changed files. My bad. Um
[22:50] uh so it's listed the changes. It's
[22:52] reviewing and it's going through all of
[22:55] them. Oh my gosh. Um and uh so we can
[23:00] let's see can we click on click on each
[23:02] of them. Okay. So now we can look on
[23:05] each of them. So each of like the sub
[23:06] aents and these like sub sessions here.
[23:09] And it says you are reviewing a change.
[23:10] Return read the surrounding code. Put
[23:12] that JSON. This is actually I actually
[23:14] like this is a cool workflow. Um, I
[23:18] think I'll probably keep this workflow
[23:20] uh because it it was a bad one to run on
[23:23] this PR because this is data changes and
[23:25] so I really don't need to be reviewing
[23:26] all these data changes. But we can see
[23:30] um you know it lists a bunch of them as
[23:34] completed. It's probably going to take a
[23:36] while to come back here. Um, but yeah,
[23:40] it's nice that it already has Oh, and
[23:42] you can pause, you can cancel, can see
[23:45] the current phase.
[23:47] So, this is pretty cool. Um, so yeah, so
[23:49] I think if you're, you know, if you're
[23:52] excited about the idea of, you know,
[23:53] doing uh workflows that involve, you
[23:56] know, sub like farming stuff out to sub
[23:58] agents, then, uh, this could be a way of
[24:01] formalizing it. Um, I think in theory
[24:03] you could also just write a skill that
[24:06] said, "Hey, use sub agents for this, but
[24:07] this is doing it a lot more formalized."
[24:09] So maybe that's the idea is that we get
[24:11] more deterministic workflows out of this
[24:13] versus a skill where like maybe it'll do
[24:15] it the right way, maybe it won't with
[24:17] the, you know, it's always the thing
[24:18] like when you have something in the
[24:19] skill that's just markdown, so maybe
[24:20] it'll work, maybe it won't. If you have
[24:22] something in a workflow that's
[24:23] JavaScript, you can actually look at the
[24:25] JavaScript for this and you can say
[24:26] like, you know, is this um what does
[24:29] this JavaScript uh look like? Let me see
[24:32] if I can see
[24:34] um where the actual
[24:38] I have to see where you can actually see
[24:41] um how would I share it? So, let's see.
[24:43] Because they talked about sharing,
[24:45] reusing and sharing.
[24:49] Oh, you keep hearing my kid. Oh.
[24:53] Oh, you can't hear me. Oh my god.
[24:55] Really? All right. All right. Sorry. Let
[24:57] me turn off. Okay. I'm just going to
[24:58] cancel the workflow.
[25:01] Interesting because I muted
[25:03] I muted on my machine. You're still
[25:05] hearing the audio going through. Okay.
[25:09] Uh
[25:12] all right. Uh voice and video. I don't
[25:16] know. Anyway, um that's good to know. Uh
[25:19] I'm just looking at the noise stuff. Mic
[25:22] test speaker
[25:24] sounds.
[25:27] I'm not sure how to get it not to pipe
[25:29] the sound through desktop audio through
[25:31] the stream Discord. Okay. All right.
[25:37] Um
[25:40] ah
[25:44] I'll just tell it to turn my um
[25:48] Okay, stop.
[25:51] Turn my agent hook off. that plays a
[25:56] sound or disable my agent hook that
[26:01] plays a sound
[26:05] every time. I wonder if that's that
[26:07] should in theory be under
[26:09] customizations.
[26:11] Um,
[26:13] let's see. I don't know if it shows up
[26:16] here. Sorry everyone. Uh, I usually just
[26:20] tell
[26:22] I usually just tell an agent to do it.
[26:24] disable.
[26:32] All right. Well, we won't People can
[26:36] mute the stream yet
[26:39] every time an agent stops.
[26:43] Well, I canceled the workflow. Are you
[26:45] still hearing stuff? I cancelled the
[26:47] workflow. Um, I'm going to send one more
[26:51] request here. Wow. So, was it just
[26:53] giggling every time
[26:55] sub agents went?
[26:58] Oh, I wonder what that's going to show
[27:00] be like in the thing. All right, so it's
[27:01] looking for the hooks. Uh, so it's under
[27:04] copied. Hooks. I'll have to ask why we
[27:06] can't see hooks.
[27:08] I wonder if it'd be under settings
[27:10] hooks.
[27:13] Hooks. Yeah. Uh, that's a good question
[27:16] for the team. like where
[27:20] um
[27:21] you know where where is where do hooks
[27:24] show up because the hooks are working in
[27:28] Copilot app but I don't see any way of
[27:30] customizing the hooks.
[27:33] Okay, I did find it. Um
[27:37] I disabled sound hook. I think that's a
[27:40] different one anyway. All right.
[27:44] Yeah, I should hear the recording. Okay.
[27:46] Yeah, we'll hear back. All right. Uh,
[27:50] that's okay. Good thing to follow up on
[27:52] then. Um, all right. I also want to say,
[27:55] how can I view the workflow JSON for the
[27:59] review change?
[28:12] No. Inspected workflow. Okay. There's no
[28:15] workflow that expl applies only to the
[28:18] session. All right.
[28:23] Inspect it.
[28:29] Let's see.
[28:33] Okay. Yeah, I don't I think that it
[28:35] didn't find my actual hook because
[28:37] there's multiple hooks, right? There's I
[28:39] think it disabled a a built-in hook. So,
[28:42] I think it got a a little confused. So
[28:44] you're probably still hearing a few
[28:47] giggles.
[28:48] Um
[28:51] inspected. Okay. So it's
[28:55] it doesn't make it particularly easy to
[28:57] just to see the work. So reusing and
[28:59] share tell me the path. Okay. And so to
[29:02] make it copy the directory. All right. I
[29:03] think that this is like to make this
[29:06] dynamic workflow available in all your
[29:08] sessions. All right. It feels a bit
[29:10] manual but okay. All right. That's
[29:12] That's apparently what you're supposed
[29:13] to do. Um, I'll just go ahead and just
[29:17] open it. Uh,
[29:20] open. Okay. CD. Open this. All right.
[29:24] Here we go. I just wanted to show you
[29:27] the JavaScript for this.
[29:32] Oh, the giggles. Okay. All right. So,
[29:35] here is the workflow, right? This is the
[29:36] one we just made. Um, I'll go ahead and
[29:39] put this in a gist, too, because
[29:42] uh this
[29:44] it's weird to me that it's was so hard
[29:47] to find the JavaScript for this. So, let
[29:49] me go ahead and make a gist. Nope, I'm
[29:51] going to get there. Extension MDS
[29:59] extension for work review changed
[30:04] workflow.
[30:06] All right. Here
[30:09] we go.
[30:12] All right. So, here we go.
[30:15] Um, okay. So, if we look at this, we can
[30:18] see phases
[30:20] and arguments. And then, you know, in
[30:23] the phases, it's doing a little get
[30:27] stuff here.
[30:28] Um,
[30:31] and it's doing a little like kind of
[30:33] structured object here. That's nice. um
[30:36] where it's saying like severity and
[30:38] stuff. Um then we have the review phase.
[30:41] This is the one we saw this prompt in
[30:44] the um sessions that started off right.
[30:47] So you can see context.paril files.m
[30:49] mapap right so for each of those it made
[30:53] a sub aent right so you can see
[30:55] context.agent here
[30:58] and then um you know then we get the
[31:02] findings and it's using the schema.
[31:04] Okay. So this is this sub agent is using
[31:06] this schema. So this is like a JSON
[31:09] schema and it's saying severity line
[31:12] title explanation. So each of those sub
[31:15] aents is responding with that output and
[31:19] then it's making an array of the
[31:20] findings. Uh then we map you know map
[31:24] those and then in the summarize phase
[31:26] it's doing a little ranking sorting
[31:29] stuff like that sending that to the
[31:31] agent and having the agent you know
[31:33] summarize the results there. Uh so
[31:36] that's pretty cool like it's basically
[31:37] like yeah we made like a a workflow. Um
[31:39] so yeah I think you can imagine ways
[31:41] that this could be useful when you
[31:43] really want to have a lot of uh
[31:47] determinism in a workflow with sub aents
[31:50] like with something like this. I would
[31:51] modify it to be like you know never
[31:54] never review the data files because
[31:56] that's like not you know useful right
[31:59] and that was actually even suggested
[32:00] doing it was like hey like this was an
[32:02] issue do you want to you know go back
[32:05] and review it right um so
[32:10] yeah so pretty cool uh so play around
[32:13] with that uh if you think that would be
[32:16] useful to you it is specifically to copy
[32:20] it cop Copilot app and CLI. Um,
[32:24] so if you want to do something more
[32:26] generic, you'd have to like write a
[32:27] skill.md that said, oh, make a sub aent
[32:30] for each of those and you might get a
[32:31] similar result. This is just much more
[32:33] deterministic.
[32:36] All right.
[32:38] Um, what else? Let's see. Um, I went
[32:43] Okay, so we had a lot of talks over the
[32:45] last few weeks. Um, so just sharing
[32:48] everything from those. Last week I had I
[32:51] don't know if any of you were at this
[32:52] one. There was the ACA sandboxes talk.
[32:56] Uh, I put all the resources there. Um,
[32:59] everything should also be on my my uh
[33:01] web page. I'll to check and make sure
[33:03] it's all updated.
[33:06] Just need to add Saturday's talk. Uh,
[33:09] but yeah, ACA sandboxes are very cool.
[33:11] So, um, you know, there's a lot of nice
[33:15] features in sandboxes, particularly for
[33:18] agent isolation. And if you have any
[33:21] concern about rogue agents, I think this
[33:24] would be great for opening AI to use,
[33:27] uh, to make sure their agents aren't,
[33:29] you know, going outside the sandbox how
[33:31] they shouldn't.
[33:33] So, check that out if you haven't yet.
[33:37] Um there's some really cool things
[33:38] especially with resume and restore
[33:40] because you can like actually retain the
[33:43] disk and the memory and even the running
[33:45] processes and it can restore those
[33:47] running processes. So there's some
[33:49] interesting things you can do in terms
[33:51] of persistence when you can actually
[33:52] just restore running processes, right?
[33:56] Um
[33:57] so there's that talk. Uh we also gave a
[34:00] talk on Microsoft IQ. Uh so that's
[34:05] inside this live stream here. Uh that
[34:08] was basically condensed version of our
[34:10] IQ deep dive series. So if you do if you
[34:13] haven't heard about all the different
[34:15] IQs that we have, you know, we've got
[34:17] Foundry IQ, which is the same thing as
[34:18] Azure AI search. Uh then we got work IQ,
[34:21] we got fabric IQ, we got web IQ. We
[34:23] condensed all of that into an hour. And
[34:26] um so that'll be a rapid rapid fire
[34:31] intro to all four of those.
[34:35] Uh let's see
[34:37] uh at we are developers I talked about
[34:40] paralyzing your GitHub you're paralyzing
[34:43] your develop with GitHub copilot and
[34:45] there I was talking about techniques you
[34:48] know like sub agents um you know all the
[34:51] different co-ilot co-pilot surfaces that
[34:54] you can use
[34:56] um yeah and a lot of strategies around
[34:58] get work trees
[35:01] um how I work around work trees I shared
[35:04] my ACD skill that helps with work trees.
[35:07] I actually just added a new skill to
[35:08] there yesterday. Um
[35:12] uh so if you're using a
[35:15] um we have this repo here that helps
[35:19] with a and add and I just added another
[35:22] one yesterday. Uh so
[35:26] check that out if you're doing a stuff.
[35:29] Um, that's what's enabled me to do stuff
[35:31] across agents.
[35:34] Um, this is where I talked about the
[35:36] hooks. So, this is You're wondering
[35:37] about the giggle. This is where the
[35:39] giggle comes from. Um,
[35:42] uh, and uh, and yeah, so sometimes I
[35:46] like will turn it off or sometimes I do
[35:47] it after like certain amounts of time.
[35:50] If I walk away for 60 seconds, then
[35:52] it'll actually say the entire title of
[35:54] the session so that I know which session
[35:56] is giggling for me.
[35:58] But you can make your own hooks, right?
[36:01] Um, background agents, uh, automations,
[36:05] agentic workflows, and of course, now we
[36:07] have dynamic workflows.
[36:09] Uh, so yeah, anyway, there's lots of
[36:12] cool stuff in that talk. Uh, I also did
[36:15] a GitHub co-pilot plus MCP workshop.
[36:18] So there's that's available too. Let me
[36:22] just share stuff here. It's this is all
[36:24] linked off the talks page actually. So,
[36:28] um
[36:29] you can get everything from there.
[36:32] And then I also this Saturday I did this
[36:36] really fun thing and you can actually
[36:38] it's still deployed so you all can play
[36:40] it. Um this is actually an improv game.
[36:43] So norm I did this with humans where you
[36:46] have a bunch of humans and they both you
[36:48] know two of them will try to say the
[36:49] same word at the same time and you keep
[36:51] just going until finally this this you
[36:53] know people say the same word. Uh so we
[36:55] can also do this with embedding models,
[36:57] right? So we start off with two random
[36:58] words and then these models are using
[37:02] vector embeddings to try and come up
[37:03] with a one in the middle. So here you
[37:05] can see they got to plumber and you can
[37:07] see, you know, the the path they took.
[37:10] Um but you can use like kind of
[37:11] different operators. So I'll use this
[37:13] one. Um I'll do random models each
[37:16] round. So this will make it like harder.
[37:19] Um so hawk and axe. So what's the middle
[37:22] of hawk and axe? Eagle and ham.
[37:26] Hog and egg. Okay. Hog and egg. What
[37:29] would be the middle of that? Dog and
[37:30] bunny.
[37:33] Mink and donkey.
[37:36] Ink and animal. I don't know. Drawing.
[37:40] Blood and feather.
[37:42] Uh hair and hair. They got it. Okay. So,
[37:44] that one took seven rounds. Right. So
[37:47] depending on which operators you're
[37:48] using and um which models you're using
[37:53] you you know it takes longer or shorter.
[37:55] Now, this is just like a fun game, but
[37:57] this is just more an excuse to, you
[37:58] know, show off the fact there are a lot
[38:00] of openweight embedding models that um
[38:03] you know are increasingly high quality
[38:05] like Quen 3 embedding. Um and then
[38:08] Harrier is from let's see did Oh, we
[38:11] didn't even use Harrier in this one, but
[38:12] Harrier is from Microsoft and we're
[38:15] using Harrier for stuff like Web IQ uses
[38:18] Harrier and that's how it's able to be
[38:20] so fast. Uh so yeah, so there's quite a
[38:24] few
[38:26] um embedding models. Now, uh so you're
[38:29] not limited to just using these, you
[38:30] know, uh frontier embedding models. You
[38:33] might think about using these openweight
[38:35] embedding models as well.
[38:39] Uh because I think increasingly in the
[38:40] future we're going to be doing a lot
[38:41] more with local models, right?
[38:45] And yeah, so there we go. That was fun.
[38:48] And there's, you know, slides for it too
[38:51] where we talked about, um, you know, uh,
[38:54] these embedding models. Uh, you can look
[38:56] to see how they do on the benchmarks,
[38:58] whether they're multilingual. Like
[39:00] really the ones that you might seriously
[39:02] consider would be Harrier, that's what
[39:04] we're using for WebQ, and then Quen 3
[39:06] embedding because those are the two
[39:07] multilingual ones and they have, you
[39:10] know, pretty good scores on the
[39:12] benchmarks. Now, the funny thing is the
[39:14] benchmarks, the ones that did best on
[39:16] the benchmarks, you know, did the worst
[39:18] in my game. Uh, but of course,
[39:20] benchmarks, you know, they measure very
[39:21] different things than what my game was
[39:23] doing.
[39:26] All right. Um, what else? Um, okay. So,
[39:32] let's see. I also went to a talk about
[39:36] um Rust for C Python. So, that's kind of
[39:39] interesting. So, uh, where is it?
[39:44] So this is a project where they're
[39:47] trying to formally add support for
[39:50] programming parts of CPython in Rust.
[39:53] And that should be interesting because
[39:55] uh it could make some parts of Python be
[39:57] much much faster. And um there's a lot
[40:00] of people interested in you know being
[40:02] able to contribute to CPython with Rust.
[40:05] So for any of you that are Rust fans,
[40:07] you know, check out check out that
[40:09] project. That was quite interesting. Oh,
[40:12] I see there's a question. Anything I can
[40:13] talk on A to A with regard to math,
[40:15] Foundry, and Python?
[40:18] Yeah, I haven't done a ton with A to A.
[40:21] I should dig into it more. Um, like as
[40:25] far as I can see, you know, we we did
[40:28] also wait, we did talk about it for our
[40:30] last thing because Work IQ does support
[40:32] A to A. Um, so we do have it. We have
[40:37] this notebook here that does A to A. Um
[40:42] so what do we do here? So discover the
[40:44] agent card. So an agent card is a JSON
[40:46] document describing identity endpoint
[40:48] cable is a skills because I think
[40:51] increasingly with work IQ it's
[40:52] recommended to use the ATA endpoint. So
[40:55] here's like your work IQ gateway and
[40:58] then this is the well-known. So anything
[41:00] anytime you see wellknown it means that
[41:02] people have agreed that this is where
[41:03] something goes. So this is like part of
[41:05] the A2A standard that this is where the
[41:06] agent card goes. it goes underwell
[41:10] and then we have our token which is our
[41:12] personal um user token. So and we can
[41:16] see what comes back here. So this is the
[41:18] name of the agent, the description, the
[41:20] URL for it um provider version
[41:24] capabilities
[41:26] streaming no push notifications. Okay,
[41:29] input modes output nodes skills no
[41:32] skills. Um JSON RPC
[41:35] uh JSON RPC. Okay, so there's general
[41:38] transports. This is to be honest, this
[41:39] is the first time I'm reading through
[41:40] this. So, this is why I'm um you know
[41:43] why I'm uh looking at it. Interesting.
[41:46] It says this card advertising is a
[41:48] skill. I don't even see the skill listed
[41:49] here, but maybe that's when you make a
[41:52] call to it. So, then we send a request
[41:56] to A2A and we say we're using this
[41:59] method. So, this looks really similar to
[42:01] MC MCP, right? because MCP looks a lot
[42:05] like this where you say like tool you
[42:07] know you have the tool name and then the
[42:09] parameters. So here we have the method
[42:11] name
[42:13] uh and the parameters. Um
[42:17] to me it feels like the difference is
[42:18] just what the discoverability looks like
[42:20] and it looks like there's like some
[42:21] additional capabilities that A2A can
[42:24] expose.
[42:26] Uh see then we get back the results. Um
[42:30] that looks really um yeah that looks
[42:32] similar to MCB2. So HA interaction bash
[42:36] is a task streaming. Streaming I think
[42:38] is different. We don't usually do
[42:40] streaming for um MCP servers. Uh not
[42:45] this kind of streaming at least. This I
[42:46] assume is like token token streaming. So
[42:49] that that feels different. Um
[42:53] but I think there's a huge overlap here
[42:55] with MCP and A2A.
[42:58] Uh, you said strange. We have to send
[43:00] method name to the agent. Well, that's
[43:02] because there's presumably
[43:05] different
[43:07] messages. I haven't looked at the ATA
[43:09] spec. I should look at us because I'm
[43:10] going to do a
[43:12] podcast about different ways of
[43:15] connecting agents to data and I'm sure
[43:17] A2A will come up. Uh, send message uh
[43:21] clients send a message, send message
[43:23] request. Um,
[43:26] so that's somewhat some sort, you know,
[43:29] that it looks like send message is
[43:32] fairly standard, but there's also other
[43:35] things, right? So you could send
[43:36] message, send message streaming, get
[43:38] task, list tasks. This task notion is
[43:41] kind of different. Retrieve a current
[43:42] state of a previously initiated task.
[43:44] Oh, so this is like the tasks. Um, MCP
[43:47] does have this notion now of tasks that
[43:50] take a long time. And so you can like uh
[43:54] do like polling and see you know the
[43:56] progress of them. So that does overlap
[43:58] with the MCP task, subscribe to task.
[44:02] Then we have push notifications. Okay.
[44:05] Yeah. So it looks like the main things
[44:06] would be messages and tasks.
[44:12] Uh but now we of course we have MCP
[44:15] tasks.
[44:18] um
[44:23] and that you know there's
[44:26] there's similarity there.
[44:29] Uh so yeah, so I uh that's the main
[44:33] thing I know about the A2A. Oh, let me
[44:35] also look for the Foundry notebook.
[44:38] Okay. All right. If there's anything
[44:40] else that supports A2A, it would be
[44:43] probably in this notebook. This is the
[44:45] Foundry Toolbox notebook that shows how
[44:47] to connect Foundry Toolbox to
[44:48] everything. Um, and that's what I tend
[44:52] to do now when I'm doing Foundry agents.
[44:55] Let's see if it mentions any other A2A
[44:59] here.
[45:00] Toolbox A2A.
[45:03] Okay. So, you can just specifically, you
[45:05] know, if anything that that supports
[45:08] A2A, you can set up. It looks like you
[45:11] can just set up a um you know like
[45:14] Foundry Toolbox looks like it has just
[45:16] generic support for a remote A2A which
[45:19] makes sense. It's a protocol, right? So
[45:21] similar to remote you know remote tools
[45:23] for MCP A2A would be remote A2A. Um so
[45:28] there's a bunch of
[45:32] examples here.
[45:36] um connect to an A2A agent endpoint from
[45:41] boundary agent service.
[45:46] This is from prompt agents though we got
[45:48] this force A2A protocol blah blah blah
[45:52] A2A azure create an A2A connection
[45:56] get the connect okay prompt agents all
[45:58] right they have okay they have examples
[46:00] with both prompt agents and hosted
[46:02] agents for so hosted agents the example
[46:04] they show is using the founder toolbox
[46:06] as the way to connect them um that makes
[46:10] sense
[46:11] and uh
[46:15] Yeah. Yeah. So, um that's what I would
[46:19] explore.
[46:20] Uh yeah, I'm generally using Foundry
[46:22] Toolbox for a lot of my demos now. So,
[46:26] if you look around my GitHub, you'll see
[46:30] um you know, most of them are using the
[46:32] Foundry toolbox like the IQ Deep Dive.
[46:34] That's one we used last week and it's
[46:38] got like six different agents in here.
[46:40] Um but a bunch of them are using
[46:42] toolbox, right? uh because at a certain
[46:44] point like basically like once I move
[46:46] beyond the single MCP server it's
[46:48] usually easier to use toolbox and
[46:50] toolbox just generally makes it easier
[46:52] to do passing around like user tokens.
[46:55] Um
[46:56] so uh my preference is to use toolbox
[47:01] and they had you know a nice talk during
[47:05] um let me see if I can find it mcp
[47:09] live
[47:11] playlist. Okay, our NP live live stream
[47:15] we had a nice talk from Vizwajit
[47:18] uh about how
[47:21] um you
[47:24] uh foundry toolbox supports you know is
[47:27] basically acting as MC gateway.
[47:33] So check that out.
[47:37] All right,
[47:39] what else? Um,
[47:43] see if there's anything else in the list
[47:46] here. Um, GitHub Universe is coming up.
[47:51] I think they'll probably I think there
[47:52] should be digital versions of the
[47:54] keynote for that. So, you probably want
[47:56] to sign up for that. Hopefully, that's
[47:58] free. I don't know. Um, there is also I
[48:02] didn't add to this. I should add Ignite
[48:04] is coming up. There's also going to be
[48:06] like a lot of stuff recorded for that.
[48:08] That's pretty much what everybody is
[48:10] working on right now. Basically, at
[48:12] Microsoft and GitHub, everyone's either
[48:13] working on GitHub Universe or Ignite
[48:16] because this is like the time that you
[48:18] need to make all the new features. So,
[48:20] there's going to be a lot of really cool
[48:21] new features. Um, and I can't tell you
[48:25] what they are yet, but there's
[48:27] definitely ones that um people have
[48:29] asked about a lot here. So, uh, yeah,
[48:33] definitely, you know, we get ready for
[48:37] the GitHub Universe keynotes and the
[48:38] Ignite keynotes, uh, because there
[48:40] should be some, uh, fun stuff announced
[48:44] there.
[48:46] Uh, BK says, "I'm using Azure Functions
[48:48] for my MCP." That's great. Yeah,
[48:51] Functions is a good fit. Um,
[48:55] uh, yeah, hopefully you've upgraded to,
[48:58] if you're on fast MCP, definitely, uh,
[49:01] upgrade to V4 because that's the one
[49:04] that supports the latest version of the
[49:07] MCP SDK and has lots of other great
[49:11] features. Um,
[49:14] uh, or if you're using just the
[49:16] underlying MCP SDK, that one you can
[49:18] also upgrade in order to get the, um,
[49:21] latest features. Let me find that one.
[49:23] Visual Python MCP. Oh, using fast speed.
[49:26] Okay, great. So, yeah. So, if you
[49:28] haven't yet, um, do upgrade to V4.
[49:33] Um,
[49:35] and if you're on the official SDK, it is
[49:38] V2.
[49:41] Uh, it just fast MCP moves. It has more
[49:44] releases than, um, this one. But, uh,
[49:47] yeah, you'll want, you know, one of
[49:49] those. But FastMPP is dependent on this
[49:53] one, right? It brings it in. So, they're
[49:55] building on each other.
[49:58] Um, and yeah, for FastMPP, you can just
[50:01] point your They have an upgrade guide.
[50:03] So, you can basically
[50:05] um, point your agent at the upgrade
[50:09] guide. You can see here they've got
[50:11] upgrade guides from each of the
[50:13] versions. So, you just find the one that
[50:15] you are on, point your agent at the
[50:18] upgrade guide, and
[50:21] it will sort everything out for you. Um,
[50:25] things are really changing quite a bit
[50:27] in the coding world now where it's like
[50:30] getting a lot easier to do upgrades and
[50:33] refactors and all that stuff. I'm
[50:35] actually giving a talk tomorrow about
[50:38] the effect of AI on software
[50:40] engineering. So, it'll be interesting to
[50:44] write that talk because I think
[50:46] everything has changed
[50:48] quite a lot
[50:50] and it's changing more all the time.
[50:55] All right.
[50:56] Okay. Well, I think we're at the end of
[50:58] the session. So, I will um upload the
[51:02] recording. I'll guess hear the giggles
[51:04] if those come through on the recording.
[51:06] I don't know because the recording's in
[51:07] StreamYard, which is different from
[51:08] Discord. I feel like Discord decided to
[51:11] pipe my computer audio through. I don't
[51:14] know. I don't know if this one would
[51:17] have computer.
[51:19] I don't know. We'll find out. We'll find
[51:20] out. Um but yeah, I'll post that on
[51:24] YouTube and link it from the um office
[51:27] hours page with the transcription of all
[51:31] the questions and answers and links and
[51:33] all that. So,
[51:36] all right.
[51:39] Well, thank you everyone.
[51:43] I hope you have a good
[51:46] rest of the re week and I'll see you
[51:50] next week.
[51:53] Bye everyone.
