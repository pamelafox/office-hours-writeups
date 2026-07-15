[00:00] Welcome to our weekly Python and AI
[00:03] office hours. Uh this is where we talk
[00:06] about everything going on in the
[00:09] generative AI industry over the last
[00:11] week especially as it overlaps with
[00:14] Python
[00:16] and you know talk about the news also
[00:18] talk about your questions sometimes do
[00:20] some live coding whatever happens. Um,
[00:24] so if you do have any comments,
[00:26] questions, links you want to share, just
[00:28] put them all in the chat. I'll be
[00:30] watching the chat the whole time and um
[00:34] we'll, you know, address anything that
[00:36] you all put there. Uh, so I always start
[00:39] off with the news that's happened over
[00:43] the last week. Uh, so that we can chat
[00:46] about anything interesting related to
[00:48] it. So the big news was GPT 5.6. six.
[00:53] Uh, so OpenAI was finally able to
[00:55] release that, uh, after, you know,
[00:57] negotiating with the government,
[00:59] whatever they did. Um, so now we do have
[01:03] TB56 available in C-pilot. Um, we also
[01:06] have it available in Foundry. I was able
[01:08] to see it in Foundry as well, so you can
[01:11] try it out for programmatic uses, too.
[01:16] Uh, so that's got released and I spent a
[01:19] long time. So I actually am pretty much
[01:21] fully on 5.6 now. I was very resistant
[01:25] because I've been uh a big Opus fan for
[01:28] the last eight months I guess. Um, but
[01:32] my colleagues are you know really
[01:34] recommended GB 5.6. It is cheaper than
[01:37] Opus. Um, so I wanted to give it a fair
[01:40] shot. Uh, so I am I think my default
[01:43] right now I think I've been using 5.6
[01:46] Soul. Uh, I've been using it all day
[01:49] with VS Code all week really and I'm
[01:51] also using it in my co-pilot app. So um,
[01:55] so yeah, it like it's definitely
[01:57] different from Opus. Um, it it requires
[02:00] a little more encouragement to follow
[02:04] through. Um, but that can be a good
[02:06] thing. So it's I would say it's more
[02:07] conservative
[02:09] um in terms of taking action uh which is
[02:12] generally the case with the GPD models
[02:14] but you know if you give it the right
[02:16] direction then it'll totally take
[02:17] action. Um so what I recommend looking
[02:20] at is they've got two they've got
[02:22] various docs they've got you know okay
[02:24] this was the blog post but then um
[02:26] what's more interesting is the um let me
[02:32] find the model the model guide. What I
[02:34] want is a model guide. Um, let me find
[02:38] GPD 5.6 model guidance. I think it's
[02:42] called model guidance. Here we go. Okay.
[02:45] So, they every time they have a new
[02:46] model, they they release the model
[02:48] guidance for it. So, you can see here,
[02:50] you know, there's tabs for the last like
[02:52] eight models or whatever. Um and so this
[02:55] is really helpful to look at because it
[02:56] it's it's basically like the diff of
[02:58] what is changed um from one model to the
[03:02] next and the kind of recommendations for
[03:03] how to work with it. Um so interesting
[03:05] thing here is also starts off with all
[03:07] the new features. So you can see that uh
[03:10] basically 5.6 has code mode built in.
[03:14] We've talked about code node here in the
[03:15] past um which you can do using we we did
[03:18] it using the mont monty sandbox but now
[03:21] um they they have this basically built
[03:23] in the idea that um you know the the
[03:26] model itself can use JavaScript to
[03:30] coordinate multiple tool calls and do
[03:32] looping and and stuff like that and they
[03:35] just run that all in a hosted runtime.
[03:37] Um so that's bringing bringing code mode
[03:39] to the masses. So that's very
[03:40] interesting. Um, there is built-in
[03:42] support for multi- aents and sub aents.
[03:44] Generally, GBD 5.6 likes to use sub
[03:46] aents a lot more. So, you have to watch
[03:48] out for that. Sometimes that's good,
[03:49] sometimes it's bad. Um, it does also
[03:51] have explicit prompt caching. This is
[03:53] something that Enthropic had for a long
[03:55] time. And so, now we do have that with
[03:57] OpenI as well. So, that can give you
[03:58] like a lot of flexibility over what gets
[04:01] cached and what doesn't. Like you set
[04:03] like these cache break points. Um, okay.
[04:06] There's some other stuff. I didn't read
[04:07] about these yet. So, persisted
[04:09] reasoning. Oh, they added a new max
[04:11] raising effort. So, that is even higher
[04:14] than X high. Presumably max is going to
[04:17] be the max. I don't know if they're
[04:19] going to add like an X-Maxx in the
[04:20] future. I don't know. Um, but then they
[04:23] also have a pro mode. So, the pro mode
[04:26] um feels like maybe it's looping harder.
[04:29] So, that's that's even distinct from,
[04:32] you know, the reasoning effort. So,
[04:33] there's reason effort, but then there's
[04:34] also pro mode. So they they're adding
[04:36] like a lot of levers here for when you
[04:38] really really need it. Most of the time
[04:40] I'm just using medium, right? Um but you
[04:43] know, you can you can try these modes if
[04:45] you really really need them. Let me
[04:47] double check that I'm on medium. Yeah.
[04:48] So by default there's medium. You can
[04:51] see that you can go up to max. I don't
[04:54] see a way of enabling pro mode in
[04:55] Copilot. So maybe we don't have that
[04:57] enabled because that's a completely
[04:59] different thing. Um but you can see we
[05:01] can change these options here.
[05:04] Oh yeah, an ultra.
[05:06] Um,
[05:08] uh, so ultra. Where's the ultra? Did
[05:11] they mention it here? Um,
[05:15] ultra.
[05:17] Ultra. They didn't even mention it here.
[05:20] Okay, let's see. Did they do it here?
[05:22] Ultra. Yeah, ultra is our highest
[05:25] capability setting. Coordinate multiple
[05:27] agents across parallel work streams.
[05:29] Yeah. So I think once again we don't
[05:31] have this in I don't think we have this
[05:33] in co-pilot because I think it would
[05:34] actually require
[05:36] um some
[05:38] tuning to work with our sub agents. Um
[05:43] but uh let's see ultra is available blah
[05:48] blah blah. So maybe ultra is something
[05:50] that you can use in probably in codecs.
[05:55] I don't know Justin if you've managed to
[05:57] use ultra yet and where you've used it.
[06:00] Okay. So, you used it. I don't think
[06:03] Ultra So, Ultra is different from Max.
[06:06] Ultra.
[06:08] I've seen some good tweets about this. I
[06:10] didn't I don't think I bookmarked them,
[06:11] but there have been some good tweets of
[06:13] people. Let me see if I have it them um
[06:18] have them like maybe I liked them. Um
[06:30] No. Um
[06:33] yeah, people have certainly been trying
[06:35] to explain the ultra versus max versus
[06:38] whatever and um you know because and
[06:42] generally people are confused about it
[06:43] but uh I think that ultra
[06:48] looks like it's it's only for soul
[06:51] and I don't think we have it for
[06:54] copilot.
[06:57] Ultra is in codeex. Okay. So if you do
[07:00] want to try ultra then you have to use
[07:02] codeex
[07:04] um I'll chat we I'll ask uh our co-pilot
[07:07] team
[07:08] uh actually um
[07:12] ultra let's see if anyone asked about
[07:13] ultra is ultra available in co-pilot
[07:15] let's see um
[07:26] Um,
[07:33] okay. Someone definitely asked about
[07:35] this. I just know what was the answer to
[07:37] this. All right.
[07:41] All right. I'm just checking with the VS
[07:43] Code team to see if we have any news
[07:45] about Soul Ultra.
[07:49] Okay. Good. Good point. Um, so Honor
[07:53] says it is not worth it for most hacks.
[07:56] soul. Medium high is enough. Yeah. And
[07:59] to be honest, I've only been using
[08:00] medium soul. Um because I guess when I I
[08:04] feel like when it's not doing a good
[08:07] job, it's not necessarily that it needs
[08:08] more reasoning effort. It's just that it
[08:10] needs more encouragement to do what I
[08:13] want to do. Um interestingly, with the
[08:16] mo the model guidance here, um it
[08:18] actually recommends, you know, using
[08:22] smaller prompts. Um, so it actually
[08:24] says, let's see here, favor leaner
[08:26] prompts, right? Um, so it says, you
[08:29] know, generally simplifying tool
[08:31] descriptions can improve performance. Of
[08:34] course, that's only for this model,
[08:35] right? And if you're, you know, if
[08:37] you're making things to be across
[08:39] models, you don't necessarily want to,
[08:40] you know, lean up your prompts, but for
[08:42] GBD 5.6,
[08:45] um, it says, you know, remove, okay,
[08:47] start with the prompt that works. Remove
[08:49] one group of instructions at a time.
[08:52] state each instruction once blah blah
[08:54] blah define autonomy and approval
[08:56] boundaries right um
[09:00] and
[09:02] yeah so it's good to
[09:06] it's good to read the model guidance um
[09:09] because it gives you a better feel for
[09:10] how how to write your prompts when
[09:14] you're using it
[09:16] um and yeah from the programmatic
[09:18] perspective this programmatic tool
[09:19] calling cool code mode definitely looks
[09:21] the most interesting and we should
[09:24] support this. We support this already
[09:27] for um Foundry OpenAI models and there
[09:31] were a couple other changes. Let's see.
[09:33] So there's the meta the multi- aent
[09:36] capability and responses. So that is
[09:39] supported as well. The so this is this
[09:41] one here. So that one you should be able
[09:44] to use with responses API from Azure
[09:48] OpenAI.
[09:49] Um
[09:52] there is a new thing not even mentioned
[09:54] in their docs uh which is websockets. Uh
[09:59] so
[10:01] um there's this websocket mode use
[10:05] for responses. I'll hear this one. Uh
[10:11] so I haven't played with this at all.
[10:15] Um but um this is with
[10:17] beta.responses.com. responses.connect
[10:20] is this here beta.responses connect
[10:25] responses.connect.
[10:27] Yeah, the Python beta SK exposes
[10:29] websocket mode through beta.responses
[10:32] connect. Okay, so this is technically
[10:34] supported on Foundry. There is a little
[10:37] bit of a bug with it. Um, so if you are
[10:42] looking to use that, um, you do want to
[10:47] follow this bug um, here. Um,
[10:53] but that's only for, you know, it's it's
[10:56] mostly working. It's just a little bit
[10:57] of an off issue there. Uh, but yeah, so
[11:00] if you want to
[11:02] try the new capabilities in 5.6, six
[11:05] then you should be able to try it from
[11:08] foundry.
[11:10] Uh so Bernard says GitHub copilot has an
[11:12] MS own trained coding model um which was
[11:15] announced by VS Code Harold. Um are you
[11:19] talking about the code one flash or are
[11:21] you talking about oh what's it called?
[11:22] Wait did we announce I never know what's
[11:25] we've announced. So we because there is
[11:26] certainly
[11:28] uh I don't see it on here. So here I see
[11:31] I do see m MI mi code one flash.
[11:35] Um
[11:38] but we do often have our own model
[11:41] variants that we're training you know
[11:45] like that we're tuning for VS Code. I
[11:47] don't see any in the public model picker
[11:50] right now. Oh okay. Okay. All right.
[11:52] That's what we're talking about. Yeah.
[11:53] So um yeah. So MIDO1 flash I don't use
[11:57] that one. um because it's more on par
[12:00] with haiku and um and I don't use haiku.
[12:04] Um I think most of my tasks are bigger
[12:06] tasks. Uh so I don't tend to go down as
[12:10] low as uh as low as IQ. But if you're
[12:12] trying to be very um cost, you know,
[12:14] cost efficient, that could be good. Um
[12:18] uh I yeah, right now I'm basically just
[12:21] using 5.6 sole medium for everything. I
[12:25] I do like to keep just one model and
[12:26] stick with it. I don't I I I we have the
[12:29] auto mode and I think if the auto mode
[12:31] works for you, great. You should totally
[12:33] use that. Um I have a hard time using it
[12:36] because of the non-determinism of like
[12:38] which model is going to be picked and I
[12:41] just like knowing exactly which model
[12:42] I'm working with so I can, you know,
[12:45] know what to expect and and prompt
[12:48] accordingly. Um okay, so that was
[12:54] um GPD 5.6. So,
[12:57] uh, check out check that out for sure.
[13:00] Um,
[13:02] what else is, uh, going on? There's lots
[13:07] of lots of cool updates here. Um,
[13:10] yeah, so Justin said, "Thoughts on using
[13:12] a larger model like Soul Ultra to create
[13:14] plans for smaller models." That's true.
[13:16] I do have a colleague who said he was
[13:18] going to do that. Um, what was what was
[13:21] he going to use?
[13:24] Let's see.
[13:25] Uh
[13:29] yeah, so he was going to do soul as a
[13:30] primary driver and 5.4 for costsensitive
[13:33] work. So that would be that would be one
[13:36] approach um
[13:39] is to to make the plan uh make the plan
[13:43] or the agents.md. Yeah, you're gonna So
[13:45] here's the thing is that you'll lose on
[13:46] the caching if you're doing in the
[13:48] session, but what you can do is make a
[13:49] plan MD, right? like today like I just
[13:52] had it make an agents.mmd right so
[13:55] whether it's a plan MD or agents.md
[13:57] right like you want to have you know the
[14:00] the more you can have um you know uh let
[14:04] me this uh you know if you can have your
[14:06] plan and your docu agentfriendly
[14:10] documentation whether that's an
[14:12] agents.mmd or a plan MD right um and you
[14:16] know keep that up to date then it's much
[14:18] easier I mean general best practices
[14:20] these days is to create new sessions as
[14:22] much as possible right because obviously
[14:24] like when you have a new session you
[14:26] don't have all that old context right so
[14:28] I do try to keep um skills and agents MD
[14:32] and planned MD all you know it's all
[14:34] markdown keep all the whatever your
[14:36] markdown file like you know source of
[14:38] truth is keep that up to date constantly
[14:41] you know say like you know do we need to
[14:43] like do we need to update that you can
[14:44] even have hooks that check that but I'm
[14:46] just like kind of you know I just have
[14:47] it in the back of my head like oh is
[14:49] there you know do we need to update this
[14:51] um because that way it's it's you know
[14:53] easy. So here um right like this was
[14:56] like let's see uh here I said okay add
[15:00] an agent.mmd file at the root it made
[15:02] all that agent db once it made the
[15:04] agents.mmd then I was happy to make a
[15:06] brand new session and say okay like I
[15:08] you know it's got all the context it
[15:09] needs now you're going to do all this
[15:11] stuff right um so as long as I feel like
[15:14] there's this up-to-date you know concise
[15:17] documentation
[15:19] um about how things work uh like in this
[15:23] case actually didn't it didn't update it
[15:24] with the this
[15:27] uh the latest stuff. So as long as this
[15:29] is kept up to date, uh then you know
[15:31] then I feel like I can make new sessions
[15:33] all the time, right? So making new
[15:35] sessions is good because less context
[15:36] and also more model flexibility, right?
[15:38] Like as long as you feel comfortable
[15:39] that anytime you can go into a new
[15:42] session, then you you can choose this
[15:45] the more expensive model or the less
[15:46] expensive model.
[15:50] And so Bernard creates ADRs first. Yeah.
[15:55] Um
[16:00] Yeah. So, I do think that's a that's a
[16:02] great plan. Um,
[16:05] and I suppose I could try after, you
[16:08] know, making a plan using MI code flash
[16:11] to implement it instead of GB 5.6.
[16:14] Um,
[16:16] and it'd be interesting to see how it
[16:17] how it did.
[16:21] I know we don't got free tokens. Okay. I
[16:24] know. Peer pressure. I should I should
[16:26] use less tokens. Okay. You know, 5.6 is
[16:29] cheaper than O Opus, so I feel like
[16:31] that's progress for me, but um it's
[16:33] still not like super cheap, right?
[16:37] Um good points everyone. Uh on that
[16:40] note, that's a good that's a good
[16:41] leadin. So, I did want to plug uh my
[16:44] colleagues video tokconomics. Um so,
[16:47] April made this video um talking about,
[16:50] you know, stuff around token economics.
[16:52] Uh so um what has it got? Uh context
[16:55] windows
[16:57] um caching for savings model router all
[17:00] sorts of things in there. Um so that's
[17:03] you know a nice video about that about
[17:05] that topic. And my colleague w watched
[17:07] it and he said wait a second is
[17:09] everybody like building their own
[17:10] harness that has like compaction and all
[17:12] that stuff and I was like no you don't
[17:13] have to build your own harness because
[17:15] we have harnesses like already built.
[17:17] Um, so, um, I think we've talked about
[17:20] this before, but agent framework now has
[17:23] a builtin agent harness. So, instead of
[17:26] just using the base agent class, right?
[17:28] This is, you know, this wraps on top of
[17:30] it to add in the kind of things you
[17:32] expect from like a full harness, right?
[17:34] So you get compaction, uh you get
[17:37] persistence, you got a to-do provider,
[17:40] um you have memory provider, tool
[17:42] approver, open telemetry, web search,
[17:45] skill provider, background agents, shell
[17:47] environment, looping, right? So um if
[17:50] you really want all batteries included,
[17:54] you know, kind of best practices for a
[17:55] harness, then uh you know, check check
[17:58] out the harness agent. You can see here
[18:00] you can set your compaction details
[18:02] here. So, max context window tokens 128k
[18:07] max output tokens.
[18:09] Um,
[18:11] and then you can add on like disable or
[18:14] enable things. Um, you can have it do
[18:18] looping like Ralph
[18:20] looping. Um,
[18:24] so yeah, so check that out because it
[18:27] does have Yeah. Yeah. I think people
[18:30] don't realize that agent framework has
[18:32] this now. So this is also very similar
[18:33] to like lang chain deep agents, right?
[18:36] Um
[18:38] I would say that would be like the
[18:39] equivalent of basically you know uh
[18:44] wanting to have all these features um
[18:47] built in
[18:49] very very similar wouldn't be surprised
[18:52] if uh there was some inspiration there.
[18:56] Uh, wow. So, Baronard says, "We spend 10
[18:59] to 20% of your salary to tokens per
[19:01] employee." Wow.
[19:05] Wait, does your boss want you to spend
[19:06] more or less tokens?
[19:11] Um,
[19:13] he wants to spend more tokens. Okay.
[19:15] Some companies are in the token maxing
[19:17] era still and some tokens are in the
[19:19] token minning era.
[19:22] Uh, so yeah, welcome to the office
[19:24] hours. It's just we go and we just talk
[19:27] about talk about things, explore things,
[19:30] ask questions, answer questions. Um so
[19:33] yeah, so tokconomics, agent harness, um
[19:37] check those out. Um
[19:40] a few other
[19:43] things I wanted to show. I also chatted
[19:45] with the Azure functions team last week.
[19:49] Um so for any of you who use functions
[19:52] or you know or you maybe just want to
[19:55] try it out um they have added this is
[19:58] actually a lot like aentic work uh
[20:00] agentic workflows. So we've talked about
[20:02] agentic workflows before. Let me bring
[20:04] up aic workflows to contrast them. Um so
[20:09] these are useful
[20:11] like when you want to have um LM like
[20:16] LLM
[20:18] um assisted
[20:20] uh workflows on your GitHub repo. So for
[20:23] example
[20:25] uh this one this one here
[20:29] um let me link to this as well. Let's
[20:32] see.
[20:34] Here's an example,
[20:37] right? So a aentic workflow for GitHub
[20:42] uh starts off with a bunch of YAML and
[20:44] the YAML is helpful because it gives
[20:46] permissions, right? So the YAML says
[20:47] like oh you get, you know, these
[20:49] permissions of what you can read. Um
[20:51] this network permissions, what tools are
[20:53] allowed so you can add like MCP servers
[20:55] and built-in tools. Uh this one even has
[20:58] a step. Most of them don't have steps.
[21:00] Um usually then you just have the safe
[21:01] output. So this workflow is allowed to
[21:04] create an issue and link a sub issue.
[21:06] Those are the only two things it's
[21:07] allowed to do. So it uses the front
[21:10] matter for doing everything that needs
[21:11] to be really uh concrete and um you know
[21:16] and needs to be cons a constraint for
[21:18] security reasons. And then the rest of
[21:21] it is just markdown. We're just
[21:22] describing what's going to do. Um and so
[21:25] that's you know it's like an easy way of
[21:27] writing an agent, right? You could of
[21:29] course also, you know, use agent
[21:30] framework and write an agent and run
[21:32] that agent in your workflow. But you may
[21:34] not want to. You might just want to use
[21:36] markdown. Um, and so you'll use markdown
[21:40] and um, describe what you want to do and
[21:43] then, you know, agents can do a pretty
[21:46] good job following instructions. And
[21:48] this way it'll follow those instructions
[21:50] and then um, adhere uh to the output.
[21:55] Um, where is it? My my colleague made
[21:57] one this week that's actually really
[21:59] similar.
[22:01] Um Oh, here we go. Okay, so his is
[22:05] really similar to the what I use, right?
[22:08] So, he he uses this automated workflow
[22:11] to generate weekly news. And it's funny
[22:14] because it's actually really similar to
[22:15] what I'm doing here to generate the news
[22:17] for our office hours. So, I could also
[22:20] be, you know, using his too. Um
[22:23] he does have this. Yeah, I I do like his
[22:25] overview here. And that's all in this
[22:27] repo here. So he's doing his with an
[22:30] agentic
[22:32] um aentic workflow. And you can see it
[22:35] if we go here I assume automerge weekly
[22:39] news digest. Yeah. So here you can see
[22:44] how he generates it.
[22:48] Uh it's easier kind of look at it's
[22:50] easier to look at the YAML in the in the
[22:52] raw mode. So those are agentic
[22:54] workflows. So, um, definitely there's a
[22:57] lot of fun ones to consider for your
[22:59] GitHub repos. Like I just go through
[23:01] this whole workflows list here or you
[23:03] can look at the docs, um, and you know,
[23:07] uh, look through these docs to find some
[23:09] inspiration or wrote write your own. Um,
[23:12] I I think there's a lot of helpful
[23:15] workflows that could be added to repos,
[23:17] right? Easier issue triaging management,
[23:20] um, release status, that sort of thing.
[23:23] Uh I'm not I haven't added into my repos
[23:25] yet because I do everything with
[23:27] co-pilot app automations. So you know
[23:29] I've got my issue triage here and other
[23:32] update like automations here as well. Um
[23:36] but if I wasn't doing it in copilot app
[23:38] then you know I would add it to the repo
[23:40] especially for shared repos right.
[23:44] Um, oh yeah, and so what I was talking
[23:46] about is that Azure Functions added like
[23:49] a really similar approach to try and
[23:51] make it very easy to write agents in
[23:54] Azure Functions, um, especially ones
[23:56] that use, you know, triggers from
[23:59] connectors um, that you might use, you
[24:02] know, for Azure Functions otherwise. And
[24:03] like if you look at this, it's very
[24:04] similar to what we were just looking at
[24:06] for workflows. So you can see, okay,
[24:09] there's the trigger, right? So in this
[24:10] case it's just a cron job but you could
[24:12] have triggers like when something's
[24:13] added to a blob storage you know you're
[24:15] going to do something right um
[24:19] so and you can do you could do quite a
[24:22] bit um for those triggers right so HP
[24:24] trigger Q trigger blob trigger event
[24:26] grid trigger service trigger all the
[24:28] triggers that you can use um for Azure
[24:31] functions and then you can connect to
[24:33] MCP servers you can connect to um Azure
[24:37] connectors this is connectors.asure.com
[24:39] azure.com. This is like based off of
[24:41] logic apps, but now it's like broader to
[24:44] be used by other people. Um, so you like
[24:47] make this connectors name space and then
[24:50] you can so I added like a Gmail
[24:52] connection. Um, but there's there's like
[24:55] a bunch of connections you can make
[24:56] there.
[25:00] Uh, and then you can add in skills,
[25:02] Python. You can you can even add in
[25:04] custom Python tools if you really want
[25:06] to. So, so yeah, this is another way
[25:09] that you can run you can build agents in
[25:12] the cloud and not have to build entire,
[25:16] you know, Python agent framework agents.
[25:20] Um,
[25:22] uh, so I don't know.
[25:26] Yeah. So, it'd be interesting to see
[25:27] what use cases, you know, people find
[25:29] for there. There's just so many
[25:31] different ways you could build agents
[25:32] now, right? like in different spectrum
[25:35] of code, right? Whether you want it like
[25:37] really really full code control, then
[25:38] you're going to, you know, use like
[25:40] agent framework or link chain. Um, but
[25:42] if you want less control and you're
[25:43] comfortable with the markdown, you know,
[25:45] then you could use something like this
[25:47] serverless agents runtime. Um, and then
[25:49] if you only need it running locally,
[25:51] then you know, then you could just write
[25:52] like an automation and copilot app.
[25:56] Um, can I share my weekly digest repo as
[25:58] well? That's a good question. I actually
[25:59] think it's not I keep meaning to I think
[26:03] it's not pushed. Is this repo push? Let
[26:05] me just ask push to GitHub somewhere.
[26:10] Um
[26:12] I'm so lazy. There's also articles going
[26:14] around like that we're getting so lazy
[26:16] because of AI. And it's true, isn't it?
[26:18] Right. We do have to be really careful
[26:20] about that. So there's lots of people
[26:21] recommending like, okay, yeah, you can
[26:22] use AI, but you know, don't don't
[26:25] outsource all your thinking to AI. Um,
[26:28] yeah, I don't think it's pushed to
[26:31] to GitHub yet. Um,
[26:35] I will work on it. What I what I'm
[26:36] probably going to do is merge because I
[26:38] do have my other repo, which is the
[26:40] office hours writeups repo. That's where
[26:42] I um where I take the transcript from
[26:46] our sessions and and write it all up.
[26:48] So, I think what I want to do is merge
[26:50] these into a single repo and then and
[26:54] then I'll just add it to here. So, I
[26:56] will I will do that as well. Um,
[27:01] okay. So, let's see. I saw some good
[27:03] stuff in the chat. Um,
[27:06] all right. I saw some news. Okay. Yeah.
[27:09] So, publishing to teams. Oh, yeah. So,
[27:11] questions about this is followup from
[27:13] last week. Um, is hosted agents GA. So I
[27:18] yeah, I chatted a bunch with um Nick
[27:22] Brady about this and um he says
[27:30] it is coming in the next few days. Okay,
[27:35] he said the next few days. Okay, I'm
[27:37] just gonna uh Is it is it GA yet?
[27:42] Getting you again.
[27:49] Okay. All right. I just pinged again.
[27:52] Um,
[27:55] let's see if we have
[28:01] Let's just check the blog, too, because
[28:02] I haven't checked this blog
[28:05] to see Foundry blog.
[28:09] June 2nd. June 2nd. Latest post. Yeah,
[28:13] we don't have a latest post yet. All
[28:14] right. Well, I just pinged the PM, so
[28:17] let's find out because he said last
[28:19] seven days ago, he said it was in the
[28:21] next few days. So, maybe it slipped
[28:22] again. Um, it should be really, really
[28:25] soon. If it's not GA, it should be very
[28:27] soon. Oh, wait. Actually, I think it is
[28:29] G because we were just talking about
[28:31] this. Um, okay. In the docs, let's see
[28:35] if we go here.
[28:42] Okay, so it says Foundry agent service
[28:46] is generally available. Some sub
[28:48] features are in public preview. Okay,
[28:50] well that's still not that useful
[28:51] because Foundry agent servers is
[28:55] like a big term. Um
[29:00] so let's wait to find out
[29:04] whether hosted agents himself is
[29:07] considered GA.
[29:12] All right, let's see. Ryan says co-pilot
[29:14] survived in a demo or succeeded in a
[29:17] demo that uses um an MTV service on
[29:20] ArcGIS server. Yay. I love Argis.
[29:24] That's great.
[29:26] July 13 through 17. So, did that just
[29:29] happen today then?
[29:32] Because today is July 14th.
[29:35] Cool.
[29:38] Uh, laziness is the mother of invention.
[29:40] We get to touch more grass now. Are are
[29:42] all of you actually touching more grass?
[29:44] I'm not touching more grass because
[29:45] there's like so much fun stuff to do.
[29:48] Um,
[29:50] you know, we always think we're going to
[29:51] do less work, but it turns out humans
[29:52] like doing work. Well, some humans like
[29:54] doing work. That's also a debate.
[29:57] And then Bernard says, "Greetings from
[29:58] the Pythonistas at Europython." Nice. I
[30:01] think Marlene is there this week because
[30:02] she's keynoting. So, I don't know if
[30:05] you've said hi to Marlene Mongami yet.
[30:08] She's from my team. Um, I think she's
[30:13] keynoting.
[30:15] Um,
[30:17] okay. So, yeah. So, say hi to Marlene
[30:22] and anyone else there?
[30:24] Okay. Oh, so the Ezri demo was this
[30:27] morning. Very cool.
[30:29] I love maps. Um,
[30:34] all right. Uh, oh, and GitHub copilot
[30:38] desktop app. It's really good. I Okay,
[30:40] so I will say I use the Copilot app like
[30:42] really extensively last week um for
[30:45] doing work in parallel. So the whole
[30:48] dream of having you know work in
[30:50] parallel I did like a bunch of PRs on
[30:53] Azure search openAI demo and we made a
[30:56] bunch of fixes also to be able to use um
[31:01] to be able to do stuff in parallel. So
[31:02] you definitely you need to if you want
[31:04] to be able to um test stuff in parallel
[31:07] you do have to make sure that like
[31:10] everything is parallelizable. So, you'll
[31:12] see I had to make various
[31:15] um I did have to make various
[31:17] improvements last week to make it more
[31:21] paralyzable. Like this was
[31:24] um this was actually one of the fixes I
[31:26] had to make. Especially because I'm
[31:28] using, right? So, especially if you're
[31:30] using
[31:32] uh you do need to, you know, do some
[31:34] amount of work um to make it more
[31:37] paralyzable. Let's see what else.
[31:40] Uh
[31:43] um right this was the port variability.
[31:47] Okay. So there was stuff like um we had
[31:50] to make sure that a like the way we were
[31:52] using a um that we were doing it based
[31:56] off this Azure MP name um because that
[31:59] way uh it you can you when you run a
[32:03] because basically all of my all of my
[32:05] sessions are trying to do a up and
[32:08] they're doing it with different uh ACD
[32:10] environments and they set a the Azure M
[32:13] name in order to do that when they're
[32:15] like running the ACD commands. Um, and
[32:17] we actually have a skill that we're
[32:19] using specifically for um, being able to
[32:22] run ACD
[32:24] commands independently of each other
[32:26] that sets that as your M name. Um, but
[32:29] you have to make sure that then whenever
[32:30] you're getting those values in your code
[32:32] that you're, you know, you're getting it
[32:34] in a way that's compatible with that.
[32:35] So, I had to make that change. I had to
[32:37] make it so that port was configurable so
[32:39] the app could run on multiple ports. Um,
[32:42] I had to make sure that like Yeah. So
[32:45] anyway, there's I'm excited because now
[32:47] I can finally run um do full AZD ups in
[32:52] parallel and that to me has been a huge
[32:54] unlock because so many of the changes
[32:57] that we make to this app are dependent
[33:00] on deployment and if I can't if the
[33:03] agent can't deploy then that makes me
[33:06] the blocker right but now that it can
[33:07] deploy like h it's just so much more
[33:09] capable now uh let me find oh I archived
[33:13] all my sessions
[33:14] Um, let me see if I can show you my old
[33:16] sessions because most of them are
[33:17] archived. But, um,
[33:23] uh, where did we do it? Uh, this one
[33:26] maybe. Let me check this one.
[33:29] Restore.
[33:35] Because there was one where I was just
[33:36] like, "Hey, I'm going to bed. I'm tired.
[33:39] Deploy everything overnight and tell me
[33:40] how it worked." Let me see if it was
[33:42] this one.
[33:46] morning report. Here we go.
[33:50] I think there was an earlier morning
[33:51] report. Let me find my Let me see. Okay.
[33:54] All right. Yeah. So, maybe So, at this
[33:56] point, I said, "Okay, it worked. I
[33:59] didn't even look at these logs. It
[34:00] worked for a long time." Okay. I am
[34:02] going to bed now. So, do as much testing
[34:04] as you can in the meantime. Thank you.
[34:06] Report back in the morning. Try other
[34:08] EMVs as well, like Azure EMVs. Um, and I
[34:11] was even connected to a VPN because this
[34:13] was testing private deployment.
[34:16] Um, so this was so this tested
[34:23] right and so then we had the morning
[34:24] report that said good morning overnight
[34:27] testing is complete. Here is the report
[34:30] um all green. So you can see it actually
[34:32] deployed it did four different
[34:34] deployments uh including like like
[34:36] existing add environments new
[34:38] deployments
[34:40] um verified everything um and that's so
[34:44] useful right because this would have
[34:45] been like an entire like I don't know it
[34:47] would have taken me hours right just
[34:48] like babysitting this and checking and
[34:51] yada yada so being able to have your
[34:54] agent do cloud deployment obviously to a
[34:57] testing environment right these are all
[34:58] testing environments but being able to
[35:00] have them to deployment to a testing
[35:02] environment is so helpful when you're
[35:04] making um you know projects that are
[35:07] heavily dependent on deployed services
[35:09] like these Azure services as all of
[35:11] these are. So um definitely recommend
[35:15] being able to do that um and also being
[35:17] able to do it in parallel right because
[35:19] last week I had a bunch of these things
[35:20] going in parallel because I was making a
[35:22] a bunch of improvements to the app and
[35:24] that was a huge unlock as well.
[35:27] Um, okay. I let me check up on the chat,
[35:30] right? Um,
[35:32] oh, so Adam says it's able to detect if
[35:35] you're using the computer. Interesting.
[35:38] Okay. Uh, I'll ask the team about that.
[35:41] Um,
[35:43] uh, let me see if there's any more
[35:45] questions on Copilot. So, Anor said, can
[35:48] you can you run codeex inside of Copilot
[35:51] desktop? Um, do you mean like can you
[35:53] use like the codeex CLI? I think you can
[35:56] in VS Code. I don't know of a way of
[35:59] doing that. Interactive
[36:02] default agent. No, these are my agent
[36:04] modes.
[36:06] Um I don't see a way that you'd use like
[36:09] I because I think it's so dependent
[36:10] because the co-pilot app is really built
[36:12] on top of the co-pilot CLI harness.
[36:16] So, I don't think Oh, I should have
[36:20] streamer mode on. Um, so we don't show
[36:25] secret stuff. Uh, accounts sessions.
[36:30] Um, yeah, I have like my details about
[36:32] how to deal with work trees. Um,
[36:39] yeah. So I think that I think that you
[36:42] know with the copilot app that it's
[36:44] because it is so based off the copilot
[36:46] CLI harness I don't think it has a way
[36:49] to use the codec cli as the harness
[36:51] instead.
[36:53] Yeah. Yeah. So yeah, I think because we
[36:55] do have that in um we have that here,
[36:59] right? Because here you can say well I
[37:01] don't have codeex here but um you know
[37:03] you've got like claude uh I think if you
[37:06] had codeex maybe you would see codeex
[37:08] here because I think v code is
[37:10] definitely the most agent agnostic right
[37:13] like that's generally the the selling
[37:15] point for vs code is that it has the
[37:17] most flexibility right so you can use it
[37:18] with different extensions you can use it
[37:20] with different harnesses you can do the
[37:23] copilot app is more opinionated and I
[37:25] don't know if they're ever going to be
[37:26] as um you know as like agnostic as VS
[37:32] code. Um
[37:34] so yeah so I would say
[37:38] as far as I know you can't use it in
[37:41] there. Uh okay Bernard says dentic
[37:44] workflows can use multiple model
[37:45] providers. That's good.
[37:48] Um so yeah I think the answer is no for
[37:51] codeex. Um but I can ask later as well
[37:53] to see if that would ever be supported.
[37:57] Uh, Bernard is missing a refresh content
[37:59] button. What do you need to refresh on?
[38:02] The right side or the left side?
[38:06] Um,
[38:08] okay.
[38:10] All right. Let's see. We had some more
[38:14] comments here. Uh, Kevin wanted
[38:17] documentation on building and deploying
[38:19] agents in AKS.
[38:24] Um,
[38:27] let me ask my colleagues for that one.
[38:31] Uh, should you use hosted agents and can
[38:34] you register for foundry?
[38:37] Uh, those are all great questions. I
[38:39] have not done anything with AKS. Um
[38:46] getting
[38:48] let me let me ask.
[38:57] All right.
[39:04] I'll ask I just asked about some AKS
[39:07] guidance. Um so we'll see. All right.
[39:11] John asked, "Can I explain the
[39:13] differences between agent architectures?
[39:15] Like why deep agents?" Uh, it's not as
[39:18] much the architectures as much as like
[39:21] the things that get added on top of it,
[39:24] right? Um, because really a lot of this
[39:27] is implemented as as like middleware,
[39:30] right? So like compaction
[39:33] that's it's like you know you can
[39:35] implement compaction as a middleware and
[39:38] so you can add your own compaction to
[39:40] any agent right like you just need to
[39:42] intercept and say like oh oh it looks
[39:45] like you know this we've gone over the
[39:47] context window limit so let's you know
[39:49] summarize and then update the messages
[39:52] list with the summarization right so you
[39:55] can implement compaction as middleware
[39:58] on top of an agent um the advantage of
[40:01] you know the harness and deep agents is
[40:03] that it's just it's built in because
[40:06] it's so common that so many people want
[40:09] to have that particular middleware. Um
[40:11] and I would say a lot of this is
[40:13] basically
[40:14] middleware of you know intercepting what
[40:18] the agent is doing and um you know
[40:21] either and like guiding it to do it a
[40:23] certain way or giving it certain tools
[40:25] right so the to-do provider that's
[40:27] probably implemented as tools to say
[40:29] okay every time like a lot of these
[40:31] could be implemented as tools where you
[40:33] say like okay now the agent always has a
[40:35] to-do tool right so it can decide to
[40:38] store a to-do um you know same thing
[40:41] with memories, right? Like um that might
[40:43] be implemented as a tool where the agent
[40:47] has this memory tool and can decide um
[40:49] whether to use it, right? So
[40:53] yeah, so I guess I don't know that I
[40:54] don't think I would necessarily try call
[40:56] this architecture. I guess the most
[40:59] architectural aspects of this is the
[41:02] looping, right? So looping I mean an
[41:04] agent already is a loop. This is like
[41:07] looping even harder. Um,
[41:10] right. Um, so this one is like, you
[41:14] know, it's like the Ralph loop idea
[41:15] where you're like, you know, you have
[41:17] the default agent loop. Um, but
[41:19] sometimes that's not enough, right? Like
[41:21] it doesn't it doesn't go as hard as you
[41:24] want it to go and you need to force it
[41:26] to loop even harder, right? And they
[41:28] have um they have different ways of
[41:31] enforcing it, right? Say you can say
[41:33] like number of iterations like um you
[41:37] know while you still have to-do list or
[41:40] you just you know do your own custom um
[41:43] you know custom call back there. Um so
[41:46] that's kind of a more architectural
[41:49] change where you're forcing it to loop
[41:52] until some condition is true. Uh
[41:55] background agents would also be you know
[41:57] that sounds more architectural to me. Um
[42:02] uh so that's a and you know that that is
[42:04] enabling
[42:05] um delegation to background agents. Uh
[42:08] so that's and that's helpful and that's
[42:11] also something they have in in deep
[42:12] agents and that's can be better you know
[42:15] better for context window management um
[42:18] because each agent has their own context
[42:20] window um and also could just be better
[42:22] for performance if they're able to do it
[42:24] in things in parallel. You do have to be
[42:26] careful because sometimes like as some
[42:28] people are saying like GD56 uses um
[42:31] agent delegation sub agents too
[42:33] aggressively. Uh sometimes it doesn't
[42:36] need to use it. So if you are going to
[42:38] enable something like background agents,
[42:39] you do want to have like a good use case
[42:41] for it, a good scenario and you probably
[42:43] want to give it some um guidance as to
[42:45] when it should use those agents and when
[42:47] it like when it when it when should it
[42:49] use sub agents versus not so that you
[42:51] don't accidentally, you know, use up
[42:54] more tokens. um you know there's a
[42:57] whenever you're dealing with
[42:59] parallelization right there's a certain
[43:00] point at which it becomes useful to
[43:02] paralyze
[43:04] um and before that point it's not useful
[43:06] just because of the startup costs of
[43:07] parallelization and of having these
[43:10] multiple things go off and coming back.
[43:12] So um you want to think carefully about
[43:13] that but that is that would be an
[43:15] architectural change is to have sub
[43:17] agents working on that.
[43:21] Uh D. So in terms of use cases, uh I
[43:25] mean I think a lot of uh like generally
[43:28] these harnesses are going to be
[43:30] particularly good when you have these
[43:33] more generic agents that you know need
[43:37] to be used for a wide wider range of
[43:41] tasks, right? I think the more like the
[43:43] more when your when your scenario is
[43:45] very focused, I don't know that you're
[43:47] going to need everything in this harness
[43:49] because it it's so focused that you know
[43:51] maybe you already like you know exactly
[43:53] that you're not going to go over the
[43:54] context window, right? But the more you
[43:58] know the more open-ended your agents are
[44:01] that you're building uh then I think the
[44:03] more you're going to want this all the
[44:06] capabilities that are in this harness.
[44:12] All right. And then Pablo says, "What is
[44:15] the state of knowledge graphs in work IQ
[44:18] and Azure AI search?" Um,
[44:22] that's a good question. Um, they are
[44:27] they're they are looking into um graphs.
[44:30] I on the I know on the Azure AI search
[44:33] they are um they are looking into graph
[44:37] rag again. Um
[44:40] uh so
[44:42] hopefully we'll see something there. um
[44:45] they don't there's nothing there's
[44:46] nothing um available yet but um but yeah
[44:49] we're we're still getting folks that are
[44:51] very interested in something like um
[44:55] like graph rag and the the whole trick
[44:58] is how to implement that in a um like a
[45:02] cost-effective way for so for example
[45:05] uh like we were looking at this feature
[45:06] right of graph rag um
[45:10] so this here right like so whole data
[45:13] set reasoning
[45:14] And in graph rag what it does is um you
[45:19] know it has clusters of information. So
[45:24] um you know you have like these LLM
[45:26] based clusters and um it can then answer
[45:30] the questions based off the clusters and
[45:32] so that way you can kind of answer these
[45:34] more zoomed out questions. They call it
[45:36] global search. I think of it as like
[45:37] zoomed out questions, highle questions.
[45:40] um they call it also kind of like a map
[45:42] produce for for queries right so the
[45:45] question is how do you do this in a more
[45:50] performant way um and one approach would
[45:54] be like to premputee those clusters
[45:56] right so if you were going to implement
[45:57] this yourself like on Azure AI search
[45:59] you know you have your index then you
[46:01] could premputee clusters semantic
[46:03] clusters and store those in like
[46:06] separate indexes and then you could have
[46:08] a router to decide ide when you're going
[46:10] to, you know, use a semantic cluster
[46:13] index versus the, you know, the actual
[46:16] original um document index, right? That
[46:18] would be um how I would try to implement
[46:21] it. So, yeah. Anyway, so there um
[46:23] there's still investigation into graph
[46:25] rag and whether that can be made um uh
[46:29] baked into a more productionfriendly
[46:33] way uh more performant way. So, nothing
[46:37] to announce yet.
[46:39] Uh on that note uh but could happen in
[46:42] the future. Um the other question was on
[46:44] work IQ.
[46:46] Uh so work IQ
[46:50] has is changing all the time. Um
[46:54] and we are we're going to have the live
[46:57] stream about it in two weeks. So if
[46:59] there's something particular that you
[47:01] want to see in that live stream, this is
[47:03] a good time to ask. Um, I'm just looking
[47:06] for their reference stocks because I
[47:07] know so they have the work IQ MCP, but
[47:10] there's also the A2A
[47:13] now. Yeah, the A2A. Um,
[47:19] and I thought that the A2A also had
[47:24] more
[47:26] capabilities. REST API A2A CLI
[47:35] uh
[47:38] A2A gateway. So there's ask
[47:43] work IQ.ask ask
[47:47] screaming. Okay. List agents.
[47:52] Okay. A2A capabilities. All right. And
[47:55] then what about the rest API?
[47:58] What is in the rest API?
[48:08] So in the MCP we've got um so it has
[48:14] fetch versus create. So it does have
[48:16] this do action now. So that's
[48:19] interesting. Now in the MCP that um they
[48:23] are distinguishing between fetch versus
[48:26] write operations right so create entity
[48:29] do action fetch
[48:32] um so that's good they have different
[48:34] tools now okay so fetch create entity
[48:37] okay so then they basically have fetch
[48:39] CRUD do action call function okay um
[48:45] yeah so I don't okay so the original
[48:46] question was about graphs um I Guess the
[48:49] question is like you know what what what
[48:51] are you looking for out of work IQ and
[48:53] graphs right like it's going to you know
[48:56] when it's doing fetching it's going to
[48:58] use whatever indexing it uses behind the
[49:01] scenes um that's not uh that that kind
[49:04] of changes all the time um so you have
[49:07] to really test it out to see if it's
[49:09] fetching um well enough for you um you
[49:12] know it is using Microsoft graph
[49:14] endpoints um
[49:17] but Um,
[49:19] yeah, it's going to it's going to decide
[49:21] how it maps, you know, how it decides to
[49:25] answer a question.
[49:31] Wait.
[49:35] Um, okay.
[49:38] So, Honor says, "I connected my agent
[49:40] that uses agent framework with Langfuse
[49:43] for observability. Any observability
[49:45] tips?"
[49:47] Uh I haven't used length views recently.
[49:49] I assume it is. Let me get my I did do a
[49:53] talk on this last week.
[49:56] Uh
[50:00] let me find it. Open telemetry. Okay. So
[50:04] the thing that I always recommend is
[50:10] oh it's already open. All right. Here we
[50:12] go. um is you know to try to use open
[50:15] telemetry.
[50:16] I assume language is using languages is
[50:20] using that and then you know one use
[50:22] open telemetry so you get more
[50:24] portability. If you use the genai
[50:26] semantic conventions, it also gives you
[50:28] more portability because if you if
[50:30] Langfuse is using the genai semantic
[50:33] conventions, then you can also export to
[50:37] Foundry like to app insights. You could
[50:39] export to app insights and then you can
[50:41] see it in both places because we
[50:43] actually have pretty good um views right
[50:46] now for for the observability. Um
[50:52] so I don't know it gives you more
[50:53] options. So I yeah I haven't used
[50:54] Langfuse recently. So I I mean I think
[50:56] like if Langfuse gives you all the
[50:58] observability you need then that's
[50:59] great. Um but we do actually have some
[51:02] really nice observability
[51:04] now. Um
[51:06] and it even works for agents like across
[51:09] different um different uh clouds. So you
[51:13] can even equip like a AWS agent or a
[51:17] Google cloud agent with open telemetry
[51:20] and you could still um you know export
[51:23] that to
[51:25] uh to to app insights. Let me see if I
[51:28] can see my
[51:30] uh
[51:33] is this last day? Let me do a month.
[51:37] Okay. So here, right? So these are all
[51:42] um based off of the open telemetry.
[51:46] Um I also have eval here. And then we
[51:48] can also open an Azure monitor.
[52:01] Uh so you can see in Azure monitor that
[52:03] Azure monitor this is all but only
[52:06] because of using Genai semantic
[52:08] conventions. Um so as long as like
[52:10] you're using Genai then you get all this
[52:12] stuff too and then there's also like
[52:14] observability agent that you can ask
[52:17] questions about and be like hey what's
[52:19] going on here right we can see the token
[52:21] consumption
[52:22] um coming in here. Uh so so yeah so I
[52:27] would encourage you to use open
[52:30] telemetry and the geni span conventions
[52:33] so that you get all these benefits
[52:35] um and uh you can even do that with
[52:38] agents that aren't on foundry right and
[52:40] then you also get this nice if you're
[52:42] doing a math agent that's hosted in
[52:44] foundry then you also get like a really
[52:45] cool let me see if I can is it still
[52:48] running here playground
[52:51] uh what's the
[52:55] in today. Okay. I don't know. Um I just
[52:59] want to get a trace here so I can show
[53:01] the current trace UI.
[53:09] Okay. So, Honor says you have language
[53:11] running in Docker locally and on the
[53:12] server for the app and so you're using
[53:14] the local instance. Um yeah, that is
[53:18] cool. Yeah. So if you were doing um the
[53:24] yeah the equivalent for us for local
[53:26] would either be Aspire or just exporting
[53:30] to app insights anyway from locally.
[53:33] Uh but um I mean it sounds like if
[53:37] you're using Langfuse like their whole
[53:38] thing is observability. So I would think
[53:40] that like it's a pretty good setup. I
[53:42] remember really liking it when I used
[53:43] it. Um I did want to show off the
[53:45] foundry tracing now because this is
[53:47] pretty cool here. So you can see um you
[53:51] know as it goes through and all the all
[53:53] the different calls here uh that are
[53:56] being instrumented
[53:58] and you can see here the the you know
[54:00] the genai conventions that each of them
[54:03] is is using here right so for tool call
[54:06] you know if we look at the metadata here
[54:09] um
[54:11] you can see genai.tool.arguments
[54:13] arguments generate a tool type
[54:15] description. Right? So, yeah. So, it's
[54:20] just I I'm just saying I'm say I'm I'm
[54:22] just putting a plug here that uh the
[54:24] foundry observability I'm impressed.
[54:27] It's I think it's it has gotten uh much
[54:30] improved um because I remember using
[54:32] Lenfuse in the past and thinking like,
[54:34] oh, Lenfuse was a lot easier to use, but
[54:36] now I do think things are getting um
[54:39] like a lot more easy to use on the
[54:41] boundary side.
[54:43] Yeah, I mean it's it's not quite a
[54:46] debugger, but it's certain it's like,
[54:49] you know, it's like a slick UI for going
[54:51] through the calls. Um, you can also do
[54:54] like the user view and like replay it.
[54:56] Like this is more useful when you have
[54:57] like multiple agent calls happening. Um,
[55:01] uh, and and yeah, and then there's like
[55:03] you can have a so you know, as Honor
[55:06] says, like you have a skill to diagnose
[55:08] his issues. So I think that's a great
[55:09] idea. I mean agents like in terms of
[55:11] getting agents to do mundane for stuff
[55:13] for us. They're so good at looking
[55:15] through logs, right? Like if you you
[55:18] know so I think that's something you
[55:19] definitely want to do is make sure your
[55:20] agents can always connect to your logs
[55:22] and like know fully how to do that. That
[55:24] was something I added to the agents.mmd
[55:27] today was how do you inspect deployed
[55:29] sessions? Um like that's something like
[55:32] that you should have in like all of your
[55:34] agents. MD like it should know how to
[55:38] look for errors, right? Because then
[55:40] you're you're using it for doing, you
[55:44] know, the boring stuff. Like the hard
[55:46] thing is that you have to make sure that
[55:47] when it identifies a root cause, it's
[55:49] truly the root cause, right? Because
[55:51] sometimes, you know, it it it doesn't
[55:53] know something that, you know, and it'll
[55:55] just assume a root cause that is a red
[55:58] herring or something like that. Um, but
[56:00] it's still it's just so so helpful. Uh,
[56:03] so I mean I think it sounds like you're,
[56:05] you know, you're you're doing good work
[56:07] with length views and taking advantage
[56:10] of both local and prod and uh having to
[56:13] look through stuff.
[56:18] Let's see. Um,
[56:21] okay. So Pablo followed up um, detecting
[56:25] data quality in work IQ.
[56:27] They both depend on the quality of the
[56:29] data stored. Does it have any
[56:31] intelligence in that sense? If not,
[56:34] there's a good reason. Create our own
[56:35] system for certain knowledge. Yeah, we
[56:37] actually got asked a similar question
[56:39] yesterday
[56:42] um about um how to structure a
[56:45] SharePoint for optimal agent retrieval.
[56:49] Um let me let me get find the answer for
[56:52] that. Um okay.
[56:55] Uh
[56:58] this was quite a long answer so let me
[57:01] put it in a file or something. Okay.
[57:07] Okay. Uh word app. Okay.
[57:12] Because here the question was you know
[57:14] how to how to architect your shareepoint
[57:17] right? Um and you know the point my
[57:19] colleague made was that um you know a
[57:22] good SharePoint
[57:24] for an agent is also good for a human
[57:27] right. So you know stuff like um
[57:31] ownership clearly defined metadata
[57:33] applied consistently permission models
[57:34] reflect business as requirements
[57:37] authority sources are easy to identify
[57:39] content domains. So these are all things
[57:41] that are going to make it much better
[57:43] for the agent um but also going to make
[57:46] it better for for humans. Um but she was
[57:49] suggesting like architect for the
[57:51] enterprise first and agent conception
[57:54] second and assume that you know that you
[57:58] know agents are going to be layered on
[57:59] top of that and be able to take
[58:00] advantage of this.
[58:04] Um
[58:08] yeah
[58:12] so yeah so I don't really know exactly
[58:14] how work IQ is implemented but you know
[58:18] if you are doing something like you're
[58:21] you know creating SharePoint for
[58:23] consumption from agents then you should
[58:26] just follow the best practices for
[58:28] SharePoint generally
[58:30] and and it should flow through to agents
[58:33] Okay. Oh, I just got a report from Nick
[58:36] Brady is that hosted agents is GA.
[58:40] All right.
[58:42] Um, so for those of you So, was LPK
[58:44] wondering about hosted agents, they are
[58:46] now GA. I don't know where that's
[58:49] documented, but we got it straight from
[58:51] the PM. So, here we go. Uh, knowledge
[58:55] catalog. Let's see. Dynamic knowledge
[58:58] graph. Okay. I haven't seen this yet.
[59:01] Um, I will ask
[59:04] if anyone's poked into this knowledge
[59:06] graph or is this maybe what my
[59:07] colleagues were talking about something
[59:08] last week. Let me see if this is what
[59:10] they were talking about. Maybe this is
[59:12] what they were talking about. Knowledge
[59:13] catalog.
[59:15] Knowledge catalog.
[59:18] Oh, yeah. Okay.
[59:21] Um,
[59:23] oh, we actually have looked into this.
[59:25] Okay. Um, yeah. So there's uh the AI
[59:30] search team is is aware of this and
[59:32] looking into some learnings from this.
[59:36] Um
[59:39] oh and this has this OKF format. Yeah,
[59:42] we did actually chat about this a lot.
[59:44] Um
[59:47] and
[59:49] uh let's see
[59:54] trying to also figure out like how to
[59:55] relate this to fabric. So my colleague
[59:59] Alvaro forked it and was playing around
[01:00:02] with
[01:00:04] um using this with fabric ontologies.
[01:00:08] Um
[01:00:11] let me just link to this one in case any
[01:00:13] of you are using fabric. Yeah, so we
[01:00:15] were looking into that OKF
[01:00:18] form format. Um
[01:00:22] and
[01:00:24] you know they they're using the front
[01:00:25] matter to build some ontology
[01:00:28] relationship path. Okay. Um
[01:00:31] entity types.
[01:00:34] Okay. So yeah he was figuring out how
[01:00:36] this because it seems the most similar
[01:00:38] to fabric ontologies in terms of ex like
[01:00:40] a kind of existing graph type things
[01:00:42] that we have at Microsoft. Um, so this
[01:00:46] is his fork where he was playing with
[01:00:49] that. So that might be fun to look into.
[01:00:52] Uh, so yeah. So it sounds like we're we
[01:00:54] are generally looking into
[01:00:56] um, you know, this sort of thing and we
[01:01:00] just have to figure out you know what
[01:01:01] approach is going to work well and
[01:01:04] what's going to scale you know to the
[01:01:07] kind of sizes that people expect from
[01:01:11] Microsoft products.
[01:01:13] That's always the hard part.
[01:01:18] All right.
[01:01:20] Okay. All right. We are over time now.
[01:01:22] So, uh let's close up the stream now.
[01:01:27] Thank you everyone for coming for all
[01:01:30] the sharing everything so that we all
[01:01:32] keep learning together.
[01:01:34] And uh let's see, next week uh next week
[01:01:39] I'll have to postpone the office hours
[01:01:41] probably till Wednesday because I'm
[01:01:44] doing a
[01:01:46] um a cohhere workshop on Tuesday. Uh so
[01:01:50] I'll probably postpone the office hours
[01:01:52] till Wednesday instead and then and then
[01:01:56] I can tell you all about coher after
[01:01:58] that.
[01:01:59] Um, and then yeah, we have the Microsoft
[01:02:01] IQ series. So, you know, sign up for
[01:02:04] that if you didn't yet. And we're also
[01:02:07] working on some MCP stuff. So, we're
[01:02:09] going to do Oh, that's the same. I just
[01:02:12] did the same thing. Delete. Uh,
[01:02:16] let me post the IQ series.
[01:02:19] And we are also working. We're going to
[01:02:21] do an MCP live stream. Keep up the love
[01:02:24] for MCP. Uh, that will be September 8th.
[01:02:28] And we're going to do MCP in person
[01:02:30] events in San Francisco and also
[01:02:32] Bengalaru.
[01:02:33] Um we'll see if we and if we do any
[01:02:36] other ones. So yeah, we got some stuff
[01:02:39] coming up. All right. Thank you
[01:02:42] everyone. I'll see you next week,
[01:02:45] probably Wednesday. Bye.
