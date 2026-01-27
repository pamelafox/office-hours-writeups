[00:02] Hello everyone.
[00:04] I am doing a little live stream today in
[00:07] order to play with some new technology
[00:10] that everybody is talking about and I
[00:13] just haven't really had the time to play
[00:15] around with stuff yet. So the two things
[00:18] I want to try out for today's session
[00:20] are the GitHub copilot CLI and I have
[00:24] used this briefly actually when it was
[00:26] not even public. So, I I used it in
[00:28] preview mode and I haven't really used
[00:30] it since, but it has been around for
[00:33] what, six months now or something. It's
[00:35] been around for a while. And newer is
[00:37] the GitHub Copilot SDK. And I think this
[00:41] one's really only been around for maybe
[00:43] a month or so. And it is based off of
[00:46] the CLI, right? It's basically a
[00:48] programmatic interface for the CLI. Now,
[00:51] of course, what I use all the time is
[00:52] GitHub Copilot, right? I use that in two
[00:54] contexts. I use that within my uh you
[00:58] know within VS code that's the way I use
[01:00] it the most and I also use that you know
[01:03] inside GitHub when I am assigning issues
[01:07] to it right you can if you have an issue
[01:10] you can go to the issue Jean's pant
[01:12] that's a great issue um let's see you
[01:16] know you can go to an issue and then you
[01:17] can assign it to copilot and I also have
[01:20] scripts that programmatically assign to
[01:22] copilot so I have used github copilot
[01:24] quite a bit. It is one of my favorite
[01:26] tools. Basically, all my coding now is
[01:28] with Copilot in collaboration. Um, but
[01:31] what I haven't used is the CLI very much
[01:34] at all and I have not used the SDK
[01:37] whatsoever.
[01:38] All right, I see some folks are
[01:40] streaming in. We got Carlos,
[01:43] we got John, we got folks from LinkedIn
[01:46] as well. Hola, buenos buenosene.
[01:51] All right, welcome everyone.
[01:54] All right. So, uh, for those of you in
[01:56] the chat, please do share what
[01:59] experience you have with these tools. If
[02:01] you've been using them for anything
[02:02] interesting, what you like about them,
[02:04] what you don't like about them. I know
[02:06] they're changing all the time, so be
[02:09] good to see. All right, so let's start
[02:11] off with GitHub Copilot. And I don't
[02:13] honestly remember if I even have it
[02:15] installed. As I said, I did install it
[02:17] back when it was in private preview, and
[02:20] I haven't really touched it since. Okay,
[02:22] so we have some options. We've got We're
[02:24] not going to do Windet because I'm on a
[02:26] Mac. We've got homebrew. I don't like
[02:28] homebrew. It stresses me out because it
[02:30] always tries to upgrade lots of things
[02:31] and it has to do with beer and I hate
[02:33] beer. Um, so if I have the option, I'd
[02:37] rather just use the curl script to be
[02:38] honest. So, first I should test to see
[02:41] if I have it. Oh, I was also trying to
[02:43] use work IQ, but that's that'll be in
[02:45] another stream. Okay. Uh, so let's see.
[02:47] Do I have co-pilot?
[02:50] All right. I do have some version of
[02:52] C-pilot. This is 0.263
[02:56] and now we're on 395. So I'm really
[02:59] behind. So probably I need to do a
[03:01] little
[03:03] upgrade. Let's see. How do I control C?
[03:06] Okay. Control C again. All right.
[03:11] First thing in a CLI. How do you exit?
[03:15] Okay. So you have to press control C
[03:17] very rapidly in succession.
[03:21] John says, John says, "Oh, yeah. Yeah."
[03:24] Okay. Yeah. So, we're starting with the
[03:27] CLI. Just making sure I have that
[03:28] installed. Um, so let's see. If I run
[03:32] the curl, is that going to upgrade it?
[03:33] Let's find out. All right. Downloading
[03:37] for ARM 64. Looks good. Okay. Let's
[03:40] let's test to see what version we're on
[03:42] right now. Um, so let's see. Copilot
[03:46] help. Okay, that didn't show the
[03:49] version. Let's do copilot
[03:51] now. Uh, it still says 0.0263.
[03:57] So, I think we're going to control C and
[04:02] maybe we need to
[04:05] let's see, maybe we need to upgrade that
[04:09] somehow. Or maybe when I installed it
[04:12] before I problem is I don't know how I
[04:15] installed it before. Um,
[04:19] co-pilot ready. Let's try this. Copilot.
[04:22] Do I trust the files?
[04:25] Uh, I don't know if I want it to trust.
[04:27] Okay.
[04:30] All right. Let's make a directory
[04:31] co-pilot experiments.
[04:34] It's kind of nerve-wracking giving it
[04:36] aspect. I giving it access to
[04:38] everything. Do I trust the files? Oh, it
[04:40] still wants to trust. Oh, I got a CD
[04:44] into it. Okay. CD copilot experiments.
[04:48] All right. And then copilot.
[04:52] Do I trust the files in that folder?
[04:53] Yes. Okay. All right. Check where I
[04:57] installed the C-Pilot SDK. I want to
[05:02] upgrade it. All right. This is very
[05:03] meta. We're using Copilot
[05:06] CLI in order to upgrade the Copilot CLI.
[05:12] Let's see. Oh, it's trying to do which
[05:15] GH. No, we don't care about which GH. We
[05:17] care about C-pilot. Um, do you want to
[05:21] run this command? Sure, I don't care.
[05:23] Uh, npm list. I run this command. Check
[05:26] for Python packages. No, I you know what
[05:29] I should do is give it access to these
[05:30] docs. Then it would be able to do it
[05:33] better. All right. And
[05:37] uh Oh, it did find. So, I must have done
[05:39] it with mpm before. That's the issue.
[05:42] Okay.
[05:43] Uh, yes. All right. How do I Okay, I'm
[05:46] going to like escape out of this. Okay,
[05:49] I'm cancelling. And then I'm going to
[05:51] say read the docs at
[05:56] as it will give you info on
[05:59] installation.
[06:03] All right,
[06:05] model call failed. Great.
[06:09] I did hear there were some issues on
[06:10] insiders today.
[06:12] um with
[06:14] a a prompt too long error. I don't know
[06:17] what model it's for it's using. Of
[06:19] course, this is the old version of the
[06:21] CLI.
[06:22] All right. So, it looks like I did use
[06:24] npm before. So, let's just let's just
[06:28] try the npm technique and see if that
[06:31] will override what's in my path, right?
[06:34] Because I think right now,
[06:36] okay, it exists. All right, we are going
[06:38] to overwrite files recklessly. Ready for
[06:41] this? Let's overwrite those files
[06:43] recklessly. Um, recommended. Okay, added
[06:47] two packages. All right, let's try it
[06:49] again.
[06:56] All right, there we go. GitHub copilot
[06:58] 0.0395.
[07:00] Pick a model with slashmodel. Delegate
[07:02] changes when they using delegate. Enter
[07:05] question mark. See all commands. Staff
[07:07] mode activated.
[07:10] Now, presumably staff mode is only for
[07:13] those of us at Microsoft or I'm I'm also
[07:16] now technically at GitHub. I'm at
[07:18] Microsoft and GitHub somehow. I don't
[07:20] know. Something like that. I work for
[07:22] everyone. I work for the world. Uh so,
[07:25] we're going to confirm Colt the folder
[07:28] trust again.
[07:30] All right. And now you can see we're
[07:31] using Opus 4.5, which is my favorite
[07:34] model even though it has the 3x
[07:36] multiplier. But that makes sense because
[07:38] it is like the best model in the
[07:39] universe. So we're going to stick with
[07:41] Opus 4.5.
[07:43] And great. So now now this is working.
[07:47] Um
[07:49] so now what do we do with it? So now we
[07:52] can just use this the same way we'd use
[07:54] uh we'd use VS Code, right? Um,
[07:58] now this is a fresh directory. So, now
[08:00] that I've got this working, I'm going to
[08:03] move into an existing repo, right? Uh,
[08:07] this one, our rag repo. And this is
[08:10] where I'm, you know, using Copilot and
[08:12] VS Code most time. So, I'm going to
[08:15] trust and remember this for future
[08:17] sessions.
[08:18] All right. Now, something I heard is
[08:20] cool is this is like slash review.
[08:24] Um,
[08:25] what is Let's just see what that I I
[08:27] just saw this uh tweeted about slashre.
[08:30] I don't know what it's going to review
[08:32] my code changes. I was thinking it would
[08:34] review a PR, but okay. It's reviewing
[08:37] whatever the current code is. I heard
[08:39] that with slashre you could actually ask
[08:42] like five different models to review it,
[08:44] which I I thought that was kind of nice
[08:46] is to be able to um have a bunch of
[08:50] models give an opinion. So, let's what I
[08:52] want to do is actually check out a
[08:56] um a
[08:58] branch that I would like a very thorough
[09:01] review on because this one is a really
[09:04] big change. Um this particular change
[09:09] here is not that exciting. Although, I
[09:12] realize this change is incorrect. So, I
[09:13] wonder if it'll catch the fact that it's
[09:15] not a good change.
[09:18] Um so, what is it? All right. So we're
[09:21] doing it's doing a web search web
[09:24] search. So this looks like the tool
[09:25] calls, right? So we can see when it does
[09:27] a tool call and it's doing a little
[09:30] research here
[09:33] and
[09:34] it's trying to look at the the issue
[09:37] that this PR is fixing. All right. And
[09:39] I'm going to say approve all URLs from
[09:42] API to github.com permanently. Okay. Do
[09:45] I want want to run this command curl?
[09:48] And I guess I'll just I'll just say yes.
[09:51] The hardest thing is deciding what
[09:53] things to approve. Like something like
[09:55] fetching information from
[09:56] api.github.com. Sure, you can approve
[09:58] that forever. But approving all Python
[10:01] commands and all curl commands,
[10:03] especially all Python commands, you can
[10:04] do anything with Python. You can delete
[10:06] your entire operating system with
[10:08] Python. Uh so you know when it comes to
[10:11] the Python commands, usually I I will
[10:15] just, you know, approve them uh one at a
[10:17] time.
[10:18] But that's what's really hard about
[10:20] approval, right? And then eventually I
[10:22] get tired of approving and then I just
[10:23] say, "Ah, screw it. Just approve all the
[10:26] commands forever, right?" And then of
[10:29] course I have no security. So I think we
[10:31] still haven't figured out, you know,
[10:34] it's one of those computer harder
[10:36] science problems. How can you look at
[10:37] some code and know if it's dangerous
[10:39] code, if it's risky code? And um, you
[10:42] know, it's hard. Okay, so it says, "One
[10:45] issue found. The revert removes a
[10:47] workaround that is still not fixed
[10:49] upstream. Ah, it figured it out. Yeah.
[10:51] So, I realiz somebody had commented on a
[10:54] previous issue saying I could revert
[10:55] this change, but then I researched it
[10:57] and I was like, "Oh, wait, no, I
[10:58] actually can't." And so, somebody had
[11:00] given me bad information and I made this
[11:02] PR based off that bad information. And
[11:05] luckily, Copilot did the same
[11:07] investigation that I did. They went to
[11:09] the upstream issue. They saw it still
[11:10] wasn't fixed and uh and this is exactly
[11:14] correct. So that's really good. So um
[11:17] that I'm that's a really good review.
[11:20] Now normally you know I could also do
[11:22] the same review like let's do give this
[11:24] assign the same review in this um in the
[11:28] actual
[11:30] UI right and presumably it'll come up
[11:33] with the same conclusion but we can do a
[11:35] little comparison and and see.
[11:39] All right so that's cool. Now,
[11:42] uh, so how do I, uh, check out a branch,
[11:46] right? I guess I'll just tell it to
[11:49] check out the branch. Uh, check out
[11:53] branch.
[11:54] Guess the other thing is we usually I
[11:56] will like start up a new session when
[11:57] I'm doing something different. Um,
[12:00] and
[12:02] uh, I'm not I'll figure out how to like
[12:04] start a new session. Do I want to run
[12:06] this command? I'll approve that going
[12:09] forward.
[12:13] Okay.
[12:14] Uh oh, it wants to pull latest changes.
[12:18] Sure.
[12:24] Uh I'll approve that.
[12:27] It's just a lot of approving. Okay. All
[12:31] right. Now, I want to try now where can
[12:34] we review? Can I do like how do I get
[12:36] help on things?
[12:39] or help
[12:42] help.
[12:43] Okay. All right. Review
[12:47] run code review
[12:51] prompt.
[12:53] But how do we All right. So, we're going
[12:54] to look up try to figure out how to do
[12:56] it. So, the the person to follow on
[12:59] Twitter
[13:01] is uh I think it's Eric Boil.
[13:06] Um here if we go I'm sure we'll find my
[13:10] feed right now is like very much Evan
[13:13] boil. Okay great. So if you're curious
[13:16] about the co-pilot CLI then you should
[13:20] follow Evan Boille
[13:23] and um he often will send messages about
[13:28] anything that is new.
[13:31] Uh, okay. So, we can find like fun
[13:32] things. Slash diff. Uh, run run shell
[13:36] commands in barrel skills as slash
[13:38] commands.
[13:40] Uh,
[13:42] ask user question.
[13:45] Uh, do okay. Review command. Reviewer
[13:48] code with multiple. This is a thing I
[13:49] wanted to see. So, how do we do it in
[13:54] with multiple models in parallel? This
[13:57] is what I want to know.
[13:59] review my code with opus. Oh, so we just
[14:03] tell it. We literally just tell it.
[14:05] Okay. Okay. So, opus 5. Codeex and
[14:09] Gemini. Okay. All right. So, let's try
[14:12] review my code with Opus, Gemini, and
[14:18] 5.2 CEX.
[14:21] All right.
[14:23] So, let's check that out.
[14:26] Hello, Alejandro.
[14:31] Welcome, welcome. All right, so
[14:32] currently Oh, say so what we can see is
[14:34] that it sent it queued up three code
[14:40] reviews. So it's doing like a background
[14:42] agent. Okay, interesting. So this is
[14:44] like a sub agent, which is something I
[14:46] haven't really used in VS Code much, but
[14:48] is a functionality in VS Code where you
[14:50] can have like these sub aents. So this
[14:52] is like a code review sub aent, and it's
[14:55] got an ID.
[14:57] And now I guess it's basically like
[14:59] queuing uh it's running those sub agents
[15:03] in parallel and it looks like it's
[15:05] basically pinging them for progress,
[15:07] right? To check and see um if it's done.
[15:11] Uh okay, I'm just going to approve
[15:15] things. Now I'm going to have to approve
[15:16] commands across three different agents
[15:18] running in parallel. So I'm going to be
[15:20] a little a little more um you know
[15:24] flexible. uh a little a little more
[15:26] willing to approve things.
[15:30] All right, so it's taking a look at that
[15:32] diff
[15:34] and
[15:36] um
[15:38] just doing lots of reviews. Now, the
[15:39] thing is I don't know which I don't know
[15:42] if these updates here are kind of like
[15:45] coming in and we're just seeing updates
[15:47] from all of them at once or if we're
[15:49] seeing updates from just one of them. I
[15:51] don't know exactly, you know, it doesn't
[15:53] say which agent this is coming from.
[15:54] That's a good question. Let me let me
[15:56] take some screenshots so we can ask Evan
[15:58] afterwards. Um, you know how this Yeah,
[16:02] it works. Oh, shift tab psycho mode
[16:04] control DNQ.
[16:06] We can encue something. So, this is a
[16:08] big request that people always have for
[16:10] VS Code Copilot is queuing up. Uh, run
[16:13] this. Sure. Uh,
[16:15] so shift tab. What is shift tab cycle
[16:18] mode? Oh, okay. Uh, okay. Now you're in
[16:22] plan mode. Okay. So, that just goes
[16:23] cycle mode. This becomes goes between
[16:25] plan and agent. So I guess they only
[16:27] have two modes in the co-pilot CLI. One
[16:30] is plan, the other is agent. And that
[16:31] makes sense because honestly I you know
[16:34] never use the edit mode anymore or the
[16:37] ask mode. You you know plan versus agent
[16:40] are really the two significant things
[16:42] right now. Uh let's see. And then
[16:44] control D is NQ.
[16:47] Let's check that out. What happens if I
[16:51] do control D control D?
[16:55] Maybe I have to have typed something
[16:56] like um summarize the reviews across the
[17:00] agents and then it can I press control D
[17:03] and cue it. Okay. Oh, that's cool. Okay.
[17:06] So, I typed a prompt then I said control
[17:08] G and you can see now it is queued up.
[17:12] Okay. Um All right. So then presumably
[17:16] after it does the reviews then it's
[17:18] going to summarize the reviews uh across
[17:22] all of them and we can see so it says
[17:24] it's waiting in like running in parallel
[17:26] but it kind of looks like it's running
[17:28] sequentially right uh so this will be
[17:30] another question for Evan is it truly
[17:34] running in parallel or is it actually
[17:37] running sequentially?
[17:40] Uh, so, uh, yeah, and it's still got two
[17:43] more reviews to go. All right. So, while
[17:46] it's doing that, I guess I kind of have
[17:48] to, this is the issue is that since it
[17:49] has to ask for approval, I'm going to
[17:51] just put it over here so we can see if
[17:52] approval props up. And then we'll go
[17:55] over here and just see what other um,
[17:59] commands there are. Where are the
[18:01] commands?
[18:04] Oh, there's the official documentation.
[18:07] Let me also paste this in here.
[18:10] So you can check out that. And then
[18:12] where's we've got the official
[18:14] documentation
[18:16] about GitHub's copilot CLI. Uh so we can
[18:20] do the things we would normally do.
[18:23] We can use the GitHub MCP server
[18:27] or uh you know anything we can do via
[18:29] GitHub and then we can customize it you
[18:32] know with agents.mmd custom instructions
[18:35] MCP custom agents. Let me see how to use
[18:39] custom agents because I already do have
[18:40] custom agents.
[18:42] So using custom agents, custom agents
[18:46] are specialized versions
[18:49] and when creating your own custom
[18:51] agents, copilot CLI
[18:53] supports loading custom agents from the
[18:55] following location. So we have
[18:56] copilot.agents directory, github.agents
[18:59] agents directory
[19:01] in the local and remote repositories and
[19:04] then an agents directory in the GitHub
[19:07] private repository in an organization
[19:09] enterprise. Interesting. So if you have
[19:11] an organization and you are using the
[19:14] same agents across multiple repos then
[19:16] you can actually make a repo
[19:18] specifically for storing those agents.
[19:22] So that's uh that's quite that's quite
[19:24] helpful I'd say. Uh so let's see. So, I
[19:28] do have I should have a GitHub.agents in
[19:31] here. Uh
[19:34] GitHub/ aagents. Yeah, I've got the
[19:37] fixer agent which fixes open issues on
[19:39] GitHub and then the triagger agent which
[19:41] looks for stale issues and tries to
[19:43] close them. So, it should have access to
[19:48] those agents.
[19:50] Uh let's see. And it's wait two reviews
[19:52] completing waiting for GB 5.2. That's
[19:55] always like the slowest one, isn't it?
[19:57] Uh,
[19:59] so new custom agents can be used in
[20:01] three ways. The slash command. So let's
[20:03] try out that one. Calling out to the
[20:05] custom agent in a prompt or specifying
[20:08] the custom agent with the command line
[20:10] option. Okay. Okay, cool. So I think the
[20:12] next thing we should do is try to use
[20:15] the
[20:17] um the custom agent. And then there's
[20:20] Oh, and then there's also MCP servers.
[20:21] That's pretty fun. Uh, so you already
[20:24] have the GitHub MCP server when you have
[20:26] this. So that makes sense. And then you
[20:29] can add more uh you know like the
[20:31] Playright MCP server. Uh the Microsoft
[20:34] Docs MCP server is a really good one. Uh
[20:37] we should probably add that one.
[20:40] And um okay. And then you can check your
[20:43] usage, you can check your context, and
[20:45] you can compact. So you can tell it when
[20:48] you want to compact your conversation
[20:49] history. Uh it will automatically press
[20:52] when you're getting to 95% of the token
[20:54] limit. uh which is that's a good idea.
[20:57] Uh if you have less than 10 20% a
[20:59] warning will be shown.
[21:02] All right,
[21:03] cool. Okay,
[21:06] so we're still
[21:09] I wonder if I could I could pretty much
[21:11] run
[21:13] I feel like I could just run in the
[21:15] other in another terminal as long as I'm
[21:17] not doing conflicting changes, right?
[21:19] So, let me do copilot over here now as
[21:22] well.
[21:24] And while we're waiting for that one. So
[21:26] now if I do slash, it says that I should
[21:29] see my custom agents here. So let's see.
[21:33] We can see all these things.
[21:38] Slash I don't see Oh, it says browse and
[21:41] select from available agents. Okay. All
[21:42] right. Actually, first let's do an MCP
[21:44] ad
[21:46] and uh unique name uh Microsoft learn.
[21:51] And then
[21:53] how do we do this? It's going to be a
[21:56] ht. Nope. How do I press enter? Oh,
[21:59] okay. Tab, shift, tab, navigate fields.
[22:01] All right. Oops. Oh, wow. I'm not very
[22:04] good at this. Okay. Shift. Nope.
[22:08] Okay. Tab. And then we're going to say
[22:11] it is a HTTP server.
[22:16] And then we need to tab to the next one.
[22:21] and get the URLs. Let me find the URL
[22:24] for the MCP list servers. Okay. Uh
[22:29] Microsoft docs that one. Start configur.
[22:36] Let's just get the information about how
[22:38] to configure that Microsoft learn MCP
[22:42] server
[22:44] because I wanted to have access to that
[22:46] so that it's smarter when it does stuff.
[22:49] Okay. All right, that's it. There's the
[22:52] URL. So, we're going to put in that URL.
[22:55] And we should not need any header. This
[22:57] is a publicly available server. And
[23:00] we'll just give it access to all tools.
[23:02] It only has like two tools anyway. Okay.
[23:04] All right. And then it says controls
[23:06] save server.
[23:09] Control. Okay. Maybe I have to tab.
[23:12] Uh, okay. Tab.
[23:15] Crl S. Nope. Okay. Uh, escape. Ah,
[23:22] okay. We'll try it again.
[23:26] Tab. HTTP.
[23:29] Tab. Remote server URL. Tab. Nothing.
[23:34] Tab. Star. And then Ctrl S. Save server.
[23:41] Maybe it doesn't work with Mac. I'm
[23:44] sorry. I'm pressing control S and
[23:46] nothing is happening. All right. So,
[23:50] that is not working. Um, unless I just
[23:55] really stuck at this. Maybe I'll try
[23:57] command s. Command s. Nope. Oh, that
[24:00] just saved the terminal. Okay. All
[24:03] right. Let's just check if there's like
[24:04] a known issue on on that. Oh. Oh, man.
[24:10] Okay. Now that I'm part of GitHub, it
[24:12] wants me to sign into GitHub. All right.
[24:15] Yay. Okay. All right. So, we're going to
[24:17] not add the MCP server since that is not
[24:20] working for me. Okay. All right. So, we
[24:23] have it open. Let's go check over here.
[24:26] Uh, it still wants to run commands. It's
[24:28] still doing the review. All right. So,
[24:30] over here, I'm going to try the agent.
[24:32] And we can see it can do default, which
[24:34] is just the agentic mode. And then these
[24:36] are my two custom agents, fixer and
[24:38] triagger. So, we'll try triagger. And
[24:41] I'll say find one stale issue to close.
[24:45] All right. So uh I can show you the
[24:50] uh command for that over here. So this
[24:52] is the triagger agent and it has access
[24:57] to all these built-in tools as well as
[24:59] the GitHub MCB server and it should in
[25:02] theory have access to the Microsoft
[25:03] learn server but we weren't able to set
[25:05] that up so it probably won't be able to
[25:07] use that unfortunately.
[25:09] Um
[25:11] I wonder if it gets the same prefix.
[25:13] Okay, that's another question I have.
[25:15] I'm going to have so many questions for
[25:16] Evan after this. All right. Um, so, uh,
[25:20] so you can see that what it does is it
[25:23] says to search for stale issues,
[25:26] examine each issue, search docs, and
[25:28] then recommend which issues to close.
[25:33] So, it found one um,
[25:37] and it says hash conflict.
[25:42] Okay.
[25:44] Yeah, I've only seen this issue once
[25:48] and okay. Suggested closing this hash
[25:50] was reported and the infra have
[25:51] undergone the current.
[25:54] Okay. Yeah, that sounds good. So, yes,
[25:56] please reply and close.
[26:00] Okay, so it's going to go and close it.
[26:03] We can go ahead and look at the issue
[26:07] and see
[26:10] that it should be closing it
[26:14] shortly.
[26:17] And let's see if it's doing it. Okay.
[26:22] Interesting. Uh I don't have Oh, it
[26:26] doesn't have the capability to close
[26:28] issues or add comments through my
[26:30] available GitHub tools. Well, that's
[26:32] weird. because my agent does have access
[26:35] to do it. All right. So, we have another
[26:39] question
[26:40] for for Evan, which is, you know, I've
[26:45] given this agent access specific access
[26:48] to the ability to close issues, but it
[26:50] seems like the agents are not paying
[26:54] attention to the loud tools here and
[26:56] they're using kind of their own tools.
[26:59] So um that's so that's not so good.
[27:05] So I will ask about that as well. Okay.
[27:09] Interesting.
[27:13] There must be some sort of configuration
[27:14] where you can like
[27:17] there. Yeah. So there's something I need
[27:18] to understand about how to work through
[27:20] that. All right. So it is still okay.
[27:24] Great. All right. It finished the code
[27:26] review. Woo. This is fun. Okay.
[27:30] All right. Two reviews completed. JD5.
[27:32] Here's the completed reviews. Quad opus
[27:35] incorrect
[27:37] variable for ACL feature flag. Uh so
[27:42] you know we did were going back and
[27:43] forth about the MVARS. So I'm not
[27:45] surprised that there's some question
[27:46] about that. Uh I see. Yeah, this is
[27:51] probably correct. Okay. And then Gemini
[27:53] code review performance risk from
[27:54] repeated client instantiation.
[27:58] Uh that could be a good point as well. I
[28:02] like it. Uh just some performance tip
[28:05] here. Bio owner excluded.
[28:09] I think we did this on purpose, but I
[28:10] will check that with my other
[28:13] maintainer. GBD 5.2 codeex re is still
[28:16] running. Okay. GBD52 codeex is too slow,
[28:20] so we're just not going to use it. But
[28:22] this is this is really cool here. Um I
[28:25] love I wish I could do this in the
[28:26] GitHub copilot interface too is assigned
[28:29] to multiple models because they all they
[28:32] like you know both Gemini and Opus came
[28:34] up with legitimate things and I'd rather
[28:36] have more
[28:38] feedback
[28:40] than less feedback when it comes to
[28:42] critical PRs like this. So now after
[28:45] this I can go and um take action take
[28:48] action on these
[28:51] All right. So, yeah, John says the CLI
[28:53] has its own tools, not the same as VS
[28:56] Code tools. Yeah, I think I mean, you're
[28:58] right. It seems to, but you know, if I'm
[29:01] I feel like the I think we need a
[29:03] resolution for that because uh you know,
[29:05] I'm going to be a lot of developers are
[29:08] using the same repo across both VS Code
[29:10] and CLI. And ideally, like if I'm able
[29:13] to use this agent.m MD in VS Code, I
[29:16] should be able to use that same agent.
[29:18] MB and Copilot CLI and and actually take
[29:21] advantage of this um you know of it
[29:24] knowing you know I whitelisted these
[29:25] tools for a reason. I was very very
[29:27] specific with this list of tools. So I
[29:29] really wanted to be able to um you know
[29:33] pay attention to those tools.
[29:35] Uh okay. All right. So we've used the
[29:38] CLI for you know the first half of this.
[29:42] So now I think it's time to move to the
[29:44] SDK.
[29:47] Uh, so the copilot SDK, here we go.
[29:53] It wraps on top of the CLI and we have a
[29:57] Python SDK.
[30:00] So, we can just
[30:03] go let's do let me go over to the repo
[30:07] and I'm going to check out main
[30:11] and then uh let me actually let me do
[30:14] this over here. get status. Okay, let me
[30:17] just pip install it without adding it to
[30:19] my requirements. So, I'm just going to
[30:20] do a pip install of the SDK.
[30:25] Here we go.
[30:28] Here's our SDK. Let's just make a new
[30:30] branch for this um SDK
[30:33] experiment. All right.
[30:36] Okay. So, let's see. We have the copilot
[30:40] CLI. So, that should be good. We have
[30:42] our preferred SDK. And then it says,
[30:43] "See the SDK readme for usage examples."
[30:48] Okay,
[30:50] I guess this is the readme. The Yeah, it
[30:52] is the readme. So, here we have the
[30:54] readme for Python
[30:56] and
[30:58] uh PR agent managing local files.
[31:03] Okay. All right. I just want the most
[31:06] basic example.
[31:10] Uh you know, my colleague shared an
[31:12] example. So, let me
[31:14] find his example.
[31:18] All right.
[31:22] All right. Let's go ahead and
[31:25] try Oh, okay. Well, John says that the
[31:30] PR visualization example is cool. Okay.
[31:33] It It'll just depress me because some of
[31:35] the PRs are really old.
[31:38] Let's try it. No, it's a good idea. Um,
[31:42] okay. So, let's see. Let's take this
[31:46] recipe here
[31:49] and make a new file
[31:55] PR visualization. And we'll just put it
[31:57] at the root. I feel like people are
[31:59] going to be like adding I guess we'll
[32:01] add it to like our scripts folder,
[32:02] right? This is like a scripts
[32:05] I feel I think people are going to be
[32:07] adding, you know, like Python scripts to
[32:09] their repos that are like automating
[32:10] things that they do like a lot a lot.
[32:13] Um, you know, so kind of like adding
[32:15] skills and stuff like that. Okay, so
[32:17] let's see
[32:19] it. Yeah, these are all just these are
[32:23] all just um type checking issues.
[32:27] This is the problem with having good
[32:28] type checking is that it has a high bar,
[32:32] but it should all work. So, let's try
[32:34] this. So, we're gonna do we're gonna run
[32:38] this example here. Python PR
[32:40] visualization py. Okay.
[32:45] PR visualization. py.
[32:51] Oh, John says he fixed it. John, if you
[32:55] fix those typing errors, you should
[32:57] submit a PR. Have you submitted a PR?
[33:00] Okay, you sent it to me on Teams. All
[33:02] right. Uh, wait, how we already have a
[33:06] bug? Okay.
[33:08] All right. John sent me the good stuff.
[33:10] All right. Let's use John's version and
[33:12] then John, you should send this in a PR
[33:14] if you haven't already. Um, okay. So,
[33:17] going back. That's That's working much
[33:20] better. Okay.
[33:23] All right, John. This version is so much
[33:25] better. Send send a PR for it. You gota
[33:28] always make the world a little bit
[33:30] better. Be the change you want to be in
[33:32] the world. Look at this. There's no
[33:34] squigglies.
[33:36] And I also didn't get this. This looks
[33:38] like a like this looks like a legitimate
[33:40] issue. How is So, what did you change
[33:42] yours to? Copilot client. C-pilot
[33:45] client. Oh, they changed it from taking
[33:48] direct options directly to taking an
[33:50] options
[33:52] class. Okay. So, yeah. So, definitely
[33:55] that code needs an update. All right.
[33:59] So, it is starting analysis. So, we can
[34:01] see. Okay. So, looking at the config
[34:03] here. So, we have co-pilot options log
[34:06] level. Uh, and then we start a session.
[34:09] We're using sonnet. We should probably
[34:11] change that to opus, huh? And then we're
[34:13] saying you are analyzing pull requests
[34:15] for this GitHub repo. Oh, what's the
[34:16] GitHub repo? Is it checking to see where
[34:18] we are right now? Yeah, it is. So, oh,
[34:21] and it's doing it. That's interesting.
[34:22] It is doing it on my fork. I actually
[34:25] would want it to do it on the upstream.
[34:26] So, I need to change that to
[34:29] the um I need to just change that to the
[34:32] upstream because it's not going to
[34:34] really find many PRs on the on my
[34:36] current fork.
[34:38] Uh but okay. So, it's your so at least
[34:40] it should be faster than this. And then
[34:41] the current uh working directory. Use
[34:44] the GitHub MCP server tools to fetch PR
[34:46] data. Use your file to generate charts.
[34:50] All right. And then starting and then
[34:52] ask follow-up questions. Okay.
[34:56] And
[34:57] now
[35:00] uh it hasn't really shown me anything.
[35:03] Is it supposed to show? Okay. So PR
[35:07] Python repo. That' be good. Uh this then
[35:11] let's and generate. Okay. I don't see a
[35:13] chart image unless it did it save a
[35:15] chart image locally. I didn't check to
[35:16] see. Oh, it did. Oh, nice. Okay, great.
[35:20] Very cool. All right. So, here you can
[35:23] see open HPRs. There's only PR three PRs
[35:26] on my fork. So, let's try that with the
[35:30] um
[35:32] with the argument. As John says, you can
[35:34] pass in an argument for
[35:37] uh for the actual repo. So, we're going
[35:39] to say
[35:41] uh we're going to say repo and Azure
[35:45] samples Azure search open AI
[35:51] demo.
[35:53] All right. So, now it's going to be a
[35:56] little fancier. So, we can look what it
[35:57] did before. It checked on the PRs and
[36:01] made this cute chart. And then you can
[36:03] do all sorts of followup. Okay. So,
[36:05] looking again at what it was doing. Use
[36:06] the GitHub sensor file and code
[36:08] execution tools to generate charts, save
[36:10] them to the current working directory
[36:11] and be concise.
[36:13] So then we get events for
[36:17] um for when things happen. So here's the
[36:19] thing is that this copilot SDK is
[36:21] basically an agent framework, right? So
[36:23] if you use lang chain or Microsoft agent
[36:26] framework, identic AI, the this copilot
[36:29] SDK is an SDK for a agentic uh you know
[36:34] for an agent. So we see really like a
[36:37] lot of similarity here like being able
[36:39] to specify the model and the system
[36:40] message um and getting events to say
[36:44] like what's happening like tool
[36:45] execution start assistant message. These
[36:48] are all the kind of events we would get
[36:49] in an agent SDK as well.
[36:53] Uh so we can set up our event handling
[36:57] and uh in this case we're just using it
[37:00] in order to find out you know when
[37:02] things are happening. Uh although I
[37:04] don't really see Did it show any of that
[37:07] before? We didn't see that before. So I
[37:10] wonder if these events are if this is up
[37:12] to date or if maybe they've changed
[37:14] their event types because we didn't see
[37:16] the
[37:18] assistant message or
[37:20] or the gear show up. So I kind of wonder
[37:23] if this might be out of date right here.
[37:25] So then we had starting analysis. Okay.
[37:27] Fetch the open pull request from the
[37:29] last week.
[37:31] From the last week. Calculate the age of
[37:32] each PR and day. Why would it do from
[37:34] the last week if you're trying to see
[37:35] age over time? That does that's weird. I
[37:38] don't know what they mean from the last
[37:39] week. Then generate a bar chart image.
[37:41] Save it. Finally, summarize the P PR
[37:44] health.
[37:46] All right. So, it interestingly it
[37:48] didn't
[37:49] it didn't really give me a summary of
[37:51] the the PR health. So, then here we can
[37:55] see okay now we can see you know 19.
[38:00] This looks like all the PRs. 194.
[38:03] There's about like 36 PRs. 19 29 29.
[38:06] Yeah. So, you can see 19 of them have
[38:09] been open for 180 days. So, I really
[38:12] should close some of them. Um, but I'm a
[38:14] bit of a hoarder, right? Uh,
[38:18] now, interesting thing. Why didn't it
[38:20] summarize? So, ask follow-up question or
[38:22] type exit and then print. I think it's
[38:25] not showing. I feel like it is not
[38:29] showing the message. So, what I'm going
[38:30] to do is say I'm just going to print all
[38:32] the events here, which might be kind of
[38:34] crazy here. We'll just do all the event
[38:36] types just to see um what's happening.
[38:41] PT
[38:43] because I feel like we're missing we're
[38:45] not we're not seeing like assistant
[38:48] message or tool to execution.
[38:51] And I think we're missing something
[38:52] because it should be summarizing the PR
[38:54] health and we're not seeing any of that.
[38:56] Okay. So see here we have pending
[38:58] message, user message, assistant turn
[39:00] start, tool execution start. So also
[39:03] notice that these are these are like
[39:05] Python enume. So instead of like this is
[39:07] a bad idea to ever hardcode a string
[39:09] literal, it's much better if you can um
[39:12] you know have the types. So let's make
[39:14] this even a little bit better and we'll
[39:16] send like a really good PR after. Uh, so
[39:19] session event type. And so then
[39:22] I'm going to find the session event type
[39:26] for
[39:28] um assistant.
[39:30] Let's see what we got here. Assistant
[39:32] message. Okay.
[39:35] And then
[39:38] does that exist too? Okay. So these look
[39:40] better now. They might be exactly the
[39:42] same thing. So
[39:44] um system message. It does look like the
[39:47] same string. Uh, so here, assistant
[39:50] message. So, we should have seen an
[39:52] assistant message here. Um, let me
[39:56] double check what the string was that we
[39:59] were using before. Assistant message.
[40:03] And this is
[40:05] assistant message.
[40:08] So, why
[40:10] maybe there was no Maybe it's the Okay,
[40:12] let's just print out event.
[40:15] Let's just print out the whole event.
[40:18] We should be really doing like
[40:19] breakpoint debugging for this under
[40:22] event.
[40:24] Event data.
[40:26] This is This is so jank, but we're doing
[40:29] it. Okay. All right. All right. Let's
[40:31] just see tool execution start. Now, do
[40:34] we see tool execution start? Yeah, we
[40:35] also see tool execution start. So why
[40:40] oh maybe equal session event type if
[40:44] it's a literal
[40:45] the double equals should work for string
[40:48] equality.
[40:51] Um okay maybe it's a key
[40:54] value check. I mean if you're doing
[40:56] event type and that's a session event
[40:59] type session event type is an enume. Oh
[41:03] session event type is an enume. When
[41:05] you're checking an eneity,
[41:11] it is not a string. I was thinking it
[41:13] was a string literal, but this is an
[41:14] enume.
[41:16] So, if it's an enume then um yeah, so
[41:21] now this should work. Um that's why it
[41:24] wasn't working before because you would
[41:25] have had to do uh like check the dot
[41:28] value, right? And then that would have
[41:30] been the string literal check. Okay, so
[41:32] that code is incorrect. All right. So
[41:34] now I actually think it's going to
[41:37] work because we're checking the enume is
[41:40] equal to the enume.
[41:43] I think that's okay. Let's see. I think
[41:48] that's going to work.
[41:51] Let's try this out.
[41:56] All right.
[41:59] Starting analysis. Great. There we go.
[42:02] Okay. Okay, I'll fetch the open PRs,
[42:04] analyze ages, create a chart, and
[42:05] provide a health summary. Fantastic. So
[42:07] now we can see the tools that are coming
[42:09] in. So report intent. That's looks like
[42:11] what it just used. Bash. It's using a
[42:13] bash tool. Uh it might be good. It would
[42:16] be fun to show the arguments here like
[42:18] uh let's see
[42:22] data dot. What else do we got? Tool tool
[42:25] names.
[42:27] What else is in there? Tool.
[42:30] Tools. Tool name, tool call ID. All
[42:34] right, we'll just have to go and inspect
[42:37] this. Okay, data is data. Data has
[42:43] what else we got here? Tool requests
[42:49] could be that
[42:51] tool tool name
[42:54] tool telemetry tools.
[42:58] I wonder if it's under tool request.
[43:00] Tool request. This is not alphabetized.
[43:04] Okay, there is tool request.arguments.
[43:11] So would that
[43:14] be? Let's try it.
[43:17] print event.data.tool
[43:20] tool request tool
[43:26] dot tool
[43:28] tool requests
[43:35] and then
[43:37] that will give us
[43:39] arguments.
[43:48] Okay, type none. Maybe because it's
[43:50] optional.
[43:53] Okay. If event data tool requests
[43:59] print the Okay. All right. So now let's
[44:04] see what we got. Okay. Now this now this
[44:06] is working. All right. So it fetched uh
[44:09] things. It used bash. I'm guessing it's
[44:11] just using the GitHub CLI given that
[44:13] it's saying it's using bash instead of
[44:15] an MCP server. Uh create a Python
[44:17] script. Okay. It ran bash again, which
[44:20] is probably Python. You really need more
[44:22] to know more than just bash. Let me fix
[44:24] the JSON escaping issue. The chart has
[44:26] been generated. Here's the uh the chart
[44:30] again. Oh, look at that. That is
[44:32] beautiful.
[44:33] Very good. Love it. That's fun. And then
[44:37] it does a health analysis. 34 open VRS
[44:40] with an alarming average age of 317
[44:43] days.
[44:44] Uh 85 are stale, 47 months are critical.
[44:48] There's the o azure oldest PR. All
[44:50] right. I Yeah. Okay. I'm getting shamed
[44:52] here.
[44:54] This repository has a severe PR backlog
[44:57] problem. Uh nearly half the opens are
[45:00] open a year old. They may need to be
[45:01] closed as stale or require urgent
[45:03] review. The maintenance team should
[45:05] prioritize rearing or closing ancient
[45:07] PRs.
[45:11] Oh no, I got shamed. Okay.
[45:14] Um All right. Well,
[45:17] you know, I I guess I I would I'm trying
[45:21] to come up with a defense now, but you
[45:23] know, I'm just a hoarder. All right, so
[45:26] um so cool. So that's working. I do want
[45:29] to figure out toolcar arguments because
[45:31] I think that's going to make it really
[45:32] much more helpful to figure out what's
[45:34] it what is it doing? And I also think
[45:36] it's interesting that I think it's using
[45:38] the GitHub CLI instead of the GitHub MCP
[45:40] server, which makes me wonder why it's
[45:43] preferring to do that. But I also see
[45:45] that in copilot itself. Oh, and let's
[45:46] change this to using a different model,
[45:48] right? We like opus. So I assume it' be
[45:50] like opus 4.5. Is that going to work?
[45:53] Nope. All right. It says it cannot What?
[45:58] Why can't we use opus?
[46:01] That's not cool. Okay, I guess they have
[46:04] really limited. These are the only
[46:06] models we can use. What? Screenshot. Why
[46:09] can't we use any, you know, new things?
[46:12] All right. Okay. Okay, apparently we
[46:14] can't change the opus, so we're not
[46:15] going to do that. Um, but we can try to
[46:17] see arguments. So, let me see if that's
[46:19] the way to see arguments.
[46:24] Okay. All right. So, this time we're
[46:27] hoping to see some arguments. Oh, John
[46:31] says he tried GD5 multiple times and it
[46:33] failed. All right. So, let's see this
[46:35] time. Okay, I'm not seeing arguments.
[46:38] So, that is not the right way to get
[46:39] arguments. So how
[46:41] how do we get arguments? Um
[46:52] so there must be some other way of
[46:53] getting arguments. All right. So that's
[46:54] another question
[46:56] for the SDK team uh as to why we're not
[47:02] getting arguments. All right. So that
[47:04] was PR visualization. Now, let's try it
[47:06] with an MCP server cuz my colleague did
[47:10] give me um
[47:13] an example with an SDK with the MCP
[47:17] server. So, let's try this out.
[47:21] Okay.
[47:26] All right. You can see our billion.
[47:31] Okay. Well, this so far is not looking
[47:33] so good. Let's see. Is it like this?
[47:36] Nope. Uh, copilot client async. So they
[47:40] are using this async thing over here. We
[47:43] are using just co-pilot client. So let's
[47:45] just try going back to co-pilot client
[47:50] and then
[47:52] so why don't we all right so let's check
[47:55] what is the deal with this co-pilot
[47:58] async. Is that something that's in this
[48:01] repo? Maybe it's just the preview
[48:03] version.
[48:05] I don't even see it in this repo. Okay,
[48:09] where did he get it from?
[48:12] Weird. All right, we are going to ditch
[48:14] that.
[48:16] Uh, I'll ask him afterwards. Okay. And
[48:19] to clarify, wait. So, here. Okay. I
[48:22] don't know why he has async because it
[48:24] looks like it is async regardless. All
[48:26] right. So, we're going to do this and
[48:29] then create session.
[48:31] This is really different. Create um a
[48:34] wait client session config. Maybe we
[48:37] just have two different versions of
[48:40] Okay, I'm just going to save this and
[48:41] tell Copilot to upgrade it. So, um
[48:46] MCP
[48:47] example.
[48:50] Uh let's see.
[48:53] upgrade MCP
[48:56] example to use same SDK interface as PR
[49:01] visualization.
[49:06] Oh, so John says they've migrated
[49:08] everything to async only. Yeah. So as
[49:11] John says, we are telling it to follow
[49:12] the working example. That's a great
[49:14] thing to do with VS Code is if you got
[49:16] one thing working, just tell it to
[49:17] upgrade. So um here we go.
[49:22] And we're going to have to change the
[49:23] model because we're not allowed to use
[49:26] that one. So, we're going to do claude
[49:28] on it 4.5. Now, it's happy. And this one
[49:32] is using the work IQ server. Doesn't
[49:35] work yet for me because I have to get
[49:36] added to a special um entra group
[49:40] because of Microsoft things. But I'm
[49:42] just going to okay change the
[49:47] local server to the Microsoft Learn MCP
[49:52] server instead. And we're going to point
[49:55] it at this
[49:57] documentation.
[50:02] And that is going to be an HTTP server
[50:04] in fact. All right. So this is looking
[50:07] good.
[50:09] And we're going to come up with
[50:10] something more interesting or more
[50:13] relevant to learn for it to do.
[50:17] Remote server unit is going to do that.
[50:19] Okay. Yep. It's going to update the
[50:21] configuration here
[50:24] and hopefully figure out the right
[50:25] things. MP server config
[50:29] and we need
[50:32] we are getting
[50:36] a
[50:38] check the high errors we're getting some
[50:42] type check errors here so I think we've
[50:45] changed something
[50:49] so I think my colleague is using an
[50:51] older version of the CLI that had the
[50:53] explicit async command So we're just
[50:56] upgrading to the latest version of the
[50:58] CLI. Uh so
[51:02] it is just going to I like this is
[51:05] basically how it always checks to
[51:06] understand how to work something like
[51:07] from copilot. So it always checks like
[51:10] tries to figure out the types and then
[51:12] it's going to upgrade it. So MCP remote
[51:14] server config. Aha nice. It found it.
[51:18] Copa is really good at looking at the
[51:22] like the Python package in the local
[51:24] environment and just figuring it out.
[51:27] Okay,
[51:29] great. All right. So, we're going to ask
[51:32] um
[51:34] uh to check readme.md
[51:38] and make sure that the information about
[51:44] Azure AI search is correct per the
[51:48] current documentation. So, I'm trying to
[51:50] get it do something that both uses the
[51:51] current repo and which goes out to
[51:56] um which goes out to the learn MCP. So,
[51:59] let's try the
[52:01] uh let's try that example here. MCP
[52:04] example.py.
[52:07] And what we might want to do, so here
[52:10] we're only going to see the final.
[52:13] We're going to see the final response. I
[52:15] think we probably want to bring in the
[52:18] same event handling from PR
[52:22] visualization
[52:23] into MCP example because I we like
[52:26] seeing those tool calls.
[52:33] Okay. Um, all right. Great. Um, oh,
[52:38] well, this is incorrect. So, um,
[52:42] now, all right, so it says check read
[52:44] me. I've updated.
[52:48] Oh, it found something wrong already.
[52:49] Okay.
[52:51] What did it find wrong? Um, oh,
[52:54] interesting. Unfortunately, it is
[52:56] incorrect because this tag has to change
[52:59] with the old name. So, we will undo
[53:03] that. Um,
[53:05] all right. Let's check
[53:08] uh Okay, now what I wanted to do uh
[53:12] let's check the tool calls because we
[53:13] want to make sure it went out to the MCP
[53:15] server. So, now let's run this again and
[53:19] see if it is
[53:23] going out.
[53:26] to
[53:28] Okay, so now we see report intent view
[53:30] web fetch. So web fetch, I'm pretty sure
[53:32] that is from the MCP server, I believe.
[53:38] Uh
[53:39] the product. Yeah. Well, yep. Oh,
[53:42] interesting.
[53:44] That could be that she could be real.
[53:49] All right. It's doing another web fetch.
[53:51] I'm pretty sure web fetch is from the
[53:53] MCP server. Let's see. Microsoft Docs.
[53:56] Uh, there's a Docs fetch. It still
[53:59] doesn't really seem like it's using. We
[54:01] should be seeing Microsoft code sample
[54:03] search, Microsoft Doc set fetch, or
[54:04] Microsoft. So, I haven't seen it make
[54:08] any calls.
[54:10] None of these look like calls to the MCP
[54:12] server.
[54:15] H. Okay, let's see. Do they have any
[54:17] examples
[54:19] that were actually using an MCP server?
[54:24] multiple sessions. Okay, that's using
[54:27] it's claiming it's using GitHub MCP
[54:29] server, but I really feel like it was
[54:30] using the GitHub CLI.
[54:33] Um,
[54:36] maybe we need to explicitly
[54:39] Okay, use the
[54:42] what did we call it? Microsoft Learn. Do
[54:46] we give it a name? Microsoft Learn. We
[54:48] give it like a typing tools timeout
[54:52] header tools type timeout URL headers.
[54:54] Okay. Does it default to all tools?
[54:57] Tools
[54:59] list of tools. Star means all. So maybe
[55:02] we have to
[55:04] I wonder if we have to explicitly say we
[55:06] want tools equals star. Let's try that.
[55:11] Okay. So now we have
[55:14] tools
[55:16] star
[55:19] uh type.
[55:21] Oh, we should be looking at remote
[55:23] server config. Where's remote server
[55:24] config? Remote. There we go. Tools star
[55:28] type http timeout doesn't matter. URL
[55:32] headers. We shouldn't need headers.
[55:34] Okay. All right. Let's see. Use the
[55:36] Microsoft Learn MCP server for
[55:40] documentation lookup.
[55:44] Okay, so let's try that again. And I
[55:49] really want to see it make a call to the
[55:51] Microsoft Learn MCP server.
[55:57] When in doubt, wild card out. Yeah, it's
[55:59] weird because like tools like I don't
[56:01] know. I feel like the default would be
[56:04] allow all tools, but I do also
[56:05] appreciate from a security perspective
[56:06] that you have to explicitly opt into all
[56:08] tools, but it is weird that you have a
[56:11] list of one element and that one element
[56:14] indicates you want all the elephants,
[56:16] but ele elephants. Um, but you know,
[56:20] you know, whatever is the important
[56:22] thing is just to document so that you
[56:23] know, but it is weird like in most other
[56:25] environments by default it's like other
[56:28] agent frameworks by default you get all
[56:29] the tools, right? Okay. So now let's
[56:32] see.
[56:34] Aha, look at this. There we go. Markle
[56:36] learn. So it prefixes it. Here we go.
[56:38] This is really helpful. It prefixes it
[56:40] with the MCB server name here. And then
[56:44] uh this is the actual tool name, right?
[56:46] Like if you looked uh locally, you when
[56:49] I was looking at it here, Microsoft Docs
[56:52] search, it's this one, right? And then
[56:56] yeah, so it did a search, it found the
[56:57] information. Okay, great. So I think the
[57:00] the issue was that you know just that we
[57:04] hadn't done this here. Let me just do
[57:06] just one more double check if we remove
[57:08] that explicit instruction because I want
[57:11] to confirm the issue was that we didn't
[57:13] have tools equals star because that's
[57:14] really important to know that that's
[57:17] required if that is indeed required.
[57:21] So let's make sure that it is there we
[57:24] go. Okay. So that is the issue when
[57:26] you're setting up the tools currently.
[57:28] You have to explicitly opt into the
[57:30] tools otherwise you will get no tools at
[57:32] all. All right. So now
[57:35] now we're it did a tiny little fix here.
[57:41] Um
[57:43] and basic tier one includes 1,000 free
[57:46] semantic requests. Okay. All right. So
[57:48] it fixed something there. I'll check
[57:49] that with the search team.
[57:52] Okay. Um, cool. So that's good. Now the
[57:57] thing I want to see is how once again
[58:00] remember my agent, right? Like can I get
[58:03] it to do the issue triagger agent? So
[58:05] I'm going to uh maybe like cp this one
[58:10] into another example and say um
[58:14] triagger. py. So I really wanted to use
[58:17] the triagger agent. Um,
[58:20] the question is whether you know is
[58:23] there uh agent.mmd? I'm trying to see if
[58:26] there's a spec like can we just point it
[58:30] at of course we're finding their
[58:32] agents.mmd.
[58:35] Can we point it at
[58:38] a
[58:41] Okay. Is there
[58:44] we're just gonna ask co-pilot on this.
[58:45] Is there a specific way to point the
[58:50] co-pilot client
[58:53] at a custom agent in the repo?
[59:02] Okay, doing a little search here.
[59:07] I always like using Copilot to learn
[59:08] more about C-Pilot. Okay, it's done at
[59:10] session creation time. Accept a session
[59:13] conf that includes custom agents. Okay,
[59:15] great. So, we're gonna say custom
[59:18] agents. Create session custom agents.
[59:22] Um, but can I just point it at it? All
[59:25] right, let's see. Can I just point it at
[59:30] an existing
[59:32] agent.md
[59:33] file?
[59:37] Try again.
[59:39] Let's see.
[59:42] Well, we broke its brain. No worries.
[59:46] Let's try it out. All right. So, scripts
[59:50] triagger.
[59:51] So, this time session config.
[59:55] Let's take a look at this session
[59:56] config.
[59:58] And what do we got here? Session ID,
[01:00:02] model tools, available tools,
[01:00:05] uh excluded tools,
[01:00:08] um provider, streaming, MCP servants.
[01:00:11] Okay, this is what we want. skill
[01:00:13] directories disabled skills infinite
[01:00:16] sessions.
[01:00:18] All right, let's take a look at this.
[01:00:20] Custom agent config
[01:00:24] um name display name tools MC servers.
[01:00:28] This feels like I would just be
[01:00:29] recreating
[01:00:31] what I already have.
[01:00:37] I guess I can do a file open. All right.
[01:00:41] Not a big fan of that, but okay. All
[01:00:42] right. Session config. Uh, custom
[01:00:46] agents. All right. I'm just going to say
[01:00:49] add a
[01:00:52] custom agents config to session config
[01:00:56] that sets up
[01:00:59] an agent based off of
[01:01:03] triagger.en
[01:01:05] using file open.
[01:01:08] And but then I have to parse the Ginga
[01:01:11] file.
[01:01:17] Uh there's there's got to be a better
[01:01:19] way to just point it at an existing
[01:01:21] agent. All right, let's keep let me take
[01:01:23] another screenshot so we remember more
[01:01:25] questions for the SDK team. All right,
[01:01:29] so it's finding the agent. It's reading
[01:01:30] the file.
[01:01:32] Um the thing is like this file has a lot
[01:01:35] more in it than just the system prompt
[01:01:36] because it has the front the YAML at the
[01:01:39] top if you look uh all the way up here
[01:01:43] right like the system prompt should
[01:01:45] really just be this part of it but uh
[01:01:48] you know let's it'll probably be okay
[01:01:51] like you know you can stuff nonsense in
[01:01:54] something um name and prompt custom
[01:01:57] agents is a list okay custom agents
[01:02:01] Okay. Okay. But the dot the agent.md
[01:02:05] file has tools in it as well. Shouldn't
[01:02:10] that be extracted out?
[01:02:14] The tree.agent.md.
[01:02:20] This is certainly too much work though.
[01:02:23] There must be a better way of doing
[01:02:24] this.
[01:02:28] Um,
[01:02:29] yeah, it ignored the tools. So we so
[01:02:31] custom Asian config going to this again.
[01:02:34] It takes a name display name. These are
[01:02:37] all things that are in the file. So it
[01:02:39] feels like there's got to be like a
[01:02:41] factory method or something that can
[01:02:42] just say hey here's the file and make
[01:02:45] the agent based off a file. Um
[01:02:50] look at this. Now we've got like
[01:02:52] YAML.
[01:02:57] Well, I'm sure I'll find out soon that
[01:02:59] there's a better way of doing this, but
[01:03:01] um okay, so now we have description
[01:03:03] tools prompt. Now, the thing I don't
[01:03:05] know is like are these tools even in a
[01:03:07] format that they'll understand? Because
[01:03:09] here we're using this like GitHub name,
[01:03:11] like the name spacing that VS Code
[01:03:13] understands with like Azure MCP and
[01:03:15] GitHub. And I'm guessing that's not in
[01:03:18] the format that you know that they
[01:03:21] expect. Um,
[01:03:25] is are the tools prefixed
[01:03:28] in a way that GitHub Copilot
[01:03:32] CLI expects?
[01:03:35] I don't think it's going to really know
[01:03:36] that, but
[01:03:38] All right.
[01:03:45] Uh, John says there Oh, John says
[01:03:47] there's an MCP field. That's a good
[01:03:48] point. There is an MCP field, isn't
[01:03:50] there? Um, MCP servers. Okay. Yeah,
[01:03:54] that's a good point. All right. Uh,
[01:03:58] actually the config accepts
[01:04:01] MCP
[01:04:03] servers. Is that what it was? MCP
[01:04:05] server. MCP MCP servers
[01:04:10] parameter. So I think we add them there
[01:04:15] with the right name space.
[01:04:19] Oh, but you know the other issue though
[01:04:20] is that in here we use a slash, but the
[01:04:23] GitHub copilot CLI doesn't use a slash.
[01:04:25] So yeah, we're going to it's going to
[01:04:27] transform. Um I think it's going to do
[01:04:30] the transformation though. It it can it
[01:04:32] could do that itself in Python.
[01:04:33] Obviously, this is like way too much
[01:04:35] effort, right? Um
[01:04:38] let's see if it did it with the tools.
[01:04:41] Do we need to map slash to underscore?
[01:04:48] Let's see.
[01:04:59] Okay, John said add the tools up there
[01:05:02] and add MSV to give the MSV server
[01:05:04] source. Yeah. So, we do GitHub, but I
[01:05:06] remember that the CLI when it showed the
[01:05:08] tool name, it was doing like GitHub
[01:05:09] underscore and like, you know, Microsoft
[01:05:11] underscore versus this one, the slash.
[01:05:15] So, I think here when it does the tools,
[01:05:18] yeah, it has to replace the slash with
[01:05:20] the underscore. I think this is my
[01:05:25] this is what it seems like. Um,
[01:05:29] but we'll see. So, we say MCP servers
[01:05:34] Or maybe it won't matter if we're only
[01:05:36] doing
[01:05:38] what we say tools.
[01:05:40] H
[01:05:44] tools. Yeah, the question is how is the
[01:05:46] tools question? How do these need to be
[01:05:51] name spaced for MCP servers?
[01:05:57] Okay.
[01:05:59] Um,
[01:06:01] okay. Let's test.
[01:06:04] All right. Now,
[01:06:06] we are going to
[01:06:10] try this out.
[01:06:14] Fingers crossed.
[01:06:17] Oh, John says to do tools equal. All
[01:06:19] right. Yeah, we could just do that.
[01:06:20] Maybe we should just do that. Tools
[01:06:23] equals. Is that going to give I'm Okay.
[01:06:27] The question is whether we should do
[01:06:28] this. tools equals
[01:06:33] that. Is that going to be all tools from
[01:06:36] all the MCP servers? Oh, you mean here?
[01:06:38] Oh, we got to do it from here. Oh, thank
[01:06:40] you. Yeah, yeah, yeah, we got to do it
[01:06:42] here. You are correct. We already
[01:06:45] learned that lesson. I think everyone's
[01:06:47] going to mess that up over and over and
[01:06:49] over because I haven't seen that in any
[01:06:51] of the other agent frameworks.
[01:06:55] I'm going to run Copilot. uh over the
[01:06:58] transcript of this live stream later and
[01:07:01] like use it to generate all the feedback
[01:07:03] for the co-pilot team. All right. So,
[01:07:06] what is it doing here? So, currently
[01:07:08] we're only seeing builtin.
[01:07:11] Um, so I think it's not
[01:07:15] Oh, wait, wait. It has a Okay. No. What
[01:07:17] are you doing? Uh, blah, blah, blah.
[01:07:20] Okay. No, I wanted to just find a stale
[01:07:24] issue to triage
[01:07:27] prompt
[01:07:29] custom agents.
[01:07:32] Where do we do the prompt prompt promp
[01:07:33] prompt prompt prompt
[01:07:35] co-pilot custom agents
[01:07:38] and message option prompt. All right.
[01:07:43] Okay, there we go. All right.
[01:07:47] All right. Find a stale issue to triage.
[01:07:51] Let's see if it uses either any of these
[01:07:53] servers. Triagger.
[01:07:55] Okay, it says it's using Oh, wait. Look.
[01:07:58] This is It said it'll use the triagger
[01:08:00] agent.
[01:08:02] So, we didn't Oh, okay. So, it sees that
[01:08:05] it has to use a Trager agent. Maybe we
[01:08:07] didn't have to configure. No. Okay.
[01:08:09] Yeah, it's using the Trager agent.
[01:08:12] Um, and I think that came from here, not
[01:08:15] from the repo itself. We could try
[01:08:18] disabling the custom agent entirely and
[01:08:20] seeing if it'll use a tree agent. That's
[01:08:22] another thing to try. Um, okay. It is
[01:08:25] not using any of the MCPS tools. Look at
[01:08:27] this. View, view, view, view, view,
[01:08:29] view, view. What is view? Okay, it's
[01:08:31] using GitHub CLI. It's not using
[01:08:35] it's not a view. We really got to figure
[01:08:36] out how to get those tool car arguments.
[01:08:38] Like, what is this view? The stalebot
[01:08:40] workflow. View view.
[01:08:45] All right, let's try
[01:08:47] what if we just do tools equals star on
[01:08:50] here too
[01:08:55] suggested closing reply
[01:08:58] and is it actually going to do it now?
[01:09:01] Let me use the GitHub CLI
[01:09:04] and then it just closed the whole thing.
[01:09:06] Okay.
[01:09:08] Um add an input loop to triagger.py py
[01:09:14] so I can
[01:09:17] communicate with the agent
[01:09:20] check um PR example
[01:09:24] you have to really want to um
[01:09:30] it has to be worth it to use the you
[01:09:33] know the SDK if you're going to be doing
[01:09:34] like a iterative agentic flow because
[01:09:36] you have to reimplement
[01:09:38] you know talking in a loop with your
[01:09:41] agent right now luckily we can just keep
[01:09:43] on following our example. Um, and
[01:09:47] you know, that's okay. Uh, I'll get rid
[01:09:50] of the examples. Okay. Keep. All right.
[01:09:53] So, hopefully that works. And then, and
[01:09:56] then, yeah, we're really trying to get
[01:09:57] it to use
[01:09:59] the
[01:10:01] MCP servers.
[01:10:05] Uh, John says, did I provide a repo? Um,
[01:10:07] the repo is already in here. I baked it
[01:10:09] into this one. So find the specified
[01:10:11] number in the Azure sample. Yeah. So it
[01:10:13] should know um from that system prompt
[01:10:17] if it's using a triagger agent. Right.
[01:10:19] So we can see report intent triagger.
[01:10:25] Uh the thing that's
[01:10:29] interesting okay I see a blank message.
[01:10:32] Bash bash bash bash
[01:10:38] MCP servers
[01:10:41] GitHub MCP servers.
[01:10:46] It's just
[01:10:48] who needs a GitHub MCP server when
[01:10:50] you've got Bash, right?
[01:10:53] Why is it not? It should be able to
[01:10:55] Maybe it just doesn't want to use the
[01:10:57] GitHub MCP server and it doesn't want to
[01:10:59] use the Microsoft MCP server because it
[01:11:01] may not you need to use this server for
[01:11:03] anything. Um, yeah. So, John asked, did
[01:11:06] I provide the GitHub MCP server config?
[01:11:08] I did in here in the custom agent
[01:11:10] config, right? But it's just not wanting
[01:11:14] to use it. See, we get these like blank
[01:11:16] messages. There's something happening in
[01:11:17] these blank messages.
[01:11:20] Um,
[01:11:27] we could also try putting these MCB
[01:11:29] servers at the global level,
[01:11:32] which
[01:11:34] I wanted. So, really what we want I just
[01:11:36] want it to exactly mimic. It really
[01:11:38] seems like there's a disconnect between
[01:11:41] these agent files and what the C-pilot
[01:11:43] CLI expects.
[01:11:46] And so I just think I think I need to
[01:11:48] dig into this with the, you know, with
[01:11:51] the co-pilot team and um figure out, you
[01:11:55] know, why there's this disconnect and
[01:11:57] and what is the strategy to reusing this
[01:12:00] whole thing across the CLI and the SDK
[01:12:04] because we could I basically would have
[01:12:06] to rewrite all this from scratch, which
[01:12:07] I don't want to do. Like I just want to
[01:12:09] use what we're already using. Uh now if
[01:12:12] you're not trying to reuse you know
[01:12:14] agents then you know then that's fine.
[01:12:16] Um but uh I'm I I was looking to
[01:12:20] basically like automate things that I
[01:12:22] sometimes use agents for right so like
[01:12:23] sometimes I might use the like use the
[01:12:25] agent in here like go here and do
[01:12:27] triagger and then sometimes I might
[01:12:29] actually like you know run a whole um
[01:12:31] command and do it here. Um but
[01:12:36] uh right now okay would you like me to
[01:12:38] post this closing comment? Let's see if
[01:12:40] this has access to post the closing
[01:12:41] comment. Right? Because before we
[01:12:42] weren't able to do it with the CLI. All
[01:12:44] right. So why it's obsolete um in using
[01:12:48] CL using general knowledge comprehensive
[01:12:51] valuation model upgrade enhanced
[01:12:53] prompts. Um
[01:12:56] let's see what they reply. Thank you for
[01:13:00] reporting. I'm claiming evaluation
[01:13:02] framework model upgrades. To be fair,
[01:13:04] it's hard to close an issue about rag
[01:13:07] going off script because
[01:13:10] it still can happen sometimes.
[01:13:13] Um,
[01:13:15] review the customization guide.
[01:13:19] Okay, I'm going to say modify the reply
[01:13:22] to emphasize that GPT5
[01:13:25] in particular
[01:13:27] is much better at sticking to the
[01:13:31] sources. I'm going to give it a blog
[01:13:34] post link in the box DVD5.
[01:13:37] Will it rag?
[01:13:39] And here we go.
[01:13:44] Point them
[01:13:46] point them to
[01:13:50] All right. I Let's see if it's going to
[01:13:52] actually be able to close this.
[01:14:05] All right. So, now added emphasis.
[01:14:08] Here's the updated closing reply. The
[01:14:10] key changes. Where is the updated
[01:14:12] closing reply?
[01:14:14] Show me the full closing reply. I don't
[01:14:19] see it in your comment.
[01:14:29] Did it was it this blank one here?
[01:14:33] Oh no. What is this? Okay, here's the
[01:14:36] complete closing reply.
[01:14:39] There is something happening. We are
[01:14:40] like getting there. Maybe there's a
[01:14:42] different type of content that's coming
[01:14:44] through, right? Because here we're
[01:14:47] seeing event.data.content
[01:14:49] and it's just empty. So what else could
[01:14:51] be in this data? It's not content. It's
[01:14:56] something. There's message. Is it
[01:14:57] message?
[01:15:00] Um,
[01:15:03] there's content source
[01:15:06] message ID. Okay. So, there's something.
[01:15:10] Let me just take another
[01:15:13] screenshot here. Okay. This is another
[01:15:16] issue is that
[01:15:18] we are getting blank messages here. And
[01:15:20] maybe it's because we should be using
[01:15:22] message. Maybe there's something else we
[01:15:23] should be using, but basically I'm not
[01:15:26] I'm not um not seeing it. So there's
[01:15:29] there's some sort of special way a
[01:15:32] different attribute.
[01:15:34] Okay, post it. All right, I'm just going
[01:15:36] to tell it to post it. I don't know what
[01:15:38] it is. We're just gonna we're just gonna
[01:15:42] post it and see.
[01:15:46] Okay, great.
[01:15:50] Listen, the good news is, you know, this
[01:15:52] is early days, right? So, it's best to
[01:15:54] find these issues now and and that's my
[01:15:57] job, right? Is to try stuff out, find
[01:15:59] issues, report it so that then by the
[01:16:01] time other developers try it, it is
[01:16:05] working. So, now the interesting thing
[01:16:06] is that it did manage to post the reply.
[01:16:08] So, this CLI had more access to using
[01:16:11] write tools than the copilot. And I
[01:16:14] don't know why that is cuz remember with
[01:16:18] the co-pilot.
[01:16:20] Okay. Um
[01:16:23] Mhm.
[01:16:25] Great.
[01:16:28] Looks good. Looks good. So all right. Um
[01:16:32] there we go.
[01:16:35] Your issue is resolved. It looks good.
[01:16:38] That's what I would hope for. It was
[01:16:40] just it would have been nice to see that
[01:16:41] before it got posted. Maybe it like can
[01:16:43] showed it in like a markdown block or
[01:16:45] something like that. Right. Okay. All
[01:16:48] right. So, uh you know, I've been
[01:16:50] streaming for uh almost an hour and a
[01:16:53] half now. So, I think we've seen quite a
[01:16:55] bit about the CLI. Um let me go ahead
[01:16:58] and post these into a branch so that
[01:17:01] anyone can check them out and then uh
[01:17:03] John, I'll chat with you about um how we
[01:17:07] get our these changes um back into
[01:17:12] the
[01:17:13] uh into
[01:17:15] the CLI repo or the SDK repo. Okay, let
[01:17:21] me just
[01:17:24] we don't Okay, we're just going to add
[01:17:26] these
[01:17:28] add GitHub
[01:17:30] Copilot SDK examples.
[01:17:34] Here we go.
[01:17:36] I gotta
[01:17:40] run rough on these. Rough ruff ruff ruff
[01:17:44] ruff rough.
[01:17:50] All right. Push.
[01:17:56] And here we go.
[01:18:04] I need to Okay. All right.
[01:18:08] I'm not going to make a PR since that's
[01:18:09] just going to add to my open PRs and
[01:18:11] we've already determined that too many
[01:18:13] open PRs. But that is the branch. So you
[01:18:17] can check out those there. They all work
[01:18:19] with the current version of the SDK and
[01:18:22] I will be following up with the GitHub
[01:18:26] copilot teams to figure out all the
[01:18:29] different things we ran into.
[01:18:32] All right.
[01:18:34] So that is
[01:18:37] pretty good for today. Thank you
[01:18:40] everyone for for joining and uh thank
[01:18:44] you as always John for for all your
[01:18:46] help. It's always helpful when you've
[01:18:47] used these things a bit u before and
[01:18:50] joined on the stream
[01:18:52] and uh yeah everyone just keep playing
[01:18:54] with this. I mean obviously this is this
[01:18:56] sort of thing is the future. I think
[01:18:58] we're all realizing we're moving towards
[01:19:00] aentic coding as the default um because
[01:19:03] it's just more oftentimes more efficient
[01:19:06] and we're just figuring out how we can
[01:19:09] make it work for us so that we're not
[01:19:12] feeling like it's you know something
[01:19:13] painful to use right so I think you know
[01:19:16] we're we're finding ways to add
[01:19:18] automation so I think with the GitHub
[01:19:19] copilot CLI and the SDK that's probably
[01:19:22] what we're going to be using for doing
[01:19:24] like autom like kind of DevOps scripts
[01:19:27] like you know developer automation like
[01:19:29] little things that we do a lot that we
[01:19:31] want to make easier to do. Um it's just
[01:19:33] the easiest way you know we don't have
[01:19:35] to deploy anything for it like we don't
[01:19:37] have to deploy a model for it because
[01:19:39] it's already using it's just using our
[01:19:40] GitHub copilot SDK uh you know model so
[01:19:44] um it it's a lower barrier to making
[01:19:46] agents right so if all we're doing is
[01:19:48] making an agent that helps our developer
[01:19:50] workflow this is basically an agent
[01:19:52] framework similar to lang chain or
[01:19:54] Microsoft agent framework but it is
[01:19:56] easier to get started with because it's
[01:19:58] got the models built in uh so I think
[01:20:01] That's will be like the use case for
[01:20:04] this is like how like lowering the
[01:20:05] barrier to creating these agents that
[01:20:07] automate our developer processes. Uh so
[01:20:10] be thinking about what processes you
[01:20:13] want to automate and how it might be
[01:20:15] useful to you know stick some scripts in
[01:20:17] your repos that people can run that's
[01:20:19] going to do something uh some common
[01:20:22] task that is helpful. All right. So now
[01:20:25] we've got GitHub agents, we got GitHub
[01:20:27] skills, we got agents.mmd, we've got
[01:20:29] scripts that use the SDK, we've got so
[01:20:31] many different ways that we can add
[01:20:32] automation to our repos.
[01:20:35] All right. Uh so thank you everyone for
[01:20:38] joining today and uh I do have my office
[01:20:42] hours tomorrow which we can chat more
[01:20:45] about this and maybe I'll have some
[01:20:46] updates tomorrow. So do come to the
[01:20:49] office hours
[01:20:50] tomorrow if um if you want to chat some
[01:20:54] more about Python and AI.
[01:20:57] All right, bye everyone.
