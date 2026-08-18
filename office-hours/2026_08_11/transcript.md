[00:00] Welcome to our weekly Python plus AI
[00:04] office hours. So this is where we go
[00:07] through the weekly news and see what
[00:11] everyone's working on and uh you know
[00:14] explore some new technologies, learn
[00:16] some new things together, discuss what's
[00:18] happening.
[00:20] So as always I start off with some news
[00:24] to to get us going. Um, but at any point
[00:27] if you have anything to share or any
[00:29] questions to ask, you just put them in
[00:31] the chat and I'll be watching that chat
[00:34] the whole time. Uh, so
[00:38] what was big for the last week? Um, so I
[00:44] think this was July 30th, so this was
[00:46] like 12 days ago.
[00:48] But this was really big is that stacked
[00:52] pull request.
[00:54] Uh so they are now this is a feature
[00:58] this does not have anything to do with
[01:00] AI actually even though the AI officers
[01:02] but it actually kind of does relate to
[01:04] AI because people are using it with
[01:06] coding agents a lot now but this is
[01:08] something that developers have wanted
[01:10] for a long time regardless of AI. Um, so
[01:13] this is basically you're like, you know,
[01:15] when you're doing like a branch off a
[01:16] branch off a branch and you kind of have
[01:17] to like ceue up all these PRs and you're
[01:20] like, "Okay, I gotta merge this PR and
[01:22] then I'm gonna merge this PR and then
[01:24] right." So you can make this stack of
[01:26] PRs and the, you know, they kind of take
[01:30] care of the merging
[01:33] for you. So
[01:36] yeah, so this is helpful if you find
[01:38] yourself, you know, doing that kind of
[01:40] workflow where you do have a lot of PRs
[01:42] that stack on top of each other
[01:46] and um you know just making it easier.
[01:49] So I haven't even gotten to try it out
[01:51] yet because I actually haven't really I
[01:54] mean I've been writing code but not in a
[01:56] repo where I've been doing lots of PRs.
[01:58] So
[02:00] I've just been pushing the main.
[02:02] So in repos that are collaborative in
[02:05] particular, right? Like in collaborative
[02:06] repos where you you know I you know I
[02:09] like where I am writing code at like a
[02:11] different pace than my reviewers
[02:13] especially that's where it's super
[02:14] helpful to be able to do a stack of PRs.
[02:17] So I'm like okay here's you know this
[02:20] I've you know created the sequence of
[02:21] PRs. you can review them, you know, at
[02:24] the pace that works for you. And that
[02:26] way I can keep my code changes separate.
[02:29] Um, but you know, make these and make
[02:32] these PRs that are like it's something
[02:35] that is possible for a reviewer to
[02:38] review like that they're not too large.
[02:43] Uh, so yeah, just check out that. Um, I
[02:47] see a question from AI engineer. How
[02:49] much practice of Python is required for
[02:51] AI and is DSA data structures algorithms
[02:54] important for machine learning?
[02:58] Um I mean generally I would say like
[03:01] that you still you know in the new phase
[03:05] of a dentic coding you still need to
[03:08] have a good idea of how code works so
[03:12] that you can reason about whether the
[03:15] code that's being produced from a system
[03:17] is is good. Um, so you can kind of
[03:20] recognize code spells, right? Sometimes,
[03:22] uh, LMS will produce melly code as we
[03:26] say, like code that isn't really
[03:27] following best practices. It might
[03:28] achieve the goal, but it's like, you
[03:30] know, it's overly complex or it does
[03:32] something is a bit of a weird way or
[03:34] maybe it's doing some sort of monkey
[03:35] patching like in Python that happens a
[03:37] lot.
[03:39] So, uh, yeah, I mean, currently I would
[03:42] recommend that you at least be able to
[03:44] read code and understand it. You know
[03:46] these days we aren't necessarily writing
[03:47] the code ourselves but you know a good
[03:50] test is can you look through a program
[03:52] and can you explain what each line of
[03:54] code is doing in the program that was
[03:56] actually the interview task that I was
[03:58] given when I applied for this job and I
[04:01] thought it was a good test um you know
[04:04] how well you understand something.
[04:06] So currently I would say we we still do
[04:09] want to be able to read code
[04:13] and understand it well enough. The other
[04:16] question was is data structures and
[04:17] algorithms important for machine
[04:18] learning? I I mean machine learning is
[04:23] based more off of discrete math than
[04:26] data structure and algorithms but it
[04:28] does use stuff like extreme programming.
[04:30] uh I would say oh it is helpful to
[04:33] understand all those ideas because you
[04:35] know machine learning like to get it
[04:38] working it doesn't have to be efficient
[04:39] but all of the goals now are to be able
[04:42] to do stuff more efficiently. So if
[04:43] you're going to do something efficiently
[04:44] then you very much need to understand
[04:45] data structure and algorithms right you
[04:47] want to use the right data structure so
[04:49] that you're minimizing you know either
[04:51] memory or or time and you want to use
[04:54] algorithms that will be more efficient
[04:56] right so that we reduce our you know
[04:59] unnecessary use of energy and and all
[05:01] that stuff
[05:03] so so yeah so I mean I think you know
[05:06] you're when you're first just getting
[05:08] the machine learning network running
[05:10] doesn't necessarily have to be efficient
[05:11] but for the people that are actually
[05:14] working on our machine learning
[05:16] networks. It helps to make them
[05:18] efficient so that we minimize energy
[05:20] use.
[05:23] All right,
[05:26] let's see what else. Okay, so this was
[05:29] um a big thing that came out
[05:32] from uh from a bunch of companies. Let
[05:35] me show
[05:39] the where we have people who are
[05:41] involved here. So this is
[05:42] agentplugins.org.
[05:44] So this is a
[05:47] new specification and it wraps skills
[05:50] and MCP. So then it like the whole point
[05:53] of agent plugins is actually to wrap
[05:55] skills and MCP. It's basically a bundle
[05:58] that points to at both of them, right?
[06:01] So, okay, we have a manifest and then uh
[06:04] the
[06:09] let me Okay, so here's like our
[06:14] Okay, how do we do it? Agent defines a
[06:16] closed mcp.json format.
[06:18] Okay,
[06:20] so that's going to be so you're going to
[06:23] make your manifest. Your manifest is at
[06:25] the root plug-in.json JSON
[06:28] and that contains all the metadata
[06:33] and then and then you're going to have
[06:35] skills and MCP servers
[06:38] inside of that. Let me see if I can get
[06:41] an example.
[06:47] Yeah, so skills are just put in a skills
[06:50] folder and that's how they're
[06:51] discovered.
[06:56] And um yeah, so I'm just trying to find
[06:58] Okay, let's see. Reference agents plugin
[07:01] specification
[07:03] JSON schemas.
[07:08] Let me see if I can find the agent
[07:09] plugins blog to see if we've linked to
[07:15] Yeah, let me see if we link to some
[07:16] example plugins in this one because that
[07:18] would just be helpful.
[07:20] See? Okay, so like this is what the
[07:24] directory looks like, right? So you've
[07:27] got a plug-in.json, you've got a skills
[07:29] folder, you've got mcp.json,
[07:31] and then you may have some client
[07:33] specific stuff, right? So this is a
[07:34] client extension. Um, so it's like VS
[07:37] Code supports hooks, but hooks are not
[07:39] part of agent plug-in spec yet. So that
[07:42] would go under the client the client
[07:46] directory there. Oh, thank you. You
[07:48] found the examples. Very good.
[07:56] Just seeing if there's anything else
[07:57] useful there.
[08:00] Okay, let me link to this one as well.
[08:05] Right. Agents plugin example.
[08:10] Oh, so this is like basically the
[08:12] template. Yeah. So great. This is the
[08:13] template. This is what you would copy.
[08:18] wanted to see if we also
[08:21] I think a lot of our VS Code plugins
[08:25] would use this too. It would just be fun
[08:27] to see, you know, example of one that's
[08:30] using it.
[08:34] Let's see.
[08:38] Not sure how I would find it. Okay. What
[08:40] plugin that we have?
[08:44] Well, anyway, we have the example
[08:47] I'll poke around for a specific ex if
[08:49] anyone finds a live plugin. Um I think a
[08:53] lot of our VS code plugins are basically
[08:57] that to follow this right because this
[08:59] is from Harold. Harold's from the VS
[09:00] Code team. So this is something that
[09:02] Harold's been working on and he wants to
[09:04] add a lot more to it but you know given
[09:06] us being a standard they need support
[09:09] from everyone.
[09:13] They do have a lot of client support for
[09:16] it. So this was de
[09:19] design developed by Amazon, cursor,
[09:21] Microsoft, OpenAI and Versell.
[09:27] Oh, you tried creating one but failed.
[09:29] The skill worked but not the MC MCP.
[09:33] Um H in VS Code or where? Because we
[09:36] could just try it.
[09:40] >> Let me see. Uh uh framework agnostic.
[09:43] Well, your question is this is a
[09:44] standard. So, um you know it depends on
[09:47] the client, right? So, here we can see
[09:49] that the this is the support right? So,
[09:52] it says you know that GitHub it claims
[09:55] VS code works Hermes agent open claw kro
[09:59] that's from Amazon cursor you know it
[10:02] claims that all of these
[10:04] support each of the components.
[10:07] Oh, you're using chatb.
[10:11] I don't actually even have chatbt
[10:13] anymore. I think I can use it on the
[10:15] website. Maybe
[10:17] you So, chat tot
[10:20] instructions
[10:30] again.
[10:35] Does this one have a Okay. skill
[10:40] agent plugin.json.
[10:47] This one doesn't have an MCP.JSON
[10:49] though, so it'd be nice to have an
[10:50] MCP.json.
[10:53] Click start.
[10:58] Enter.
[11:03] Okay. So presumably. All right. Okay.
[11:04] So, what we can do
[11:07] is fork it.
[11:11] Okay. Let's fork this
[11:27] and
[11:29] we need to add an MCP to it.
[11:35] What MCP server are we going to add to
[11:40] put portable NC? Okay.
[11:49] Okay. Let's do this.
[11:58] Canvas system there.
[12:15] I lost the Okay, come on. Copilot app.
[12:19] Here we go. All right. Oh, it's being
[12:21] really funny. It's still got the canvas
[12:23] on top from the other one. That's a bug.
[12:27] Let me screenshot that. Okay.
[12:31] We try new session.
[12:36] Come on.
[12:40] We're going to just quit
[12:42] and restart it.
[12:50] I'm gonna make
[12:53] a mcp.json JSON
[12:58] do this plugin
[13:02] and
[13:04] oh, we'll just use the myself learn MCP.
[13:16] Okay, let's see.
[13:24] That should be
[13:27] GBT. So once we
[13:32] make it, we can
[13:36] in chat GBT. So we'll try it in co-pilot
[13:38] first. Oh, what am I doing? I'm trying
[13:41] to make a plugin. I'm trying to make an
[13:43] agent plugin um
[13:47] and test it out. Make sure that it
[13:51] actually works. Um, so I forked the
[13:54] plugins example
[13:57] and um, and now it's time to add the
[14:04] the MCP.json. Let me just give it
[14:07] example because it's kind of struggling
[14:08] on that.
[14:10] I'll just point it. Here's the schema.
[14:22] Yeah. Oh, I eventually found it. Here we
[14:24] go.
[14:27] Yeah.
[14:28] So, it's going to add this mcp.json and
[14:31] that says, okay, for this plug-in,
[14:34] we're going to have, you know, these MCP
[14:37] servers. You can see this example of an
[14:38] HTTP server. This example of of a
[14:41] standard input output server. We're just
[14:43] going to do a simple HP server that is
[14:47] public off
[14:49] and doesn't have any headers.
[14:53] And then um once that works
[14:58] we can first try it
[15:01] in GitHub copilot.
[15:04] Okay plugins. Okay added the root.json.
[15:10] Let's check it.
[15:13] Oh
[15:18] hopefully that was good. Let me see. Oh
[15:20] here we go.
[15:22] um
[15:26] speed.json. Okay. All right. So, this is
[15:28] what it added. This looks
[15:32] right. Is that the MCP server?
[15:36] No,
[15:38] the MCP
[15:40] server URL.
[15:44] Okay. Give it the right URL and use the
[15:47] documentation page instead.
[15:55] And then we plug in star reference and
[15:58] the skills.
[16:05] Not really the skills we want, but
[16:07] that's okay. We just want to test to see
[16:08] if this works. We could change it to a
[16:11] different skill. Uh, okay. So, that
[16:13] looks good.
[16:17] and we'll just commit and push that.
[16:20] Okay, so now we have a plugin
[16:24] and our plugin has an plug-in.json
[16:27] mcp.json.
[16:29] So then the next thing is how do we
[16:32] install it?
[16:35] Oh, interesting. This says mcp.json
[16:38] instead of sp.json. I think that may be
[16:40] a bug. I think there's some con like
[16:44] there's some places where it's mp.json
[16:46] JSON and some places where it's
[16:47] MCP.json. Oh, it says either M.MCB or
[16:50] MCP. Okay. So, there's maybe some
[16:55] there's support for both because in the
[16:57] agent plugins said just MCP. All right.
[16:59] So, then how do we install it
[17:04] or
[17:07] install
[17:09] and copi cloud agent? What about the
[17:11] app? What about the app?
[17:15] Forgot about the app.
[17:19] They should add instructions for the
[17:20] app. Okay, note to self is that this
[17:24] should add app. All right, I'll find it
[17:26] in the app. So, we'll just go here
[17:29] and we'll go to
[17:37] maybe manage copies integration from
[17:40] customiz. Oh, okay. There's a whole new
[17:41] sidebar. Okay, look. MCP plugins,
[17:44] skills, extensions, canvas installed.
[17:46] Okay, plugins. All right. So, can I
[17:51] I'm going to
[17:54] Can I just plug it from a repop? No.
[17:58] Available.
[18:00] How about this? Manage marketplaces. Is
[18:03] that a marketplace?
[18:05] Let's find out if this repo counts as a
[18:07] marketplace.
[18:11] How would I just install it from a repo?
[18:17] Okay, so you can install plugins from a
[18:19] marketplace or repository local path.
[18:22] Okay, you can All right, we're just
[18:24] going to Okay, we'll just do we'll go to
[18:27] the CLI because the CLI is actually the
[18:29] same thing as the app
[18:33] as in if I configure it in the CLI, it
[18:35] should work in the app. So we'll say
[18:38] copilot plugin install d-help
[18:43] right and it says
[18:47] I can just provide a git URL
[18:51] from a GitHub repository coh okay so
[18:54] we'll say our GitHub repository is this
[18:58] owner repreo name
[19:02] install owner/reo
[19:04] okay it said it installed installed.
[19:08] Oh, and then it says, okay, another
[19:11] another interesting note. It says direct
[19:13] plug-in installs are deprecated.
[19:16] Only plug-in markspace will be installed
[19:18] in a future release. All right.
[19:21] Okay. That's another interesting thing
[19:23] to note that that doesn't really agree.
[19:25] All right. So now let's see
[19:28] whether I can refresh this list here.
[19:32] And
[19:34] it's not showing it installed over
[19:37] there. Copilot plugin.
[19:40] Oh,
[19:43] let's do co-pilot plugin list.
[19:48] Okay. So, it does not show the one that
[19:51] we just installed.
[19:55] Um,
[19:57] so it doesn't show the It doesn't show
[20:00] the one that was just installed.
[20:12] Even though it claimed it installed
[20:13] success. All right. So, that didn't
[20:15] work. So, now I have a lot of feedback
[20:18] for the plugins folks after this. Um,
[20:22] okay. So, let's try
[20:26] let's try VS Code. That should
[20:31] work hopefully.
[20:34] Um,
[20:36] instructions, agent plugins,
[20:40] discover and install, extension views,
[20:43] brow list of available plugins,
[20:46] and select install.
[20:48] So they definitely want you to install
[20:51] from a marketplace but oh install plugin
[20:54] from source. So let's do that. Install
[20:56] plugin from source.
[20:58] So going to
[21:02] go here
[21:05] and say install plugin from source
[21:11] and do that.
[21:19] Okay. And you can see um that it
[21:22] basically like kind of filled in.
[21:25] It's doing it's doing it's pretending as
[21:28] if it found it in the extensions
[21:29] marketplace and installing it from
[21:32] there. Um, so you can see now that I do
[21:35] have it installed here. And if I go to
[21:41] myization
[21:45] window here, I click on plugins. Okay.
[21:50] So now this one is working and you can
[21:52] see it's undercoil install plugins
[21:54] direct
[22:01] here twice. So that I think one of these
[22:05] came from our co-pilot install and the
[22:08] other one came from the one we just did.
[22:09] So that's another um interesting thing
[22:13] to note. Okay, so I now have it
[22:16] installed. I possibly have it installed
[22:17] twice.
[22:19] So let's just see
[22:23] now I should have access to that server
[22:29] and um yeah so we can see Microsoft
[22:32] learn actually shows up several times
[22:34] because I have it installed other ways.
[22:36] So so but you can see when I click on it
[22:39] it shows it does come from
[22:42] that plugin. So now I have access to
[22:45] this Microsoft learn server because it
[22:47] came from a plugin. I also have access
[22:49] to the skills because they came from the
[22:50] plug-in. So once if I go if I go to chat
[22:52] customizations
[22:56] that skill
[22:58] should come. Yeah. So here you can see
[23:00] that skill see migrate agent plugin that
[23:03] skill came from a plugin as well. So
[23:04] that's the point of a plugin is once you
[23:06] install the plugin you get both skills
[23:09] and MTP servers right. So you can see
[23:11] like I have the work work IQ is uh
[23:13] basically a plugin and um it has both
[23:19] skills and it has MCP servers right so
[23:21] this work IQ came from a plugin so we
[23:24] can see that when we look at skills we
[23:26] look at MCP servers we can see that some
[23:29] of them came from plugins so plugins are
[23:30] a good way of bundling teams together
[23:34] when you know that oh you want to you
[23:36] know you want to have both MCP servers
[23:38] and skills because they're you They're
[23:40] kind of they useful for different
[23:42] reasons. All right. So, the goal we were
[23:44] trying to do is figure out how to do
[23:45] this with chat GBT.
[23:48] So, let's see if I can log into this and
[23:50] maybe it'll be happier if at least I'm
[23:51] logged in even though I'm not currently
[23:54] paying them money.
[23:58] Let's see if we can use plugins.
[24:02] Okay.
[24:06] Plugins, right?
[24:09] So,
[24:10] are they going to let us?
[24:14] What did they say for the quick start?
[24:16] Select the plus button and enter.
[24:20] Go to setting security. All right. So,
[24:21] first we're going to go to settings and
[24:23] turn on developer mode
[24:31] settings, security, and login.
[24:34] And let's turn on
[24:40] Okay,
[24:42] I turn that on. Then there's a plus
[24:45] button here. Ah, new plugin.
[24:49] This is like making a plugin from
[24:50] scratch.
[24:54] I want to
[24:57] make a plugin just from the GitHub.
[24:59] Okay, let's check on this. Read the
[25:00] guide.
[25:02] Nope. There's your plugin. Okay.
[25:07] Did that
[25:09] package industry view go to chat to
[25:11] plugins?
[25:27] I'm trying to install
[25:30] again from GitHub repo
[25:35] tuc.
[25:40] So, oh, so Justin, what did you do when
[25:42] you were installing your plugin in
[25:44] chatbt? How did you install it? Because
[25:47] you said that you I it sounds like you
[25:49] were able to install it,
[25:51] but you know, you're saying that the MCP
[25:53] didn't work.
[25:58] Oh, we got a discount on MI code one
[26:01] flash. We're doing all these discounts
[26:02] now for for models to encourage people
[26:04] to use them. This one is apparently
[26:06] fairly popular and things. Okay.
[26:12] Yes, it says this one says I really have
[26:14] to make a marketplace.json. I don't want
[26:16] to have to make a marketplace.json
[26:18] unless that's what you did.
[26:23] It also says MCP.json. JSON.
[26:31] Well, we could add a marketplace.json
[26:33] and make it.
[26:36] Okay. So, Justin's saying workspace
[26:37] plugins. Workspace plugins.
[26:46] Um,
[26:49] do you only get a workspace when you pay
[26:51] for chatbt projects? lower left.
[27:04] There's plugins here.
[27:12] Nope. Going back.
[27:18] You've installed developer mode.
[27:22] He's passing me around.
[27:34] It may not be free. Click on your name.
[27:36] Okay. Yeah. So, here. Oh, I can try plus
[27:40] for free. Woohoo. Free.
[27:47] Okay.
[27:49] Oh, yay.
[27:54] Remind me to stop paying for this next
[27:56] week.
[28:02] That
[28:11] 00
[28:14] 30 days free. All right, we got 30 days
[28:16] to mess with this because I gave up chat
[28:19] GBT so I could use do Spotify instead.
[28:26] Okay, here we go.
[28:29] Welcome to plus we still don't get a
[28:32] workspace. Yeah, it might be for So here
[28:35] we do get sites and we get GPTs.
[28:40] Oh, so this is like a Google pages kind
[28:42] of things
[28:44] or GitHub pages, any sort of pages,
[28:47] right?
[28:49] That's kind of fun. They're going to
[28:51] replace Facebook. All right. So, I get
[28:54] library project scheduled plugins
[28:56] finance site GBT.
[28:59] Yeah. Okay. So, so, so far we've only
[29:03] gotten plugins actually really working
[29:06] in properly in um
[29:11] VS Code, at least being able to install
[29:14] from a repo, right? I think that's that
[29:17] the development hurdle is installing
[29:19] from a repo when we're not using a
[29:21] marketplace.
[29:23] I think we need better guidance on how
[29:25] to do that since
[29:27] you might be developing that way.
[29:32] Uh so John says by adding a plugin to an
[29:34] agent it keeps both skills and FC
[29:36] capable the same vendor in a single
[29:38] place. Does it reduce context loading
[29:39] initially?
[29:41] No, I would say it doesn't particularly
[29:43] reduce context loading initially like
[29:45] reducing context it I mean it really I
[29:48] mean increases context because if you
[29:49] install a plugin now you got skills and
[29:50] MSP servers but you know the thing to
[29:54] keep in mind is all right let me do like
[29:56] a new just a brand new conversation and
[29:59] we'll we'll try mi code on flash I'm
[30:03] just going to say hi think can handle
[30:05] that
[30:07] um so let's just look at
[30:10] you know at the the the
[30:13] log. That's a fancy hello. Okay. So, if
[30:18] we look at the chat bug view for this
[30:21] one, we said hi.
[30:31] Oh, interesting. So, this is really I
[30:33] think this is really fun. I love looking
[30:34] at VS Code's debug view because you can
[30:38] see all the requests that go over to
[30:40] LMS. So actually I'm seeing this
[30:43] interesting request here which is
[30:44] summarize virtual tools. So you're
[30:47] giving multiple groups of tools have
[30:48] been clustered together based on
[30:49] semantic similarity. So I think this
[30:51] must be happening because I have a how
[30:53] many tools do I have? Oh, I have 267
[30:56] tools for some reason. I think I've got
[30:58] too many enabled right now. So
[31:00] apparently if you have a huge number of
[31:03] tools then VS code u
[31:07] to do some some sampling it says okay
[31:10] you're going to given one group of tools
[31:14] and then it goes back it says Microsoft
[31:16] documentation tools. Okay. So, I think
[31:20] it must have sent this off because it
[31:22] noticed the this is probably something
[31:24] it does like as it sees more things get
[31:27] added over time because it's only in
[31:28] this case it's only summarizing the VS
[31:30] code tool. So, so that's interesting.
[31:32] So, I think that just happened because
[31:34] it saw a new tool because we added the
[31:35] plugin but this is you know this is our
[31:38] actual request right. So,
[31:41] you know we have the you know the system
[31:43] instructions from VS Code. It's actually
[31:46] pretty short now. As the models get,
[31:50] you know, as the models get better, the
[31:52] the system prompt can go, you know, the
[31:54] main system prompt here can get shorter.
[31:57] Um, but then we have more instructions
[32:00] here. All right. So, I'm trying to find
[32:02] the tools because you were asking about
[32:03] like context.
[32:08] I mean, there's a lot more in the
[32:09] system. Okay. Skills, right? So when you
[32:12] have skills, you can see the skills get
[32:14] appended here using XML. It's funny how
[32:17] we use XML with LMS, but the skills, you
[32:20] can see each of them have a name and a
[32:22] description.
[32:23] Name, description, and file. So then if
[32:25] it decides it wants to use the skill,
[32:27] it's going to do it based off that. So
[32:30] that's how it does the skill. So skills
[32:31] actually add the most to your context
[32:33] because it always loads in the
[32:35] description at the beginning currently.
[32:37] But if we go down, okay, so we've got
[32:40] all these skills. We got sub agents as
[32:42] well. Sub agents are similar where they
[32:45] have names and descriptions.
[32:48] Let's see. That's my agents.mmd.
[32:51] Okay. And then
[32:54] and then here's the question is what
[32:55] about the tools? Right. So the tools
[32:59] I'm trying to find the tools for you.
[33:02] Date.
[33:05] Okay. So the tools are actually way up
[33:09] here.
[33:12] And um you can see the tools. So in this
[33:15] case it is sending the tools with their
[33:18] names and descriptions as well.
[33:20] Oh that's because we're using Okay. So
[33:23] so this is what it looks like with MI
[33:25] code one flash which doesn't have any
[33:28] sort of fancy tool deferred tool loading
[33:31] or searching. So for for this model this
[33:34] model we have to send all the tools and
[33:36] skills up. So, let's actually try it
[33:39] with um GPD 56 soul because we're going
[33:43] to see it looks a bit different.
[33:47] Okay.
[33:49] Right. So, here
[33:51] you can see that the tools there's just
[33:53] 21 tools with the first one being the
[33:55] tool search. So, in fact, what it does
[33:58] is that it uses tool search for most of
[34:01] the tools and all the rest of these
[34:03] tools are just the built-in VS code
[34:04] tools. So VS Code decides that it always
[34:07] wants to have just these be, you know,
[34:11] very easily available to the agent and
[34:14] the rest of them it puts behind tool
[34:15] search. And it can do that because the
[34:17] OpenAI models are specifically trained
[34:19] to be able to search tools. That's
[34:21] actually something that's part of their
[34:23] their reinforcement learning process.
[34:27] So So yeah, so they'll it'll you know
[34:29] tell them like, hey, if you you know, if
[34:32] you need to Oh, so here you go. tool
[34:34] usage guidance. So, use the search tools
[34:37] if you need them. And then I think it
[34:40] also does potentially give the names.
[34:43] Does it give tool names
[34:46] there? You can see all the skills again.
[34:47] Skills, skills, skills, skills, agents.
[34:52] Let's see. Okay. And then it says
[34:54] available deferred tools must be loaded
[34:57] with tool search for use. So, this is
[34:59] really interesting. Well to me is that
[35:02] we um there is for the models like MI
[35:06] code one flash we um you know we have to
[35:10] send every single tool name in and
[35:13] description beforehand. But for the open
[35:16] models and also for the anthropic models
[35:18] because both of them support tool search
[35:19] and deferred tool loading as something
[35:21] that the model inherently knows how to
[35:23] do. then we can should send a lot more
[35:26] information because here we're just
[35:28] sending the tool names and that is why
[35:30] when you're developing tools you should
[35:31] have good tool names because you know
[35:34] this if you have a good tool name this
[35:36] is going to realize that oh okay like
[35:38] and you can see it even does a little
[35:40] bit of name spacing too for GitHub one
[35:42] so it's like okay it's a GitHub MCP
[35:44] server and it's this tool name right so
[35:47] you do want to try and make that be
[35:50] descriptive so that it decides that it
[35:52] does want to use that tool search use
[35:55] it.
[35:58] Now I just want to try anthropic model
[36:00] just because I believe that it's
[36:03] implemented very similar but it might be
[36:05] slightly different.
[36:14] A
[36:16] is a prompt categorization for I find it
[36:19] so interesting. Okay. class.
[36:23] So, why are we classifying it? I'm not
[36:25] in auto mode. Interesting.
[36:27] Anyway, all right. So, let's go. This is
[36:29] the main message. And this one Oh, this
[36:32] one is actually sending all the tools. I
[36:34] wonder why this one is sending all the
[36:36] tools. 4.8
[36:42] full use instructions.
[36:45] tool search
[36:47] says you must use tool search to load
[36:49] deferred tools but it also
[36:54] shows a lot of tools being sent.
[36:58] So I don't know maybe because this one
[36:59] it might be because this one has a
[37:00] larger context. Oh I'm on high 1 million
[37:03] context
[37:05] why that's a lot of context. Maybe the
[37:07] other one if I was in soul that has less
[37:10] context. Maybe that's the reason why.
[37:12] Maybe maybe when we switch to one
[37:14] million contacts, we don't bother and
[37:17] maybe we just always send all the tools,
[37:19] right? I mean, this is the kind of stuff
[37:20] that VS Code tests out um to try and
[37:24] figure out.
[37:26] Um yeah, so when you're to open this,
[37:28] it's just Okay, sorry. I always click
[37:30] the one wrong, but anyway, click the
[37:31] burger icon, the dot dot dots, and um
[37:35] click show chat debug view. Um, there's
[37:37] other stuff too like we have this agent
[37:40] debug logs
[37:42] and that can be helpful as well. That's
[37:45] a little more I guess higher level here.
[37:47] I'm used to just doing the chat debug
[37:49] view. Okay. And I also excitingly now
[37:53] now have cat. So this is this is a cat.
[37:57] So now we're going to start having cats.
[37:59] Well, they're kittens. So they're kind
[38:02] of insane as kittens are.
[38:06] I think it's behind. Yes.
[38:10] Um, yeah. So, how to enable LM calls
[38:13] view. Oh, I it might be I'm trying to
[38:15] remember if this is something you have
[38:16] to enable. I think it's on by I think
[38:19] you're always can get it, but let's see.
[38:21] So, I just did you just, you know, you
[38:23] do your chat and you do show chat debug
[38:25] view and you can also do agent debug
[38:27] logs for the one I have open right now.
[38:30] Um I let me see if you need to enable
[38:34] that was something I had to enable.
[38:40] Um there certainly are come some kinds
[38:43] of debugging you have to enable but I
[38:46] think that this one is on always.
[38:52] Yeah. Just let me know if you don't see
[38:53] it.
[39:01] Okay. All right. Right. So, what we were
[39:03] talking about, um, context. Yeah, I just
[39:04] find it super interesting. Um,
[39:08] let me see. There's a blog post about
[39:09] it. Let me find the blog post. I've been
[39:12] I've been using Copilot to try and keep
[39:14] my book like to bookmark for me, but
[39:16] it's like bookmarking way
[39:19] too many things. It's crazy. is you
[39:23] shouldn't like I've discovered you can't
[39:25] just have an agent bookmark for you. Um,
[39:27] but this was the this is the I think I
[39:29] started off manually.
[39:31] Let's see. So, wasn't that one? It was
[39:49] No, I'd have to like I should like list
[39:51] the on here very and now I can just ask
[39:55] copilot like
[39:57] is it link
[40:00] to find all the VS code blog links?
[40:18] Yeah, this wasn't the one I was thinking
[40:19] of. I don't think tweet would be the
[40:21] hypo. No, let me find this one. Here we
[40:26] go.
[40:27] So this one mentions the different tool
[40:30] search approaches here and it did say
[40:34] that for anthropic
[40:38] it does tool search as well but you know
[40:40] maybe it depends on the model.
[40:44] Okay. All right. So Justin saying okay
[40:47] that it did not import the MP. Okay. All
[40:50] right. That's good to know. Um I will
[40:53] send a bunch of feedback to Harold.
[40:56] and um see if there's some known issues
[40:59] there.
[41:02] All right, so Pablo says, "When I
[41:04] normally work with Copilot app, do I use
[41:05] a reviewer agent to evaluate and improve
[41:07] the answer from the model answering the
[41:08] chat or modifying filed or does app
[41:11] already implement actions to use several
[41:13] models to reach requests or more
[41:14] complex?"
[41:17] Um
[41:19] yeah, so
[41:21] sometimes what I do let me see where I
[41:23] did it. Where did I do it? It did
[41:26] something like that.
[41:28] Or did I do it? Um,
[41:35] I asked it to I asked it to like send
[41:39] something off to a bunch of um, you
[41:42] know, a bunch of a bunch of models. So,
[41:45] I'm just seeing if I can
[41:47] next.
[41:49] No, I just kind of want a list of every
[41:51] I because I can't even remember what I
[41:53] was doing.
[41:56] do it here.
[42:00] It was something where I asked it. Oh,
[42:03] this is what I did. Wait, was this it?
[42:05] We can keep it.
[42:10] No, no,
[42:14] no. That's what we did today.
[42:17] What the heck have I been working on?
[42:19] All right. Um, nope. Nope.
[42:23] So, let's just see if we can try it
[42:25] here. Um,
[42:29] okay. Use
[42:31] DVD 56 soul
[42:34] opus 4.6
[42:38] to
[42:40] suggest a MS learn MCP related skill we
[42:46] can add to this repo instead.
[42:50] What? So what I'm trying to get it to do
[42:53] is to use sub aents and I did this in
[42:56] another repo but I can't remember where
[42:58] I did it. Um because the thing is that
[43:00] copilot has access to all these models.
[43:03] It has access you know it has the
[43:05] ability to do sub agents. So in theory
[43:08] you know I can just be like hey just do
[43:11] this across you know across multiple
[43:13] models. And we have like built-in things
[43:15] that do that like the review, you know,
[43:18] you can just say like review and tell it
[43:20] what models to review with and it will
[43:21] do that, you know, kind of same thing. I
[43:24] mean, really with any of them,
[43:27] you could ask it to do it across
[43:29] multiple models and it should be able to
[43:31] use a So this is a sub agent, right?
[43:34] It's basically sorry because you see
[43:36] here it's a little little co-pilot. So
[43:39] this it has like kind of forked off and
[43:42] made a sub agent here and we can look at
[43:46] each of the sub aents and see them
[43:48] running and one of them should be
[43:51] running with GP56 soul and the other one
[43:54] should be running with opus 4.6. So uh
[43:58] yeah so right now I just am just I just
[44:00] ask it but you could make a skill just
[44:03] if you got tired of saying the same
[44:04] model names over and over that that's a
[44:06] little tiring. So you could be like you
[44:08] know like your you know your multiple um
[44:12] you know multiple model skill or
[44:13] whatever. Um
[44:16] so here this one
[44:19] you know so we got a proposal from this
[44:21] one and then
[44:24] right from this one it's doing some more
[44:27] checking. So yeah I think that's all I
[44:30] do so far. And also if you know if
[44:31] you're specifically doing review you can
[44:33] just say review with you know opus
[44:38] 4.6 and GBD 56 soul. I don't tend to use
[44:42] review as much right now. Sometimes I
[44:44] do. Um but the co-pilot cloud agent
[44:47] review is way pickier in like a good
[44:49] way. So you know it's I I might start
[44:52] off with the slash review. Um but it
[44:54] tends to be a lot nicer, more forgiving.
[44:58] Uh so it's a good first check to make
[44:59] sure you didn't do anything like
[45:00] completely wild. Uh but that co-pilot
[45:03] cloud view agent is you know much much
[45:06] quicker uh much bigger. So yeah so
[45:09] that's what I would say is that you know
[45:11] if if you just say something like this
[45:13] it will naturally go off and use sub
[45:16] agents. It just it just knows that
[45:18] that's what it should do when you've
[45:20] asked it to use multiple models.
[45:23] So maybe hopefully that's what you were
[45:26] talking about.
[45:28] Um uh I I don't think the app already
[45:31] implements an architecture to use
[45:32] several models.
[45:34] Of course, auto mode would use you know
[45:37] a fancier model if if you were in auto
[45:39] mode, right? That would use a fancier
[45:41] model but just for that task. It as far
[45:45] as I know it doesn't have any sort of
[45:46] mode where it's automatically farming
[45:47] stuff out except for when you're using
[45:49] like skills right the skills you know
[45:52] like review already expects you to ask
[45:55] it to you know give multiple models like
[45:58] kind of that's built into it. So some of
[46:00] the skills kind of expect you to use
[46:02] them, you know, to to maybe ask for
[46:04] multiple models,
[46:06] but uh yeah, that's say you can just ask
[46:10] it. You can just ask things.
[46:15] That's a good Yeah, it's a good
[46:16] question, too. I should I was even going
[46:18] to tweet about this. I should need to
[46:20] remember where I was doing it because I
[46:22] thought it was really great how easy it
[46:23] was to do because that's one of the big
[46:25] advantage of Copilot is that it's so
[46:27] easy to to do that parallel farming out.
[46:31] Um, okay. What?
[46:34] Okay. What else?
[46:37] Let's go back to the news. See if
[46:41] there's anything else. Okay. All right.
[46:43] So,
[46:45] agent plugins. All right. Let's see.
[46:47] Meta has a new openweight model. I see a
[46:50] lot of excitement about that today. That
[46:51] was like just today, I think, the
[46:53] glimmer one. So, people are starting to
[46:57] play around with that. Of course, like
[46:58] Llama 3.18B, they released a few years
[47:00] ago, and that was like the first like
[47:01] really good openweight model. So, you
[47:04] know, maybe this one will be just as
[47:05] good. 30B, I don't know if I can run
[47:07] 30B. My laptop started making popping
[47:10] sounds when I ran a 20B, so I don't
[47:12] think I'm going to run a 30B,
[47:14] but let's see if there's Wait, are there
[47:16] smaller versions of it, too? It just
[47:18] says 30B. Let's check all Llama. Does
[47:20] the llama have it? Glimmer.
[47:24] use glimmer dated 13 hours ago.
[47:28] Yeah, that's pretty big. That's pretty
[47:31] big. It's only 30B. There is a 30B MLX
[47:33] which might work better on the Mac. I
[47:36] think MLX is the one that works better
[47:37] on the Mac, but
[47:40] yeah,
[47:42] maybe I'd be kind of scared. MLX is for
[47:46] Mac.
[47:47] I'm just I to be honest I haven't run an
[47:50] openw weight model since the popping
[47:52] sounds incident because I just really
[47:53] don't want to like pop hardware.
[47:57] So I'm kind of too scared. Let's get
[47:59] Wait, is it on can I run.ai?
[48:02] Do we have Muse here yet? Muse? No, they
[48:05] haven't added or glimmer. Glimmer. No,
[48:07] they haven't added it yet because you
[48:09] know it says Okay, 32B. It says actually
[48:12] that 32B
[48:16] should work. I mean, surprising thing is
[48:17] that Why did it Why did it pop?
[48:21] We can
[48:23] do I want to download this while I'm
[48:26] streaming on Discord.
[48:30] Well, you know, the worst that happens
[48:32] is it disconnects.
[48:35] Oh, yeah. You're telling me I need a I
[48:37] need to get a Windows box, don't I? A
[48:38] Surface RTX.
[48:42] Yeah. Well, if if Microsoft gives you
[48:44] one for free, I'll take it
[48:47] to download the the newest version.
[48:49] Okay. So, I don't even have Maybe they
[48:51] improved MLX support in the latest.
[48:59] Hey, now we're downloading
[49:02] Lama.
[49:07] Even that takes fair amount of time.
[49:11] I don't know how long it's going to take
[49:13] to download 18 gigs for glimmer.
[49:22] I wonder if we're going to get Wait, do
[49:23] we have glimmer in? Because if it's on
[49:25] hugging face then
[49:29] let's see models.
[49:32] Always better if I can use my
[49:36] not here. Muse.
[49:38] Muse. Image to image. Nope. Oh, we have
[49:41] our own model called Muse. Oo. A world
[49:44] and human action model. Wham.
[49:47] Okay.
[49:53] Right. It is pooling. That's going to
[49:55] take a while.
[49:58] I don't think we'll be able to out
[50:01] during today's office hours. Okay, let's
[50:04] see. So, that was cool.
[50:08] Of course, there was the big hugging
[50:10] face incident and then there was a black
[50:12] hat talk about it. A lot of people found
[50:14] that really interesting. Um, so, you
[50:18] know, from a security perspective, if
[50:20] you're interested in, you know, in the
[50:23] that that incident, you know, check this
[50:26] out.
[50:27] You know, you should be really careful
[50:28] when you sandbox something that you have
[50:30] very much sandboxed it
[50:34] is that we keep finding out is that a
[50:36] lot of sandboxes are not true sandboxes.
[50:40] Let's see what else. Um I am I did build
[50:43] a repo using pedantic AI and this new
[50:45] Playright capability that they're
[50:47] building. Um it's still in PR but we're
[50:50] going to release it really soon. So if
[50:52] you're using pedant guy with playright,
[50:54] you could check that out. I'll be
[50:57] updating it once they do the release.
[50:59] I've also been experimenting with
[51:00] Gemini. So I actually have this is a
[51:02] Gemini agent. And this is just me doing
[51:04] a comparison to see be able to compare
[51:07] Foundry to the Gemini experience. And of
[51:10] course, you know, there's a lot of
[51:11] things in common, but there's also a lot
[51:12] of things that are really different. So
[51:14] now I'll have a better idea for you know
[51:16] for those of you are you know probably
[51:18] going across different clouds
[51:20] you try and get a feel for what the
[51:22] differences are.
[51:28] Oh, James says, "Yeah, there's a lot of
[51:30] complaint that when we have these
[51:31] security incidents is that, you know, it
[51:34] basically turns into a marketing thing
[51:35] and people aren't like really,
[51:38] you know, treating it as like a, you
[51:40] know, like a true like retrospective
[51:42] postmortem situation that, you know,
[51:44] people are using it for marketing like
[51:45] to brag
[51:47] the fact that it was able to escape
[51:51] and then and then other people other
[51:53] models start going like, "No, but mine
[51:55] escaped even harder."
[51:57] I don't know. Yeah, we should just It's
[52:00] just a good reminder to really care
[52:03] about security and responsibility
[52:06] even if other people aren't.
[52:10] >> Let's see. On that note, we are going to
[52:12] have a live stream about ACA sandboxes.
[52:14] That's September 30th. That's coming up.
[52:17] MC Live is the big stream we have.
[52:20] That's going to be our next stream on
[52:21] September 9th.
[52:24] And uh let's see. And then we also have
[52:27] a co-pilot dev camp summit. So there's a
[52:29] bunch of live events. So if you haven't
[52:32] yet, you know, do register for these
[52:38] live events. Let's stick these all in
[52:40] here. And then I see there was a
[52:41] question. Okay.
[52:44] Um, do I find myself dealing with
[52:47] projects with many markdown documents
[52:49] for documentation and project
[52:50] management? Best practices used OKF
[52:53] schemas, rules, etc.
[52:57] I do not I think that's something
[52:59] probably a lot of the yeah product
[53:00] managers are dealing with um
[53:05] and a lot of my PM friends are writing
[53:07] lots and lots of agent skills
[53:10] and you know you know you can do
[53:12] something like making an auto wiki or
[53:15] something like that but I yeah I I
[53:17] haven't had that
[53:20] yet so I haven't tried anything fancy uh
[53:22] I haven't even tried obsidian right like
[53:24] that's what everybody uses for authoring
[53:25] their markdown. I've thought about it
[53:26] because right now I don't have a great
[53:29] um personal markdown authoring system,
[53:34] but uh yeah, I would say I'm pretty
[53:36] early days when it comes to markdown. I
[53:38] actually really for a long time hated
[53:40] Markdown because I love HTML so much and
[53:42] so I was mad that you know everyone was
[53:45] using markdown for everything when it's
[53:47] not as expressive as HTML. But now I get
[53:49] it. Like now I appreciate markdown for
[53:52] what it is that you know a lot of times
[53:53] markdown you know is the the best of
[53:55] both worlds. It's not too fancy but it's
[53:58] just enough.
[54:00] Okay. So Justin also says agent skills.
[54:02] Yeah. So agent skills are helpful with
[54:03] this if you control the repo. Tell
[54:05] agents I need to check the docs for
[54:06] publishes self-document. Oh yeah. We are
[54:09] actually like when I'm doing this Gemini
[54:10] one. Um we have um so I guess I I'm
[54:14] doing a little bit with this. Um, so
[54:16] while we're doing this like test here,
[54:18] we have this like ease of use journey.
[54:21] MD, we have working diary.mmd
[54:26] and to-do.md. And then all of this is
[54:29] managed via an agent skill. So I have
[54:31] this agent skill and every time I start
[54:33] off a thread, I reference a skill just
[54:36] to make sure it it just keeps
[54:38] referencing it. Like ideally it it would
[54:40] bring it in but but yeah so you know it
[54:44] says okay maintains a discipline
[54:45] sharable record. This is how you're
[54:48] going to first set it up if it doesn't
[54:49] exist yet right these are the files
[54:51] you're going to make link them append
[54:54] blah blah blah.
[54:58] So
[54:59] yeah. So I I guess I am doing a little
[55:01] bit of this just for this one because
[55:03] we're all trying to have consistent
[55:05] markdown files as we test out
[55:09] test out different things on different
[55:10] platforms. And so this is helping, you
[55:13] know, making sure it keeps them, you
[55:16] know, mostly up to date.
[55:18] You can see like different timestamps.
[55:21] There's a lot of info in here, though.
[55:23] Like, so I feel like this is the kind of
[55:25] stuff where we're going to like take the
[55:26] markdowns and then pipe them to an LLM
[55:28] for summarization because it's it's very
[55:30] verbose. And I think that's one of the
[55:32] hard things is like, okay, like if you
[55:34] just want to get like everything out
[55:35] there that you can look through later,
[55:37] great. Like it's basically like your the
[55:39] traces of your work. But in terms of
[55:42] human readability, I wouldn't say that
[55:44] these are like particularly human
[55:45] readable. Even the to-do.md like
[55:47] sometimes I read the stuff it writes and
[55:49] I'm like, what are you even saying? like
[55:51] what words are you using? Because it
[55:54] like these models, especially these
[55:56] frontier models, tend to use like really
[55:59] technical uh like unnecessarily
[56:02] technical
[56:05] descriptions for things. So, a lot of
[56:07] times I'll push back and be like, what
[56:09] did you actually mean by this? Like, can
[56:10] you like explain this more simply? So,
[56:14] yeah. So anyway, so that's something to
[56:16] keep in mind is that if LLMs are
[56:17] updating your markdown for you, you you
[56:21] know, you have to think about whether
[56:22] human readability is a goal or if you
[56:25] only care about LLM readability.
[56:29] All right, we are at time now. Uh so
[56:34] that was really cool. I'm glad we had an
[56:36] opportunity to try out agent plugins and
[56:41] get a lot of feedback what it needs to
[56:44] be improved about the developer
[56:45] experience for installing those and
[56:47] testing those out.
[56:50] And yeah, so hopefully I'll see you next
[56:53] week. Should be back next week. And also
[56:56] register for our live streams.
[56:59] Where did the cats go?
[57:02] Okay.
[57:04] Bye everyone. Have a good day.
