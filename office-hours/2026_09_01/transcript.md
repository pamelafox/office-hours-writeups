[00:00] Welcome everyone. Uh so as as usual,
[00:04] I'll
[00:05] start off with some news and what I've
[00:09] been up to. Um so on the news front,
[00:14] actually what I'm most excited about is
[00:16] that fast MCP vision version 4 is now
[00:20] stable. I saw this last night that this
[00:24] is now stable. And this is exciting
[00:27] because fastmcpv4
[00:29] works on the new sessionless protocol
[00:31] and supports the old protocol 2
[00:35] basically does like a little negotiation
[00:37] to figure out which one to support. Um
[00:40] so it can support both. So you should be
[00:43] able if you're already using fastmcp you
[00:46] should be able to um to upgrade to v4.
[00:50] There is an upgrade guide. So, I would
[00:52] just, you know, if you have anything
[00:54] built in Fast MCP, I would, you know,
[00:57] open up your coding agent, point them at
[01:00] the upgrade guide, and, you know, have
[01:03] them try everything out, run the test,
[01:05] and see um if stuff is still working.
[01:08] And, you know, you'll want to test both
[01:10] with the clients that support
[01:12] sessionbased things and clients that
[01:15] support uh only support the old one. Um
[01:20] and there's a good website where you can
[01:23] check to see um the current current
[01:27] support for for different aspects of
[01:30] MCP. This is can I use.dev.
[01:34] Uh so let me link here
[01:37] before
[01:39] and then this this one is can I use for
[01:42] MCP stuff. So that's useful to see just
[01:44] what um which protocol versions are
[01:47] being supported, right? If you're
[01:49] depending on what clients you are
[01:51] targeting.
[01:53] Uh so definitely check that out.
[01:57] I see there's a lot of chatter in the
[01:58] chat already. So uh looks like we've got
[02:01] some things people want to talk about.
[02:04] Um
[02:07] uh okay. Okay. So, just to follow up on
[02:08] MCP, do I have a link to discuss
[02:11] about secure MCP developing? I mean,
[02:13] secure MCP um you know, there's there's
[02:17] a uh that can mean a lot of things. Uh
[02:20] and I think we've talked about this
[02:21] before. Um
[02:24] you know, so when you go to this website
[02:26] mcp.org,
[02:28] most of the security discussion here is
[02:30] about off. And I think normally um
[02:36] you when Pablo when you ask about
[02:38] security you're talking about more about
[02:40] like injection attacks and stuff like
[02:41] that. So that's not covered as much in
[02:45] here. So here when you go to security uh
[02:48] it's pretty much all authorization
[02:51] aspects. Um these are all pretty much
[02:56] almost all of these pretty much all of
[02:58] these are about
[03:00] um authorization. So uh good feedback
[03:04] for uh the MCP team is that you know it
[03:08] sounds like you probably you you're
[03:10] looking for more resources beyond the
[03:14] authorization aspects, right?
[03:17] Um you're looking for other sorts of
[03:20] attacks. Yeah. How to how to protect
[03:25] the MCB server from your own agent when
[03:27] itself is not working safely. I guess
[03:30] the question is what kind of attacks are
[03:31] you are you envisioning right? Are you
[03:34] looking for prompt injunction?
[03:36] Um you know
[03:40] what are we looking for there? We can
[03:42] look for some more resources. Okay. now.
[03:45] Yeah, I think everyone
[03:48] um everyone wants to talk about
[03:50] security. Okay, so yeah, so [laughter]
[03:53] let's talk about this um the hugging
[03:55] face instant. There's been a lot of
[03:58] different um posts and videos and
[04:01] whatnot. So there was a black hat talk
[04:03] that was from the OpenAI team. There was
[04:06] this independent investigation.
[04:09] Uh there was the Dwaresh I this morning
[04:11] was just reading the Dwares
[04:14] hotel version but actually I was reading
[04:17] criticisms of this one. Um so uh you
[04:23] know this is another one you can read
[04:25] but um uh I actually haven't I haven't
[04:29] read through any of them in total. I was
[04:31] actually mostly reading the criticisms
[04:32] of this one because this one this is
[04:35] from Darkish Patel who has an amazing
[04:37] podcast. So, if you're not listening to
[04:39] his podcast yet, that's a great one if
[04:40] you do listen to podcasts. Um, because
[04:43] he's got great interviews. He's a very
[04:44] good interviewer. And so, you know, this
[04:47] one does give this timeline of, you
[04:51] know, what happened except the criticism
[04:53] of it that is it it anthrop overly
[04:56] anthropomorphizes the agents, right? It
[04:59] calls them agent civilizations. It is
[05:01] like describes like Oh, I think at one
[05:03] point it says it faked their own death.
[05:06] Yeah. the agents didn't manage to fake
[05:08] their own deaths. Right? So this is very
[05:10] much anthropomorphizing the agents. So
[05:12] it is like a correct description of what
[05:15] happened but really really assigning um
[05:18] a lot of like almost like emotional
[05:20] motivation to these agents. Um whereas
[05:24] really what happened is that OpenAI, you
[05:27] know, put these agents into a sandbox
[05:30] that wasn't properly protected, right?
[05:33] like it's not really a sandbox if you
[05:35] haven't really disabled the you know the
[05:38] ability to to reach out to the network.
[05:40] So it wasn't even a true sandbox. They
[05:42] didn't have their monitoring on, right?
[05:43] So it's a great list of things not of
[05:45] what not to do, right? They really
[05:46] didn't do a good job. like people in the
[05:49] security space are looking at this going
[05:50] like uh yeah of course you know uh
[05:54] you're you're basically put these agents
[05:56] in a situation where you're like
[05:59] rewarding them for um you know for being
[06:03] able to get out and they were able to
[06:04] get out easily because it wasn't a true
[06:06] sandbox right so um you know so I think
[06:09] this is more a security learnings right
[06:11] like if um you know if if you
[06:17] uh you know don't um properly sandbox
[06:20] and properly log, right? The other thing
[06:22] you can do is logging, right? Like so
[06:24] being monitoring like hey um you know
[06:28] did these are these agents uh going out
[06:32] of the network, right? Um there's
[06:35] uh you know a lot of things from a
[06:36] security perspective that
[06:39] um you know you should do instead. Uh so
[06:43] I was reading the Gary Marcus'
[06:48] review. [laughter]
[06:49] Uh, yes. So, Nambdi says it feels more
[06:51] like Doom theater to drum up support for
[06:54] data centers. Um, okay. So, this was a
[06:58] good So, five lessons from the OpenAI
[07:02] hugging face incident. Um,
[07:05] let me find it.
[07:07] Yeah. So he talked here about, you know,
[07:11] sandboxing
[07:14] um
[07:15] and levels of security, right? When you
[07:17] whenever you're doing security, you want
[07:19] levels of security, right? So one person
[07:21] I saw pointed out is that they said I
[07:23] guess in the prompt it says it said you
[07:27] should you do not have access to
[07:29] internet versus you should not access
[07:31] the internet, right? Because I think in
[07:33] the prompt they said you do not have
[07:34] access to the internet. Um but then once
[07:36] they realize they did have access,
[07:37] they're like, "Oh, great. We're going to
[07:38] access the internet." Right? So
[07:40] obviously like your prompts should be
[07:41] better, but you should not be relying on
[07:43] your prompts, right? So you should have
[07:44] sandboxing. Um but then you should also
[07:47] be having like monitoring, right? So in
[07:49] case something gets out of the, you
[07:51] know, you can have monitoring that's
[07:52] inspecting network traffic, right? Um
[07:56] and OpenAI has this monitoring. They
[07:58] just didn't have it turned on at the
[08:00] time, right? So they said like you know
[08:02] if our monitoring system was running it
[08:04] would have caught it like before right
[08:06] and it would have paged the security
[08:07] team
[08:09] um and they had all sorts of you know uh
[08:12] chains of thought that indicated what
[08:13] they were doing right so you really want
[08:14] defense and depth um and uh you know
[08:19] there's right so you know example you
[08:22] know enforcing network restrictions
[08:25] um a they have an LLM that's judging
[08:28] each action to decide uh they have
[08:31] health checks, right? Um, you can have
[08:35] canaries, right? So, you can like set up
[08:37] like a honeypot, which is like, oh wow,
[08:38] if it got to the honeypot, like then
[08:40] something is already wrong, right? So,
[08:42] honeypot is kind of trying to tempt
[08:44] them. Uh, so this is all like security
[08:47] we've known about for a while.
[08:50] Um,
[08:52] so yeah, like it just means we all have
[08:54] to have better approach to security. Um,
[09:00] oh yeah, and this was the example of the
[09:02] prompt, right? Soft scoping, hard
[09:04] scoping. Uh, so yeah, you know, you
[09:06] know, just having system prompts is not
[09:08] enough. That's really model dependent.
[09:10] Uh, you really need to have, um,
[09:13] infrastructure things. Uh, so they have
[09:15] an example here of all their protection
[09:19] proxies, guardian agents,
[09:22] uh, an audit trail. Right. This is
[09:24] great. Actually, this is really good.
[09:25] This is my first time seeing it.
[09:31] Um, yeah. And for the question about the
[09:33] YouTube video, as I said, that is going
[09:35] to be posted here. It's recorded. It's
[09:37] posted each night. So, we'll have the
[09:38] YouTube video up of this office hours
[09:41] later today.
[09:43] Uh, yeah. So, John says it's the way the
[09:47] agents talk to each other is
[09:48] interesting. Okay. So, let's take a look
[09:50] at how they talk to each other.
[09:54] Was this [clears throat] how they talked
[09:56] to it? That's a funny way of talking.
[09:58] Are they talking with underscores?
[10:02] I once again like I really need respect,
[10:05] right? And they start I did hear, you
[10:07] know, they start shortening their talk,
[10:09] right? Um
[10:12] uh they really like leave out
[10:14] unnecessary words. And that's really
[10:16] interesting because one of the the
[10:18] things about LMS is that they're very
[10:19] very good at fluent English but yet they
[10:24] also happily
[10:26] uh use like a shorter English like
[10:28] almost like a a pigeon English like a
[10:31] they develop their own dialect and
[10:34] that's curious because they've mostly
[10:36] been trained on full fluent English and
[10:39] other natural languages. So, the fact
[10:41] that they start shortening tokens, I
[10:43] think that's really interesting, right?
[10:44] That they would
[10:46] um yeah, that they would start just
[10:48] dropping grammar because that uh that to
[10:51] me is itchy even harder. Like I would
[10:53] say like I would argue that if they're
[10:54] able to just arbitrarily shorten
[10:56] grammar, they actually have a better
[10:58] understanding. They have actually like
[11:00] if you can actually do that, I feel like
[11:02] that means you actually have a pretty
[11:03] good understanding of language, right?
[11:05] Because you can still we can still
[11:07] understand this, right? like they know
[11:09] what to shorten. Uh so that's pretty
[11:11] fascinating. Like how does that, you
[11:13] know, how does that come about? Like is
[11:15] it because of something that they're
[11:16] trained on? Like that that from a
[11:18] linguistic perspective, because I have a
[11:20] linguistics background, too. I I think
[11:22] that's actually really really um
[11:23] fascinating. Like I once wrote a
[11:25] linguistics paper about how, you know,
[11:27] because the internet, we were all
[11:29] starting to spell things differently
[11:30] because it was just shorter, more
[11:32] efficient. And this is kind of the same
[11:33] thing like you realize this efficiency.
[11:36] So the fact that LLM have realized it
[11:38] efficiency, it makes you wonder at what
[11:40] point in the training do they discover
[11:42] that it's more efficient to drop, you
[11:45] know, prepositions and stuff like that.
[11:46] Is it because of they're trained on
[11:48] Reddit threads or something like where
[11:50] people get shorter.
[11:54] Uh, okay. So Fei points out
[11:59] that um an AI this has triggered an AI
[12:04] kill switch bill. Okay. Uh, did this
[12:07] come out? Well, this says it's July
[12:09] 23rd, so that must have been an
[12:13] is it that long ago that it happened. I
[12:16] guess so. I guess it's just we've had
[12:17] the
[12:19] um
[12:22] is that I guess it's just taken a while
[12:24] for us to do all the writeups and the
[12:26] reports and stuff.
[12:32] So they want the ability
[12:35] to
[12:38] um
[12:40] shut down. Okay. Require cover
[12:42] developers maint to throttle suspend or
[12:45] fully shut down.
[12:47] Um graduate respons initial slowdown.
[12:54] Yeah. Very interesting.
[12:58] It it might be a good idea. Um I I think
[13:01] always the concern like I both do like
[13:04] AI safety uh improvements but there's
[13:08] also just the concern that we don't have
[13:11] the ability to regulate everything. So
[13:15] um yeah there's a question of like you
[13:17] know can we get everyone together to
[13:20] agree on you know on these things like
[13:23] on a more global level. Uh there was a I
[13:27] really like this post from Bill Gates.
[13:30] Um [laughter]
[13:32] uh where's his blog? Um
[13:34] Gates notes. Okay, this one
[13:39] uh this was I thought a nice balanced
[13:41] post about both the risks and the
[13:43] benefits of
[13:46] AI
[13:47] and you know what how he thinks we
[13:50] should go about it, right? The world
[13:53] needs a plan and
[13:56] uh h how do we create a framework for
[14:00] that?
[14:02] And he
[14:05] you know I wants I think he wants to
[14:06] bring together multiple governments for
[14:09] this right national leaders countries
[14:12] will need to learn from each other. And
[14:14] I like this idea here set aside some
[14:16] jobs for humans. So he thinks there
[14:18] should this be this idea of human
[14:20] reserved where particular jobs are just
[14:23] human reserved and this might be culture
[14:25] dependent. Um and some of them could be
[14:27] for economic reasons, some of them might
[14:29] be for social reasons
[14:32] and um you know like in health like just
[14:35] having right imagine a robot giving you
[14:38] awful news that you have cancer, right?
[14:39] You you would probably want a human to
[14:41] do that instead. um
[14:45] t changing taxes blah blah blah. So
[14:48] yeah, I thought this was an interesting
[14:50] post as well.
[14:53] Uh so Bernard says the element itself
[14:55] developed a memory error JSpace. Yeah, I
[14:58] remember this came out. Didn't this come
[14:59] out a few months ago? Yeah, the JSpace,
[15:02] right? And this this is kind of their
[15:04] thinking
[15:06] their thinking space.
[15:08] And you can like change something in the
[15:11] Jspace and then it'll change the the
[15:15] output there.
[15:20] You know, I was this is kind of
[15:21] unrelated, but I was watching a video
[15:23] about elephants yesterday and elephants,
[15:25] you know, we have this phrase, an
[15:26] elephant never forgets. And the reason
[15:28] is because elephants have this huge
[15:30] temporal lobe and that's way they can
[15:33] like remember an elephant that they met
[15:35] like five years ago at a watering hole.
[15:37] Right? So it's interesting just to see
[15:38] the I find it really fascinating to read
[15:41] about intelligence across animals and
[15:43] across plants. Right? There's a great
[15:44] book uh the light eaters which is about
[15:46] plant intelligence because you know we
[15:49] have so many ideas about what is
[15:50] intelligence because obviously LLMs are
[15:53] intellig there's definitely a big way in
[15:54] which they are intelligent. They're not
[15:55] the same as us. they, you know, they
[15:57] learn they, you know, we're training
[15:59] them in different ways than we learn,
[16:01] but you know, they have some every
[16:03] everything. There's all these different
[16:05] kinds of intelligence. Um, so plants
[16:07] have a kind of intelligence. Elephants
[16:09] have a kind of intelligence, right? And
[16:10] in some way, elephants are smarter than
[16:12] us. And an elephant can remember an
[16:14] elephant that they met five years ago,
[16:15] right? They have incredible long-term
[16:17] memory because that's what their brain
[16:19] decided to optimize for.
[16:24] Uh Tanish says LLMs are mainly developed
[16:27] by Claudethropic.
[16:29] Uh no, LM are developed by many many um
[16:32] you know organizations. Uh where's the
[16:34] like artificial intellysis?
[16:36] [clears throat]
[16:37] What's that one that shows
[16:41] this one?
[16:44] Artificial analysis. Right. So here if
[16:46] we look at the current top models on
[16:49] this benchmark, right? We can see it
[16:51] puts Opus 5 at the front. I think a lot
[16:53] of us don't like Opus 5 as much. Uh, put
[16:57] it right next to Fable. Yeah, I think
[16:58] Fable is a bit better. Uh, 56 Soul.
[17:01] That's what I normally use. That's from
[17:02] OpenAI. Apparently, the new Grock models
[17:05] are quite good. Uh, I know some folks
[17:07] here have been using the Grock models.
[17:09] Uh, Kimmy is a really good one. GLM53.
[17:13] Apparently, that there was that model
[17:15] that they released um what was called 0x
[17:18] Alpha. So maybe some of you saw this was
[17:21] they released this model 0x Alpha and
[17:24] they didn't say what model it was and
[17:26] they just released it without saying and
[17:28] people tried it out and they're like oh
[17:30] my god this is incredible model and
[17:31] everybody was trying to figure out what
[17:33] model is it and I think it turned out it
[17:36] was basically GLM 5.3 right it was based
[17:40] off that one uh but it was an
[17:41] interesting approach to release that
[17:43] model without telling people anything
[17:47] um about uh you know what it what it was
[17:51] based off right they later did actually
[17:54] uh announce what it was based off I
[17:56] think but with GLM uh but there was a
[17:58] lot of you know getting people to try it
[18:00] without telling the new meta model is
[18:02] actually decent muse spark right so
[18:04] anyway so as you can see lots of people
[18:06] develop models
[18:08] um both open source or open weight
[18:12] models
[18:13] and uh lots of closed models as well And
[18:17] you know, we can track um roughly the
[18:22] quality
[18:24] over time.
[18:29] Okay. Uh let's see what else. Oh,
[18:31] Bernard, this looked fun. Okay, so you
[18:33] probably also heard the other thing that
[18:35] happened last week. I didn't even note
[18:36] this because it wasn't like didn't
[18:38] necessarily really happen, but um
[18:44] Nvidia, there was this I think it's
[18:46] still a rumor that Nvidia, right, has
[18:49] agreed
[18:51] Oh, I can't do Techrunch websites. Let's
[18:53] see. Mashable.
[18:56] Um, so there's this I think it's still
[19:00] technically a rumor that Nvidia is going
[19:02] to buy Hugging Face and um
[19:07] that would be very interesting. Hugging
[19:09] Face is kind of, you know, it's this
[19:12] website that has a huge number of
[19:15] opensource models and data sets and it's
[19:19] a great place for learning and uh
[19:22] finding stuff for machine learning. So
[19:24] if Nvidia acquired Hugging Face, you
[19:26] know, it would have access to this this
[19:28] whole ecosystem of open AI models.
[19:32] Uh but I don't think it's like for sure
[19:34] happened. So what happened last week or
[19:36] this week with Hugging Face is that they
[19:38] did launch Micro Duck, which is super
[19:42] cute looking. It's a small robot that
[19:45] you can um use with reinforcement
[19:49] learning
[19:50] and you know kind of so it already it
[19:52] has some RL behaviors that it starts off
[19:54] with right um so it does know how to I
[19:57] think walk when it starts off so it come
[19:59] it comes with learn behavior and then
[20:02] you can teach it to do stuff right and
[20:07] uh let's see it communicates with weird
[20:08] little sounds okay and um It gets its
[20:12] own little voice,
[20:14] right? So, it looks like a cool learning
[20:17] opportunity. Like, if you know, if I had
[20:19] like a classroom or something. I mean, I
[20:21] do have two little kids, so you know,
[20:23] maybe this could be their first real
[20:24] robot. We have some not so fancy robots.
[20:28] Um,
[20:30] I think it would be a good one for a
[20:31] classroom. It's $400, so it's not
[20:33] something I'm going to casually buy, but
[20:36] it's also within the realm of, you know,
[20:39] if you wanted a first robot to teach in
[20:43] a teaching situation, then that could be
[20:45] fun, right?
[20:50] So, I don't know if any of you are
[20:51] planning to get the micro duck like for
[20:53] Christmas.
[20:55] Family's first robot. Yeah, here's
[20:58] another report about Nvidia. Wait, so
[21:01] did it get
[21:04] This one says has reportedly acquired. I
[21:06] thought it didn't. I don't think it's
[21:09] It's not actually confirmed, is it? Um I
[21:13] think it's I thought it was still in
[21:15] rumor stages.
[21:17] Let's see. Let's ask the AI. Did Nvidia
[21:21] definitely acquire Hugging Face?
[21:29] reportedly
[21:31] closes in nears agrees.
[21:37] This one says acquires but this is in
[21:41] reportedly so I don't I don't I mean I
[21:44] think it seems very very likely but I
[21:46] don't think that either of them for sure
[21:49] confirmed it.
[21:51] So, I think we're still waiting
[21:55] for a confirmation.
[22:01] Uh, okay. What
[22:06] else? Um,
[22:09] let's see. Oh, a few weeks ago we talked
[22:11] about WebMCP, so I wanted to point out,
[22:14] let's see, is it due already? 2012.
[22:18] Okay, this is a fun animation. Um,
[22:20] [laughter]
[22:22] so they are having a challenge for
[22:25] WebMCP.
[22:27] It is due September 3rd. Okay. You still
[22:30] have two days. So if you have some
[22:33] availability the next two days, you
[22:35] could join the WebMC challenge. Um,
[22:39] and
[22:41] uh Oh, Ilia. Oh my gosh, Ilia's great.
[22:45] That's cool. I didn't know he was
[22:46] working on that. Um Sarah is also well
[22:50] known. I just met Alex. So yeah. So uh
[22:54] there's a you know chat GBT
[22:57] added formal support for WebMP now and
[23:01] that really elevates chat GBT to you
[23:05] know the web MCP right now that chat GBT
[23:07] formally supports WebMCP
[23:10] then you know that that really makes
[23:12] webc more mainstream right? So now
[23:14] there's really motivation for
[23:18] uh getting into WebMCP and for trying it
[23:21] out on websites to see where does it
[23:23] make sense to have web MCP where does it
[23:24] make sense to have a standalone backend
[23:26] like you know keep in mind like ideally
[23:30] you have an MCP
[23:32] a you know a proper MCP server for
[23:35] something that's like a backend API uh
[23:37] but there's places where web MCP uh
[23:40] might make sense as well um so yeah So,
[23:44] if you're interested in WebMCP, check
[23:46] out the challenge. Also, we should also
[23:48] be now able to try
[23:52] it out. Friend chat GBT.
[23:56] Let me double check because they did say
[23:58] chat GBT supports web MCP.
[24:01] I haven't actually tried it out yet.
[24:04] Okay. Chat site tools with web spins in
[24:07] this. Oh, this is in the chat desktop
[24:11] app. Okay. So I don't think we can do it
[24:13] on the web version.
[24:16] Uh but if you open a website, the
[24:17] builder asks you if the page offers site
[24:20] tools.
[24:24] Okay.
[24:29] I don't think Let me just check. I don't
[24:32] think I have the chatbt app. I could
[24:35] download it. All right. Yeah, I don't
[24:36] currently have it. Download chatbt.
[24:41] I don't remember if I can use the
[24:44] the app with just a free chat GBT
[24:47] account or not, but we'll try it out.
[24:58] Okay.
[25:02] She got DBT.
[25:10] All right. [clears throat] And then
[25:16] downloading.
[25:22] Almost there.
[25:24] So then it says find the documentation.
[25:28] Select open in chaptt.
[25:31] Okay,
[25:35] I'm still transferring it.
[25:40] And let's also remember we had that
[25:42] pizza MCP. There we go. The pizza maker.
[25:45] That was the one we tried before because
[25:47] this one has um MCP tools on it, right?
[25:52] So, we had the application WebMCP. Yeah.
[25:56] So these are when we open up the
[25:59] inspector, we can see
[26:02] all the tools that are exposed on this
[26:05] website via WebMCP. So the bare minimum
[26:08] I was thinking of just adding WebMP to
[26:10] my personal website just so I have
[26:11] something, [laughter]
[26:12] you know, to demo it. It feel a little
[26:14] silly because my personal website is so
[26:16] simple. Um but, you know, it it it would
[26:20] make some things a little more efficient
[26:21] because sometimes I do have agents parse
[26:23] my website for stuff. All right. So,
[26:26] let's see if we got it. Did it transfer
[26:28] it over yet? Uh, let's try chatgbt.
[26:34] Okay.
[26:37] Open.
[26:40] Uhhuh. [clears throat]
[26:44] Chat dbt.
[26:47] Okay. It's opening over here. Let me get
[26:49] it. All right. Continue to log in.
[26:57] Uh, okay. Continue.
[27:02] All right. Open. Allow.
[27:06] Whatever I disallowed.
[27:09] Okay.
[27:11] Uh, what best disguise my work? Who
[27:13] knows? Engineering. Okay.
[27:18] Blah blah blah. Skip. Go to chatbt. All
[27:21] right. Import work. Nope. Nope.
[27:25] Skip.
[27:28] All right, let's open here. Uh, let's
[27:31] say
[27:36] open this website. What tools does it
[27:39] have? Let's just try this and see.
[27:44] I'm using the inapp browser skill to
[27:46] inspect the site's expose web MCU tools
[27:48] directly. Great. So that is kind of what
[27:52] I was hoping for. Um that's seems like
[27:56] it immediately understood about because
[27:58] I didn't even say WebMTP, right? I just
[28:01] said what tools does it have? So um oh
[28:04] it says allow. Okay, so we're going to
[28:06] allow
[28:09] this is cute. It wants to record my
[28:11] computer screen and audio.
[28:14] I'm just going to deny for now because I
[28:16] don't think it's necessary. Um, okay. It
[28:18] exposes seven web MSP tools. Okay. Add
[28:22] pineapple and
[28:25] um
[28:27] add pineapple to the pizza.
[28:32] Let's see. I'll use the pages add
[28:34] topping tool to add one pineapple
[28:36] topping. Let's see if it's going to pop
[28:37] up in the browser. Reconnect to the
[28:39] pizza maker page.
[28:43] Add pineapple to the pizza.
[28:47] I want to see. Okay, it said added, but
[28:50] I the problem is I don't see the
[28:52] browser. I don't know if there's a way
[28:53] to like kind of Oh, here we go. There we
[28:55] go. It added pineapple.
[28:58] All right. So, yeah, it works. Um,
[29:01] so that's very cool. So if since chat
[29:04] GBD desktop now has you know that was
[29:07] actually the easiest because I remember
[29:08] we tried to use WebM last week and it
[29:10] was kind of painful to get agents to use
[29:11] it but that worked probably easier than
[29:13] any of the other agents we tried. Uh
[29:17] so
[29:21] I think that this is really promising
[29:24] for WebMCP that it's now working so
[29:27] well. Uh, so I think that's like way
[29:29] more motivation for for us to add WebMCP
[29:32] to websites, right? Because chat GBT is
[29:34] very consumer friendly. Uh, so yeah,
[29:37] this is really cool.
[29:40] So check that out and open the, you
[29:43] know, enter the challenge if you've got
[29:45] time, if you've got a good um, you know,
[29:49] idea for for that challenge
[29:53] and hopefully we'll have a winner.
[29:56] Let's see. I see folks are talking. Um,
[30:02] few other things from
[30:07] this week. Well, I do want to see what
[30:08] people are saying. Um, I uh
[30:13] let's see if there's anything I can talk
[30:14] about while people are talking. Okay, it
[30:16] also said you could open
[30:19] the
[30:21] the OpenAI website itself. So, let's try
[30:24] a new chat here. while people are
[30:26] chatting. Okay. How do I do I want a new
[30:28] chat. New chat. Okay. Open and tell me
[30:32] what Skype tools are available.
[30:45] This one didn't mention WebMCP, but I'm
[30:47] assuming it's going to use WebMCP
[30:52] for this one, too.
[30:55] Awaiting approval. All right. I have to
[30:57] It's weird. It pops up the approvals
[30:58] down here. I'm used to approvals being
[31:00] in a different spot. Okay. Yeah. And
[31:03] this one has five site tools, right? So,
[31:06] search docs, lookup page, blah blah
[31:08] blah. Um,
[31:11] and navigating around the website. So,
[31:15] yes, this is working. This is working
[31:18] really well.
[31:19] Okay, that was like too easy. All right.
[31:22] Um, [laughter]
[31:25] let's see. Uh, another thing I did this
[31:28] week was that a lot of times I like step
[31:31] away from my computer and you know I
[31:35] have the agent working on something that
[31:37] you know might take a long time. Um, and
[31:43] you know I want to just be able to like
[31:45] go do some laundry or something, right?
[31:48] So what I did was I added an agent hook.
[31:51] Uh so an agent hook is something you can
[31:53] have for GitHub copilot and it works
[31:55] across VS code and copilot app and
[31:59] basically you set up these hooks and say
[32:02] hey you know on this certain event
[32:04] you're going to do this thing. So I have
[32:05] a hook for stop and basically every time
[32:08] the agent stops it runs this hook right
[32:11] and what this hook does is that it plays
[32:14] a sound and this is a sound of my
[32:18] four-year-old singing. So, she goes like
[32:20] dut.
[32:22] So, every time an agent stops, I get to
[32:24] hear my four-year-old singing. And it's
[32:27] actually very cute. Uh, and then it also
[32:29] checks to see if my computer's currently
[32:31] idle. And if it's been idle for more
[32:34] than 60 seconds, uh, meaning that
[32:37] there's no mouse or keyboard activity,
[32:39] then it will look at the title of the
[32:41] conversation. So, in this case, like you
[32:43] know, the title is this thing up here on
[32:44] the conversation. And then it uses say
[32:47] in order to say the the title, right?
[32:51] And says so that way if I've walked away
[32:53] and I'm like doing dishes or whatever,
[32:55] I'll hear duh and then, you know, plan
[32:59] MD is finished, right? So then I can
[33:01] think, oh, okay, do I want to go back to
[33:03] the computer? Um, and you know, keep
[33:06] working on this thing. So, this is how
[33:08] I'm trying to be able to, you know, have
[33:10] agents uh delegate to a agents but still
[33:13] keep myself busy at the same time in a
[33:16] way that like I feel productive um while
[33:19] it's doing something because I don't
[33:20] want to just sit there and you know
[33:23] browse social media or YouTube shorts or
[33:25] whatever while it's working. Uh so, uh
[33:29] yeah, so I do this instead. Another
[33:30] thing you can do is actually like you
[33:32] can use an LLM to summarize to like say
[33:35] the last message or to summarize the
[33:37] last message. I was talking to somebody
[33:38] last week that that's what they do is
[33:40] they have a local LLM like a a local
[33:43] Quen model that looks at the most recent
[33:45] message and then gives a summary of that
[33:46] message because that's the kind of thing
[33:48] that a local LM could do. So that would
[33:50] be another approach. Um and that you
[33:52] know that's could be a useful thing as
[33:54] well.
[33:57] Uh so oh let me share this this agent
[34:01] hook. Uh but there's lots of different
[34:03] hooks you could do. Um
[34:07] uh there's a great post from Nakasa's
[34:10] about agent hooks and how he uses it and
[34:12] he uses it for doing enforcing linting
[34:16] um for uh when he's you know working on
[34:18] files just making sure that it's always
[34:21] you know running a particular interlin.
[34:22] So his is much more fancy with checking
[34:24] on like tools and what tools have run
[34:26] and stuff like that. Uh so there's quite
[34:28] a few ways that you can use agent hooks
[34:30] to, you know, customize what your agents
[34:33] are doing.
[34:37] Uh Bernard researched elephant
[34:39] communication. They've got many
[34:43] different ways of communicating.
[34:45] Acoustic, seismic, is that like stomping
[34:48] on the ground because they're so heavy.
[34:49] tactile, chemical, and visual. Yeah. I
[34:53] mean, that's an interesting thing is
[34:55] just the different ways of
[34:56] communication, right? Like the other um
[34:59] thing they were talking about was ants.
[35:01] Like ants have ganglia at like every
[35:03] joint in their body. So ants like, you
[35:06] know, have kind of multiple like mini
[35:08] brains within their body. And of course,
[35:09] ants themselves become this super
[35:11] organism. So when I kill an ant, I
[35:14] actually don't feel that bad because I
[35:15] think I'm just killing one brain cell in
[35:17] a super oranism. That's my
[35:18] justification. Um, but they have like,
[35:21] you know, so, oh, and then I was also
[35:23] reading, my gosh, have you read Sorry, I
[35:26] this is I'll I'll I'll focus again, but
[35:29] Portuguese manow
[35:31] is a made up. It's a colonial organism.
[35:36] And so, a single man of war, this thing
[35:39] here, is actually
[35:42] um multiple organisms, but they're
[35:45] genetically identical, but they look
[35:46] completely different, right? is as if
[35:48] each of them decided to become a
[35:49] different part of it. So like I mean
[35:51] when you like when you look into nature
[35:55] you realize that like we really try to
[35:58] oversimplify all the time all the things
[36:00] because we're like oh humans are like a
[36:02] single you know each each human is a
[36:04] single human and we're one organism blah
[36:06] blah but like things are not that
[36:08] simple. Anyway, uh I'll get I'll focus.
[36:12] Let me focus back to AI.
[36:15] [laughter]
[36:17] Let's see what else. Um
[36:24] uh let's see. I did go to this meetup
[36:28] last week uh which was very cool about
[36:32] DSpy. I don't know if any of you are
[36:34] using DSpy. Um, DSpy is a Python
[36:38] framework where it takes a very
[36:41] different approach to LMS. Instead of
[36:43] like, you know, you maintaining your
[36:46] prompts, instead you maintain your your
[36:48] signature and you compile the prompt,
[36:52] right? So your prompt becomes like this
[36:53] built artifact and the thing you know
[36:56] that you're changing is just the input
[36:59] output signature. Um, so there's a great
[37:02] meetup about that. uh last week
[37:07] um where people were sharing different
[37:09] things, right? So there was like
[37:10] dspy.flex which instead of just
[37:12] optimizing the prompts, it actually
[37:14] optimizes your entire Python module. So
[37:17] it'll write your full code for you,
[37:19] right? Um so there your artifact
[37:22] actually becomes the module.
[37:24] And that probably feels a bit funny to
[37:28] to have that be the artifact, but um
[37:31] basically like an experiment he showed
[37:33] the he was like rewarding like you know
[37:36] reducing LLM calls and so it came up
[37:38] with a program that used like regular
[37:41] expressions for a lot of the checks and
[37:44] only would use an LLM when it really
[37:45] needed it. Um and so there like he got
[37:49] like higher accuracy but less LLM usage
[37:52] right because of that. So that's really
[37:55] interesting and that you know is another
[37:57] approach to
[37:59] um you know to working with LLMs and uh
[38:03] yeah I I haven't been able to use DSpy a
[38:06] lot in my own stuff uh but I think it's
[38:08] really fascinating. uh it uses something
[38:10] called JEPA which is uh genetic parto
[38:13] algorithms in order to find candidates
[38:16] to decide like oh what's the next thing
[38:18] like what's the next prompt we're going
[38:19] to explore what's the next Python module
[38:22] uh we're going to explore um and they
[38:25] you know worked on paralyzing that so
[38:26] you can do it more efficiently uh here's
[38:29] something exciting if any of you use
[38:30] light LLM light LLM is you know an LLM
[38:33] agnostic layer but it has definitely
[38:36] some issues it has security issues it
[38:38] got famously breached this year. It also
[38:40] just is generally like too heavyweight
[38:43] and um it's not really modernized. So
[38:46] they are working on this thing called
[38:48] LM15 and they're making versions of it
[38:51] in Python, Rus, Go, and Typescript and
[38:54] basically they're trying to make a
[38:56] low-level LM agnostic library. They've
[38:59] got support for responses and chat
[39:00] completions already. I told them I want
[39:02] to check it with Azure, but apparently
[39:04] they have been actually testing it with
[39:06] a Azure at least with the Azure key
[39:08] version. Um, so yeah, so that I think is
[39:13] really exciting because I know a lot of
[39:15] us are using light LLM. Uh, so I would
[39:19] consider it LM15
[39:21] because there's a lot of practices in
[39:23] the light LLM codebase that I'm not
[39:25] comfortable with.
[39:27] Um
[39:29] so yeah so that was that was a cool
[39:32] thing to look into. Okay. All right. I
[39:35] saw there were some questions. So
[39:36] Krishna
[39:38] said um okay. So Krishna says
[39:42] a question about implementing an MP
[39:45] server. Let's say you have three API
[39:46] endpoints that need to give access to a
[39:48] voice AI agent to make a decision for
[39:50] the user.
[39:52] If the endpoint access is agent from
[39:54] agnostic, what is the best way to
[39:56] implement it?
[39:59] Um, so the voice AI agent is making
[40:04] a decision
[40:06] for the user. Well, then yeah, if you're
[40:09] trying to make it be generally if you're
[40:11] trying to make endpoint access be agent
[40:12] framework agnostic, then that's usually
[40:15] why you're going to go to MCP, right?
[40:17] because typically all the agent
[40:19] frameworks have built-in support for
[40:21] MCP.
[40:23] Um so you know once you know you want
[40:25] that portability uh then you know you
[40:28] can expose it MCP server. So I guess the
[40:31] other question is like you know is there
[40:33] a reason why you don't want to use MCP
[40:35] or something else you're considering? Uh
[40:38] you said different frameworks send
[40:39] params to the endpoints in different
[40:41] ways.
[40:43] uh the best way to implement the
[40:44] parameter access from request no matter
[40:46] the agent framework it receives. Well,
[40:48] if you're doing if you're exposing
[40:49] things as an MCP server, then that's
[40:52] going to constrain how they send stuff
[40:55] endpoint. But of course, yeah, there is
[40:56] going to be differences in arguments
[40:58] like I did my
[41:00] um
[41:03] uh talk about evaluating upspevers.
[41:11] Um
[41:13] I
[41:14] oh this one improving
[41:17] improving MP tool schemers to increase
[41:20] agent relability. This one
[41:25] uh find the blog. Okay this all right
[41:27] here's the blog about it. Okay so here I
[41:29] did measure right I made the MCP server
[41:32] and I did check them across
[41:34] uh different agent frameworks. That was
[41:36] one of my evaluations.
[41:39] Um and uh I I generally things did
[41:43] pretty well across the frameworks. Um
[41:48] uh you know so I matched things like
[41:50] okay did it call the tool? Yes it called
[41:52] the right tool. Did it call it with the
[41:54] right parameter?
[41:55] You know they were pretty similar in
[41:58] that um same thing here. So you know I
[42:02] would say you write your MSP server you
[42:05] write the tools you run some evaluations
[42:07] across the two different frameworks and
[42:09] then you also often are looking at the
[42:10] models right like do you know which
[42:12] models are going to be used because
[42:13] that's where we see a huge variation
[42:16] right um you know this is back when
[42:18] we're doing like 404153
[42:20] and just really big variation and then
[42:23] also looked on like reasoning effort
[42:25] like big variation there so I actually
[42:27] saw a lot more variation across models
[42:30] in reasoning effort than I did across
[42:33] agent frameworks. Um but there was some
[42:35] variation across the agent frameworks.
[42:38] Uh so it's you know you you know ideally
[42:42] you're you're running those evaluations
[42:45] and um you know it's not not too hard to
[42:49] set up evals like uh I just had co-pilot
[42:53] write up a custom eval framework. this
[42:55] is said hey this is what I want to
[42:56] evaluate you know set up the evals for
[42:59] me and um you know and it just does it
[43:02] uh you know it's
[43:04] uh I find that these coding agents are
[43:07] quite good at writing evals for
[43:09] themselves
[43:11] um but you can you know you can use
[43:12] frameworks too so um yeah I would say
[43:15] you know do MCP set up your schema start
[43:17] with your best guess and then do some
[43:21] eval with the sorts of models and agent
[43:24] frameworks you expect and see what kind
[43:26] of variation you're seeing and where you
[43:30] need to improve you know make things
[43:33] more clear in your uh in your MCP tools
[43:38] and schemas whether you need to have
[43:40] split into different tools whatever
[43:43] uh the question was is eval built using
[43:45] Azure AI evaluation no in this case uh
[43:49] literally it you know it just vibe coded
[43:52] an eval framework um So I actually told
[43:55] it to use pleantic AI evals and I
[43:58] thought it was using that uh but then I
[44:01] realized the day before the talk that it
[44:02] just wrote its own eval framework right
[44:04] because you know really for eval um
[44:07] especially with something like this like
[44:09] here we're really checking like we know
[44:12] like I didn't really have to use LLM as
[44:13] evals for this right most of the times I
[44:15] was just checking for exact um exact uh
[44:20] matches right so for this one right uh
[44:24] you So there's the prompt. Uh this is
[44:27] like for an expense tracking thing,
[44:28] right? Here's the category we expect.
[44:30] Here's the date we expect. Here's the
[44:32] amount we expect. Right? So when you're
[44:35] evaluating MCP servers, a lot of times
[44:39] you just know exactly what you want it
[44:41] to pass in. So you often don't even need
[44:45] to have the an LLM evaluation. you can
[44:48] add LML evaluation if there's some free
[44:51] text uh parameter that you want to you
[44:54] know evaluate how well it did with that.
[44:56] Um but you you don't it it just depends,
[44:59] right? So yeah, so I just had it write
[45:02] its own it just wrote its own eval
[45:04] framework. Um and then like it wrote its
[45:06] own uh reports. Uh wait, here's like the
[45:10] runs. So for each of the runs, we would
[45:13] have a JSON, right? And then I was like,
[45:16] "Oh man, this JSON is crazy to look at.
[45:18] Can you make a markdown file?" So it
[45:20] would make the markdown file. And then a
[45:22] lot of times I wouldn't even necessarily
[45:24] look at this. I would just say hey tell
[45:26] me like look at these runs and tell me
[45:29] what was significant between them. So um
[45:32] you know generally I think that coding
[45:35] agents make it much easier to work with
[45:37] evaluations because it can kind of like
[45:39] look through all of them like you just
[45:41] need to be you know recording as much as
[45:43] you can right record everything you can
[45:46] so that it can look through right so
[45:48] here you can see there's a lot of
[45:49] information here so I record as much as
[45:51] I can like reasoning if there's
[45:53] reasoning tool calls so as long as you
[45:56] record as much as you can then if the
[46:00] data is there you can ask the coding
[46:01] agent hey you know compare this one you
[46:04] know compare these two runs and tell me
[46:06] what's significant between them right
[46:08] and sometimes it'll write a script to
[46:10] compare them sometimes it'll just store
[46:12] them like load them into memory uh but
[46:15] it's like really really helpful for
[46:18] sorting through all this data because
[46:19] when you do evals you get so much data
[46:21] so I would say do it get all that data
[46:24] and then just point a you know point a
[46:27] good model at it and say hey help me
[46:29] sort through this data Right. And you do
[46:31] need to I mean this is like with the
[46:33] data science you do need to like you
[46:35] know keep a critical eye and be like
[46:37] pushing back like if anything seems
[46:39] surprising uh like when I first did the
[46:42] runs between Pantic AI and CO cop SDK
[46:45] copot
[46:46] like uh for this one with the date match
[46:50] it got like zero out of 17 and that was
[46:54] because I was running it at a time of
[46:57] day where my date wasn't the same as UTC
[47:01] and I think the copilot SDK like has
[47:03] like the time baked into UTC. Uh which I
[47:07] think it what like is a bit of an issue
[47:09] but um you know like I was like okay why
[47:11] did that happen? Let's run it like let's
[47:13] dive into it and so I you know reran at
[47:15] different times a day and got different
[47:16] results. So you want to keep a critical
[47:18] eye and you want to be like working with
[47:20] the LM and pushing back and saying hey
[47:22] like let's really dig into it. Why was
[47:24] there difference? Right? If you ever see
[47:25] a difference between things, you really
[47:26] really want to dig into it. But I think
[47:28] if you record as much information as
[47:30] possible, then you know you can dig into
[47:34] it and find out what the issue is.
[47:38] Um Nomi asks, "Is copilot agent
[47:40] framework different from Microsoft agent
[47:42] framework?" Yeah, so the copilot SDK
[47:43] means that you are using the harness
[47:46] that is underlying the GitHub copilot
[47:49] app and the copilot CLI, right? And soon
[47:53] BS code as well. although I'll be using
[47:54] the same harness and one of the news
[47:57] this week is that the copot cli has been
[48:00] rewritten in rust uh so it should be
[48:05] uh faster right copi cli runs on native
[48:08] rust
[48:09] um so yeah so with the SDK
[48:13] that's a uh it's available multiple
[48:15] languages but in this case I was using
[48:16] the python SDK in order to you know
[48:20] access that that harness so that's in
[48:23] here, right? So, you can see I've got an
[48:25] agent framework agent and I have a
[48:26] copilot SDK agent. So, here I'm like
[48:29] implementing the copilot client or um
[48:32] you know integrating it and then calling
[48:34] it. So, it's being able to
[48:35] programmatically run the same kind of
[48:38] sessions. Oh, this is chat GBT
[48:41] >> [clears throat]
[48:41] >> uh the same kind of sessions that were
[48:42] running in the copilot app or the CLI.
[48:46] And uh you can integrate it with agent
[48:49] framework. So if you want you can kind
[48:50] of use agent framework as kind of the
[48:53] higher level thing and then use co-pilot
[48:55] as your agent inside the agent framework
[48:58] like if you wanted to build workflows
[49:00] that use the copilot SDK so there is
[49:02] like an agent framework copilot package
[49:05] they do have overlap but in this case I
[49:08] was just doing it separate which is like
[49:10] let's make a agent framework agent let's
[49:11] make a copilot agent let's make a
[49:13] pedantic let's make a lang chain right
[49:14] like um just so I could compare the
[49:18] agent harness harnesses, right? So,
[49:19] these are basically different harnesses
[49:21] because, you know, they have slightly
[49:23] different underlying system prompts and
[49:24] ways of managing tool calls. Uh, so I
[49:28] wanted to see, you know, did how much
[49:30] did the harness matter? And the only
[49:31] thing that really mattered was the fact
[49:33] that the Copart SDK seemed to have a
[49:36] date time as part of its underlying
[49:38] system prompt at the time. I think it's
[49:40] changed now. Um so yeah so here I'm
[49:43] really comparisoning comparing the
[49:45] differences in how they manage their
[49:48] tool calling and if there's any you know
[49:50] underlying system prompt that they're
[49:52] adding
[49:54] in copilot ID can you do sub agents
[49:56] parallel sequential looping agents uh
[49:59] you know I haven't messed with the SDK a
[50:00] lot but I would say probably given that
[50:03] um you have that you know if you can do
[50:06] it in the co-pilot app then you know you
[50:10] can probably do it in the SDK. So, um
[50:15] you know, you can see, let's see,
[50:16] there's like lots of samples. Oh, we
[50:19] should have more samples in that. Uh
[50:21] here's the Copot SDK. Um let's see if
[50:24] they mention like sub aent.
[50:27] Okay, they don't specifically mention
[50:29] sub agent. Um but there's quite a few
[50:35] features here. So, um, yeah, generally I
[50:40] would say like if you can do it in the
[50:42] CLI or or the the app, then I would
[50:45] assume you could do it with the agent as
[50:47] well.
[50:51] All right, Bernard says, "Today is the
[50:52] release date for 3:15." Oh my gosh. I
[50:55] was just thinking today because I was
[50:56] looking at working on some um
[51:00] some things and I you know that had like
[51:02] Python 312 and I'm like gosh 312 is
[51:05] probably old news, isn't it? So here um
[51:09] what is the 312 is a security in
[51:12] security mode. 39 is end of life.
[51:15] Hopefully you're all off 39. 310 is
[51:17] getting close. Oh 39 310 is almost end
[51:20] of life because of course yeah October
[51:22] is normally when we do like release
[51:23] party, right?
[51:25] So 3:15
[51:29] we should have a release party soon.
[51:31] Pre-release right now. Very exciting.
[51:34] All right. Okay. And yes, we are at time
[51:38] now. Uh so thank you everybody for
[51:40] joining. Super fun as always.
[51:44] Um
[51:46] uh I'll I'll post every uh the recording
[51:50] tonight in the um in the office hours
[51:54] thread. Uh I think I can hold office
[51:57] hours next week. I'll be in Redmond, but
[51:59] I think I can still hold it. Uh and
[52:02] we'll have MCP live on Wednesday. So
[52:05] that'll be on YouTube. So hopefully you
[52:07] will join us for MCP live.
[52:11] Uh so register for that if you haven't
[52:14] yet.
[52:16] Yes. All right.
[52:19] Thank you everyone.
[52:22] See you next time. Bye.
