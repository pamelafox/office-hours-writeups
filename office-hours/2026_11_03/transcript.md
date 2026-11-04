[00:00] Welcome everyone to this weekly office
[00:03] hours. Uh we actually we skipped last
[00:07] week because of GitHub Universe since I
[00:09] was there. Uh so we have a few more
[00:12] things to talk about this week. As
[00:15] usual, I've rounded up the news for this
[00:18] week. So we'll kind of go through go
[00:21] through these news. Um but we can also
[00:24] talk about whatever you all are
[00:27] interested in. So at the very top I
[00:31] actually put that we now have the
[00:34] decisions API for Azure OpenAI. Uh this
[00:38] is something we've in the past we've
[00:40] played around with it from openai.com
[00:43] but now we've got it on Azure. Uh it is
[00:46] basically a version of the GP6 Luna
[00:48] model. So that's what it uses behind the
[00:50] scenes. Uh which means it's multimodal
[00:53] and it has a 1 million context window.
[00:55] So that's very cool. Uh so we've got
[00:57] these docs now.
[01:00] And we're working on um a PR that adds
[01:05] here we go. Uh
[01:08] so this PR here
[01:11] adds uh a bunch of code samples across
[01:15] different languages. So whichever
[01:17] language uh you want to use
[01:20] um you can do that. So here you can see
[01:23] Python.
[01:24] Um,
[01:26] so I just tested out the I tested out
[01:29] the Python uh the other day. Uh, so I
[01:33] actually have that I have that open
[01:35] actually. Let me get that open here. Oh.
[01:39] Uh, so here, right? So we've got in
[01:45] Python the decisions example.
[01:48] Uh, so we can see here how to how to set
[01:50] it up. Uh so
[01:54] you know we connect and we can connect
[01:55] either using you know keyless or keys.
[01:58] So you know um if we're doing keyless
[02:01] here this is using the ACD credential
[02:03] otherwise we can use a key and then uh
[02:07] we you know we connect to using the
[02:09] openAI client to
[02:12] our open Azure OpenAI endpoint
[02:16] V1
[02:18] and then
[02:20] uh we can actually you know use the
[02:23] client to create a decision. So here we
[02:26] tell it you know we give it a user input
[02:28] and say uh so this is a multimodal
[02:31] example where it expects inspects a
[02:34] photo
[02:36] and then it asks we have a bunch of
[02:38] questions here. Uh this one actually I
[02:42] think this one of I gave feedback that
[02:43] this code example is confusing because
[02:45] it tries to do too many things at once.
[02:47] Um but here let me let me run it.
[02:51] So without a photo
[02:55] um
[02:56] it just says uh I was charged twice for
[03:00] order 123 and then we tell it
[03:04] uh which department should handle this
[03:05] request that sort of thing right so then
[03:08] when we get back answers
[03:10] uh we get back oh is it a re is there a
[03:12] refund requested what was the department
[03:14] choice what was the severity so you can
[03:17] see each of them has a value and a
[03:19] confidence right so this is how decision
[03:20] models work is that you get back these
[03:23] values and you get confidences for for
[03:25] each of them.
[03:28] Uh so there you go. So it is now
[03:31] supported on Azure OpenAI. Um so you can
[03:37] start so now you actually have two
[03:39] decision models. Um so I'm working on
[03:42] Ignite demo right now and and now I can
[03:44] have to decide which one to use, right?
[03:46] Because there's also Microsoft decision
[03:48] one. Um and that's also available in in
[03:53] foundry. So you uh but this is a much
[03:56] smaller context window and
[03:59] it is not multimodal but it might be
[04:03] faster or cheaper. What was the pricing?
[04:05] Let's look at the pricing. So this one
[04:07] input tokens cost 0.042.
[04:11] Okay. And then what is the pricing on
[04:14] this one?
[04:18] Uh
[04:22] for pricing information. Okay,
[04:26] let's go over here. Maybe it's just
[04:28] literally the same pricing as
[04:31] Luna 6.
[04:36] Okay, so we have all this stuff. Yeah,
[04:38] so it's probably just the same.
[04:41] Let's see. There's nothing about
[04:42] decision, so it must just be this. So
[04:44] GBD6 Luna
[04:47] um
[04:48] input output so 0.10.
[04:52] Yeah. So I think that that's the
[04:54] difference is that here this looks
[04:56] really really cheap. Um so I think I
[04:59] think that your you know price pointwise
[05:03] decision one is going to be your your
[05:06] cheaper option. Um
[05:09] so you may want to you know go with that
[05:11] if it works. Um otherwise if you need
[05:15] the longer context and the multimodal
[05:17] support then you've got this Azure
[05:19] opening eye decisions API instead.
[05:23] All right. Uh so definitely check that
[05:25] out. There's there's so many places
[05:27] already where I'm starting to bring in
[05:29] decision models um you know for routing
[05:32] classification
[05:34] and um judge evaluation that sort of
[05:37] stuff. There's a lot of places where you
[05:40] might be able to bring it in as long as
[05:42] you calibrate and see that it's working
[05:43] well.
[05:46] All right. Besides that, uh last week
[05:48] was GitHub Universe. Uh so there was
[05:52] some announcements at GitHub Universe.
[05:56] Um there actually wasn't like a huge
[05:59] number of announcements. Um but uh there
[06:02] were a few. So one change is that
[06:04] there's now what we call co-pilot
[06:06] fusion. This is what we used to call
[06:08] hydrofusion. And we've talked about
[06:09] hydrofusion
[06:11] here before. Um, basically it's a, you
[06:15] know, instead of just doing a straight
[06:18] shot with a single model, it's going to
[06:20] choose an orchestration pattern or an
[06:22] execution pattern. So, we've got single
[06:24] cascade or critique. Um, usually
[06:28] [clears throat] I look at the
[06:29] Hydrofusion
[06:31] uh D. Oh, hydro fusion
[06:36] blog post.
[06:40] There we go. I think this one.
[06:43] Yeah. So, this is a better
[06:46] uh visualization here. Right. So, you
[06:48] you know, we've got a model that
[06:51] uh looks at the task and decides what
[06:53] kind of task it is and how to route it.
[06:56] And then that goes to either single,
[06:58] cascade or critique and then we get the
[07:01] results. So that is copilot fusion. Uh
[07:05] so you can try it out in GitHub copilot
[07:08] wherever you use your you know copilot
[07:10] at or whatnot. Uh then we also had a
[07:12] bunch of changes in the app. So if we go
[07:15] to the app uh you can see that I was
[07:16] making it using it to make the news. Um
[07:19] but the significant thing here is
[07:21] projects right well two thing two big
[07:23] things automations and projects. So
[07:25] projects this is brand new. So this is
[07:28] the most useful for um cross repo work.
[07:32] So for example like earlier I was I
[07:35] tried to do um I tried to like do an
[07:38] upgrade to Python 311 across a bunch of
[07:40] repos. Um
[07:43] uh say let's say uh look at my repos
[07:48] listed on github.comfox.
[07:53] identify which of them need upgrading to
[07:58] Python 311.
[08:01] [clears throat]
[08:02] So that's what so these projects these
[08:04] are really good for cross repo work
[08:06] right. So, if you have a maybe like an
[08:08] upgrade Oh, you can hear my [laughter]
[08:11] as usual. You can hear my agent hook. If
[08:13] you're new to office hours, you'll hear
[08:15] my child giggling every so often.
[08:24] Uh, so here, right? So, the thing that's
[08:27] really good about this is that it it's
[08:29] very good at scanning up parallel
[08:31] sessions. This one's gonna maybe be a
[08:34] lot of work because it's going to do
[08:35] like 60 repos or something like that. Uh
[08:39] maybe I should do an easier one. Um oh,
[08:43] I had an idea actually. Uh
[08:46] let me
[08:48] I just want to like find examples that
[08:50] show off
[08:53] um Okay, here we go.
[08:56] All right, let's see. I'm going to say
[08:58] okay. So I'm going to also do this one
[08:59] and say I have
[09:02] Coco R data across these four repos.
[09:08] Identify the data in each one and
[09:12] whether they are in sync. All right. So
[09:15] here's a here's another case where it's
[09:17] clearly a cross repo thing. Uh so here
[09:22] okay it's doing lots of scanning still.
[09:25] Um, this one. Okay, this one we should
[09:27] get faster to it making child sessions
[09:30] in it.
[09:32] Uh,
[09:34] oh, it can't it can't reach all the
[09:36] repos. [clears throat]
[09:38] Some of these are we're we're working on
[09:40] our Ignite Ignite demos. So, these are
[09:44] some private repos here. Uh,
[09:49] okay.
[09:56] All right, this one is not making child
[09:59] sessions. I just want to show you child
[10:02] sessions. Okay, while that's working,
[10:06] um Oh, let me think of another one. Um
[10:10] uh Okay. Um
[10:15] how about this? All right, we'll do this
[10:16] one and say, "Try out brand new designs
[10:22] for my website look and feel.
[10:27] Give me screenshots at the end."
[10:32] All right, so let's try this one. Okay,
[10:36] so this is a project. This one didn't
[10:37] end up making making sub sessions, so
[10:40] that's not so exciting. Um, this one.
[10:46] All right, let's just say likely. Okay.
[10:48] All right. Startups. Okay. Upgrade the
[10:54] 3.81s
[10:57] and 3.91s.
[11:00] Okay. So, let's see what that's going to
[11:02] do. Website design.
[11:15] All right. Upgrading 16 repos.
[11:27] Well, it is not making it. I guess it
[11:29] it's deciding it doesn't need to use.
[11:33] Last time I used this, it made child
[11:35] sessions for everything and you could
[11:37] like follow the child sessions. I maybe
[11:38] I have to explicitly tell it to use
[11:41] child sessions. I'm surprised actually.
[11:42] How is it managing? Oh, creating a work
[11:44] tree.
[11:46] All right, it's doing everything without
[11:47] using child sessions. So maybe
[11:50] uh can you do it in child sessions?
[11:54] Maybe you have to explicitly ask for it
[11:55] to do it in child sessions.
[12:00] Uh because that's how it worked for me
[12:02] when I was doing the thing.
[12:05] So Adam has a comment about Copilot
[12:07] Fusion. Looks like it tries to smartly
[12:08] route to a proper model. Yeah. So it's a
[12:10] combine of trying to find the right
[12:12] model and trying to find the right
[12:13] orchestration.
[12:15] So both of those um so it says so Adam
[12:18] says at the time it felt like it might
[12:19] conflict with some of the already
[12:20] available agent skills or agent
[12:21] instructions. Yeah. So that's the thing
[12:24] if you already have um orchestration
[12:28] then you know because this was because a
[12:31] lot of people weren't setting up their
[12:32] own you know custom orchestration. If
[12:34] you already are doing your own custom
[12:36] orchestration, then you probably don't
[12:38] need fusion. Um, if you, you know, if
[12:41] you think it's working well. Oh, here we
[12:43] do. Okay, this is what I want to show.
[12:45] All right, so maybe we have to
[12:46] explicitly ask it to do child sessions.
[12:48] It also might depend on the model. So, I
[12:50] just tell it, can you do it in child
[12:52] sessions? Because then what you get is
[12:53] this really nice um overview here of
[12:57] your project and the work that's
[12:58] happening in parallel. And that's nice
[13:01] because then what you can also do is you
[13:03] can [laughter]
[13:05] um
[13:07] oh switch a child to uh can we
[13:11] yolo them all? [laughter]
[13:14] Um
[13:16] here we go. Trust
[13:19] seems like permissions maybe changed. Um
[13:23] [snorts]
[13:24] somebody is doing a lot of Okay. Which
[13:27] one is that all here? you'll need to
[13:30] turn it on. Oh, so maybe my interactive
[13:33] tool permissions. I have that on Pro
[13:35] Ball. Okay. [clears throat]
[13:37] Um, so then we can go bear and make sure
[13:40] that's on autopilot. It looks good.
[13:49] Wow. Okay. Well, I feel like I'm running
[13:52] into issues now. It says I couldn't make
[13:53] the redesign because this session is not
[13:55] allowed to write files.
[13:58] All right. So, I must have something
[14:00] some permission set up on my version of
[14:03] the Copilot app that is preventing this
[14:06] from working as well. Uh, but uh
[14:09] definitely experiment with it. Uh, and
[14:12] there's probably different settings.
[14:13] I'll I'll ask my colleagues about that.
[14:16] The other thing that changed was
[14:17] automations. So, now with automations,
[14:20] what they're um trying to do is make it
[14:23] easier to do automation. So, in fact,
[14:25] you could just say like every day at
[14:28] 1000 p.m. uh check daily issues for
[14:32] Pamela Fox site. Right? So, you make
[14:36] that automation, right? And so, here I'm
[14:37] just describing it. Um, actually, let me
[14:41] do one that's going to have actual
[14:43] issues
[14:45] down. Okay. And then we select our repo.
[14:48] Okay.
[14:50] And there we go.
[14:53] So that so basically they're trying to
[14:54] make it super easy to make automations
[14:59] and so then I start that session.
[15:03] So that's going to that's going to make
[15:06] the automations
[15:18] does Oh good question. Yeah. Does GitHub
[15:20] copilot support the MC events pack?
[15:22] Okay. All right. All right. Well, first
[15:22] let's look at this. Sorry. This
[15:25] [laughter] what happens when we make
[15:26] lots of sessions. We get lots of agents
[15:28] up agent updates. So, what you can see
[15:31] is what it did is that it based on my
[15:33] description, it created the automation.
[15:36] So, it says, "Okay, we're going to use
[15:38] the cron trigger
[15:40] and it said it's going to do
[15:44] okay. There's too many things happening
[15:46] now in the app." Um and then oh it even
[15:49] like made a much more formal uh
[15:52] description right so that was a big
[15:54] change the launch was making it so that
[15:58] you know using an LLM to write your
[16:01] automation and then the automation
[16:02] itself will also use an LLM but
[16:04] basically they're just trying to make it
[16:05] easier to make automations right and
[16:07] then you could add this automation and
[16:09] then it would be here um however I want
[16:12] to point out you can also click create
[16:13] manually so because if you're happy to
[16:15] do all this yourself because then I
[16:17] actually prefer create manually because
[16:18] then look, you can see all these
[16:20] triggers here. So you can have Oh, I
[16:21] didn't know you could have automation
[16:22] failed. Yeah. So that I love this
[16:24] because it's like you can discover what
[16:26] all the possible triggers are. So
[16:27] obviously you can do stuff on a
[16:29] schedule. That's easy. But then what's
[16:30] interesting is like new issue,
[16:32] automation failed, code scanning alert,
[16:35] dependent alert, discussion comment,
[16:37] pull request, secret, right? So these
[16:39] are all super useful. And then the thing
[16:41] is you can also have them um you know
[16:44] you can tell them to run in the cloud
[16:47] right um and actually it looks like it
[16:49] defaults to run in the cloud when you do
[16:50] a trigger of dependabot alert.
[16:53] So that's that's really helpful, right?
[16:55] So um yeah, so I like I like to create
[16:58] manually because then I can get ideas
[17:00] for all the different triggers there are
[17:02] and decide like okay, you know, um you
[17:06] know what do what what do I want to make
[17:08] here, right? And then if they run in the
[17:09] cloud, then that's really helpful.
[17:10] They're going to run even when my
[17:12] machine is not is not on. Um, so I think
[17:15] if you're doing things that are
[17:16] generally useful for the whole repo,
[17:19] like everybody is using a repo, then I
[17:21] would do, you know, I would run them in
[17:23] the cloud instead.
[17:26] Um,
[17:27] oh, I see some comments. All right. Um,
[17:30] can the cron switch to web option? So in
[17:33] cron, you get a cron syntax, right? This
[17:36] is the cron, what you would normally put
[17:37] in cron tab.yamel on your computer. Um,
[17:42] that's in cron. Uh let me see do you get
[17:45] and this one does not seem to have the
[17:49] option for cloud. Let me see if daily
[17:51] has this one. Daily has the option for
[17:53] cloud. It's interesting. So cron does
[17:56] not have the option for cloud. So
[17:58] presumably if it's cron it can only run
[18:02] on your reader. Um which is interesting.
[18:04] That's another question I might ask the
[18:07] app team about.
[18:09] Um oh you can add another trigger. So
[18:12] that's cool. So you can have multiple
[18:15] multiple triggers there. Uh so there but
[18:18] yeah all of the rest of these can run in
[18:20] the cloud. Um can the cron switch to web
[18:24] hook? So I don't think so since the cron
[18:26] is only seems to only be working locally
[18:30] and I don't see like a generic
[18:33] this one's cool workflow like a GitHub
[18:35] actions workflow. So you can run it when
[18:37] a workflow completes. That's quite neat.
[18:40] Um, yeah, I don't see anything that's
[18:42] generically a web hook, but I presume
[18:44] all of these maybe correspond to web
[18:46] hooks. I actually haven't written much
[18:49] of my own handling of GitHub web hooks.
[18:53] Um, oh, you're trying to like have
[18:54] support for just any arbitrary web hook.
[18:57] Oo, that's a good question. That's
[18:58] another good question for the app team.
[19:02] Yeah, you want arbitrary. So, just non-
[19:04] GitHub web hooks is what you're looking
[19:05] for.
[19:08] Uh, so it doesn't look like it now. Um
[19:10] but I can file a request. Um
[19:15] uh yeah so Bernard says is the
[19:17] automation a parallel project mechanism
[19:18] to GitHub agentic workflows? Yeah this
[19:20] came up at GitHub universe right so
[19:22] we've talked about GitHub agentic
[19:26] workflows before
[19:29] um and these are still very much you
[19:32] know supported and um I saw that that
[19:36] team was at GitHub universe as well. So,
[19:41] um I think right now the lines are
[19:43] definitely blurring because you could
[19:45] obviously you know make you know
[19:47] something similar to GitHub aogentic
[19:49] workflows here. Um
[19:53] I think I think you would basically I
[19:55] would say probably just try to make them
[19:57] here. Um or I this is a much lower
[20:01] barrier, right? I I think like heentic
[20:03] workflows are that to me feels like a a
[20:06] little higher friction, right? So I
[20:08] would say try them here. Um but if you
[20:11] find that you know these ones aren't
[20:13] working as well then then maybe when you
[20:15] move to GitHub aogentic workflows when
[20:17] you need more control and complexity um
[20:22] also like aentic workflows I think those
[20:24] are like checked into you know actually
[20:27] checked into your repo. So they are more
[20:29] you can reason about them you can do
[20:31] code review on them right. So, I I think
[20:33] that if you are, you know, you've got a
[20:36] repo and you've got multiple team
[20:38] members on that repo, then you may still
[20:40] want to be using GitHub agentic uh
[20:43] workflows instead because I think I feel
[20:44] like that's a little more team friendly.
[20:49] Um,
[20:51] so yeah, so this question is, GitHub
[20:54] Copilot support the MCP event spec? Let
[20:57] me just ping my usual GitHub copilot MCP
[21:00] people.
[21:02] Um, [clears throat]
[21:04] does GitHub pilot support the MP events?
[21:11] Uh, well, of course, the answer is
[21:13] probably no. Um, we can go to can I
[21:15] use.dev and we can see who supports MP
[21:18] events. Um,
[21:20] where is it? Where's events?
[21:23] Uh, really? There's no events on here.
[21:25] Let's see.
[21:27] Uh, how might have been apps? Perhaps
[21:36] events. No triggers. No.
[21:40] H. All right. Let me ping.
[21:43] Um,
[21:47] is MSV events filterable?
[21:53] I'm not seeing it.
[21:57] All right. Um, yeah, I'm sure the answer
[22:00] is no because I feel like I would know
[22:02] about it if it did.
[22:07] Uh, but let me just go and nag the team
[22:09] about it anyway so that we can make it
[22:13] clear that we would like it to support
[22:16] the MC event spec. What I asked about
[22:18] last week actually was um skills over
[22:20] MCP. Uh, so let's actually
[22:25] Oh my gosh. Stop with the slop. All
[22:28] right. Uh,
[22:30] so Pierce, just trying to find because
[22:33] people were very excited about skills
[22:36] over speed. Oh, I still need to reply to
[22:39] that one. Um, okay. All right. So, is
[22:42] there any tracking support?
[22:45] Um,
[22:47] okay. So, he said not at the moment. And
[22:50] he doesn't actually like the idea of
[22:52] skills over MCP.
[22:55] Um, but I do uh let me just reply that
[22:58] devs are super excited about skills over
[23:03] MCP since it unlocks the ability to
[23:07] personalize skills based on the logged
[23:11] in user.
[23:14] Don't think that's possible with
[23:17] plugins.
[23:22] Okay, I'll just say we'd also love
[23:26] skills over MCP. All right, just gonna
[23:28] put in a good word for all of our
[23:30] favorite MCP feature.
[23:34] Um, all right. All right. So, I pinged
[23:37] the team about those.
[23:39] Um, so Nomi says the GHcon trigger for
[23:43] GH actions is four to five hours late.
[23:45] So, that's using a different mechanism,
[23:48] right? Events that trigger workflows.
[23:51] Um,
[23:54] Ah, I see this one you're saying on this
[23:57] cron interesting
[24:00] and it's always is it this is this what
[24:04] you're finding? So even in your
[24:05] workflows when you do a cron it's just
[24:07] late
[24:10] and you do you specify the time zone
[24:13] [laughter] because then it could be time
[24:14] zone issues. I assume it's not but
[24:17] um okay.
[24:21] Yes. All right.
[24:24] H
[24:27] uh default time zone GCC GitHub
[24:29] community discussion. All right. Let's
[24:32] find the
[24:34] uh GitHub community. Is there any
[24:39] discuss discussions and product
[24:41] feedback? This is also other place like
[24:44] to put to put um ideas. So let's see.
[24:48] Kron is late.
[24:51] scheduled. Oh, is this one 3 to 6.5
[24:56] hours late?
[25:01] Okay, this looks very similar. Our
[25:04] workflows blah blah blah each run.
[25:09] Okay, so um
[25:13] this seems like the relevant issue. Um I
[25:17] can Where would I post this? Okay, I'll
[25:20] have to figure out which Slack channel
[25:22] corresponds to GitHub actions because I
[25:24] usually
[25:26] um not find bugs in that. But um I can
[25:29] if you you may want to add a plus like
[25:31] you know more than just a plus one.
[25:34] If you can add a little more detail here
[25:36] just to show that there's additional
[25:38] people affected then I can
[25:42] uh post that in the uh in our Slack for
[25:47] GitHub actions because it looks like
[25:49] maybe it's a regression did like did
[25:51] this work before presumably
[25:53] um you know maybe some things happening
[25:55] there were obviously a lot of releases
[25:57] last week as part of GitHub universe so
[25:59] I think some of those you know there
[26:01] could be some regressions as part of
[26:03] those releases.
[26:07] Uh, all right. Let's see. Okay. So,
[26:10] yeah. So, play around with automations.
[26:14] Uh, let's see how our projects ended up
[26:16] going. Okay. All right. Uh, so it did
[26:20] manage to do a few things there. Um,
[26:25] because I approved it. So yeah, the
[26:28] generator with projects is that you get
[26:30] this overview and you can dig into each
[26:33] of the child sessions. So I think it's
[26:34] just a nicer way of handling cross repo
[26:37] and multi session work. Uh so that's
[26:40] when I would use it. Um oh gosh, it just
[26:43] made 16 PRs. Yay. Uh [laughter]
[26:47] problem with any sort of upgrade is that
[26:48] it requires, you know, some amount of
[26:51] time to do. I have not been able to get
[26:53] it to the point where I can upgrade
[26:54] everything and just have it just, you
[26:57] know, just work.
[26:59] Okay. All right. So, that is I think
[27:02] that's most of what we had for GitHub
[27:05] Universe, right? So, we had Fusion, we
[27:07] had projects. Um, it oh, it does say
[27:09] teams can share automations.
[27:14] Um,
[27:16] so build shared workflows for your
[27:19] teams.
[27:20] Uh,
[27:22] I need to stop. Here we go. All right.
[27:27] Um, okay. So, how they work. Visible to
[27:29] your team. Build to the repository
[27:31] owner. Act as co-pilot so that they're
[27:34] attributed to co-pilot. Build to last.
[27:36] Okay. Create a shared automation. When
[27:38] you create an automation, choose shared
[27:41] under type. Okay. Let's go ahead and
[27:44] check that out again. So, automations,
[27:47] go here, edit, and then under type. I
[27:51] think that one's not going to work
[27:52] because it's this is another I'm just
[27:55] noting noting for myself for the
[27:57] transcript is that um when we
[28:00] automatically created it, it used a cron
[28:02] type and the cron type does not seem
[28:04] compatible with cloud and I think what
[28:05] we really want is cloud. Um so, let's
[28:09] see if we look at this one. I think this
[28:12] one
[28:14] maybe we have to do like um okay all
[28:17] right we'll just try doing a new
[28:18] automation so we can get the thing new
[28:20] automation create manually. Oh it was on
[28:23] there. So when we
[28:25] if you click it here so maybe you have
[28:27] to that's another question is can we
[28:29] change it to shared after the fact or do
[28:31] you have to start it off shared? So yeah
[28:34] if you're doing one for teams and I also
[28:36] don't see is there a way to make it
[28:38] shared. Okay. Another question is how do
[28:41] we mark it as shared when we're using
[28:44] Oh, there it is. Right here. Type. Okay.
[28:46] All right. So, yeah, when you're
[28:48] creating it, you would mark it as
[28:49] shared.
[28:51] And then where does it show up? Uh,
[28:57] all right. Let's just make one and see
[28:58] where it shows up. Daily issue report.
[29:02] Run in the clouds. Select tools
[29:05] tree. look for new issues and summarize
[29:10] them in a table. Okay. All right. We're
[29:14] just doing a little experiment here.
[29:16] Okay. Um, interesting. It's trying to
[29:20] load. Well, my repository doesn't have
[29:21] any MCP servers, so that would make
[29:23] sense. All right. Let's just screenshot.
[29:25] That is another issue. Look at this.
[29:28] Repository not found.
[29:31] Weird. Okay, let's try it again.
[29:35] could not. All right, that's this is why
[29:38] we need to try stuff out that's new so
[29:39] we can find all the bugs. So, let's try
[29:42] I'll just give it a random one. You
[29:43] should be able to find this one. Okay.
[29:46] All right. So,
[29:48] AI credit limits. Oh, that's nice. You
[29:51] can set limits. Little tokconomics here.
[29:54] Create a little budget. Okay.
[29:57] So, daily nine o'clock. All right.
[30:02] Uh I [laughter] see lots of your normie
[30:05] friends have automations that destroy
[30:07] their credit totals. Um so Nomi says
[30:10] what is crown cron and cloud mean. Um so
[30:13] there's two there's all these trigger
[30:14] types here and there's cron which means
[30:18] you can specify arbitrary cron syntax
[30:20] because cron syntax is like a particular
[30:23] um syntax that you use in a cron tab.
[30:25] And then but then there's also just
[30:27] simply daily, weekly, hourly. Um, so
[30:29] when I picked cron, I didn't have as
[30:31] many options. So I'm picking daily here
[30:33] so that I can also run in the cloud,
[30:35] right? Because if this is a shared
[30:36] automation then, um, I'm actually
[30:40] surprised that you could do how could
[30:41] Yeah, if you do if you don't do run in
[30:43] the cloud, you don't even have the
[30:44] option to do shared. So I think you have
[30:46] to do run in the cloud if you want it to
[30:48] be shared. All right. So I'm going to
[30:50] say create. And then what I'm curious
[30:53] about is
[30:56] um whether can we okay run via API.
[31:01] Okay. So you have a way of running it
[31:02] via an API. Does this show up somewhere
[31:07] um on my actual
[31:10] repo, right? Because this is the shared
[31:13] a shared automation
[31:17] agent.
[31:20] Here we go. It does show up. Okay,
[31:22] automations. There we go. Okay, we're
[31:25] learning so much. All right, so um the
[31:28] agents tab has automations. And when we
[31:33] do shared Oh, you can even see personal
[31:35] there. Oh, that's very nice. In this
[31:37] case, it's, you know, this is literally
[31:38] my personal website. So, I could just do
[31:40] personal, but it doesn't matter. Um, so
[31:42] yeah. So, there is the daily uh issue
[31:46] report there. Um, so then we could, you
[31:48] know, once it runs. So none of them have
[31:49] run so far. So we don't have anything
[31:51] cool to see. U but then once it runs uh
[31:55] you know we' be able to see it and
[31:56] everyone in the repo would be able to
[31:57] see it as well.
[32:00] Uh the other thing that's worth pointing
[32:02] out on this note is that GitHub Copilot
[32:04] Cloud agents have gotten a lot better.
[32:07] So I actually I use them the other day
[32:09] from the um the C-pilot app. Uh so if
[32:13] you have I'll show my C-pilot app. Okay.
[32:16] Uh Uh,
[32:20] all right. So,
[32:22] I you know, I was like at ballet class
[32:24] for my kid and decided I would, you
[32:26] know, do little little things in here.
[32:28] So, you can use the Copilot app and you
[32:31] can make, you know, a new um session and
[32:34] you can either make the sessions tied to
[32:35] a repo or in my case, I was just cutting
[32:39] out um papel pic for diia muertos. So, I
[32:43] made a new session that wasn't in a repo
[32:45] at all. So that's cool is that you can
[32:46] now use the copilot tab from the mobile
[32:50] app just for arbitrary work, right?
[32:52] Because I was like, well, I want an
[32:54] agent that can write code because I
[32:56] think it's going to have to write Python
[32:57] in order to, you know, like make these
[32:59] SVGs and stuff. Um, so I decided to use
[33:02] the CIT app. So I will say the, you
[33:04] know, GitHub mobile app, the C-pilot tab
[33:07] is working much better. And then of
[33:08] course you can also,
[33:10] um, you know, you can also do things
[33:12] tied to a repo. So at the same time in
[33:14] parallel I um I worked on a repo and had
[33:18] it triage all the issues cut a new like
[33:21] make a new PR merge it all. Um so yeah
[33:25] so you can you can do a lot. So then you
[33:27] can also like the nice thing is once
[33:29] you're doing that then you know once I
[33:31] returned back to my computer I just went
[33:35] to github.com/copilot
[33:39] and here you know this is using the
[33:41] cloud agent as well. So then I could
[33:44] this was the you know what I started on
[33:46] mobile so you can see you know started
[33:48] it via GitHub mobile two days ago. Um,
[33:51] so I can resume that session and and
[33:54] then I can keep chatting. Right? So
[33:55] these were all messages that once I got
[33:56] back to my my machine with my um with my
[34:01] you know printer and cutter um then I
[34:03] was able to resume the session. So uh so
[34:06] yeah this was a nice exper uh
[34:08] experience. Um so do consider cloud
[34:11] agents just because that's going to give
[34:13] you more portability across different
[34:16] devices. Um and it's there's more kind
[34:19] of sharability as well like because if
[34:21] you use GitHub copilot inside teams or
[34:24] slack then those become shared sessions
[34:27] that anyone you know whoever's on that
[34:29] can see um so that's quite convenient.
[34:32] Um this was the other one that I started
[34:34] from GitHub mobile. So uh so yeah so
[34:37] that is another thing that improved at
[34:40] uh at GitHub universe was cloud agents.
[34:43] Uh so do do consider what you can do in
[34:46] the cloud and what benefits you get from
[34:48] using a cloud agent. Uh it takes a
[34:50] little more setup right like sometimes
[34:52] you're going to have to configure MCP
[34:53] servers. Right now you can't configure
[34:55] like the base image that it uses. Um but
[34:58] that should improve going forward.
[35:02] Uh cool. All right. What else? Um,
[35:07] oh yeah, this is this is important.
[35:09] Okay, so we've talked about the GitHub
[35:11] copilot SDK and the GitHub copilot
[35:14] harness. So two things changed. Um, so
[35:16] one is that in oh it's not changed in
[35:20] this one, but um generally in VS Code
[35:23] what you should see is that it now
[35:26] defaults to the co-pilot harness, right?
[35:28] So when you look down here um it should
[35:31] say co-pilot or maybe it doesn't even
[35:33] show anything at all. Um but that means
[35:35] it's using the copilot harness versus
[35:36] the local harness. So you know for a
[35:39] long time VS code and and the GitHub
[35:41] copilot app and CLI had two different
[35:43] harnesses which is like the coding agent
[35:46] uh logic and so you get different
[35:48] results if you ran the same task across
[35:50] both of them but um basically you know
[35:54] that was confusing for people to have
[35:56] such different experiences and it's also
[35:58] just repeated engineering work to be you
[36:01] know working on different harnesses. So
[36:02] now VS Code is deprecating their old
[36:05] harness um and there's some features
[36:08] that the old harness supported that the
[36:10] new one doesn't. So you do have to look
[36:13] out for that um and report it if you
[36:16] think it needs to be brought back. Uh so
[36:18] yeah going forward it everything should
[36:21] be using the co-pilot harness now. Now
[36:25] that copilot harness corresponds to the
[36:27] copot cli, the copot app, and now also
[36:30] to a bunch of co-pilots like you know
[36:32] because we've always joked that we have
[36:34] all these different things called
[36:35] copilot but they're all different
[36:36] products but actually now they're all
[36:39] increasingly going to be using the same
[36:41] underlying harness. So they actually are
[36:44] more going to be more similar, right? Um
[36:46] what's a harness and why is it hard?
[36:48] Good question. Um
[36:52] uh so yeah so it so now you know when
[36:56] you use copilot in PowerPoint and Excel
[36:59] like that is actually using the same
[37:00] harness is what's used in VS code and
[37:02] copilot app right and then the SDK if
[37:06] you use the copilot SDK
[37:09] uh which presumably
[37:12] they're going to maybe rename this
[37:14] [laughter]
[37:15] um because this would be the Microsoft
[37:16] copot harness uh SDK know um you know
[37:20] that's using the same harness. It uses
[37:22] this like rust uh harness behind the
[37:25] scenes. Uh so yeah just keep in mind
[37:29] that now it is called the Microsoft
[37:32] co-pilot harness and increasingly
[37:35] you should see more similarity between
[37:38] uh all the different co-pilots at
[37:40] Microsoft. Uh they don't all use it yet
[37:43] confusingly. So I've heard that in teams
[37:45] this one doesn't use it yet or sorry in
[37:47] Edge. Um and also maybe in teams too. So
[37:50] a few of the co-pilots don't yet use the
[37:52] new harness. Um but um you know some of
[37:56] them do.
[37:59] Who is the pilot? Are is it the agent or
[38:01] the human? Is that the question?
[38:06] Um yeah well um you know increasingly
[38:11] it's changing isn't it? Um
[38:14] yeah, with Opus 55, like I think that
[38:17] once you use Opus 55, you start to get
[38:19] very convinced that uh you know, our job
[38:24] is is changing quite a bit, right?
[38:26] Because Opus 55 just writes good code uh
[38:30] like better code maybe than most of us.
[38:34] Um, so you know, I think we I I'm
[38:37] basically preparing for the world where
[38:39] we just assume that the LLMs are writing
[38:41] good code and we just care about whether
[38:43] the output matches our expectations,
[38:45] right? I think that's where we're going
[38:47] toward. We're not quite there yet. Um,
[38:51] but uh we're getting really really
[38:54] close. So yeah, our days Okay, what is
[38:58] this? Your AI agents get a home here.
[39:03] Oh my gosh. All right. You did a little
[39:06] Sim City for agents.
[39:11] Go to the research lab. Go to the
[39:12] research lab. Okay. Research lab.
[39:15] Research lab.
[39:17] Uh,
[39:19] there we go. Oh, it's a multi. Oh, MS.
[39:22] Oh, nice. Okay. When you said MS, I
[39:24] thought you meant Microsoft. Okay, cool.
[39:26] How do we go to it? I'm not that good at
[39:28] games. just in
[39:33] maybe if I scroll. Am I supposed to be
[39:34] able to go in it?
[39:38] Oh, right click. Okay.
[39:42] Oh, man. You got to sign it. Okay, let's
[39:43] try this
[39:48] cake repository.
[39:55] the
[39:56] totally save item.
[40:00] Oh my gosh. No, no, not now. Too much
[40:04] too much security. Okay. Uh, I save it.
[40:08] Okay.
[40:11] [laughter]
[40:13] 10 factor off. All right. Here we go.
[40:16] [clears throat]
[40:17] Go in.
[40:20] Enter room. All right. Look at this.
[40:25] So cute.
[40:28] All right, so this is the research lab.
[40:32] Cool. I saw a talk at Asian Con about
[40:35] somebody whose dog got cancer and they
[40:39] um, you know, used LMS to research, you
[40:42] know, all the different things and then
[40:44] design a custom um a custom vaccine. So
[40:48] it seems like custom vaccines are uh
[40:51] something that people are increasingly
[40:53] doing
[40:54] with uh with agents. This is very cool
[41:00] research boards
[41:03] cure MS.
[41:06] It's it's a very ambitious thing. Um
[41:10] very cool. Well, it's great to see
[41:12] people using agents to, you know, do
[41:16] something that is very helpful for
[41:18] society. Yeah.
[41:21] Yeah. Um, that's awesome. Cool. All
[41:26] right.
[41:27] All right. Well, hang out there and
[41:30] contribute to uh so I guess there's like
[41:33] issues here and then pull request.
[41:38] Nice.
[41:40] Very cool.
[41:43] All right. What else?
[41:45] Yeah. So, if anyone's
[41:48] um got done some work around MS, you
[41:51] could join that. I have not looked into
[41:53] that at all myself.
[41:57] Uh let's see. Okay. Um
[42:01] oh yeah, I did last week also do a
[42:02] workshop at GitHub Universe. That's all
[42:04] open sourced here. This was about
[42:06] connecting GitHub Copilot to MCP servers
[42:09] first to GitHub MCP and then Foundry IQ
[42:13] MCP server.
[42:15] Oh, good news. We've got some late
[42:17] breaking news from the um VS Code copy
[42:21] team.
[42:22] Uh so they just got skills over MCP in
[42:25] the REST SDK.
[42:30] So uh looks like the first thing we're
[42:31] going to get is skills over MCP, right?
[42:34] All right, cuz I was saying the copod
[42:35] harness uses a rust uh like a rust
[42:38] binary. Wait, and if it's in the SDK, so
[42:40] actually you remember we were going over
[42:42] here rust. Okay, so that means that they
[42:46] um so if they did this
[42:51] Oh man, sorry to sign into a GitHub repo
[42:53] actually is hard for me. Um
[42:56] uh but here we go. Rust. Okay. So, it
[42:58] sounds like this one
[43:00] has must have just gotten skills. Can I
[43:04] see the history? No. All right. It's
[43:07] going to make me log in. And that's
[43:09] really a 10 factor off. You don't want
[43:10] to see that. All right. So, hopefully
[43:12] this is the one he's talking about. So,
[43:14] that should have skills over MCP. Um,
[43:17] they didn't reply about events yet. Um,
[43:19] but you know, skills will be really
[43:22] cool. Really, really cool. I actually um
[43:25] don't know anyone any of the agents yet
[43:27] that support skills or rims. So, it'd be
[43:30] very cool if if we uh led the charge
[43:33] there.
[43:36] Let's see anything else here. Uh oh,
[43:39] this was everybody was talking about
[43:40] this yesterday. Uh so, LMS can natively
[43:44] read and write neural network weights.
[43:46] Um,
[43:49] so they basically like fix the weights
[43:53] directly, which is crazy. I I actually I
[43:57] don't I don't know if all of you looked
[43:58] at this as well. I don't know if I you
[44:01] know entirely
[44:02] understand this. Uh, a train. Okay.
[44:07] A general purpose LM reads and writes a
[44:09] network's weights directly. So not with
[44:12] gradient descent, not with an optimizer.
[44:14] Um, so they just find the LM can just
[44:17] find the trait inside the weights.
[44:21] Wow.
[44:28] Oh wow. And they can also so they can
[44:30] really like they have like inspection.
[44:32] They can basically inspect like for
[44:34] example
[44:36] it could tell that it was trained on the
[44:40] breakout, right?
[44:43] That's really cool. Um, can Astra tell
[44:46] what the diffusion model will generate?
[44:49] Um,
[44:50] and can the output weights contain curd
[44:54] frame segments? So, yeah, apparently
[44:56] they can tell that as well.
[45:01] Oh, wow. Okay.
[45:05] So, LLM understand LLMs better than we
[45:08] do is what I think.
[45:11] brain surgery. Uh so Namdu is saying
[45:17] yeah so without Yeah. Yeah. So basically
[45:21] LLMs can look at
[45:26] they can look at their they can look at
[45:29] their weights and they understand it.
[45:32] Uh so maybe that's good for maybe better
[45:35] understandability, right? Because if the
[45:36] LLM can look at its weights and
[45:38] understand it, then maybe it can help us
[45:40] look at the weights and understand it,
[45:41] right? Because we've kind of created
[45:43] these things that we don't entirely
[45:45] understand. So here also, this is what
[45:46] everybody was most excited about is
[45:48] that, you know, it was able to tweak its
[45:50] weights to get better at math.
[45:53] So I guess that would be another
[45:54] approach instead of fine-tuning is this,
[45:56] right? Maybe maybe instead of needing
[45:59] fine-tuning, if you just say, "Hey, the
[46:01] most important like, you know, like for
[46:02] rag, it's like, oh, okay, the most
[46:03] important thing is accuracy and not
[46:05] hallucinations, right? It seems like
[46:06] that would be something that you'd be
[46:08] able to have it just tweak its weights,
[46:12] right? Um,
[46:14] you'd still have to run it though. So, I
[46:16] think you still have the you'd still
[46:17] have the expense of running a custom
[46:19] model, but it might be more efficient
[46:21] than fine-tuning.
[46:23] Oh, Justin says hopefully it can't tweak
[46:25] them real time without good oversight.
[46:28] Yeah, I think I assume not like um
[46:31] because if like how are the way that
[46:33] models are run with inference engines
[46:35] like can could an inference engine
[46:37] actually tweak its own weights uh like
[46:40] with like VLM and stuff like that? That
[46:43] also leads us to this other piece of
[46:45] news was that DeepS they open sourced
[46:48] their own inference framework for
[46:50] Deepseek models. Uh so you know it's
[46:54] just optimized for DeepS. Um but
[46:58] you know that's always cool. People are
[47:00] excited about that. Uh let's see.
[47:03] Cloudflare bought Dino
[47:07] uh mostly for this SLD thing. So Dino is
[47:09] going to be all wounded wound down. So
[47:12] if you were using Dino that's like an
[47:13] alternative to node and bun. You need to
[47:16] move off Dino now. Uh, oh, we finally
[47:19] got 61 Terara. And that's interesting
[47:22] because I thought they'd just given up
[47:24] on Tara
[47:26] because like Tara, people were always
[47:29] like, well, you either use the cheap
[47:30] one, Luna, or you use the good one,
[47:32] Soul, and Terra was this like weird
[47:34] middle one. But they did actually launch
[47:36] a 61 Terra. Um, and they they think it's
[47:39] like particularly good um for visual
[47:43] stuff for some reason. So, from visual
[47:45] understanding action. So I that's kind
[47:47] of random. So maybe
[47:49] um
[47:51] yeah, I don't know. I have not tried
[47:54] Terra at all because it's always kind of
[47:56] like the weird one in the middle. But
[47:58] maybe for some reason it is randomly
[48:02] better at visual stuff. So worth
[48:05] considering that there is a 61 terra
[48:06] now.
[48:09] Uh 62 Astrobets. I mean, right now,
[48:11] like, I feel like we should just pace
[48:14] and just use Opus 55 forever. I'm kind
[48:16] of scared of something being even better
[48:18] than Opus 55,
[48:20] but yeah, everybody does talk about
[48:21] Mythos. Um,
[48:24] uh, I haven't personally used Mythos
[48:27] myself. I've seen the results of Mythos,
[48:30] um, but it's kind of hard for me to
[48:31] judge based off results. People are
[48:34] seeing Astra 6.2 show up on bills.
[48:36] Interesting. Okay. Uh I also don't
[48:40] really use the Astra model like I think
[48:42] is GitHub copilot. Do I even have I
[48:45] don't even know if I have access to
[48:47] Astra.
[48:49] Uh so here. Okay. So we have fusion. I
[48:52] don't have it on right now because I'm
[48:54] because I like to use Opus 55 for
[48:55] everything. Okay. So I do have access to
[48:57] six Astra.
[48:59] Uh the default is 61 soul. I've changed
[49:02] mine always to use opus 55.
[49:05] So to me opus 55 is the best. And I
[49:08] never want to use anything besides Opus
[49:10] 55, which is why I don't have Fusion on
[49:14] and I don't have auto on. Um,
[49:18] oh, maybe wait, did Fusion take place of
[49:20] auto? Do we not have Is that what
[49:23] happened? Fusion took the PL because now
[49:26] I don't see an auto.
[49:28] Oh,
[49:29] that would make sense. Okay.
[49:33] Uh Namdi says the problem with mythos
[49:35] and fables is just so expensive and they
[49:37] make you lazy because they do too much
[49:38] for you. I think the bigger problem
[49:41] would be too expensive. I think at this
[49:43] point we've realized that what you know
[49:45] what we are doing is is guiding um
[49:47] agents and you know not necessarily
[49:50] writing code ourselves. Um, so yeah,
[49:54] they might they may very well make us
[49:56] lazy, but I you know, I think it's just
[50:00] um, you know, whether you need whether
[50:04] you need it for the amount of cost. Um,
[50:07] and given that Opus 55 is like less
[50:09] expensive and seems to be really really
[50:12] good and like it doesn't like it doesn't
[50:15] do anything weird. The thing about Opus
[50:16] 55, it doesn't have any quirks, right?
[50:18] Like a lot of the other models kind of
[50:19] have quirks where you're like, "Oh, it
[50:20] just did something weird." OPI 55 has
[50:22] like never done anything weird for me,
[50:24] right? It is the most reliable.
[50:27] Uh, okay. So, Justin likes to have it
[50:29] use lesser agents, right? Yeah. So, you
[50:32] can do that. And that would be easy to
[50:33] do in in here, too. Like, um, you'd be
[50:37] like, okay, you know, redesign my
[50:39] website. That's actually um that's
[50:42] something fun you can do. co-pilot like
[50:43] in you know here I could have said like
[50:46] okay use a different GPT model for each
[50:51] redesign in a you know a child session
[50:56] um and that should work. I'm not going
[50:58] to do it because my child giggles so
[51:00] much but [laughter]
[51:02] um well we can try it. Uh so you know
[51:06] that's that that would be a good thing
[51:08] right especially with anything with like
[51:09] design that is something where like I
[51:12] keep seeing people using LMS for making
[51:15] slides which I do but you can't use the
[51:18] text from the LMS like it's not good
[51:20] text like it is helpful for making your
[51:22] diagrams and for doing layout and and
[51:25] all that stuff but you really need to be
[51:27] going through if you're you know if
[51:28] you're using LMS to generate slides you
[51:30] really got to be going through and re
[51:32] really massaging the text and making
[51:34] sure the text is something that, you
[51:36] know, is going to, you know, resonate
[51:38] with the person who's looking at your
[51:40] slides because it's going to be a human
[51:41] looking at your slides, right? Um,
[51:45] people don't like to read.
[51:48] Yeah, they automate with the eye and
[51:49] then don't read it. All right, now you
[51:51] can see it's starting up. Uh, so yeah,
[51:53] here here you go. So here it's using six
[51:55] one soul, six Luna, and 53 codex.
[52:00] Um,
[52:03] and there you go. It's it's very active.
[52:06] Uh and I might still have permissions
[52:08] issues. I'm not sure. But um but that
[52:12] would be that's a really good use case
[52:14] for doing a bunch of different child
[52:16] sessions is design. And as you see, like
[52:18] I do do a lot of design. Like I was
[52:19] doing the um the Papel Picado, right?
[52:24] And this one like um this was a
[52:27] combination of a couple different
[52:27] models, but like I could have had it
[52:29] like I could have been like, "Okay, do
[52:31] five different sessions for five
[52:32] different models because you're just
[52:33] going to get more variation, right?" Um
[52:36] and so like what I often find now is
[52:38] when I do that and I'll often ask for
[52:40] like a like a pallet to compare. So I've
[52:43] got this like repo where I do all my
[52:46] kind of you know design work in and um
[52:50] here. So I I'll tell it to do a bunch of
[52:52] logos. This is for a fake chocolate
[52:54] company. [snorts] Um, and then
[52:57] [clears throat] I have it make like a a
[52:58] gallery or a contact sheet. And then I
[53:01] have to look at the logos and decide
[53:02] like which of them, you know, which of
[53:04] them I actually like. Um, these were the
[53:06] this was my short list here, right? And
[53:08] so now the hard part becomes, you know,
[53:10] your like taste, right? Like I look at
[53:12] all these and I think, wow, like you
[53:14] know, I kind of like a lot of these. Um,
[53:16] and then you have to decide, right? And
[53:18] then you have to look at it and be like,
[53:19] well, which of these is actually, you
[53:22] know, good? like which one would you
[53:23] know maybe you've independently come up
[53:26] with or thought was the best. Um so yeah
[53:29] so now I think the hard part is you know
[53:33] taste right and deciding like okay when
[53:36] it comes to design stuff right because
[53:37] it's very easy to have get lots of great
[53:40] designs um but then but then yeah you
[53:43] got to narrow them down.
[53:47] Uh oh good fast support skills over MCP.
[53:50] So that means if you're making an MC
[53:51] server it can support it as well.
[53:55] Cool. All right, we got to do like
[53:57] another MSP live stream sometime and do
[54:00] all the new stuff. Um, we're actually
[54:02] doing a fast MP event in December in
[54:05] person with the team and I think one of
[54:07] them is is going to talk about skills.
[54:10] All right, I have to uh go now, but
[54:14] [laughter]
[54:16] the agents are having a really fun time
[54:18] with the redesign. Oh, brutalist. All
[54:21] right.
[54:25] Okay. I'm just gonna like All right. Lot
[54:28] of lot of sessions happening there. All
[54:30] right. All right. Thank you everyone.
[54:32] I'll post everything in uh in the usual
[54:35] thread afterwards with the recording and
[54:37] whatnot. And I will see you next week.
[54:41] Bye.
