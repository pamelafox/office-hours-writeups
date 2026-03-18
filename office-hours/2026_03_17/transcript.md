[00:00] Welcome to our office hours today on
[00:03] March 17th. Pretty sure today is March
[00:06] 17th. Let's double check. Yes, it is.
[00:09] Which means it is St. Patrick's Day. And
[00:12] I am at least 116th Irish, maybe.
[00:17] So, yay. Um, happy St. Patrick's Day to
[00:21] all who celebrate. And that is why
[00:23] everything is green today. All right. So
[00:26] I always start off with um you know news
[00:29] that I think might be helpful for
[00:32] everyone. So on the Foundry side, the
[00:36] Foundry agent service is now generally
[00:39] available. Uh so here's the blog post
[00:43] about that. Oh, yep. The screen stopped.
[00:46] Thank you. That's Discord. All right. So
[00:48] we're going to
[00:50] reconnect the screen. Thank you.
[00:54] All right. Hopefully that'll be
[00:56] Discord's last green stop today. There
[01:00] we go. We're back. All right. So, the
[01:02] Foundry agent service is now GA. Um,
[01:07] which includes compatibility
[01:10] with many models, private networking,
[01:13] um, connection to tools, MCP servers,
[01:17] uh, interesting MCP authentication. I'll
[01:21] have to look and see how that's
[01:22] implemented. Uh, voice live, so real
[01:25] time text to speech. I haven't tried
[01:27] that one yet with Foundry Agents.
[01:29] Evaluations,
[01:30] um, continuous evaluations
[01:34] and hosted agents are still in preview.
[01:36] So, some stuff are still in preview. Um,
[01:38] but quite a lot is now generally
[01:41] available.
[01:44] Uh, MCP off pass through. Okay.
[01:48] Oh, okay. Voice Live is also preview.
[01:50] Okay. So that's I was wondering I hadn't
[01:52] seen that before. That's that's new.
[01:56] And then evaluations and this is using
[01:59] the OpenAIS SDK combined with the Azure
[02:02] AI project SDK. And I have not used this
[02:06] particular way of doing evaluations. Um
[02:08] so I need to I need to try this out as
[02:12] well.
[02:14] and hosted agents still preview
[02:18] and there's a video uh walking through
[02:21] it.
[02:24] So there you go. Uh if you've been using
[02:26] Foundry agents, that's good news for
[02:27] you. If you've been postponing using
[02:29] them because you're waiting for them to
[02:31] be GA, then also good news. Uh you can
[02:33] see all the examples out here are in
[02:35] Python. Um you can use it from other
[02:39] languages too, but this is Python office
[02:41] hours, so we like that. And uh yeah,
[02:44] I've actually been using it in the last
[02:46] week, combining it with uh Foundry IQ,
[02:49] Azure AI search, and it's been working.
[02:53] Okay, so there's that. Now, there's lots
[02:56] of news on the GitHub copilot front. And
[02:58] remember when we say kit, GitHub
[02:59] copilot, GitHub Copilot is now in so
[03:02] many places. So it's in VS Code, which
[03:05] is where I use it the most. And um today
[03:08] they're just rolling out GD 5.4 Mini.
[03:12] And normally I would not use a mini
[03:15] model for coding, but it does have uh a
[03:19] 0.33x multiplier, which is really really
[03:23] cheap. Uh so if you have some tasks that
[03:26] GB54 mini could uh could work for, uh it
[03:31] sounds like maybe it's good for
[03:32] searching um maybe a light refactor. So
[03:38] yeah, so check check that out as a very
[03:40] cheap um frontier model available now.
[03:44] And then where else do we have copilot?
[03:46] We have the copilot CLI. The copilot CLI
[03:48] is GA actually it went G a few weeks
[03:51] ago, February 25th. Uh so if you are a
[03:55] CLI user, um I've got it open last
[03:58] night. Last night I used it because my
[04:00] Photoshop wouldn't open because I didn't
[04:02] have enough RAM. And so I told it like I
[04:06] just said, "Hey, stitch together these
[04:08] two files. Put one on top, one on the
[04:10] bottom." Right? So I I used it for a a
[04:14] quick uh quick Photoshop alternative. Um
[04:19] here I have an example of the Cop CLI
[04:21] connected to an MCP server that it can
[04:23] search. And this is actually a a Foundry
[04:26] IQ um knowledge base, Azure AI search
[04:29] knowledge base. And so it's able to to
[04:32] uh search that knowledge base, right? So
[04:34] you can connect your CLI to MCP servers
[04:39] and um
[04:42] you know use it to access local files.
[04:44] There's all all kinds of things you can
[04:46] do with the CLI. Um
[04:50] so yeah, so definitely check that out if
[04:53] you haven't yet.
[04:56] Then um there's related to that there's
[05:00] co-pilot metrics. Uh so let's see
[05:03] co-pilot usage metrics. Yeah, there were
[05:06] various announcements around co-pilot
[05:09] metrics um both for enterprise and
[05:12] non-enterprise. So I guess there's I
[05:14] haven't even looked at co-pilot metrics
[05:16] but if you're especially if you're using
[05:18] GitHub enterprise like people want to
[05:20] see how their employees employees are
[05:23] using GitHub copilot. So there's a whole
[05:26] there's all this stuff around metrics.
[05:28] Now
[05:30] um the other one. Okay. So we did the
[05:33] CLI, we did the metrics. Let's just
[05:35] close things we've done um
[05:41] or mini. All right. And the thing I
[05:42] really like is this. And this sounds
[05:44] like such a minor thing, but the other
[05:47] place that GitHub Copilot exists is
[05:49] inside your repos, right? So what you
[05:52] can do is assign a um you know assign
[05:58] something to copilot right so let's see
[06:00] this this is one I assigned to co-pilot
[06:03] and the thing that's annoying is that
[06:05] typically oh this one I already approved
[06:07] it but usually it won't run the CI until
[06:10] you approve it and that basically means
[06:12] it's really hard to work with it but now
[06:14] finally you can skip approval for this
[06:17] so that makes it much more
[06:20] much more practical Um, so that's in a
[06:22] repository setting. So I actually I even
[06:25] have uh this documentation open because
[06:28] I want to I want to actually set this
[06:30] up. So I'll just go ahead and set this
[06:32] up here so we can see how it happens. So
[06:34] we click on settings
[06:38] and then code and automation. Code
[06:43] code and automation. I don't see it.
[06:45] Okay. Edit it in the code and select
[06:47] co-pilot and then coding agent. Oh,
[06:49] that's code and automation. Okay.
[06:51] Copilot coding agent.
[06:55] Okay, so we have firewall allow list
[06:57] require approval.
[07:00] All right, now I can turn that off. Yes.
[07:03] Okay,
[07:05] so that is really exciting to me because
[07:08] now now finally
[07:11] co-pilot is going to be useful. Let's
[07:13] see if there's anything I can assign to
[07:14] co-pilot right now. Let's see any of
[07:16] these broken. Broken. Broken. That one's
[07:19] broken. Okay.
[07:21] Um All right. So I'll just make a new
[07:24] issue. So we go here and say
[07:30] upgrade pedantic properly.
[07:33] This PR failed
[07:36] check its CI logs and make a new PR that
[07:39] does it right.
[07:42] Okay. So I make a new issue.
[07:45] Um I create it. I assign it to co-pilot.
[07:52] Assigning. All right. So now co-pilot uh
[07:56] co-pilot sees it. See the little eyes.
[07:58] Copilot's like, "All right, I'm on you.
[08:00] I'm on it." And yeah, and so it should
[08:02] start working on it. And then it's going
[08:03] to send a PR. And so we'll see uh we'll
[08:06] see how that PR looks. Uh there's even
[08:08] you can see it immediately makes a draft
[08:10] PR. Um but that's there's nothing in
[08:12] that draft PR when it starts. It just
[08:14] starts off always with a draft because
[08:16] that's where you can kind of watch its
[08:18] work. Says here you can say like view
[08:19] session and we can see what it's doing.
[08:21] And that's quite interesting because you
[08:22] can see where it goes wrong and that's
[08:24] if you see where it goes wrong then you
[08:26] can like edit your agents.mmd to you
[08:30] know give it better guidance. Um I've
[08:33] discovered that you know upgrading
[08:34] Python dependencies is the most
[08:36] difficult thing that an you know an
[08:38] agent could ever do. So I I often give a
[08:40] lot a lot of guidance in my agents.mmd.
[08:44] Uh so it's still working on here. So
[08:46] it'll ping me when it's ready. Uh so I
[08:49] see the question there's no need to
[08:50] create tokens for co-pilot now. Uh I
[08:54] don't think I've I don't think that I've
[08:55] ever had to make tokens for co-pilot
[08:58] coding agent. Um
[09:02] yeah, it depend when when did you have
[09:04] to make tokens before? Did you have to
[09:05] make it for the coding agent?
[09:08] Uh it's I I've been I have been using
[09:10] the coding agent for quite a while
[09:12] because I I have this
[09:14] um you know this
[09:17] repository here and this repository
[09:20] basically because I have like hundreds
[09:21] of repos right so this repository like
[09:23] auto assigns issues to copilot across
[09:25] all the repos but I kind I stopped using
[09:28] it because of this issue where you know
[09:31] I was basically babysitting the PRs and
[09:33] telling copilot hey the CI failed hey
[09:36] the CI failed
[09:38] um you know and having to approve the CI
[09:40] to run each time. So I'm hoping that if
[09:42] this really works that then I can start
[09:45] using this again and programmatically
[09:46] assigning issues to Copilot and having
[09:48] them all go through.
[09:52] Um
[09:55] all right so I see some more
[09:58] questions. Let's see. OpenAI wants to
[10:01] see your code. Uh well here we're not
[10:04] we're using Azure OpenAI to clarify
[10:07] Azure OpenAI has a pretty good um
[10:10] privacy policy. So um you know if you're
[10:15] in terms of like what's going through
[10:17] the the Azure infrastructure right your
[10:21] prompts completions embeddings and
[10:22] training data are not available to other
[10:23] customers not available to open AAI or
[10:25] their direct models priority blah blah
[10:27] blah are not used to train right I know
[10:29] a lot of people think that I mean
[10:30] obviously like GitHub co-pilot the
[10:32] codebase I believe that is used to train
[10:34] right so um if I'm checking code into
[10:37] GitHub
[10:38] uh but in terms of what we're sending to
[10:40] the LLMs
[10:42] when we're using these Azure models like
[10:44] Azure OpenAI then this privacy um policy
[10:48] applies here right uh so uh I think
[10:52] that's that's good
[10:55] um okay
[10:57] so can I talk about claude well claude's
[11:00] a big topic um are we talking about
[11:04] Claude code
[11:08] what was the other one co-pilot
[11:10] um cla anthropic models.
[11:14] Um I think I don't even have I used to
[11:17] have claude on my machine, but I
[11:18] recently had to delete a lot of stuff
[11:20] off my machine just to make space. Okay,
[11:22] I don't have claude on here anymore.
[11:25] Um I do of course use anthropic models
[11:28] quite a lot that my default model is
[11:31] opus 4.6
[11:34] um even though it does have a 3x
[11:36] multiplier.
[11:37] Um Claude Co. Okay.
[11:41] Yeah. I also got asked this week if I've
[11:42] used Microsoft Copilot. Uh co Microsoft
[11:45] Co-work. Um can we download Cloud
[11:48] Co-Work for free? Uh no, I don't want
[11:51] Windows. Okay, let's see.
[11:58] Uh I and I believe I do have the ability
[12:00] to test out our Microsoft co-work as
[12:02] well, but I think that's all private for
[12:04] now. So, uh, I don't think I should test
[12:06] that right right now until it's a little
[12:09] more public. All right, let's try.
[12:15] And I heard that our Microsoft version
[12:17] of this is very similar. So, let's see
[12:20] if this is a nice experiment experience.
[12:26] All right. Well, that just looks like
[12:28] Claude.
[12:30] Okay. Oh, okay. So, it's just part of
[12:33] Claude. I could have just kept Claude.
[12:35] All right, let's go here and find
[12:39] Claude.
[12:42] Uh, well, we'll see.
[12:46] I think I have enough storage space on
[12:47] my machine. I did. So, I I ran this cool
[12:51] app that shows you like how much space
[12:53] is being um used up on your machine and
[12:55] discovered it was like all these small
[12:57] language models that were um stuffing up
[13:00] my machine. So, I cleared off a lot of
[13:03] cached small language models. All right,
[13:06] we're going to continue with Google.
[13:14] Let's see.
[13:25] A wrapper on Claude. All right.
[13:32] Okay.
[13:37] Oh, you can. Okay. So, they do want your
[13:39] data to train models. All right. I
[13:41] turned it off. Okay. So, then it says
[13:43] you do the Oh, I What is that? Oh,
[13:45] Incanita. That is cute.
[13:50] That's really cute. Okay. Um, let's see.
[13:52] So, we find that it said download.
[13:54] Navigate to the top toggle and choose
[13:56] which product to work in. Is this the
[14:00] You can see. So, I have used it before.
[14:03] Um,
[14:04] all right. So, how the top toggle I
[14:07] don't really The top toggle looks like a
[14:08] ghost. Um, has anyone figured out how to
[14:12] get co-working
[14:14] here? Uh, let's see.
[14:23] Oh, maybe up here
[14:26] file.
[14:29] Maybe I need a subscription. Yeah, maybe
[14:30] you do need a subscription. Let's see.
[14:32] Down up. Oh, open to all paid uses. Not
[14:35] on a paid plan upgrade now. Oh gosh, I
[14:38] don't So, here's the thing. I don't pay
[14:41] for things anymore.
[14:44] Um, yeah, I'd have to pay. I don't
[14:47] really
[14:49] want to pay because I don't feel I need
[14:51] to pay because I basically use GitHub
[14:54] Copilot for everything. Or the other
[14:57] thing I use is
[14:59] um this
[15:01] um responses API wrapper that my
[15:04] colleague wrote and I just use it with
[15:06] um with a a GPD model 54 model that I've
[15:10] deployed right and you know it's like
[15:14] it's just like a vibecoded chat app but
[15:17] as it turns out that's that's all you
[15:19] need. Um, I'm sure that like co-work has
[15:22] lots of other stuff. Maybe it has like
[15:24] better tools and stuff, but when you use
[15:25] responses API, you get web search and
[15:28] you get code interpreter. And if you
[15:30] have web search and code interpreter,
[15:31] then you can do you can get so many of
[15:35] your questions answered, right? And then
[15:37] we could add MCP servers. So, currently
[15:40] I don't pay for chat GBT. I don't pay
[15:42] for claude. I don't pay for co-pilot
[15:44] only because my my company pays for it.
[15:47] If I was going to pay for anything, I'd
[15:48] be paying for co-pilot. I know how much
[15:49] I spent in the last month. It was like
[15:51] $800 on Copilot. Probably because I'm
[15:54] always using that um 3x. Actually,
[15:57] there's one that has a 6x multiplier and
[15:59] I'm usually using the one with 6x, but
[16:01] that one's secret. So, right now, we'll
[16:03] pretend I'm using 3x.
[16:05] Um
[16:08] so, John asks, "How does the web search
[16:10] and co-interp work for responses API?"
[16:13] Uh yeah, let's try and prompt it to use
[16:15] it like um search the web for the best
[16:20] um goro dame recipe. All right. And I'll
[16:23] just make sure we got it turned on. Web
[16:26] search low. Okay. All right. So, let's
[16:29] see. Let's see if this is going to work
[16:34] for us. Okay. It is reasoning about it.
[16:41] Um where does the code get executed and
[16:42] which search provider is used? It is
[16:44] using Bing. So this is basically like
[16:47] the like similar Bing grounding if you
[16:49] um you know the Bing grounding right. So
[16:52] it's this is all via Bing um and the um
[16:57] let me see if we can see the JSON that
[17:00] comes back. Okay.
[17:02] So we can see the reasoning. It says
[17:05] it's searching and then we can see it
[17:07] made the web search call and it says
[17:10] what queries it sent in. So it actually
[17:13] sends in multiple queries. So it does a
[17:15] little you know you know a little query
[17:17] planning there decides it's going to
[17:19] send in multiple queries. Um and then
[17:24] uh d oh I had one more reasoning and
[17:28] then in the okay in the output you get
[17:32] annotations. So, here's the thing. You
[17:33] don't get access to the full text
[17:37] because of being licensing reasons. Uh,
[17:40] like you don't even get access to a
[17:41] snippet, but what you get is the
[17:43] citation so that you can make URLs,
[17:45] right? So, we did get a bunch of URLs
[17:46] here. Um, we get the right. So, we get a
[17:50] bunch of URLs and then you you get the
[17:54] answer, right? So it works it works a
[17:57] bit different than a standard tool call
[17:59] because of the licensing
[18:02] issues. So we we don't get to see
[18:06] exactly what um you know if you were
[18:10] using like Tavi or some other perplexity
[18:12] whatever like some other web search
[18:13] service you'd make the tool call and
[18:15] you'd probably see back like snippets
[18:17] from the web pages and then the LM would
[18:20] form the answer based off the snippets
[18:22] but you'd still see the snippets but
[18:23] because of being licensing reasons uh we
[18:26] don't get to see the snippets uh at
[18:28] least not currently uh we just get to
[18:30] see the URLs and the final answer. Um,
[18:36] uh, so and so John asked, does it only
[18:38] work for Azure OpenI, not OpenAI? I
[18:40] thought OpenAI had their own access to
[18:43] the same, you know, basically the same
[18:45] service. Do they not? Let's see. Um,
[18:50] function quick start extend the model
[18:52] tools
[18:54] uh, file search. Okay, it does have file
[18:56] search. That's you can see I have file
[18:59] search here.
[19:01] Um tool search function calling remote
[19:04] MCP.
[19:06] Oh,
[19:10] web search. Here we go. Okay. Um
[19:14] use Yeah. So you just have to configure
[19:15] it. So I I think I believe it uses the
[19:18] same um underline
[19:21] underline Bing call, right? And so you
[19:23] can see it gets the search. It does the
[19:26] search and it can either open uh it can
[19:28] do search sorry it can do search it can
[19:30] do open page or it can do find in page.
[19:32] Um and then you get back the message
[19:34] with the text and the annotations.
[19:37] Uh so here's yeah so this is this looks
[19:39] like what we were showing. Let's see you
[19:42] can do domain filtering
[19:45] uh diet limitations
[19:48] okay when using tools
[19:51] and some rate limits. I have run into
[19:53] the rate limits. You'll notice when I
[19:56] set it up, I did search context size uh
[19:59] low. Uh when I had medium and high, I
[20:02] ran into some rate limits, I think. Um
[20:06] just because I I'm uh my deployment
[20:08] doesn't have that many tokens, I think.
[20:11] Uh yeah, good question. Do you pay extra
[20:13] for using the service? There's only the
[20:15] token consumption.
[20:19] It's a very good question. I'm glad
[20:21] you're asking it so I can learn. Uh
[20:23] let's find let's see using that web
[20:27] search. Okay. So here's our Azure.
[20:31] There's the Azure thing here. Okay. Web
[20:33] search
[20:35] uh web search preview tool.
[20:39] Okay.
[20:41] Blah blah.
[20:43] Oh so many so many things from legal.
[20:46] Good good good. Okay.
[20:52] Deep research. Okay. All right. We do
[20:54] it.
[20:57] Control results. All right. So, use the
[20:59] deep research model. Okay. I don't think
[21:00] anyone uses that anymore. Okay. All
[21:03] right. So, what the heck is the pricing?
[21:08] Um,
[21:12] as your opening eye responses pricing.
[21:20] Oh, we want Bing web search.
[21:25] Okay. Will incur costs. Learn more about
[21:28] pricing. Incur costs. Oh, okay. I This
[21:31] is why you should always read the things
[21:33] that say important. Okay. All right.
[21:36] Important. Grounding with bringing
[21:38] pricing details. All right. Here we go.
[21:42] Um, so what did we see here?
[21:49] All right. $14 grinding with Bing. We
[21:52] were just doing normal search, Bing
[21:54] search. So that's um 150 transaction per
[21:56] second. Okay. $14 per,000 transactions.
[22:00] Okay. So yeah, if you had like a user do
[22:06] well, no, if you had like a thousand
[22:07] users do one web search a day, then
[22:08] that'd be $14, right? Um
[22:13] so is that reasonable? I don't I can't
[22:15] even reason about what I think it's like
[22:18] sounds it sounds reasonable.
[22:22] You think it's steep? Okay. I don't know
[22:23] that that compares to like I guess we
[22:25] could look at like Tably, right? That
[22:27] would be the the other equivalent. Um
[22:31] it looks like they've got different
[22:32] pricing models. So this one they do have
[22:35] a free level pay as you go. All right.
[22:38] So they're doing it a bit different. So
[22:41] each request costs one API credit.
[22:44] Okay.
[22:48] All right. I don't know if I can do the
[22:49] math fast enough to see. Um,
[22:54] okay. If it's a thou, okay,
[22:57] 4,000, monthly price 30. Oh, it's not
[23:00] that different. Then four like monthly
[23:02] price 30 for 4,000 and one request is
[23:05] 4,000. So, I think it's tably is about
[23:08] half half the pricing. Oh, duck. Go. Are
[23:11] people using that? Duck. Go pricing. I
[23:13] just feel like all the tutorials
[23:16] but do they have like an MCP server like
[23:20] um
[23:21] yeah I wait do they actually have one?
[23:23] These all look not official.
[23:26] So unless they have like how are you
[23:28] integrating with DuckGo? I don't see an
[23:31] obvious
[23:33] Oh, there we go. There is an MTP server.
[23:35] Let's see how much does Duck Duck. Go
[23:36] cost. Uh advance the personal and duck
[23:41] go search are all free. Uh, where's MCP?
[23:46] MCP.
[23:51] I don't really see an MCP server here.
[23:55] Does anyone see a way that you would
[23:56] programmatically connect your agents to
[23:58] Duck? Oh, yeah. I feel like these are
[24:00] all unofficial. Oh, and XA. Yeah, EXA is
[24:03] the one that ever Yeah, that's the other
[24:05] one I heard about a lot. Exa MCP. All
[24:08] right, so we got Exa. So this one is
[24:13] seven different levels of search. Um
[24:15] it's like deep versus not. Okay. This
[24:17] one's $7 for one query request. All
[24:18] right. So generally I feel like Tavi and
[24:20] Exa are half the price.
[24:23] Um that to me seems reasonable. Like I
[24:26] mean Microsoft is not generally going to
[24:27] be the cheapest option for for
[24:30] everything, right? Because we're usually
[24:31] adding on like additional, you know,
[24:33] enterprise controls and stuff like that.
[24:35] So it's it's not like it doesn't seem
[24:37] like it's a magnitude. It's not like 10
[24:39] times more expensive. It looks like it's
[24:40] twice as expensive over here. I'll share
[24:45] this one. Oh, there's an SDK for Dr. Go.
[24:47] Okay. Yeah, I just don't know if
[24:49] anyone's um All right. So, maybe you
[24:52] would just have to pay whatever
[24:57] their pricing model is. Um but like Tavi
[25:00] and Exa are both, you know, basically
[25:02] designed for a gentic use. Okay, here we
[25:05] go. Thank you, John. Yeah, we're looking
[25:08] at that one.
[25:15] I still don't really see which one we'd
[25:16] be paying for as a Oh, Google. We're
[25:21] going to bring up Google. No, obviously
[25:23] I use Google as well. Um, uh, let's see.
[25:26] Pricing. This one is
[25:30] $5 per thousand queries. Okay. So, that
[25:33] is a third about a third the price. All
[25:37] right. Well,
[25:39] I can tell the Bing team they're too
[25:41] expensive. Um, but um I think they, you
[25:45] know, we'll see. Uh, I know various I
[25:47] mean when we give feedback like that, if
[25:48] that's the reason that people aren't
[25:50] using it, that's good feedback to give.
[25:52] I know with like Azure AI search, they
[25:54] often get told their um prices too much.
[25:57] So, they are working on some other
[25:58] options. So, you know, you can come to
[26:01] build this year, find out about them. Uh
[26:05] so yeah, it's good good to hear if
[26:09] something's too much if that's the
[26:11] reason why people aren't using stuff. Um
[26:15] so that was with the uh web search API,
[26:18] right? And then we can also try let's
[26:21] see um calculate the exact um recipe to
[26:26] serve 40 people with Goroami. Let's see
[26:30] if this is going to bring up the code
[26:31] interpreter. Uh the thing with a code
[26:32] interpreter is you you I mean obviously
[26:34] I could tell explicitly to use the code
[26:36] interpreter. So maybe I'll do that. But
[26:38] you know you never know when it's going
[26:39] to use the code interpreter. And I have
[26:41] had it use the code interpreter when um
[26:44] doing like recipe stuff, right? Um
[26:49] but it doesn't it doesn't always do it.
[26:51] All right, let's give it let's find it a
[26:54] recipe. Uh let's see. Gard
[26:57] Gorodami. I think I said it wrong. Um,
[27:01] Gora
[27:04] Panzu.
[27:06] Okay. All right. Give me
[27:10] a
[27:11] sushi rice recipe for 40 people. I don't
[27:15] know. I just wanted to I just wanted to
[27:17] interpret something. Use a code
[27:19] interpreter.
[27:21] What is that? I was It was because I was
[27:23] learning about Shaboo Shaboo last night.
[27:26] Um
[27:27] I must gadare
[27:30] gad. Okay, that's what I meant to say.
[27:33] All right, let's see. It is not doing
[27:35] it. Okay. Uh use the code interpreter
[27:41] to check your numbers.
[27:46] Sometimes you can just tell
[27:51] it's really cool and it works. What else
[27:53] did I use it for? like if you wanted to
[27:55] like generate a chart or a table. So
[27:56] here you go. Code interpreter. It's now
[27:59] running the code interpreter
[28:01] and um okay so from fractions import
[28:05] fraction we got all the fractions cups
[28:08] to te and cup half batch blah blah blah
[28:10] output right so you can see this is the
[28:12] code and the code runs in a sandboxed uh
[28:15] environment um on like aure container
[28:18] apps dynamic sessions and then we get
[28:21] back the output and it said okay I
[28:24] checked the math right uh and and Then
[28:28] it it did correct itself a bit there. Uh
[28:30] now let's say generate a chart for
[28:33] amount of vinegar needed as people
[28:38] increase from 1 to 40.
[28:44] All right. I just wanted to see if it'll
[28:45] generate a chart because the code
[28:46] interpreter can also work with files. So
[28:48] it can kind of like save files, output
[28:51] files. Um, you could upload a file and
[28:55] and it could get sent to the code
[28:57] interpreter
[28:59] and uh and yeah, I should point out this
[29:01] app does not have a backend. This is
[29:03] actually all happening in the front end
[29:05] using the like the responses API. All
[29:08] right, so here we go. We it used metplot
[29:11] lib and then um you know we got back
[29:14] that data frame and then it generated
[29:16] the image as well. So here's the image.
[29:19] Oh, it's so beautiful, isn't it? It's
[29:21] just so cool. This is all just a
[29:23] responses API. Isn't that crazy? I just
[29:25] think it's so cool. So, and then we can
[29:26] download, right? So, then we download.
[29:29] So slick. Okay.
[29:32] Uh, right. So, now now we have our
[29:35] chart. Um,
[29:39] so, so yeah. So there's so this is this
[29:42] is why one of my um plans for this week
[29:46] or maybe next week is to port more of
[29:50] our examples from chat completions to
[29:52] responses API because as soon as you're
[29:54] using the responses API you can just
[29:57] like a couple lines of code you can add
[30:00] on these built-in tools and like look
[30:02] how much you know how much more powerful
[30:04] the application becomes when you have
[30:06] access to web search and code
[30:08] interpreter. Like these two tools to me
[30:09] are a really compelling reason to to
[30:11] switch over. Um if the app is only in
[30:14] the front end, are the API keys safe? Oh
[30:16] yeah, it's a good question. I mean the
[30:17] question is who has access to your like
[30:21] that means they're on you know they're
[30:22] so they're they're
[30:25] um they are on the m machine, right? So
[30:27] they actually are stored in um in local
[30:30] storage. Um let's yeah, it's probably
[30:34] going to show you them. don't remember
[30:36] if we're encrypting them here or not. Uh
[30:40] Azure OpenI settings. No, we're not
[30:42] encrypting them. So, we should probably
[30:44] we can probably encrypt them on the
[30:45] machine, but it is on the it's like it's
[30:47] on the So, it's on local storage and
[30:49] then and then you know getting sent um
[30:52] over the network. It is an HTTPS post.
[30:56] Um let me try it.
[30:58] Uh make the chart. Okay. Thank you. I'm
[31:02] just gonna say thank you and then All
[31:04] right. So we send off the request
[31:08] and um this should be a uh this is like
[31:13] a post that's a post over an HBS. So
[31:18] when we're posting you know that is
[31:20] going to have authentication uh should
[31:22] have like a bearer token. Is it a bearer
[31:24] token here? Let's see. payload request
[31:28] payload uh request method response
[31:31] headers request headers
[31:35] bearer. Oh, you can see that.
[31:37] All right. Yeah, you saw the key.
[31:41] All right. So, that I wonder if why did
[31:44] it show that I guess Chrome DevTools
[31:46] does Chrome DevTools always show your
[31:47] bearer token?
[31:49] Yeah, maybe it does. Okay. All right.
[31:52] We'll regenerate that key.
[31:55] don't use it.
[31:58] Uh, and I'll I'll chat to see I don't I
[32:02] still I don't think it's it's a good
[32:04] question. Let's let's actually ask like
[32:05] okay is it a risk if we are sending a
[32:09] bearer token from because I do this a
[32:12] lot actually from JavaScript over HBS
[32:14] post because also when we're like when
[32:16] we have a front end that communicates or
[32:18] the back end a lot of times the front
[32:19] end does like the entra off and it
[32:22] receives a token and it sends that token
[32:24] as a bearer token to um you know to the
[32:28] back end. Uh so yes so if we're doing
[32:31] HPS only send the tokens. Ah so the one
[32:35] issue is that we're sending a key it
[32:38] would be better if we were actually
[32:40] sending a token versus a key because of
[32:42] course also you know tokens are
[32:43] shortlived right and so that is that is
[32:46] a an an issue. It does says avoid
[32:48] storing them in local port um storage.
[32:51] Uh restrict tokens obviously don't put
[32:53] them in euro query params. We're not
[32:54] doing that. So it says generally bearer
[32:56] token over hs is fine. Um,
[33:00] but it would be better if we were uh if
[33:03] we were using uh actual, you know,
[33:06] shortlive tokens versus keys.
[33:12] All right, good good questions. Okay.
[33:16] Uh,
[33:20] token theft in the browser, right?
[33:23] leakage through logs or error reporting
[33:25] or screen sharing
[33:28] overly long live tokens
[33:30] and yeah
[33:34] all right let's see so John V says
[33:39] um how important is system design for
[33:42] multi- aent systems any recommendations
[33:45] to keep up with design architectures or
[33:48] just dig deep um I mean I think I think
[33:53] it's like it's important in terms of you
[33:56] know we talked about this in the in the
[33:58] you know in the agents series we talked
[34:00] about uh various
[34:04] um architectures right um because when
[34:06] we're talking multiple uh you know
[34:09] multi- aent let me just bring up those
[34:13] slides
[34:15] uh you know you different ways that you
[34:17] can coordinate the agents and when you
[34:19] say multi- aent like that could mean so
[34:20] many things because basically You know,
[34:22] there's lots of ways you can um put
[34:25] together multiple agents, right? Uh the
[34:28] most basic one is this one, right? The
[34:29] supervisor agent or the sub agent or the
[34:32] uh agent as tools, right? Where you
[34:34] basically just say, "Hey, you've got
[34:36] these tools and the tools themselves are
[34:39] agents, right? Oh, access denied." All
[34:41] right, I should fix
[34:44] I should fix that URL then. Oh, there we
[34:47] go. All right, that was just a fluke. Um
[34:50] but then we have like other like a lot
[34:52] of other approaches too, right? Uh oh,
[34:55] let me see. I think we did it.
[34:58] Uh here. Okay. Conditional
[35:02] one.
[35:05] Okay. Right. So then we had other
[35:06] orchestrations. Wait, let me do that
[35:08] handoff. I think the handoff is more
[35:10] okay.
[35:12] Right. And then there's this other
[35:13] architecture here with handoff
[35:16] orchestration where um it looks similar
[35:19] but it's actually quite different. And
[35:22] you know so what like what matters is
[35:25] how much context like who who's in
[35:27] charge? Who's going to decide what
[35:29] happens next right? How much control do
[35:31] you have over that? How much context is
[35:34] be giving given to each of your agents?
[35:36] Right? Um are you purposely giving them
[35:38] a lot of context? How are you giving
[35:39] them the context? Are you controlling
[35:40] that much context? How are you managing
[35:42] your context window so that you you know
[35:45] people all the agents have all the
[35:46] information they need but not too much
[35:48] information and you're you know not
[35:49] going over context window limits. Um
[35:53] and uh and yeah so there there's just
[35:56] different
[35:57] considerations there. Um but I think you
[36:01] know you just want to you know put
[36:03] together your system and then and then
[36:05] and evaluate it and see uh you know what
[36:09] what your actual issues are like what
[36:11] are you struggling because you're you're
[36:13] you've got too much context that's
[36:15] getting added that or you is your
[36:17] control out of control and like you you
[36:19] don't know which agent is in charge
[36:21] next. Um, so I would say you you you
[36:25] know, you put it together and then you
[36:26] evaluate it and see what the actual
[36:28] issues are before you say, "Oh, we
[36:31] definitely need architecture X or we
[36:32] definitely need, you know, architecture
[36:34] Y."
[36:39] Um, let's see. So, best says, "What is
[36:41] my opinion about RL on agent Slayer?"
[36:47] I I need to So, I'm actually gonna go to
[36:49] an RL meetup tomorrow because everyone
[36:54] keeps talking about it and
[36:57] I just haven't had time to dig into it.
[36:59] So, tomorrow,
[37:02] well, they said, okay, it's going to
[37:03] talk through RLMs. So, which I think
[37:07] it's related, right? Um,
[37:10] uh, let's see. So, so this is
[37:13] reinforcement learning on the agents
[37:16] layer. Are they fine-tuning it?
[37:21] Uh, like is it like RHF but
[37:25] applied it's applied to the final thing
[37:28] like what what is actually okay policy
[37:30] training blah blah blah. What is
[37:32] changing? Are they changing
[37:36] graceful weight updates? Okay. So, they
[37:38] are they're actually changing the
[37:40] weights on the model that powers the
[37:43] agent. Is that what it's doing?
[37:51] And they love Latte in papers. Okay. Um,
[37:55] yeah. So, I don't uh I don't I don't
[37:58] actually have a a strong opinion. I
[38:00] think generally reinforcement learning
[38:02] has been one of the most helpful parts
[38:04] of generative AI because that is how we
[38:07] have tool calling and structured outputs
[38:08] and safety and less hallucinations and
[38:11] all that stuff, right? So clearly even
[38:13] though reinforcement learning has a lot
[38:14] of issues like if you watched um the
[38:17] Andre uh Parathi
[38:21] uh sorry Carpathy on Dwarish Pat Dwarish
[38:25] Patel's podcast
[38:28] um you know he talked about how like uh
[38:32] reinforcement learning has so many
[38:33] issues
[38:36] but it's also like inc like surprisingly
[38:38] effective right um RL, right? RL is
[38:42] terrible.
[38:46] So funny. Um, but it's also really
[38:48] effective, right? So clearly RL is very
[38:49] effective and I'm happy that we have
[38:51] RLHF um on our LLMs because we've, you
[38:55] know, um, really improved them in many
[38:58] ways and uh, yeah, and it seems like
[39:00] people are applying RL at different
[39:02] points now. Uh, and there's this thing
[39:05] called RLMs, which I don't even Okay,
[39:07] recurs. Oh, so RLM is different. Okay.
[39:10] So, I'm getting confused between
[39:11] reinforcement RL for reinforcement
[39:13] learning and RLM for recursive language
[39:16] models. Okay. Okay. So, I actually will
[39:19] not
[39:20] be hearing
[39:23] about RL on agents tomorrow.
[39:27] Yeah, that's a good idea. Wait, let's
[39:29] try responses API. See if we can get
[39:31] Okay, ready? Can you summarize this
[39:36] paper? Let's see.
[39:39] That's nice. So now, you know, the other
[39:41] reason I like using this responses um
[39:44] app is that, you know, then I can really
[39:47] see what's going on because of course
[39:48] open chat uses responses like behind the
[39:50] scenes, right? Um but, you know, now as
[39:53] a developer, I can like actually see,
[39:55] you know, what's going on. So, it gives
[39:56] me a better feel for, you know, what I'm
[39:58] going to be developing um uh what's
[40:01] working. And you can you can you can all
[40:03] deploy this or you can actually just use
[40:04] it yourself, too. uh if you trust your
[40:07] or you can send PRs to improve the uh
[40:09] security of the keys like maybe encrypt
[40:12] them. Um
[40:15] uh but here we go. So it's just deployed
[40:16] on GitHub pages, right? Okay. So here
[40:19] you can see it does open page, web
[40:21] search, open page, web search, open
[40:23] page, open page, web search. Oh, it
[40:25] wanted to look at the GitHub thing.
[40:26] Okay. All right. So here we go. Oh. Oh,
[40:30] and Nambdi also got a summary. Here we
[40:32] go.
[40:33] Um,
[40:38] okay. But okay, but then what does it
[40:41] actually do? Is it
[40:45] um
[40:46] are they fine-tuning the LLM?
[40:52] A framework that tries to collapse a
[40:54] boundary between deployment and
[40:55] training. Every interaction becomes both
[40:57] useful work and potential learning
[40:58] example. Wait, so that mean like they're
[41:01] doing continual fine-tuning?
[41:04] Okay, so yeah, not just to complete Oh,
[41:10] online RL training. Interesting.
[41:13] Well, you'd have to have like a good
[41:15] machine for doing that. How do you have
[41:18] a machine powerful enough
[41:22] to do online RL training?
[41:28] because I think oftentimes when we're
[41:30] running these models for inference,
[41:32] we're running them on machines optimized
[41:34] for inference.
[41:36] Okay, so online RL means online data
[41:38] collection with asynchronous background
[41:40] training. So you don't have to do it all
[41:41] on a giant machine. Uh survey model
[41:44] interactions log prompt model action
[41:47] next state feedback optional reward
[41:48] judgment goes into a training queue
[41:52] separate geos do the judging or so we're
[41:55] using the LM as a judge here. Okay. Um,
[41:59] a checkpoint is served. Okay, so this is
[42:01] going to be more expensive, right?
[42:02] Anytime we're doing any sort of
[42:04] fine-tuning, that is going to be more
[42:05] expensive. Um, but you know, if you're
[42:07] doing something really domain specific,
[42:09] then then that might be good for you.
[42:12] Um,
[42:14] okay. I'll ask my fine-tuning friend if
[42:18] uh what he thinks about this
[42:22] training.
[42:27] That's cool.
[42:29] Um,
[42:33] nice.
[42:36] Okay. So,
[42:39] yeah, I it sounds interesting. I I would
[42:41] say generally that um you know, anything
[42:44] that relies on having to set up
[42:45] fine-tuning, I don't see as much
[42:47] adoption of it. But, you know, once
[42:49] again, like if if you know, if you
[42:51] really benefit from that, like if if
[42:53] you're really not getting good enough
[42:55] results from the base LLM, then, you
[42:58] know, then that might work. And this
[42:59] this is interesting like if we make it
[43:01] easy to do, uh like if if this becomes
[43:04] commonplace for people to be doing this
[43:06] like kind of almost online RL, then
[43:09] yeah, then maybe we'll start doing it.
[43:10] But it means it has to be like something
[43:12] reasonable that you could run and um and
[43:16] that you know it'd be reasonable to pay
[43:19] for serving your own LLM, right?
[43:22] Generally it's it's more expensive to
[43:24] run your own fine-tuned LLM.
[43:29] Okay, let's see.
[43:32] Uh so Pablo says, "We see more and more
[43:35] SAS providers offer their agents or even
[43:38] tools for agents in their environments."
[43:40] uh they prefer to offer agents instead
[43:42] of being accessed by agents
[43:44] um you know in other providers that
[43:46] access servants if this will be the case
[43:48] there'll be more ato usage and
[43:49] interaction with the most s use the SAS
[43:52] services instead of using MCP what's my
[43:54] impression about this yeah you know
[43:57] you're probably right because then they
[43:58] have like more control now as a
[43:59] developer I don't like it because I if I
[44:03] want to access data I want to access
[44:06] data I want an API an MCP server that is
[44:09] going to give me access to to that data,
[44:12] right? Like already like with this being
[44:14] web search, it's not ideal because, you
[44:16] know, we get back an answer, we get back
[44:18] citations, but we don't actually get
[44:19] back the snippets, right? And there
[44:21] might be some use cases where we'd love
[44:23] to have the snippets. So,
[44:26] um, and and if we're and if these
[44:27] services only offer agents, agents are a
[44:31] wrapper on top of their own data and
[44:34] tools and you're going like that's
[44:35] that's so lossy, right? you have to go
[44:38] through uh you know go through that
[44:40] wrapper, right? Like we actually very we
[44:42] have an example of this at Microsoft
[44:43] which is the work IQ server right it be
[44:46] like um what events are I think I have
[44:49] this connected work calendar for today
[44:52] let's see um and this should use the
[44:56] work IQ MCP server but the work IQ MCP
[45:00] server yeah access to work IQ tools it
[45:02] is actually like an it's an agent it's
[45:04] an MCP server that's just wrapping an
[45:06] agent and um and that means that I'm not
[45:11] getting direct access, you know, I'm not
[45:13] just getting, you know, access to the
[45:14] direct graph API. Luckily, the the graph
[45:17] API still exists. So, if I wanted to, I
[45:19] could, you know, um I could try and
[45:22] connect via the graph API, too. But, um
[45:26] but this is going to use an LLM to call
[45:29] the graph API, answer the question, and
[45:31] then give me back an answer. And I don't
[45:34] like that because I don't know what
[45:36] system prompt their agent is using. And
[45:38] maybe it's like a better system prompt
[45:40] than you know I might come up with but
[45:42] you know for ultimate flexibility as a
[45:44] developer I would prefer that uh you
[45:48] know that that tools there at least
[45:50] should be tools available that are not
[45:53] wrapped in an LLM right for so that we
[45:56] have better direct data access and so
[45:58] that we don't have the lossiness of
[46:00] going through an LLM call and the risk
[46:03] of hallucination um like the work AQ
[46:06] server works quite well for events
[46:09] Um but um but if I use it to like search
[46:14] through my chats then it's much more
[46:16] likely to uh to hallucinate because it's
[46:19] just a lot harder to search through
[46:21] chats and um you know and it it has a
[46:25] tendency to to want to you know answer
[46:30] in a helpful way but it may not be
[46:32] always accurate, right?
[46:34] Uh so yeah, so I I mean I think that
[46:39] you know companies like wrapping in
[46:41] agents because then they feel like they
[46:43] have the control and kind of do like
[46:44] more agentic retrieval on their side,
[46:47] but that means that you know we have
[46:51] another LM in the way between us and the
[46:53] data we're trying to get to.
[47:02] Um, so John asked, "What are my go-to
[47:04] resources for system design interviews?"
[47:08] I don't know that I've necessarily done
[47:09] a system design interview. Like when I
[47:11] would interview people, I would
[47:12] typically interview for full stack
[47:14] developers because I'm like a I'm a full
[47:16] stack web developer, right? So there
[47:20] um you know there I would ask them to to
[47:23] design things that usually involved a
[47:25] front end, a backend and maybe like a
[47:27] cron job or a messaging system.
[47:30] And um I don't remember if I ever like
[47:32] practiced for those myself.
[47:35] Um
[47:36] I'm sure there must be like I know for
[47:39] front end it was always Darcy Clarks.
[47:43] Ellie, do you have system design
[47:45] interview question resources? You've
[47:47] done those more often.
[47:48] >> I failed them more often.
[47:49] >> Oh, you failed them more often. Okay. I
[47:51] was just asking my partner. Um yeah, I
[47:55] remember the these front end ones. So,
[47:56] I'm sure there's ones online. I haven't
[47:59] looked into them for a while. Um you
[48:01] know,
[48:03] uh you know, you want to um I don't want
[48:05] front end. Here we go. Uh you want to
[48:07] know about messaging systems, cron jobs,
[48:10] queuing, like you know, all the um
[48:13] deferred tasks. uh
[48:18] you know that sort of stuff. Um
[48:23] and that's the kind of thing that maybe
[48:25] you haven't always had uh you know had
[48:28] access to. I remember there was a good
[48:30] one that had like mess chain system.
[48:41] Yeah, I don't remember. I I don't have
[48:43] an immediate resource. Um, but that's
[48:46] the sort of stuff I expect people to
[48:48] have some familiarity with if you're
[48:51] going to be designing like a a full
[48:53] system, right? Um, understanding how
[48:55] things go through the system and how you
[48:58] can defer things, how you can schedule
[49:00] things, how you can cue things up when
[49:02] there's different varying amounts of
[49:04] load. um you know uh that sort of thing
[49:07] because that's what happens when you
[49:08] actually deploy something in production
[49:13] is you get all this variable load.
[49:20] Okay, so Pablo says um oh we got a good
[49:24] recommendation systems design.pro. Oh,
[49:27] okay. Let's check this out. Just see if
[49:30] I agree with it. Uh
[49:35] okay. So this more this is like some
[49:38] sort of designing thing. Okay.
[49:43] Yeah. Well, I guess this gives you an
[49:44] idea of what's involved in system
[49:46] design. Although I don't know all these
[49:48] words. I don't know all this compliance
[49:50] framework stuff. Uh but that's because I
[49:53] haven't. I've worked more at startups
[49:55] than enterprise myself.
[49:57] Okay. So Pablo says uh auto research. So
[50:00] this is really cool from Andre Karpathy.
[50:02] I don't know if everyone saw this uh
[50:07] auto research. Okay, so he wanted
[50:10] basically had agents running on his nano
[50:12] chat in order to improve the parameters
[50:15] and he just like forced them to go go
[50:18] keep working working working
[50:21] um and then trying new things um and
[50:24] going over and over and so lots of
[50:25] people had fun with that and he got some
[50:27] good gains from it and he was very
[50:28] impressed. Pablo says, "I've seen it
[50:31] applied to improve a skill. I wonder if
[50:33] we could also use it to prove MCB
[50:34] service servers or even agents created
[50:36] with agent framework or similar." Yeah.
[50:39] So, the thing is you need a validation,
[50:41] right? So, what is the validation? Now,
[50:43] this does relate to my um my PI AI talk
[50:48] uh that I did last week and I just wrote
[50:50] a blog post about it yesterday. So I
[50:53] asked I was investigating do stricter
[50:56] MCP schemas increase agent reliability.
[51:00] Uh so basically I I set up a um MCP
[51:06] server with a bunch of different tool
[51:07] schemas, right? And then I created an
[51:10] agent and I pointed out the MCP server.
[51:13] Uh this one's in pedantic AI, but I did
[51:15] also use agent framework and I use the
[51:18] copilot SDK and I use lang chain. So
[51:20] really you can do you know any agent,
[51:21] right? So you can all point all agents
[51:24] at MCV servers and then um and then I
[51:27] set up a bunch of prompts and for each
[51:30] of them I said this is what I expect
[51:32] right so this is the validation so if
[51:34] you're going to have any sort of
[51:35] optimization loop you need to know what
[51:37] the expected value is that you're you're
[51:39] you know you want a reward that that
[51:41] should be the correct thing. Now for
[51:43] this it was easy because I'm just saying
[51:44] like okay well I know what category I
[51:46] want I know what the date is. I know
[51:47] what the expected amount is right. So um
[51:50] you know for an MCP server like you know
[51:52] this is something I can actually set up
[51:54] and then what I did is I ran evaluations
[51:56] right. So for each evaluation like okay
[51:58] did we call the tool and if so did we
[52:00] match the expected category right so you
[52:03] know I was able to look and see which
[52:04] schema was correct
[52:07] um and evaluated cross models and all
[52:09] that stuff. So what you could do is um
[52:13] you know set up something like auto
[52:14] research and have it keep iterating on
[52:18] the schemas and the prompts right and I
[52:20] think this is actually a fairly um I
[52:22] think this exists in other things like I
[52:24] think this is um lightning I think
[52:28] lightning might be similar
[52:31] um the lightning let's see we might have
[52:33] a lot of things called lightning so
[52:34] let's see oh optimize any agent with any
[52:36] framework okay so maybe this isn't so
[52:38] this But you did also say agents create
[52:40] with agent framework. So I haven't tried
[52:44] it out yet, but um
[52:48] I think it might be similar. Um I think
[52:53] MCP yeah MCP servers are are easy
[52:55] because you're just optimizing for
[52:57] making sure that the tool calls come out
[52:59] correctly. And you would just want to
[53:01] make sure that the you know your harness
[53:04] knows you know what kind of options it
[53:06] has for uh improving the MCP schema for
[53:10] what it can change in the prompts right
[53:12] like it can it so with an MCP tool
[53:15] you've got the the tool name the tool
[53:17] description and then the tool parameter
[53:19] and the tool return values so those are
[53:21] all the things that it can change and
[53:23] you can imagine an LM iterating on that
[53:25] and running evaluations um you know like
[53:28] these ones until it got the best
[53:30] results.
[53:31] Uh so, so yes, I do think you set up
[53:34] something like that. Um I think for a
[53:37] lot of people it, you know, it feels
[53:39] like, you know, it's too much work
[53:41] because I always tell people like, "Hey,
[53:43] why don't you run evaluations?" And
[53:46] people almost never run evaluations. Um
[53:48] even when I encourage it, but you learn
[53:50] so much when you set it up. And uh and
[53:53] really like GitHub Copilot can like set
[53:55] up your evals for you. like the eval
[53:57] here. Uh I didn't even have to write the
[53:59] evals. I just said, "Hey, I want an
[54:00] evaluation framework." And it just made
[54:01] an evaluation framework.
[54:04] Um but here we have there is
[54:07] let's see where is the packages
[54:12] under lab
[54:15] lightning. So this is the agent
[54:17] framework integration of lightning. I
[54:19] haven't tried it yet but you try that
[54:22] out. And then there was also Gaia.
[54:26] Oh, Gaia is just evaluation. Okay, that
[54:29] one doesn't have enough details. Um,
[54:33] yeah. Yeah, try it. If you've got the
[54:35] time, try it out. Oh, also on that note,
[54:37] I was going to show Let's see. Shane
[54:39] Boyer.
[54:41] Okay, so this is a skill for iteratively
[54:44] approving improving a skill. I haven't
[54:46] tried it yet, but I just wanted to point
[54:48] that out. And then he also has
[54:51] Waza
[54:53] Where's Waza? Waza. Here we go. Waza. He
[54:57] has been having a lot of fun with
[54:59] skills. He's going so hard on it. Um, so
[55:01] it should be just Waza. Let's find Waza.
[55:06] Oh, where did he move it to? Maybe it's
[55:08] under Microsoft.
[55:12] Yes. All right. Here is Waza.
[55:16] And Waza is um a goi for evaluating
[55:22] skills. So this is for evaluation.
[55:25] So that seems really fun too.
[55:28] So there we go. Okay. All right. And it
[55:32] looks like Oh, good. We're still
[55:33] recording. All right. So we managed to
[55:35] capture everything today. Lots of great
[55:38] questions. Uh let me also just link but
[55:40] link dump for the upcoming events just
[55:43] so you have these links here.
[55:46] Um, it doesn't actually.
[55:49] Come on. Let's have it actually
[55:51] PowerPoint does this weird thing when
[55:52] you copy and paste it becomes an image.
[55:54] All right, let me try this.
[55:56] Here we go. All right, so there's some
[55:59] upcoming events. Um, oh wow, it embedded
[56:03] everything. Well, there you go.
[56:07] Oh, you're working on duck go. Nice.
[56:10] Maybe share that next week.
[56:13] Cool.
[56:16] All right. Oh, wait. That wasn't even
[56:18] the one I wanted to Oh, that wasn't even
[56:21] the links I wanted to share. All right.
[56:25] Let me just do one
[56:27] one more attempt at this link dump.
[56:31] Okay, here we go.
[56:34] And here we go. All right. So, yeah,
[56:37] there's a bunch of online events coming
[56:39] up. Um, so you may want to tune into
[56:40] them. Like Found Your IQ series. Uh the
[56:43] first one is tomorrow actually. Um
[56:47] and then there's various inerson events.
[56:50] Um but then there's cosmos to be online
[56:52] and pose online.
[56:55] All right. Um yeah, it I it's hard for
[56:58] me to do other people presenting because
[57:00] of how I do the StreamYard um
[57:04] because my computer setup. Um but we
[57:07] could try.
[57:11] Uh, but if you have like a public URL,
[57:12] maybe a gist or a GitHub repo, then we
[57:14] can share that. That'd be cool.
[57:19] All right. Oh, and next week, oh, next
[57:22] week I will be in Redmond for the MVP
[57:24] summit, but I'm still I've been told I
[57:27] can hold the there's like computers and
[57:30] monitors that I can use at the Microsoft
[57:32] office. Uh so uh so hopefully I can pull
[57:36] off office hours next week, but it will
[57:38] be a little different because um you
[57:40] know I'll be in the Microsoft Redmond
[57:42] office.
[57:44] Sweet.
[57:46] All right, thank you everyone. See you
[57:48] next time.
[57:50] And I will publish all of this like
[57:52] tonight. Uh we'll have the recording up,
[57:54] the write up, all that stuff so you can
[57:56] reference everything we covered. Bye.
