[00:00] Welcome to our weekly office hours.
[00:03] Today is January 27th.
[00:06] Uh so we'll start off with some news in
[00:09] case you haven't seen these news yet. So
[00:13] big thing that was all over yesterday
[00:16] was MCP app support. This is what was
[00:20] previously known as MCP UI. uh but I
[00:24] think when they added it to the model
[00:27] context protocol they uh it you know
[00:31] they renamed it to MCP apps this is a it
[00:34] is the first official MCB extension so I
[00:37] guess maybe it's not technically part of
[00:39] the core protocol but it is an official
[00:42] extension so I guess now MCB has
[00:45] official extensions and the idea of MCB
[00:47] apps is that you know instead of servers
[00:50] right now can only pass down you know
[00:52] like text and maybe binary files like
[00:56] images. Um although even that I think is
[00:58] pretty limited but now servers could
[01:00] pass down like uh actually like rich uh
[01:04] interfaces like presumably this works
[01:06] during iframes. I have to assume that
[01:07] this is all done via iframes where you
[01:10] pass down an iframe and have you know
[01:12] like width and height and stuff like
[01:14] that but I haven't actually looked
[01:15] through the spec to see how it works and
[01:18] I haven't built an MP app myself. Uh but
[01:21] the idea is that sometimes you need you
[01:23] want richer you want a richer interface
[01:25] right you don't just want text
[01:28] and um
[01:30] and this gives you the ability to do it
[01:33] okay so I see a good question will we be
[01:35] able to deploy MC apps to co-pilots and
[01:38] teams I do not know the answer but I
[01:41] will immediately
[01:43] um
[01:45] ask in a channel
[01:48] um
[01:51] whether whether there anyone knows if
[01:54] we're going to have support for that
[01:58] though that's a good question and I
[01:59] don't know uh I'll just ask colleagues
[02:02] to see if they know more about support
[02:04] for copilot and team so generally vs
[02:06] code is basically like the most complete
[02:09] MCP feature complete client out there
[02:12] that's why VS Code often has support for
[02:15] these features immediately um other
[02:17] clients clients, you know, tend to lag
[02:19] behind MCP Sport, including, you know,
[02:22] like teams co-pilot that uh but you
[02:26] know, hopefully eventually they would
[02:27] add it. I, you know, there is kind of
[02:29] probably more of a security issue to
[02:30] think about. Uh, but I presume that all
[02:32] the apps are I framed, which does
[02:35] relieve a lot of security issues.
[02:39] So, you can see there's like a demo
[02:42] repository MP apps playground. Oh, it's
[02:44] from Harold. Thank you, Harold.
[02:46] Um so it shows it shows the the tools
[02:51] you could have a
[02:54] okay so question is what does it so you
[02:57] give back okay so you pan you hand back
[03:01] HTML
[03:03] and then that HTML
[03:06] goes to the server. Well this is all
[03:09] JavaScript. What we need to do is make
[03:12] the Python version of this
[03:15] of that playground.
[03:18] Um,
[03:20] since Harold was doing, let me just ask,
[03:26] let me ask Harold.
[03:30] Is there are is there a Python version
[03:35] acquiring Python devs? Want to know?
[03:38] Okay.
[03:40] All right. So, that's another good
[03:42] question is where do we get more fun
[03:45] examples in Python? Um, obviously we
[03:49] could port this. Oh, let's take a look
[03:50] at fastmcp and see if fastmcp
[03:55] has support for apps.
[03:59] Apps create an Azure.
[04:02] I think that it probably doesn't have
[04:03] support for apps yet, but maybe the
[04:06] official um MCP SDK does. Let's see if
[04:11] there's an open issue about MCP app.
[04:16] Okay. And
[04:20] or maybe MCP UI.
[04:26] Uh
[04:31] interesting. I'm not seeing a
[04:37] a uh you know an issue about it. Um
[04:42] so
[04:44] let me also just tweet at
[04:49] the JLo. Let's tweet at JLo.
[04:54] Does
[04:56] is
[04:58] MCB adding any particular support for MC
[05:03] apps?
[05:05] A quick look through.
[05:13] All right, let's see.
[05:17] Okay. Uh, so all right, so we'll find
[05:20] out about MCP. We'll find about teams
[05:22] co-pilot. Yeah, as for where to circle
[05:25] back, um, it's a good question. Uh,
[05:30] sometimes we get the answers during the
[05:32] stream and I'll just keep checking my
[05:34] teams to see if we get an answer during
[05:35] the stream. Uh, you know, if if not,
[05:39] sometimes I'll put it in the writeups
[05:40] and if not, you can just ping me on
[05:43] LinkedIn and I'll let you know if I hear
[05:45] anything back or not.
[05:49] All right,
[05:51] good questions. Okay, so so that's MCB
[05:55] apps. So that's definitely um you know a
[05:58] really
[06:00] uh really intriguing thing and you can
[06:02] imagine this being like the future of
[06:03] the web. I have to link always to Kent
[06:05] Dod's really good talk where he
[06:07] introduced
[06:08] um MCP apps. There we go. Future of user
[06:11] interaction. This is always this is my
[06:14] favorite where he um you know discusses
[06:19] a future where maybe instead of going to
[06:21] websites we're doing all of our chatting
[06:24] using uh aentic chat interfaces like you
[06:27] have co-pilot
[06:29] uh Microsoft copilot cloud code whatever
[06:31] chat dbt team and uh you know and when
[06:34] we need rich interaction it just comes
[06:36] into that chat terminal using MP apps uh
[06:40] so that's quite an interesting feature
[06:41] especially for those of us who are full
[06:42] stack developers that maybe websites are
[06:45] not going to be the prominent way that
[06:47] people interact uh you know with with uh
[06:50] the things they want to do. Increasingly
[06:52] we're already seeing that as developers,
[06:54] right? Like how many like I haven't gone
[06:56] to Stack Overflow for the last I don't
[06:58] know couple months, right? Uh instead my
[07:01] primary way of debugging and working
[07:02] through things is inside a GitHub
[07:05] copilot interface. So uh I think we're
[07:08] already seeing that for developers.
[07:12] Oh yeah. So you have relatives that use
[07:14] WeChat for everything uh and all chat to
[07:17] do everything. Yeah. So there's already
[07:18] that's true like in many countries uh
[07:21] you know SMS and WeChat, WhatsApp, all
[07:24] of that stuff are already the you know
[07:28] accepted way of um you know interacting
[07:32] with things like food ordering. Uh so so
[07:35] maybe that jump maybe that jump will
[07:37] just be an easier jump, right? like uh
[07:40] you know like it just will be more
[07:42] natural for them.
[07:44] Uh I think the advantage now is now we
[07:46] have LL like currently with SMS like
[07:48] you'd have to be you know you have to
[07:50] kind of it's it's not as sophisticated
[07:53] once you add an LLM like you have more
[07:55] flexibility right that ideally
[07:58] okay so there's other updates for VS
[08:00] code insiders for for those you have
[08:02] insiders installed you can see I have
[08:04] both VS code stable and VS code insiders
[08:06] and I just use both of them at the same
[08:09] time
[08:11] but if you use insiders you get all the
[08:14] cool stuff. So, Pierce Boggin is the one
[08:16] to follow if you want to see everything
[08:18] that's going on with insiders. Here's
[08:20] his um you know tweet from this week
[08:23] about some of the stuff, right? So, he
[08:25] had he says there's this like new agent
[08:28] HQ now. So chat, open agent session
[08:31] windows
[08:33] and various
[08:36] updates here add uh so you know
[08:40] definitely follow pi if you want to get
[08:41] the updates on everything in VS code and
[08:45] uh there's a bunch of new stuff so more
[08:47] context more tool calls better support
[08:49] for enthropic messages so we should see
[08:51] better updates from like opus models
[08:53] when we're using opus models uh better
[08:56] integration with claude so if any of you
[08:58] are using claude
[09:00] as your primary like coding tool. Now, I
[09:03] guess it's like directly integrated. I
[09:04] actually don't use Claude, but I know
[09:06] many people do. Uh there's a switch
[09:08] agent tool. So, if you do have custom
[09:10] agents in your repo, the switch agent
[09:11] tool can help you realize that actually
[09:13] you might want to be using one of the
[09:14] other agents. Uh let's see. Now, it VS
[09:18] Code can do reads allowed reads outside
[09:21] the workspace if you approve, which can
[09:23] be helpful sometimes. And there's now a
[09:26] way to run terminal commands in a
[09:28] sandbox. So that's that's nice from a
[09:31] security perspective.
[09:34] Uh so uh yeah, if you have insiders,
[09:38] just update your insiders. Let me make
[09:40] sure that I've got the latest. You just
[09:43] do restart to update. It'll go and grab
[09:46] the new insiders. That one's updated
[09:48] like basically every day. So there's a
[09:50] you do a lot of restarting, but you do
[09:52] get to see, you know, what they're
[09:54] experimenting with and give feedback
[09:56] really early. So I do like to use
[09:59] insiders most of the time.
[10:03] And then the other thing that everyone's
[10:04] talking about uh you know on social
[10:06] media is that people are really a lot of
[10:08] very well-known developers are coming
[10:10] around to the idea that actually at this
[10:13] point uh a lot of coding is mostly done
[10:17] via agents right so Andre Karpathy he's
[10:19] very famous in the AI space incredible
[10:22] ML researcher and he said he's basically
[10:24] doing uh you know 80 80% of his code is
[10:28] written from uh by agents right he's
[10:32] still writing like 20% and he is still
[10:34] watching them like a hawk. I like that
[10:36] he said that. He said like if you care
[10:37] about the code, you do want to watch uh
[10:41] you know watch them watch your code like
[10:44] a hawk uh like in an IDE like VS Code.
[10:47] Um, but that like really it's just much
[10:49] more efficient for him to have the agent
[10:50] write the code and he he reviews the
[10:53] code and he says his codew writing
[10:54] skills is atrophying but his code
[10:57] reviewing skills like he still has to
[10:59] have very good code reviewing skills
[11:00] because he's looking constantly at this
[11:01] code.
[11:05] Uh, and I see okay co-pilot and co-pilot
[11:08] CLI. Yeah. So I actually did a live
[11:10] stream yesterday. I think a couple of
[11:13] you might have joined for that. Um I
[11:16] have a write up here uh with the with
[11:19] the live stream um if you want to see
[11:22] the live stream or just see what we
[11:24] talked about. Um basically I use the
[11:26] GitHub co-pilot CLI and I mostly used
[11:30] the review command um because I'd seen
[11:33] that on the internet. Um I also tried
[11:37] custom agents but they didn't work very
[11:38] well. I tried MCP. It also didn't work
[11:41] that well, but I have a I figured out a
[11:43] better approach afterward. And then I
[11:45] tried the GitHub copilot SDK and that I
[11:48] think is very interesting. Let me check
[11:50] out my branch with that so you can see.
[11:53] Uh so we could actually see it. Uh let's
[11:56] see. So
[11:58] uh where's the branch?
[12:02] SDK experiments. Okay. Get check out SDK
[12:05] experiments.
[12:08] Okay. All right. So,
[12:12] um
[12:14] this one. All right. So, where did we
[12:16] put Okay. All right. So, this is using
[12:20] the um the Copilot
[12:24] SDK.
[12:26] And
[12:27] here we've got a couple different
[12:29] scripts, but like this one. Okay. So,
[12:31] basically it is a programmatic way to
[12:33] access GitHub Copilot. And the thing
[12:35] that's helpful about this is that it you
[12:38] don't have to deploy any models. You can
[12:40] use the models that are built in SK.
[12:42] Now, what's a little annoying is that
[12:44] you're actually pretty limited in the
[12:45] models right now. And I just sent that
[12:47] feedback to the team because I'm like, I
[12:48] don't want to use Sonnet. I want to use
[12:50] Opus. Um, but you know, right now
[12:52] there's a limited set of models for some
[12:54] reason. So, I'm chatting with the team
[12:56] to figure out why. Um, but you know, I
[12:58] can at least use any of those models and
[13:00] not have to deploy. So it's basically
[13:01] like an agent framework that you don't
[13:04] have to do any deployment for. And if
[13:07] you're already using GitHub Copilot, you
[13:10] know, it'll be you'll be able to use
[13:12] similar prompts to what you're using in
[13:13] Copilot and it'll, you know, run inside
[13:16] your your environment here, right? So
[13:19] we, you know, we create a C-pilot client
[13:22] with some options. We configure the
[13:24] session to use a model and a system
[13:27] message
[13:29] and um
[13:32] yeah in this case it is analyzing pull
[13:34] requests. So let me just
[13:37] uh run this
[13:40] so you can see what it does.
[13:48] Um so let's see what so
[13:54] I see some comments here. So,
[13:59] all right, let's see.
[14:02] Oh, no module. You do need to install
[14:06] Do you need to install the SDK? I I
[14:08] switched branches, so I lost mine, so I
[14:10] just need to reinstall it. So, you can
[14:12] just do pip install with this this um
[14:16] SDK. Uh, so let me go inside my
[14:20] environment, my virtual environment. PIP
[14:23] install it. Make sure we have it here.
[14:27] And now we've got it. So now I'm just
[14:29] going to run the script here. Okay.
[14:35] So this is running. It's got access to
[14:37] the repo. It's got access to the PRs.
[14:40] You can give it access to MCP servers.
[14:43] You can get it access to tools
[14:45] and um you can give it access to custom
[14:48] agents. So Cthra said or was it Cthra
[14:52] said that you got custom agents to work
[14:53] with Copilot SK? I do I have uh was it
[15:01] uh let's see. So this one is where I
[15:03] pointed it at an MCP server. So you can
[15:05] point it explicitly at MCP MCP servers.
[15:08] The interesting thing is that it doesn't
[15:10] just like use your VS Code
[15:13] configuration. So if you wanted to have
[15:15] access to MCP servers, you do need to
[15:16] explicitly set that up. Um, and then
[15:20] also with custom agents. So this is
[15:23] where we did a custom agent. So you can
[15:25] also like set up sub aents, right? So
[15:27] here I said, okay, here's a sub agent.
[15:29] And I tried to do it based off of my
[15:31] existing agent file here,
[15:33] triagger.agent.mmd, the one I use in VS
[15:36] Code. Um, but it was a little tricky to
[15:39] do that. Uh, I So, Cold Thrust, I don't
[15:41] know when you did custom agents if you
[15:43] were just writing an agent from scratch.
[15:44] I was trying to reuse an existing agent.
[15:46] But you can see with the agent, I set up
[15:48] the name, description, tools, and MCP
[15:50] servers. Um, so that then it could it
[15:54] could, you know, use that. So, um, so
[15:58] yeah, you can you can do a lot with it.
[15:59] And I think I just think of it as like
[16:01] an easy way uh to automate developer
[16:05] workflows, right? And it's just it's
[16:07] very easy to just check in a script,
[16:09] right? And as long as somebody has
[16:10] access to the co-pilot
[16:12] CLI, I think I think that's a
[16:14] requirement. If they have if you have
[16:15] the co-pilot CLI, then you know, then it
[16:18] should work, right? So if we look at the
[16:19] co-pilot um CLI,
[16:24] right? Is that the requirement? Yeah. So
[16:26] you do need the co-pilot CLI. So, you
[16:29] know, as long as your colleagues have
[16:30] the copilot CLI, then they can work. So,
[16:32] you can see here's the copilot CLI. We
[16:34] can pick a model.
[16:37] Uh, so here I'll go to what do I change?
[16:40] No, I want Opus. Give me OBS. All right.
[16:43] Thank you. All right. So, we can change
[16:44] the model. You can see our MCP servers,
[16:47] right? So, I've got one I've got work IQ
[16:50] now. I wonder if that one's going to
[16:51] work for me today. Like, okay, show me
[16:53] what events
[16:55] I have on my work calendar today. Let's
[16:57] see if that'll use the work IQ MCP
[17:00] server. It would be fun if it does. Um,
[17:04] yeah. So, here's our co-pilot CLI and it
[17:08] can do stuff. Oh, it's going to use the
[17:09] work IQ. So, work IQ. I should add that
[17:11] to the news. Work IQ. Work IQ is um that
[17:15] is a like a new command line tool and
[17:19] it's basically an MCP server, but you
[17:21] can kind of use it as you can use it
[17:23] like as a chat. You can use it as an MCP
[17:25] C server and um I've been using it like
[17:29] let's see where was I uh I was actually
[17:32] using it to try and prep the PowerPoint
[17:34] for today. So I said check the
[17:35] generative AI messages for the past week
[17:37] and summarize industry news only since
[17:38] Tuesday 120. Now I will say I feel like
[17:41] it did it didn't quite apply the date
[17:44] filter completely correctly but actually
[17:47] it kind of did. It said that you know AI
[17:49] assisted coding goes viral again. That
[17:51] that was the point I was talking about.
[17:52] So work IQ basically has access to your
[17:57] um you know like your outlook, your
[18:00] email, your teams. Now it only has
[18:02] readonly access. So we can't that kind
[18:04] of limits the usefulness of it. Um but
[18:07] you know it's still kind of fun. So we
[18:09] can say all right do I want to use this
[18:10] tool? Yes. And so now it is actually
[18:13] making a call to that work IQ server
[18:16] which is going to reply back.
[18:19] Uh, so work IQ also an interesting
[18:23] thing. Two events on the calendar today.
[18:27] Still
[18:28] working. All right. And you see I don't
[18:30] have that much today. We've got the
[18:32] weekly office hours and I always block
[18:34] my schedule for school drop off. Um, so
[18:37] that's fun. So that's the Copilot CLI.
[18:40] U, but we were using we were using the
[18:42] C-pilot SDK. Here you can see this is a
[18:44] chart it generated um using the SDK
[18:46] based off of PRs. Uh, but you can do all
[18:49] kinds of things with it. All right, so
[18:51] let's see. I'm behind on questions. Uh,
[18:54] so let's see what
[18:57] questions we have. Um,
[19:03] okay. So, Nick got an email about an
[19:06] upcoming hackathon hosted by Microsoft.
[19:08] Am I involved with this AI Dev Days
[19:12] hackathon?
[19:14] Huh?
[19:16] I don't know this one.
[19:18] I heard just about another one. There's
[19:20] another one coming up called Agent
[19:21] League. And apparently it's like an
[19:23] esports approach. Let me see if I can
[19:26] find the agent league one. Um Oh, we
[19:29] could ask Work IQ. Uh Work IQ.
[19:33] Is there an agent league event coming
[19:37] up? I think it emailed in my Outlook.
[19:41] All right, let's see if it can work. I
[19:43] cue this.
[19:45] Oh, here we go. I found it here. Um, so
[19:48] this one I heard about which is quite
[19:50] interesting.
[19:51] Uh, which is like a battle and you're
[19:54] like live coding it or something.
[19:57] They said it's based off of esports. I
[19:59] don't do esports, so I don't even know
[20:00] really what that means, but there is a
[20:03] creative apps battle, a reasoning agents
[20:05] battle, and an enterprise agents battle.
[20:07] So perhaps one of you, some of you would
[20:11] like to participate in one of these
[20:14] agents leagues. Um, and for AI dev days,
[20:18] who's involved with this one? Uh, Aaron
[20:23] Stark. I know Aaron. He's on marketing.
[20:25] I don't know. Osman. Um, so yeah, looks
[20:29] like we've got two
[20:31] hackathons coming up, which is can be
[20:34] really fun. good thing for the
[20:37] portfolio. Uh so we should definitely um
[20:42] you know definitely consider signing up
[20:44] for those. Um yeah, we'll make sure
[20:47] we'll get those in the notes. All right,
[20:49] cool.
[20:51] Okay. Is this a good place to ask about
[20:53] the Microsoft Foundry SDK or the agent
[20:57] framework SDK? Uh you can certainly ask
[21:00] about it. I uh we're going to be doing
[21:02] the agent series coming up. So pretty
[21:04] soon I'm going to be going diving diving
[21:07] uh head first into agent framework SDK
[21:11] uh which sometime like can wrap the
[21:13] Foundry SDK. Um I I haven't been
[21:17] directly using the Foundry SDK d like
[21:20] that much recently. Um but yeah, you can
[21:22] ask a question. We'll see if you know
[21:25] it. Um, I I'll probably start diving
[21:27] into that maybe after the office hours
[21:29] because I need to start making the
[21:32] slides and curriculum for our agent
[21:35] series. Uh, so uh if you know if you
[21:40] haven't registered for the agent series
[21:41] yet,
[21:43] definitely
[21:45] do that because that should be fun and
[21:47] that will be my excuse to get really
[21:50] deep into agent framework. Uh, so far
[21:53] I've done like the basics with it. Uh,
[21:55] but there's a lot deeper I can go.
[21:59] Am I using something like STD to guide
[22:01] the current coding agent? Um, STD sounds
[22:05] like TDD. Uh,
[22:09] is STD
[22:11] is STD? Oh, like spec driven. Okay.
[22:13] Yeah, got it. All right. STD is spec
[22:16] driven development.
[22:18] Um, and am I guy using that to guide the
[22:22] coding agent? Not really. Not that much
[22:26] because um because I haven't been
[22:28] working on really
[22:31] uh really big things. Um if I was going
[22:35] to write something from scratch, I would
[22:36] at least use plan mode first just to
[22:40] think through all the the details and I
[22:42] would maybe um have it write like a
[22:44] document first. So I have used like you
[22:47] know basically make documents um
[22:49] Nicholas Saka's persona
[22:53] assisted development. Um this is the so
[22:56] mainly I either use the plan mode which
[22:58] is new in VS code or I have used this
[23:00] persona based approach to software
[23:04] development. So this one I kind of likes
[23:05] because it starts off with a very like
[23:07] userfacing PRD that like a product
[23:09] manager would write and that's like
[23:11] really focusing on what is the user
[23:13] story going to be like and then we go to
[23:15] the architect that goes into like okay
[23:17] what are the design choices we're going
[23:18] to make technically and then finally the
[23:20] implement is going to turn that into
[23:22] code right um
[23:25] so so I like that approach is more
[23:28] structured but I haven't done speckit I
[23:29] know everybody asked me about speck kit
[23:31] and I haven't done speck kit yet Um,
[23:35] so, uh, I'd have to
[23:40] find a good, uh, use case for for spec
[23:44] kit. Um, I think I suspect that this is
[23:48] a good one if you really know what you
[23:52] want versus something if you're more
[23:54] like experimental and you kind of want
[23:55] to see what happens along the way.
[23:57] Lately, I've been being a like I'm I'm a
[24:00] little more experimental to see what
[24:01] happens on the way. And so, I'm not
[24:03] really ready with like I'm not
[24:05] necessarily spec. I'm iterating as, you
[24:09] know, as I go along.
[24:13] Yeah. So, here's SK spec kit. Uh, we
[24:15] talked about this briefly last time
[24:17] because this was originally made by Den
[24:19] and Den has now moved to Anthropic. Uh,
[24:22] so now there is a new maintainer for it,
[24:24] but they do say that there is a new
[24:26] maintainer for it. So hopefully it will
[24:28] keep going. Um,
[24:32] so yeah. So it's good to hear that you
[24:34] like that. I'm curious what kind of I'd
[24:36] like to know what kind of projects
[24:37] people have used for spec like where it
[24:39] works really well. Like if it's like a
[24:41] structured API like with fast API or
[24:43] something like that. That would be
[24:44] really interesting.
[24:50] All right.
[24:52] So let's see.
[25:00] Okay. Uh
[25:02] some audio stuff. Okay. All right. So,
[25:07] um other things
[25:09] happening. All right. So, we looked at
[25:11] work IQ. Um looked at the Copilot SDK.
[25:17] definitely check out the copilot SDK
[25:18] because I I I do think it's going to
[25:20] lower the barrier to developer
[25:22] automation and you know as developers
[25:25] like we want to we definitely want to do
[25:26] that. Uh I did just cut make a release
[25:30] in the rag repo. So if any of you are
[25:32] using the rag repo I just added
[25:35] basically we're trying to make our cloud
[25:37] ingestion pipeline be fully featured.
[25:40] And so now the cloud ingestion pipeline
[25:42] supports ACL that was a big thing I
[25:44] added. Uh so basically you can point the
[25:50] the repo at an Azure data lakeink
[25:53] storage account which is basically blob
[25:56] storage but with access controls on each
[25:58] of the blobs and then the we have these
[26:02] Azure functions and the Azure functions
[26:05] will um will process them and look at
[26:08] their their ACL's and turn those into
[26:12] oids and groups. So that's the
[26:13] individual user erids and then the entra
[26:15] group ids and then uh when it indexes
[26:18] them it will add the oids and groups. Uh
[26:23] so that's uh exciting because it means
[26:26] that you know when you're uh you know
[26:29] logging in and asking questions you
[26:30] should only get access to things you're
[26:32] allowed to have access to. Let me show
[26:34] my uh example
[26:37] so that you can see what I'm talking
[26:39] about
[26:41] on the rag repo side. It's the
[26:49] Yeah. So it's a good question. Colther
[26:51] says, "Isn't the ACL built into AI
[26:53] search now?" So yes, so AI search does
[26:55] have built-in understanding for ACL. So
[26:58] like when we set up the index you can
[27:02] see here that we um when we do the the
[27:06] fields right so okay um so if you say
[27:09] you want to use ACL's then
[27:13] uh let me find okay so then you actually
[27:15] set up your field you say it's going to
[27:17] be oids and then you explicitly say hey
[27:20] this is my user ids field so you
[27:22] basically have to make the field and say
[27:24] this is the user ids field and then you
[27:26] make your groups field and say hey this
[27:27] is the group ids field. So you're
[27:29] marking particular fields in the search
[27:31] index as specifically being for either
[27:33] users or groups. And then when um yeah
[27:37] when you're setting up the index then
[27:39] you and you also set set the option that
[27:41] says hey I want to enforce access
[27:44] control. So that's how you enable it
[27:47] from like the search index and the
[27:49] searching perspective. So then um you
[27:52] know when you run search it's actually
[27:53] going to it's going to obey that. Uh let
[27:55] me actually I I also added this script
[27:58] to make it easier to verify
[28:00] um you know like that it was working so
[28:04] that oh let me let me go back out to our
[28:06] other branch because we're in the
[28:08] experiments branch right now. Uh
[28:12] okay. All right. And then I'm just gonna
[28:17] run the script.
[28:20] So I added this script here so we can
[28:23] see. Right. So this is a very small test
[28:25] index. It only has three documents in
[28:27] it. If I search without sending in any
[28:31] tokens or headers, I only get back this
[28:34] one document. And that's because this
[28:35] document is set to allow everybody to
[28:38] view it. So you can set an ACL so that
[28:40] everyone's allowed to view it. So that's
[28:42] why I was able to get this back. you
[28:44] know, if I didn't send any um headers
[28:46] in, then if I send in my specific user
[28:50] token, me, Pamela Fox, then I get back
[28:52] both this one and the junest patterns,
[28:55] junst patterns, because this is uh this
[28:58] is one that my user specifically uh in
[29:01] data lake storage has permission to
[29:03] view. And then finally, if I'm really
[29:05] testing things out, there's a special
[29:07] header we can set in and that we've set
[29:09] permission like I gave myself an arbback
[29:11] role where I'm allowed to see
[29:12] everything. So here I can see, okay,
[29:14] we've got the woolly sunflower. It's got
[29:16] all on it. We've got the rush. This is
[29:18] my oid. And then we've got this one here
[29:20] that no one is allowed to see because
[29:22] has no ID oids and no groups. Um, so
[29:26] that's how it looks like from the search
[29:27] perspective. Uh, now in order to add
[29:30] support to cloud ingestion for this, um,
[29:34] there is a built-in indexer for AI
[29:37] search. Unfortunately, we couldn't use
[29:38] that due to some limitations. So
[29:41] basically I had to rewrite that using a
[29:43] data lake client instead in Python. Um
[29:45] but it's okay. I tried to make it just
[29:47] be functionally the same. So in the
[29:49] future we might be able to use the
[29:50] built-in indexer. Uh so yes, AI search
[29:52] does have it built in in various ways
[29:54] and we try to use as much as the
[29:56] built-in stuff uh as much as possible.
[29:59] So here you can see I am logged in and
[30:01] then I can say okay um
[30:05] does Woolly Sunflower like sun? Okay.
[30:11] So, when I ask questions, it's only
[30:14] going to search on and find the things
[30:16] that I have access to. In this case,
[30:18] Woolly Sunflower everybody has access to
[30:20] because it has oids and groups of all.
[30:24] Um,
[30:25] now with this one, does Junkus patterns
[30:27] like full sun?
[30:31] This one I should also be able to see
[30:33] myself, but if I asked my colleague to
[30:34] ask the same question, he wouldn't be
[30:37] able to see it. um because he wouldn't
[30:40] have his oid right so here you can see
[30:42] this is only my oid and then finally we
[30:45] can say does brristly matia poppy like
[30:49] full sun
[30:52] and it should not know the answer to
[30:54] this good it didn't know the answer
[30:56] that's what we wanted because it
[30:57] shouldn't have found any results at all
[31:01] um I see a question can I support oa
[31:04] ACL's from other identity writers like
[31:07] oka for whatever AWS and GCP are using.
[31:10] If you wanted to do that, you would
[31:12] basic you'd have to just basically do
[31:14] what we did before was um before AI
[31:17] search had it builtin support for like
[31:19] Entra ACL, we just implemented our own
[31:21] by passing along the token. So you would
[31:24] you would like need to like like for
[31:25] this repo you have to fork the repo add
[31:27] support for octa and then um forward on
[31:31] the the token and in the token you would
[31:34] like check the oid and you know like
[31:37] groups if if there's groups there and
[31:39] then you would need to check those on
[31:40] the index. So you can still like apply
[31:42] like the same the same idea is that you
[31:46] need to in your index you need to note
[31:50] the ACL's per you know per searchable
[31:53] chunk. Um but in your actual uh you know
[31:57] in your actual application you need to
[32:00] get the you know get that token and
[32:02] extract the relevant information from
[32:05] the oath token.
[32:08] Um, but this like yeah uh AI search only
[32:11] has built-in support for Entra.
[32:15] Uh, but I'll pass on your feedback that
[32:17] that would be interesting to you. I'm
[32:19] curious if you'd be using that for are
[32:20] you deploying something on Azure with
[32:22] Azure as search but then using IDP like
[32:25] other IDPs like octa. You know the
[32:27] interesting thing is I'm now in GitHub.
[32:29] I'm part of both GitHub and Microsoft
[32:30] now because we did this merger thing of
[32:32] Devrell and so I actually do use OCTA
[32:35] now um because GitHub uses OTAA. So now
[32:38] I'm experiencing what it's like to use
[32:39] octa and I got to say it's really buggy
[32:41] on my back. Um so I don't have it open
[32:44] right now because it does too many
[32:46] alerts. But at least I'm getting to to
[32:48] see what octa looks like
[32:51] or octa. I'm probably saying it wrong.
[32:56] All right. Uh so
[32:59] that's fun. Okay,
[33:03] so those are the main updates that I
[33:06] have. We do have the you know the
[33:07] upcoming events. Python and agent
[33:09] series. Markx FAI tour has been going
[33:11] around. It was just in New York City.
[33:12] Don't know if any of you made it to that
[33:14] one. Uh Pi AI is in San Francisco. I'll
[33:17] be speaking at that in March. MCP Summit
[33:19] is in New York City in April. Hopefully
[33:21] we'll speak at that. We submitted three
[33:23] talks for it. And then Pyon is in Long
[33:26] Beach in May.
[33:29] Uh so you said customers have other
[33:31] identity providers. So consuming datas
[33:33] from Salesforce and other systems and
[33:35] maintain ACL is in the question.
[33:37] Genesis. Yeah. So you so if you need to,
[33:41] you know, develop using other ACL, you
[33:43] could do that. I don't uh other IDPS. I
[33:46] don't know if AI search would ever add
[33:49] built-in support um for other identity
[33:51] providers because it might be more
[33:53] difficult to do, but uh I'll certainly
[33:55] pass on the feedback that that is uh
[33:59] that would be interesting.
[34:03] All right, what
[34:06] else
[34:08] do people want to talk about? Let's see.
[34:13] So there was some chat about
[34:17] agentic coding finding the point where
[34:19] agents start to run implementations of
[34:22] context.
[34:24] Yeah, I found that the context has
[34:26] gotten better. Um
[34:28] you know that it's it's not running out
[34:30] of context as much. So I'm able to to do
[34:33] longer things and I think the compaction
[34:36] is working better. Um but that that
[34:39] certainly can be limiting.
[34:42] All right. What else? We can go back to
[34:47] We could go back to the SDK experiments
[34:50] branch and look at the copilot SDK more.
[34:52] Uh we could just try spec kit if people
[34:55] want to just try spec kit right now and
[34:57] see how it works. We could do that. Um
[35:01] what do people want to
[35:04] see for the last 20 minutes? Let's see
[35:07] here. Let me run the triager agent.
[35:10] Okay, there was I think there were some
[35:13] issues with triagger triager. py.
[35:30] All right. So, what is it doing now? It
[35:33] is uh trying to find a stale issue to
[35:36] triage. You can see these are the tools
[35:37] it's using and it's it's reports like
[35:40] that it's using this sub agent in one of
[35:42] the tools and you can see the tool name
[35:46] is just bash for a lot of this um
[35:49] because I think it's running the GitHub
[35:50] CLI. I've tried to get it to use the
[35:52] GitHub MCP server but it seems
[35:56] very unwilling to use the GitHub MCP
[35:59] server. Um, I don't, this is a general
[36:02] issue I'm having right now is that it
[36:04] seems the cloud models in particular
[36:07] seem to really prefer using the CLI
[36:09] versus the MCP servers and um, you know,
[36:12] it it makes it a little harder to
[36:14] understand what they're doing.
[36:18] Uh, so there are memory tools you can
[36:20] add to GitHub Copilot. Would you want to
[36:22] use an additional memory provider? I
[36:25] haven't tried adding I did actually
[36:26] experiment with memory today in copilot
[36:28] because I got really annoyed. Uh so this
[36:31] copilot right so here you can see okay
[36:34] so I got so I was looking for that
[36:36] diagram right uh so I was in like work
[36:39] mode and I was trying to find the
[36:40] diagram it did eventually find it which
[36:41] is good but then then it said TL let me
[36:45] get this bigger so you can see um
[36:49] we'll pop it out.
[36:53] Okay. And then it's all the chat history
[36:58] is always like outdated. I always have
[36:59] to do like a hard refresh. Okay. There
[37:02] we go.
[37:04] Um,
[37:06] okay. So, here we go. And it said if
[37:09] someone said Pam's deck with the cloud
[37:11] ingestion pipeline diagram. The thing is
[37:14] that I hate the name Pam. And so then
[37:19] that's funny. It actually lost it. I
[37:20] think there's something I don't know the
[37:22] way they coded co-pilot like sometimes
[37:24] they just lose messages but I told it
[37:26] remember this is basically what I said
[37:28] remember to never call me Pam only call
[37:32] me Pamela right so I wrote a message
[37:33] like that I don't know why it's not
[37:35] showing it anymore it just forgets
[37:36] sometimes um but then if you look at
[37:39] settings and then look at
[37:41] personalization and memories manage save
[37:44] memories then you can see what it it
[37:46] remembered and it it did actually like
[37:48] if you ceue it up with remember then it
[37:52] will it will save that memory. Um I and
[37:56] this is the first memories I are ever
[37:58] saved. I have had a lot of conversations
[37:59] with it and it hasn't saved any other
[38:01] memory. So I think you really have to
[38:03] ceue it up using um remember
[38:10] uh yeah so the memory question. So I
[38:13] haven't tried uh let's see we can do
[38:16] insiders.
[38:17] Uh, so presumably you're using like a
[38:20] memory. Are you using an MCP server for
[38:23] memory? Let's see. Go here. MCP servers.
[38:27] Uh, memory.
[38:30] There's context stream MCP server.
[38:35] It's a MPX one.
[38:38] Uh, do you have one that you like? This
[38:39] one only has 17 stars, which concerning.
[38:44] Um
[38:46] yeah, I have used skills. I can show you
[38:48] some of my skills. Um
[38:52] so the other repo, uh I was just using I
[38:56] just added a new skill today. Uh dot dot
[39:00] office hours writeups. Okay. So this is
[39:02] the repo where uh when we after these
[39:04] office hours I I generate writeups and
[39:08] then um post lots of post lots of
[39:11] things. Um, so it does lots of things.
[39:15] It it makes like a whole writeup. It
[39:17] makes a bunch of questions and answers
[39:18] to post to the forum. Uh, here I can
[39:21] show you the there right here. Okay.
[39:25] So, it makes all of this, right? Like it
[39:28] makes this list. It makes it posts every
[39:30] question. So, every question that's
[39:31] happening now will get posted as a
[39:34] question here. And then it even has like
[39:36] a time stamp, right? So uh so that's
[39:39] quite nice I think because if we do get
[39:41] the same questions across across
[39:42] repeated weeks then in theory we can
[39:45] just you know point at um you know point
[39:48] at this one right and and remember and
[39:50] last week we did cover the fact that Den
[39:52] left Microsoft to join anthropic and we
[39:55] we have the new maintainer here right so
[39:57] I really like this because I I like you
[39:59] know that once we've learned something
[40:01] like that to share the learnings with
[40:02] the world and um I'm realizing that LLM
[40:05] are making it very easy to go from video
[40:08] to text. So I did the same I also did a
[40:10] write up today of the live you know I
[40:13] was saying the live stream from
[40:14] yesterday I also you know I was able to
[40:16] so that's what makes me skills is that
[40:18] originally I made this repo to write up
[40:21] office hours but then I did that live
[40:22] stream yesterday and I was like oh I
[40:24] kind of want to write up of that one too
[40:25] but I like I was able to customize it
[40:27] and say hey I really need a list of
[40:28] issues to report to the GitHub team. So
[40:31] then here we have GitHub copilot issues,
[40:34] right? So I basically I went through
[40:36] this right up afterwards and and um sent
[40:39] all of these to the GitHub team, right?
[40:41] So that's the nice thing about skills is
[40:42] like you can use them for your you know
[40:45] your your standard workflows, but also
[40:47] like if you have something that's kind
[40:48] of similar that can use the same skills,
[40:50] then it becomes easy to just re reuse
[40:52] them. So here I've got a skill that can
[40:56] grab the live chat transcript because I
[40:58] was grabbing it from yesterday's and you
[41:00] know it just uses some Python package.
[41:02] I've got the YouTube transcript one
[41:04] that's using another Python package to
[41:06] grab the transcript. I've got the
[41:09] discussion commenter that can go and
[41:10] post each of the questions and answers
[41:13] as comments on the QA.
[41:16] So, I'll probably just, you know, keep
[41:18] adding to that um to those skills. And
[41:23] um and then I also usually modify the
[41:26] agents.mmd to give it kind of hints
[41:28] about what skills to use. Right? So, for
[41:30] here in the agents.md
[41:32] it says like, oh, use this skill and
[41:34] then use this skill, right? So, I want
[41:36] to give it as much
[41:38] um you know, ideas as possible. And then
[41:41] the readme has suggested prompts. But
[41:43] then I also added these prompts too. So
[41:48] that if somebody want to, you can just
[41:49] do slash and then you know uh do the
[41:54] prompt. Um so I I I think you know I'm
[41:58] I'm really liking skills for that. I
[42:00] made another repo based off of that one
[42:03] that I'm using to turn um talks into
[42:06] presentations.
[42:08] Uh let me share
[42:10] let me share that this repo it has
[42:13] slightly different skills
[42:15] in it. Um actually for this one I didn't
[42:18] use skills. So that's interesting is
[42:19] that like yeah when do you use skills
[42:22] versus when do you write a script? In
[42:23] this one I decided to write a script
[42:25] because I wanted to have it be more of a
[42:30] standard flow but I pointed it at the
[42:32] skills I used in the other one. So
[42:34] basically like took the skills and just
[42:36] turning scripts. So this is what's
[42:37] interesting here is that you know when
[42:39] you're just doing stuff to automate your
[42:40] own life at this point it doesn't
[42:41] matter. You can pick whatever form of
[42:45] programmatic manipulation you want,
[42:47] right? Do you want a custom agent? Do
[42:49] you want a bunch of skills with prompts?
[42:51] Do you want to just do a Python script?
[42:53] Do you want an agent that's using a
[42:54] fancy agent framework? Right? Like you
[42:57] have all of those options now. So, like
[42:59] for this one, I decided like, oh, I'm
[43:01] going to, you know, I'm gonna have a
[43:03] Python script, and the Python script is
[43:05] going to go through each of these steps
[43:07] because I always have this standard, you
[43:08] know, standard set of scraps steps, and
[43:10] I want to be able to run these on like
[43:12] lots of lots of files, right? Um, and
[43:14] it's it's just I'm just really impressed
[43:17] with um how it can take just, you know,
[43:22] a slide slides and a transcript and it
[43:25] does such a good job
[43:27] um you know turning it into a write up,
[43:30] right? So this was a write up of our
[43:32] Ignite talk. Um and you can see we have
[43:35] all the slides and it has timestamps for
[43:37] each of them too. So, it figured out
[43:39] like the LLM figures out the slide the
[43:41] slide timestamp alignment and it does it
[43:44] so easily and that shocked me because I
[43:46] always thought that timestamp to slide
[43:49] alignment would be a really difficult
[43:50] problem and I had all these like
[43:52] algorithmic ideas of how I would do it
[43:54] using like a binary search like I had
[43:56] all these ideas and then instead I just
[43:58] threw all the you know images and the
[44:00] you know YouTube transcript and boom it
[44:03] just figures it out right so it's
[44:05] definitely worth you know just trying
[44:07] things and seeing, you know, what it
[44:10] does really well. Now, the funny thing
[44:11] is sometimes it'll do so poorly at. So,
[44:13] for example, I really wanted to have um
[44:17] I wanted the casing of the headings to
[44:20] be this is what's called sentence case
[44:22] where you have a capital letter and then
[44:24] the rest is lowercase.
[44:26] But LLM's always love to do title case,
[44:29] which is where like every single letter
[44:31] is capital like this one. I mean, this
[44:33] one is on purpose because this is an
[44:35] acronym, but they love to do that. And
[44:37] so, I spent so much time trying to get
[44:40] the LM to output sentence case instead
[44:42] of title case, and I could not get it to
[44:45] do it. And and instead of doing sentence
[44:48] case, it would just do everything
[44:49] lowercase. Like even the word AI became
[44:51] lowercase AI. And I was like, no, no, I
[44:54] just want it to be sentence case. Why is
[44:58] it so hard? Um, so the nice thing about
[45:01] having a script is that I actually did
[45:03] post-processing. So after the LM
[45:06] generated the headings, I did
[45:07] post-processing um just using Python to
[45:10] then write the table of contents at the
[45:13] top and uh and make sure all the the
[45:16] headings were the way I wanted them to
[45:18] be, right? Um so you know that's the
[45:21] funny thing is you never know what's
[45:22] going to be really easy for a model and
[45:24] what's going to be really hard.
[45:26] Okay. Um, yeah, you have customers
[45:28] asking when you should use Foundry IQ
[45:30] retrieval agents with sources like
[45:31] Elastic versus using Elastic MCP tool as
[45:35] an example. So, wrapping a knowledge
[45:38] source in Foundry IQ versus using a
[45:41] knowledge source outside of Foundry IQ.
[45:43] Okay. Well, when you use the term
[45:44] knowledge source,
[45:46] that does sound like, you know, like
[45:49] you're you're using a Foundry IQ agentic
[45:52] um agentic knowledge base. Let me find
[45:55] my uh environment for that. Um just so I
[45:59] can show what I'm
[46:01] talking about.
[46:06] Aentic. Okay.
[46:11] All right. Let's just look at
[46:15] found. So foundry IQ is basically it's
[46:19] basically Azure Azure AI search. Um
[46:22] maybe it'll get renamed or who knows. Um
[46:26] but Foundry IQ is like when you go to it
[46:28] in Foundry, it's basically wrapping on
[46:30] top of the Azure AI search uh uh
[46:34] capabilities. So if we go and we find
[46:37] our search service here, here we can see
[46:40] we have knowledge sources
[46:42] and then we have knowledge bases. So a
[46:45] knowledge base is a basically like an
[46:49] agentic engine that can be connected to
[46:53] different knowledge sources and it can
[46:55] do query planning. It can do answer
[46:57] synthesis. Um it can do it'll do like
[47:00] the full hybrid search with semantic
[47:02] ranking, semantic classification. It can
[47:03] even do like a second step of iteration.
[47:05] It just depends on how you configure it.
[47:07] But you know it's like a basically an
[47:08] agentic search over potentially multiple
[47:11] knowledge sources. When you have
[47:12] multiple knowledge sources, it can it
[47:13] can decide if you want to it can try to
[47:16] decide which sources to use if you think
[47:18] there's some cases where it's only going
[47:20] to use one source versus the other. Um,
[47:22] so anyway, so then we have knowledge
[47:23] sources, right? And there's different
[47:25] kinds of knowledge sources.
[47:28] So here you can see that it only shows
[47:31] search index and Azure blob. But um, you
[47:36] said MCP. Now here's the thing is that
[47:38] MCP
[47:40] is a kind of knowledge source in private
[47:43] preview.
[47:44] So um
[47:47] if you wanted to you could try
[47:50] um you could you know you can get you
[47:53] can ask for access to that private
[47:54] preview and you could try the um the
[47:58] elastic MCP as a knowledge source here.
[48:01] Now this is all assuming you're talking
[48:02] about like you know using Foundry IQ
[48:05] with knowledge sources this way. It's
[48:07] possible you're like talking about um
[48:10] some other thing in Foundry. So then
[48:13] I'll have to log into Foundry and um see
[48:16] what else is
[48:18] uh what else
[48:20] uh Foundry refers to. Let's see. Let me
[48:22] just try and find a Foundry
[48:25] Foundry.
[48:30] Oh, I am answering your question. Okay,
[48:32] good. All right. So, I did go through a
[48:34] foundry tutorial made a foundry foundry
[48:37] project. Okay.
[48:39] Uh go to foundry portal. Okay. So, yeah,
[48:41] if you are talking about this kind of
[48:43] agent then um MCP is a kind of knowledge
[48:47] source that's in private preview. Let me
[48:49] get our slides about it. Let's see.
[48:50] Build agents.
[48:52] Probably this one.
[48:55] I always have to remember. Yeah, Ignite.
[48:57] Okay, great. So in these slides we
[48:59] talked about how so these are the
[49:01] knowledge sources right so there's the
[49:03] index knowledge sources like a search
[49:04] index blob one lake shareepoint is
[49:07] interesting because you can set it up as
[49:09] an index knowledge source which
[49:10] basically is copying all your data which
[49:11] you don't usually want to do or better a
[49:14] remote um knowledge source and that's
[49:16] better because then you know you get the
[49:18] ACL's you're not making copies of things
[49:20] then we've got the web and then MCP in
[49:23] private preview so um if you know
[49:26] elastic expose an MCP server then in
[49:29] theory um you should be able to point at
[49:32] it and uh I can connect you to the PM
[49:35] for that.
[49:37] Um and then once you have it then it can
[49:40] just
[49:42] you know send search queries to it and
[49:44] and get back results.
[49:49] Let's see what what does Foundry look
[49:51] like these days? Okay, I think I like
[49:53] going discover
[49:56] tools
[49:58] custom MCP. Oh my, there's a lot of
[50:00] tools now. That's a bit overwhelming.
[50:03] That's too much. Okay, where is it?
[50:05] Build. I think build I build is the one
[50:08] I like. Okay, build
[50:10] tools. Knowledge. Knowledge bases. So
[50:14] knowledge bases we were just looking at.
[50:15] Okay, so here you can see how it's
[50:16] called Foundry IQ. Here it's called a
[50:19] search service. You know,
[50:21] Microsoft loves names. You know, why
[50:26] have one name for something when you
[50:28] could have like four names, right?
[50:30] Sorry,
[50:31] I might be a little bitter about
[50:33] renames, but um yeah, but this is a
[50:35] knowledge base and you we can that's the
[50:38] same um sort of thing, you know, it's
[50:40] just different this is like different
[50:42] UIs for the same thing, right?
[50:46] Yeah. Four non-related names. I I've
[50:48] already written up a long rant about
[50:49] this. Um because in the four as long as
[50:53] I'm ranting in like the what is it I've
[50:55] been here almost four years it started
[50:57] like this service I think went from
[50:58] Azure search to as your cognitive search
[51:00] to Azure AI search to found your IQ. So
[51:02] that is four names. Most of those are
[51:04] related because see that search there
[51:06] foundry IQ
[51:08] is just not not related. So anyway, once
[51:12] once marketing can decide if this is the
[51:15] final name, then we will all learn the
[51:18] new name again and we will love it and
[51:21] cherish it and all of our code will
[51:23] still reference cognitive search because
[51:25] here's the thing is that when you're a
[51:26] developer, uh, a lot of the code can't
[51:29] change, right? When we're doing like
[51:30] bicep, right? Like in our uh, like
[51:33] search services.bicep, right? Um, the
[51:35] bicep arm resources here. So luckily it
[51:39] says search services. So we'll have to
[51:40] just know that we're using search
[51:42] services. So that's the interesting
[51:43] thing is that uh you know Microsoft uh
[51:45] marketing might decide to change names
[51:47] but in the bicep bicep names don't
[51:50] generally change uh they tend to stay
[51:52] say stay the same. So you'll see all
[51:54] this like legacy this leftover names in
[51:57] in your infrastructure.
[52:02] Oh yeah and then the acronyms. That's
[52:03] why you can't use acronyms anymore.
[52:05] Right. So, we went from Azure search to
[52:09] Azure Cognitive Search and I was using
[52:12] um ACS for a while there and then Azure
[52:16] AI search and I never really acronymed
[52:17] that. And then we have Foundry IQ which
[52:20] we could call FIQ except that there's
[52:23] potentially like another like I think
[52:25] fabric IQ I think they said. Anyway, so
[52:29] we can't we can't use acronyms and also
[52:32] it's a weird acronym so no more
[52:34] acronyms.
[52:36] And that is my rant.
[52:41] Uh great. Uh but I do really like
[52:44] knowledge bases. I might not like the
[52:46] renames, but I really like AI search and
[52:48] the underlying technology. Um so I would
[52:50] certainly play around with them. I
[52:51] actually like you know one of the um you
[52:54] see here this Azure docs that is in fact
[52:56] a knowledge base. So my colleague uh I
[52:59] can show you that one actually. Azure
[53:00] docs where is it? Um it should be in our
[53:03] there we go. Um he put in here. So he
[53:08] indexed basically he indexed every um
[53:13] here I'm going to look at my So there's
[53:15] like this MCP config.json
[53:17] uh that has all this stored in it. Um
[53:21] but I also have a key in there so I
[53:23] can't show you it. But let's see foundry
[53:25] foundry projects. Where's the resource
[53:26] group? So he made he indexed every he
[53:30] downloaded so all the Microsoft learn
[53:32] documentation is in a GitHub file. So he
[53:35] downloaded that GitHub zip and then he
[53:38] indexed it using an AI search knowledge
[53:41] base and then um yeah made the knowledge
[53:44] base and let's see is it in here? Just
[53:48] wanted to show the knowledge base
[53:50] because it was cool. Uh I don't see it
[53:53] there. Um here's that's a different one.
[53:57] Um, but yeah, so you could have like you
[53:59] can make a knowledge base because a
[54:01] knowledge base also there is an MCP
[54:03] endpoint for knowledge bases. Uh, I
[54:05] guess it's not documented. Maybe I'm not
[54:07] supposed to talk about it, but there is
[54:08] an MCP endpoint for knowledge bases. So
[54:11] if you make a knowledge base in AI
[54:12] search, you can actually use it as an
[54:15] MCP server. Uh, which is fun
[54:19] and it's it's quite a good server. So
[54:21] yeah, good indexing. Okay. All right.
[54:26] Very good. Um,
[54:30] sweet. All right. Uh, we are at time
[54:34] now. Uh, so I will, uh, do the usual
[54:38] thing. I'll upload the recording to
[54:41] YouTube.
[54:43] Crop out anything I wasn't supposed to
[54:44] say. No, I think I'm good.
[54:47] I'll up the recording to YouTube. I'll
[54:49] wait for it to generate the transcript.
[54:50] I'll make the write up. I'll post all
[54:52] the questions to that forum. Uh, let me
[54:54] just check to see if we got any
[54:56] responses on our questions today about
[54:58] SP apps. Nope. Okay. Um, so, uh, yeah,
[55:03] if I get any updates, I will, you know,
[55:05] find a place to post them. All right.
[55:11] Thank you everyone for joining as always
[55:15] and I hope you have fun playing around
[55:18] with all the new technology of the week.
[55:21] There is always new stuff to try. I am
[55:24] behind every day of my life. But that's
[55:28] fun. There's more to learn. Bye
[55:30] everyone.
