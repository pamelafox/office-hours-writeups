[00:00] Welcome everyone to our weekly Python
[00:03] plus AI office hours. It is April 13th
[00:09] and hope you all are doing well. It's a
[00:13] lovely spring day here.
[00:16] The Bay Area has very funny weather. All
[00:19] right, so as usual um I'll you know
[00:22] start off with news that has happened in
[00:25] the last week. uh just sharing that uh
[00:28] for you know if you have any questions
[00:30] related to the news or just things we
[00:32] want to try out. Um but if you have any
[00:35] questions about what I'm showing about
[00:37] anything you've been working on just put
[00:40] them in the chat and I will see them in
[00:43] the chat. Um since we are recording
[00:47] uh with my StreamYard uh we only I will
[00:51] have the audio on stage. So if you do
[00:53] have any questions, just write them in
[00:55] text in the chat.
[00:57] So let's see what is going on this week.
[01:02] Now I think I feel like at this point
[01:04] you all have heard this already, but I
[01:06] did finally migrate pretty much every
[01:09] sample over to the Azure responses API.
[01:14] Um, and I use this skill to do it. Uh,
[01:17] so and it's very easy to install this
[01:19] skill. I like using MPX Skills AD to
[01:22] install all skills now. Um, but there's
[01:24] other ways you can install skills as
[01:26] well. Uh, just depending on, you know,
[01:29] what coding agent you want to use it
[01:31] for. But if you do have any repos that
[01:33] are using the chat completions API, then
[01:36] I do recommend moving over to the
[01:38] responses API. Um, and that's what we're
[01:41] trying to get everyone to do. So, at
[01:43] this point, everything is ported over,
[01:45] including our large rag sample. Um,
[01:52] and that this was quite quite a big uh
[01:55] quite a big change. Uh, but it's it's
[01:58] ported over now. And the cool thing now
[02:00] is that it should be easy for relatively
[02:03] easy for us to add on support for the
[02:05] code interpreter and the web search
[02:07] tools because those are both built into
[02:09] the Azure responses API. And so that
[02:11] means just, you know, being easily have
[02:14] easy access to both of those. And I it
[02:16] just makes everything so much more
[02:18] capable when you have access to a code
[02:20] interpreter and uh web search because I
[02:23] I use those tools constantly with the
[02:25] responses API.
[02:28] Uh so definitely try out that skill uh
[02:32] on any repos that use chat completions
[02:34] and let us know if you have any feedback
[02:37] about how we can improve it. Uh we've
[02:40] already gotten a few PRs actually.
[02:44] What else? a lot happening in the
[02:46] copilot CLI world. So this one's pretty
[02:48] fun. So the copilot CLI that's basically
[02:51] um you've got you can see I've got it
[02:53] going a bunch here. So I just used it to
[02:56] I generated these slides actually. So
[02:58] these were just generated with the
[03:00] copilot CLI. So uh you know Copilot CLI
[03:03] is um a a command line version of GitHub
[03:09] copilot uh similar to cloud code if you
[03:11] know cloud code and uh you know I use it
[03:14] just for lots of um side things I'm
[03:18] working on. Um here I was checking to
[03:20] see what tweets people liked about the
[03:22] copilot CLI. Very meta.
[03:25] Um, but it's, you know, what's really
[03:27] helpful is when you hook it up to MCP
[03:29] servers and it's got and skills and it's
[03:31] got more capabilities. Now, what's fun
[03:32] is that now there's this remote control
[03:34] for the CLI. So the idea is that what
[03:38] you do is you like start up your you
[03:40] know you've got your copilot running on
[03:42] your machine and then if you start it up
[03:45] with copilot-
[03:47] remote then
[03:50] you can then log in on your phone like
[03:53] using the GitHub mobile or the mobile
[03:56] app or the GitHub mobile website and
[03:59] then on your phone um you can you can
[04:02] just participate in the session that's
[04:04] happening on your computer. So the nice
[04:05] thing there is that your computer has
[04:07] access to your repos, right? So if you
[04:09] were, you know, working on something on
[04:12] your computer, you don't have to worry
[04:13] about how how to get your, you know, get
[04:15] it checked out on your phone. Um, you're
[04:17] just using your phone as a remote
[04:19] control
[04:21] to change what's going on on your
[04:22] computer. Uh so uh you know I know
[04:25] there's definitely some of my colleagues
[04:27] really really uh was were trying to
[04:30] figure out how to do this and they set
[04:31] up various like tunnels and stuff from
[04:33] from their phone to the machine. Uh so
[04:36] this would be the the official
[04:39] doing that.
[04:41] Uh so yeah try that out if you find that
[04:45] you often like I guess want to like go
[04:47] to the beach. The interesting thing is
[04:50] what are the scenarios for it? Maybe
[04:51] when you're on the BART, like when uh
[04:52] sorry, not Bart, the train, the train,
[04:55] the bus commuting, commuting, like you
[04:57] know, you don't want to bust out your
[04:59] whole laptop, but maybe you do want to
[05:01] do something. Uh although that case,
[05:03] your laptop probably in your bag. So,
[05:05] I'm very interested to see what are the
[05:06] actual scenarios that people are using.
[05:08] The scenario that the PM gave was like,
[05:10] oh, you go to the beach, but if I'm
[05:11] going to the beach, I'm not going to be
[05:14] working with my agent. Um
[05:16] so uh yeah so I'm interested to see um
[05:20] what snares have. So Nambdi says codeex
[05:22] has it via the chatb app and then cloud
[05:25] code also has remote. So yeah so both of
[05:27] these so all it looks like all the
[05:29] popular coding agents have this remote
[05:31] ability now. So clearly it's something
[05:33] that people want. Um I I haven't
[05:35] personally used it yet. I think it's
[05:38] probably something I would uh you know
[05:40] like need to get used to using so that I
[05:42] figure out what are the use cases where
[05:44] I really want to be controlling co-pilot
[05:48] via my phone um where that's more
[05:51] convenient than just using my laptop. So
[05:53] I'm curious if any of you are using the
[05:54] codeex or cloud code versions of remote
[05:57] like what are the situations where
[05:58] you're using it for?
[06:01] Uh but yeah, people really wanted that
[06:03] and so now it has it. Um what else? Uh
[06:07] now Copa CL CLI also has this rubber
[06:10] duck feature which will use multiple
[06:13] models to give a second opinion and they
[06:16] added that because what they saw is like
[06:17] lots of people will you know ask a
[06:21] second model for their review and so
[06:24] rubber duck is like an official feature
[06:26] to um you know to be able to get a
[06:29] second opinion from you know from
[06:31] another model.
[06:33] Uh, so, uh, I also haven't tried this
[06:36] one yet, but this sounds like a good
[06:39] thing to try. It's nice to It's always
[06:42] It's always nice to get a second
[06:43] opinion. I I am always asking Co-Pilot
[06:45] to review all my PRs, and that's
[06:48] basically having a second model. So,
[06:49] this would be basically like having a
[06:51] review earlier on in the process and
[06:54] having that review be by a different
[06:56] model, right? So, it'll just always
[06:59] choose a model different than the one
[07:01] that you're currently using.
[07:03] um so that you can
[07:07] you can get some feedback on it. Uh so
[07:10] that's nice because then you can get
[07:11] that feedback before you get to the PR
[07:13] stage, right? I get lots of feedback
[07:15] from co-pilot at the PR stage, but this
[07:16] way you can get that feedback earlier if
[07:18] you're doing something larger.
[07:23] Uh so Nambdi says codeex is limited to
[07:25] the cloud and you need to attach GitHub
[07:27] repos. You might use it when you're out
[07:29] at events to run tests and debug.
[07:32] Okay. Yeah, I could see that being at
[07:33] events, you may not want to bring out
[07:34] your whole laptop. Um,
[07:37] yeah, I think it's see maybe it'd be I
[07:40] don't know if you'd want to use it when
[07:40] you're on call maybe, but you'd have to
[07:43] really make sure it was all set up
[07:45] really well for that. Um, okay. I see
[07:48] there's a question about work IQ and I
[07:50] am using
[07:53] um work IQ. So, I've got work IQ set up
[07:56] in my MCP
[07:58] config. Um, so,
[08:02] uh, the only problem is that I also have
[08:04] some tokens in there. So, let me move
[08:05] this off screen and just get the tokens
[08:08] out of the way. Uh, so you can just see
[08:11] the work IQ part. One sec.
[08:15] How can I get Okay, tokens. Okay, great.
[08:18] All right. So, here we go. Um, I'm
[08:22] trying not to show Can I do it? Trying
[08:26] not to show
[08:28] what's higher up in there.
[08:31] Here we go. Okay. So, this is in my
[08:34] copilotmcpconfig.json.
[08:39] So, this is how I added the work IQ
[08:40] server. Um, so right now it's basically
[08:42] what we call a standard input output
[08:44] server. So, it's actually running a
[08:46] command. So, sometimes I also like I was
[08:48] doing I was just using the let's see
[08:50] these are all copilot. I was using work
[08:52] IQ a bunch just via the the um because
[08:55] here's the thing is like my my um teams
[09:00] was being really buggy my team's chats
[09:02] and it felt like I wasn't seeing a lot
[09:04] of chats so I was actually using work IQ
[09:06] and being like hey like what chats do
[09:08] you actually see from me so there's two
[09:10] ways to invoke work IQ you can say work
[09:12] IQ ask so when you actually have it
[09:14] installed like okay um you know what
[09:17] meetings do I have today right so you
[09:20] can just chat with it because work IQ
[09:22] work IQ is basically it's an agent it's
[09:25] like a rag agent that has access to your
[09:28] you know teams your office etc right
[09:33] uh so now it's going out and it's
[09:36] running some calls and it'll it'll
[09:39] stream back and answer so that's one way
[09:41] of working with it the other way is that
[09:42] you're invoking it as an MCP um server
[09:47] right so here uh so here it queried my
[09:51] calendar and found all my events. Right?
[09:54] So, you don't even have to this here's
[09:56] the thing is work IQ itself is an agent.
[10:00] It h it it's doing rag um you know it's
[10:03] or it's I say it's using tools to get
[10:05] context and answer questions based off
[10:07] tools. Um but you can also use work IQ
[10:11] via another agent, right? So that's what
[10:13] I'm often doing and you can see it's
[10:14] actually being used in a bunch of these
[10:16] files, right? Um so where was I? Let's
[10:19] see. So like this one when I was making
[10:21] the deck for today um it was searching
[10:25] let's see where did it do okay so it did
[10:28] ask work IQ so there's this tool in work
[10:31] IQ so called ask work IQ and um here I
[10:35] said find emails chats and messages
[10:37] right so in this case that's the query
[10:39] that it sent to work IQ and then work IQ
[10:43] responded right um so that's how it
[10:46] would get used as an MC MCP server. I
[10:50] think I did. Uh so wait, this one was
[10:53] just using the Twitter MCP server. Um
[10:57] uh but uh here if I do recap my week. So
[11:01] this is another this is I've been making
[11:02] lots of skills this week. So um recap my
[11:06] week
[11:08] will go and it'll use the work IQ MCP
[11:11] server, the Twitter MCP server, and the
[11:13] GitHub MCP server. Um oop sorry I there
[11:16] we go. Uh, recap recap my week. Here we
[11:21] go. All right. So, this is recap my
[11:24] week. Here's the skill. So, you can
[11:26] install this myself. Uh, not yourself.
[11:29] Sorry. Um, and this uses these three MCP
[11:33] servers if you have them installed.
[11:38] So, here's Work IQ. So, here's the
[11:40] instructions on
[11:42] installing it. Um it is it is beta. It's
[11:47] still being worked on. It's you know
[11:49] it's not perfect. Um still working on
[11:52] like more comprehensive retrieval. Uh
[11:55] but you can see here like I you know in
[11:57] my skill I actually explicitly say like
[11:58] okay to get work activity you're going
[12:00] to use the tool to ask these questions
[12:02] right. So, um you actually see now if I
[12:05] go to my uh pilot CLI, it it you know it
[12:09] goes and sends off those three
[12:10] questions, right? And um gets back the
[12:14] answers for it. Uh now it's going to my
[12:16] Twitter. Okay. Yes. Yes. Yes. Yes. Yes.
[12:19] Yes. Uh so yeah. So that's work IQ. Um,
[12:22] so it works well for stuff like this
[12:25] where um, so I use this like uh to be
[12:28] able to report to my manager what I'm
[12:30] doing also because we do kind of like a
[12:32] teamwide weekly rollup. So it's it's
[12:34] it's helpful for that. It's helpful for
[12:37] um, you know, generating these slides
[12:38] because it can look through my emails
[12:40] and find all I get so many newsletters
[12:42] every week. So I can look through all
[12:44] the the newsletters and roundups and say
[12:46] like, "Oh, okay. This is what we saw
[12:48] here." Um, so I like it for that. What I
[12:51] would say it's not good for is if you
[12:52] need really really um
[12:56] this looks like a bug. Uh if you need
[12:59] really really comprehensive retrieval,
[13:01] right? So for example, I was trying to
[13:02] get it to get every single chat that I
[13:05] had with a particular person uh you know
[13:08] over the last four days and I wanted it
[13:10] like in strict order and timestamped and
[13:13] everything right and it it's not as good
[13:16] for that because it's it's not designed
[13:18] for like these highly structured queries
[13:20] and for necessarily doing comprehensive
[13:22] retrieval. I'm hoping it'll like get um
[13:26] better at that. It's doing some weird
[13:30] stuff there. Okay. Uh but yeah, there's
[13:32] definitely lots of things it does work
[13:33] well for. Um ex just like really just in
[13:36] terms of like personal productivity
[13:38] management. I think that works well.
[13:42] Uh so yeah. So let me know if you have
[13:45] other questions
[13:48] about that.
[13:52] Black Panda Chan said you you made
[13:54] mistake of helping your copilot studio
[13:55] team and you were tired of main topics
[13:57] and adaptive cards. I still haven't done
[13:59] that which means I'm I can't answer
[14:02] questions about Copilot Studio. I'm I'm
[14:05] currently working on Foundry Hosted
[14:07] agents so that we're able to show that
[14:09] for our upcoming series. So um that's so
[14:12] this week I've been working on MCP and
[14:15] Foundry hosted agents and uh because we
[14:18] have upcoming talks about both of those.
[14:19] So, um, yeah, so I was playing around
[14:22] with some new features in MCP like MCP
[14:25] apps and form based elicitations, which
[14:27] are cool. Uh, and I'm working on Foundry
[14:30] hosted agents, being able to host your
[14:33] agent framework agents and link chain
[14:35] agents on Foundry and run evaluations
[14:37] and all that good stuff.
[14:40] Uh, let's see what else. There's the
[14:42] agent customizations window. Uh, so
[14:44] that's if you go to Here we go. It's
[14:47] just this. So when you click if at least
[14:49] when you're in insiders I think this is
[14:50] in stables now you click this gear icon
[14:53] and what's nice it'll show you all your
[14:56] customizations both for the work the the
[14:58] user the workspace and the repo. So this
[15:00] is nice because sometimes you kind of
[15:01] lose track of like everything that you
[15:04] have built in to customize your coding
[15:06] agent here. So you can see like okay
[15:08] I've got my comedy roast skill my review
[15:11] PR comment skill um uh we've got some
[15:15] workspace level skills right so we can
[15:17] see our skills we can see custom agents
[15:19] uh some of them come from extensions
[15:21] some come from my workspace some are
[15:23] builtin uh instructions as well uh uh
[15:28] prompts so this is just really helpful
[15:31] because you know we're bringing in
[15:33] customizations from so many places I
[15:34] should really add a hook a hook would be
[15:36] And I want it just to make a sound when
[15:38] I something's done, right? So that I can
[15:40] come back from the kitchen from washing
[15:41] dishes. Uh MCP servers
[15:45] and plugins, uh which is really like a
[15:47] bundle of customizations. Uh so yeah, so
[15:50] if you're wondering like, hey, what what
[15:52] does my coding agent have access to
[15:54] right now? Then just, you know, click
[15:57] this icon and you can go through and
[16:00] see, you know, all the ways that your
[16:02] agent is being customized, right?
[16:06] um and see if there's anything missing
[16:08] or something you want to improve. Uh so
[16:10] here is let's see this is a video about
[16:14] that feature. And then also my colleague
[16:17] Gwen did a series
[16:20] about agent first development with VS
[16:23] Code and really just stepping through it
[16:25] um one by one and uh she probably used
[16:30] it looks like she used Python for it
[16:32] which is cool. So, you know, given we're
[16:35] in the Python series, that's an
[16:36] appropriate series for for us, uh,
[16:39] because Gwen's on the Python team.
[16:42] Uh, so check that out. Let's see. So,
[16:45] that's our news on our side. Uh, let's
[16:49] see. On the industry side, stuff that I
[16:52] found was interesting. Um, was a new
[16:55] there's a new benchmark. There's always
[16:56] new benchmarks all the time. Oh, let's
[16:58] find it. So, that was not the right
[17:00] link. I think my my skill needs to work
[17:03] on finding better links. I think
[17:05] sometimes it makes it up. I just told it
[17:08] actually to improve that part. So, it
[17:09] should be better next time. All right.
[17:11] So, here is Parsbench. This is from
[17:13] Llama Index, which um you may know that
[17:17] they were kind of the first to do a lot
[17:18] in the Rag space and set up all this a
[17:22] lot of functionality specific for for
[17:24] Rag. Um so parse bench is a benchmark to
[17:31] to you know just establish whether you a
[17:34] document parser is is good and so it's
[17:37] got tables visual grounding charts
[17:39] semantic formatting. Uh so I think this
[17:41] is nice because we always get asked like
[17:43] hey you know data ingestion like how do
[17:45] you know what the best thing is right so
[17:46] here now of course what you'll see is
[17:50] that they're saying uh you know llama
[17:52] parse is the best uh the best uh parser
[17:56] but I don't think that they didn't
[17:58] actually test Azure docu oh oh here it
[18:00] is oh okay so well they claimed that
[18:03] Azure document intelligence is only
[18:04] getting a 59.6 six. I don't know if they
[18:07] tried the new Azure content
[18:08] understanding. So, that would be good to
[18:10] test out um and see
[18:15] uh
[18:19] but uh but yeah, I I sent it to our team
[18:22] so maybe it's something that we can test
[18:23] with our as your content understanding
[18:26] and see how it does.
[18:28] Um, other stuff I thought was cool is
[18:30] that I went to this um, DS PI meetup.
[18:35] DSPI
[18:36] is this project from Stanford. So, it
[18:41] kind of came out of the the
[18:43] U academic community. Um, but it's it's
[18:47] a way of writing your AIdriven programs
[18:50] in a way that they can be improved
[18:52] easily and optimized and you can
[18:54] actually like easily use like genetic
[18:56] algorithms to optimize them. And I just
[18:58] thought it was really interesting all
[19:00] the talks that were uh at that
[19:02] conference. So for example
[19:05] um there was this talk oh let me get the
[19:08] link.
[19:13] This was uh
[19:20] Oh,
[19:26] let me actually if you just look at the
[19:28] channel, you can see a bunch of
[19:31] um
[19:33] various talks about DSPI.
[19:37] So I thought that was quite interesting
[19:38] about a different approach to optimizing
[19:40] your applications. Uh yes. So Sylvester
[19:43] posted yeah we did have a few
[19:48] um
[19:50] podcast this was this was a podcast
[19:53] which was very which was done very was
[19:56] very fancy production high high
[19:57] production quality um and where we
[20:01] talked about a few things. Um, it it's I
[20:05] think it like some people said it wasn't
[20:07] there was a comment that it you know it
[20:08] wasn't like technical enough. Like I
[20:10] think this podcast was kind of trying to
[20:12] like both be for technical people and
[20:15] nontechnical people. My friends actually
[20:16] watched it, my non-technical friends, so
[20:18] they they liked it. But if you want
[20:20] something a little more um, you know,
[20:24] specific, we also had this video
[20:26] recently. Uh, where is the video? Um
[20:32] and this one I use the rag repo for much
[20:35] demos. So if you want to see the foundry
[20:38] IQ knowledge bases um you can also watch
[20:41] this one.
[20:47] Um okay so yeah so Pablo said you read
[20:52] um about researched people starting to
[20:55] use auto research for auto automatic
[20:58] improvement of rag parameters tuning. Do
[21:00] you think that would make sense?
[21:02] Um yeah, I've talked with some
[21:04] colleagues that are playing around with
[21:05] auto research for some very exciting
[21:08] experimentations in the rag space and
[21:10] that's more but that's kind of I think
[21:12] more on the um vector search tuning like
[21:16] for example trying to find a more
[21:17] efficient vector search and see if
[21:19] there's some heruristics we could use to
[21:21] speed up vector search uh for rag
[21:24] parameters tuning for that I think um it
[21:28] might be useful to try I haven't tried
[21:30] this yet but um This this came up at
[21:33] that meetup and and this is used by DSPI
[21:36] but they made it a version that could be
[21:38] used for anything or at least they clear
[21:41] they clear um they claim this right so
[21:44] if it's if you have text parameters
[21:45] right so for the rag parameters some of
[21:48] those parameters are a lot of them are
[21:51] probably numeric like maybe you're
[21:52] thinking of the temperature um or let's
[21:55] see what else can we change with the re
[21:56] well with the you know with the new
[21:59] models the reasoning models so the
[22:00] reasoning effort the temperature like
[22:03] there but there the thing is there's so
[22:04] few parameters that I don't know that
[22:05] you necessarily need to use auto
[22:07] research depends like which parameter
[22:09] you're
[22:10] thinking of doing because really what
[22:12] you're doing is you need to run a bunch
[22:14] of evals and then see which one's better
[22:16] so to me it's just a matrix of evals but
[22:19] maybe maybe auto research would help in
[22:22] in um a better hill climbing approach
[22:25] but I think I would yeah so um I' I'd
[22:28] have to look and see how auto research
[22:30] would help via just running the matrix
[22:32] of evals for each of those parameters.
[22:34] Maybe auto research would help in
[22:36] avoiding ones that clearly um you know
[22:39] weren't worth pursuing. Um but I think
[22:41] generally what you want to do is set up
[22:42] your evals and set up the parameters and
[22:45] then for numeric ones you know you you
[22:48] try things in the region. Um, I guess
[22:51] the interesting thing is like with
[22:52] reasoning effort, if you see that medium
[22:55] is good and high is worse, does that
[22:57] definitely mean that X high is going to
[22:59] be worse than high? Or could X high
[23:02] actually be better than high? Probably
[23:05] not. So, you could probably say like,
[23:06] okay, if I see that medium is good and
[23:08] high is worse, maybe I'm not going to
[23:10] try X high at all, right? And then if I
[23:12] see medium is good and low is worse,
[23:14] maybe I'm not going to try none at all.
[23:16] That's a kind of interesting question is
[23:17] whether because you talk about like hill
[23:18] climbing like is that definitely a hill
[23:20] or is it like disparit right because I
[23:22] think the question is do you need to try
[23:24] every parameter or do you need to you
[23:26] know start with your best guess and you
[23:28] know go in each direction and then you
[23:30] can stop at a point once you start to
[23:31] see a trend. Uh so it's interesting um
[23:34] you know in the past I've like tried
[23:36] every parameter within reason. Um but
[23:40] maybe you can save on eval time by like
[23:43] you know cutting stuff out now for text
[23:45] parameters. So um this is like if you
[23:47] have uh your prompt your skills etc. So
[23:51] basically DSPI is using this they can
[23:53] use this behind the scenes uh using this
[23:56] jeep uh jeepa genetic para parareto
[23:59] which is the prompt optimizer. Um but
[24:01] this blog post here is just showing how
[24:03] you can use it for anything right. So
[24:05] they used it to optimize agent skills.
[24:08] um cloud algorithms
[24:12] um agent architecture
[24:14] uh prompt optimization
[24:16] I don't know they have like a lot of a
[24:19] lot of um
[24:22] examples here uh so haven't tried it yet
[24:26] I fantasize about having the time to try
[24:28] it yet try it because it just seems
[24:30] really really interesting um and I met
[24:33] Lakshia at the meetup and everyone was
[24:36] just super excited and and talking about
[24:39] u about this at the at the meetup. Uh so
[24:43] uh yeah maybe something like you know
[24:45] auto research eval ja optimize anything
[24:48] um you know just uh putting them all
[24:51] together. It's just a question of like
[24:52] what do you have the time to set up?
[24:53] What do you like how many evals do you
[24:55] have the time to run and what parameters
[24:58] do you think are you know worth fiddling
[25:00] with and which of those parameters would
[25:02] be a text parameter where you want to
[25:04] use something like this and which of
[25:05] them are just numeric parameters and um
[25:08] you know you you can just figure out how
[25:12] to bury them and when to stop burying
[25:14] them.
[25:18] Uh,
[25:20] let's see. Link. Um,
[25:24] oh, here's let me link DPY as well. I
[25:26] don't think I l Oh, yeah, I did. Okay,
[25:28] great. Okay. Um,
[25:32] yeah. What what else we can look at? Let
[25:34] me get a link for auto research too
[25:36] since we're talking about that. That's
[25:37] must I assume that's under Andre's
[25:39] GitHub. Yes.
[25:45] Here's auto research.
[25:47] Um
[25:56] and we another experiment modifies the
[25:58] code trains for five minutes checks
[25:59] results for scars and repeats.
[26:02] Yes. So this one's fairly specific to
[26:04] training. At least this particular repo
[26:07] is specific to training, right?
[26:12] Um
[26:20] but just looking let's see AMD. Yeah. So
[26:22] these so this repo does seem very
[26:24] specific to training but I think people
[26:26] have taken these ideas and um you know
[26:30] used it for other stuff too.
[26:35] All right. What else am I excited about?
[26:39] mythos. H kind of scared.
[26:43] I think we're supposed to be scared
[26:44] about it, right? I don't know. Somehow I
[26:46] I Yeah, I've only been reading the
[26:48] fear-mongering parts of it. Um
[26:53] uh but I've also chatted with some folks
[26:54] that that are maybe testing it out and
[26:56] the results seem good. Well, they don't
[26:58] know if they're testing it out.
[26:59] Sometimes we get asked to test models
[27:01] and we don't know what we're testing. Uh
[27:03] so yeah, I mean it like the Opus model,
[27:06] Opus 4.6 is amazing. So, um I don't know
[27:09] what the plan is for releasing Mythos. I
[27:12] I somehow haven't what is the what is
[27:15] the whole deal with Mythos? Um
[27:18] like is it going to get released? Uh is
[27:21] a highly advanced discovery and
[27:23] explained. Oh, so specifically for
[27:25] software vulnerabilities. Okay.
[27:28] Uh
[27:30] so it's it's like been fine-tuned for
[27:32] that. Okay. Microsoft. Okay. Good. So
[27:36] Microsoft's involved.
[27:39] Okay. Well, I'm glad Microsoft is
[27:41] involved because we can, you know, you
[27:44] could imagine getting it integrated into
[27:46] something like Microsoft offender or
[27:48] something like that. Um, plans for
[27:50] project last week
[27:55] will receive access to Mythos. Okay,
[27:57] good. And Microsoft also owns GitHub.
[28:02] Um, so you could imagine also
[28:05] integrating it with GitHub.
[28:10] And now I'm just going to check out
[28:11] this. Oh, this butterfly is named for
[28:13] it's so cool. Oh my gosh. Okay.
[28:17] Uh, yeah. Well, so I mean I'm glad that
[28:21] um you know that the partnership
[28:23] involves Microsoft since I think we can
[28:26] do good things with um security related
[28:29] stuff and we also and there's other
[28:30] people involved here
[28:32] um that are all yeah these all seem like
[28:35] the good partners. So uh if we're going
[28:37] to have a super powerful thing that can
[28:39] hack us um I'm glad that we're
[28:43] partnering.
[28:46] Um, I also see a claw emoji. So, we are
[28:50] working on being able to deploy OpenClaw
[28:52] on Azure. I actually did submit a talk
[28:55] about that for the AI engineer world
[28:58] fair. Um, oh, I didn't add it. I didn't
[29:02] add it there yet, but you know, the AI
[29:04] engineer world fair. There was just one
[29:05] in Europe. There's one coming up in in
[29:09] uh San Francisco. And one of the talks I
[29:11] submitted was about deploying OpenClaw
[29:13] on Azure.
[29:15] So, uh,
[29:17] in theory, we can do that. Um, I
[29:19] actually haven't even deployed it myself
[29:21] yet. My colleague gave me access to the
[29:23] repo, though. So, you know, it's a work
[29:25] in progress. Um, but for those of you
[29:27] who do want to deploy OpenCloud securely
[29:29] on Azure, we will hopefully have a way
[29:32] for you to do that.
[29:35] Uh, so Pablo says, "I heard lately that
[29:37] very few people are actually using Copi
[29:39] in the MS365 contents. What I heard is
[29:41] the answers are not good or too much
[29:43] filtered. Um, do you think that's true?
[29:45] Would it be something that can change
[29:46] without sacrificing safety? Uh, yeah.
[29:49] So, work IQ is basically as far as I
[29:51] understand it like this is basically
[29:54] co-pilot, right? So, when you chat with
[29:56] co-pilot in teams,
[29:58] um, I would I would expect to get a very
[30:01] very similar response to when I asked
[30:03] this question, right? Um, so we can I
[30:07] think we can presume that work IQ and
[30:09] MS365 copilot are um a very similar
[30:13] experience as long as you're using like
[30:15] the default copilot and not like uh a
[30:17] particular agent like researcher or like
[30:19] co-work right because those those would
[30:21] be slightly different. Um, but like you
[30:23] know if you're using your team's
[30:25] co-pilot
[30:26] um or even the co-pilot in the browser
[30:29] like if I went to this and then let's
[30:33] just try this out a work right so you
[30:35] can see work or web. So I'm going to
[30:37] click on work and then say what meetings
[30:39] do I have today?
[30:44] So I think that it's going to
[30:49] um yeah I found six events total earlier
[30:53] today happening now right so that's a
[30:55] pretty similar response so then the
[30:58] question you have is on actu right so as
[31:00] I was saying like I do think that the
[31:02] retrieval needs to be better especially
[31:04] if you are searching teams chats I think
[31:06] that searching teams chats may be one of
[31:08] the hardest problems just because of the
[31:11] way in which the very loose way in chats
[31:14] are formatted and um you know it can be
[31:17] hard to find stuff. So I think that's a
[31:19] hard retrieval problem. I think also
[31:21] generally their retrieval stack isn't
[31:23] necessarily using the like the really
[31:26] good retrieval we have for Azure AI
[31:28] search. I don't think it's using all of
[31:29] that same technology yet. So that could
[31:31] help as well. Um it, you know, works
[31:34] well for stuff like uh meetings and
[31:37] documents. Like a lot of times I do use
[31:39] it like all right find me um you know
[31:41] find presentations I've given about rag
[31:44] like I'm just trying to you know search
[31:47] through to find stuff or if you're
[31:48] trying to find presentations your
[31:49] colleagues have given about topics I've
[31:51] done that as well. Um so so yeah I agree
[31:55] that the retrieval is not optimal and I
[31:57] I've told the team that that they need
[31:58] to have better retrieval. Um, but uh I
[32:02] think I do encourage like figuring out
[32:05] where it works well and um but keeping
[32:09] in mind where it doesn't work well. Uh
[32:12] and um
[32:15] you know having it be stuff you can
[32:16] verify. For example, like I did ask it
[32:20] um to tell me like a like I asked about
[32:22] a decision we made about the rag repo,
[32:24] right? I was like, you know, did we
[32:25] decide, you know, to do there was some
[32:28] decision we had about, I think, an
[32:30] environment variable or something. So, I
[32:31] asked the co-pilot like, hey, what
[32:33] decision did we reach about that
[32:34] environment variable? Are we going to
[32:36] like, you know, use it or not? And it
[32:38] actually gave the opposite response of
[32:40] what was true, right? So, that was a
[32:42] case where it just could not understand
[32:45] the conversation well enough to
[32:47] accurately,
[32:48] you know, um, answer that, uh, in a way
[32:52] that reflected our conversation. So, um,
[32:56] yeah, I would I would hesitate against
[32:58] using it for stuff like that. Like, hey,
[32:59] what was it? What was the dec like the
[33:01] question, what was the decision that we
[33:03] reached about this topic? Like, what was
[33:05] the decision? Like, that is a hard
[33:07] question for it to answer because it has
[33:09] to really look at every single chat and
[33:13] make sure it's seen every single thing
[33:15] and understood, you know, thumbs up,
[33:17] reactions, everything, right? So, I
[33:18] would not use it for something like
[33:20] that. something like this where I'm like
[33:21] h I just need to like you know get some
[33:23] data quickly. Um and this is much
[33:26] faster. Like actually it did a very good
[33:28] job here. I actually think it is getting
[33:30] better over time too. That was that's
[33:31] the other thing I'll say like this. It
[33:33] does seem like it's getting better. So
[33:35] you know so something like this is is
[33:36] just a a helpful way of um you know
[33:39] having somebody check my data for me and
[33:42] you know I can verify I can click on one
[33:44] of these and be like yeah that's what I
[33:45] want or that's what I don't want right
[33:46] and have it go deeper.
[33:49] Uh am I in edge or copilot? Sorry, this
[33:51] here I was using um using edge uh in
[33:55] work mode. Um but that should be pretty
[33:58] similar to using see if I is my teams
[34:01] open. Um let me open my teams and get it
[34:04] to the co-pilot view without showing
[34:08] anything.
[34:11] Um
[34:13] let's see co-pilot.
[34:16] Uhhuh.
[34:18] Okay. So then we have co-pilot. But you
[34:21] see this looks pretty similar, right? We
[34:22] have work or web, right? Like okay, what
[34:25] meetings do I have today?
[34:33] Yeah, it looks it's it looks the same.
[34:36] Yeah. Um
[34:39] All right. So yeah, so you can imagine
[34:42] like basically we have like different
[34:44] interfaces, right? We could use it in
[34:45] teams. We could use it in the browser in
[34:47] the edge. We could use it from our
[34:48] command line. We could use it from our
[34:50] coding agent. Right? So um you know we
[34:54] can use it from a lot of places but
[34:55] definitely do keep in mind there are
[34:57] things it works well for things you can
[34:58] verify where you're just using it to you
[35:01] know quickly get this data and gather it
[35:03] and just being able to because it can
[35:05] more quickly do searches than you can
[35:06] right like it's faster doing lots of
[35:08] searches right like getting all those
[35:10] rag presentations like it was it was
[35:12] much faster at that than I could have
[35:14] gone um but it may not be comprehensive
[35:17] and I would not use it to to um you know
[35:21] get answers about like something like
[35:24] what product decision did we make?
[35:27] Um let's see. Pier says, "Do you think
[35:29] the deployment of open clause reflection
[35:31] that is safe to use? You're still
[35:33] confused on privacy concerns."
[35:35] Um I think yeah concerns are definitely
[35:39] um you know founded. Let me get the exp
[35:42] the um let me find the
[35:47] the description that we were doing for
[35:49] our session on open
[35:54] claw. Uh
[36:00] um
[36:07] okay.
[36:09] >> All right. So here, let me get this.
[36:14] Okay.
[36:16] Uh
[36:19] I'll just post this in the chat. All
[36:21] right. So this is what I this is what I
[36:23] submitted. Um
[36:27] and so here we would be deploying it to
[36:30] an Azure platform using containers and
[36:34] we would be doing sandboxing and um
[36:37] guard rails and that stuff, right? So,
[36:40] so I actually don't as because I haven't
[36:42] I haven't um deployed it myself. Um you
[36:45] know, I was kind of submitting this on
[36:47] behalf of my colleague. Um so I I don't
[36:51] know what like how much that openclaw
[36:53] will actually be able to do inside this
[36:55] highly sandbox environment, right?
[36:57] Because I think what a lot of people are
[36:58] doing is they're giving openclaw access
[36:59] to their iMes account and their Gmail
[37:02] and stuff like that, right? Because
[37:04] really a lot of like what makes agents
[37:06] insecure is when you give the agents
[37:08] just access to like just any you know to
[37:11] to to data to the to your accounts to
[37:13] your credentials right so it'll be
[37:15] interesting to see is that if you if
[37:17] when we set up openclaw in a sandbox
[37:19] environment
[37:20] it will be secure it'll be fully
[37:22] sandboxed but
[37:25] what can it do and I actually do not
[37:27] know the answer to that yet but I'm
[37:30] excited to at least like
[37:33] like deploy just even that version of it
[37:35] because so far I've been too afraid to
[37:37] deploy it because I also think openclaw
[37:39] it's b it's an agent it is like it's an
[37:40] agent harness it's an agent right so
[37:42] it's similar to codeex and github
[37:44] copilot right it is an agent that runs
[37:46] tools in a loop it has its own memory
[37:48] system so in some way you can just think
[37:50] of it as being another way another take
[37:53] on agents with its own particular memory
[37:55] system and its own way of doing um
[37:58] integrations
[38:00] um but that's basically you know what it
[38:01] what it is at its heart is that it's
[38:03] it's just another agent. I think why it
[38:06] went so um big is because it had all
[38:09] these built integrations, but that's
[38:10] also where the security issues come
[38:12] from. So yeah, so I don't honestly know
[38:15] um you know how capable it will be
[38:17] inside that sandbox and you know whether
[38:21] it makes sense to even use it if it's
[38:23] hobbled. But you can imagine once you
[38:25] have a sandbox, you can start to add
[38:27] things into that sandbox and say like
[38:28] okay, you have access to just this,
[38:31] right? Um and that and you know maybe
[38:34] and maybe you like openclaw enough that
[38:36] you you know that you'll want to give it
[38:38] access to that just that and and still
[38:40] find it's very capable because I think
[38:41] also openclaw is more longunning than
[38:43] other agents and that's also what people
[38:45] like it like more autonomous more
[38:46] longunning able to do deeper tasks. Um,
[38:48] so I imagine we'll set up the sandbox
[38:50] and then say like, okay, what can we
[38:51] like other tools can we give it?
[38:53] >> Oh, yeah, that's right. Bruno made like
[38:55] a net version. Um, I think Johan's been
[38:59] working on like a JavaScript version
[39:01] maybe too. Um, so
[39:05] yeah. So check out I think Bruno is he
[39:07] doing it is it only in Spanish or is he
[39:10] doing it also in
[39:15] English? Oh, this one says Oh, wait.
[39:18] This one is English. Okay. All right.
[39:21] You're just linking to the Yeah, the the
[39:23] um It's cuz your reactor is in Spanish.
[39:27] Uh cuz both of them speak different
[39:29] languages, too. And Okay. It's okay.
[39:33] Espanol.
[39:37] Let's see.
[39:40] Open claw.
[39:45] Okay. Yeah. Yeah. So, here it is in
[39:46] Espanol. Okay. Is it also in
[39:52] Portuguese or
[39:56] sometimes Pablo does
[39:59] Portuguese?
[40:01] Uh, no. This is Spanish. Okay. Okay. So,
[40:05] cool. Yeah. Just search Reactor for Open
[40:07] Claw and you'll find a bunch of
[40:11] events. Oh, Bruno is challenging the
[40:13] Python advocates to build MS Open Claw
[40:15] Pi. Well, now now I feel like I have to
[40:18] quickly just check the repo that I got
[40:20] added to to see
[40:23] um whether it's in how it's implemented.
[40:27] Let's see. Let me just see open claw
[40:30] mark.
[40:33] All right, I'm just checking the repo
[40:36] source. Is it in Python? Well, it's not
[40:39] in Python because it's just a Docker
[40:41] file.
[40:43] Uh, so it's a Docker file. Oh, because I
[40:45] guess OpenClaw itself is written in
[40:46] JavaScript. Is that right? That's what
[40:48] it looks like. Um, yeah. So, it installs
[40:54] looks like we install
[40:57] Do we install Open Claw on the Docker
[41:00] file? Yeah. So, it's using the npm
[41:03] package. Um
[41:08] and
[41:10] let's see isolation changing a bit.
[41:16] Oh yeah. So the nice thing so it' be
[41:17] open. It'll be always on
[41:20] always connected using managed identity.
[41:24] Um
[41:30] very interesting. Very very interesting.
[41:32] Okay. Well, hopefully our talk gets
[41:35] accepted and then I'll become an
[41:36] openclaw expert.
[41:40] Nemo claw. Nemo claw is the enterprise
[41:43] rapper. All right, let's check out
[41:44] Nemoclaw.
[41:48] Oh, Nvidia. Okay. Yeah, people were
[41:50] talking about this one.
[41:55] I mostly want to do open cloud just so I
[41:57] have an excuse to like get into this
[41:58] whole lobster thing that everyone's
[42:00] doing. like all this lobster stuff. I
[42:03] told uh Pete, the guy who made open
[42:06] claw, I was like, "Listen, if you ever
[42:07] need someone to wear a lobster costume,
[42:10] I'm there."
[42:12] Um, yeah. So, that would be another
[42:15] approach, but that's not I just checked
[42:17] our repo. So, for the Microsoft one,
[42:19] we're just pulling down the node modules
[42:21] for OpenClaw.
[42:22] Uh, so if we go to like npm,
[42:25] I think they're on here. Yeah.
[42:30] I wonder what the weekly downloads
[42:34] to a million
[42:36] that millions. Yeah.
[42:41] Good times. Um,
[42:46] cool. Let's see what else.
[42:55] Okay. Okay, I don't I think we've
[42:56] covered those questions. All right, let
[42:57] me go back to slides and see. Let's see.
[43:00] I have been working a lot with MCP
[43:01] servers this week and getting
[43:02] disappointed because a lot of them are
[43:05] um a lot of them don't conform to the
[43:06] MCP spec like especially some Microsoft
[43:09] servers. So, I keep reminding people
[43:11] that, you know, you should check for
[43:13] conformance to the spec. So, if you are
[43:15] making MCP server, now here's the thing.
[43:16] If you're using an official MCP SDK like
[43:18] fast MCP or whatever, like it should
[43:20] conform to the spec. Um, but if you're
[43:22] like writing your own MCP server from
[43:26] scratch, then then you should definitely
[43:29] be checking to see if it conforms to
[43:31] spec because otherwise like people the
[43:33] whole thing about MCP is supposed to be
[43:34] portability, but if you don't conform to
[43:35] the spec, like I try to use your MCP
[43:37] server in another MCP client and boom,
[43:39] like it doesn't work, right? So I filed
[43:40] like a bunch of bugs this week with um
[43:42] Microsoft MCP servers like this doesn't
[43:44] work, doesn't work, doesn't conform to
[43:46] the spec, right? So you know MP is a
[43:49] protocol and it has certain expectations
[43:51] and so um you know you want to check and
[43:55] make sure that if you are
[43:57] um you know building SP server that it
[44:00] conforms to the spec.
[44:02] Uh let's see what else. Uh this is
[44:05] another
[44:08] skill. Um this is actually my favorite
[44:10] skill. I I posted about this. I I do use
[44:13] this all day every day and it's just a
[44:16] skill that um helps me go through
[44:19] reviews uh PR reviews or you can see I
[44:22] was just using it just this morning. So
[44:24] basically what it does um you know I
[44:27] invoke the skill and it looks to see uh
[44:30] if there's any comments both top level
[44:33] comments and inline comments summarizes
[44:35] them and then goes through them one by
[44:37] one. um these two had already fixed and
[44:39] then for each of them it'll say it's
[44:41] recommendation whether to accept or
[44:43] reject or or iterate and so then I'll
[44:46] say okay yeah sounds good or whatever
[44:48] right and then it goes through and it
[44:50] comments on my behalf which is nice and
[44:52] it try it also resolves the comments on
[44:54] my behalf and then you know commits and
[44:56] push uh so that is the only way like
[44:59] whenever I get comments on a PR I am
[45:02] always invoking the skill it's just so
[45:04] much nicer to have, you know, a a pair
[45:08] reviewer, right? That's basically what
[45:09] I'm doing is like pair reviewing, right?
[45:11] So, it's just really nice to have a pair
[45:12] reviewer to get like um a second opinion
[45:16] and um you know, it makes it it makes it
[45:20] a more collaborative experience. It
[45:22] makes coding and reviewing and iterating
[45:25] on PR less lonely.
[45:27] Am I coming to Vancouver for the web
[45:29] summit? I don't think so. What is the
[45:31] web summit? Vancouver. Well, it autocomp
[45:35] completed. May 11th to 14th.
[45:38] Uh, no.
[45:41] Who's going to be there?
[45:45] I've actually never been to Vancouver.
[45:48] I should go sometime. Maybe like Pi
[45:50] Cascades.
[45:52] Wow. Look, Brad Smith quote. He's cool.
[45:57] Oh. Oh, yeah. Yeah. Because we have like
[45:59] this PM, right? Um,
[46:02] yeah. So, that's different. Yeah. We
[46:04] there's this there's you know somebody
[46:05] announced that he's like working
[46:07] entirely on openclaw for M365. So that
[46:09] would be different. That would be like
[46:10] integrate that' be like a userf facing
[46:12] product. You can see this big
[46:14] advertisement. I I have advertisements
[46:16] disabled on my um DNS. So it just wow
[46:19] techrunch is apparently I never go to
[46:21] techrunch. You can see all these like
[46:22] block boxes that just say advertisement.
[46:26] Um yeah. Yeah. So maybe there'd be a
[46:28] userf facing claw as well because I saw
[46:31] that there's somebody at Microsoft who's
[46:32] just entirely working on that now. So
[46:34] that's interesting.
[46:36] Uh so yeah my upcoming events is the
[46:40] host your agents on foundry live stream
[46:42] series the cosmos DB virtual conference
[46:45] agent con which is in Silicon Valley
[46:47] thought it would be cool with claude is
[46:49] an SF that's an anthropic contract cont
[46:52] uh conference but we're going to have a
[46:53] workshop there. uh Pyon so that's uh May
[46:57] mid May so similar time as the web
[46:59] summit uh Posette which is Postgress
[47:01] conference that's virtual in June and
[47:03] then Microsoft build which is in San
[47:05] Francisco in June
[47:08] copyclaw is that what's going to be
[47:10] called Copclaw I don't know if that
[47:13] rolls off the tongue
[47:18] um but you know we'll see we'll see what
[47:20] they call it
[47:23] Um,
[47:26] yeah.
[47:30] What is that emoji?
[47:33] Oh, a bucket.
[47:36] Let's see. Anything else? Um,
[47:40] okay. I think we've
[47:44] covered a lot of stuff.
[47:48] All right.
[47:51] Very good.
[47:55] Okay.
[47:56] See if there I think there's I think we
[47:59] covered the questions for today. I can
[48:03] see. Uh so
[48:06] let's just see if anyone has one last
[48:10] question.
[48:11] Sometimes we get a bunch in the last
[48:13] minute or we're just saying bye. Let's
[48:15] see. Type D type.
[48:23] I have a you have So, Uncle Patrick has
[48:25] a foundry agent up and running. How do
[48:26] you publish as an N365 co-pilot agent?
[48:29] It's a good question. Um, when you say
[48:31] agent, you have a Foundry hosted agent
[48:33] or a prompt agent? Um,
[48:37] I have to find my
[48:40] uh sign in. Why aren't you
[48:44] hosted agent? Okay, great. All right,
[48:46] good. I need to work on that anyway. So,
[48:47] let me go up. Let me open my hosted
[48:49] agents repo.
[48:55] Okay.
[49:02] Where is my
[49:06] It's this one.
[49:10] This one maybe.
[49:14] All right. AI project pfed.
[49:19] Oh yeah, here we go.
[49:38] All right. Trying to get my
[49:42] I think this one
[49:45] build
[49:47] ages version five. Okay. And then where
[49:53] is our
[49:58] do we have a publish here?
[50:07] Thought we had a publish there. No. Go
[50:10] check
[50:19] share.
[50:21] Nope.
[50:24] All right. So, I was thinking that we
[50:25] had a publish here, but maybe we only
[50:27] have the publish for prompt agents.
[50:30] So, let's go ahead and see the actual
[50:33] documentation. Oh, I should have all the
[50:34] docs in my agents. MD
[50:39] uh set of deploy a hosted agent hosted
[50:43] agents overview. Okay.
[50:46] Um
[50:48] so how can we can we publish? Okay. So
[50:52] publish hosted agents to channels.
[50:56] So it says
[50:59] that we should be able to do web app. We
[51:01] saw that one. Marxus 365 copilot and
[51:04] teams. Yeah. So, why haven't I seen
[51:08] that?
[51:16] Um, I don't know. I feel like we used to
[51:19] have a publish button and now I can't
[51:20] see it or looking for existing. Yeah, I
[51:25] don't know. I should be able to answer
[51:26] this question. I need to be able to
[51:27] answer this question because I'm sure
[51:28] this is going to come up
[51:31] um during the live stream series.
[51:34] uh because it does say that we should be
[51:36] able to p post it at um
[51:40] to M365, but right now I'm not seeing
[51:43] it, which is confusing.
[51:45] Um yeah, I'll I'll look into this after
[51:48] because I need to I need to switch work
[51:51] to this repo anyway. Um
[51:55] I'm really confused.
[51:58] So I'm not sure
[52:01] it like this problem is our docs say you
[52:03] can do it. Um, but they don't have any
[52:04] instructions. Uh, let's wait. Let's
[52:06] actually check here. Deploy. Deploy. No,
[52:08] I don't think so. Configure your agent.
[52:11] Create the hosted agent. No, that's the
[52:13] deployment. Hosted agent. Nope. Nope.
[52:15] Nope. Nope. Okay. So, um, yeah, I'm not
[52:20] sure. I need to find that out.
[52:24] Yeah. So, where what happened to the
[52:25] publish button? I wonder if it's because
[52:26] of I am I in a flight here? Build
[52:29] version flight. Okay. All right. Uh
[52:32] yeah, I will check and see what happened
[52:34] to that
[52:36] publish button. Uh you can ping me on
[52:38] LinkedIn to see if I find out.
[52:41] Um so John says, "I know your foundry
[52:43] deployment session is coming up. Are
[52:45] there good resources to dig deeper on AI
[52:47] agents deployment?" Well, if you mean
[52:49] foundry hosted agents, then uh you can
[52:52] see
[52:54] um these are the resources that I'm
[53:00] um using. I think it'd be just easiest
[53:02] to wait for the series because there's a
[53:04] lot of stuff happening right now.
[53:05] They're like literally like redoing the
[53:07] SDKs and stuff like so. Um I think it's
[53:10] just easiest to wait two weeks to be
[53:12] honest because things are changing. Um
[53:15] but um
[53:17] uh
[53:19] there's, you know, those are the the
[53:20] hosted agent ones, but also the other
[53:22] the thing that you can try that should
[53:24] work right now is um the AZD
[53:28] example.
[53:29] this one. Uh oh, sorry. GitHub chin.
[53:33] This one.
[53:35] So, this was what I started with to test
[53:38] it. And there's a um a blog post that
[53:42] corresponds to it. And this was like a
[53:44] pretty recent blog post. So, if you do
[53:47] want to try Foundry Hosted agents, maybe
[53:48] go through that blog post first. That's
[53:51] what I had my colleague do. Um which
[53:53] deploys this Seattle hosted agent. That
[53:54] was the basis for mine. Uh and then if
[53:57] you if there's any issues, you can file
[53:58] them in the uh ACD repo with the
[54:02] deployment.
[54:04] There's a link here to file issues.
[54:07] So yeah, so that is where I would start
[54:10] off.
[54:13] All right. Okay. All right. So now we
[54:16] are over time actually. So, I will go
[54:18] ahead and
[54:21] close this up and later I'll publish the
[54:23] recording and the transcript and all
[54:26] that good stuff. I'll put it on usual
[54:30] link which is linked from my GitHub up
[54:32] here.
[54:34] All right, thank you everyone. Thanks
[54:37] for coming for all the great questions
[54:38] and comments. Bye.
