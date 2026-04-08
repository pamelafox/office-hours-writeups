[00:00] Welcome to the Python AI office hours.
[00:03] This is our weekly office hours where we
[00:06] talk about everything Python and AI
[00:08] across Microsoft GitHub and the
[00:10] industry. Uh if you do have any
[00:13] questions, comments, links, news you
[00:15] want to share, put them in the chat. Uh
[00:18] we are recording this on YouTube
[00:20] unlisted so that we can uh share it
[00:22] afterwards for anyone who missed it. And
[00:26] um for that reason um we don't do the
[00:29] audio from the audience just uh you can
[00:31] just put your your stuff in the chat.
[00:34] Uh I am sharing the screen so you should
[00:39] can you hear it? Let's see.
[00:42] Let's try it again. Oh, you know what? I
[00:45] bet you PowerPoint messed with it. All
[00:47] right, let's do it again.
[00:49] Here we go. I think you can see it now.
[00:56] Okay. Uh, so here's a lot of lot of
[01:00] stuff happening this week. This slide
[01:03] was actually generated two minutes ago
[01:06] from the co-pilot CLI. And that's
[01:09] actually the first thing I wanted to
[01:10] show just because I was having fun with
[01:11] it this morning. Um, and uh, basically I
[01:15] I had it go through and use three
[01:18] different MCP servers. So I now have a
[01:21] GitHub MCP server hooked up. the new
[01:24] XMCP server, X being Twitter, and the
[01:27] Work IQMCP server. So, I said, uh, you
[01:30] know, search for the past seven days to
[01:33] see everything going on. And so, it made
[01:36] tool requests to work IQ, to Twitter,
[01:39] um, and to GitHub. And then it
[01:42] summarized everything here. And then I
[01:44] said, okay, great. But now I want you to
[01:46] make a slide. So, then it made a slide.
[01:48] And then I just iterated on the slide a
[01:50] bunch. Uh, so now I'll probably make a
[01:52] skill. so that I can do this every week
[01:55] uh and have it be the way I want it to
[01:57] be.
[01:59] Uh if you yeah if you have a question or
[02:02] comment just put it in the chat. Uh we
[02:05] don't do the audio since we are doing
[02:06] recording and my recording only catch
[02:09] only is able to get my audio.
[02:14] Uh so yeah. Okay. So, let's go back to
[02:18] our news
[02:20] unless there's any questions about about
[02:23] that. Actually, let me show my MCP
[02:25] config. Um, here I've got the MCP server
[02:28] running locally for X. So, X is a
[02:30] locally running HTP server that I had to
[02:32] set up. Um, and then
[02:37] for
[02:38] the rest of it,
[02:41] is this like Open Cloud but with Copilot
[02:43] CLI? Well, arguably everything's like
[02:46] OpenClaw is an agent that has access to
[02:48] lots of things, right? So, I think
[02:49] OpenClaw, they've added lots of
[02:51] integrations. Basically, like the more
[02:52] MCP servers you add, you know, the the
[02:55] closer you get to something that's like
[02:58] OpenClaw. So, OpenClaw is just another
[03:00] agent that has an incredible number of
[03:02] integrations and uh like a memory it has
[03:05] its own particular memory system. Uh,
[03:07] but I don't Yeah, I you know I I don't I
[03:10] guess I don't think of OpenClaw as being
[03:12] a radically different thing. I think
[03:13] it's just a slightly different agent
[03:15] harness with a lot of integration as far
[03:17] as I can tell. I actually haven't run it
[03:18] myself yet because I don't have a secure
[03:20] way of doing so. Uh, but yeah, so I have
[03:22] my Let me delete this one. This one's
[03:23] old. Uh, but in my MCP servers, you can
[03:25] see I've got Work IQ and Twitter. Uh, I
[03:28] didn't have to put GitHub here because
[03:29] Copilot always comes with the GitHub MC
[03:31] server installed, but it, you know, so
[03:34] it also has the GitHub MC server and
[03:36] then it can query all of those.
[03:40] So Justin asks um, when working with a
[03:43] multi-tool calling workflow is is
[03:46] generating skill to guide the the agent
[03:48] that use tools correctly the right
[03:49] design in your eyes? Yeah. So actually,
[03:51] let me show you. I actually did just
[03:53] make my first skill that you can install
[03:57] and um it's based off of it's based off
[04:01] the same servers. It is a formal skill.
[04:04] This is the comedy roast skill and it is
[04:07] my favorite thing to do is to ask
[04:09] co-pilot to roast you. A roast, if you
[04:11] don't know, a comedy roast is when
[04:13] somebody gets on stage and basically
[04:15] like makes fun of someone famous, but
[04:17] they do it like out of love and it's
[04:19] just really fun. So I someone you know
[04:22] someone told me like hey it's really fun
[04:23] when you ask copilot to roast you and I
[04:25] was like oh okay so I did but then
[04:26] originally it only did it I was using
[04:28] like teams co-pilot so it was only doing
[04:30] it based off like work stuff but of
[04:31] course I do a lot of stuff on GitHub and
[04:33] on social media so I'm made this comedy
[04:36] row skill um because I agree like it is
[04:39] best if you're trying to like you know
[04:41] gather you know have something like that
[04:42] that's gathering activity from lots of
[04:44] places like it does help to make a
[04:45] formal skill that says how to do it
[04:46] right so I said hey you're going to do
[04:48] get work activity this way. You're going
[04:50] to get GitHub activity this way. You're
[04:52] going to get Twitter activity this way.
[04:55] Uh and then this is how to actually you
[04:57] know deliver deliver the roast. Um so
[05:00] that's going to be more effective. Now
[05:02] the the you know maybe the drawback of a
[05:03] skill is that sometimes it's too
[05:05] prescriptive like you know maybe I
[05:07] shouldn't tell it exactly you know which
[05:08] tool to use because maybe there'll be
[05:10] like new better tools, right? So there
[05:12] is a balance with skills and giving it
[05:15] too much direction. Um, but in this
[05:18] case, I I like this one. Uh, and I'll
[05:22] show you the the output here. Right? So,
[05:25] this is the and it just came up with
[05:27] this earlier. It said, "I've never seen
[05:29] someone so aggressively productive and
[05:31] yet so fundamentally unhinged at the
[05:33] same time." Um,
[05:37] uh, let me find the code roast. Right.
[05:39] Uh, you ran a find and replace crusade
[05:41] across every Abra samples repo like a
[05:43] woman possessed.
[05:50] I love it. I really love it. So, it just
[05:52] it you can read the whole roast. There's
[05:55] nothing private in it because most of
[05:56] the stuff I do is public, right? And so,
[05:58] it also roasted my social media. Zero
[06:01] likes.
[06:03] Um, some conference planning. Uh, now
[06:08] closing those in PR. So, uh, but
[06:10] basically what I'm going to do is make a
[06:12] similar I'll make a skill for like
[06:14] generating these office hour powerpoints
[06:16] each week, right? And then I can just
[06:17] run that skill. So, it's going to use
[06:20] similar servers. So, like also like my I
[06:23] had a one-on-one with my manager
[06:24] yesterday and she's like, "Oh, so what
[06:25] did you do last week?" And my mind went
[06:27] completely blank because yesterday was a
[06:29] Monday and after, you know, like the
[06:31] weekend I remember nothing. And so I was
[06:33] like, "Uh, I know I did something."
[06:36] Right? So, if you have like one-on- ones
[06:38] with your, you know, manager and you're
[06:40] trying to like report what you did or,
[06:42] you know, if there's some sort of
[06:43] recording mechanism for that, right? So,
[06:45] there's just so many ways that it's,
[06:46] it's just useful to have um, you know,
[06:49] the an agent go through your last week
[06:52] of activity and, you know, it's just
[06:53] whatever you're doing, you can hook up
[06:55] an MVP server, right? So, if you use
[06:56] like ADO, like Azure DevOps, you could
[06:58] hook up the ADO MCP server and have it
[07:00] go through that. Um, you could hook up
[07:03] different social media and look through
[07:05] other different kind of posts.
[07:08] Um, how did this skill get my details?
[07:10] It's it's calling the the tools, right?
[07:13] So, uh, so you can see here like for the
[07:16] PowerPoint um, it uh, let's see, it
[07:21] failed the first time, but um, it got,
[07:24] you know, it called Twitter tools. Uh,
[07:26] then it it did the work IQ correctly.
[07:29] So, it's calling tools and I am
[07:31] authenticated into each of these. Right.
[07:33] So, I'm authenticated to work IQ because
[07:36] I've set up the the access for that um
[07:39] that server. Where is it? Um
[07:42] all right. So, I am I'm authenticated to
[07:45] work IQ already because that's a command
[07:46] line that you can install and then you
[07:48] authenticate it. And so, then it just is
[07:50] always auth. And then for Twitter,
[07:52] that's actually a Python server that I'm
[07:54] running locally and that's set up
[07:55] because I set up a M&V file that had all
[07:58] my Twitter developer account uh details.
[08:00] So I I am paying for that because to get
[08:03] an X developer account now, they don't
[08:05] really I don't think they have free P
[08:06] plans anymore, but it's like really
[08:08] really low amounts of money. Like I pay
[08:10] like 20 bucks a month for my Twitter API
[08:13] usage, so like that's fine. Um so yeah,
[08:16] so these are making authenticated calls
[08:19] uh on my behalf. Um, in theory, some of
[08:22] these are all public, so you don't you
[08:24] wouldn't necessarily have to be
[08:25] authenticated, but I am already
[08:26] authenticated into work IQ and GitHub
[08:28] and and Twitter.
[08:32] Um, and yeah, the rose skill is using
[08:34] the same it's using this the same the
[08:37] same uh servers. Um, right. So, here I
[08:41] can I can roast myself again. Uh, let's
[08:44] see. Let's do a new tab.
[08:50] uh
[08:52] compilate
[08:55] okay so like when I started and you know
[08:57] you can do this with any coding agent so
[09:00] I'm also using um this is installable
[09:03] with npf skills so that's this is this
[09:07] package on
[09:08] and npm that makes it easy to add any
[09:11] skill so if you want to share a skill
[09:13] this is the easiest way to do it uh so
[09:15] we've started doing this for some of our
[09:16] other skills at Microsoft right um
[09:19] making it so you can just do npx skills
[09:21] add and I only discovered it last week
[09:24] but I think this is really cool. So so
[09:26] easy to to set it up and then you can
[09:28] just add it, right? And then this is the
[09:30] experience, right? So I said, uh, so you
[09:32] could try this yourself. Um,
[09:35] and what it does is it looks it, you
[09:38] know, searches the GitHub repo for for
[09:41] skills and it looks in a bunch of
[09:42] places. It finds, in this case, it found
[09:44] one skill and then said, "Oh, which
[09:46] agents do you want to install to?" And
[09:47] it installed to lots of different uh
[09:49] agents.
[09:50] I only really use GitHub Copilot, but
[09:53] it's fine to install it for other
[09:54] places. And so then it just copies it
[09:56] into all the relevant folders. So that's
[09:58] worked for those. And you can add on
[10:00] lots of other agents as well. Um, so
[10:04] yeah, so I do recommend if you want to,
[10:07] you know, if you make a skill that you
[10:08] think is, you know, generally useful for
[10:10] other people, um, this one's kind of a
[10:12] silly skill, but I will actually, this
[10:15] was just my test, right? Because I, you
[10:16] know, I'm just playing with this now. I
[10:18] will actually um share some of my more
[10:20] practical skills
[10:23] um you know uh now that I've seen how to
[10:25] do it right. So okay, roast my last
[10:29] uh day of activity.
[10:32] All right. So you know when you're doing
[10:35] a skill uh hopefully it's going to find
[10:37] the right skill to use here. Um, if not,
[10:40] you can like explicitly I can also
[10:41] explicitly trigger the skill with slash
[10:43] comedy roast in copilot. But yeah, no,
[10:45] it figured out it should use that skill.
[10:47] Says, oh, there's a comedy roast skill
[10:49] available. They want a comedy roast.
[10:51] Okay, it says for the last day. So now
[10:53] you can see it's, you know, it's looking
[10:54] at all those tools. It's sending it off.
[10:56] It's checking, okay, what meetings, what
[10:58] emails, what files, searching,
[11:01] searching. So it, you know, it got a
[11:03] bunch of information from all those
[11:04] sources. And now it's generating the um
[11:09] all the thoughts. Um uh so Justin asks,
[11:14] "Do you put a skill in a repo or
[11:15] globally?" I usually install them
[11:17] globally now because I just so often
[11:20] want the same skill across all my repos.
[11:23] Um
[11:24] you know, that's if I if I'm like if I'm
[11:26] doing an NPX skills ad, it's usually
[11:28] that I do want that skill across
[11:30] multiple repos. like you know for but
[11:32] for this one like actually I might have
[11:34] it just like let me just try unit now
[11:36] right um so I always like to give you
[11:39] know to give um things information all
[11:42] right so creating agent skills okay
[11:44] create a new skill based off this
[11:47] conversation
[11:50] for co-pilot CLI that can generate
[11:54] weekly powerpoints for the office hours
[11:59] docs here so This skill I'll probably
[12:02] this is a very specific skill right so
[12:05] this skill I will just keep it in this
[12:07] repo. So for in the repo it'll go inside
[12:10] the repo it can go in agent/skills
[12:13] um and it'll probably ask me if that's
[12:15] where I want to put it. So yeah some
[12:17] skills are really really specific and
[12:20] you're just going to put them um in a
[12:22] repo. Others are um more generic.
[12:25] There's one that I've used like I don't
[12:27] know 20 times in the last day uh which I
[12:30] finally installed across all my repos
[12:32] and that's the one I will go and um oh
[12:36] good there's no secrets okay uh let me
[12:38] find how do we okay if we go here
[12:42] okay so skills skills
[12:45] global
[12:47] uh user okay this is the one okay so
[12:50] this is the skill that I'll go ahead and
[12:52] put in a standalone repo because so
[12:55] helpful. And this is the one I use to
[12:57] review comments on an active PR. Um, so
[13:00] I've already installed this globally
[13:02] just manually in Copilot, but I'll I'll
[13:04] I'll put this in a standalone GitHub
[13:06] repo soon so that it's super easy for
[13:08] other people to install because
[13:10] basically any PR any repo I'm in, if I
[13:13] get comments on a pull request, I like
[13:15] to go through those comments
[13:16] collaboratively with Copilot to decide
[13:19] whether to how to, you know, how to um
[13:22] take action on those comments. and just
[13:24] makes it so much nicer to review PRs.
[13:27] Uh so yeah, it just depends whether it's
[13:29] going to be, you know, super specific.
[13:31] So here, um it's going to
[13:35] uh I'm going to tell it to
[13:39] make the skill inside this project only
[13:45] in I think it's agentskills.kills
[13:51] agentskills.
[13:58] All right. So, hopefully it'll do that.
[14:00] And what is it doing here? Oh, okay. Uh
[14:03] I think we have our new
[14:08] uh our new roast here. This is So, it's
[14:10] now
[14:12] um look right now. Look at this. And
[14:15] right now you're supposed to be in the
[14:18] Python AI Discord weekly MA, but instead
[14:20] you're here in a terminal getting
[14:21] roasted by AI. Your tenies are out there
[14:24] asking questions about Azure Open eye
[14:25] and you're over here asking a robot to
[14:27] hurt your feelings priorities.
[14:32] I'm sorry. I just think it's I just
[14:33] think it's so funny. Um,
[14:37] okay. So, yeah. So, one good thing to do
[14:39] is like after you've done a workflow
[14:41] with an agent, if you know for sure like
[14:43] that's a useful workflow that you'd want
[14:45] to do again, uh have the agent, you
[14:48] know, you know, work with the agent to
[14:50] create a skill. Um I was doing that
[14:52] again. I did that last night for uh a
[14:55] different skill. Um so here, this is my
[14:59] like presentation
[15:01] writeups repo. And uh let's see. I used
[15:06] it yesterday to do this writeup. And
[15:09] normally when I have it do it these
[15:11] writeups, it's based off of PowerPoint
[15:13] decks and it just converts the
[15:15] PowerPoint decks to images. This one we
[15:17] didn't have a PowerPoint deck. It was um
[15:19] just the the video. So I had it go
[15:22] through and take um screen caps of the
[15:24] video. And then the fun thing was that I
[15:26] had to make a skill where it would look
[15:28] at the screen caps and look at which of
[15:30] our mouths were open and if whether our
[15:32] eyes were open or closed and forced it
[15:34] to find the right frames where we the
[15:37] right person's mouth was open and where
[15:39] we both had our eyes open which is like
[15:41] surprisingly hard right to get like this
[15:43] one you know I don't love my face here
[15:45] but at least uh it got my mouth open. Uh
[15:48] but yeah, it did like you know this took
[15:50] def this definitely took some iteration
[15:52] and um in order to get this skill
[15:56] uh working well um but uh you know but
[16:00] it's like you know you know once you
[16:01] have it you iterated on it you keep
[16:03] trying uh and so there these skills this
[16:06] new one is this uh let's see capture
[16:10] video frames skill here right so it both
[16:13] has a skill.md and has this so these
[16:16] ones are pretty useful skills And I
[16:18] might also um you know make make these
[16:22] more sharable as well. Right. So
[16:24] criteria for best face.
[16:29] It's so funny.
[16:31] Um okay, good. And now look, this one
[16:33] has made the skill. So it's got a skill
[16:36] and a skill.md. Okay. So then basically
[16:39] next week before office hours, I'll have
[16:42] it actually just, you know, use that
[16:45] skill, right? I'll just say, "Okay,
[16:48] you're gonna use that skills." Oh, we'll
[16:50] just do skills reload. Skills reloaded,
[16:53] right? And now I can just autocomplete
[16:56] and be like, "Okay, generate slides for
[16:59] this week." Right. Um, so yeah, it's
[17:02] surprisingly easy to to start making
[17:05] skills and and uh iterate on them. Okay.
[17:09] All right. It's really fun. Like
[17:11] honestly, it can make you like it really
[17:12] can increase productivity. Okay. So,
[17:14] let's see. Let's go back to the actual
[17:16] news. I have I do have a bunch here
[17:18] thanks to the that um you know the the
[17:21] autogeneration. Uh so the big thing that
[17:24] everyone's super excited about is that
[17:26] agent framework
[17:28] is now uh 1.0. Uh we're all super pumped
[17:33] about this. A lot of people basically it
[17:35] means it's it's generally available
[17:36] right? So if you go and look at the
[17:39] Python packages you can see it is now
[17:41] 1.0 O and it also that means it's
[17:44] generally available. Uh and so that
[17:47] means for anyone who's in a company
[17:48] where you're only allowed to use GA
[17:50] things, you can now use agent framework.
[17:52] And so to celebrate that, we went
[17:54] through and um updated all of our agent
[17:59] framework uh demos, right? So the all
[18:02] the ones that we made for the last live
[18:03] stream series, these are all updated to
[18:08] 1.0.
[18:09] Um and for the most part there were
[18:13] there was one issue. So there is one
[18:15] issue because the new default
[18:19] um API that they're using is responses
[18:22] API instead of chat completions API. Now
[18:25] that's a good thing because responses
[18:26] API is generally much fuller featured
[18:28] and you get the built-in tools like code
[18:30] interpreter which is so powerful. Um,
[18:32] but there is this one open issue that
[18:34] they're working on that did affect one
[18:36] of our samples and uh I had to simplify
[18:39] it. Um, so keep that in mind is that if
[18:42] when you're using agent framework 1.0,
[18:44] if you're using it with like an Azure
[18:45] OpenI endpoint or or any of the Foundry
[18:48] Direct models, it is going to default to
[18:50] the responses API, which is a good
[18:53] thing, but you could run into some
[18:56] issues with that. Um so just you know
[18:58] file an issue on the repo if you
[19:00] actually do run into anything there. Um
[19:03] especially if you're if you were
[19:05] previously using chat completions then
[19:07] you know then you you might see some
[19:09] differences.
[19:11] Let's see. Oh yeah as your openi modules
[19:14] are now getting migrated to foundry
[19:17] models. That's just an email alert you
[19:18] might get in your inbox. uh Langchain
[19:21] shared that there's a huge amount of
[19:23] traffic coming from Azure OpenAI uh that
[19:26] it grew like 4x in the last you know uh
[19:30] I don't know what it was like six months
[19:31] or something. So lots of people are
[19:32] using lang chain with Azure OpenAI. It's
[19:35] a nice combo. Um so uh it's nice to have
[19:38] link chain supporting that. Uh let's
[19:42] see.
[19:43] Uh oh this was this was something this
[19:45] morning that I really liked. um that
[19:48] when you are on
[19:51] so let's say you're on no let me go here
[19:53] uh
[19:55] all right so we you're on a pull request
[19:57] so let's see I get all these dependabot
[20:00] things all the time right so I got this
[20:03] um prettier all right so I got this
[20:05] prettier update here and the first time
[20:09] that it ran the CI failed you see this
[20:11] like red red X so the CI failed because
[20:15] the prettier update Actually, I had to
[20:17] rerun pretty on some files. Now,
[20:19] normally I would have to do that myself,
[20:21] but here you can now just say at
[20:23] copilot. So, I said, hey, at Copilot,
[20:25] the prettier CI failed, you know, fix
[20:28] it. And so then copilot basically took
[20:30] over the PR, made the fix and committed
[20:34] it and then and then and then, you know,
[20:36] everything passed and then I was able to
[20:38] approve it. So, I'm personally really
[20:40] excited about that because I get so many
[20:41] of these auto PRs from Dependabot and a
[20:43] lot of them you'll see like half of them
[20:45] will fail and uh you know and then I'll
[20:48] have to be like, "Oh, okay. What was the
[20:50] fix?" Blah, blah, blah. So, now I can
[20:51] just be like, "Hey, at Copilot, right,
[20:53] I'll go on here and be like, I co-pilot
[20:58] CI failed. Figure it out. Let's see if
[21:01] that works."
[21:06] Just work it. Just make it work. just
[21:08] make it work. Okay. Um, so yeah. So
[21:12] that's cool. So I think you can probably
[21:13] do that with any PRs, have co-pilot take
[21:15] it over, but I'm most excited about it
[21:16] for dependent bot PRs because that's the
[21:18] ones where it's often like, uh, that's
[21:21] annoying. I don't want to figure it out,
[21:22] blah blah blah. Let's see. We talked
[21:25] about MPA skills, NPX skills ad. And I
[21:28] will say where I first discovered that
[21:30] is with the Cosmos DB skills. So if you
[21:32] are using Cosmos DB, you can NPX skills
[21:35] ad. uh their their um bundle of skills
[21:40] here. And the nice thing is that it will
[21:42] review your data model and critique it.
[21:45] So you notice how I roasted my week. It
[21:47] will roast your data model. It's not
[21:49] quite in a roast format, but it's
[21:51] basically basically a roast format,
[21:54] right? Um
[21:56] uh no, it's nice. I I used it and it did
[21:59] make some like really good um
[22:01] suggestions for how to improve a data
[22:04] model. Uh, so it's just got all these
[22:06] best practices built in that it knows
[22:08] about. So here's the skills. Um, there's
[22:12] skill
[22:13] and, uh, it's got, wow, tons of
[22:19] rules. So, it's just got a it's got a
[22:22] huge library of information that it can
[22:25] pull in um, when it needs to. So, it
[22:28] says use the linked rules.
[22:31] Okay, so that's how they set up their
[22:32] skill is to avoid having a huge amount
[22:35] in the main skill. They have these um uh
[22:40] link skills there and we do something
[22:42] similar
[22:43] for the Azure OpenI to responses skill
[22:46] that I've been um working on. Right. So
[22:48] this one we have skills
[22:51] and that skill.md
[22:54] uh does actually have a lot of stuff in
[22:56] it, but then it has these linked files
[22:58] like cheat sheet MD, right? And the
[23:01] cheat sheet has even more stuff. Uh, so
[23:04] skills, you know, can have more than
[23:06] just their skill.md. They can have
[23:08] related references, assets, images,
[23:11] scripts, etc. Whatever you need to do.
[23:17] Uh, let's see.
[23:21] Yeah, it is now in VS Code. If you um at
[23:24] least in insiders I think in stable now
[23:26] perhaps when you click on this gear icon
[23:29] you see everything that is customizing
[23:32] your co-pilot experience. So you see
[23:34] agents, skills, instructions, prompts,
[23:37] hooks. I don't have any hooks yet. I
[23:39] should add a hook. That'd be cool. MCP
[23:41] servers, plugins. Uh now it's there's so
[23:44] many different ways of extending your,
[23:46] you know, coding agent experience. Now
[23:49] hopefully over time some of these will
[23:50] consolidate. Like I think um that
[23:53] prompts I think prompts maybe are being
[23:56] going to be deprecated in favor of
[23:57] skills because a prompt is so similar to
[24:00] a skill.
[24:02] Um and so yeah so we'll see uh how these
[24:07] evolve over time but right now you do
[24:08] have many ways of extending the GitHub
[24:13] copilot experience in VS Code. And now
[24:17] you can see at a glance what are all the
[24:20] ways um you know that are currently
[24:22] enabled and and you know maybe you want
[24:24] to remove some of those ways or add some
[24:26] ways based off of what's here now.
[24:32] Uh okay. All right. So those are updates
[24:35] on the Microsoft and GitHub side. uh in
[24:41] industry side. Um
[24:45] uh I was excited to see that fast MCP
[24:48] does have built-in open telemetry
[24:50] support right now. So we were actually
[24:51] able to uh update our Python MCP demos.
[24:56] Before we had to have our own custom
[24:57] middleware. We were able to just remove
[24:59] that middleware and now uh you know we
[25:02] can just use the built-in open telemetry
[25:04] support and that will work. We've got it
[25:07] working with a few different things. We
[25:09] got it working with Aspire and also with
[25:12] App Insights and with Logfire.
[25:16] Uh so that's great if you're using fast
[25:18] MCP servers.
[25:20] Uh if you're doing other MCP stuff, uh
[25:23] as we saw, there's an XMCP server. Now
[25:25] there's going to be a ton of MCP
[25:26] DevSummit events all over the world. So
[25:29] if you're into MCP, do check the Linux
[25:31] Foundation website to see uh you know
[25:34] which ones are coming to you.
[25:37] Um, and what else? Okay. Oh, I I
[25:41] published some blog posts this week. Uh,
[25:46] not this one.
[25:50] So this one is blog post from this week
[25:58] and this is about using uh building fast
[26:02] MCB servers that authenticate with entra
[26:04] ID and do not use the DCR proxy approach
[26:10] that I've talked about before. Uh so
[26:12] this only works with VS Code which is
[26:14] limiting but is also the most secure
[26:16] from kind of the Entra perspective. So,
[26:19] you know, if that's if that is what you
[26:22] need, um, then, you know, check out
[26:25] check out that blog post.
[26:29] Um, uh,
[26:33] and then we put out some podcasts and,
[26:37] uh, and videos,
[26:40] right? So, we had some stuff on on
[26:43] Foundry IQ. So, Foundry IQ is basically
[26:45] Azure AI search, but inside Foundry.
[26:47] looks fine.
[26:49] Uh let's see. Oh, basically that video
[26:52] like you know we had a few things. Uh so
[26:54] there was a video and I already showed
[26:56] the write up for it here but let me link
[26:58] to the actual video too.
[27:01] Here's this one
[27:04] and then there is also uh
[27:08] soft. Okay, this is like this fancy
[27:13] uh you know fancy podcast series and so
[27:16] you might want to just check out the
[27:17] whole series. Uh it's you know it's well
[27:21] done
[27:22] and we did this one about is context
[27:26] engineering the new rag.
[27:30] I don't know why it's on here twice.
[27:31] Okay.
[27:35] Uh okay. All right. So, that's a lot of
[27:38] the a lot of the stuff
[27:41] that I had in my list. Do we have any
[27:45] questions this week?
[27:50] Oh, maybe that's unpublished. Okay.
[28:02] What else do people want to talk about?
[28:04] Let's see.
[28:09] And pretty soon I will be working on the
[28:11] Foundry hosted agent samples. So uh
[28:14] hopefully I'll know more about those
[28:15] soon.
[28:17] Uh yeah, I keep
[28:20] suggesting things to to chat about.
[28:24] Let's see.
[28:26] Gemma 4. Oh, that is a good question.
[28:28] Gemma 4. Yeah, that actually is a very
[28:30] good question. I I have some updates on
[28:32] that. So um let me see. Do I have the
[28:35] link on here? Because it was a cool
[28:36] thing. Um, yeah, this one. Okay. All
[28:39] right. So, GN open models. Okay. Let me
[28:42] see if I can find their tweets about it.
[28:43] Lang chain open models.
[28:47] Um,
[28:49] no. Let me look at my man. I should just
[28:52] be able to Let's see if I can use um Can
[28:54] you find the tweet I liked this week
[28:58] about lang chain and open models? All
[29:02] right. I wonder if it's going to work.
[29:04] Um,
[29:07] let's see who's faster. It's always f
[29:08] fun to like race yourself against the
[29:11] MCP server. I do this all the time with
[29:12] work IQ. Um, okay. So, like tweets. I'm
[29:17] going to use the same strategy. Uh,
[29:19] yeah, really just look at all my like
[29:21] tweets. This is also a nice um video
[29:23] from James. Okay. So, oh, and and we've
[29:28] got a new series on YouTube about
[29:29] co-pilot from our friend Gwen who does
[29:32] the Spanish office hours. Okay. So,
[29:34] there's some good videos there. Uh,
[29:38] we sent people to the moon. That's
[29:39] great. Um, okay. Where is
[29:43] There we go. Wait, and did they did
[29:45] co-pilot already found find it? Um,
[29:48] yeah, they did. Okay. All right. So we
[29:51] kind of we kind of you know uh got a
[29:54] good uh
[29:56] equal equal timing.
[30:00] All right. So this is what I see. So um
[30:02] basically like lane chain
[30:05] the folks from lane chain have are
[30:07] arguing that now
[30:10] you know the open models have crossed
[30:12] the threshold and they were evaluating
[30:15] it on on link chain specifically. Um and
[30:19] I replied I was like okay well you know
[30:22] we were trying to like sure so here's
[30:24] the thing there's open models and then
[30:26] there's small language models right so
[30:28] he was looking at they were looking at
[30:29] open models and they're like okay with
[30:30] these open models like they're close to
[30:32] Frontier but the other question is small
[30:34] local like the small versions of these
[30:36] right how well can the small versions do
[30:38] and we're trying to find good small
[30:40] language models so that people can run
[30:42] our open source repos without having to
[30:45] have an Azure subscription set up and
[30:48] and I in a you know we were trying to
[30:50] use this one Gwen 3.5
[30:54] 9B but I was getting just not like bad
[30:58] results with it. I was getting you know
[31:00] it was forgetting my original question.
[31:02] It was outputting Chinese yada yada. Um
[31:05] and Mason said like oh it looks like
[31:06] Gemma might change this right. So then
[31:11] uh so then Gwen who I just posted Gwen
[31:14] did test out Gemma. Now the first thing
[31:17] that happened was that Gwen ran into a
[31:19] bug. So there is an open bug in O Lama
[31:22] that affects that affects um
[31:27] uh the the our ability to use
[31:31] where is
[31:40] LinkedIn.
[31:43] This one. Okay. So, this one also
[31:46] affected our ability to use Gemma. Um,
[31:49] and the they're they're working on it
[31:52] now.
[31:53] Um, but we did a patch for it. So, we
[31:57] patched it for now just so we could
[31:58] compare. And we saw much better results
[32:01] from Gemma 4. Uh, and that was I think
[32:04] it's like an 8 8B model. Maybe it's
[32:06] listed on a lama now. Let's see. Gemma
[32:09] Gemma 4.
[32:12] Uh, so what do we got? E2B
[32:16] Python.
[32:18] No. Where's the actual Okay, so there's
[32:21] this. Okay, there's a They're calling it
[32:24] E4B. Okay, I don't really know what the
[32:26] E4 means versus just calling it E4. Why
[32:31] are they calling it E4B? E2B. Okay, so
[32:34] they call it E forb. E2B.
[32:38] Those are the smaller ones. Okay. So, I
[32:41] believe we tested,
[32:43] let me figure out which one we tested
[32:44] because these look pretty similar in
[32:46] size, right? This one is eight.
[32:49] This one is almost 8 gigabytes. This
[32:52] one's almost 10 gigabytes. So, which one
[32:55] did we test? Did Gwen test? We check it
[32:59] out.
[33:04] Um,
[33:10] let's see what Gemma
[33:12] says. 8B. So, I think 8B must mean this
[33:15] one here. So, I think that's the one
[33:19] that we tested. And then let me get the
[33:23] results.
[33:25] Okay. So we were you know we were
[33:27] comparing um using it these uh with
[33:31] various M like basically an agent
[33:33] pointing at an MTP server that has a
[33:35] task right so that's like a pretty good
[33:36] tool calling scenario because they have
[33:38] to decide which tool to use call the
[33:41] tool correctly get back the response and
[33:43] then use the response in order to answer
[33:45] the question right um and so you know
[33:48] when it was a simple HP server uh a
[33:51] simple MCP server with a simple tool
[33:53] they both did fine with it. Um, but the
[33:56] one that was tricky was this one, which
[33:59] was the the Microsoft learn MCP because
[34:01] that can return back a lot of context.
[34:04] And so I guess in this case, Gwen did
[34:06] okay. But when I, you know, in my
[34:08] experiments with Gwen, it was like
[34:09] returning Chinese. It was completely
[34:11] forgetting what I want. And you can even
[34:13] see here it says it said it didn't
[34:15] provide the exact command and ask for
[34:16] clarification. Right? So Gemma 4 did
[34:18] better here. So this is actually a
[34:20] pretty good test using the learn MCP
[34:21] because it does send back a you know a
[34:25] lot of um uh information right and a
[34:31] small language model can get more
[34:32] overwhelmed by just you know a lot of
[34:35] stuff in their context window than a
[34:36] large language model right and then it
[34:38] said um
[34:41] and this is one's actually similar um
[34:44] but it liked uh Gemma better but I think
[34:46] this to me is the big the big one
[34:48] because Gwen was just doing so poorly at
[34:51] this one. Um, so we are going to move to
[34:54] the Gemma 4 looks like the eight this
[34:56] one the E2B 8 basically 8 gigabyte
[34:59] model. Um, let me double check that
[35:03] that's one that Gwen was using in her
[35:06] analysis. Did you use
[35:11] in your experiment? Just find out.
[35:14] Uh, so yeah. So, I think uh once once
[35:17] the Olama issue is fixed, and they did
[35:19] they did tell me that they're working on
[35:20] it, then hopefully we'll go through and
[35:24] verify that that's a good um option for
[35:27] our local
[35:30] local SLM story. Um as for using these,
[35:34] you know, in production in the cloud,
[35:36] that's a different story. Um I you know
[35:39] in that case you know you you want to
[35:42] like really make sure you can get it up
[35:43] to um a good good level. Um but I did
[35:47] share some things around that because I
[35:50] went to the DSP pie meetup and there it
[35:54] was a lot of people who use DSPI
[35:57] with small language models. So in this
[35:58] case, here's the they did Quen and then
[36:03] they used DSPI to optimize the prompt so
[36:06] that they got really
[36:08] uh really good results from Quinn and it
[36:10] was cheaper. Um right so you can see 75x
[36:15] cheaper. So if you are going to be using
[36:18] these in production like maybe you're
[36:20] putting them on like a serverless GP
[36:23] like a container app serverless GPU or
[36:24] whatnot then you may want to use
[36:26] something like DSPI which will actually
[36:29] iteratively um improve the prompt using
[36:32] genetic algorithms uh so that your
[36:34] responses are the best.
[36:38] Let's see. And I see
[36:40] Sylvester shared a cool screenshot
[36:48] text arena text to text. Uh so yeah, so
[36:53] you can see good results for Kimmy,
[36:54] Gilen, Gemma, Quinn, etc.
[36:58] Yeah. So there's exciting stuff
[36:59] happening with the with these new
[37:01] models. Um a lot of them are available
[37:04] on foundry models. Uh but you know not
[37:07] all of them. Uh but for local use a lot
[37:10] of them are available on Alama
[37:13] and uh yeah try definitely try them out.
[37:19] So John has a question. How is the
[37:22] co-pilot CLI accessing the web browser
[37:26] so easily?
[37:28] Um, what a case I haven't necessarily
[37:31] Let's see. Oh, I do have a Playright MCV
[37:33] server set up. Um, so let's see. I don't
[37:38] actually know. So here's the question is
[37:40] whether open it up in my
[37:44] in my normal browser instance which has
[37:45] my cookies or in an unauthenticated
[37:48] browser in so say use playright to check
[37:52] my LinkedIn post for this week. Right?
[37:54] Because you notice I didn't I didn't
[37:56] hook up my LinkedIn because LinkedIn
[37:59] does not have an MCP server and in fact
[38:01] LinkedIn is kind of difficult to use
[38:03] from an API programmatic perspective. So
[38:05] I often have to use um tools. Right. So
[38:08] here you can see it's going to try and
[38:09] use playright. It says it wants to use
[38:12] playright and in order to get to this
[38:14] URL
[38:16] um and I don't know if this is an
[38:18] authenticated URL or not. Let's see.
[38:23] So, okay, that's definitely not me.
[38:27] I should tell. It wouldn't be good if it
[38:29] knew who who I am. All right. My URL is
[38:34] blah.
[38:37] It definitely Yeah. In your global like
[38:39] global instructions for agents, it's
[38:41] really helpful to say this is my GitHub
[38:43] username and these are like my social
[38:45] like just so you know where you are on
[38:46] the internet. It'll make it much better.
[38:48] All right. So, let's see. So now it
[38:51] wants to go to this URL and um so this
[38:55] is my recent activity. Now does this URL
[38:58] work in
[39:00] so this now this is what's really
[39:02] notable. This URL requires off. So if
[39:05] playright opens in my normal browser it
[39:08] will work. If it opens in a new browser
[39:10] uh it's not going to work right. So
[39:12] let's just see what happens
[39:15] because that's that's that is what is
[39:17] tricky is that a lot of times you might
[39:18] be wanting to use these browser tools to
[39:21] browse uh authenticated URLs and I think
[39:25] in this case yeah so here you can see
[39:27] what happened is that
[39:30] uh playright opened it in a separate
[39:34] browser which does not have the cookies
[39:36] and on so the thing is in one ways
[39:39] that's really good right that it's it's
[39:40] hard for, you know, an agent to just get
[39:43] access to, you know, your bank accounts,
[39:45] blah blah blah, right? Because if it had
[39:46] unfettered access to your web browser,
[39:48] you've got all your cookies in there,
[39:49] and that's hard. Um, however,
[39:53] um, you know, oh, so here, no, let me
[39:54] type my credentials. Um, other um, I
[39:59] thought that maybe they had,
[40:02] let's see, with MCP server, if there is,
[40:04] I think you can maybe opt your browser
[40:06] in to agent sharing. Uh let's see player
[40:12] MCC server
[40:14] uh drag
[40:16] configuration
[40:18] user profile
[40:20] uh persistent isolated
[40:24] okay connect your existing so this is
[40:26] what you need is you do need this
[40:29] playright
[40:30] that didn't that wasn't so good didn't
[40:33] work uh kitub user attachments packages
[40:36] extensions all right so I'll let the
[40:39] GitHub the Playright team know that that
[40:42] is not the right URL but user
[40:44] attachments packages extension. All
[40:46] right. So I think that maybe
[40:54] all right let's just find this playright
[40:56] MCP bridge extension.
[41:04] Oh maybe we can go to like the Edge
[41:06] extension store. This would make sense
[41:07] for this to be a browser extension.
[41:09] Okay. So, let's look for
[41:13] playright MCP bridge. Now, if you're
[41:16] going to do this, you want to um be
[41:19] careful about it. All right. I don't see
[41:20] it here.
[41:24] Um it looks like we might have to get it
[41:26] from
[41:31] It's interesting that they made it for
[41:32] Chrome first. Okay,
[41:35] switch to Chrome.
[41:37] Oh, look. I can just get it. All right.
[41:41] Thank you, Edge. Um, okay. I'm going to
[41:44] add it.
[41:46] It is now installed.
[41:49] And let me go ahead and pin to the
[41:52] toolbar.
[41:54] And set this. Oh, it's got a little key.
[41:57] Okay, good to know. Um, oh, wow. So, you
[42:01] really All right. Well, I'll be
[42:03] regenerating that afterwards, but um
[42:06] let's go ahead
[42:09] and
[42:12] I'm just going to exit this and then add
[42:15] this to my
[42:19] servers.
[42:20] Okay, so now we have playright and this
[42:23] time you see it's using the argument
[42:26] dash extension and it has a freaking
[42:28] hard-coded key, which is my favorite.
[42:31] Uh, so then I'm gonna go and
[42:34] I'll get rid of my old
[42:37] playright.
[42:40] Oh, I wonder if I need my browser thing
[42:41] though. Let me add in the browser
[42:43] command. Browser because normally I tell
[42:45] it which browser to use. So we're going
[42:46] to say browser
[42:48] and MS edge. Okay. Okay. So we'll delete
[42:53] this one.
[42:56] All right. co-pilot
[43:01] and let's see
[43:04] if it can
[43:07] uh
[43:10] all right find my post from this week
[43:13] using playright.
[43:20] All right,
[43:24] let's see if it's going to be able to
[43:25] use that bridge extension.
[43:34] Now, this does mean that it could go to
[43:37] any web page. So, once again, we want to
[43:39] be careful, but let's see. All right,
[43:42] we're going to say yes.
[43:44] And look at that.
[43:47] You notice it opened in my existing
[43:49] browser, the one with a billion tabs
[43:52] and uh now it's checking the page and
[43:56] getting it all. So that worked. Um but
[44:00] it so once again I did need the um
[44:03] extension to do that. So let me link to
[44:06] the extension and you do want to be you
[44:10] know careful about that. Um this is
[44:14] let's see where do we get it? Uh,
[44:20] a little more information on it here.
[44:24] Uh, I need to file a bug that that link
[44:27] is broken.
[44:31] And there we go. So now now that I have
[44:34] that, I can actually have a roast based
[44:36] off my LinkedIn activity as well.
[44:42] Uh, vertical tabs. I don't know. I think
[44:44] I tried vertical tabs once. So, it's
[44:48] really during these office hours that I
[44:50] accumulate so many tabs and I leave them
[44:52] open on purpose because I actually have
[44:54] an extension that um
[44:58] saves all my tab URLs. So, then what I
[45:00] do is like at the end of the session I
[45:05] um you know use this extension uh and
[45:08] then when I'm generating the transcript
[45:11] it's just even easier for it to find the
[45:13] links. So, normally I don't have a
[45:15] billion tabs. I purposfully do leave
[45:17] them open during these office hours just
[45:20] so that I can save them afterwards for
[45:22] prosperity.
[45:26] All right. Browsing my LinkedIn still.
[45:29] Okay.
[45:30] So, if you have to analyze a repo that
[45:33] has over a 100 files and five megabytes
[45:36] in them, what techniques does GitHub
[45:38] copilot use
[45:40] um when it's processing lots of files?
[45:42] Yeah, I it Copilot has its own semantic
[45:47] search. Um,
[45:50] so let me find out see if I can find the
[45:52] most recent blog post about how
[45:55] um code search how they implement their
[45:58] code search.
[45:59] Uh, so this is from March 17th,
[46:03] 2026. That's very recent. Okay, great.
[46:06] So this should be
[46:08] the most recent
[46:11] um
[46:13] uh
[46:15] opi
[46:16] okay
[46:18] semantic code search tool. Oh well this
[46:21] isn't quite what I wanted. No I wanted
[46:23] the implementation. So this just says
[46:25] that copilot coding agent has access
[46:27] that search. Oh, and that's also a a new
[46:29] change is that um now when you're
[46:32] searching repos on like github.com, it
[46:35] uses the semantic search. So even if you
[46:38] didn't get like an exact before you had
[46:41] to have exact matches, now it does use
[46:42] basically like a vector search, right?
[46:44] Um but this is okay. I was trying to
[46:46] find
[46:48] benefit.
[46:50] Okay. Copilot will not use semantic code
[46:52] search. Okay. when you start a
[46:54] conversation process automatically index
[46:59] um and then similarly so indexing runs
[47:01] in the background
[47:04] um blah blah blah
[47:07] still haven't found what I want is the
[47:09] blog post that explains the algorithm
[47:11] they use because they do have
[47:15] there is a particular algorithm that
[47:16] they use
[47:33] search
[47:36] algorithm. Um,
[47:39] I don't even think they necessarily use
[47:41] vector, but I'm going to look for
[47:42] anything. Okay, there's that's about
[47:44] their new embedding model.
[47:47] That was 2025.
[47:52] Yeah. So, they do I I mean that's that's
[47:53] part of it is maybe this is the most
[47:56] recent post. So, generally Oh, and then
[47:58] what do you say? Okay. Uh
[48:06] workspace search indexes.
[48:10] No more
[48:15] always semantic. Okay.
[48:20] So, are they all getting remote index
[48:22] now? I mean, it's probably good to have
[48:24] more consistency.
[48:27] Um,
[48:29] all right. It's possible that like
[48:32] Yeah. Oh, so this was the instream blog
[48:34] post. So I I do think this is an
[48:35] instream blog post and um of course this
[48:39] was a year ago so it might be with the
[48:42] the changes but we could also look at
[48:45] markaw
[48:46] code
[48:48] GitHub.
[48:53] Let's see how it's doing in LinkedIn.
[48:54] Oh, look at this. Your LinkedIn post
[48:56] from the last week. Nice.
[49:02] Cool. Okay. Uh, I just want the repo.
[49:06] Ah, I'll just go
[49:08] github.comicrosoftscode.
[49:12] Okay, thank you. Um,
[49:17] does VSCode index the repository for use
[49:22] by code
[49:25] used by copilot?
[49:27] It sounds like with what Desh posted is
[49:30] that
[49:32] it's
[49:34] um remote
[49:36] and since I don't have time to read it,
[49:39] I'm just going to go ahead and ask the
[49:42] responses API to read it.
[49:46] Here we go.
[49:50] I'll copy. It'll just copy. Uh so is
[49:54] co-pilot search remote or local?
[50:03] Okay. So VS code does not uh
[50:08] local work local workspace indexing
[50:11] local representations.
[50:18] Yeah, I don't think it has necessarily
[50:20] the best. Copilot search is no longer
[50:22] userf facing.
[50:24] It's just indexing. Copilot may use a
[50:26] hybrid approach.
[50:28] Okay.
[50:31] All right. I don't know. I Yeah, I don't
[50:33] have a great reply here because I I now
[50:35] I'm not sure exactly how it's
[50:36] implemented um because I think it just
[50:38] keeps changing. Um, so I do think that
[50:40] this this post was interesting, but I
[50:43] don't know if this is um, you know, how
[50:46] how up to date this is in terms of the
[50:48] actual algorithm.
[50:52] Maybe you all understood it better.
[50:53] Let's see what DH
[50:59] uh, would we possibly do a QA session
[51:01] for member of VS Code team in that call?
[51:03] That would be cool. Yeah, that's a good
[51:04] question. Does VS Code have? So the
[51:07] thing is the VS Code team they um they
[51:11] they do at least they do internal office
[51:13] hours
[51:14] uh with us like just us like people who
[51:18] work at Microsoft and those are super
[51:19] fun. Um I think they do on the VS code
[51:23] channel I don't know if they do AMAs
[51:27] though that would be
[51:29] um that would be a cool thing. Let's see
[51:31] what they have again the last week
[51:33] whether they're doing stuff like AMAs
[51:37] uh live stream April recap. So the best
[51:41] one to ask questions is the when they do
[51:43] these release posts, right? Uh so that's
[51:46] coming up April
[51:49] April 16th. But I'll also tell the team
[51:54] uh I don't know also if they have their
[51:55] own Discord channel or not. That's
[51:57] another good question for them.
[52:00] So I will ask them. Um but yeah since
[52:03] they have such a you know such a good
[52:06] channel uh popular channel you know a
[52:10] lot of times they post so much stuff
[52:11] there that usually you can catch catch a
[52:14] live stream and you know at put comments
[52:17] on those live streams. Uh but yeah I
[52:20] will ask about that.
[52:23] All right. Okay. We are now at the end
[52:28] of the hour. Thanks all for coming and
[52:32] bringing
[52:34] fun questions and things to explore as
[52:37] always. I learned a few new things. I
[52:39] hope you did too. I will looks like are
[52:43] we still recording over here? We are
[52:44] still recording. Very good. Uh so I will
[52:48] publish the recording on YouTube. I'll
[52:50] put the transcript up with all the
[52:53] questions and links in our weekly thing
[52:56] here. And I usually post on LinkedIn as
[53:00] well.
[53:03] All right.
[53:05] Bye everyone. Have a great day.
