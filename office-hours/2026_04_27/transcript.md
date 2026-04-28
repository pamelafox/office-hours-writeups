[00:01] Okay, welcome everyone. So, see lots of
[00:04] people in the audience. We don't see
[00:05] questions yet, but I know there was a
[00:07] ton of questions in the chat. Um, I'm
[00:10] going to start writing notes about
[00:11] things actually. So, we had that. Okay,
[00:13] so we had foundry memory was a question
[00:16] and also just other memory integration.
[00:19] Um, we had the question about regional
[00:22] availability.
[00:26] Um, so
[00:28] what else do we have? Okay. So, Pablo,
[00:30] great. Um, good question. In which
[00:32] cases, in which cases would it be better
[00:34] to deploy the agents as host agents? In
[00:37] which cases using other Azure computing
[00:39] resources?
[00:41] Um, so to me like the advantage of
[00:44] deploying as hosted agents is um is
[00:48] actually the evaluation, right? So,
[00:49] that's what we're doing like in in day
[00:51] three um is doing the evaluation. Uh, so
[00:54] it's, you know, it's just easier to set
[00:57] up the scheduled evaluation and the
[00:59] online evaluation, continuous
[01:01] evaluation, the evaluation alerts.
[01:03] That's just way easier when it's on a
[01:06] hosted agent platform. Um, so that to me
[01:09] is that that to me is the for me
[01:10] personally, that's the number one
[01:11] advantage. Um there's other advantages
[01:13] too like maybe you like having it all
[01:15] inside this founder UI like for people
[01:17] being able to just like you know um
[01:20] having this this playground like that
[01:21] might be useful you know depending on
[01:23] your organization and how it works like
[01:25] making it easier for other people to um
[01:28] you know interact you know with with
[01:30] everything here and having the
[01:31] playground and the traces and everything
[01:33] um you know just in one location. So
[01:35] that might be advantage. Um but to me
[01:38] the number one advantage is the the ease
[01:41] of setting up evaluation on the live
[01:43] traces and that would be s to
[01:47] significant effort to set up if you were
[01:49] doing it uh on your own computing
[01:51] platform.
[01:53] Um, so yeah. Uh, and I think also like
[01:56] what you should do is if you've got
[01:58] something right now that's on container
[01:59] apps, you can try deploying it on the
[02:02] agent platform and seeing like maybe
[02:04] like do some tests, right? Do some
[02:06] performance tests. Uh, you also this is
[02:08] all like public preview right now,
[02:09] right? So you probably if if you're in
[02:11] production right now on container apps,
[02:12] you probably want to stay in production
[02:13] on container apps and wait um to go into
[02:17] production on this. Um, but you can test
[02:18] it out and I would set up do some
[02:21] performance tests and some load testing.
[02:23] Like I do actually have um a locust file
[02:26] that I was using for load testing and I
[02:29] did actually find uh various issues that
[02:31] I'm reporting to the hosted agents team
[02:34] um uh with um you know when I I because
[02:37] I sent it like thousand I sent them
[02:39] thousands and thousands of requests over
[02:41] a couple hours with my load test because
[02:43] I was doing quite a lot of load testing.
[02:46] Yeah. So, you know, try it out. Um, see
[02:49] if it works. Uh, you know, take
[02:50] advantage of the like it would only make
[02:53] sense if you're like really taking
[02:54] advantage of the things like the
[02:56] evaluation and um, and I guess also
[02:59] that, you know, there is this that this
[03:00] new microVM platform and you might find
[03:02] that you like the performance of that.
[03:06] Um, okay, the question is are the
[03:08] foundry evaluations kept in our tenant?
[03:10] That's an important topic in Europe.
[03:12] That is a good question. Let me follow
[03:14] my link to evaluations and red teaming.
[03:18] Um
[03:20] so it like it is a per region thing
[03:22] because right now I'm that's why I'm
[03:24] using um North Central
[03:28] US. Um because I needed it for that. Uh
[03:31] but the question is let's see bring your
[03:35] own storage. Uh you so because it is
[03:38] it's it is storing behind the scenes but
[03:41] I believe the storage would be okay. So
[03:43] you probably want wait transparency
[03:45] note. What is a transparency note? No.
[03:48] Um
[03:51] yeah I I'm not a lawyer so I don't want
[03:53] to tell you exactly. So it's it's
[03:55] certainly a per region thing and it does
[03:58] create storage. Um, so if you wanted to
[04:02] be really certain,
[04:05] I was hoping there'd be a note that said
[04:06] that the storage is in the region. I
[04:08] would assume the storage is in the
[04:09] region. Um,
[04:12] but if you wanted to be very safe, then
[04:13] you could use you could bring your own
[04:15] storage, right? And that I presume would
[04:17] um make, you know, make your um
[04:20] organization happier. Uh so I would look
[04:23] I would look through these docs and see
[04:25] and if it's not clear um then
[04:30] yeah just uh you know just let me know.
[04:33] Let me let me also just make a note of
[04:34] this too. Um
[04:36] uh are eval stored
[04:40] in the tenant?
[04:45] Uh but if you bring if you make your own
[04:47] bring your own storage container then
[04:48] the answer would be yes. Right.
[04:51] Okay. Um, so we have this question. Do
[04:53] you get more customizable orchestration
[04:56] with hosted agents? Um, well, as
[04:59] compared to prompt agents, yes, if you
[05:01] were using prompt agents before, um,
[05:04] right, if we go back to the foundry
[05:05] slide, okay, so prompt agents, so let's
[05:08] say if you were using prompt agents
[05:09] before, those were quite limited, right?
[05:11] you could only do, you know, any
[05:13] whatever you could do in the SDK, which
[05:14] was like, oh, here's here's my
[05:16] instructions and here's my tools and,
[05:19] you know, and and there wasn't much you
[05:21] could do on that. Um, I guess we had
[05:24] like a a workflow mechanism in the
[05:27] foundry portal, but don't use that. Um,
[05:31] so definitely compared to prompt agents
[05:33] because now you can bring your own
[05:34] framework, right? So as saying with
[05:35] Microsoft agent framework, you can build
[05:38] you know very complex workflows with
[05:39] that and you just wrap that as an agent
[05:41] and in the responses host server and
[05:42] boom you've got a hosted agent. So um
[05:45] yeah so I would say yes compared to
[05:47] prompt agents. Um but the foundry agent
[05:51] service platform itself it's not really
[05:52] the one giving the orchestration it's
[05:54] the agent framework that's giving the
[05:56] orchestration. Right? So it depends can
[05:58] you do that orchestration in agent
[05:59] framework? Can you do it in link chain
[06:00] or pantic AI or whatever right? So it's
[06:02] the agent framework doing the
[06:03] orchestration. So yes, you can have more
[06:05] orchestration only because your agent
[06:07] framework can do it.
[06:09] Callian asked, is this the same as
[06:10] hosted agents and found a agent service?
[06:12] Yes. Um but this is we're using the new
[06:14] version that came out last week that is
[06:16] running on a faster microVM platform and
[06:20] has this different like slightly
[06:22] different SDK.
[06:25] Um so Wedi asks, can you connect the
[06:27] agents with external MSP tools using
[06:29] agent platform? uh maybe you could
[06:33] clarify what you mean by agent platform
[06:35] if that's a specific thing. Um but
[06:37] generally what I did show today is we
[06:38] showed multiple um MCP connections. So
[06:42] let me actually show the stage 4 the
[06:45] full code.
[06:47] Um okay so here we have the agent and
[06:50] it's pointing at two different MCB
[06:52] tools. Um, so one thing I glazed over
[06:56] during the live stream is that there is
[06:58] currently a bug with the Foundry toolbox
[07:01] where when deployed it doesn't work with
[07:04] MCP tools. Um, they are hot fixing it
[07:08] right now and they tried to get out this
[07:10] morning for me but it's not out yet. Um,
[07:12] so currently I actually am connecting
[07:15] multiple MCB tools to this agent. So I I
[07:18] in this in this case I'm connecting the
[07:20] um knowledgebased tool separately from
[07:23] the toolbox tool. So this one is giving
[07:25] me web search and code interpreter and
[07:27] then this one is giving me the
[07:28] knowledgebased retrieval tool. Uh so
[07:31] yeah so this shows already we've got two
[07:33] different uh MCP servers here and you
[07:36] could add any MCP server. Um you just
[07:38] have to you know pass in the O. Uh in
[07:40] this case I in order to do the O I set
[07:42] up a whole uh client that can do uh can
[07:47] do the O for each of them correctly. Um
[07:53] uh but um you know however you want to
[07:55] do the O whether it's a key or ent or
[07:57] whatever uh you can point an agent
[08:00] framework agent at at that tool.
[08:06] Um okay. All right. So next question. So
[08:10] Shandra Sakar asked how do you decide a
[08:13] model from foundry to create queries by
[08:15] the agent and get the data from DB? Are
[08:17] you asking how do you pick a model like
[08:19] for a particular use case? Are you
[08:20] trying to get one particular for like NL
[08:23] to SQL? Like can you give them more info
[08:25] on your question?
[08:27] Let's see. Pablo asks how does safety
[08:30] play a role in using the web search tool
[08:32] regarding prompt injection? Um well, so
[08:37] first of all, in terms of safety, I
[08:38] didn't talk about safety and I should
[08:40] have. Um so in terms of safety, we've
[08:43] got all the Foundry guard rails. Let's
[08:44] see. Is Foundry working now? It seemed
[08:46] like it was having some issues earlier
[08:48] today. Um but remember everything is
[08:50] going through the um you know, I'm using
[08:53] an LLM uh that's on Azure OpenI. So that
[08:56] means everything's going through the
[08:58] Foundry safety filter system. Um and I
[09:02] was hoping let's see. Yeah, can I
[09:04] operate? So if we go to the operate tab
[09:06] and we go to
[09:09] is it going to be compliance now?
[09:11] Guardrails. Okay. Policies guardrails.
[09:13] Okay. Guard rails.
[09:15] Um so guardrails is where you can create
[09:19] new um new filters. Uh all right. Let me
[09:25] go. Let's see does
[09:27] how is
[09:30] how is this working today? Discover.
[09:32] Okay. Build. Let's go to build. Okay.
[09:35] All right. Guard rails. All right. Build
[09:37] also has a guardrails tab. Uh I'm still
[09:39] getting used to the new foundry because
[09:40] it has all these tabs up here. Yeah.
[09:42] Yeah. All right. This is this is this is
[09:44] my problem. This is not Azure's problem.
[09:46] This is my problem. Um my computer
[09:51] can't log into Azure right now. Okay.
[09:54] All right. Um so,
[09:57] uh yeah. So anyway, there's there's
[09:59] guardrails, right, which are the
[10:00] policies. And so they check, you know,
[10:02] they'll check for stuff like um you
[10:05] know, jailbreak detection, indirect
[10:07] jailbreak detection, um hate, violence,
[10:10] sexual, self harm, all that stuff. Uh
[10:13] and by default, they all the block is on
[10:15] medium level, but you can increase the
[10:17] amount of blocking. You can turn things
[10:18] on or off. So you can turn on um you
[10:21] know, more jailbreak detection. So
[10:23] generally, I've had a hard time, you
[10:25] know, trying to doing any any sort of
[10:28] injection. Um so you know so that's my
[10:31] first response would be that everything
[10:33] all of these calls are going through a
[10:35] foundry model which is protected by the
[10:37] foundry guard rails um which uh let me
[10:40] you know it's an RAI policy um which you
[10:45] can you can turn things on and off um as
[10:48] for web search particularly are you so
[10:50] you that what you're asking about there
[10:52] is uh let me find it it's called content
[10:54] safety indirect
[10:57] attack detection That's what it is. Um
[11:00] for web search. Okay. So now are we
[11:02] calling it prompt shields? Okay. Sure.
[11:04] All right. Uh so this one. Okay. So an
[11:10] indirect attack is the attacker attempts
[11:12] to embed instructions and grounded data
[11:13] provided by the user. Um so for example,
[11:16] if a website had some prompt injection
[11:18] in it, right? Um, so what you want to do
[11:21] is make sure that in your filter that's
[11:25] on the model, you should make sure you
[11:26] have indirect attack enabled. Uh, I
[11:29] don't know that it's enabled by default
[11:31] right now because not everybody needs it
[11:33] because not everybody is doing
[11:34] grounding. Um, so what I would say is,
[11:38] um, and I could even add this to the
[11:39] bicep. Let me see if I have the bicep
[11:41] for it right now. Safety.
[11:44] Safety. Um
[11:49] um
[11:52] okay. All right. I can't remember which
[11:54] one I had it in. Okay. Um so what we can
[11:57] do is create a new filter that had has
[12:02] indirect attack enabled.
[12:04] And that is what you'd want to do. So we
[12:06] should probably actually do that in the
[12:08] repo itself. All right. Let me add a
[12:09] to-do. We're gonna have so many to-dos.
[12:11] All right. make a custom REI policy that
[12:15] enables indirect attack detection. Okay.
[12:20] All right. Uh and let me link link to
[12:22] this as well.
[12:24] So I think that direct jailbreak attacks
[12:27] are always enabled but not indirect
[12:28] attacks. So that's why you'd want to if
[12:30] you're doing any sort of rag or web
[12:31] search, you would want to make sure that
[12:34] indirect uh attacks, you know, document
[12:36] attacks, whatever you want to call them,
[12:38] that those are enabled in the filter.
[12:40] Um,
[12:43] good question. Okay. All right. So,
[12:45] Anorag asks, "Is there something similar
[12:48] to code mode in agent framework or can
[12:50] you use pedantic monte?" Uh, so, okay,
[12:53] good question. Code mode. So, code mode
[12:55] is for um MCP as I well, as I think of
[12:59] code mode, code mode is a a way of using
[13:02] um MCP servers. Um, so what you might
[13:05] want to do is just use pedantic AI with
[13:08] pedantic monty. I haven't tried
[13:10] combining pedantic monty with agent
[13:11] framework itself. I don't think so I
[13:14] think that um and we're actually
[13:16] chatting with the pedantic guy folks.
[13:17] Let me just check my Twitter to see if
[13:19] they've implemented it. They they were
[13:20] talking about making it like super easy
[13:22] to deploy to Foundry hosted. Um so let's
[13:25] see. So where's Pedantic? Um
[13:28] so I think they added like specific
[13:30] support. Yeah, they did.
[13:32] Uh
[13:34] wraps your single tools in a code mode
[13:36] powered by a mounty signbox. So, I would
[13:38] say like if that's what you want, you
[13:39] probably just want to use pedantic AI.
[13:41] And then let's see if they've uh Okay.
[13:44] All right. I don't see any updates, but
[13:45] they are. So, these are this is the
[13:47] Pantic AI maintainers, Marcelo and
[13:50] Samuel. Um, and it said April 24th. Give
[13:54] us a few days. It's been a few days.
[13:56] We'll follow up be like, hey, did you do
[13:58] it yet? U I know some people have
[14:01] already deployed pantic AI to foundry
[14:04] hosted agent service but using the
[14:06] invocations protocol which that's the
[14:08] easiest way to do something because
[14:09] that's just an HP endpoint. The issue is
[14:11] if you want the responses API adapter
[14:13] then you have to write your own adapter
[14:15] and so I'm hoping that maybe paid AI
[14:18] will do that for us. Um because it is a
[14:21] a a bit of effort to write your own
[14:23] responses API adapter. I don't think you
[14:25] want to do that willy-nilly. So I would
[14:27] say you probably want to use
[14:30] pedantic AI um because I don't know that
[14:33] we have that in agent framework. Um and
[14:36] you could start with invocations
[14:39] uh like somebody who did it they
[14:40] deployed with invocations and then they
[14:41] used the agui on top um for the
[14:45] invocations protocol. So that would be
[14:47] an option. Uh let me just uh Okay. All
[14:51] right. Great questions everywhere. Uh
[14:54] let's see. What would be an efficient
[14:55] way to automatically analyze traces and
[14:58] logs? Um, I'm assuming you're analyzing
[15:01] kind of from the like evaluation
[15:03] perspective, like seeing, you know,
[15:05] things going wrong. Uh, that's a good
[15:07] question. Maybe I don't know if Gwen's
[15:09] here if Gwen's used like the Azure
[15:10] skills um yet because you could there's
[15:15] I can imagine lots of things you could
[15:16] do, right? Um, you could, you know, you
[15:19] can use Azure skills to to bring in the
[15:21] logs and, you know, look for errors. Um
[15:24] because you really want to look at
[15:26] errors, right? So here do I have errors?
[15:28] Right? So um you know so you could use
[15:31] you can also just ask um you know GitHub
[15:33] copilot like hey like you know query
[15:36] everything's going to reload on me. Okay
[15:39] you could you could tell GitHub copilot
[15:41] like hey please um you know grab all
[15:44] these logs. Let me get to the hotel one.
[15:46] Okay you know grab grab all these log
[15:48] you know look through error logs and you
[15:51] know find the top errors and report
[15:53] them. Uh I spent a lot of time with
[15:55] GitHub copilot having it look through
[15:57] errors and coming up with like and I'd
[15:59] ask copilot like okay is this an error
[16:01] with my code is this an error with the
[16:03] platform like who is it an error with
[16:04] right and then if it really really
[16:06] thinks it's an error with you know no
[16:08] with an SDK or with a platform then I
[16:10] ask it to write you know a very good
[16:12] report but I like when you're looking at
[16:14] errors you do want to push back a lot um
[16:17] because it's very easy for the LLM to
[16:20] say like oh like it's not our fault or
[16:23] you know something else is going wrong.
[16:24] So you want to like really go back and
[16:26] forth a lot when you're when you're
[16:28] debugging errors and trying to figure
[16:29] out if some error in the logs like what
[16:31] it's really coming from. Um but I do
[16:33] find it helpful. So uh sometimes I have
[16:34] it write custoto queries uh custo
[16:37] queries like in app insights um and
[16:39] it'll execute those using the I think
[16:41] it's the a monitor command. Um so yeah
[16:45] uh but you could also try as your skills
[16:47] and see if there's something there. But
[16:48] you know um you've got some options.
[16:51] It's a good question. I haven't done
[16:53] that a ton.
[16:55] Let's see. Does hosted agent support?
[16:57] So, Kion's question. Does hosted agent
[16:59] support per agent identity and is there
[17:01] VNET support? Great questions. Okay. So,
[17:03] first of all, yes, the agent has its own
[17:05] identity and you can actually um I
[17:07] happen to have the code for pulling that
[17:09] out if you need it. So, because normally
[17:11] you shouldn't have to need it because
[17:12] it's going to the platform. Um when you
[17:14] do a to deploy in the post- deploy
[17:16] stage, it's going to take care of uh
[17:18] assigning things to agent identity. But
[17:21] um I do have
[17:24] uh is it this one? Yeah. Um so if you
[17:28] did need to get the agents principal ID,
[17:31] you can get it using
[17:34] um this command.
[17:37] So AZDI agent show. I've asked them to
[17:41] make this easier. H sorry I forgot that
[17:45] I can't log into Azure right now. Okay.
[17:47] It's all it's it's my computer's fault.
[17:49] Okay. But anyway, this command will um
[17:52] it'll it'll give you a bunch of
[17:53] information um in JSON form. And so
[17:56] inside there, there's an instance
[17:58] identity and a principal ID. So you can
[18:00] pull that out. And then in this case um
[18:04] I was using it to assign search uh a
[18:07] search role specifically to that agent
[18:09] identity. I actually don't need this
[18:11] anymore, but I needed it um when I Well,
[18:15] now we do need it because I'm using you
[18:17] don't need it if you're using the
[18:18] Foundry toolbox. Um but if if you're s
[18:21] if you're if you're calling an Azure
[18:24] service directly from the agent
[18:29] uh and you know if you need a token for
[18:33] that agent to access the service then
[18:36] you need to specifically give that role
[18:38] to the agents principal ID. Um so you
[18:41] can follow my it's the post-eploy.shell
[18:43] script. You can follow that pattern. Uh
[18:46] I'm hoping that they make it easier to
[18:48] get the to like assign stuff to the
[18:50] principal ID in the future because
[18:52] normally I do this all in bicep. So this
[18:54] was the only time I had to use the Azure
[18:56] CLI to assign the arch ro. Um so
[19:00] hopefully that gets better. Okay. Is
[19:02] there V-Net support? There is V-Net
[19:04] support that is
[19:07] covered
[19:09] on one of these pages.
[19:13] Net virtual. Yes.
[19:16] They support deployment with network
[19:18] isolated foundry resources for
[19:20] information. C configure private
[19:23] network. So this is the docs now. You
[19:27] should try it out and see because I
[19:29] haven't I haven't gone through this
[19:31] particular doc yet. Um
[19:35] so if you need to bring your own uh I
[19:38] think I I I feel like they're already
[19:40] it's a question where they are. No.
[19:44] Okay. It does say that the ACR has to be
[19:47] reachable over public net endpoint.
[19:49] That's a bit of a shame. Okay.
[19:53] All right. So, there is VNET support.
[19:55] Um,
[19:57] you should try it out because I haven't
[19:58] personally tried it yet and I know
[20:00] things things are often interesting when
[20:02] you try it out yourself. But, um, but I
[20:04] do think that was a big thing that they
[20:05] were working on because there's so much
[20:06] desire for that.
[20:09] Let's see. Pablo asks, "If we wrap a
[20:12] workflow as an agent and it contains the
[20:14] other agents using tools, would the
[20:15] tracing still capture all internal
[20:17] information?" Um, yeah. So, if you're
[20:20] using agent framework, it just really
[20:21] depends on what agent framework is
[20:23] emitting, right? But as long as agent
[20:25] framework is emitting that. Now I guess
[20:28] what you won't get is um so when we do
[20:32] like responses host server that actually
[20:35] wraps
[20:36] it it wraps uh the agent all the it
[20:40] wraps all the calls in one more
[20:44] um parent span. So like in this
[20:46] screenshot here I think this top one
[20:48] here is actually the um the the coming
[20:53] from the responses host server. So
[20:55] that's an additional
[20:58] um span that it adds on top. Whereas
[21:00] these ones are coming from agent
[21:02] framework itself, right? Um so uh you'll
[21:07] only get so I think I would say if you
[21:09] wrap a workflow in an agent, you know,
[21:10] you're only going to get one of these
[21:12] like kind of top level parent spans. Um
[21:15] but you should be able to get all the
[21:18] rest of the spans from just from the
[21:21] fact that agent framework is
[21:22] instrumenting them, right? Uh and you
[21:25] can see in the agent, let's go to the
[21:26] agent frameworks docs just to get their
[21:31] information about what the instrument uh
[21:34] doc
[21:39] let me find observability agents. Okay,
[21:41] observability
[21:43] um spans and metrics. Okay. So this is
[21:46] everything that is that is everything
[21:49] that is emitted by um you know by this
[21:54] thing. So you know for the chat client
[21:55] and chat operations and for function
[21:57] invocation and you know agents right. So
[22:02] as long as your workflows are doing
[22:04] those you know they're doing those
[22:06] things and you should get this stuff. Um
[22:08] there might be things that your
[22:09] workflows are doing that you want
[22:11] additional instrumentation for and in
[22:13] that case you have to emit your own
[22:14] spans right and you can you can do that
[22:16] as well if you need to. Um but you know
[22:19] as long as you call enable
[22:20] instrumentation from agent framework it
[22:22] should be adding all these operations.
[22:28] Let's see.
[22:32] Okay. All right. So then the question
[22:34] from Shan Sakar was how to pick a better
[22:36] model that can query the DB. Um well
[22:39] there is this nice uh where is it? NLB
[22:42] benchmark. Uh let's see if I can find
[22:44] it. Uh I think I saved it. Let's see. Um
[22:48] there was this good blog post um that I
[22:51] was reading LLM SQL benchmark. Yeah. Um
[22:54] so this was some someone specifically
[22:57] who is interested in um NL to SQL. So um
[23:02] so I I would go I would look at this
[23:03] blog post. I thought it was quite well
[23:05] done. Um so he tried to make his own
[23:07] benchmark specific to using models to
[23:11] generate queries and um you know and you
[23:15] can you can see he says basically
[23:18] uh you know sonnet opus
[23:21] uh GLM and gro 4.1 all did well. Um did
[23:26] he not do the opening eye models at all?
[23:30] or maybe it just didn't do as well. Both
[23:31] caught, both failed.
[23:34] Um yeah, so I I would look through that.
[23:37] I mean that was he would specifically
[23:39] try to look at that particular thing of
[23:42] generating like otherwise you can look
[23:44] at you know the more generic stuff but
[23:45] it's nice if if if you have a specific
[23:47] use case in mind then ideally you you
[23:49] know would actually do some um
[23:51] evaluations or find in this case find
[23:53] the most relevant benchmark.
[23:56] Yeah, because now we have GBD 5.5 and
[23:58] they say GBD 5.5 is like basically like
[24:01] a whole like I was just reading the
[24:03] prompting guide for it this weekend.
[24:05] They're like, "Oh, it's like a whole
[24:06] other model, like a whole other level."
[24:08] Like don't think of it as just an
[24:10] incremental improvement on 5.4. Think of
[24:11] it as like a whole new model, right? And
[24:13] they have like quite a extensive
[24:16] prompting guide for GBD 5.5. So
[24:19] definitely worth um trying out um GBD
[24:23] 5.5 as well. So ideally you set up your
[24:25] own specific scenarios for what exactly
[24:28] you need and run evaluations um on the
[24:31] models uh because all of these
[24:33] benchmarks and other pieces of
[24:34] benchmarks they you know they tell you
[24:36] what they tested but that's not
[24:37] necessarily going to be what's best for
[24:39] you right that's why you want to run
[24:40] evaluations to see
[24:44] okay so let's see um
[24:50] all right so Jamor is trying to use the
[24:52] ADOM SP connections. It seems the
[24:55] functionality is not available. Is that
[24:59] when you say not available like well
[25:01] right now I don't think I can check
[25:02] anything but um as you're saying the
[25:05] tool isn't working. Can you specify what
[25:07] you mean by not available? Um let's see.
[25:10] Nambdi says I've seen a couple posts
[25:12] where people talk about having each
[25:14] agent of a multi-agent system in its own
[25:16] sandbox. Yeah, I just saw a demo of that
[25:19] a couple days ago actually too. What are
[25:21] the pros and cons of this? Um,
[25:24] I mean the the pro is that those
[25:27] sandboxes like they like it that's like
[25:29] context context window minimization to
[25:32] the extreme, right? If they're running
[25:33] in their own sandbox, then they
[25:35] definitely they both they have their own
[25:37] context window but also they have their
[25:38] own like file system. So if they were
[25:40] doing like a bunch of research or
[25:41] something like you know they they get
[25:43] their own like they could like store
[25:46] lots of files on that sandbox as they're
[25:48] doing like research and just like stuff.
[25:50] you don't have to worry about any
[25:51] collisions, right? So, if you were doing
[25:52] like a deep research agent that had like
[25:55] was using the file system for storing
[25:57] artifacts along the way, then you don't
[25:59] have to worry about any collisions at
[26:01] all because you're like, well, each of
[26:03] the sub aents is going to have its own
[26:04] sandbox, its own file system. It can do
[26:07] whatever it wants on that file system in
[26:09] order to get the answer. Right? So
[26:10] that's one benefit is that you've got
[26:11] that isolated file system. So that if
[26:13] you are using an agent that is um
[26:15] storing stuff on the file system for
[26:17] example like lang chain their deep
[26:19] agents um repo stores on the file system
[26:22] right that's the the way they um
[26:24] approach having deep agents. Uh so that
[26:27] would be you know that would be a big
[26:29] benefit. Um, and of course there's like
[26:31] it's got its own dedicated CPU and
[26:34] memory, right? So then you're you're not
[26:37] having to worry about the kind of
[26:39] performance aspects of running multiple
[26:41] agents synchronously like at you know at
[26:44] the same time. Um, so there's less
[26:47] competition there. So I think it could
[26:48] make sense for highly like tasks you
[26:51] want to like highly paralyze like really
[26:53] deep tasks tasks where you want to um
[26:56] you know have a lot of like artifact
[26:58] creation and inspection.
[27:00] Um but I wouldn't I wouldn't like jump
[27:03] for it. I would you know I would
[27:06] currently I would only go to it when
[27:08] like when you really really need it uh
[27:10] because that's takes some effort to to
[27:12] set up.
[27:14] Uh okay so let's see. Colleen asked,
[27:17] "What is the pricing criteria for hosted
[27:19] agents?" That's a great question. Um, I
[27:22] think because I think the whole
[27:24] advantage of the new platform is that
[27:26] the pricing is in fact going to be um
[27:31] based off of
[27:34] uh based off of your usage. Uh let's
[27:37] see. Hosted agents uh it's post on
[27:39] consumption of preview. No, I think this
[27:41] is I think we need new blog post.
[27:43] Where's the new blog post?
[27:50] because this one says vCPU memory.
[27:54] Is that still the way we think of it? I
[27:55] just want to find our most recent blog
[27:57] post just to double check. So, I'm going
[28:00] to check my LinkedIn.
[28:02] Uh
[28:07] I'm sure I linked it at some point.
[28:12] Where? Okay. Uh, need a refresher. Nope.
[28:16] All right, let's find that blog post.
[28:17] Where's that blog post?
[28:24] There we go. This one. Ah, I clicked the
[28:27] wrong thing. Okay. A new found this one.
[28:29] All right. So, uh, uh, so this is a new
[28:33] blog. This is the blog post that went
[28:35] out last week.
[28:39] Um,
[28:42] and where's do we talk about pricing
[28:44] here? Okay, great. So, the memory. Oh,
[28:48] that's memory. Memory. Memory is free.
[28:51] Memory is free to use. Poor June first.
[28:53] Everybody try out memory now. Oh, and
[28:54] this talks about memory. Okay. Oh, so
[28:56] that's a better answer to the memory
[28:59] question. So, Foundry memory preview as
[29:02] your in memory history. Foundry memory
[29:04] provider. Okay, cool. All right. I
[29:07] should have done that. All right. All
[29:08] right. Pricing. Pricing. Okay. Hosted
[29:10] agent billing begins April 22nd during
[29:13] preview. You pay only for active
[29:14] execution. Okay. So, here you go. I
[29:17] don't know if this is Oh, it does link
[29:20] to the pricing page. So, the pricing
[29:21] page should also be um
[29:24] correct given that this links to it, but
[29:26] we can double check.
[29:29] Um, but with the new model, so what's
[29:31] nice about the new platform as well, the
[29:33] the um that uh it it's not like it's
[29:38] only going to be running while while
[29:40] it's really being used. It's it's not
[29:42] going to just like stay alive. Um, so
[29:45] you're only paying for the active
[29:46] executions, what's really nice. Uh, so
[29:48] zero idle cost and also faster startup.
[29:52] So all of this should help with it being
[29:55] better pricing.
[29:59] Great questions. Okay. Um,
[30:05] can you publish prompt ages when you
[30:07] have public network
[30:10] in disabled? You were able to pub in
[30:12] past but not able to do it now and which
[30:15] endpoints you used to connect to an
[30:17] agent from external app. Um, so I can
[30:20] tell you for the responses API, uh, we
[30:23] have,
[30:25] uh, so I don't, well, I guess it would
[30:26] be similar for prompt agents. I I really
[30:29] haven't used prompt agents that much.
[30:31] Um, I know I know that they've been
[30:33] changing the publish tab. So, if you're
[30:34] not seeing that publish button anymore,
[30:35] it's possible that that's either a bug
[30:37] or maybe they did take it off um, of uh,
[30:41] you know, things that aren't public. Um,
[30:44] I'd have to check with the the product
[30:47] team for that. Uh so to call the you
[30:50] know call responses API or you were
[30:52] looking for the HTTP URL. So the HP URL
[30:56] is on the slide here and it is let me
[31:00] just get the slide get it. Okay. Uh so
[31:04] it looks like what you put in there. So
[31:06] dot
[31:08] um base URL slash agents
[31:13] uh
[31:16] see what you wrote. Okay, yours looks
[31:18] slightly different. Um so at least for
[31:21] the foundry hosted agents, it's slash
[31:23] agent agentamepoint protocols openi
[31:26] responses. Oh, let me get the docs for
[31:27] it. Let me get the docs. Let's get the
[31:29] docs. The docs are
[31:33] we got a lot of docs open here. Um
[31:36] uh let's get it open again. Uh
[31:43] because there is a doc about it. Um
[31:46] deploy deploy
[31:49] package and test.
[31:51] Oh no no no no. Um
[31:55] invoke the agent. Okay. This is what has
[31:58] it. So if you're invoking it. Oh no. I
[32:02] want to deploy. No. Okay, invoke the
[32:04] agent this one with the responses API.
[32:06] Okay, so it depends on whether you're
[32:08] using for hosted agents, depends on
[32:09] whether you're using um you know uh
[32:14] invocations versus responses. So this is
[32:16] the docs about how to call it. If you're
[32:19] doing prompt agents, maybe that is the
[32:21] endpoint for prompt agents. I uh I don't
[32:24] have a prompt agent example open right
[32:26] now. So, um, it it might be that prompt
[32:28] agents
[32:30] support a different endpoint,
[32:33] but you could test to see maybe they
[32:35] support both. That's the other option.
[32:36] Maybe maybe that maybe there's um, you
[32:39] know, we often have multiple endpoints
[32:42] supported at once. This would it
[32:44] wouldn't surprise me if we supported
[32:46] multiple endpoints.
[32:48] Let's see. Okay, so Pablo says in
[32:51] another Discord event it was prevented
[32:53] presented how to connect boundary agents
[32:54] with co-pilot studio agents to achieve
[32:56] that it was necessary to assign certain
[32:58] arbback changes to the hosted agent is
[33:00] there any places with typical arbback
[33:02] roles you might need for hosted agents
[33:04] so usually the addi should be the one um
[33:08] assigning the necessary arbback roles
[33:11] but as I was saying like if yeah if your
[33:13] agent need access to something else then
[33:16] um then you have to assign it. Um I only
[33:21] had to do it for that search service. So
[33:23] this was only when the agent code itself
[33:27] needed to access something. Um
[33:32] uh otherwise like things should be taken
[33:34] care of. But there are there certainly
[33:35] are a lot of roles that um you your
[33:38] bicep needs to make and uh I've been
[33:41] going through and making sure uh that I
[33:43] have all the right roles. So for example
[33:45] like recently uh let's see uh let me
[33:48] find it
[33:50] infra core AI AI project okay so uh like
[33:56] for example you do need this log
[33:58] analytics reader that role is very
[34:00] important and that's on the foundry
[34:02] project right so for the agent identity
[34:05] generally um AZD is going to deploy it's
[34:08] going to assign everything and then you
[34:09] only need to assign additional roles if
[34:11] your agent is accessing something like
[34:13] mine accessing search
[34:14] But your bicep um you know you have to
[34:17] make sure um that your bicep does have
[34:20] things for the foundry project. So it
[34:22] needs to be able to read the log
[34:24] analytics so it can show you the traces
[34:26] and it needs the Azure AI user role as
[34:29] well so it can run the projects. Um
[34:31] there's also like an ACR role that gets
[34:33] set up. Um
[34:36] yeah. Yeah. Yeah. So, I actually I don't
[34:38] know. It's a good question as to what
[34:40] are the other I don't I don't know what
[34:42] other things get assigned to the agent
[34:44] identity. Um you could probably query it
[34:47] after the fact using the Azure CLI. I
[34:50] would do it right now if I could log in.
[34:53] Um
[34:54] but you could do uh if you were
[34:56] wondering just you know use code like
[34:58] this and then instead of create you can
[35:00] do list I think and then you could check
[35:03] to see. So if you were curious um for
[35:05] with a default deployment you could uh
[35:08] afterwards you know get that principal
[35:09] ID and then use the Azure CLI and check
[35:13] what are all the roles that are assigned
[35:14] to it. Uh because I don't actually know
[35:16] it's a good question.
[35:22] Um so Nomi is it is it harder is it much
[35:26] harder to set up and you know agents and
[35:28] docker containers. I don't know. It
[35:30] sound like I think right now it sounds
[35:32] like more harder than I want it to be
[35:36] right now in terms of like yeah like
[35:38] productionizing. Uh I do think well I
[35:42] saw a demo of something that'll be a
[35:44] build that'll make it easier. So come to
[35:47] build stay tuned to build. Um, okay. So,
[35:51] Kian asks, "Can we have agent endpoints
[35:53] proxied with an API gateway and have
[35:56] policies applied at the gateway level?"
[36:00] It's a good question. I don't know.
[36:04] Uh, let's see. I haven't I don't
[36:06] particularly know about integration.
[36:09] I'm just adding to my questions list.
[36:11] Um,
[36:13] yeah, I don't know. Let's check that
[36:15] blog post because if there was anything
[36:17] I should check that blog post for
[36:18] everything. Um, let's see anything in
[36:21] the gateway. Gateway. Nope.
[36:24] Nothing on gateway. I think we Okay.
[36:31] Fancy fancy fancy. Publish. Publish.
[36:36] Oh, look. They linked to our series.
[36:37] That's so nice of them. Okay. All right.
[36:39] Um,
[36:42] uh, let's see. Is there anything on I
[36:47] don't think we have anything go gateway
[36:48] here. So I think that yeah we call it
[36:50] the foundry gateway. So the interesting
[36:51] thing is that basically like you're
[36:53] going through a couple layers at that
[36:55] point. Um but I know that's common when
[36:58] you set up a gateway. Uh so I don't know
[37:00] that's a good question. Um oh because
[37:02] you want to do rate limit and off
[37:03] policies. Um so when you say API gateway
[37:06] you mean you're doing an Azure that's
[37:08] basically Azure API management right? Uh
[37:11] so API gateway
[37:13] in Azure API management. Yes. Okay. All
[37:16] right. So, that is the question. Yeah,
[37:19] that's a good question. Um, I will ask
[37:23] uh afterwards to see if that's something
[37:26] that's already kind of documented.
[37:32] Uh you can always try it out because
[37:34] basically it is a it's a it's you know
[37:37] it is an HP endpoint that is using um
[37:40] Entra authentication, right? So um you
[37:43] know going back to
[37:45] the
[37:47] um deploy uh
[37:52] where did we invoke invoke invoke invoke
[37:56] all right it's going back to slides.
[37:57] Okay. So here, right? So as long as you
[37:59] if the gateway has the ability to pass
[38:02] along
[38:03] um
[38:05] the Entra token, uh then you know then
[38:10] it should in theory be able to proxy
[38:13] these. Um but maybe there's some other
[38:16] considerations.
[38:19] Uh that token would be
[38:22] oh yeah here I was just using my local
[38:24] token but you would you would have to
[38:26] pass a token that had the um that had
[38:30] access to that endpoint.
[38:38] Okay, I see we have a better link. AI
[38:40] gateway. Is that the Oh, yeah. So,
[38:42] that's even Okay, forget. So, we have
[38:44] API gateway and we have AI gateway.
[38:47] Okay. Um, so I guess a good question
[38:50] would be whether you want not a sep Oh,
[38:53] it's not a separate offering. Okay.
[38:55] Sometimes I have a hard time keeping
[38:57] track of everything. We have so many
[38:59] things. Um, let's see. And let's see if
[39:03] it mentions agent service.
[39:07] Connect an AI gateway to Foundry agent
[39:09] service. Bring your own model.
[39:15] That's for a model.
[39:17] We want
[39:19] an agent.
[39:26] Yeah.
[39:28] Yeah. I think we we want we need like a
[39:30] dedicated
[39:32] document about it. Um, I'm not seeing
[39:37] pages
[39:51] agent.
[39:53] Uh, you can register an agent. You would
[39:55] think there would be like you kind of
[39:56] want to have like maybe a built-in
[39:58] support. Um, connect clients agent. Are
[40:01] they using
[40:03] client threads create? Okay. Yeah, I
[40:06] think I need to dig into this one more.
[40:10] It's a good question.
[40:15] All right, let's see.
[40:20] That's okay. Let's see.
[40:24] today.
[40:26] Oh, so Honor says using Monty as a tool.
[40:30] Uh, yes. So, just to clarify, Monty is a
[40:33] uh code sandbox.
[40:36] Um,
[40:37] and basically it's like a rewritten
[40:41] Python. So, you know, with code
[40:42] interpreter when you're doing code
[40:44] interpreter, code interpreter is like
[40:45] creating like a full
[40:47] VM sandbox thing, right? Whereas Monty
[40:51] is basically they rewrote Python from
[40:54] scratch and only wrote the parts only
[40:57] wrote some parts of it. Um so that it
[41:00] couldn't have it didn't have it can't
[41:02] doesn't have access to anything insecure
[41:04] because it just doesn't even have access
[41:06] to file system. They just didn't write
[41:07] that part of Python. Um
[41:11] so the suggestion is that you could
[41:14] actually
[41:15] um you know use Monty basically put
[41:18] Monty as a tool. So yeah, you could do
[41:19] that, right? So if you had uh so you
[41:21] like import pedantic monty. So you would
[41:24] basically make like a local function
[41:25] that would call pedantic monty with the
[41:28] suggested code. Um or maybe your
[41:31] function would like accept code
[41:34] imports. Yeah, you have to decide what
[41:36] it's what this looks like. You should
[41:37] share your code for this because that
[41:40] looks kind of fun. Um so yeah, in theory
[41:41] you could have it uh you could have it
[41:43] as a local tool. I guess you could also
[41:45] have an MCP tool, but couldn't you also
[41:47] just have it as a local tool? Because
[41:48] the whole thing with Monty is that you
[41:50] don't have to, you know, you don't you
[41:52] shouldn't have to start up a separate
[41:53] server for it, right? You could simply
[41:56] um be um running that.
[42:01] What is this one? But I haven't actually
[42:03] I I've seen Samuel talk about Monty um
[42:07] but I haven't actually used it myself
[42:10] yet.
[42:13] Okay.
[42:15] interesting
[42:20] code execution tool set.
[42:23] All right. Oh, let me link to this as
[42:24] well.
[42:36] It's good to know that there's interest
[42:37] in Monty. Um Oh, here's your Monty.
[42:40] Okay, great. Yay. We got a link.
[42:41] Awesome. Thank you. Okay.
[42:45] So, here,
[42:48] oh, I see you're saying you were using
[42:50] it as a tool in your MCP server, right?
[42:52] Right. Um, so analyze data code.
[43:04] Okay. And I presume your analyze data
[43:08] is
[43:10] analyze analysis.
[43:13] Yeah. Okay, great. Um, right. So, what I
[43:16] was saying is like what if you had this
[43:18] as a you know, if you had this as a a
[43:21] local function
[43:23] um like a like this right to I don't I
[43:28] don't have Monty installed right now,
[43:29] but um if this was a tool that took in
[43:32] code and data and then and then you gave
[43:37] you know gave access to this tool,
[43:40] would this work? I I think it would
[43:42] right um you like the thing you have to
[43:45] decide is what the um you know what the
[43:51] uh what arguments you want to accept. So
[43:52] in this case you know we have code and
[43:54] data um but that's that's a very
[43:57] datacentric one. Uh you could just do
[43:59] the more general thing would just be
[44:01] code right and say code
[44:05] and then it's just going to
[44:09] right this would be like the most
[44:11] generic version of it execute the code
[44:15] and then we just won't give it any
[44:16] inputs.
[44:19] Yeah, exactly. I feel like we could try
[44:22] this right now. Wait add what is it?
[44:24] Pantic monty. See
[44:30] I should be able to at least run a local
[44:32] local agent even if I can't log into
[44:35] Azure.
[44:37] Um,
[44:39] is that is it pedantic monty? Pedantic.
[44:48] Yeah, it's pedantic monty. Okay. Oh, I
[44:52] still has a
[44:54] Okay. UV add pedantic monty.
[45:00] Okay.
[45:02] Uh
[45:04] All right. So now we've got Monty. And
[45:05] so now I should be able to
[45:08] import it up here.
[45:12] Okay. All right. And then that looks
[45:15] good.
[45:17] Um, now we need we need like an example
[45:21] of something
[45:23] that that would require it to use Python
[45:26] code, right? Let me just make sure
[45:27] there's no import errors or anything.
[45:30] Um, let's see. Uh, when does it Oh,
[45:34] create a graph. Oh, wait. It can't it
[45:36] probably doesn't have access to mapplot
[45:37] lib. That's why I like the code
[45:38] interpreter because I'm always telling
[45:39] it to create a graph. Um
[45:43] uh you know write write a Python program
[45:46] to calculate or write a Python program
[45:49] to calculate
[45:55] to calculate
[45:57] the number of days until enrollment
[45:59] closes. Okay, we'll just try that
[46:01] because it Yeah, I might do it.
[46:06] All right, now I'm going to have it do
[46:08] this. I should add. Do we have logging
[46:10] in here? Let's see. Logger. Logger.
[46:12] Logger. Let's add logger
[46:16] info.
[46:19] Uh, okay. I want to see the code.
[46:23] Let's let's call it also something. Run
[46:25] Python code. All right. We're going to
[46:27] make it execute using Okay. And then
[46:30] code. Here we go. Execute Python code
[46:33] safely.
[46:36] Code. Code. Code. run Python code and
[46:41] code percent s code. All right,
[46:45] now let's try this out.
[46:50] Um, this Okay. Uh, analyze. Oops. Sorry.
[46:53] I got to let me update this. Uh,
[47:03] uh, and we should be recording. Let's
[47:04] just make sure. Yeah, this is still
[47:06] recording. Yeah. So, we are recording
[47:07] this office hours uh for the the
[47:09] question that I just saw.
[47:12] Okay. So, let's see if we can if it's
[47:13] going to call Monty.
[47:17] Call Monty.
[47:24] Uh
[47:27] well, it's slowing down. Maybe that
[47:28] means it's calling it.
[47:31] Didn't call it. Um write a Python
[47:34] program.
[47:35] Oh, you know what? Because also I'm
[47:36] using let me do this because this is
[47:38] using the local model. Um let's add this
[47:41] to the foundry model one because
[47:44] you know local models are not as
[47:47] obedient,
[47:49] not as good.
[47:52] Uh let's see. Pantic monty. Pantic
[47:54] monty. Okay.
[47:57] All right.
[47:58] Okay. Pantic monty. All right. And then
[48:02] we're going to add it as a thing. And
[48:04] then done. Okay, great.
[48:07] Good co-pilot. All right. And
[48:12] okay. All right. So, let's try this one
[48:16] and see if we can get it
[48:20] to call the Python code tool.
[48:26] Uh, line 79 or what? Probably the last
[48:29] one.
[48:32] Yeah.
[48:34] Oops. Did I save it? All right. Um,
[48:39] yeah, the tricky thing is getting it to
[48:43] getting it decide to call the tool.
[48:50] Here's an answer.
[48:52] Oh. Oh, right. Because my because I
[48:55] can't log into Azure. Ah, all right.
[48:57] Well, try that out. Um
[49:02] uh it yeah the because for some reason
[49:06] the local one let's see we can really
[49:08] force it. Okay write I'm just going to
[49:11] tell it write a Python program to
[49:13] calculate number of days until
[49:16] net
[49:19] 30th number of seconds. Okay. Just
[49:22] something that's just straight up going
[49:23] to use
[49:25] use the code tool.
[49:38] And this, of course, the funny thing is
[49:39] that for me, because my Mac is not a
[49:42] very powerful Mac, when I use small
[49:44] language models, it's way slower than
[49:47] using a deployed model. So that's why
[49:50] it's so slow. Here we Okay, so Oh, good,
[49:52] good, good. Run Python code succeeded.
[49:54] Okay, great. Good. So, it got back this
[49:58] thing and then it said
[50:02] um I mean the the agent didn't
[50:04] understand what just happened but um
[50:06] return result execute the code. Um it
[50:10] looks like that's the interesting thing
[50:12] is I don't actually know for sure is the
[50:14] result the standard input output is it
[50:17] getting the print result or
[50:20] um m.run what does m.tr run give back
[50:23] returns result of the last expression in
[50:25] the code. Yeah. So what you want is
[50:27] actually um
[50:30] print call back. Uh so you might want to
[50:32] actually do a print call back um or we
[50:35] have to make it really clear um write a
[50:37] Python and and and return
[50:41] or like your last statement. This is the
[50:43] tricky thing whenever you're doing
[50:44] something your last
[50:46] statement. You'll have to mess with this
[50:48] but your last statement should not print
[50:52] the result.
[50:54] It should be the variable that stores
[50:57] seconds.
[51:00] Uh just the variable. Yeah. So this is
[51:03] the tricky thing is I so I think what
[51:05] you'll want to do is both grab the
[51:07] result and then also um uh execute this
[51:11] uh implement the print call back so you
[51:13] can collect print stuff. Um it just
[51:15] depend like it depends what kind of code
[51:17] you expect it to to run. But I think in
[51:19] this case, even though we see this print
[51:22] here, I don't think that uh I guess we
[51:24] should print let's do logger.info result
[51:28] um logger.info. Yeah, let's look at the
[51:31] result because I I think in that last
[51:33] case it would have gotten a null result.
[51:36] Uh so let's try it. Let's try it this
[51:39] time. Um cuz I had to do something very
[51:43] similar actually when I was using
[51:44] piodide which is Python
[51:47] in the browser is that I had to like
[51:50] really specifically collect the um print
[51:54] print statements.
[51:58] Okay. So now let's see. Oh, I think it
[52:01] followed the instructions. So this time
[52:03] it might work because look there's no
[52:05] print statement this time. It's just
[52:07] putting the variable and technically
[52:09] that should mean that that's the result
[52:11] of the final expression. Um
[52:14] gh but then
[52:16] exception. Okay. And then I don't see
[52:22] I don't see the result. Did I not save
[52:23] it? Gh.
[52:26] So this requires a little bit of
[52:27] finagling.
[52:31] Uh Samuel's actually going to give a
[52:32] talk about Monty next Monday at a
[52:34] conference that I'm organizing. So now
[52:37] I'll get to actually So if if you have
[52:39] any questions for Samuel, I will harass
[52:42] him in person
[52:44] and also just tell him nice things too.
[52:47] Uh he's going to be talking about Monty
[52:48] there. So this is relevant. Okay. Oh,
[52:51] good. Look at that. It says result. All
[52:52] right. So this time, so I think I just
[52:55] didn't have the the thing saved. So now
[52:56] we can see the final thing is seconds.
[52:58] Now we get the results.
[53:01] Uh the fun thing succeeded.
[53:04] um the small local lang language model
[53:07] is struggling a little bit as to what to
[53:09] do with that information.
[53:12] What do you try to do with this number?
[53:13] Right? I didn't tell it anything to do.
[53:14] I just wanted to write the program. Uh
[53:15] but the point is that it works. So let
[53:17] me go ahead and put this in I'll put
[53:20] this in a gist um so that uh we have
[53:24] this minimal example here. So this was
[53:27] agent framework plus monty tool.
[53:32] Uh, I'll I'll tweet it to Samuel, too.
[53:35] He'll get a kick out of it, probably.
[53:37] All right. Monty. py. Here we go.
[53:43] All right. So, you should be able to
[53:44] This should work fine. I would think
[53:47] this should work fine just hosted, too,
[53:49] because it's just running, you know,
[53:51] Python. Um, this is running Python. I
[53:53] mean, it's written in Rust, but it's
[53:55] Python, basically. So, here you go.
[54:00] All right. Nice. I'm glad we at least
[54:02] got to do some sort of live coding. I'm
[54:04] always happy when we get to do that.
[54:10] All right, we are at the end of the
[54:11] session. So hopefully you're just typing
[54:15] goodbye. I know at the end of the
[54:17] session is awesome when people often
[54:19] have questions.
[54:20] Do I like getting nerd mail? What is
[54:22] nerd mail? Um I like um getting
[54:27] technical questions in terms of like my
[54:29] LinkedIn inbox. If I get a technical
[54:31] question about something I presented, I
[54:33] try to answer it if that's what you mean
[54:35] by nerd mail. Um, if it's not related to
[54:38] that, I just don't always have time.
[54:40] Like I'm supposed to be reviewing a book
[54:41] about LM inference training right now
[54:45] and but I just haven't had time to
[54:47] reply. So when it's a technical question
[54:49] about something that's like in my, you
[54:51] know, wheelhouse like Microsoft Azure,
[54:53] whatever, all that stuff, then uh then
[54:55] that's usually what I have time to reply
[54:57] to. And then I don't often just have
[55:00] time for everything else.
[55:03] Um
[55:08] the agent management world, you know,
[55:10] it's good to learn new things. Uh we did
[55:12] this series, you know, when I do these
[55:14] series sometimes it's because I feel I
[55:16] have, you know, something I like
[55:17] knowledge that I already have that I
[55:19] want to share with the world. This
[55:20] series was the opposite where it's like,
[55:22] okay, you know, I want to learn about
[55:25] more about Foundry hosting and this
[55:29] series is the excuse for me to learn it.
[55:31] Um, so uh thank you all. Thank you
[55:34] everyone for learning along with me.
[55:36] It's always nice of you to uh to to join
[55:39] in the learning journey together.
[55:44] Oh yeah, cool. Yeah, I do like
[55:46] flashcards.
[55:50] Oh, a symposium next month at MIT. I
[55:52] know there's something else happening at
[55:54] BA in Boston June 1st, but that's also
[55:56] when build is happening. So, I think it
[55:59] was was it OCON or something happening?
[56:02] Um,
[56:04] so I I know I can't make it to that one
[56:06] because build is happening. You can see
[56:07] my this is my next month. Um, build is
[56:10] happening June 2nd 3rd and there'll be
[56:12] lots of good announcements there. Um,
[56:16] so I don't know if any of you are coming
[56:18] to that. Um, but uh, at least pay
[56:22] attention to the news that comes out
[56:23] because it should be fun.
[56:26] All right, cool. Thank you everyone. I
[56:29] will, um, post the office hours and the
[56:32] write up and all that stuff from the
[56:34] from the thread um, so that you can get
[56:37] it get it there. and then I will see you
[56:40] on Wednesday to talk about lang chain
[56:43] and Thursday to talk about evaluation.
[56:46] All right,
[56:49] thanks for bearing with all the my Azure
[56:51] issues today. I'm going to go talk to it
[56:54] right now and see if we can fix my Azure
[56:56] account now because I can only stay
[56:58] logged in for a half hour at a time. So,
[57:00] I was logged in for the first like 20
[57:02] minutes of the live stream and then it I
[57:04] got kicked out. Ah, computers so hard.
[57:08] All right. All right. I'm blabbing. Bye,
[57:10] everyone.
