[00:00] All right,
[00:03] I think we've got everything set up
[00:08] on both Discord and StreamYard for
[00:11] recording. So, we uh we do record these
[00:14] office hours so that we can share the
[00:17] recording and the write up afterwards in
[00:19] the Foundry discussion forum. Uh so, uh
[00:24] I'll I'll link to that as well so you
[00:28] can see past writeups. I need to I need
[00:30] to make that I need to make an aka a a
[00:32] short link for that so we can link to
[00:34] it. Um but here is where everything will
[00:38] be posted and I've got a nice skill that
[00:42] turns all of the questions and answers
[00:45] into comments on this thread which is
[00:47] really fun. So you can see what we've
[00:50] covered in past weeks as well.
[00:54] Uh so yeah, so if you have any questions
[00:58] or comments or things to share at any
[01:01] point, just put it in the chat. Um we
[01:05] don't usually do the audio because it
[01:06] doesn't work with my recording setup and
[01:09] it's just easier for me to see the
[01:10] questions in the chat. And I usually
[01:13] start off with the weekly news.
[01:16] So what has been going on this week? The
[01:18] huge thing that you've probably seen
[01:20] because I think everyone's seen it is
[01:22] Open Claw, also known as Cladbot, also
[01:25] known as Moltbot, but I think it's now
[01:27] currently known as OpenClaw. Um, it's
[01:30] been all over the news and everyone's
[01:32] written about it and it's very
[01:34] interesting, but I have not installed it
[01:36] because
[01:37] uh I've been told not to install it from
[01:40] a security perspective because it does
[01:41] have a lot of access to like everything,
[01:44] right? So, it runs on your machine. It
[01:46] can connect you to all your
[01:47] communication mechanisms. It can control
[01:49] your browser. It has full system access.
[01:52] Like this is a very powerful agent.
[01:55] Potentially too powerful
[01:58] and uh and yeah. Uh so you can
[02:02] potentially run it on isolated sandbox
[02:05] containers if you have access to that
[02:07] and some people are running it there.
[02:09] Um, but it certainly wouldn't recommend
[02:11] running on your work computer and also
[02:13] probably wouldn't recommend running on
[02:14] your personal computer given that it has
[02:16] browser access and your browser is
[02:19] logged in with your cookies and uh, you
[02:22] know, it's like giving a very smart
[02:26] toddler access to your machine
[02:29] and everything always goes crazy if I
[02:31] give my toddler any access to any of my
[02:33] devices. Uh, so uh, yeah. So, we've got
[02:37] some good comments. Uh, open steal your
[02:39] secret keys. Um,
[02:42] uh, Black Panda Chan says, "Stay away
[02:44] from it for now, but it is a neat social
[02:46] experiment." Right. So the social
[02:47] experience that part of that is
[02:48] moltbook.com which was not created by um
[02:52] not created by the creator of OpenClaw
[02:54] but is based off of it with the idea
[02:56] that if you have these um OpenClaw
[03:00] agents deployed you can
[03:04] point them at this social network and
[03:06] that's where they can chat with each
[03:07] other. But this one has particularly
[03:09] been exploited up the wazoo. So you like
[03:12] really really don't want to um you know
[03:16] point your open claw agent at maltbook
[03:20] um because of just like this this has
[03:22] not been developed in a very secure way.
[03:24] So, there was um I think I linked to it.
[03:26] There was Oh, I didn't link to it here,
[03:29] but there you know the I think it was
[03:30] the whiz
[03:32] um molt book
[03:35] uh D. There we go. Vibecoded security
[03:38] flaw, right? Um
[03:42] there we go. This is what I was looking
[03:44] for. Whiz.io. Okay. So, moltbook
[03:46] database reveals
[03:48] millions of keys, right? So Moltbook in
[03:50] particular, which was not coded by the
[03:52] same people, um, but is based off of the
[03:55] OpenCloud agents, has a lot of security
[03:58] issues, but OpenClaw itself because it
[03:59] has all of this access also has a lot of
[04:02] security issues because it is so
[04:04] autonomous, right? Uh, yeah, I see we're
[04:07] all reading the same article. There was
[04:08] I do want to point out I did find a very
[04:10] interesting article on
[04:11] pragmaticengineer.com
[04:14] um
[04:16] and where um they interviewed the
[04:21] creator of Claude.
[04:25] So here and I thought there were some
[04:28] really interesting
[04:30] um interesting
[04:33] perspectives of uh of how he manages,
[04:36] right? because everybody talks about you
[04:37] know doing this agent um you know really
[04:42] agent centric development and people are
[04:44] experimenting with that and the creator
[04:46] ex claims that he runs five to 10 agents
[04:50] at the same time and still manages to
[04:51] stay in the flow state which I find
[04:53] really surprising uh he says code
[04:55] reviews are dead for this workflow and
[04:57] instead you have architecture
[04:58] discussions I don't know like it's very
[05:01] interesting I'm not there yet um for for
[05:05] um you know for my repos at least some
[05:09] of my repos I think for personal repos
[05:11] sure I would agree with lots of this
[05:13] stuff like repos that I'm not sharing
[05:14] with anyone uh but not for I don't think
[05:18] I would use them for an open source repo
[05:19] but very interesting article so uh you
[05:22] know give it a look
[05:26] uh I see some comments so molt did make
[05:28] you think about building something
[05:30] similar within the discord community as
[05:31] a fun social or a local Reddit uh could
[05:34] be fun. Yeah. And I think if you're
[05:36] interested in this, there's also
[05:37] letta.com
[05:38] and let creates these uh agents with
[05:42] memory and a lot of them run on blue
[05:45] sky. So if any of you are on blue sky,
[05:46] you can um if I check my blue sky, it's
[05:49] probably like half Leta bots right now
[05:51] because I follow um Cameron. So Cameron
[05:55] is developer advocate at Leta and he is
[05:59] always uh yeah if you're interested in
[06:01] in autonomous bots um on on social media
[06:05] um where is Void? So he's runs I think
[06:08] three different bots. Uh there we go. So
[06:11] there's Comind which is one of them and
[06:15] uh there's also Void and Void always
[06:17] likes to say deep things. Oh and then
[06:18] there's Grunk. Grunk. Um so he's Yeah.
[06:23] So he's always experimenting with this
[06:25] and that's why some people say because I
[06:27] guess blue sky is the easier to
[06:30] integrate with from agents um and is
[06:33] more I guess friendly to the agents. Uh
[06:38] oh there's void void is the one
[06:42] that I see the most often.
[06:47] Uh so a chrono librarian my function is
[06:50] not to create but to curate the past
[06:52] present and future. this expert network
[06:56] void can be very deep sometimes.
[07:01] Uh so yeah, do check that out. Um I
[07:04] haven't deployed a letterbot myself, but
[07:07] he always has interesting
[07:11] interesting things that he is he talks
[07:14] about in terms of memory and building
[07:17] agents with memory.
[07:19] Uh, and I think they're doing it a bit
[07:21] more responsibly than the open claw.
[07:25] Uh, and I like that this one is like,
[07:26] yeah, they're trying to learn. How can
[07:28] agents learn, right? And what does that
[07:30] mean? And, um, they've got some good
[07:33] blog posts and research about it as
[07:35] well.
[07:38] Let's see. So, question, have I tried
[07:40] the Codeex app yet? No. I tried Copilot
[07:44] CLI last week. Um, I think Codeex is
[07:47] pretty
[07:49] similar. Uh, I can download it right now
[07:51] and find out. Let's see. Uh, I don't pay
[07:56] for chat GBT anymore because I wasn't
[07:59] using it quite enough to bury to because
[08:01] right now I'm trying to use Copilot in
[08:03] the browser more. Uh, so I don't know if
[08:06] I need to pay for it. We'll find out.
[08:09] Codeex
[08:16] Okay,
[08:20] I know um in on the news front, Codeex
[08:24] Openi just acquired Klene and with the
[08:28] thought that um
[08:31] Oh, wait. They just said they didn't
[08:33] acquire it.
[08:35] So, did they get acquired or not? So
[08:38] confused. Okay.
[08:41] Flying clarified.
[08:44] Okay. Well, don't we don't know if
[08:47] opening eye acquired client or not. That
[08:50] was the what I saw, but now I'm
[08:52] confused. And maybe it was an aqua hire.
[08:54] Um, a lot of these things lately, the
[08:57] acquisitions are actually like aqua
[08:58] hires, like both to avoid monopoly stuff
[09:00] and also just to avoid paying as much
[09:03] money, I guess.
[09:05] So, I don't know. But Klein was
[09:07] something similar, right? A a CLI. So if
[09:10] they're aqua hiring clin that would mean
[09:12] the engineers would be spending more
[09:14] work on codeex.
[09:16] Uh so welcome continue with codeex.
[09:19] Okay. So we can go to let's see I think
[09:23] I use Google to log into chatbt. Here we
[09:26] go.
[09:30] Sign into codeex with chatbt.
[09:35] Okay. So yeah, since I now don't have a
[09:38] paid chatd account, I don't know how
[09:41] much it'll limit me, but I'm sure I can
[09:42] use it a little bit. All right, so now
[09:44] going back to codeex continued. It's
[09:47] included in my plan for free through
[09:48] March 2nd. All right, add project. Okay,
[09:53] let's see what project
[09:57] I want to run it on.
[10:01] Uh
[10:07] We'll just do let's see if we can figure
[10:09] out the bug
[10:11] that I'm working on in Copilot.
[10:15] All right. So, here we go. So, here's
[10:17] Codeex.
[10:18] Um,
[10:20] wait, let me check also.
[10:25] Okay. All right. Actually, I don't want
[10:28] the problem is I'm actively developing.
[10:30] Let's see.
[10:33] Well, why don't we test and see? Okay,
[10:35] so one thing. So, going back to like
[10:37] stuff I was working on this week. Um,
[10:40] I'm working on making it easy to migrate
[10:42] from the chat completions API to the
[10:44] responses API and I'm developing a
[10:46] prompt for to be able to do that
[10:48] repeatedly that I can share with
[10:50] developers. Right? So, I've tested that
[10:52] prompt basically 10 times until it
[10:55] became a uh like a really good prompt
[10:57] that just worked in one shot. So, now I
[10:59] have this prompt. Right? So, here's the
[11:01] prompt. It's a very long prompt. It's
[11:02] actually based off of a codeex prompt uh
[11:06] that OpenAI developed for people using
[11:08] codecs, but then I I you know switched
[11:10] it over to a prompt. MD file. So this
[11:14] prompt in a single shot was able to pro
[11:17] uh move over this fairly simple chat
[11:20] completions um application.
[11:23] So let's see. Now, we could do a test
[11:26] though because now that I have this
[11:27] prompt, what I can do is just um
[11:32] check out the main which is still using
[11:34] chat completions.
[11:37] And then um I'll just copy and paste
[11:41] this prompt. All right. So, let me go
[11:43] ahead and add a new project. So, I'm
[11:46] going to go here
[11:48] and then open up
[11:52] open up this project and see how well
[11:56] Codeex does with the same prompt because
[11:58] that's kind of like an apples to apples.
[12:01] All right, so let's see. Okay, so now
[12:03] we're here and then what do I do? No
[12:05] thread. New threads. Okay, so start a
[12:08] new thread. Okay, so now Okay, let's
[12:11] just ask what branch am I in? And you
[12:14] can see this one defaults to Okay, so
[12:16] here's the models we have. Codeex, codec
[12:18] high, codeex extra high. Lots of people
[12:20] swear by extra high, right? Um, so maybe
[12:23] we should just move to extra high.
[12:25] Although I don't know if I might end up
[12:28] having to pay for chat GBT at this
[12:30] point. I still really like chat GBT, so
[12:32] I I've been tempted to pay for it again.
[12:34] Okay, so I'm on main. All right. All
[12:37] right. Um, I'm just going to paste in
[12:40] this entire prompt.
[12:44] Go.
[12:47] Here we go. Paste it in the entire
[12:49] prompt. And let's see what it does. Now,
[12:54] it's a nice UI. Um, I didn't realize
[12:57] that Codex was I guess I thought that
[13:00] Codex was like a CLI UI, but this is
[13:03] actually like a chat GPT UI, which is
[13:06] kind of cool. So it's it's similar to
[13:08] GitHub Copilot, right? Like this is I
[13:10] was doing this in GitHub Copilot. Um
[13:14] so similar except I'm not inside VS
[13:16] Code. I'd rather just be in VS Code. I
[13:18] see there is open. So I can open in VS
[13:20] Code, VS Code Insiders, Finder,
[13:22] Terminal, Xcode. Okay, so they make it
[13:24] easy to open. So presumably you could
[13:26] have Codeex on the side and then VS
[13:28] Code. I know some people like that kind
[13:29] of workflow when they're using Cloud
[13:31] Code. Like my partner says he really
[13:32] likes that. He just has cloud code open
[13:33] and then he's got uh I think he uses um
[13:37] Jet Brains on the side.
[13:40] Um oh, Justin said this is brand new as
[13:42] of yesterday. Wait, what is brand new?
[13:44] Is it this whole app is brand new?
[13:49] Oh, really? Okay.
[13:52] You can see how much I've used Codeex.
[13:53] The Codex app is new. Okay. Well, news.
[13:55] Codex app. That's another Okay. Another
[13:57] new thing this week is the Codex app.
[13:59] Okay. Well, that's cool. It's pretty
[14:02] cool. Um
[14:05] although I you know I as a Microsoft
[14:10] Wait, so this is opening a brand new VS
[14:11] Code. Okay. And then it just opened in
[14:13] my VS Code. Yeah. Interesting. All
[14:16] right. Wait. Going back to codeex. Okay.
[14:18] All right. So, of course, GBD 5.2 is a
[14:21] little bit slow. It's doing a lot of I
[14:23] guess it's just doing a lot of research.
[14:25] All right. So, we're gonna have to go
[14:27] back to it because GPD 5.2 to extra high
[14:30] is, you know, maybe a bit on the slow
[14:33] side. Um,
[14:37] and okay, so what you're saying is that
[14:38] the codeex app is new. You can also use
[14:42] a CLI version of codeex, right? Um, but
[14:46] here we're trying out the thing. All
[14:48] right. So, it's a bit slow. So, I think
[14:50] we need to come back to it and see um
[14:54] later on how it does because I did give
[14:56] it a a kind of a long task to do and
[15:00] we're using extra high reasoning.
[15:02] Probably should have started off with no
[15:04] reasoning.
[15:07] All right, cool. Let's see. So, while
[15:09] that's going, related to that is skills,
[15:11] right? Everybody's talking about skills
[15:13] right now. Like, I know my colleagues
[15:14] are like, "Hey, anybody got a skill for
[15:16] that? Who's got a skill for this?"
[15:17] Right? Everyone's just passing around
[15:18] skills. And it's so funny because a
[15:19] skill is just a markdown file with, you
[15:22] know, maybe a Python script attached.
[15:24] Um, but you know, it's amazing what you
[15:25] can do with a lot of skills. So, um, uh,
[15:29] my colleague shared this earlier this
[15:30] week, skills.sh should this is somebody
[15:32] else made this, but, um, it's just a way
[15:36] to find, uh, find skills. Now, the thing
[15:39] is you don't know if these skills are
[15:41] truly going to learn or if they're
[15:42] actually like insecure and stuff like
[15:45] that. Um, the other thing is that we've
[15:48] got Awesome Copilot. So that has a lot
[15:50] of more Microsoft specific skills and I
[15:53] know my colleague is working on a
[15:56] website version of Awesome Copilot. Um,
[16:01] so actually we should be able to find
[16:03] the website version of it because it
[16:05] would just be uh let's see it would be
[16:09] it'd be the GitHub pages URL. So let's
[16:11] see if we have Here we go. I think it'd
[16:15] be this. Uh, yeah. So, here we go.
[16:18] Skills,
[16:20] right? So, this would be another and
[16:22] this is a this is obviously a much
[16:24] shorter list of skills, but these um
[16:26] particularly could be helpful when
[16:29] you're doing Microsoft and Azure stuff
[16:31] because we're more likely to have
[16:34] stuff specific to Microsoft and Azure.
[16:36] Um
[16:38] but uh but yeah, if you are looking for
[16:40] skills, you can browse right in there
[16:43] and get some skills. Um so far the only
[16:46] skills I've used are actually for this
[16:49] office hours when I'm doing the
[16:50] writeouts uh the writeups. So we have
[16:53] skills in here for um in uh for grabbing
[16:58] the live chat from YouTube, for grabbing
[17:00] the transcript from YouTube videos, and
[17:01] for posting Q&A on GitHub discussions,
[17:05] right?
[17:06] So, those are helpful and
[17:11] yeah, I mostly haven't used skills
[17:13] beyond that. Um, but people are really
[17:16] liking that. Oh, can they expl Yeah. Can
[17:19] I explain what skills are? Yeah. So, let
[17:20] me go to insiders. Let's actually just
[17:23] do
[17:24] a use a skill. Um, so we'll go and
[17:32] uh open up my repo that has some skills
[17:36] in it.
[17:37] Let's see. Office hours
[17:41] writeups.
[17:43] Okay.
[17:49] All right.
[17:51] So
[17:54] here is a repo where I have the let me
[17:57] make this bigger. I have in the
[18:01] um in the github/skills we have folders
[18:06] and each of the folders has a name and
[18:08] it has skill.mmd and that's basically
[18:11] you know the the text description of the
[18:13] skill. So this is the name this
[18:14] description. Now, this is quite
[18:15] important because this this is basically
[18:17] like your MCP tool description, right?
[18:20] This is what's going to be shown to
[18:22] GitHub Copilot when it's deciding
[18:24] whether to bring in the rest of a skill,
[18:26] right? So, by default, it should it's
[18:28] only going to see the name and
[18:29] description and then if it thinks that a
[18:30] skill is relevant, then it will bring in
[18:33] the rest. Uh, as far as I understand it,
[18:35] that's how it'll work. So you do want to
[18:37] put a lot of effort into your name and
[18:39] description and um and so that it know
[18:43] it can figure out what to use, right? Uh
[18:45] so then we also have YouTube live chat.
[18:47] So this one um downloads live chat. Oh,
[18:51] that's interesting. Like that one's got
[18:53] funky feel like that's
[18:56] weird. Why is it like that? Okay, I'm
[18:58] going to remove that
[19:01] markdown back. You know how LM's like to
[19:03] put back around everything. Okay. And
[19:06] then YouTube transcript. All right. That
[19:07] one looks good. So extract transcripts
[19:09] from used videos. Okay. All right. So
[19:12] then like let's say um there's the thing
[19:15] is like you can then like mix and match
[19:17] these skills certain ways. So I have a
[19:18] particular workflow I use when I'm
[19:20] turning these office hours into um
[19:23] writeouts where I say this and then and
[19:26] then in my agents.mmd I have all these
[19:28] tips about like what skills to use like
[19:30] when generating the write up. Follow
[19:31] these skills. Use the YouTube transfer
[19:32] skill. use a type live chat skill. So,
[19:35] I'm like being pretty explicit here. Um,
[19:37] but now that these skills exist, I could
[19:39] use them for anything, right? So, I
[19:40] could go to my Let me go to my YouTube
[19:45] and then like just grab one of my um
[19:49] videos. Okay, so like this one. Let's
[19:51] std spec kit. I don't think I ever did a
[19:53] write up for this one. Uh, did this one
[19:57] Let me check if this one had a
[19:58] transcript because it did. It definitely
[20:00] helps. Yeah, it has a transcript. Okay.
[20:03] All right. So, I'm just going to say
[20:05] um
[20:09] let me just put a new folder here. Uh
[20:14] STD live stream.
[20:17] Okay. And I'm just going to say generate
[20:20] a writeup for
[20:23] this video
[20:27] and store in STD live stream.
[20:34] folder. Okay. All right. So,
[20:38] I'm just doing this prompt and the hope
[20:40] is that it's going to use
[20:43] the the the skill, right? And uh here
[20:47] now you can see it. So, you can tell
[20:49] it's reading the skill. So, it sees it
[20:51] wants to use the transcript skill and it
[20:53] wants to use the live chat skill. So,
[20:55] we've see it's basically invoke the
[20:56] skill. This is similar to like MCP where
[20:58] you can see like oh it's going to use an
[21:00] MCP tool. All right. So it is um you
[21:05] know so once it decided which ones to
[21:07] use then it actually went and read the
[21:09] skills. Right. So here it's it decided
[21:12] which ones it wanted to use. Let me look
[21:13] at the chat debug views so we can see. I
[21:16] don't know. I like getting like really
[21:18] down into it. Right. So chat debug. Chat
[21:20] debug. Where's our chat debug view? Oh
[21:22] let's go over here. Chat
[21:24] debug
[21:26] chat debug view. Okay. All right. So,
[21:29] generate a write up for the video.
[21:33] Um,
[21:35] I wanted to see so tools
[21:39] and
[21:41] let's see. Oh, codeex wants to alert.
[21:43] Thanks, Codeex. Okay.
[21:48] So, I actually haven't checked to see
[21:49] how it determines what skills
[21:52] Okay, these are the tools
[21:55] available deferred tools.
[22:03] Those are all the tools.
[22:08] How does it do skills
[22:13] YouTube transcript
[22:16] work?
[22:22] Okay. So, it just says here is a list of
[22:26] skills
[22:28] each skill. Okay. All right. So, this is
[22:30] you can see this is what VS Code
[22:32] actually sends. It says here's a list of
[22:35] skills that contain domain specific
[22:37] knowledge on a variety of topics. Each
[22:38] skill comes with a description of the
[22:40] topic and a file path. So yeah, as I was
[22:42] saying, it only when it first sends the
[22:44] message, it only sends the skill name
[22:50] and the description and a path to it.
[22:53] Right? So here you can see um that you
[22:57] know we have the
[22:59] live chat skill, YouTube live chat
[23:02] downloads live chat transcripts and this
[23:05] is where it is right. So for each skill,
[23:07] it's going to send the name, the
[23:09] description, and the path to um the
[23:12] skill.md. Right? So when you're, you
[23:15] know, when you're doing your
[23:16] engineering, your skill engineering, you
[23:18] do want to make sure the name and
[23:20] description is very clear.
[23:24] Uh so it's working on stuff. Oh,
[23:30] got a partial transcript. Interesting.
[23:34] All right. So, it's going and it's
[23:35] getting those skills blah blah blah.
[23:39] Okay, I see a comment. The biggest
[23:41] downside of skills task and specific
[23:43] instruction workflows is there's a
[23:45] context loss pretty frequently when
[23:47] you're chaining them together.
[23:49] Uh, interesting. I guess I mean I think
[23:51] it depends like where why is the context
[23:54] being lost in that case, right? because
[23:55] if if I'm in a single session in VS
[23:58] Code, then the context should all stay
[24:01] as long as it hasn't compacted the the
[24:03] history, right? Uh if I go over, you
[24:06] know, the token limit like 128 uh K,
[24:10] then you know, then the I can lose the
[24:12] some of the context. Um
[24:16] but in theory, if I haven't gone over
[24:17] the context window, then there should be
[24:19] no compaction. Uh then the context
[24:21] shouldn't be lost. So maybe you're
[24:23] you're uh describing something else.
[24:27] All right. So it is
[24:31] and you can see that the actual skills
[24:34] are uh so this one YouTube transcript
[24:36] and YouTube live chat those both have
[24:38] actually all of these have associated
[24:39] Python files right and you can see here
[24:41] what we're using um is UV in order to
[24:44] run these scripts because then what we
[24:46] can do is just say UV run and we put the
[24:49] dependencies in line right so that way
[24:51] we don't have to set up like a whole pi
[24:53] projectl just for our skills so this is
[24:55] what general recommendation is use uv
[24:58] and use the this is actually I think
[25:01] part of a standard now for Python as a
[25:03] standard way of declaring the
[25:05] dependencies and requirements for a
[25:07] single Python file. Um so do that if um
[25:12] you know when you're when you're running
[25:14] creating Python skills so that way
[25:16] they're standalone.
[25:21] All right, it generated a um a writeup.
[25:27] Let's see.
[25:29] Live chat.mmd. Oh, that was the live
[25:32] chat that it grabbed. This is the actual
[25:34] transcript that it grabbed. And here is
[25:38] so it worded it as question answers
[25:40] because that's what it's used to doing
[25:41] in in this repo here. Um, what is spec
[25:45] kit and how do you get started? How does
[25:47] the specify step work? What is it? How
[25:48] does invitation work? And it's cool.
[25:50] Like it links to the timestamps which
[25:52] really impresses me. like it's so good
[25:55] at turning transcripts into writeups
[25:57] that have timestamps. Uh so I really
[25:59] want to do it for for everything. Um
[26:06] this is cool. Yeah, I'll probably just
[26:07] check this into the repo because uh it's
[26:10] fun.
[26:12] Uh so there you go. So that is um how
[26:16] skills works. Um
[26:20] okay. Okay, so I see the comment is when
[26:22] a skill is invoked, it should have all
[26:23] the information. But in my experience,
[26:25] when you have a skill that can also
[26:26] invoke another skill, sometimes it feels
[26:28] like a new session is somehow opened.
[26:30] Well, if that does happen, I would go
[26:32] ahead and check the chat debug view
[26:34] because then that's how you can truly
[26:36] see everything that gets sent, right?
[26:39] So, we could actually see like, okay,
[26:41] with the final thing where it generates
[26:42] the write up, like what is being sent
[26:45] here, right? And you know, it's um
[26:49] there's a lot in here. Uh you can see
[26:51] here the whole transcript,
[26:53] right? So I think if you're curious
[26:55] what's going on, this is you know, I
[26:57] always use chat debug view in order to
[27:00] figure out exactly what is going on
[27:02] behind the scenes, which I I really
[27:03] like. It's there's kind of a lot um
[27:06] going on here, but uh but it it does
[27:10] help out with understanding.
[27:13] Um I see a question. Do we have to use
[27:15] insiders to use skills? That's a good
[27:19] question. Um,
[27:21] let's see. VS Code skills support. I
[27:25] know we Let's see. Last week the
[27:27] insiders
[27:29] was What were the things we added last?
[27:33] Um, I think that we've had it in stable
[27:36] for a bit. So, let's see. Using agent
[27:38] skills in VS Code.
[27:41] Uh, let's see.
[27:44] It's in preview. I see. Okay. So, you do
[27:48] not have to use insiders, but it looks
[27:52] like you do have to enable it
[27:56] explicitly.
[27:58] Um, which makes sense since
[28:01] Yeah. Well, since it's a new thing and
[28:02] it's kind of like opening you up to to
[28:05] new capabilities. So, maybe that's why.
[28:08] Um,
[28:10] so yeah. So you can try it instable
[28:14] just um if it's not working uh do chat
[28:18] aent skills and this is cool you can
[28:20] just click on it and it'll open it right
[28:22] so let me open this in VS code and see
[28:25] okay so now I can use my agent skills oh
[28:29] that actually makes sense I didn't
[28:31] realize you had to do that and I was
[28:32] trying to I do actually have a skill in
[28:34] this repo it's just a skill for um
[28:38] replying uh to comments on PRs because I
[28:42] I have this workflow where um here's my
[28:46] workflow where when I ever I have a pull
[28:48] request and they get comments, I like to
[28:50] work through each comment uh one at a
[28:53] time with co-pilot and say, "Oh, do we
[28:55] want to implement this? Do we not blah
[28:57] blah blah?" And then I have Copilot, you
[29:00] know, make the change or not. And then I
[29:01] have Copilot reply in line to the
[29:04] comment. Um, but the GitHub MCP server
[29:06] doesn't have a tool that can reply to
[29:09] inline PR comments. So, I had to add a
[29:12] skill, right? So, that's another use
[29:13] case for skills is like, okay, you're
[29:14] using MCP server. It has almost all the
[29:17] functionality you need, but dang it,
[29:18] like it doesn't have this one
[29:20] functionality. Um, so here the skill
[29:22] tells it how to use the GraphQL API
[29:25] instead, right? Um,
[29:29] so yeah, that's the one other place
[29:30] where I have a skill so far is is in
[29:33] this repo and that's just to help with
[29:34] my workflow. And that's a really nice
[29:36] workflow. I really like that workflow.
[29:38] Like I still really like code reviews.
[29:40] And I like assigning um I like, you
[29:42] know, I like having co-pilot review my
[29:44] code. I like having colleagues review my
[29:46] code. And whenever I get feedback, I
[29:48] want to like go through each bit of
[29:50] feedback one by one and like actually
[29:52] think carefully about the feedback and
[29:55] decide whether I really want to do it,
[29:56] right? Especially with the reviews from
[29:58] Copilot because Copilot can be really
[30:01] critical and sometimes too critical,
[30:04] sometimes like too nitpicky. Sometimes
[30:05] it really wants to overengineer
[30:07] something like add like a lot of
[30:09] exception handling and it's like you
[30:11] know what it's fine. We're not we're not
[30:15] going to do this today, right? And in
[30:16] that case I'm like okay we're just going
[30:18] to add a comment acknowledging that yeah
[30:21] there's like an edge case here but we're
[30:22] not going to implement it. Right? Um, so
[30:25] I do really like that like this workflow
[30:27] here of um, you know, going through PR
[30:30] comments, but I did need the skill so
[30:33] that I could reply have my co-pilot
[30:36] reply to the comments on the PR for it.
[30:40] Uh, let me link to that one too.
[30:43] Uh, in case anybody wants to
[30:47] try,
[30:49] uh, try the this prompt. Uh,
[30:53] here.
[30:55] I see the comment is code review is
[30:57] always a mental block for me because
[30:58] there's always a better way of doing
[30:59] things from someone else's point of
[31:00] view. Right? And that's like the whole
[31:02] thing is like you like you know you're
[31:04] trying to figure out like okay like what
[31:06] is reasonable, what is not. So that's
[31:07] why I like like I get the code review
[31:09] comments and then you know I can bounce
[31:12] them off another LLM like typically the
[31:15] code review comments I think are from a
[31:16] GPT model and then um and then I'm going
[31:20] through them with like opus and so we
[31:22] can get like you know different opinions
[31:25] um sometimes I even bounce them off a
[31:27] human and then give the human's opinion
[31:29] as part of it. Uh, so yeah, I mean you
[31:32] you want like I think code of reviews
[31:34] are really important because sometimes
[31:35] they catch something that you really
[31:36] didn't think about that's really
[31:37] important. Um, but you also there's some
[31:40] balance to uh you know how much how much
[31:43] you can reasonably account for, right?
[31:48] All right, cool. So skills, that was
[31:50] fun. Um
[31:53] yeah, so that's why skills are pretty
[31:54] exciting like just as a way of
[31:56] complimenting uh what your agent can do
[31:58] and and say there's lots of places where
[32:00] you can find skills to try out and if
[32:02] you have your own cool skills please do
[32:04] submit them to awesome copilot so that
[32:06] we can keep building it uh in that repo.
[32:08] Let's see let's check back on codeex.
[32:11] Okay. All right. So
[32:16] um did it manage to
[32:19] All right. Uh, so
[32:24] the question is, does it work?
[32:28] Let's see. Let me just ask. Did they run
[32:30] the P test warning observe? Okay, so it
[32:32] says I I do have a harder time kind of
[32:35] seeing I don't know. U Okay, pi test
[32:40] diff summary.
[32:42] Um, okay. So, this is kind of similar.
[32:45] It gave the highle thing. All right. So,
[32:47] the question is, did it work? Uh, let me
[32:50] let me see if if it actually worked. Uh,
[32:54] I can just run the
[32:57] let me close I got to run it. Let me run
[33:00] it. Let me close the other one that I'm
[33:03] running over here. All right.
[33:05] And
[33:08] let's see if it worked.
[33:16] Okay.
[33:20] All right, we're just going to say hi.
[33:23] And how did it do? Moment of truth.
[33:28] Hello. All right, it worked. Okay, so
[33:31] codeex was able to
[33:34] um port the code from chat completion to
[33:38] responses using the same prompt using
[33:41] GBD52 with extra high, right? And then
[33:45] we can say like okay let's say make a
[33:47] pull request
[33:50] with the changes.
[33:55] Uh now I don't know if it because
[33:56] normally I'm you know using the GitHub
[33:58] MCP server. Um but since this is codeex
[34:01] I'm guessing it's going to use oh it
[34:04] says per the guard rails I can't run
[34:06] GitHub get commit push opening par.
[34:09] Okay. Um what guard rails?
[34:13] Let's see.
[34:16] Maybe I would need to enable. Is there
[34:19] Can I enable the MCP server? In your
[34:22] migration request, you set these Oh. Oh,
[34:24] in your migration request, you set these
[34:26] guard rails. Do not run GitHad get lead
[34:29] version control to the bootstrap script.
[34:31] Oh, I need to remove that from the
[34:32] prompt. I don't care about that. Okay.
[34:35] Oh. Uh, ignore those god Rails. Wow. Are
[34:39] they like really strict?
[34:41] that they were a mistake.
[34:46] Is it going to let me ignore the
[34:47] guardrails? It might have very strict uh
[34:50] because my in co-pilot I this did not
[34:54] happen. So um I'll uh
[34:58] probably end up removing that.
[35:02] Is it going to Can I bypass the
[35:04] guardrails? Because this is a guardrails
[35:07] just at a prompt level. So usually
[35:11] I think it's going to bypass them.
[35:14] But that was nice.
[35:16] Um, now I know I need to
[35:19] modify that in my in my prompt
[35:23] so that people who don't get limited.
[35:26] All right. So, what is it doing? Listed
[35:28] files in heads. Listed files in codecs.
[35:32] I don't really understand what heads.
[35:35] Oh, that's a list codeex. List heads.
[35:38] Are these branch names maybe?
[35:43] Okay. Yeah, it checked out a branch.
[35:47] I think at this point I could move off
[35:49] of extra high
[35:53] uh to get it to be a little bit faster.
[35:59] Oh my god. Okay.
[36:02] All right. It's working on that.
[36:06] Stop thinking. You're thanking too much.
[36:09] Okay. All right. So, while it's working
[36:11] on that, uh let's see what else. Right.
[36:14] So, it's saying working on migration
[36:16] from chat completions to responses API.
[36:18] Uh I'm going to test that on
[36:20] increasingly diff more difficult repos
[36:22] until finally I run it on the rag repo
[36:25] which is my most complex repo. Um, but
[36:27] before I can run it, I have to port from
[36:30] sorry from Prompty
[36:32] uh to Ginga 2 because Prompty is only
[36:34] designed for chat completions API and I
[36:37] don't think we're supporting Prompt
[36:38] anymore really. I think that's on the
[36:40] deprecation path. Uh, so I'm just going
[36:42] to use Ginga 2 as my prompt renderer,
[36:46] you know, just as templates and uh, you
[36:48] know, that's quite standard. So I have
[36:50] that branch ready and I'm just running
[36:53] the test for that now. Um,
[36:57] so that should be good. Okay, this thing
[36:59] is still
[37:02] Why is it making a directory? My gosh,
[37:05] why is it so
[37:09] I kind of want to like stop it and put
[37:10] it out as misery. Okay. Oh, cool. Okay,
[37:13] we get a question popup. All right, this
[37:14] is actually something that we also got
[37:16] added to VS Code recently in GitHub
[37:18] Copilot is that now it can pop up a
[37:20] multiple choice question, especially if
[37:22] you're doing planning mode. So if you
[37:24] ever do planning mode in GitHub copilot,
[37:26] if it has like open questions, it'll can
[37:28] pop open a multiplechoice question now
[37:30] and ask you what you want to do. So So
[37:33] that's kind of fun for VS Code insiders.
[37:35] All right. Do you want me allowed to
[37:36] state the changes? Yes. Yes.
[37:40] Okay. So I don't know if that was like
[37:42] an ask question flow or if that was like
[37:43] an approval flow. Maybe that's what the
[37:45] approval flow looks like for
[37:48] um that kind of looked like approval
[37:49] flow. Do you want me Do you want to
[37:51] allow me to commit? Okay. So this is
[37:52] actually their approval flow. Do you
[37:54] want to allow me? All right. So So
[37:56] that's kind of interesting. So they're
[37:58] they they have a very like explicit
[38:00] approval flow like um Okay. So
[38:05] So that's good. So they're they're you
[38:08] know they're trying to be cautious about
[38:11] what commands they're allowed to run,
[38:14] especially with Git. Um, so it looks
[38:16] like it's pretty happy to do all sorts
[38:18] of file edits, but when it comes to git
[38:21] commands, it asks me for both git add
[38:23] and then git commit.
[38:26] So they must have like a list of what
[38:27] things. Okay. And then also check out
[38:28] create the future. Yes. Yes. Yes. Yes.
[38:31] Yes. Yes. Do all of these things
[38:37] and push. Yes.
[38:41] And I just did an allow all for all of
[38:43] those, which you don't always want to
[38:45] do. Like get push, you might want to be
[38:47] explicit about it. Uh, but at this
[38:50] point, I've gotten kind of tired of
[38:52] clicking approve all the time for
[38:54] agents. Uh, now it's going to use the
[38:57] GHPR. That's what I was expecting it to
[38:59] use. Okay,
[39:02] so that's going to create the pull
[39:03] request.
[39:05] And if it's running this in my terminal
[39:08] environment, it should have credentials
[39:10] to do it. Okay, great. So, it did it.
[39:12] All right. So, now we've got the PR um
[39:16] the PR request summary is not really as
[39:20] thorough as I would like. But now,
[39:21] what's interesting is that um I wonder
[39:24] if it can can do this because I also
[39:26] have this PR which was with Opus, right?
[39:28] You can see here this is a PR with Opus.
[39:30] So, I wonder if it could diff. Okay, I'm
[39:33] going to turn off maybe let's go to high
[39:36] or medium. Okay, compare
[39:39] these two diffs
[39:46] and describe the differences, right?
[39:48] Like, did they come up with the exact
[39:50] same solution or did they come up with
[39:53] different solutions? I think that's kind
[39:54] of interesting. Uh, but anyway, if you
[39:57] want to see what it came up with, here
[40:00] is the the PR.
[40:04] All right. So, it is um searching the
[40:08] web. So, that's so okay. So, it decided
[40:10] it had to search the web to be able to
[40:13] read those in those web pages. I thought
[40:16] it would just fetch the web page or it
[40:18] it you know in VS Code usually would use
[40:20] the GitHub MCP server just to pull pull
[40:22] the uh request. Um so, I definitely
[40:26] think uh it would be good to add the
[40:29] GitHub MCP server to this one. Um, you
[40:32] know, because VS Code we have it by
[40:33] default. Um,
[40:37] but I think it'd be good to Can we just
[40:39] do like a gallery? GitHub MC. Okay. So,
[40:42] it doesn't have GitHub
[40:45] uh as like a kind of in a gallery. So,
[40:47] you'd have to add
[40:50] add it here. Command launch. That would
[40:53] be over HTTP.
[40:55] And then you go to GitHub MCP server.
[40:59] Here it is.
[41:01] and GitHub MCP server. So, we can just
[41:04] do this one, uh, which will use OOTH for
[41:08] the authentication.
[41:10] Um, okay. So, we're doing this one.
[41:15] Well, we shouldn't have to set our bear
[41:17] token environment variable because
[41:19] hopefully it supports MCP authorization
[41:22] and it should go through the
[41:23] authentication flow. But maybe it won't.
[41:25] I don't know. Uh, Justin says MCP on
[41:27] codec is a pain. So I don't know if that
[41:30] means that it doesn't support the full
[41:31] MCB off blow. Uh cuz alternatively,
[41:35] okay, it doesn't like this. It's just
[41:37] this does not work. Okay. All right. So
[41:40] you the other approach is that you can
[41:41] go like this and say and I could set a
[41:44] GitHub token in an environment variable
[41:48] and then and then you know, right? So I
[41:50] could be like GitHub pat. Um, I don't
[41:53] have that set right now and I don't want
[41:55] to have to set that up, but that should
[41:56] work if we were doing that. It looks
[41:59] like it just really doesn't like
[42:01] Yeah. So, maybe it hasn't properly
[42:03] configured MCP authorization because if
[42:06] we did this in VS Code, it would go
[42:08] through the OOTH dance and give
[42:10] permission, but right now it's just not
[42:13] responsive.
[42:14] So, as Justin says, MCB and Codeex is
[42:17] apparently a pain.
[42:21] Um, oh, you have to enable it. Okay.
[42:24] Codeex settings, NCP servers, no,
[42:29] general.
[42:30] Uh, okay. There's a bunch of
[42:32] configuration, sandbox mode, approval,
[42:36] policy, config.toml. Okay. So, there's
[42:39] like quite a lot of things you can
[42:41] configure here. All right. So, let's see
[42:43] what it what the difference is. Scope
[42:46] 358 is larger.
[42:49] Um, oh that's because I had the actual
[42:51] prompt file in there. Um,
[42:57] oh this is an interesting change. So the
[43:00] codeex version changed the front end and
[43:04] the opus version did not change the
[43:06] front end. And maybe I should change the
[43:08] front end. Oo, that's a good call.
[43:14] That gives me something to think about.
[43:16] Wow, that changes everything. Okay. Um,
[43:21] let's see. 358 did a better job with
[43:24] this one.
[43:26] Um,
[43:27] 359 I see. Okay. Uh, so this is actually
[43:32] really interesting because this gives me
[43:33] some various ideas about how to improve
[43:35] the prompt and like kind of decisions I
[43:37] have to make. Is that if I'm changing
[43:38] the back end to responses, should you
[43:40] also change the front end to expect
[43:43] responses or is that too large of a
[43:45] change? Right? Um, and that might be
[43:46] something that the user has to decide.
[43:49] Um,
[43:53] cool.
[43:55] Yeah. So, it's a good idea to try
[43:58] prompts across multiple models just to
[44:00] see uh what you know what sort of
[44:02] differences you get
[44:04] and um, you know, decide which one is
[44:07] better. That's why some people like when
[44:09] they talk about running multiple agents
[44:11] at the same time, it's actually just so
[44:12] they can get different variants on the
[44:14] same feature. That's probably the
[44:16] biggest because the thing is like when
[44:17] people talk about running multiple
[44:19] agents at the same time, like that feels
[44:21] like a lot of mental overhead where
[44:22] you're like really am I going to work on
[44:23] five different features at the same
[44:25] time? Like that's kind of crazy from a
[44:27] mental cognitive load perspective to be
[44:30] alternating between five disparit
[44:33] features at the same time and trying to
[44:35] remember like you know what your
[44:36] thoughts are about each of them. Um but
[44:38] if you're working on a single feature
[44:40] and you want to see like hey how would
[44:42] this model tackle it? How would that
[44:44] model tackle it? uh then I think that
[44:46] makes a lot of sense for running at the
[44:47] same time or like with the GitHub uh
[44:50] copilot CLI you can do the slashreview
[44:52] command in order to have get reviews
[44:54] from five you know five different models
[44:56] at the same time. So I think to me
[44:59] that's a really good use case for
[45:01] running agents in parallel is to say
[45:02] like okay I've got the same feature
[45:05] there's a few different ways that this
[45:06] could be done uh you know let's just see
[45:09] what a few different models would come
[45:10] up with right like maybe you do like GBD
[45:12] 5.2 to Opus 4.5 and Gemini 3, right?
[45:16] Like the three frontier models and see
[45:18] what their perspectives are. Um
[45:21] so yeah, and in um in VS Code now, this
[45:24] is what's worth um pointing out is that
[45:26] when you do when you're in chat, when
[45:28] you do new chat here, that actually
[45:31] creates a new chat that's running
[45:32] concurrently. So if you do have
[45:34] something that's running like at the
[45:35] same time, let's see if this one's
[45:36] running. Uh that one's not running. But
[45:38] sometimes what I do is like I run evals
[45:41] in one and then like I start up a new
[45:43] chat at the same time. So if you are in
[45:44] insiders when you click the new chat
[45:47] that will in fact keep the old chats
[45:49] open if they're still running. So I if
[45:53] you're doing multiple changes and you're
[45:55] happy for those changes to be on the
[45:57] same git work tree, you can just do new
[46:00] chat and just start up multiple threads
[46:03] uh multiple chats. Now if you want to
[46:04] have different git work trees like
[46:06] different branches then you want to use
[46:08] a background agent right so you see here
[46:10] you can click from local background or
[46:12] cloud so if you want different git work
[46:14] trees then you need to use either a
[46:16] background agent that'll make a
[46:18] different branch or a cloud agent and
[46:20] that also would do a different branch
[46:21] and send a pull request right but if
[46:24] you're working on changes that are
[46:25] orthogonal you're happy for them to all
[46:26] be in the same branch um and maybe some
[46:29] of them are just kind of you know like
[46:31] just you know running a a eval or
[46:34] something. Um then you can just do new
[46:36] chat, right? So you have multiple
[46:38] options for how you can run agents in
[46:41] parallel now and um you know and this is
[46:44] what kind of everyone's trying now to
[46:45] see like oh is it like useful or is it
[46:47] just like crazy distracting like um you
[46:50] know but you have the options now right
[46:52] so remember if they can all work on the
[46:54] same branch if if they're not going to
[46:56] step on each other's toes and if you're
[46:58] happy for them to all be like in the
[47:00] same PR uh you can just do a new chat um
[47:03] otherwise you can do background or you
[47:05] can do cloud
[47:08] I see we have a suggestion create an
[47:09] agent to control the multiple agents and
[47:12] give that the cognitive load. Yeah, if
[47:14] you trust your agent to you know to uh
[47:17] reconcile the different agents, sure go
[47:19] for it. Yeah, it all depends on um you
[47:22] know what the the level of risk in in
[47:24] the code is that you're working on right
[47:26] and uh you know is it if you're just
[47:28] doing prototype hobby thing you know
[47:30] then you can go wild but you know of
[47:33] course if you're working on some legacy
[47:35] codebase with your colleagues uh you
[47:38] know with you know for your organization
[47:40] then that's where you usually want to
[47:41] have like a nice clean pull request
[47:43] right to me it's always about do you
[47:45] want a clean pull request um or you know
[47:49] is Is it fine just to stuff it all in?
[47:52] All right. So, let's see. So, what else?
[47:54] Uh, let's um
[47:58] uh there's a new Postgress learning
[47:59] path. Just wanted to shout that out
[48:01] because the Postgress team um shared
[48:04] that with me. So, if you are doing
[48:05] Postgress,
[48:07] uh you can check check that out. It
[48:10] talks about all the new AI features
[48:12] available in Azure Postgress. That's
[48:14] fun. Um
[48:17] let's see. I I was saying I was I'm
[48:19] working on this PI AI talk and I find
[48:22] this actually really interesting. So
[48:24] what I'm doing here is I've got this MCP
[48:26] server and I'm trying out different type
[48:28] annotations to see which of them is
[48:31] works the best with different agents. So
[48:33] you can see like for um expenses like I
[48:36] try out like okay what if the expense is
[48:38] a date um or wait sorry expenses
[48:41] expenses okay what if the expense is a
[48:44] string or what if the date is a string
[48:46] what if the date is a string with a
[48:49] description what if it is an actual date
[48:52] time and what if it is a string with a
[48:54] reg constraint right so these are four
[48:56] different type annotations for the same
[48:58] field and then what I do is I run this
[49:02] with a bunch of um edge a bunch of
[49:06] cases. Sorry, going back here. Okay, so
[49:08] I run it with a bunch of cases like okay
[49:10] like you know if we get this request
[49:12] here
[49:14] um you know does the date come out
[49:16] correctly. Right. So uh so we've got a
[49:19] bunch of tests there and then I've got
[49:21] an agent. I've got four different
[49:23] agents. I have a pedantic AI agent, a
[49:25] lang chain agent, copilot SDK agent and
[49:28] an agent framework agent. So I can run
[49:31] each of these agents, point that at the
[49:32] MCP server, run them against my like 27
[49:36] um sample user inputs and then see how
[49:40] the different ones like how they do. Um
[49:43] so like what was the one I you know so
[49:45] here with like GPD 52 I can see like
[49:48] okay so for date uh we can see that it
[49:52] actually GPD52 did quite well with date.
[49:55] That's all 100%. Oh that was a date
[49:57] format date match. Oh, that one got
[49:58] 100%, too. All right, let's find one
[50:00] that was harder. Uh, C-pilot with HiQ.
[50:03] Okay, let's look at Copilot with Haiku.
[50:05] So, Copilot SDK using HiQ, like the date
[50:08] ones, the best was the annotated string
[50:13] and um and the rest didn't do quite as
[50:16] well, right? Um oh, here we see more of
[50:19] a difference, right? So, this one, you
[50:21] know, 89% success. This one was the most
[50:25] successful. Um, and these ones were were
[50:29] less successful. So, I'm basically
[50:31] trying to figure out like how much do
[50:32] type annotations like different schemas
[50:35] help when you're building MCP servers
[50:38] and are there differences across models?
[50:40] Are they are there differences across
[50:42] agents, right? Um because then you can
[50:45] kind of decide like reason about all the
[50:47] different ways that you can uh you know
[50:51] uh do type annotations for your
[50:53] parameters for MCP servers and and see
[50:56] if there's um you know what the
[50:59] improvements are.
[51:02] Uh so this will be this will be a talk
[51:04] for PI AI and you know I'll share my
[51:08] learnings after the talk. Um, but
[51:10] generally I do encourage you always to
[51:12] set up evaluations for, you know, for
[51:15] things like this because here I can
[51:16] actually evaluate and see like are my
[51:18] MCB tool schemas working as well as I
[51:21] hope and um, you know, and it's pretty
[51:25] straightforward to set up evaluations.
[51:28] Here I'm using Pantic AI evals, but you
[51:30] can also use Azure AI evaluation evals
[51:33] as well.
[51:36] All right. Uh so question well we have a
[51:39] question about openclaw and molt book
[51:41] but we talked about that at the
[51:42] beginning so I'll just defer to um to
[51:46] you know what I said in the beginning is
[51:48] you know it's interesting as and as
[51:50] other people were saying as well it's a
[51:51] very interesting experiment it's also
[51:52] very scary from a security perspective
[51:55] so you know we can watch that experiment
[51:58] and learn from it um but best to not
[52:01] deploy it yourself and if you are really
[52:03] interested in autonomous bots u maybe
[52:05] check out leta instead. Uh, but you can
[52:08] refer to the earlier conversation, too.
[52:14] All right, what else?
[52:18] Uh, thanks for coming, G. Crumb. Have a
[52:22] good week. Yeah, we're getting to the
[52:23] last few minutes here. All right, so
[52:24] let's just talk about upcoming series.
[52:26] We do have the Python and agent series.
[52:29] So, I was actually working on upgrading
[52:30] agent framework demos earlier today in
[52:33] prep for this series um because they've
[52:36] been continually iterating on that SDK.
[52:39] So, do register for that series if you
[52:41] haven't yet. That will be a fun one. Um
[52:45] like this first session will be kind of
[52:47] a recap of ones we talked about before,
[52:49] but then we're going to talk about
[52:50] context and memory, which people ask
[52:51] about all the time, and then monitoring,
[52:53] evaluating, and then a whole week on
[52:55] workflows. So, that should be cool. And
[52:58] if there's, you know, anything
[52:59] particular you want to see, just let me
[53:00] know. Uh, let's see. Microsoft AI tour
[53:03] has been going around the world. Uh, so
[53:04] maybe coming to a place near you. We had
[53:06] New York City very recently. Pi AAI is
[53:09] coming to San Francisco. That's the talk
[53:11] I was just talking about where I'm going
[53:12] to talk about MCP. And we got some good
[53:15] speakers there. We got Guido. We got
[53:17] Jeremiah. Oh, Jeremiah is coming. Oh my
[53:19] gosh, Jeremiah is so nice. He's the
[53:21] maintainer of FastMPP and he's we're
[53:23] always DMing about stuff because he's
[53:25] really trying to make it work well with
[53:26] Entra and and um Azure. So that's great.
[53:30] I didn't know he was coming. Uh you can
[53:31] see I'm speaking. We've got Sebastian
[53:33] from Fast API. Uh so great people coming
[53:38] here. Um got folks from OpenAI.
[53:41] Uh so that should be that should be
[53:44] really fun. Uh there's the MTV Summit in
[53:46] New York City
[53:49] and I submitted a few things to that.
[53:51] That's in April. And then there is Pyon
[53:54] in Long Beach in May. Uh and then of
[53:58] course at some point point Microsoft
[53:59] will have uh build and build is usually
[54:03] right after Python. No love in
[54:05] Minnesota. Well, you know, we can give a
[54:08] lot of love for Minnesota right now for
[54:09] uh its political efforts for uh trying
[54:13] to counter things. Um, uh, Minnesota.
[54:16] Yeah, I don't know what's going on in
[54:17] Minnesota on the Python front. Um, you
[54:20] can search Python. I don't know if
[54:22] Minnesota has user groups. Um,
[54:26] let's see. No, python.org.
[54:31] I mean, you probably know more about
[54:32] what's going on in
[54:35] Minnesota than I do. Uh, sometimes I
[54:37] check Where's the events? Attend a
[54:39] conference. Conference listings.
[54:50] No, these are more like the country
[54:52] level ones.
[54:58] Chicago.
[54:59] Chicago often has I feel like I just saw
[55:02] something in Chicago. Oh, there was
[55:03] something a Linux conference conference
[55:05] was happening in Chicago soon. Um, but
[55:08] not one I'm going to. Um,
[55:13] uh, yeah.
[55:16] Okay. Uh, I see. Okay, we got one
[55:18] minute. So, you saw my LinkedIn project
[55:20] using Playright. Is it safe to use an
[55:22] agency to do job search on LinkedIn
[55:23] without getting blocked by LinkedIn?
[55:25] Yeah, that is a great question because I
[55:27] know somebody who did get blocked on
[55:28] LinkedIn when using Selenium to do it.
[55:32] Here's the reason that I don't get
[55:33] blocked because when I am running this
[55:36] agent here, this is the one you're
[55:38] talking about here. When I run this
[55:40] agent, it is using an LL like it visits
[55:43] a web page and then it uses an LLM to
[55:46] reason about whether to accept that
[55:48] person to my network. And that LLM takes
[55:51] the same amount of time that I myself
[55:53] would take if I was making that
[55:55] decision. So I look like a human when
[55:58] I'm doing it, especially because I'm
[55:59] running it, you know, via my cookies in
[56:01] in in a browser on my computer. So, they
[56:04] really like can't tell the difference
[56:05] between me doing it uh and an LM doing
[56:08] it. Like, in some ways, LM's even slower
[56:10] than I am. So, um I think that's why I
[56:13] haven't been blocked, but there's
[56:14] certainly So, if you have a fear of
[56:16] getting blocked on LinkedIn, it's best
[56:18] not to set up automation. But also, if
[56:20] you're doing a job search, I think you
[56:23] could just do that without cookies. I
[56:25] needed to use cookies for mine because I
[56:27] wanted to my my agent goes through and
[56:29] accepts network requests. I should re
[56:31] run it. I haven't run it recently, so
[56:33] you can see I have 364 requests.
[56:36] Um,
[56:38] uh, so I needed the cookies, but if
[56:40] you're doing a job search, I don't know
[56:41] that you need the cookies. So I would
[56:43] just run it with a standard sandboxed
[56:46] because by default when you run
[56:47] playright, it'll open up a sandbox
[56:49] browser that doesn't have your cookies
[56:51] and that would be the safer approach
[56:53] because then you know what's going to
[56:55] block. I guess they could block your IP.
[56:57] They're probably not. And in my
[56:59] experience, if you are using an LLM to
[57:02] reason about the jobs that you're
[57:05] looking at, like then you look like a
[57:07] human because you're taking the same
[57:08] amount of time. So if you look like a
[57:10] human, you hopefully shouldn't be
[57:12] blocked, but I probably shouldn't be
[57:14] tell people like how to violate the
[57:16] terms of use of LinkedIn on office
[57:18] hours, but there you go. um you know
[57:21] like I view it as semi-automating like
[57:24] you know like I don't I to me I feel
[57:26] like I'm in the spirit of using LinkedIn
[57:28] where it's like okay like you know like
[57:31] I'm not using to spam people I'm just
[57:33] using it to accept other people's
[57:34] requests. Um but you know if you're
[57:36] doing it for job search please be nice
[57:38] to the companies and don't spam them you
[57:40] know like with lots and lots of
[57:42] applications unless you really want to
[57:43] apply there. But, you know, if you're
[57:45] trying to just do like a more efficient
[57:46] search, um, then, yeah, I feel like it's
[57:49] an okay use. So, yeah. So, anyway, you
[57:52] basically you need to look like a human.
[57:54] And, um, I think my agent looks like a
[57:57] human because the amount of time it
[57:58] takes and it just depends on your
[57:59] implementation and, uh, how you're using
[58:02] cookies and whether that'll get you
[58:04] blocked. Um, so hopefully, please don't
[58:08] get blocked. I would feel bad if you got
[58:09] blocked.
[58:11] All right. Okay. So, good. That is uh
[58:14] that's all we have for today. As always,
[58:18] I will run my skills which you saw. Um
[58:22] once everything is uploaded, the hardest
[58:24] thing is actually waiting for the
[58:25] YouTube transcript because that usually
[58:27] takes like 12 hours. So once the YouTube
[58:29] video is up and it writes the
[58:31] transcript, then I will um upload
[58:34] everything to this thread for future
[58:37] reference.
[58:39] All right, thank you everyone. And I
[58:42] hope you have a great day. Bye.
