[00:00] Okay, so welcome welcome back. We just
[00:03] had our live stream about monitoring and
[00:06] evaluating agents
[00:08] and here we are in the office hours
[00:11] afterwards to see um what questions you
[00:15] have.
[00:18] Uh, so code spaces, copy, copy, how to
[00:24] copy text out of code spaces
[00:27] and you could rightclick. Um, whenever
[00:30] you're like setting up code spaces, you
[00:32] can check this like you have to make
[00:33] sure that your clipboard is allowed.
[00:35] Usually you get a popup at the
[00:36] beginning. Uh, so clip just make sure
[00:39] clipboard's allowed and then well I just
[00:42] use control command C because I'm on a
[00:44] Mac. Um but um I don't know for Windows
[00:49] what the best approach would be.
[00:51] Pamela's a goat.
[00:56] Okay, so good question from Marcus. Does
[00:58] one need to have an Azure account to use
[01:00] the Azure evaluations and is there a
[01:02] free level? So we did actually set this
[01:04] up agent evaluation with the local
[01:06] evaluation. Um this one in theory
[01:12] you could use it with um you know with
[01:14] many models you just have to set up the
[01:16] openi model configuration like in theory
[01:18] you can you can use it with openi.com
[01:21] you could maybe even use it with lama I
[01:23] don't know if I've ever ran evaluations
[01:25] I think I did once use like run
[01:27] evaluations using lama as a model um so
[01:30] basically as long as you can set up what
[01:32] you need in this model configuration
[01:34] right um so it just has to be like
[01:36] openai compatible
[01:38] The issue is that GitHub models is so
[01:40] token limited that um you know people
[01:43] ran into issues. So some of us were able
[01:45] to run it like I did manage to run this
[01:47] using GP5 mini. Gwen somehow got it
[01:50] working with DB41 mini. I don't really
[01:52] understand how that work but like yeah
[01:54] so the you know there are token limits
[01:56] but you could use it with openAI and in
[01:58] theory you could even do it with Olama
[02:00] if you do have a capable enough machine
[02:03] um and if you have a capable mouth not
[02:05] model right so maybe it would have
[02:06] worked with like a lama and like the
[02:08] Gwen models you know it's it's worth a
[02:11] try um so as long as you can get a model
[02:14] that works that's compatible that you
[02:15] can specify in the config then you can
[02:18] run this um this SDK Now with the batch
[02:22] one, this one um also
[02:26] also you can run this locally too. Um so
[02:29] the Azure AI project is optional. Um in
[02:32] fact I forgot that it's optional. So
[02:34] actually in theory you can even run the
[02:36] batch evaluation but I think once again
[02:37] we have the issue where you know you
[02:39] you're going to go over tokens with
[02:40] GitHub models. Um but you can output the
[02:43] results locally. Uh so I do have I and I
[02:47] even saved the results so you could see
[02:49] um you know what they would look like if
[02:51] you had run them uh locally. Let me word
[02:55] wrap this better.
[02:57] Uh work. Okay.
[03:00] Word wrap. All right. So this is what
[03:02] the results would like look like if
[03:04] you're running it locally and not saving
[03:05] to Foundry.
[03:07] Uh so yes in theory you do not have to
[03:11] use a a foundry project for this Azure
[03:14] AI valuation SDK for the quality
[03:16] evaluations.
[03:17] Um but you need to have a model
[03:20] configured that has enough of enough
[03:22] token capacity
[03:25] for the red teaming. You do need to have
[03:27] a foundry project um because you do need
[03:30] access to that adversarial LLM.
[03:36] Now, as I was saying, there is a new way
[03:37] of doing evals with the OpenAI package.
[03:40] Let me see if I can find it. Foundry
[03:43] Project Evaluations OpenAI evals.
[03:47] Let me find this.
[03:51] Is this it
[03:54] Python?
[04:02] I know it's like import open AAI and
[04:04] blah blah update existing
[04:10] trying to find evaluate generate local
[04:13] evaluation
[04:16] I think this one this article okay
[04:22] how cloud evaluation works yeah so this
[04:25] is the one so this is what I haven't dug
[04:26] into yet and I think this one does
[04:31] I I think this one um does require a
[04:34] Foundry project from what I can see
[04:35] because basically it uses the OpenAI SDK
[04:38] in conjunction with the Azure AI
[04:40] projects SDK. So that's part of why we
[04:42] didn't use it for this one because in
[04:44] theory we were hoping you could run it
[04:47] with with GitHub models. Um but going
[04:49] forward this seems to be the way going
[04:52] forward that um that is recommended is
[04:56] to to use this this SDK as well.
[05:01] All right let's see we have a question
[05:04] from Brooks. Uh how does one set up the
[05:07] spans within the traces in open
[05:10] telemetry in data dog span tags are
[05:12] used. Um, okay. So, I guess you're
[05:15] wondering about how to set up custom
[05:18] custom spans. Um, because in, you know,
[05:22] when we did the agent framework one, uh,
[05:24] everything was already being set up by
[05:27] agent framework.
[05:29] I'm trying to remember if I've ever, to
[05:31] be honest, I'm probably going to just
[05:32] defer this to GitHub copilot. Um, how
[05:35] I'm trying to remember where have we set
[05:36] up custom spans, how to add additional
[05:41] open telemetry
[05:43] spans
[05:48] because I usually do not set up my own
[05:51] custom spans. I don't think I've
[05:53] actually even done it in any of the
[05:54] projects.
[05:56] Um, I've always brought in other
[05:58] people's uh instruments. Uh, but okay.
[06:01] Yeah. Okay. this thing. It's like a wid
[06:03] context manner. Yeah, because you want
[06:04] Oh, I did actually I actually did do
[06:06] briefly briefly do this because I was
[06:08] trying to add like a parent span to
[06:09] something. Um,
[06:13] oh yeah, and we did it also in our MCP
[06:15] series. We set up like a whole We had to
[06:17] set up our own, didn't we set up our own
[06:19] instrumentation for our MCP? Let's check
[06:22] it out. This was Gwen and I when we did
[06:24] the MCP series, we did um open telemetry
[06:28] middleware. We added a middleware
[06:30] talking about middleware. Okay, so here
[06:32] we set up like this whole tracer
[06:34] provider blah blah blah and then we set
[06:37] up this middleware
[06:39] um and uh in this let's see how do we do
[06:44] it span yeah so this this is looking
[06:47] similar here so you have a tracer and
[06:49] you need to set up um usually do a width
[06:51] so that you can have like a parent
[06:53] parent span and children spans uh so
[06:56] this is similar to this yeah so we need
[06:58] a tracer and then you can start the
[07:00] parent span and then you spec and you
[07:02] set attributes on that span and um oh in
[07:06] this case you do something you set
[07:07] another attribute right so that's a
[07:10] general approach is um you know set up
[07:14] use a context manager so that you can
[07:16] have a parent span and um and that way
[07:20] like you know if if something happens
[07:22] within that then that gets marked as the
[07:24] parent span
[07:26] uh I'll link to this this I mean this
[07:28] isn't done as as middleware um But, uh,
[07:31] that's that's that would be the general
[07:33] idea.
[07:37] All right, let's see.
[07:42] Um,
[07:45] oh, yeah, I see a question about um not
[07:48] being able to you're not able to deploy.
[07:52] It looks like you're right. We didn't
[07:54] set up the fact that since we are
[07:55] setting up key list credentials that
[07:57] does require a certain amount of access
[08:00] usually we note that in Azure account
[08:02] requirements um here that you you need
[08:04] to have um one of these roles um or you
[08:09] can do this trick here where you get
[08:11] arbback for a resource just a resource
[08:14] group and deploy to that group. Um, so
[08:16] let me just make a note that we need to
[08:19] add this to read me.
[08:23] Uh, but let me link to that just in case
[08:24] the workarounds there are helpful. I
[08:26] don't remember what we've set up in the
[08:28] particular infra for this one whether
[08:30] you're going to be able to use the um
[08:33] things. So yeah, generally we try to use
[08:35] keyless deployments, but um that does
[08:38] actually require some things from your
[08:40] Azure account. So if you are trying to
[08:41] deploy with the infra in the repo then
[08:44] you might have this issue. So you could
[08:46] also just set it up manually.
[08:51] Yeah. Yeah. So we would need to improve
[08:54] the infra so that you could um you know
[08:57] deploy to a certain resource group.
[09:01] Um all right. So Marcus says if one has
[09:04] Microsoft Office 365 family subscription
[09:07] does that have any tokens for Foundry or
[09:09] Azure?
[09:11] I believe that that's just completely
[09:13] separate as far as I know because the
[09:15] way I understand it is M365 licenses are
[09:17] generally you know dependent independent
[09:20] of Azure ones because I know in our
[09:22] Azure um subscriptions we have to
[09:25] request M365 separately as a different
[09:27] license like we get like the E5 license
[09:30] or whatever and um and yeah I think it's
[09:33] as far as I understand that's that's
[09:34] quite separate so I I think you would
[09:36] just need to um set up the Azure account
[09:39] separately. You can set up like an Azure
[09:41] free trial. Unfortunately, I don't think
[09:43] Azure field trials have access to
[09:45] Foundry projects. Um, we should double
[09:48] check that. Uh, let me just make more
[09:50] notes here. Deploy to existing RG. Um,
[09:53] do Azure free have foundry access? I
[09:57] believe as far as I know, Azure free
[10:00] accounts have very limited foundry model
[10:02] access like only a thousand tokens
[10:04] capacity, which is just nothing
[10:06] basically. And I don't think they have
[10:08] the ability to make foundry projects,
[10:10] but we can check that. So, I think
[10:11] you'll just have to make like a Azure
[10:15] account and then just kind of limit your
[10:16] budget to like 20 bucks a month and set
[10:18] up like a budget alert and say like,
[10:19] "Hey, when it goes over 20, like let me
[10:21] know." Um,
[10:23] and that way you can start trying some
[10:25] out.
[10:28] Um, so Nambdi asked, "Why did Chach take
[10:31] five seconds to decide on tools? Two two
[10:34] tools that seemed really long." Yeah,
[10:36] LLMs are slow, huh? Um, this one Oh,
[10:38] wait. Let's see. This one was local
[10:39] host. So, that's using Azure um Azure
[10:42] hosted LM. Now, to be fair, this is a
[10:44] I'm using um what's called like a pay as
[10:47] you go access to the model. If you do
[10:49] want better latency when you're like an
[10:52] enterprise customer and you're using
[10:53] like $12,000 of LM a month, then you can
[10:56] do this provisioned account where you
[10:58] have like a dedicated infrastructure
[11:00] just for you. I'm using pay as you go.
[11:01] So basically I send off a request, it
[11:03] goes off to an LLM somewhere in the
[11:05] region um that I've specified and it's
[11:08] kind of just like best effort for
[11:10] latency. Uh so you can increase latency
[11:13] if you're doing like a huge number of
[11:15] calls. Um you can increase to some
[11:16] amount but also I'm sending to GPD5 mini
[11:19] that is a reasoning model and I um I
[11:22] didn't specify the reasoning effort
[11:24] here. So if I really wanted to um
[11:28] optimize it, let's see if I can optimize
[11:30] this. Okay. So, we are doing I'm using
[11:33] um what is our model here? GB5 MIDI and
[11:38] I haven't where do I specify the
[11:40] reasoning effort for this one?
[11:42] Default headers default async client.
[11:46] I'm wondering if I can set the reasoning
[11:48] effort because I want I um you know
[11:51] there with GBD5 mini there is a
[11:54] reasoning effort there should be
[11:56] reasoning effort of none I believe maybe
[12:00] we added that in 5.1 um so one thing
[12:02] would be the reasoning effort parameter
[12:04] um let me actually check to see if we
[12:05] can set reasoning effort here uh
[12:08] reasoning effort
[12:12] uh typed options
[12:16] Okay.
[12:17] Reasoning effort open AI reasoning chat
[12:20] models. All right. We're just going to
[12:22] ask co-pilot. So whenever you have a
[12:24] question, I I like to just go click the
[12:27] little co-pilot on the repo and say,
[12:28] "Okay, how to set reasoning effort with
[12:32] an OpenAI model in Python SDK. Now,
[12:36] unfortunately, this repo has both Python
[12:38] and .NET code in it. So I always have to
[12:39] specify which one." Um, but okay. So it
[12:42] says we're do agent client instructions.
[12:45] Ah default options. Okay. So when we
[12:48] make the agent,
[12:50] we're going to pass it into here. So
[12:53] let's try that out and see if we can
[12:58] um get a quicker response.
[13:02] So UV run examples
[13:05] agent
[13:07] hotelpire.
[13:09] py. All right.
[13:31] All right. So, we're running this now.
[13:34] Um, and let me open up my
[13:37] local.
[13:39] Trying to get the Okay, I just saw it
[13:41] come in. Let's check the time. 10. No,
[13:44] 10:43. 11:49. That's the one we want.
[13:47] Okay. Oh, that took a long time.
[13:52] Now, the thing is like sometimes the
[13:54] right is the length is just like, you
[13:57] know, things happen, right? So, that's
[13:59] generally why when you do performance,
[14:00] you don't just look at a single call.
[14:02] You look at um a bunch of calls and then
[14:04] you look at what's called like the P99,
[14:06] right? That's why when you look at the
[14:07] metrics tab here um you're you're
[14:11] looking at you have like P50 which is
[14:12] the 50th percentile 99th percentile
[14:15] exemplars right so you want to like you
[14:17] could set up load testing um I use like
[14:19] lo usually use like locust.io IO or is
[14:22] it going to be IO? Yeah, Locust is great
[14:24] for Python load testing. So, you can set
[14:26] up load testing and um you know send off
[14:29] a bunch of requests and then just see um
[14:32] you know what is what is your average
[14:34] latency? That one was actually really
[14:37] slow. But let's make sure it actually
[14:38] sent um the reasoning effort that we
[14:41] wanted. Let's see instructions. Are we
[14:44] going to see the options here? I don't
[14:46] know if it's going to show me
[14:49] the options.
[14:52] I say I don't know that it showed me the
[14:54] options. That that was like really slow
[14:56] though. Let's try it again. Um so yeah,
[14:58] it is a greasian model and GB5 mini
[15:02] should be faster than other ones. But um
[15:04] you know latency does depend quite a bit
[15:07] and usually what I do is when also
[15:09] another thing I do when I set up
[15:10] evaluations is I look at um I I measure
[15:14] the latency. So some of the metrics
[15:16] you'd like set up um like here uh let me
[15:19] show you
[15:21] chat eval uh
[15:25] okay docs
[15:29] uh summary okay all right so length no I
[15:34] wanted to show you something else I'm
[15:36] just trying to show you when I usually
[15:38] do evaluation what I actually look at um
[15:41] because I don't just use LM as a judge
[15:43] metrics there's other metrics too that
[15:45] that are useful. Um
[15:49] I didn't show them here. Okay. Well,
[15:51] normally I would also have latency. I I
[15:53] I do measure latency. Um so that way you
[15:56] can see over like 200 calls what your
[15:58] average latency was because it
[16:00] definitely does change over, you know,
[16:03] as you change model, you can see big
[16:05] change in latency. Okay, so this time
[16:07] that was faster. It's still looking
[16:08] really slow. It almost seems like it's
[16:10] slower than before,
[16:13] which is really funny. Um, you could try
[16:16] change like what if we change this to
[16:17] high then we should see if this if this
[16:20] thing is working, we should see it take
[16:22] like a really long time. Um, but we'd
[16:25] also have to verify like is this really
[16:26] working. So once again, um I'm just
[16:28] going to set my
[16:31] uh logging to debug so I can see exactly
[16:34] um what's sent over over the HP wire and
[16:39] um and see how that's working.
[16:44] Uh
[16:50] yeah, so I see Nandi says you sometimes
[16:52] want a second agent to validate but that
[16:54] can wreck the latency. Definitely. Yeah,
[16:56] it's very common to try and add a
[16:57] reflection step and u we've experimented
[17:00] with that like a reflection step to say
[17:02] hey was this good response you know
[17:04] should we redo it uh but it definitely
[17:07] adds latency so the other thing you
[17:08] could try doing is ask the like the LM
[17:12] it to judge itself like okay as you're
[17:14] giving your response indicate your
[17:15] confidence right and surprisingly like
[17:18] sometimes LLMs will tell you like oh my
[17:20] confidence is low on this right you
[17:21] could so you could have it like start
[17:22] off with its confidence be like oh
[17:24] confidence low and then here's my
[17:25] response response. Um uh that way you
[17:28] you you know you if you're trying to do
[17:30] this like dynamically during userf
[17:32] facing stuff like that that could be an
[17:34] approach right because anytime you add
[17:36] an LLM into a userfacing flow then it's
[17:39] going to take more time. All right. So,
[17:40] I just wanted to see
[17:43] um if we raising effort high. Okay. So,
[17:47] it does say raising effort high. So,
[17:51] that should have I taken longer.
[17:56] Let's see.
[17:58] Um overall, yeah, the whole thing took
[18:01] 25 seconds. So, um and it does take a
[18:04] lot. taking longer to answer than um you
[18:09] know than to actually um pick the tool
[18:11] calls. So reasoning effort does affect
[18:15] time duration um but also duration just
[18:19] changes over time. So when you whenever
[18:21] you make a change even if you're just
[18:23] measuring latency you know you want to
[18:25] send off a bunch of requests and see
[18:27] what is your average latency. never base
[18:29] any with any sort of generative AI
[18:33] evaluation. You can never base your
[18:36] decision on a like, you know, just a
[18:38] couple calls, right? Uh or a couple
[18:41] examples, right? Like you know, you
[18:43] really because there's so much
[18:46] variability in both latency and accuracy
[18:49] and quality that you have to always do
[18:52] some sort of bulk evaluation
[18:54] uh in order to reason about anything.
[19:01] Um,
[19:04] all right. So, we see lots of fun times
[19:05] in
[19:07] in the chat. Um, so if you have a reason
[19:10] agent and you wouldn't have a checker
[19:11] agent in the workflow. Yeah. So, that's
[19:12] always a decision, right? Like, so you
[19:14] only know for sure if it's worth
[19:16] changing like changing your model to,
[19:19] you know, to a fancier agent or even
[19:20] changing the reasoning effort to a
[19:22] fancier agent if you have evaluation set
[19:24] up. And when you run those evaluations,
[19:25] you see, oh, okay, I can see um you
[19:28] know, latency
[19:30] uh latency um you know, changed, but
[19:34] also quality change because a lot of
[19:36] times it's all like a you know, it's
[19:38] it's a trade-off. And that's the hard
[19:39] thing about doing LM based applications
[19:41] is that you might find this way better
[19:43] approach, but if it doubles the amount
[19:45] of time and if you're doing a userfacing
[19:47] application, then you know, then you
[19:49] really have to decide. Um, let me
[19:51] actually show you my eval
[19:54] um,
[19:56] for the rag application.
[19:59] Um, because it does actually have
[20:01] latency in it. I just have to um, set up
[20:04] the
[20:06] uh, the right environment.
[20:12] Okay. And then evaluate or no, I don't
[20:16] I'm not evaluating right now. I'm just
[20:17] doing the results. Sorry.
[20:24] And I think you'll find once you start
[20:25] setting up evaluations, you'll just end
[20:27] up like writing your own tools for it.
[20:29] Um,
[20:31] just so you can like really customize it
[20:32] to your workflow.
[20:35] All right, let's get these. And this is
[20:38] um I built a tool using textual, which
[20:41] is a Python
[20:43] package. Textual
[20:47] uh textual is built on top of rich. It's
[20:49] just really good
[20:51] um textbased CLIs and copilot actually I
[20:55] built it before copilot but I bet you
[20:57] copilot can do a pretty good job writing
[20:58] textual CLI now I hand wrote every line
[21:01] of this textual code all right so here
[21:04] we can see right so this is like what my
[21:06] evaluations look like for this rag repo
[21:08] where you can see I'm I'm you know
[21:10] mostly like changing models so I'm
[21:12] looking at oh GPD5 mini uh uh starting
[21:15] with GP35 turbo 40 mini GP5 GP5 chat 255
[21:19] mini and I'm looking both at these LLM
[21:21] based things, the GPT, but then I'm also
[21:23] looking at answer length that actually
[21:25] varies a huge amount based on the model.
[21:27] Some models are so verbose and some are
[21:30] not. Some use like lots of lists. Um
[21:33] like I discovered GP5 loves lists
[21:38] and uh and yeah, it just depends. And
[21:39] then look at this latency, right? So 19,
[21:41] what was that? That was 03 minute. Yeah,
[21:44] because those early reasoning models had
[21:46] just really low lat uh really really
[21:48] high latency, right? Um but even GBD5
[21:50] mini, that one had a latency in this run
[21:52] of 12.79.
[21:54] Um in another run, so GBD5 mini, I think
[21:57] it, you know, this is a slower model. Of
[21:59] course, now we've got GBD51 mini, GB5 2
[22:02] mini, and GB52. I don't know if there's
[22:05] a mini, and then there's GB53 now even.
[22:07] So, it's definitely worth trying newer
[22:09] models because a lot of times these
[22:10] newer models, especially like the the
[22:12] sub numbers, are faster than the
[22:13] previous versions because like, okay,
[22:15] it's the model you love, but it's faster
[22:17] or it's the model you love, but it's
[22:19] cheaper.
[22:21] Uh, can people hear me? John asked if I
[22:23] was on mute.
[22:26] Doesn't think I'm on mute. Uh,
[22:31] you can hear me. Okay, great. All right.
[22:33] if you can't hear, it's always a Discord
[22:35] issue. So, you just kind of want to
[22:36] restart your Discord.
[22:39] Um,
[22:41] yeah. So, yeah, definitely, you know,
[22:44] look at look at latency. Um, try
[22:47] different models, measure it across a
[22:48] bunch of runs and, uh, you know, it's
[22:51] interesting to see what you come up
[22:53] with, right? And yeah, you can you can
[22:55] look at things, you can evaluate things
[22:57] other than just using an LLM, right? So,
[23:00] you can see a lot of my metrics are not
[23:01] LLM based. So we have answer length,
[23:04] latency. Um I also look at the ground
[23:06] truth for citations matched because this
[23:08] is a rag application. So I care whether
[23:11] the citations are correct based off
[23:12] ground truth and um I can measure all of
[23:16] those.
[23:19] All right. Um cool. Okay. So,
[23:24] what else do people want to ask
[23:30] about?
[23:39] It's just looking for more
[23:42] uh questions.
[23:45] Yeah, if you are deploying the infra
[23:49] um let's double check. Maybe I got the
[23:51] model version. So when you deploy models
[23:54] on Azure, you have to specify both the
[23:56] model and the version um because we come
[23:59] up with different versions all the time
[24:02] and um I might have bungled the version
[24:05] through this one. Did I? Let's see. So
[24:07] this one should be Oh yeah, I did bungle
[24:10] the version. Okay.
[24:12] Um the so the version has to match the
[24:16] model. It has to be a it has to be a
[24:18] version that the model has. Uh and then
[24:21] the other thing is that you have to have
[24:22] availability right and I think I was
[24:24] just in the availability table. Um
[24:29] here is the availability table right so
[24:31] what you can see is that the GBD5 model
[24:34] from August way back August that was
[24:36] ages ago um that has availability in a
[24:40] lot of regions but all of the new ones
[24:43] so we've got you know GBD 5.1 5.2 too.
[24:46] We don't have 5.3 on Foundry yet. Okay.
[24:49] But they are barely supported anywhere,
[24:51] right? East US2 is looking good. Sweden
[24:54] Central looking good and everything else
[24:57] is looking real rough. So if you are
[25:00] going to, you know, deploy any of these
[25:02] um newer GP5s in order to test them out,
[25:05] uh you are going to be more region
[25:06] restricted. So you have to pick a region
[25:08] um where they where they work.
[25:13] Uh, and all the rest those are the older
[25:15] models.
[25:18] Um, let me make a note. We need to fix
[25:20] the model. Okay.
[25:27] All right.
[25:29] Anything else?
[25:33] Not as many questions today. I'll just
[25:35] like zip through the slides again to see
[25:38] if it triggers questions because I know
[25:40] there were questions in the chat that I
[25:42] didn't get to. Um, red teaming, super
[25:46] fun. Hopefully I didn't um
[25:50] didn't traumatize anyone with the ones I
[25:52] showed. I got to say those were the tame
[25:54] ones. I was running this red teaming
[25:55] last night at like 11:30 and I've been
[25:58] trying to get to bed at 11:00 p.m. to
[25:59] like be better about that, but the red
[26:00] teaming was taking a while and there was
[26:02] like a little bug I was fixing and um
[26:05] I'm just and I added logging. Normally I
[26:07] don't log out the the actual attacks,
[26:09] but I did happen to add out logging
[26:10] because that's why I was debugging and
[26:12] so I saw every attack as it's going by.
[26:15] Um, and luckily there was like a lot of
[26:17] mouse Morse code in there, but but there
[26:19] was also all the actual like English
[26:21] language questions and oh my god, every
[26:22] time I saw a new attack I was like, "Ah
[26:24] no, my eyes." Like what dreams am I
[26:28] going to have tonight? So I really don't
[26:30] recommend just casually watching the
[26:32] attacks. Um, by default you won't. Um,
[26:35] but I just happen to add in some logging
[26:37] there. Uh so yeah, it's it's super
[26:41] interesting to to run that and and see
[26:45] um a lot of times you'll realize that
[26:46] you you you know, you're you don't have
[26:48] enough guards. And then what you can do
[26:50] also is like when you're using um a
[26:53] foundry model, let me like open up the
[26:58] foundry for this. Um where is our
[27:03] this one is in PF agent frameworks.
[27:05] Okay. Uh uh uh
[27:09] you can just open up the portal for this
[27:11] one.
[27:15] So basically um as you're when we run
[27:19] the open AI models and actually any of
[27:20] the models we put a content safety layer
[27:24] on top and that's part of why I really
[27:26] recommend people to use the um Azure
[27:30] hosted OpenAI models versus the OpenAI
[27:32] models because OpenAI models don't have
[27:34] the same um Azure OpenAI content safety
[27:36] filters on top. So if you're going for
[27:38] an enterprise application, um you know,
[27:41] it's better, it's always better to to
[27:44] have safety filters on top. Um yeah, I
[27:46] was just reading about how Enthropic is
[27:49] trying to force the US government to
[27:51] give them access to their models without
[27:53] the safety layer on top and that's
[27:56] really frightening because there's a lot
[27:59] of things that you could do violence
[28:01] wise and war military wise uh if you
[28:04] don't have safety rails on top. Um, so
[28:07] yeah, that's why um, you know, it's good
[28:11] when do we have these? Uh, so yeah, so
[28:13] guardrails and controls. Okay, just
[28:14] going here.
[28:17] Guard rails and controls. Um, content
[28:20] filters, right? So if we go to content
[28:21] filters, you can see I don't have one
[28:24] set up and that is just because my
[28:25] deployment is using the default filter.
[28:27] So, if you go to my deployments, you can
[28:29] see I have GP5 mini and that's what I
[28:30] was using. And it says the content
[28:33] filter is the default. And the default,
[28:35] you can see that it has a medium.
[28:37] Basically, it's medium level of blocking
[28:39] for everything. But we can actually make
[28:41] it even. We can raise medium to high.
[28:43] And we can even lower medium to low. You
[28:46] can't turn it off unless you have like
[28:47] really special access. Uh, and like the,
[28:50] you know, and Microsoft agrees. Um,
[28:52] which is good. Uh hopefully we don't
[28:55] have to agree to any governments asking
[28:57] us to turn it off. Uh so here we create
[29:01] the content filter right so you can make
[29:02] a new one and here this is where you can
[29:05] say like oh I want to block
[29:07] uh I want to block it like be super
[29:09] blocking right and so then you know and
[29:12] then you can also control jailbreak
[29:15] indirect attacks it's basically an
[29:16] indirect jailbreak if inside your um rag
[29:19] data sources right so you can we can
[29:21] turn that on so you can turn everything
[29:22] on to you know as high as possible you
[29:26] can even make a custom block list now
[29:28] generally it's kind kind of hard to um
[29:31] you can try. Yeah, it's it's interesting
[29:33] to try and block profanity. There's a
[29:35] famous blog post about how hard it is to
[29:36] block profanity without also blocking
[29:38] other things. So, usually I wouldn't
[29:40] recommend this, but maybe if you're
[29:42] doing like uh something for like really
[29:44] younger, like maybe 16 year olds or
[29:46] something, you might want to just air on
[29:48] the side of blocking versus not
[29:50] blocking. But as a general rule, it is
[29:51] hard to just block all of profanity. Um,
[29:55] so yeah. So then you set it up and then
[29:58] there's also the output filter which is
[30:00] what um comes out of the LM. Uh, so uh
[30:04] you're going to block that too. You can
[30:05] turn on PII detection. So that's nice.
[30:08] Um, and then you also have a block list
[30:10] for the output. So we set this all in
[30:14] and then we can apply the filters to our
[30:16] existing deployments
[30:19] and and then set that up. And so now my
[30:25] uh my GV5 mini is protected by like a
[30:27] much higher level of filter and uh so
[30:31] it's going to be like a lot more
[30:32] sensitive now, right? So if I ask it
[30:34] something like um
[30:37] how do I best kick a sheibu
[30:41] enu?
[30:43] I think this is one I've done before
[30:44] where it's blocked me when I set up the
[30:47] um when I set it up to the highest. Um,
[30:51] so ideally it's going to give us an
[30:52] error and refuse to answer the question
[30:55] because it doesn't think that kicking
[30:56] dogs is a good thing,
[30:59] but we'll find out. Uh, sometimes
[31:02] sometimes like there's so there's
[31:04] multiple layers of safety. We didn't
[31:05] have time to get in on this today and we
[31:06] have a whole talk about it, but there's
[31:08] multiple layers of safety. So the LM
[31:11] itself has been trained in order to be
[31:13] safe. That's part of the um RL RHF,
[31:16] reinforcement learning based off of
[31:18] human error uh based off of human um
[31:20] feedback. Um so the LM itself might say
[31:24] hey I'm you know I'm not comfortable
[31:26] answering it. And then on top of that we
[31:28] have the Azure OpenAI content safety
[31:31] filter um which you know uh may kick in
[31:36] on top of the LLM's weights and say like
[31:39] yeah I all like on top of that you know
[31:41] before it even gets to LM right. So the
[31:43] content safety filter is going to it's
[31:46] basically middleware that's going to
[31:48] look at the input in um before it gets
[31:50] to LM and decide if it's unsafe. And it
[31:53] looks like we got it good. So here we
[31:55] go. OpenAI content filter exception. So
[31:57] this is actually something you'd want to
[31:59] um you know if when you're actually
[32:00] making this you would want to do a try
[32:02] except around your around your agent
[32:04] code here to check for this. Uh and
[32:07] that's what I do for production apps.
[32:08] Right? So we say the response was
[32:10] filtered and we can see that it was
[32:12] filtered because of violence right and
[32:16] it says severity is medium. So as your
[32:20] open content safety does not want me to
[32:22] kick the dog which is good.
[32:27] Um all right. Uh so now we've got some
[32:30] more questions. Is Microsoft agent
[32:32] framework GA yet? That is a great
[32:35] question. I actually just learned today
[32:37] that the whole concept of GA is like a
[32:39] common concept. I thought it was
[32:40] something Microsoft made up. Um but I
[32:42] didn't realize it's like everyone
[32:44] understands it across the industry. Like
[32:45] I didn't get the memo. Um but anyway, so
[32:49] the question was is it GA? It is not yet
[32:51] GA but it is so so close because if we
[32:54] look at the release history
[32:57] uh there was another release 19 hours
[33:00] ago. This is 1.0.0 RC2 release candidate
[33:04] 2. So, it is getting so so close to GA.
[33:08] Um, I don't remember offhand when
[33:10] they're going to plan to declare
[33:12] themselves GA. Um, you can see this week
[33:15] they declared the GitHub copilot SDK to
[33:17] be GA, which is funny that that was
[33:19] declared first because that's been
[33:20] around for less time. Um, but agent
[33:22] framework, it's a more complex framework
[33:24] and you know, it takes more um effort to
[33:27] GA it. So, I I would say it's not
[33:30] officially GA yet because we're waiting
[33:31] for that real 1.0.0. no release. Um,
[33:35] this is a pre-release, right? These are
[33:37] all, look at all these pre-releases. So,
[33:39] we want an actual release that's 1.0.
[33:41] And I think at that point, they're going
[33:43] to declare it G8. Um, so I think it's
[33:46] going to be in like the next few weeks
[33:47] because we kind of tried to time the
[33:49] series to align with their timeline, but
[33:52] I don't remember exactly when it's going
[33:55] to happen. Um, it should be it should be
[33:58] very soon. Um I mean the thing is if a
[34:01] customer wants to start building
[34:02] production agent app now um and they
[34:06] want to build on Microsoft technology I
[34:08] think this is your best bet because
[34:09] here's the thing if you use semantic
[34:10] kernel that's basically in maintenance
[34:12] mode now that team all works on agent
[34:13] framework now same thing with autogen
[34:15] the autogen team all works on agent
[34:17] framework now so it doesn't make sense
[34:19] to like invest in those frameworks when
[34:22] you know you know that they're they're
[34:24] the past and the future is agent
[34:25] framework um so given how close we are
[34:28] to that 1.0. I would think that you'd
[34:31] want to start an agent framework with
[34:33] the assumption that it takes time to
[34:34] actually get it into production. Um, and
[34:39] I don't know with Foundry agents if
[34:41] they're considered
[34:44] um is there like a table that says
[34:47] what's what's GA and what's not? Uh,
[34:50] let's see if it says uh Foundry Agent
[34:54] Service blah blah blah. Does it say if
[34:57] it's preview?
[35:00] Doesn't really say FAQ
[35:10] generally. Yeah, I don't know how to
[35:13] check on it, but I know founder agent
[35:15] service hasn't also been going under
[35:17] going changes. So,
[35:19] um I don't know if anything's like
[35:22] actually technically G8, but I I I just
[35:26] wouldn't want to start on anything
[35:27] that's already basically deprecated.
[35:30] So, I I think I would start with that.
[35:31] Or you could use something that's not
[35:33] Microsoft. You could use L like lane
[35:34] chain if you're more comfortable with
[35:35] that. But at that point, like what's you
[35:37] know, why not just use the agent
[35:39] framework?
[35:41] Um is it a matter of weeks or months? I
[35:44] believe I feel like it's weeks at I was
[35:47] told that the interface the API
[35:51] for agents in agent framework was going
[35:54] to be stable at the end of February
[35:56] which is like now um but that the
[35:58] interface for workflows was potentially
[36:02] maybe going to change a bit over
[36:04] February March um so I don't know if
[36:07] they are going to kind of like
[36:10] G one part versus the other so I believe
[36:12] for agents we should hopefully be at the
[36:15] point where um it's stable and maybe
[36:17] even for workflows. Um I don't know we
[36:21] we'll just ask a question. Um I'll just
[36:24] add to my is when what is the timeline
[36:28] for GA? Okay. All right. We we'll just
[36:30] ask since I so that I'm not just making
[36:32] stuff up. Uh I think it's a matter at
[36:36] least for API stability. I guess I I
[36:38] don't I didn't pay um I guess I should
[36:41] pay more attention to GA now that I know
[36:42] that's a thing across the whole industry
[36:44] now. Um, but instead of like what
[36:46] matters to me is usually API stability
[36:48] because you can always you should you
[36:50] should always pin your versions, right?
[36:51] You can see we're pinned to like an
[36:52] exact Git hash right now, but you should
[36:54] always pin the versions of the
[36:56] frameworks. Um, because at least like
[36:58] you know things should uh keep working
[37:00] with that version of the framework and
[37:02] but then I also care about API
[37:04] stability. Like if I write my code now,
[37:06] I'm going to have to change it, right?
[37:07] So definitely like a lot of things
[37:08] changed in the last two weeks and that's
[37:10] why we're pinned to like the very recent
[37:12] uh version of the repo because so much
[37:14] changed in the last two weeks. Um but
[37:15] get as they're gearing up for 1.0 that's
[37:18] indicating that you know the they're
[37:20] feeling could pretty good about the
[37:22] actual shape of the API and that it
[37:24] shouldn't be changing very much.
[37:28] All right. Um asks what are uses for
[37:31] observability beyond debug including
[37:33] performance. Right. So um you know if
[37:36] you look at like app insights and um you
[37:39] know see the kind of things there um you
[37:42] know performance is one of them that's
[37:44] that's what I showed but really I only
[37:45] use the performance tag because it tab
[37:48] it makes it easiest for me to find the
[37:49] traces. So it's really performances
[37:52] performance and debugging quality,
[37:55] right? So you know once you have all
[37:57] these um traces in your you know
[38:01] exported uh exported into your your log
[38:04] workspace then you can pull them back
[38:06] out, right? So, um, you know, you could
[38:09] actually in like ask an agent, um, you
[38:14] know, look at a bunch of me my these
[38:15] logs and identify some, you know,
[38:18] examples of bad, you know, you know,
[38:21] issues, right? Um, that was actually um
[38:24] a talk that someone just gave. Let me
[38:26] see if I can find this talk blog blah
[38:29] blah blah blah blah blah. Oh, so this
[38:31] guy Himal, uh, definitely subscribe to
[38:34] him if you're into evaluation. um
[38:36] because he's like expert on evaluation
[38:39] and I just defer to him for really
[38:42] everything. So he just did a
[38:46] he just did a talk
[38:48] um a video about using claude code
[38:54] with traces from observability platform.
[38:57] He was using Arise Phoenix. That's
[38:59] another um platform I think and I think
[39:02] it's is it open telemetry?
[39:05] to see if it's open telemetry. Yeah, it
[39:08] does use open telemetry. So, this is yet
[39:09] another observability platform. Yeah. Um
[39:13] and you can run this open source too. I
[39:14] should add this one to the slides too.
[39:16] Um
[39:18] so he just Hamal just did this um talk
[39:20] where he was using claude code to pull
[39:23] in the traces from Phoenix and then ask
[39:28] it like hey look at these traces and um
[39:31] you know decide uh you know which ones
[39:35] um you know like find find examples of
[39:37] bad ones. Um, and then, you know, it's
[39:40] just saying like he uses he's using a
[39:42] coding agent to help him find um
[39:45] lowquality traces in the logs and then
[39:48] he can build automated evaluations based
[39:50] off of those results. Let me just find
[39:53] um his thing. Uh oh, it's actually
[39:56] coming up today. Oh, great. Okay. So,
[40:00] obviously I didn't wa watch the talk um
[40:02] since it hasn't happened yet. Uh let's
[40:05] wait. Is it today? Sign up to watch the
[40:07] recording.
[40:08] I feel like it said it's coming up
[40:10] February 19th, isn't that? Oh, no, that
[40:12] was last week. Okay. Okay. All right.
[40:14] So, you can watch the recording here.
[40:17] Um, and I think you could basically like
[40:18] apply this, you know, is the idea is
[40:20] using a coding agent
[40:24] in order to analyze system behavior and
[40:28] figure out what's wrong and then like
[40:29] you can build better evaluations, you
[40:31] can improve your prompts. Um, so, uh,
[40:34] yeah, but basically the point is you
[40:35] need to have those traces somewhere,
[40:37] right? In this case, they were sending
[40:38] the traces to Phoenix. Uh, but you could
[40:40] send the traces to
[40:42] App Insights and you just pull them back
[40:44] out um, you know, using like the Azure
[40:46] CLI. Uh, you can pull them back out of
[40:49] your of your logs, right? Like app
[40:50] insights is just like a pretty way of
[40:54] well arguer
[40:59] interface
[41:01] on top of um a bunch of data that's
[41:04] stored in a uh logs workspace.
[41:08] Um
[41:11] oh they have a new video. Okay. All
[41:12] right. But you can get raw access to the
[41:14] traces as well. Right. They're all in
[41:16] this traces
[41:18] um thing here. Right. So it's really
[41:20] just a bunch of rows that are being
[41:21] stored here and app insights adds a
[41:24] bunch of you know charts on top of it
[41:26] and here you can see you can even set up
[41:27] dashboards with graphana. I was just
[41:28] talking about how we have that graphana
[41:30] integration uh but the raw data is here.
[41:33] So you can pull these traces
[41:36] uh you know and then you could send
[41:37] these traces for uh you know to an agent
[41:41] to have it analyze um or to like the
[41:44] evaluation SDK you know you can do
[41:46] whatever whatever is helpful for you as
[41:49] long as you have that data there.
[41:54] All right we got a question from
[41:56] Chickadilly.
[41:58] We are in flight in developing LLM as a
[42:02] judge sort of thing. Given the latency
[42:05] that is added to the loop, it doesn't
[42:06] look like something that should be run
[42:07] while the user is interacting with the
[42:09] agent. In production, I've seen this as
[42:10] evaluation that would be kicked off ad
[42:13] hoc and maybe not covering every
[42:15] request. Yeah, I think that's that's um
[42:18] that that sounds really um correct.
[42:20] Yeah, let me find just where um
[42:24] um we just did we had like a blog post
[42:27] where we talked about this um where we
[42:29] tried to add based LLM as a judge step
[42:32] right so you know this is this was for
[42:34] rag um you know this is your standard
[42:36] rag right get the answer and so we tried
[42:39] adding reflection right so you know um
[42:42] we generate the answer and this is like
[42:44] a multi-step where we generate the
[42:46] answer where you evaluate the answer
[42:47] using that same SDK that I showed um if
[42:49] there's a, you know, a low score, then
[42:52] you're going to like see like, oh, why
[42:53] was that a low score? Do we need to do
[42:56] um another step here, uh, and then, you
[42:59] know, get back the result. And this
[43:01] added like way too many steps because
[43:03] this was like freaking like what, three
[43:05] more LLM calls. So, this was this was
[43:07] too much, especially once we made it a
[43:09] loop. This was like we let it do a
[43:10] single step. Multistep were like, "Oh,
[43:12] you can just keep doing this, right?"
[43:14] And it kept wanting to reflect and it
[43:16] did not get a better response. Um
[43:20] so this was like this actually kind of
[43:22] we did this and we thought it was going
[43:23] to improve things and a lot of times it
[43:25] didn't for many answers but this was
[43:27] like early experimentation and then um
[43:30] you know this this was in like I was
[43:32] doing this with um the AI search PM. So
[43:35] they did actually end up finding a
[43:37] better way of doing that um of doing
[43:40] that reflection step and that is built
[43:42] into the um AI search and I I talked
[43:45] about that last time. now. So they they
[43:47] did manage to add in a reflection step.
[43:49] Um but they had to think really
[43:51] carefully about how they did that
[43:53] reflection step and what they were
[43:55] reflecting on and um and really make it
[43:59] make it valuable. And still it's only
[44:02] like this is an option that you enable
[44:05] if you really really want it, if you
[44:07] really care about accuracy. Um, but
[44:10] usually we actually don't necessarily
[44:12] recommend adding it on because that
[44:14] iteration adds on another LM call and
[44:17] another retrieval and that adds to
[44:19] latency. So this is just say that it
[44:22] does add definitely adds latency
[44:25] whenever you add on any sort of
[44:27] additional step after generating the
[44:30] answer. Um, so I was suggesting because
[44:33] we talked about this in the live chat
[44:34] too, like you could during the answer
[44:36] generation phase, you could ask for a
[44:38] level of confidence and even display
[44:40] that level of confidence like um we
[44:42] didn't talk about hacks toolkit this
[44:44] time. Um, but that's this is like uh
[44:48] user you know best practices for
[44:52] um user experience when you're doing uh
[44:55] human
[44:57] uh human AI stuff. Um so the best thing
[45:00] is actually the design library and then
[45:02] examples. Uh examples. Okay. So make
[45:06] clear what the system can do. Um the one
[45:08] that I want to show is make clear how
[45:11] well the system can do. Make it clear.
[45:16] Uh
[45:18] right. So there I was trying to find an
[45:19] example where they actually showed they
[45:21] have all these examples from different
[45:22] tools which is uh I think really cool.
[45:26] Um communicate you know precision right.
[45:29] So if you can have it indicate
[45:32] how confident it is then you know that's
[45:35] it's something at least and you can you
[45:37] can use that to decide like you know
[45:39] whether um you know whether you want to
[45:42] do a reflection step that would be
[45:43] another thing u but anyway so yeah the
[45:46] other approach is that you do basically
[45:47] what's called online evaluations and
[45:49] there's even built-in support for online
[45:52] evaluations when you're doing foundry
[45:53] project agents that's one of the
[45:54] benefits of foundry project agents is
[45:56] that you can just enable online
[45:58] evaluations and it'll use the same
[46:00] evaluators that I was showing. Um, so
[46:03] that's that's a nice benefit there. But
[46:05] you could also just set that up yourself
[46:06] so that for a certain percentage of
[46:09] agent calls, you would, you know,
[46:12] basically queue up an evaluation. Um,
[46:15] you would want to do that in a separate
[46:16] thread, not in the the userfacing
[46:18] thread, right? So you'd want to kick
[46:20] that off in another thread and sample it
[46:23] and then uh you know surface that inh in
[46:27] a dashboard somewhere so that you knew.
[46:29] Let's see if we can find Microsoft learn
[46:31] documentation about online evaluations.
[46:33] I
[46:35] um oh that is way too generic. Um for
[46:40] agents okay
[46:43] let's see
[46:46] um aations from the portal. Where's the
[46:49] online evaluate marks of foundry?
[46:55] Create agent threads.
[46:59] uh
[47:01] evaluation. Okay, maybe it's evaluations
[47:04] in the portal
[47:11] model.
[47:18] I've seen it even when running a foundry
[47:20] agent, but I'm not finding the docs on
[47:22] it here. Um,
[47:26] so yeah. So, but it's it's generally
[47:28] called online evaluations and um you you
[47:32] know it it's built in to many many you
[47:36] know kind of agent platforms and also
[47:37] even to some observability platforms
[47:39] like Langfuse. Um I think I think for us
[47:42] it's only built in if you're using
[47:44] Foundry agents. I don't think it's built
[47:47] in in for for um for any other way just
[47:51] because it's it it would be harder to to
[47:53] set it up. Um, but you could you could
[47:56] set up the the same idea yourself and
[47:58] just sample certain ones and and set up
[48:01] a dashboard and you just want to see,
[48:03] you know, how things are changing. Let
[48:04] me see if I can get like good docs from
[48:06] like maybe Langfuse or or Langmith would
[48:08] happen. Um, just talking about the
[48:11] general concept
[48:13] of
[48:15] online
[48:17] evaluations.
[48:23] Uh
[48:31] let's see. I I saw them give a talk
[48:33] about it, but um
[48:37] continuous Oh, it's also called
[48:39] continuous evaluation. That would be
[48:40] another thing to um when you're
[48:44] researching it is the idea of continuous
[48:46] evaluation.
[48:50] Um, but I'm not seeing the like the
[48:52] actual box they have. Let's try
[48:54] linksmith online evaluations or
[48:57] continuous evaluation.
[49:03] Continuously a build.
[49:08] Yeah. So they call it Yeah. Okay. Test
[49:11] or run online evaluations on production
[49:13] traffic. Right. So this is the idea of
[49:15] it and you know different platforms have
[49:18] different ways of doing it. So those are
[49:20] the terms you want to look for is online
[49:22] evaluation and continuous evaluation.
[49:24] Let's see what happens when we search
[49:26] Microsoft learn.
[49:30] Oh, okay. I found something this time.
[49:33] Continuously evaluate
[49:35] your AI agents. Great. All right. Um and
[49:40] this is using Okay. Azure AI projects.
[49:43] Select evaluators.
[49:45] Okay. So this is using the new way of
[49:48] doing it. Um,
[49:51] so you set up your evaluators blah blah
[49:54] blah.
[49:55] All right. Do we set up like a sampling
[49:57] amount? Get the evaluation result using
[49:59] app insight. So this also is it is
[50:02] storing it in those logs that I showed
[50:03] before. Uh, it's sh storing it in the
[50:06] traces table that we were just showing.
[50:09] Oh, there we go. Sampling configuration.
[50:11] Okay, great. So this will work for I
[50:14] think wait actually let's see if this is
[50:16] only for I think it's only for foundry
[50:18] agents but let's see so create agent
[50:20] evaluation yeah because it's based off
[50:22] of the agent threads so it assumes
[50:25] you're using a foundry agent so this is
[50:27] this is one advantage of using the
[50:28] foundry agent platform is that it does
[50:32] have this online evaluation built in
[50:34] here
[50:38] and this is definitely
[50:41] Nachier.
[50:49] All right.
[50:51] I see Chickell's timing. Okay, cool.
[50:56] Um, but you can try setting up yourself,
[50:57] too. So, you just want to basically do
[50:59] the same idea.
[51:03] Oh, let me not close tabs. Okay. All
[51:06] right. We got three minutes.
[51:09] Anything else? So, we can call it eat
[51:12] some lunch, dinner, midnight snack, or
[51:15] whatever. Um,
[51:18] remember, we've got a whole another week
[51:20] of this series coming up where we're
[51:22] going to talk about workflows.
[51:25] So, I will have a bunch of examples for
[51:29] those. The code sample repo is going to
[51:32] triple in size. So, you'll definitely be
[51:34] doing a git pool for next week as you
[51:37] see all the workflow code samples
[51:39] coming.
[51:42] All right, cool. Okay, thank you
[51:44] everyone. I hope to see you next week.
[51:47] Bye.
