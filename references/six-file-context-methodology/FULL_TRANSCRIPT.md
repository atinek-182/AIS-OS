# Full Video Transcript: How Senior Engineers Actually Build With AI in 2026

**Video Title**: How Senior Engineers Actually Build With AI in 2026 | Build a Full Stack Systems Architecture App
**Uploader**: JavaScript Mastery (Adrian Hajdin)
**Duration**: 3 hours 58 minutes 17 seconds (14,297 seconds)

---



## Chapter 01: Introduction (00:00:00)

[00:00:00] It's 2026 and most of the senior
[00:00:02] engineers I know aren't really writing
[00:00:05] code anymore. They design the systems
[00:00:07] and let AI handle the implementation.
[00:00:09] And the gap between developers who can
[00:00:11] do that and developers who can't is
[00:00:14] dividing the industry right now. This
[00:00:16] app is what that looks like when you do
[00:00:18] it well. Real-time multiplayer SaaS, AI
[00:00:21] agents running in the background, full
[00:00:23] production code, and I didn't write a
[00:00:26] single line of it. An agent built the
[00:00:28] whole thing. And by the end of this
[00:00:30] video, you'll have built it, too. The
[00:00:32] same app, the same stack, the same way I
[00:00:36] did. And here's what makes this
[00:00:37] different from other AI build tutorials.
[00:00:40] I built this app using the exact
[00:00:42] methodology the app itself is designed
[00:00:45] to teach. Specs first, architecture
[00:00:48] defined, every feature planned before we
[00:00:51] start building. I've been doing this
[00:00:52] architecture work by hand before every
[00:00:55] serious project for years. And at some
[00:00:58] point, it hit me. I'm a developer. Why
[00:01:01] am I doing all of this manually when I
[00:01:03] could build the tool that does it with
[00:01:05] me? So, I did. This is Ghost AI, a
[00:01:09] real-time collaborative workspace where
[00:01:11] you describe a system in plain English
[00:01:14] and then AI agent maps it onto a shared
[00:01:17] canvas live. Your team edits the design
[00:01:20] together and when it's ready, the app
[00:01:23] generates a complete technical
[00:01:24] specification you can build from.
[00:01:27] Now, if you've tried building anything
[00:01:29] serious like this with AI, you already
[00:01:31] know the wall.
[00:01:33] The first few hours feel incredible and
[00:01:35] then a week later, the agent has
[00:01:37] forgotten every decision you've made,
[00:01:39] one new feature breaks three others, and
[00:01:42] the code base you were excited about
[00:01:44] just starts fighting you.
[00:01:45] That's not an AI problem. It's an
[00:01:48] architecture problem. And it's the same
[00:01:50] wall all of you are hitting in your
[00:01:52] careers where the senior dev advice
[00:01:54] online sounds great as long as you're
[00:01:57] already senior. The developers who win
[00:02:00] in this market aren't avoiding AI, and
[00:02:03] they're not handing everything over to
[00:02:05] it, either.
[00:02:06] They're learning to think like senior
[00:02:08] engineers, and then using AI to build at
[00:02:11] the speed of one. And that's what this
[00:02:13] video teaches. By the end, you'll know
[00:02:16] how to design a system before writing
[00:02:19] any code, how to use the six-file
[00:02:21] context system I write before every
[00:02:24] project, and how a senior engineer
[00:02:27] actually thinks when working with AI.
[00:02:29] Oh, and that six-file context system I
[00:02:31] just mentioned, I've packaged it into a
[00:02:34] free guide you can grab and use on any
[00:02:36] of your upcoming projects, not just this
[00:02:38] one. The link is down in the
[00:02:39] description. Next, the stack is Next.js,
[00:02:43] React 19, Liveblocks for real-time
[00:02:46] collaboration with agents, Trigger.dev
[00:02:49] for background work with AI agents,
[00:02:51] Clerk for auth and user management,
[00:02:54] Prisma and Postgres for data, Vercel
[00:02:57] Blob for storage, all production grade
[00:03:00] and deployed by the end of the video.
[00:03:03] So, one person with the right system can
[00:03:06] now build what used to take a team. And
[00:03:09] by the end of the next few hours, that
[00:03:11] person is you.
[00:03:12] So,
[00:03:13] let's build it.


## Chapter 02: Crash Course (00:03:15)

[00:03:17] Before we open up a single tool, I want
[00:03:19] to spend the next 10 minutes on the part
[00:03:22] of the video that I think is most
[00:03:24] important, and that decides whether what
[00:03:27] you're building ships or falls apart in
[00:03:30] the third week. There's going to be no
[00:03:32] syntax and no code in this section.
[00:03:35] Rather, what I'm teaching you is the way
[00:03:37] that I think before I write a single
[00:03:40] prompt, and the way I plan a build
[00:03:43] before I touch the agent, and the system
[00:03:46] that I use to keep AI from drifting
[00:03:48] halfway through a project.
[00:03:50] So that by the end, you'll know the
[00:03:52] conversations to have before you build
[00:03:55] the six-file context system that turns
[00:03:57] an AI agent from a guesser into a
[00:04:00] developer who already knows your
[00:04:02] codebase,
[00:04:03] and how to break any project into units
[00:04:06] the agent can ship cleanly one at a
[00:04:08] time. So, if you've been frustrated by
[00:04:11] AI breaking your code,
[00:04:13] then this is the video that fixes it.
[00:04:14] The intro touched on something I want to
[00:04:17] sit with for a minute.
[00:04:19] You heard me say senior engineers a lot.
[00:04:22] And if you're early in your career, that
[00:04:24] framing probably hit a nerve. So, let me
[00:04:27] be direct about what I mean.
[00:04:29] The job market for developers right now
[00:04:32] is harder than it was 2 years ago.
[00:04:35] Some entry-level work has been
[00:04:37] automated. Clients who used to hire
[00:04:39] freelancers for straightforward projects
[00:04:42] are now doing it themselves. And a lot
[00:04:44] of people who learn to prompt without
[00:04:47] learning how to think are now flooding
[00:04:49] the market. So, if you're worried about
[00:04:51] that, you're not wrong to be worried.
[00:04:54] But the developers getting squeezed
[00:04:56] aren't the ones who learned deeply.
[00:04:59] They're the ones who learned just enough
[00:05:01] to execute without understanding the
[00:05:03] system behind it. That was always a
[00:05:06] fragile place to be.
[00:05:08] And AI just made that fragility visible
[00:05:11] faster.
[00:05:12] So, the way through is to learn the kind
[00:05:15] of thinking that AI cannot replace. The
[00:05:18] architectural thinking, the
[00:05:20] systems-level judgment, and then use AI
[00:05:23] to build at the speed of someone twice
[00:05:25] your experience. The clearer your
[00:05:28] understanding of what you're building,
[00:05:30] the better the AI output. Which means
[00:05:32] that learning properly isn't a waste of
[00:05:35] time in the AI era. It's the best
[00:05:37] investment that makes everything else
[00:05:39] possible.
[00:05:41] So, when I say things like think like a
[00:05:44] senior engineer in this video, I don't
[00:05:46] mean you need 10 years of experience to
[00:05:48] apply this.
[00:05:50] These are learnable habits and you can
[00:05:52] start building them today on this
[00:05:54] project. And here's something most
[00:05:56] developers outside of Big Tech don't
[00:05:58] really know. At Google, Amazon, and
[00:06:01] Netflix, before any serious project
[00:06:04] starts, engineers spend weeks writing
[00:06:07] documents and sometimes months.
[00:06:10] Design docs, one-pagers, RFCs, the
[00:06:14] format changes by company, but the
[00:06:16] principle is the same.
[00:06:18] Figure out what you're building before
[00:06:21] you build it.
[00:06:22] And senior engineers at these companies
[00:06:24] sometimes go months without writing
[00:06:26] production code. They're designing
[00:06:28] systems, making architectural decisions,
[00:06:31] reviewing what other engineers ship. So,
[00:06:34] software engineering has never really
[00:06:36] been about typing the most lines per
[00:06:38] day.
[00:06:39] It's always been about thinking clearly
[00:06:41] about what should exist before you build
[00:06:44] it.
[00:06:45] And AI didn't invent that discipline. It
[00:06:48] just made it the most important skill in
[00:06:49] the room. And that's the whole
[00:06:51] foundation for the spec-driven agentic
[00:06:54] development course that I've been
[00:06:55] developing for a long time now. So, if
[00:06:58] you want to stay up-to-date on how
[00:07:00] that's going and receive an occasional
[00:07:01] email where I share my thoughts at the
[00:07:03] current state of the industry, I'll
[00:07:05] leave the link down below so you can
[00:07:06] subscribe for the newsletter. But, let
[00:07:08] me immediately make it concrete in this
[00:07:10] video.
[00:07:11] Here are two different prompts that two
[00:07:14] different developers might write to
[00:07:16] build the same feature.
[00:07:18] The first one says, "Build me a SaaS app
[00:07:21] with authentication and a real-time
[00:07:23] canvas."
[00:07:24] And the second one says,
[00:07:25] "I'm adding a LiveBlocks room provider
[00:07:28] to the workspace route.
[00:07:29] Auth is already handled by Clerk
[00:07:31] middleware. The canvas uses React Flow.
[00:07:35] Room tokens should be issued only after
[00:07:38] verifying project membership. Wire the
[00:07:41] provider into the existing workspace
[00:07:43] layout without touching the sidebar or
[00:07:45] navbar. Both developers want roughly the
[00:07:49] same thing.
[00:07:50] But the second prompt reveals a
[00:07:52] developer who knows their auth layer,
[00:07:54] understands their component boundaries,
[00:07:57] and knows what should and shouldn't be
[00:07:58] touched. They've thought about the
[00:08:00] system, so they're communicating
[00:08:02] decisions and not wishes.
[00:08:04] So, the AI isn't smarter when it reads
[00:08:07] the second prompt. The developer is.
[00:08:10] And that is the difference between vibe
[00:08:12] coding and what I'm going to teach you,
[00:08:14] which is spec-driven development, which
[00:08:17] is also the premise behind that
[00:08:19] spec-driven agentic development course
[00:08:21] that I'm actively developing. Vibe
[00:08:23] coding focuses on the outcome.
[00:08:26] You describe what you want, let the
[00:08:28] agent run, and react to whatever comes
[00:08:31] out.
[00:08:32] For a weekend prototype, that's fine.
[00:08:35] But for anything you're going to
[00:08:36] maintain, it just collapses.
[00:08:39] New features break the old ones, the
[00:08:42] code base starts contradicting itself,
[00:08:44] and you spend more time untangling AI
[00:08:46] mistakes than actually building.
[00:08:49] Spec-driven keeps the thinking with you
[00:08:52] and gives the agent a system to execute
[00:08:55] against.
[00:08:56] You stay the architect and the agent
[00:08:59] becomes the implementation engine. So,
[00:09:01] how do you actually build that system?
[00:09:03] Because that's the part that nobody
[00:09:05] really teaches. It starts before you
[00:09:07] open up any AI coding tool, with a
[00:09:10] conversation. When I get an idea for
[00:09:12] something I want to build, I open up a
[00:09:15] planning AI, ChatGPT, Claude, or Gemini,
[00:09:18] whichever's on hand, and I talk through
[00:09:20] it. What does this thing actually do?
[00:09:22] Who uses it? What are the core flows?
[00:09:25] Where are the complex patterns, and what
[00:09:26] could go wrong?
[00:09:28] I push back on the answers and let AI
[00:09:31] pressure test my thinking until the
[00:09:33] system becomes clear in my head. This
[00:09:36] conversation is the work. It's what
[00:09:38] senior engineers do before they build,
[00:09:41] except they usually do it in their head
[00:09:43] or on a whiteboard. But, doing it with
[00:09:45] AI externalizes it and makes it faster.
[00:09:49] When the system is clear, you write it
[00:09:51] down. And that's where the six-file
[00:09:53] context system comes from.
[00:09:54] Not from sitting at a blank page trying
[00:09:56] to write documentation, but from taking
[00:09:59] the output of the architectural
[00:10:01] conversation and organizing it into
[00:10:03] documents that travel with the project
[00:10:06] for its entire life. For Ghost AI, I
[00:10:09] organized everything into one folder
[00:10:11] called context.
[00:10:13] Six files, and what matters is that
[00:10:15] before your AI agent writes anything, it
[00:10:18] already knows what you're building, how
[00:10:20] it fits together, what the rules are,
[00:10:22] and where things stand right now. That's
[00:10:24] what you're going to learn about in this
[00:10:26] video. But, very quickly, here's what
[00:10:28] each one of them does at a glance.
[00:10:31] The project overview covers what the
[00:10:34] product is, who is it for, the core
[00:10:36] flows, and what's deliberately out of
[00:10:39] scope.
[00:10:40] The architecture file defines the tech
[00:10:42] stack, the boundaries between layers,
[00:10:45] and the invariants the codebase must
[00:10:47] never break. The code standards keeps
[00:10:50] the agent consistent across every unit
[00:10:52] of the build with shared TypeScript and
[00:10:55] Next.js conventions. The AI workflow
[00:10:58] rules keep the agent disciplined,
[00:11:00] defining how to scope work and what to
[00:11:02] do when something needs a decision.
[00:11:05] The UI context holds design tokens and
[00:11:08] component conventions, so the UI stays
[00:11:11] coherent across every page the agent
[00:11:13] ships.
[00:11:14] And the progress tracker, which is the
[00:11:16] one most developers skip and most need,
[00:11:19] holds the current phase, what's in
[00:11:21] progress, what's complete, and the
[00:11:23] architectural decisions made along the
[00:11:25] way. It's the only file that actually
[00:11:27] updates constantly throughout the build.
[00:11:30] And it's how the agent picks up exactly
[00:11:32] where you left off in a single prompt.
[00:11:34] These six files are what make the
[00:11:37] difference an AI agent that drifts and
[00:11:40] one that executes. And you don't have to
[00:11:42] build them from scratch for every
[00:11:44] project. I've put together a free blank
[00:11:47] template of all six files with
[00:11:49] step-by-step instructions on how I
[00:11:51] generate them using AI for whichever
[00:11:54] project I'm working on. And it's not
[00:11:56] specific to Ghost AI. It works for any
[00:11:58] application. Click the link down in the
[00:12:00] description to get it so you can apply
[00:12:02] this methodology to your own project
[00:12:04] starting today.
[00:12:06] We'll open up each one of these and I'll
[00:12:08] walk you through what's actually inside
[00:12:10] in the next lesson when we set up the
[00:12:12] project architecture for real. But yeah,
[00:12:14] once these six files exist, the build
[00:12:17] runs in units. We're going to break down
[00:12:19] the project into specific scoped pieces
[00:12:22] before we start. Not vague phases like
[00:12:25] build a dashboard, but concrete units
[00:12:28] small enough to build in a single focus
[00:12:31] session with clear conditions for what
[00:12:33] done looks like. That means that
[00:12:35] together for Ghost AI, we'll map out the
[00:12:38] entire build. Each lesson will have its
[00:12:41] own spec file. The spec defines the
[00:12:44] goal, the design decisions, the
[00:12:46] implementation details, dependencies,
[00:12:48] and a checklist of what has to be true
[00:12:51] before the unit is complete.
[00:12:53] You write the spec in the same way you
[00:12:55] write the context file through a
[00:12:57] conversation with the planning AI.
[00:12:59] Then you give the spec to your coding
[00:13:01] agent in one prompt. Make sure to read
[00:13:04] that spec. Mark that unit as in progress
[00:13:07] in the progress tracker. Implement it
[00:13:09] exactly as specified without going
[00:13:12] beyond scope. The agent will read your
[00:13:14] spec, read your context file, and build
[00:13:17] against a defined system instead of
[00:13:20] guessing.
[00:13:21] You review it against the checklist and
[00:13:24] if it passes, you close the unit, push
[00:13:26] the code, and move to the next spec. If
[00:13:29] something's off, you write a focused
[00:13:32] corrective prompt, exactly what's wrong,
[00:13:35] exactly what you expect, fix that
[00:13:36] specific thing, and move on.
[00:13:39] That's the entire workflow, the same one
[00:13:41] I used to build Ghost AI, and the same
[00:13:44] one you're about to use to build it with
[00:13:47] me. Oh, and last thing before we begin.
[00:13:49] These files take time to write. The
[00:13:52] conversation, the architectural
[00:13:54] decisions, the unit planning, all of it
[00:13:57] is real upfront work. And a lot of
[00:13:59] developers skip it because they want to
[00:14:01] feel productive immediately. I mean,
[00:14:04] I've done that as well. So, you open up
[00:14:06] the agent, type a prompt, and start
[00:14:09] watching code appear.
[00:14:10] But, that's the trap. The time you save
[00:14:14] by skipping this is the time you lose in
[00:14:17] week three debugging AI output that's
[00:14:20] drifted away from anything coherent. So,
[00:14:23] do this work once, and you'll do it
[00:14:25] faster every project after. And finally,
[00:14:28] it's time to build.


## Chapter 03: Project Setup (00:14:31)

[00:14:32] Okay, enough talk, and let's build.
[00:14:36] Open up your desktop and create a new
[00:14:38] folder. Call it something like Ghost AI,
[00:14:42] and then simply drag and drop it into
[00:14:44] your favorite code editor. For this
[00:14:46] video, I'll be using VS Code as we have
[00:14:49] the file explorer on the left side, we
[00:14:51] have the code in the middle, and then we
[00:14:53] have the chat window which you can open
[00:14:55] up by pressing command shift P, and then
[00:14:58] just search for chat. Or, I think it's
[00:15:00] just command shift I to open it as well.
[00:15:03] No matter which agent you're using, is
[00:15:05] it Copilot, Claude, Codex, or whatever,
[00:15:07] the interface is more or less the same.
[00:15:10] This is how it looks like on Codex, and
[00:15:12] this is just general chat.
[00:15:15] So, this video is completely agentic
[00:15:17] tool agnostic. The thinking and the
[00:15:20] specs are what matters. The tool is
[00:15:23] completely your call. I'll personally be
[00:15:25] using Claude code as that's what most
[00:15:27] people are using and what's we're using
[00:15:29] internally within JSM. If you want the
[00:15:31] budget option, you can go with Codex.
[00:15:34] There's the Go plan, which is super
[00:15:35] cheap, the plus plan, which is also
[00:15:37] cheap, and I think they're also offering
[00:15:39] a month for free. And if you're already
[00:15:41] paying for something like Cursor, Win
[00:15:43] serve, or any other AI agent, just use
[00:15:46] that. I'll make sure you don't spend a
[00:15:48] lot of tokens, no matter what you're
[00:15:49] using, and that you learn a ton. Okay,
[00:15:52] so let's get started.
[00:15:54] We'll start with a fresh Next.js
[00:15:56] project. I'll do this manually with no
[00:15:58] prompts and agents.
[00:16:00] It's just a single command and it takes
[00:16:02] a couple of seconds and that'll give us
[00:16:04] a clean and predictable foundation to
[00:16:06] build everything else in top of. So,
[00:16:08] simply open up your integrated terminal
[00:16:11] and run MPX create next app at latest
[00:16:15] dot, which is going to create it in the
[00:16:16] current repository. It'll ask you
[00:16:18] whether you want to install the Next.js
[00:16:20] installer, so you can just say Y, yes,
[00:16:22] and proceed.
[00:16:23] And I also want you to know that you
[00:16:25] don't necessarily have to follow along
[00:16:27] by using Next.js.
[00:16:29] Of course, the majority of the context
[00:16:31] for AI agents we'll be working with is
[00:16:33] going to be featured around Next.js, but
[00:16:36] if you want to build this in TanStack,
[00:16:38] Angular, Vue, or anything else, the
[00:16:40] concepts will still be as valuable.
[00:16:43] So, let's just say Y for now. It's going
[00:16:45] to ask you whether you would like to use
[00:16:46] the defaults, so just press enter,
[00:16:49] which is going to install React,
[00:16:51] TypeScript, ESLint, Tailwind CSS, and
[00:16:54] the app router. Let's give it a moment
[00:16:56] until it finishes. Once the installation
[00:16:58] finishes, we need to clear out the
[00:17:00] default boilerplate.
[00:17:01] That's going to be within app and then
[00:17:04] page. Next.js ships with a lot of
[00:17:06] placeholder content that, honestly, we
[00:17:08] don't really need. Now, you could go
[00:17:11] ahead and clean it up manually by
[00:17:13] opening up your globals.css
[00:17:15] and cleaning everything besides the
[00:17:17] Tailwind CSS directives, deleting some
[00:17:20] SVGs and other stuff within the public
[00:17:22] folder, and replacing the page.tsx with
[00:17:25] a minimal component.
[00:17:27] Or we can use this as our first
[00:17:29] interaction with the coding agent.
[00:17:33] So, go ahead and open up your agent of
[00:17:35] choice. I'll just press command shift I
[00:17:38] to open up my chat sessions. And what I
[00:17:40] love about VS Code is that it's not
[00:17:43] shying away from the agnostic approach
[00:17:45] to agents.
[00:17:46] You can use their agents right here,
[00:17:48] such as Copilot CLI,
[00:17:51] or if you head over to extensions and
[00:17:54] then install an extension like Claude
[00:17:56] Code,
[00:17:58] which has like 12 million downloads, or
[00:18:01] something like CodeX, which has 8
[00:18:03] million downloads,
[00:18:05] and I installed both, you can actually
[00:18:07] just navigate over to them by selecting
[00:18:10] additional views,
[00:18:11] and then choosing the extension you
[00:18:13] want. Of course, alternatively, you can
[00:18:15] also just run all of these agents within
[00:18:17] the CLI by typing Claude, and you're in.
[00:18:21] For the longest time, I've been using
[00:18:23] Claude CLI, but the Claude VS Code
[00:18:26] extension recently got so much better,
[00:18:28] and honestly, it's working the same way
[00:18:30] as the CLI does, but with a bit of a
[00:18:32] nicer UI and a graphical interface that
[00:18:35] allows us to use it in an easier way.
[00:18:37] So, that's what I'll be proceeding with.
[00:18:39] I'll expand it so we have more space to
[00:18:41] work with, and you can notice that
[00:18:43] there's a little microphone button right
[00:18:44] here. So, you can either tap it or hold
[00:18:47] the command D key to speak into it. With
[00:18:50] CodeX and other agents, you can either
[00:18:52] type it manually,
[00:18:53] or what you can do is use a tool like
[00:18:57] Whisper Flow, not sponsored by the way,
[00:18:59] which is what I use to write prompts
[00:19:02] when I speak with agents. Speaking is
[00:19:04] just much faster. If you install it, you
[00:19:06] can just press the command key
[00:19:09] and start speaking into it. Like, clean
[00:19:12] up this Next.js boilerplate. Strip
[00:19:15] globals.css down to just the Tailwind
[00:19:17] directives. Delete all SVGs in the
[00:19:20] public folder, but keep the favicon.
[00:19:23] Remove page.module.css.
[00:19:26] Replace page.tsx with a minimal
[00:19:28] component that just renders a centered
[00:19:31] div saying Ghost AI.
[00:19:34] And I can stop it right here, and you
[00:19:36] can immediately see the output. Cool
[00:19:38] stuff, right? Go ahead and write
[00:19:40] something like this, and let's see how
[00:19:42] well Agent handles it.
[00:19:43] Also, just so we don't have to give it
[00:19:46] permissions every single time whenever
[00:19:47] we're doing something, for now I will
[00:19:49] say edit manually. Oh, and of course, we
[00:19:52] have to talk about the actual models
[00:19:54] we'll be using. In this case, we're
[00:19:56] using the default model, which is Opus 4
[00:19:58] 7 with a million token context, which is
[00:20:00] amazing, but you're going to hit the
[00:20:02] limits very soon. Instead, you'll be
[00:20:04] able to follow along this entire build
[00:20:06] with using Sonnet 4 6. It's fast, it's
[00:20:10] inexpensive, and it sometimes get lost
[00:20:13] unless you have the context files, which
[00:20:16] I'll teach you how to build so you guide
[00:20:17] it in a bit of a better way, and make it
[00:20:20] work much more like Opus does. So,
[00:20:23] that's what I'm going to select. If
[00:20:24] you're working with Codex, you can also
[00:20:26] go ahead and choose any model you'd
[00:20:27] like, like 5 4, 5 3, or anything else.
[00:20:31] Okay, let's give it a shot. It's going
[00:20:33] to think for a couple of seconds, read
[00:20:35] all the necessary files, and apply all
[00:20:38] four changes.
[00:20:39] Globals, just the import. Page, minimal
[00:20:42] centered Ghost AI component. Deleted
[00:20:44] five SVGs, but kept the favicon. And
[00:20:47] this file that I tried to trick it with
[00:20:48] doesn't really exist, so there's nothing
[00:20:50] to delete.
[00:20:51] You can see all the changes in the diff
[00:20:53] right here, and you can also see which
[00:20:55] files have been modified on the left
[00:20:56] side.
[00:20:58] There we go, just simple Ghost AI, and
[00:21:01] just the import for Tailwind. Which
[00:21:03] means that these classes right here
[00:21:04] should work to center the div. Before we
[00:21:06] run it, let's actually head over to
[00:21:08] package.json.
[00:21:10] Make sure that the project name is set
[00:21:12] to Ghost AI, and let's run it by running
[00:21:15] npm run dev.
[00:21:18] It'll run it on localhost:3000. So, if
[00:21:21] you open it up, you should be able to
[00:21:23] see something that looks like this.
[00:21:25] This means that our project is
[00:21:26] initialized, it's cleaned up, and now we
[00:21:29] are ready to move to the part that
[00:21:31] actually determines just how well
[00:21:33] everything goes. Setting up our context
[00:21:36] files and planning the build before the
[00:21:38] agent writes a single feature. So, let's
[00:21:42] do that next.


## Chapter 04: Preparing Context (00:21:43)

[00:21:45] Not that long ago, I talked about how
[00:21:47] senior engineers spend weeks designing
[00:21:50] systems before anyone writes a line of
[00:21:53] code.
[00:21:54] They write design docs, they define
[00:21:56] boundaries, and they make decisions
[00:21:59] early on so that everything else becomes
[00:22:01] predictable.
[00:22:02] So, let me show you how we are going to
[00:22:04] approach that.
[00:22:06] We're going to create a new folder right
[00:22:08] here in the root of our application,
[00:22:10] which we're going to call context.
[00:22:12] Everything inside of it is what your
[00:22:15] coding agent will read before it does
[00:22:17] anything. This is how it knows your
[00:22:19] project, and this is how it stays
[00:22:21] consistent across every session, commit,
[00:22:24] or unit of the build.
[00:22:26] So, you can switch multiple agents and
[00:22:28] share the context file with another
[00:22:30] developer so he can continue working
[00:22:32] with his agent from there. That's the
[00:22:34] catch. We're going to have a couple of
[00:22:36] different files within the context
[00:22:37] folder. Now, I don't want you to do a
[00:22:40] lot of copy-pasting, so I'll provide you
[00:22:42] with the final zipped context folder so
[00:22:44] we can easily review everything
[00:22:46] together. So, delete the context folder
[00:22:48] you just created. In the video kit link
[00:22:51] down in the description, get the zipped
[00:22:53] version of the folder, unzip it, and
[00:22:55] then just drag and drop it in.
[00:22:57] And here, you'll see six, well, seven
[00:23:00] different files with this agents.md.
[00:23:02] Might seem scary at first, but don't
[00:23:05] worry as I walk you through every single
[00:23:07] one of these files and show you how you
[00:23:09] can create them for yourself in the
[00:23:10] future. Let's start with the project
[00:23:13] overview. And let me walk you through
[00:23:16] why it's structured the way it is
[00:23:18] because understanding this is more
[00:23:20] valuable than just copying the file.
[00:23:23] Currently, we're looking at the markdown
[00:23:25] version of the file, but in VS Code, I
[00:23:28] believe this is done by default, you can
[00:23:30] also open the preview to the side by
[00:23:32] pressing command K and then V or just
[00:23:34] pressing this icon at the top and then
[00:23:36] you can close the actual MD and just see
[00:23:38] the formatted version. I think it's a
[00:23:40] bit easier to read this way. I typically
[00:23:42] open up these project overview documents
[00:23:45] with a one paragraph summary and then a
[00:23:48] numbered list of goals. This gives the
[00:23:51] agent the big picture immediately. So,
[00:23:54] when a requirement gets ambiguous 3
[00:23:56] weeks into the build and it will, this
[00:23:59] is where you resolve it. The agent uses
[00:24:02] this constantly to understand intent
[00:24:05] when a spec isn't specific enough.
[00:24:08] Notice the goals are concrete and
[00:24:10] measurable, not build a good canvas.
[00:24:13] Instead, let authenticated users create
[00:24:16] and manage architecture projects or let
[00:24:19] AI generate an initial architecture from
[00:24:21] a natural language prompt. The agent
[00:24:24] knows exactly what success looks like.
[00:24:27] And yeah, this is useful for us while we
[00:24:29] are going through the process of
[00:24:30] building the app. Just so you know what
[00:24:32] we are building. Just so everybody in
[00:24:34] the team, in this case me teaching you
[00:24:36] and you following along and you building
[00:24:38] it with me, are all on the same page. Go
[00:24:42] stay eye is a real-time collaborative
[00:24:44] system design workspace. Users describe
[00:24:47] a system in plain English and then AI
[00:24:49] agent maps that system onto a shared
[00:24:51] canvas. Collaborators refine the
[00:24:54] architecture and the app generates a
[00:24:56] technical specification document from
[00:24:58] the resulting graph.
[00:25:00] Okay, great. We have the overview, we
[00:25:03] have the goals, and then we have the
[00:25:05] core user flow. So, let me zoom this in
[00:25:08] and let's go through this together
[00:25:10] because this sequence matters. The agent
[00:25:13] can sometimes lose track of how features
[00:25:16] connect to each other.
[00:25:17] By defining a full flow from sign in to
[00:25:21] the spec generation, we make the logical
[00:25:23] sequence explicit. So, the agent won't
[00:25:26] try to build the spec generation feature
[00:25:28] on the login page because it knows the
[00:25:30] user has to create a project and the
[00:25:32] design architecture first. In the
[00:25:34] features, we get specific about
[00:25:37] technologies. And I want to take a
[00:25:39] second on this because the tools I chose
[00:25:41] for Ghost AI weren't random. I took a
[00:25:44] lot of time to choose what actually
[00:25:46] makes sense. Starting with
[00:25:47] authentication. For user sign in, route
[00:25:50] protection, project creation, ownership,
[00:25:53] and collaborator access, we're using
[00:25:55] Clerk. Could you have gone and created
[00:25:57] the full auth from scratch? I mean,
[00:25:59] sure, but it would take you a couple of
[00:26:01] days up to a couple of weeks to do it
[00:26:03] properly, even with AI.
[00:26:06] And when you do it, it's never going to
[00:26:07] be as secure as something like Clerk.
[00:26:10] And nowadays, the speed of shipping
[00:26:12] matters more than anything. If you have
[00:26:15] a specific product you want to push, you
[00:26:17] want to get it in front of potential
[00:26:18] users as soon as possible. And that's
[00:26:20] why for many of these agentic builds,
[00:26:22] it's just a no-brainer to plug and play
[00:26:25] Clerk into it. Especially considering
[00:26:27] just how well Clerk works with your
[00:26:30] agents. You can either just copy the
[00:26:32] prompt or use Clerk skills with
[00:26:36] whichever agent you're using.
[00:26:38] That way, it'll immediately become a
[00:26:40] professional developer at using Clerk
[00:26:42] and it'll be able to implement it within
[00:26:45] any project. And there's also the MCP,
[00:26:48] which is a server that allows AI agents
[00:26:51] like Claude,
[00:26:52] or others
[00:26:54] to access Clerk as the case snippets and
[00:26:56] implementation patterns, and basically
[00:26:58] implement everything for you. Oh, and
[00:27:00] not to mention that Clerk CLI is also
[00:27:03] being worked on. You'll just be able to
[00:27:06] ask your agent to use the Clerk CLI to
[00:27:08] add auth to your app, allowing you to
[00:27:10] not even have to leave your terminal or
[00:27:12] copy and paste any API keys. Clerk right
[00:27:14] now really is the leader in agentic
[00:27:17] development. And with a completely free
[00:27:19] pricing of up to 50,000 monthly
[00:27:23] recurring users, it's a no-brainer for
[00:27:25] me to build all of my applications with
[00:27:27] it. So, while we're here, I'll leave the
[00:27:30] link down in the description. You can
[00:27:31] click it, and then sign up so that we
[00:27:33] can very soon more easily get started
[00:27:35] with building. Okay, on top of auth, the
[00:27:38] most important part of our application
[00:27:40] is the collaborative canvas.
[00:27:42] And in this case, I wanted to make it
[00:27:45] real-time. So, for any kind of canvas,
[00:27:47] it makes sense to use React Flow. And if
[00:27:50] you want to make any part of your
[00:27:51] application live with cursors, so you
[00:27:54] can see what other people are doing,
[00:27:55] presence indicators, and node or edge
[00:27:58] editing, I mean, it just makes sense to
[00:28:00] use Liveblocks. Liveblocks is the leader
[00:28:03] for anything multiplayer, but not only
[00:28:05] apps, agents as well. Let me show you
[00:28:08] what I mean.
[00:28:09] I mean, this is the app without
[00:28:11] Liveblocks, and then if you add it, you
[00:28:13] immediately get live avatars. You can
[00:28:16] get the AI chat to generate something,
[00:28:19] and you can also leave comments and
[00:28:21] track what people are doing within your
[00:28:22] app, which is super useful for the
[00:28:24] collaborative canvas we're building.
[00:28:26] But, what's even cooler is interacting
[00:28:29] directly with AI assistants to do
[00:28:32] something within our application. I
[00:28:33] mean, if you try to build all of this
[00:28:35] from scratch, it would definitely take
[00:28:37] some time. But, with their AI assistants
[00:28:39] feature, you can just watch an AI do it
[00:28:42] for you. Oh, and this whole React Flow
[00:28:44] thing you're seeing, that got released
[00:28:46] recently, which means that in this
[00:28:48] video, we're building the latest stuff
[00:28:49] out there. Oh, and like Clerk and the
[00:28:52] many other amazing dev tools that are
[00:28:54] adapting to agentic development,
[00:28:56] Liveblocks also offers the agent skills,
[00:28:59] which you just have to install, and your
[00:29:01] agent will immediately know what it has
[00:29:02] to do to make the Liveblocks integration
[00:29:05] work. I'll teach you about all of that
[00:29:07] as we continue with the build. After the
[00:29:09] canvas, we have the starter system
[00:29:11] design, which I decided to have because
[00:29:13] it's very difficult for people to start
[00:29:16] with a blank canvas. So, I want to have
[00:29:18] some kind of a curated library of
[00:29:20] pre-built system design templates, where
[00:29:23] users can import a starter template into
[00:29:25] the canvas at any point during editing.
[00:29:27] But also, if the template doesn't do
[00:29:29] what you want it to do, we're going to
[00:29:31] allow our users to generate a system
[00:29:33] design from a prompt with AI. Then, that
[00:29:37] output will be structured as canvas
[00:29:39] nodes, and then we'll write it onto the
[00:29:41] canvas. And finally, we'll take a look
[00:29:43] at everything that is on the canvas, and
[00:29:45] we'll convert it into a technical
[00:29:47] specification in a markdown format. And
[00:29:49] then users will be able to view and
[00:29:51] download the generated specs. Oh, and an
[00:29:54] additional thing that I want to teach
[00:29:55] you is while we're generating stuff with
[00:29:58] AI, that'll obviously take time. As the
[00:30:00] user will likely provide a long idea of
[00:30:03] how they want to architect their app,
[00:30:05] and then the AI output is going to take
[00:30:07] potentially a minute or two. And running
[00:30:10] a more than 60-second AI generation call
[00:30:13] inside a Next.js API route will just
[00:30:16] time out in production. So, that's why
[00:30:18] I'll also teach you how to use
[00:30:19] Trigger.dev. It'll allow us to run
[00:30:21] background tasks that can run as long as
[00:30:24] they need to, with the retry logic and
[00:30:26] status tracking built-in. The way in
[00:30:28] which we'll combine Liveblocks and
[00:30:30] Trigger.dev is pretty amazing. So, we'll
[00:30:33] have to be very clear in letting our AI
[00:30:35] agent understand that it doesn't have to
[00:30:37] invent a custom web socket
[00:30:39] implementation when Liveblocks is
[00:30:41] already in stack, Or it won't try to run
[00:30:44] AI generation inside a request handler
[00:30:47] when trigger dev is defined as the layer
[00:30:49] for that work. Naming the tools we're
[00:30:51] going to use for the project in advance
[00:30:53] is crucial. Oh, and trigger allows you
[00:30:55] to do so much more. Recently, they've
[00:30:57] been diving deeper into allowing you to
[00:30:59] build and deploy AI agents, which is
[00:31:01] something we can explore in an
[00:31:02] additional video. But in this one, we'll
[00:31:05] also focus on many of its features,
[00:31:07] specifically running background tasks
[00:31:09] and reporting back to the front end. So
[00:31:11] while a long task is happening, we can
[00:31:13] keep the user updated on what's
[00:31:15] happening behind the scenes and allow
[00:31:17] the user to continue doing whatever
[00:31:19] they're doing on the application because
[00:31:20] we're no longer blocking the front end
[00:31:22] side while handling a specific task. So
[00:31:24] I'll leave a special link pointing to
[00:31:26] trigger as well as live blocks down in
[00:31:29] the description so you can create your
[00:31:31] accounts and then we'll be able to
[00:31:32] immediately dive into the development.
[00:31:34] Then we have the scope part which
[00:31:36] contains the in scope and out of scope
[00:31:38] features. And it's maybe the most
[00:31:41] important section for keeping your build
[00:31:43] focused. The out of scope section is
[00:31:45] doing serious work right here.
[00:31:48] Billing and subscription systems,
[00:31:50] enterprise permissions, version
[00:31:51] specification history and so on. This is
[00:31:54] telling the agent, don't even think
[00:31:56] about them. But we can add them later on
[00:31:59] after we build the base of our
[00:32:00] application. This is great because it
[00:32:02] keeps every session focused on what we
[00:32:04] are actually building.
[00:32:06] And finally, there's success criteria.
[00:32:09] Here, we define what actually matters.
[00:32:12] These are the benchmarks that your agent
[00:32:14] and you can verify against after each
[00:32:17] major feature lands. Not, does it look
[00:32:19] right? But, can a signed in user create
[00:32:22] and open up a project? Can multiple
[00:32:24] users collaborate? Can the graph be
[00:32:26] converted into a persisted markdown
[00:32:28] specification?
[00:32:30] Very simple, yet concrete.
[00:32:33] So that's our project overview. Written
[00:32:35] in a way that makes sense to agents, but
[00:32:38] also other team members working on the
[00:32:40] project. Next, let's take a look at the
[00:32:42] AI workflow rules. This file is
[00:32:45] different from others in a way that it's
[00:32:48] not about what we're building. It's
[00:32:50] about how the agent behaves when
[00:32:52] building it. And the most important rule
[00:32:54] right here is to work on one feature
[00:32:57] unit or subsystem at a time. We don't
[00:33:00] want to combine unrelated system
[00:33:01] boundaries in a single implementation
[00:33:03] step. And that single rule prevents most
[00:33:06] failures that the agents cause.
[00:33:08] Basically, all of these rules right here
[00:33:10] tell the agent, "Stay in your lane.
[00:33:13] Focus on one part of what you're doing,
[00:33:15] and then move on to the next one." After
[00:33:17] that, we have the code standards. So,
[00:33:20] you can open up that, and let's quickly
[00:33:23] take a look. This file is what keeps the
[00:33:25] code base consistent from our first all
[00:33:28] the way to the last chapter. Without it,
[00:33:31] the agent would drift away. Like,
[00:33:33] specific patterns that it uses for API
[00:33:35] routes when implementing feature five
[00:33:37] might look different from feature 16. Or
[00:33:40] maybe it's going to change some things
[00:33:41] regarding the TypeScript types, or how
[00:33:43] it uses Next.js, how it styles things.
[00:33:46] But here, we add that consistency. Like,
[00:33:49] we tell it, "Make sure to have strict
[00:33:52] mode enabled, and avoid using any." Or
[00:33:54] we're telling it to add use client only
[00:33:57] when the component needs browser
[00:33:59] interactivity. Or for styling, we're
[00:34:01] telling it, "No raw Tailwind color
[00:34:03] classes. Reference the tokens through
[00:34:06] the Tailwind utility names." I think you
[00:34:08] get the point. We want to stay
[00:34:09] consistent. Then, we have the UI
[00:34:12] context, which, as you can guess, dives
[00:34:14] a bit deeper into theming. Like, when I
[00:34:17] was initially coming up with a design
[00:34:18] for this application, I wanted to have
[00:34:20] something that is simple, yet functional
[00:34:23] and modern. And I spoke with AI a bit to
[00:34:26] generate this theme. Dark mode, no light
[00:34:29] mode, Uh, all colors are already
[00:34:31] defined, and we're telling the AI to use
[00:34:34] these colors.
[00:34:35] And again, if you're wondering how
[00:34:37] exactly I created all six of these
[00:34:40] documents by speaking with different AI
[00:34:42] agents, that's something that I'll cover
[00:34:45] in much more detail within the
[00:34:47] spec-driven agentic development course.
[00:34:49] So, you can join the waitlist in the
[00:34:51] description. But, I think you get the
[00:34:52] idea that I didn't just sit down and
[00:34:54] handpick every color in the file. I
[00:34:56] described the aesthetic that I wanted to
[00:34:58] AI, dark, technical, precise, something
[00:35:01] that feels like an engineering tool, and
[00:35:04] then I went back and forth on the
[00:35:06] palette, um, the token names, and this
[00:35:08] is what it came up with. Also, some
[00:35:10] font, border radiuses, and so on. That's
[00:35:13] exactly how you should approach your own
[00:35:15] UI. You don't need to be a designer, but
[00:35:18] you need to know the feel you're going
[00:35:20] for, and then AI can help you get there.
[00:35:22] Oh, and while the project overview gave
[00:35:25] some information about the project, the
[00:35:28] architecture context will give you the
[00:35:30] blueprint on how to build it. Here, I
[00:35:32] specified the tech stack,
[00:35:35] like every technology that we want to
[00:35:36] use, alongside the role that it has
[00:35:38] within the application. For auth, we're
[00:35:40] using Clerk for user identity and route
[00:35:42] protection. For databases, it's going to
[00:35:44] be Prisma and Postgres. For canvas, it's
[00:35:47] going to be Liveblocks and React Flow
[00:35:50] for real-time collaborative canvas.
[00:35:52] For background tasks, it's going to be
[00:35:54] Trigger.dev, and for storage, we're
[00:35:55] going to use Vercel Blobs. We also
[00:35:57] defined some system boundaries, like
[00:35:59] where we're going to put the request
[00:36:01] handlers. Trigger is what we're going to
[00:36:03] use for the long-running background
[00:36:05] jobs, and some other folders that we're
[00:36:07] going to use.
[00:36:08] Then, we defined the storage model,
[00:36:10] where and how we're going to save
[00:36:12] something. And specifically here, I
[00:36:14] decided to use a hybrid storage model,
[00:36:16] which is another senior-level decision.
[00:36:18] We aren't going to be stuffing massive
[00:36:21] JSON blobs or three-page markdown files
[00:36:23] into our database. Instead, we're going
[00:36:25] to use Postgres only for metadata and
[00:36:28] Vercel blob for the actual files. And
[00:36:31] this keeps our database lean. And this
[00:36:33] is important. We also need to tell it
[00:36:35] how different tools are working
[00:36:37] together.
[00:36:38] Since we're using Clerk with Liveblocks,
[00:36:40] we need to set a strict rule that
[00:36:42] project memberships must be verified
[00:36:45] before a Liveblocks token is ever
[00:36:47] issued. This ensures that our Ghost AI
[00:36:50] isn't just collaborative, but secure.
[00:36:52] And finally, invariants are the rules
[00:36:55] that the system must never violate. For
[00:36:57] example, request handlers do not run
[00:37:00] long-lived AI works. That belongs in
[00:37:02] background tasks through trigger.dev.
[00:37:05] Metadata and large artifacts are stored
[00:37:07] in separate layers. Auth and ownership
[00:37:10] are enforced at every mutation boundary.
[00:37:12] Client components only used when needed.
[00:37:15] And the canvas schema must remain
[00:37:17] consistent. Of course, we'll dive much
[00:37:19] deeper into this when we actually dive
[00:37:21] into building the application. But I
[00:37:23] wanted you to have a good idea of what
[00:37:24] it is that we're building. And finally,
[00:37:26] there's the progress tracker. This is
[00:37:29] the only file in the context folder that
[00:37:31] will look completely different by the
[00:37:33] end of this video.
[00:37:35] Right now, it is completely empty.
[00:37:37] Intentionally, because it reflects the
[00:37:40] actual state of the project. And right
[00:37:42] now, nothing has been built yet. So, as
[00:37:45] we complete each lesson, we're going to
[00:37:47] update this file. The current phase,
[00:37:49] what's in progress, what's complete, and
[00:37:51] what's coming next. And remember what I
[00:37:53] said in the beginning about agents
[00:37:55] having no memory between sessions.
[00:37:57] This file is the solution to that
[00:37:59] problem.
[00:38:00] At the start of every new session,
[00:38:02] whether that's tomorrow, next week, or 6
[00:38:04] months from now, one prompt is all it
[00:38:06] takes to restore full context. Our agent
[00:38:10] will read the progress tracker,
[00:38:11] understand exactly where the project
[00:38:13] stands, and pick up exactly where you
[00:38:15] left off. So, you don't have to
[00:38:17] re-explain yourself. Even though it's
[00:38:19] going to be a small file, it does more
[00:38:21] work than any other file in the project.
[00:38:23] Oh, and finally, there's the agents.md
[00:38:26] file. Within it, we're going to wire
[00:38:29] everything together. When you installed
[00:38:30] Next.js,
[00:38:32] that file was already created for you
[00:38:34] automatically at the root. This is the
[00:38:36] entry point file, and every major coding
[00:38:38] agent has one. They just name it
[00:38:40] differently.
[00:38:41] Claude calls it claude.md, Cursor, Win
[00:38:44] Surf, and others use different names,
[00:38:46] but the idea is always the same. It's
[00:38:48] the first thing that the agent reads at
[00:38:50] the start of every session.
[00:38:52] So, Next.js has already added the first
[00:38:54] section for you, and it tells the agent
[00:38:56] that this is a recent version, and its
[00:38:58] training data might be outdated, so read
[00:39:00] the install documentation before writing
[00:39:02] any code. Good default, and we can leave
[00:39:04] it, but now we can add our own part
[00:39:06] below it.
[00:39:08] So, copy your agents.md, delete it from
[00:39:10] the context, and instead move it right
[00:39:13] here. It's not long, so let's see what
[00:39:16] do we have within it. We're basically
[00:39:17] instructing the agent to read all six
[00:39:20] context files in order before
[00:39:22] implementing anything, and then to
[00:39:25] update the progress tracker after each
[00:39:27] change. And you might think, "Isn't this
[00:39:29] going to waste context and tokens?"
[00:39:32] Well, I mean, sure, it has to read
[00:39:33] through the files, but that's not even
[00:39:35] 1/10 of how many tokens you're going to
[00:39:37] save because there's going to be less
[00:39:39] back and forth, and less mistakes and
[00:39:41] bug fixing and correcting while you're
[00:39:44] implementing the features in the first
[00:39:45] place. So, that's the system. And now
[00:39:48] that you understand it, let's start
[00:39:50] building with it.


## Chapter 05: UI Primitive Components (00:39:51)

[00:39:53] Now that the context files are ready,
[00:39:55] before we build a single feature,
[00:39:57] there's one more thing we need to set
[00:39:59] up, and skipping this one is the most
[00:40:01] common mistake I see in AI-assisted
[00:40:04] projects.
[00:40:05] And that is the globals.css
[00:40:08] file.
[00:40:09] This one right here. We've defined all
[00:40:11] of our color tokens within our UI
[00:40:13] context right here. But, if we don't
[00:40:16] translate those tokens into actual CSS
[00:40:18] custom properties within the globals.css
[00:40:21] file, well, it'll just write the inline
[00:40:23] colors. So, instead of maybe saying
[00:40:25] something like text faint, it'll just
[00:40:28] write #505060.
[00:40:31] And the moment you want to change it,
[00:40:32] you have to change it across all places.
[00:40:35] So, let's set it up correctly. And this
[00:40:36] is also the first real demonstration of
[00:40:39] the spec-driven workflow in action. So,
[00:40:42] let's do it properly. Create a new
[00:40:44] folder inside side of the context folder
[00:40:47] and call it feature specs, like this.
[00:40:51] And then inside of it, create the first
[00:40:53] spec file.
[00:40:55] 01
[00:40:56] design system.
[00:40:59] md. And then within it, we want to tell
[00:41:01] it something like read the agents file
[00:41:04] before starting.
[00:41:06] Then, we need to tell it what we're
[00:41:07] doing here, like adding the design
[00:41:09] system and the UI components.
[00:41:12] Then, we're telling it to install and
[00:41:15] configure shadcn-ui.
[00:41:17] And then we want it to add the following
[00:41:20] components.
[00:41:21] I figured we're going to use these
[00:41:23] across the rest of the application.
[00:41:24] Whenever we wanted to modify these files
[00:41:27] after the installation, so we can
[00:41:29] specify that.
[00:41:30] We can also ask it to install
[00:41:32] lucid-react for icons
[00:41:35] and create a lib-utils.ts
[00:41:38] with a reusable class names helper for
[00:41:40] merging tailwind class names. Although,
[00:41:42] I think it would do this by default,
[00:41:44] it's good to mention it.
[00:41:46] Finally, we want to ensure that all of
[00:41:49] the components match the existing dark
[00:41:51] theme within globals.css.
[00:41:54] And then, we want to apply some checks
[00:41:56] when it is done.
[00:41:58] For example, we want to make sure that
[00:42:00] all components import without errors,
[00:42:02] that the cn works properly, and that no
[00:42:05] default light styling appears. This is
[00:42:08] what we call a feature specification or
[00:42:10] a feature spec.
[00:42:12] Every unit we build from here on has
[00:42:14] one.
[00:42:15] The spec tells the agent exactly what to
[00:42:18] do, exactly what not to touch, and how
[00:42:21] to verify when it's done. No guessing.
[00:42:24] So, let's open up our agent by pressing
[00:42:26] command shift I. As I said, you can use
[00:42:29] anyone. I'll use Claude code.
[00:42:31] I'll start a new chat, and you can even
[00:42:34] open up that file, which will
[00:42:35] automatically put it within its context.
[00:42:37] And then, you can tell it something like
[00:42:39] read
[00:42:41] add 01 design system update
[00:42:45] the progress tracker MD file to mark
[00:42:49] this as in progress.
[00:42:51] And then, implement exactly as
[00:42:55] specified. This is the same template
[00:42:57] we'll use often, but the only thing
[00:42:58] that's going to change is going to be
[00:43:00] the spec of the feature we're
[00:43:01] developing. So, let's go ahead and run
[00:43:04] it, and notice what will happen before
[00:43:06] the agent writes a single line of code.
[00:43:08] It'll read the specification, and then
[00:43:11] update the progress tracker. You can see
[00:43:14] how it's going through all the files we
[00:43:16] prepared for it, and only once it has
[00:43:18] enough context, it'll write and save the
[00:43:20] plan, and then execute it. And only when
[00:43:23] it has a full plan, it will update the
[00:43:25] progress tracker.md, and then start
[00:43:27] doing it. So, we can already take a look
[00:43:30] at the progress tracker,
[00:43:32] and I'll open it up so we can see what
[00:43:34] it is doing. And you can see that the
[00:43:35] current phase is feature 01 system
[00:43:38] design, the current goal to install and
[00:43:40] configure shadcn with dark theme, and
[00:43:43] that is currently in progress with the
[00:43:45] feature 02 to be done. And it's also
[00:43:48] adding the architectural decisions
[00:43:50] needed for every step, as well as the
[00:43:52] session notes. It's going to ask us
[00:43:54] whether we want to run this command to
[00:43:55] install shadcn, so I'll say yes, go
[00:43:58] ahead. And after it installs everything,
[00:44:00] it'll verify it with TypeScript. It
[00:44:03] looks like it completed with zero
[00:44:04] errors, and finally, it needs to update
[00:44:06] the progress tracker to complete it.
[00:44:09] So, we can already open it up right here
[00:44:12] under progress tracker, and it should
[00:44:14] move it from current phase over to
[00:44:16] completed.
[00:44:18] So, now at any point in our application,
[00:44:20] if we come back 2 months later, it'll
[00:44:23] know that it's using shadcn, Tailwind V4
[00:44:26] with the following components, only
[00:44:27] using dark theme,
[00:44:29] and all the additional helpers,
[00:44:31] as well as the architectural decisions.
[00:44:33] So, once it finishes, the agent will
[00:44:35] have configured shadcn, installed the
[00:44:38] components, and verified that it all
[00:44:39] works. So, what do you say that we test
[00:44:41] it out?
[00:44:42] Back on localhost 3000, the first good
[00:44:45] sign should be that we're now officially
[00:44:47] in dark mode. And if you head over to
[00:44:49] the home page, that's going to be within
[00:44:51] app page, we can try to use a shadcn
[00:44:54] button component coming from components
[00:44:57] UI button, and we can try to make it say
[00:44:59] something like click me. You can see
[00:45:01] it's coming from there,
[00:45:03] and it follows our UI theme. That's it.
[00:45:06] Our first feature, being the theming and
[00:45:09] shadcn setup, is done. And that's the
[00:45:11] spectrum workflow I was telling you
[00:45:13] about. We define the specifications, we
[00:45:16] run the prompt, we verify the output,
[00:45:19] and then we move on. But just before we
[00:45:21] move on to our second feature, I want to
[00:45:24] add just one little extra step to this
[00:45:26] whole workflow that's going to make our
[00:45:28] codebase even more scalable,
[00:45:30] predictable, and less error-prone. And
[00:45:33] that is whenever we implement a specific
[00:45:35] feature, let's also review it with Code
[00:45:37] Rabbit. There's been a report that says
[00:45:40] that AI code creates 1.7 times more
[00:45:42] problems, which means that even though
[00:45:44] we're faster, we're producing more
[00:45:46] issues per PR. Also, the code becomes
[00:45:50] less readable, naturally, and the error
[00:45:52] handling isn't being done properly.
[00:45:54] Security also suffers. So, let's add
[00:45:57] that one additional line of defense.
[00:45:59] Let's review every single feature that
[00:46:01] we add to our project in the same way
[00:46:03] that biggest teams, such as the
[00:46:04] developers over at Nvidia, are doing it.
[00:46:07] I'll leave the link down in the
[00:46:08] description, so you can create your free
[00:46:10] account and follow along.
[00:46:12] You can log in with GitHub, and once
[00:46:14] you're in, you'll be able to see that I
[00:46:15] already gave it access to many of my
[00:46:17] repos. But first, we got to push our
[00:46:19] project over to GitHub. So, head over to
[00:46:22] github.com/new
[00:46:24] and create a new repo. You can call it
[00:46:26] Ghost AI.
[00:46:30] And just create it. Next, you can copy
[00:46:32] these commands one by one, or you can
[00:46:35] just copy all of them together,
[00:46:37] open up your agent, and paste it. Then,
[00:46:39] press enter. It's going to ask us
[00:46:41] whether we're going to allow it to stage
[00:46:43] all the changes. So, I'll say, "Yeah, go
[00:46:45] ahead." And it'll also allow all future
[00:46:47] commits, as that's going to help us
[00:46:49] speed up the workflow, as well as adding
[00:46:51] a remote, and finally push. You can see
[00:46:54] that the changes have been pushed
[00:46:55] successfully. So, if you come back and
[00:46:57] reload,
[00:46:59] you'll be able to see the current list
[00:47:00] of changes over on the repo. It's always
[00:47:03] good to make your project descriptive,
[00:47:05] so you can remove the releases,
[00:47:07] deployments, and packages, and add a
[00:47:09] short description,
[00:47:10] such as Ghost AI
[00:47:13] is an interactive systems
[00:47:16] architecture
[00:47:19] builder.
[00:47:20] We can route to the deployed website.
[00:47:21] For now, I'll just route it to
[00:47:23] jsmastery.com, and here we can put the
[00:47:25] different topics, such as Next.js,
[00:47:28] React, My Blocks, Clerk, Trigger.dev,
[00:47:33] and even Code Rabbit, which we'll be
[00:47:34] using for reviewing your code. And I
[00:47:37] like how AI always adds nice commit
[00:47:39] messages and not random gibberish that
[00:47:41] I'm used to. But yeah, now back within
[00:47:44] Code Rabbit, you can head over to add
[00:47:46] repositories,
[00:47:47] sign in, and give it access to all your
[00:47:49] repos. And then, when you're back, you
[00:47:52] can just find your project right here.
[00:47:58] Which means that it's automatically
[00:47:59] being tracked. So, as soon as we start
[00:48:01] adding the real features to the app,
[00:48:03] we'll be able to open up a PR for every
[00:48:05] new feature as we're developing within a
[00:48:07] large organization and then get it
[00:48:09] reviewed and only when Code Rabbit gives
[00:48:11] it a green light,
[00:48:12] merge it over to main.


## Chapter 06: Layout Setup (00:48:14)

[00:48:16] Now that our colors are in and the
[00:48:18] initial Shards and components are in as
[00:48:20] well, we are ready to start building the
[00:48:22] actual application. And the first thing
[00:48:24] that we need is the editor, including
[00:48:27] the top navbar and the left sidebar
[00:48:29] because they're the foundation of every
[00:48:30] feature we're going to build from here
[00:48:32] on. We're not yet touching off and we're
[00:48:35] not building this project creation. We
[00:48:37] just need to establish the layout so
[00:48:39] when these features come, they have
[00:48:41] somewhere to go. So, inside of feature
[00:48:43] specs folder, create a new file called
[00:48:46] 02 editor.md.
[00:48:49] And within it, we're going to follow a
[00:48:50] similar structure we followed before. We
[00:48:53] want to start with explaining what we
[00:48:55] need,
[00:48:56] such as the base chrome components that
[00:48:58] frame every editor screen, the top
[00:49:00] navbar and the left sidebar shell. These
[00:49:04] will be reused and extended in every
[00:49:06] chapter that follows. Then, we need to
[00:49:08] focus on what are we actually creating?
[00:49:11] That's going to be the editor navbar.
[00:49:14] So, we wanted to create a new component
[00:49:16] within the editor editor navbar file
[00:49:19] and then we want to specify some
[00:49:20] requirements that follow. We want this
[00:49:23] navbar to be of a fixed height at the
[00:49:25] top. We want it to have both left,
[00:49:28] center, and right sections, which you
[00:49:30] can see right here. On the left, we open
[00:49:32] up the sidebar. In the middle, we have
[00:49:34] the name and on the right side, we have
[00:49:36] additional actions. That's exactly what
[00:49:38] we explained right here.
[00:49:41] And of course, it's going to be of a
[00:49:42] dark background with a subtle bottom
[00:49:44] border. Next, we want to explain what we
[00:49:47] want to do with the project sidebar. So,
[00:49:49] right below, we can say create a project
[00:49:52] sidebar component.
[00:49:54] It should float above the editor canvas.
[00:49:57] Opening it should not push the page
[00:49:59] content. So, you can see it remains
[00:50:01] where it is.
[00:50:03] And slides in from the left. It has the
[00:50:05] header that says projects and title and
[00:50:08] a close button right here. It can use
[00:50:10] the Shazian tabs component. And both
[00:50:13] tabs show empty placeholder state, full
[00:50:16] width new project button at the bottom
[00:50:18] with the plus icon. So, something like
[00:50:20] this. Oh, and finally, when we click
[00:50:23] create new project, we need this kind of
[00:50:25] a dialogue. A new pop-up that shows.
[00:50:29] So, for that, we can say something along
[00:50:31] the lines of
[00:50:33] dialogue pattern. Use the existing color
[00:50:36] tokens from globals for dialogue
[00:50:37] styling. It supports title, description,
[00:50:40] and footer action, but don't build any
[00:50:42] dialogues yet.
[00:50:44] We just want to create the component for
[00:50:46] it. Finally, to check whether it is
[00:50:48] done, we can check whether new
[00:50:50] components compile without TypeScript
[00:50:52] errors, no lint errors, and diagram
[00:50:54] pattern is ready for future use. So,
[00:50:57] hopefully, you were typing this out with
[00:50:59] me, or maybe you paused the screen and
[00:51:01] typed it with your own words. But, this
[00:51:03] course isn't at all about typing. It is
[00:51:06] about understanding what we're doing
[00:51:08] right here. So, if you don't really feel
[00:51:10] like typing, nor you should, in the
[00:51:12] video kit link down in the description,
[00:51:14] I'll provide you with all the prompts
[00:51:17] that we're going to use throughout the
[00:51:18] rest of this course. So, if at any point
[00:51:20] I'm going too fast when explaining them,
[00:51:23] and you just want to have it on your end
[00:51:25] and listen along, you can totally do
[00:51:27] that. But, yeah, let me quickly walk you
[00:51:29] through the structure because this is
[00:51:31] the template that every spec file in
[00:51:33] this project will follow. We start with
[00:51:35] a goal. One or two sentences, what does
[00:51:38] this unit produce when it is done? Then,
[00:51:41] we go over some specific design
[00:51:42] decisions. Is it visual or structural or
[00:51:46] something specific to the component like
[00:51:48] layout behavior, responsiveness, and
[00:51:51] this is where we can refer to that UI
[00:51:53] context file so that the agent isn't
[00:51:55] guessing the colors.
[00:51:56] Then we go over into implementation, and
[00:51:59] in this case, I decided to separate it
[00:52:01] into sections. So, we have the editor
[00:52:03] navbar, the project sidebar, and the
[00:52:06] dialog pattern, and finally the
[00:52:08] verification checklist. So, let's open
[00:52:10] up our agent. Whenever you're building a
[00:52:12] new feature, always open up a new chat
[00:52:15] and don't use one of the older chats.
[00:52:17] That's because we don't want some stale
[00:52:19] context lingering around. Only remain
[00:52:21] within the same chat when what you're
[00:52:23] about to do next is related to what
[00:52:25] you've done before, such as when you
[00:52:27] want to fix specific issues. You can see
[00:52:29] that it already has access to the editor
[00:52:31] file.
[00:52:33] So, I'll say, "Read this file and update
[00:52:37] the tasks on the progress
[00:52:40] tracker and then
[00:52:43] implement it
[00:52:45] exactly as specified."
[00:52:48] And press enter. And in about a minute,
[00:52:51] it's all done.
[00:52:52] It developed the editor navbar, the
[00:52:54] sidebar, and also the dialog pattern.
[00:52:58] TypeScript and ESLint both pass clean.
[00:53:00] Progress tracker also got updated. So,
[00:53:03] let's check the progress tracker first.
[00:53:05] It'll be right here within the progress
[00:53:07] tracker.
[00:53:08] So, if you check feature two completed,
[00:53:12] editor navbar and project sidebar both
[00:53:15] implemented. You can see them right here
[00:53:17] under editor, editor navbar, and project
[00:53:20] sidebar.
[00:53:21] We just created them so far, but they're
[00:53:23] not yet being used within the layout.
[00:53:25] And even though this wasn't part of the
[00:53:27] checks,
[00:53:28] I want to actually be able to see them.
[00:53:30] I want to tell it to use the navbar and
[00:53:33] the sidebar right now within the
[00:53:34] project. So, I'll open up the chat in
[00:53:37] the same context window and tell it to
[00:53:39] use these two components within a
[00:53:41] layout. And within a minute it put it to
[00:53:44] use. It even created a placeholder page
[00:53:46] so we can navigate over to the editor
[00:53:49] and check it out. So, head over to
[00:53:50] localhost:3000/editor,
[00:53:53] and you can see a canvas coming soon,
[00:53:55] but there is a top bar and a left
[00:53:58] sidebar, which opens up the projects.
[00:54:01] So, you can see that what we requested
[00:54:03] indeed got implemented. Since we're not
[00:54:05] yet at the point where we need that
[00:54:06] because we don't even yet have the
[00:54:08] editor, I actually want to show you how
[00:54:10] you can undo the changes, at least right
[00:54:12] here in Claude code. The only thing you
[00:54:14] have to do is press this back arrow on
[00:54:16] the message that you used to create
[00:54:18] these components, and then say rewind
[00:54:20] code to here. Which is going to bring us
[00:54:22] back and only give us what the
[00:54:24] specification wanted, and that is the
[00:54:27] components that we can then use and that
[00:54:29] compile, but we're not using them quite
[00:54:32] yet. Perfect. So, now that we have the
[00:54:33] navbar and a togglable sidebar, let's
[00:54:36] quickly check them out. The editor
[00:54:38] navbar is pretty straightforward, and
[00:54:40] the sidebar accepts some props such as
[00:54:42] is open and on close, and uses the
[00:54:44] Shadsy and tabs to modify what's being
[00:54:47] shown. But, when you're writing code
[00:54:48] yourself, you have a natural
[00:54:50] understanding of every decision you
[00:54:52] made. Heck, you wrote it.
[00:54:54] You know why a function is structured in
[00:54:57] a specific way or why you used specific
[00:54:59] props.
[00:55:01] But, AI-generated code doesn't come with
[00:55:04] that context.
[00:55:05] The agent made decisions that that were
[00:55:08] reasonable most of the time, but you
[00:55:11] didn't make them. And that means that
[00:55:13] reviewing AI output isn't optional. It's
[00:55:16] the step that keeps you in control of
[00:55:17] your own codebase. So, that's the
[00:55:19] perfect use case to test out the Code
[00:55:21] Rabbit edition that we added in the last
[00:55:23] lesson. I'll open up the chat and tell
[00:55:25] it to push all the current changes to a
[00:55:29] new branch called development.
[00:55:31] Typically, in real production databases,
[00:55:33] you often have multiple branches such as
[00:55:36] dev, staging, and only then main.
[00:55:40] So, for now, we want to push this over
[00:55:41] to the development branch, get it
[00:55:43] reviewed, and only if it's good, merge
[00:55:45] it over to main. So, by giving it this
[00:55:47] quick message, it'll run a couple of Git
[00:55:50] commands,
[00:55:51] figure out that we're currently on main,
[00:55:53] that we need to switch over and push to
[00:55:55] that new branch. And that's a little pro
[00:55:57] tip. Uh-huh, I mean, sure you could run
[00:56:00] these commands through the terminal, but
[00:56:02] I find it super easy to just stay in
[00:56:04] flow and tell the agent to push the code
[00:56:07] for me, which you can see it just did.
[00:56:09] So, if you head back over to your repo,
[00:56:11] you'll see that the development branch
[00:56:13] had recent pushes 3 seconds ago.
[00:56:15] So, let's go ahead and compare them and
[00:56:17] open up the pull request. We have 333
[00:56:20] new lines of code across five different
[00:56:23] files. So, Code Rabbit immediately
[00:56:25] hooked itself onto the PR, and we'll see
[00:56:28] whether it'll be able to pull out some
[00:56:29] bugs out of the hat.
[00:56:31] Let's give it a minute, and then I'll be
[00:56:33] right back. And we got back the
[00:56:35] walk-through, where it says exactly what
[00:56:38] we introduced in this project, such as
[00:56:40] two new React components for an editor
[00:56:42] UI Chrome, an editor navbar, and a
[00:56:45] project sidebar. These are super simple,
[00:56:47] as this was a simple review. Later on,
[00:56:50] these are going to get much more
[00:56:51] detailed, but yeah, let's check whether
[00:56:54] we have some potential issues even on a
[00:56:56] simple PR, such as this one. There's one
[00:56:58] major issue that says, "Hide the
[00:57:01] off-screen sidebar from focus order and
[00:57:03] assistive tech when closed." So,
[00:57:05] specifically, this is an accessibility
[00:57:07] fix, which is definitely a good
[00:57:09] implementation.
[00:57:10] Since we haven't yet utilized this
[00:57:12] component in our app, I'll leave this so
[00:57:13] we can add it later. There's also a
[00:57:15] minor issue, where the spec lists only
[00:57:18] the is open for the sidebar, but the
[00:57:21] implementation also requires on close.
[00:57:23] So, actually, it's suggesting to change
[00:57:25] the specification. This is interesting,
[00:57:27] because sometimes you're going to miss
[00:57:29] some stuff from the spec, and it's okay
[00:57:31] if AI tries to fix it or add some stuff,
[00:57:35] but it's equally as important for Code
[00:57:37] Rabbit to flag it. Because the whole
[00:57:39] reason why we're writing specs in the
[00:57:41] first place is so we can have predictive
[00:57:43] output. So basically, you can just copy
[00:57:45] this part right here, go back to your
[00:57:47] code base where we're saying accepts
[00:57:50] and then it's going to be is open prop.
[00:57:52] But we're going to say accepts both is
[00:57:55] open and on close props. Little change,
[00:57:59] I know, but now our code base is
[00:58:01] consistent with the spec. And that's it
[00:58:03] for this simple PR. As we continue
[00:58:05] developing more components, the reviews
[00:58:07] are going to get significantly more
[00:58:09] detailed. So for now, I'm going to go
[00:58:11] ahead and merge it, which means that we
[00:58:13] are ready to continue developing the
[00:58:15] next component.


## Chapter 07: Authentication (00:58:17)

[00:58:18] For this type of application, we don't
[00:58:21] really need a traditional homepage.
[00:58:23] Most tools like this drop you straight
[00:58:26] into the editor.
[00:58:27] You sign in from a simple sign in page
[00:58:30] and you manage everything from the
[00:58:32] canvas. And that's exactly what we'll do
[00:58:34] within our app.
[00:58:36] But we need auth, sign in, sign up, and
[00:58:39] other similar pages where you explain
[00:58:41] how your application works
[00:58:43] and then allow users to sign back in. So
[00:58:46] to get that set up, click the Clerk link
[00:58:48] down in the description and sign in. You
[00:58:50] can sign in with Google or GitHub. And
[00:58:53] once you're in, you can head over to
[00:58:54] applications and create a new app on the
[00:58:57] dashboard. You can give it a name such
[00:58:59] as Ghost AI and choose the sign in
[00:59:02] options
[00:59:03] such as email, Google, and since this is
[00:59:06] a development website, we can also do
[00:59:08] GitHub. Then click create application.
[00:59:11] We're building on Next.js, so what you
[00:59:13] can do is just install @clerk/nextjs
[00:59:17] by copying this command and paste it
[00:59:20] straight into the terminal.
[00:59:22] And while that is being installed, you
[00:59:24] can also set up your Clerk API keys by
[00:59:27] copying them from here
[00:59:29] and creating a new file called
[00:59:31] .env.local
[00:59:34] and then paste them right here.
[00:59:35] Now, before we hand anything over to the
[00:59:38] agent, there are two things you need to
[00:59:40] know about Clerk and Next.js 16
[00:59:42] specifically, because if you skip this,
[00:59:45] the agent will get it wrong. And it says
[00:59:47] it right here. If you're using Next.js
[00:59:49] 15 or lower, name your file
[00:59:52] middleware.ts instead of proxy.ts.
[00:59:56] The code itself remains the same, only
[00:59:58] the file name changes. But, because most
[01:00:00] agents were trained on Next.js 14 and 15
[01:00:03] code bases, it'll almost certainly
[01:00:06] create a middleware.ts file by default.
[01:00:09] So, we'll have to specify proxy.ts
[01:00:11] explicitly in our spec so it doesn't
[01:00:13] have to guess. Oh, and another important
[01:00:15] thing is that just by adding middleware,
[01:00:18] it doesn't automatically protect all
[01:00:20] routes. As you can see right here, by
[01:00:22] default, it leaves all the routes
[01:00:24] public. And this catches a lot of
[01:00:26] developers. You have to explicitly
[01:00:28] define which routes are protected and
[01:00:31] which are public, which means that we
[01:00:32] have to configure everything
[01:00:34] intentionally. And this is exactly why
[01:00:36] reading the updated documentation before
[01:00:38] building with AI matters. The agent
[01:00:41] knows Clerk, not necessarily the version
[01:00:43] of Clerk you just installed or the
[01:00:45] version of Next.js you're running on.
[01:00:46] The spec bridges that gap. Oh, but we
[01:00:49] can also use agent skills.
[01:00:52] As I told you at the start, most major
[01:00:54] frameworks and libraries now publish
[01:00:56] official skill packages specifically for
[01:00:58] this problem. It gives your agent
[01:01:00] up-to-date knowledge, current APIs, and
[01:01:03] patterns, and the best practices of the
[01:01:05] library you're using. So, if you search
[01:01:07] on Google or within the docs, Clerk
[01:01:09] agent skills, you'll be redirected to
[01:01:11] this page. Then, simply copy the
[01:01:14] installation command,
[01:01:15] head back over to your code base and
[01:01:17] paste it in your terminal. npx skills
[01:01:20] add clerk skills. Press enter.
[01:01:24] You might need to install the skills
[01:01:25] package by saying Y and then enter. And
[01:01:28] then, by pressing the arrow up and down
[01:01:30] keys and the space key, you can select
[01:01:33] specific packages, such as core clerk.
[01:01:36] You can either select some additional
[01:01:38] clerk features or some additional clerk
[01:01:40] frameworks. Like in this case, I'm going
[01:01:42] to go with clerk next js patterns. And
[01:01:46] press enter.
[01:01:48] Then, you can select additional agents
[01:01:50] that you want to add it to. By default,
[01:01:52] it's going to work on codex, cursor, and
[01:01:54] anti-gravity. But, if you want to add
[01:01:56] Claude code, you have to select it here
[01:01:58] and press enter.
[01:02:00] And we can install it in project scope
[01:02:02] via symlink. That's the recommended way.
[01:02:05] So, just proceed with installation.
[01:02:07] Perfect. Our skill is installed and
[01:02:09] we'll be able to invoke it later on once
[01:02:12] we focus on implementing the auth
[01:02:13] functionality.
[01:02:15] So, now we are ready to write the spec.
[01:02:19] Open up your context feature specs and
[01:02:21] create a new file called 03 auth.md.
[01:02:25] And once again, the full feature specs
[01:02:28] files are linked in the description in
[01:02:30] case you want to just copy them and then
[01:02:31] follow along. Or, you can slowly type it
[01:02:34] out with me.
[01:02:35] Let's start by telling it that clerk is
[01:02:38] already installed and connected. So, we
[01:02:40] just need to wire it into the next js
[01:02:42] app, provider, auth pages, redirects,
[01:02:46] route protections, and the user menu.
[01:02:49] When it comes to the design, we just
[01:02:52] want to use the clerk's dark theme from
[01:02:54] the @clerk/ui themes as the base, and
[01:02:57] then we want to override the clerk
[01:03:00] appearance variables using the app's
[01:03:02] existing CSS variables.
[01:03:05] With no hardcoded colors. For the sign
[01:03:08] up and sign in pages, this is what we
[01:03:11] want to develop. On large screens, we
[01:03:14] just want to have a simple two-panel
[01:03:16] layout. On the left side, a logo, a
[01:03:19] tagline, and text-only features. On the
[01:03:22] right side, a centered Clerk form, and
[01:03:25] on small screens, forms only.
[01:03:27] We don't want to have any kind of
[01:03:29] gradients, as that's going to seem
[01:03:30] AI-ish. No oversized hero sections,
[01:03:33] cards, or scroll-heavy layouts. Keep the
[01:03:36] layout minimal and professional.
[01:03:38] And then we can dive into a bit more
[01:03:40] details on the full implementation.
[01:03:43] So, we can say
[01:03:46] wrap the root layout with a Clerk
[01:03:48] provider using the Clerk's dark theme.
[01:03:52] Create sign-in and sign-up pages using
[01:03:54] Clerk components. And as I told you
[01:03:56] before, we have to be specific in
[01:03:58] telling it that it should use the
[01:04:00] proxy.ts file name at the project root
[01:04:03] instead of the middleware.ts.
[01:04:06] And then, we have to define public
[01:04:07] routes using the existing sign-in and
[01:04:10] sign-up environment variables. Protect
[01:04:12] everything else by default. Which means
[01:04:15] that we have to update our home page so
[01:04:18] that when authenticated users visit it,
[01:04:21] we redirect them to the editor. Or when
[01:04:24] unauthenticated users visit it, we
[01:04:26] redirect them to the sign-in page.
[01:04:29] We also want to implement Clerk's
[01:04:32] built-in user button to the editor
[01:04:35] navbar right section for profile
[01:04:37] settings and log out. We want to keep
[01:04:39] Clerk's default user menu and profile
[01:04:41] flows intact and not rebuild heavily
[01:04:44] custom- ized Clerk internals, and want
[01:04:46] to use existing Clerk environment
[01:04:48] variables without renaming or inventing
[01:04:51] new ones. Finally, we can specify
[01:04:54] additional dependencies, such as Clerk
[01:04:56] UI, if we need to install it. And then,
[01:04:59] when it's done, we want to check that
[01:05:00] proxy file is there, that all routes are
[01:05:03] protected except public auth routes,
[01:05:06] auth pages use CSS variables with no
[01:05:09] hardcoded colors, Clerk provider wraps
[01:05:12] the layout and the build passes. This is
[01:05:15] our complete authentication
[01:05:17] implementation. Now, you know the drill.
[01:05:20] Go ahead and open up your agent,
[01:05:22] give it access to this file, and tell it
[01:05:25] to read this file and update the
[01:05:28] progress tracker.md file accordingly.
[01:05:31] Then, implement the auth feature exactly
[01:05:34] as specified in the auth.md file. Okay?
[01:05:38] You can see that the built-in microphone
[01:05:40] feature right here still isn't perfect.
[01:05:42] Let me try to do the same thing with
[01:05:43] Whisper flow specified in auth.md file.
[01:05:50] There we go. That's a bit better, and
[01:05:52] specifically it's 03.auth.md.
[01:05:55] Perfect. Let's go ahead and run it.
[01:05:58] First, it's asking me to run some bash
[01:06:00] commands to check whether Clerk has been
[01:06:02] properly installed, and we'll say,
[01:06:04] "Yeah, go ahead, you can run it." It
[01:06:06] took him about 2 minutes or so to go
[01:06:09] through all the context we shared, and
[01:06:11] only then it'll start to implement
[01:06:13] everything in parallel.
[01:06:15] And this is much better than if it
[01:06:17] started right away and then just ended
[01:06:20] up with a bunch of mistakes. So, the
[01:06:21] list of updates that it put right here
[01:06:23] is to update the .env.local with Clerk
[01:06:26] sign-in and sign-up URL vars, create a
[01:06:29] proxy with Clerk middleware route
[01:06:31] protection, update the app layout with a
[01:06:33] Clerk provider and dark theme, create
[01:06:36] sign-in and sign-up pages with a
[01:06:38] two-panel layout,
[01:06:39] update the app page to redirect based on
[01:06:42] the auth state, add the user button to
[01:06:44] editor navbar,
[01:06:46] and create editor page, and then update
[01:06:48] the progress tracker, and run npm run
[01:06:50] build to verify. It's going to ask me
[01:06:53] whether it has the ability to create
[01:06:55] some directories, and I'll tell it,
[01:06:57] "Yeah, go ahead."
[01:06:58] And in the future we can give it some
[01:07:00] more permissions so it can do things a
[01:07:02] bit more freely. And after it came up
[01:07:04] with the initial plan, it actually built
[01:07:07] out everything pretty quickly. Maybe
[01:07:09] even in less time than it used to think
[01:07:12] how to approach it in the first place,
[01:07:13] which shows you just how important the
[01:07:16] initial context and a proper task are.
[01:07:19] And there we go. The build passes, and
[01:07:21] here's the summary of everything that
[01:07:23] was implemented. I think all of these
[01:07:25] things right here shouldn't come as a
[01:07:27] surprise because we initially specified
[01:07:30] them in the spec. Then it updated the
[01:07:33] to-do's, and now it just did it. And
[01:07:36] yeah, it's pretty interesting that it
[01:07:37] even notes right here that it would have
[01:07:39] gotten confused about this middleware
[01:07:41] proxy thing if we didn't specify it
[01:07:43] properly. But thankfully, it did it in
[01:07:46] the right way thanks to the research
[01:07:47] that we've done at the start.
[01:07:49] So, what do you say that we take it for
[01:07:51] a spin? The application is running on
[01:07:53] localhost 3000, but whenever I make some
[01:07:55] bigger changes, I like to rerun it. But
[01:07:58] initially, if you head over to
[01:07:59] localhost, you might get redirected to
[01:08:02] this clerk handshake part, which is
[01:08:04] going to lead to a broken page. But
[01:08:06] after you reload, it should properly
[01:08:09] redirect you back to the homepage. And
[01:08:11] after that, it should just work.
[01:08:14] This is something that we can polish and
[01:08:16] fix up later on.
[01:08:18] But yeah, this is looking interesting.
[01:08:20] Definitely not quite as nice as the
[01:08:23] original application that I've showed
[01:08:25] you that's deployed.
[01:08:26] So, what are some of the things that we
[01:08:28] can do to make it look more similar to
[01:08:31] that one? Well, step one is to search
[01:08:34] some kind of design websites online like
[01:08:36] Dribbble or award-winning websites, and
[01:08:39] then just take a screenshot and try to
[01:08:41] get it to match to that closer. Or in
[01:08:43] this case, you can head over to the
[01:08:45] deployed version of this application,
[01:08:48] take a screenshot of this whole UI that
[01:08:51] you can see right here,
[01:08:52] and then we can feed it over into our
[01:08:55] chat. So, go ahead and open up the chat.
[01:08:57] Keep in mind that we can still stay
[01:08:59] within the authentication window that we
[01:09:01] worked on
[01:09:02] because now we're fixing some parts
[01:09:04] about that specific implementation. So,
[01:09:06] what you can do is just click this plus
[01:09:08] right here and upload from computer or
[01:09:10] just drag and drop the screenshot. Then,
[01:09:13] select it and then we can further point
[01:09:15] out to some things that could be
[01:09:17] improved, not just the layout. It seems
[01:09:19] like it didn't properly read the fonts,
[01:09:22] that the right side of the screen is
[01:09:24] taking a larger portion, so maybe we can
[01:09:26] split them 50/50, same as it is right
[01:09:28] here, and make the font size a bit
[01:09:31] larger. So, it's not just the layout. We
[01:09:33] needed to review the screenshot and
[01:09:35] update the UI of our current application
[01:09:38] to look more like the one on the
[01:09:39] screenshot. Means 50/50 left and right
[01:09:43] side layout with some kind of a color on
[01:09:45] the left side to differentiate it from a
[01:09:47] dark background,
[01:09:49] as well as we need to fix the fonts so
[01:09:51] that it uses the ones outlined in our UI
[01:09:55] guidelines. I think for now this is
[01:09:56] going to be enough for it to get closer
[01:09:59] to the design we want to get. So, press
[01:10:01] enter and let's see how it handles it.
[01:10:03] And there we go, the build passes, it
[01:10:06] updated the globals from circular font
[01:10:08] reference to the one that should be
[01:10:10] correct right now. The body was pointing
[01:10:12] at itself, so this font was never
[01:10:15] actually applied to anything. Same fix
[01:10:17] for the heading and it also implemented
[01:10:19] some other fixes. Let's check it out.
[01:10:21] The design now looks much closer to the
[01:10:23] finished product. The fonts are being
[01:10:26] properly applied and that makes a big
[01:10:28] difference. So does the increase in font
[01:10:30] size and this shift between the two
[01:10:33] different background colors. Of course,
[01:10:35] later on we can come up with a unique
[01:10:37] logo that we can put right here, but for
[01:10:39] now this is looking great.
[01:10:41] And believe it or not, we have a fully
[01:10:44] functional authentication system built
[01:10:46] in right here. So, what do you say that
[01:10:48] we go ahead and test it out? You can
[01:10:50] head over to sign up to see whether that
[01:10:52] works and it does. Later on, if you want
[01:10:55] to, you can modify the contents on the
[01:10:57] left side depending on whether you're in
[01:10:59] sign-in or sign-up page. And then let's
[01:11:01] use something like GitHub to sign in.
[01:11:04] I'll authorize it and the redirect
[01:11:06] redirects us to a page that currently
[01:11:09] breaks. So, I'll try to head back over
[01:11:12] to localhost:3000 one more time. And now
[01:11:15] when we get back, it actually redirects
[01:11:17] to the editor properly. You can see that
[01:11:20] we have the sidebar, we have a space for
[01:11:23] the canvas that's about to come in the
[01:11:25] future. And then on top right, we see
[01:11:27] all the information about our currently
[01:11:29] logged-in account, which is beautiful. I
[01:11:31] mean, we get complete user management
[01:11:34] within a single prompt that we've done.
[01:11:36] Let's also try to sign out for now, and
[01:11:38] we do get one issue when we click that
[01:11:40] button saying there's an unexpected
[01:11:43] response received from the server. So,
[01:11:45] if we head back over here and open up
[01:11:47] the terminal, we can see an unhandled
[01:11:49] rejection. Unexpected response was
[01:11:51] received from the server. And then in
[01:11:53] the terminal, we see something like
[01:11:55] this, which doesn't really tell us much.
[01:11:58] Now, what we could do is just copy this,
[01:12:00] open up the chat window one more time by
[01:12:03] heading over here, and then just pasting
[01:12:06] this error and telling it to fix it.
[01:12:08] But, I'm actually glad that this error
[01:12:10] happened because I can teach you a bit
[01:12:12] better and more precise way to handle
[01:12:14] these issues and so that when you try to
[01:12:16] fix them, you don't cause new ones.
[01:12:19] So, instead of pasting this right into
[01:12:21] the chat, we're actually going to open
[01:12:22] up a new file right here within context
[01:12:26] and call it current issues.md.
[01:12:31] You can even do it within feature specs.
[01:12:33] Either way works. Then, you can paste
[01:12:35] any kind of errors that you have and
[01:12:37] explain what's happening. So, I'll
[01:12:39] explain that when I click the logout
[01:12:43] button,
[01:12:46] the following error appears. And now I
[01:12:49] can paste this error message. And we can
[01:12:51] also specify that sometimes when we log
[01:12:54] in, we get redirected to this weird long
[01:12:57] URL, which doesn't show anything on the
[01:12:59] page.
[01:13:00] And then we can just paste this URL
[01:13:03] right here. Again, the errors on your
[01:13:05] end might be a bit different from what
[01:13:08] I'm seeing right here. Whatever they
[01:13:10] are, I don't want to teach you how to
[01:13:12] copy and paste. I want to teach you how
[01:13:14] to solve the problems for yourself.
[01:13:16] Explore the current issues file and
[01:13:19] deeply analyze the problem.
[01:13:22] Only when you have the analysis, give it
[01:13:24] back to me with the idea of how you're
[01:13:26] planning to solve it, and then wait for
[01:13:28] me to give it the green light to execute
[01:13:31] it. So yeah, writing something like this
[01:13:33] makes sense because that way it doesn't
[01:13:35] go into the spiral of trying to fix its
[01:13:37] own bugs while breaking 10 other things.
[01:13:39] You provided the error, it's going to
[01:13:41] come back with the analysis. You're the
[01:13:43] one deciding whether that analysis makes
[01:13:45] sense and whether it can actually
[01:13:47] execute it. So, let's run it and see
[01:13:50] what it comes back with. And after some
[01:13:52] thinking, it's back with the analysis.
[01:13:55] And this is so much better and so much
[01:13:58] more detailed than if we just told it to
[01:14:00] fix it immediately. Now, it actually
[01:14:03] tried it out and has a deep idea of
[01:14:05] what's happening. The server log is the
[01:14:07] key clue. Proxy took 373 milliseconds
[01:14:11] out of a half a second total request.
[01:14:13] Almost all time is spent in the proxy.
[01:14:16] So, that already points it in the right
[01:14:18] direction.
[01:14:19] As a human person, I would never figure
[01:14:22] this out on my own. At least not from
[01:14:24] such a vague error message. But yeah,
[01:14:27] here it figures out that this button
[01:14:29] needs an after sign out URL. So, it's
[01:14:32] just going to add it.
[01:14:33] And a similar thing is happening with
[01:14:35] the handshake URL. It basically needs to
[01:14:38] configure that after sign up URL, and
[01:14:41] that way it's going to route it
[01:14:42] properly. So, it provided a two fix
[01:14:44] plan. So, this looks plausible to me,
[01:14:47] looks good. So, let's just tell it to
[01:14:50] execute the plan and fix the issues.
[01:14:52] There we go. So, the fix now seems very
[01:14:55] apparent. We just needed this after sign
[01:14:57] out URL. And if you want to learn more
[01:14:59] tips and tricks just like this one about
[01:15:02] actually analyzing and fixing the errors
[01:15:04] and how I approach building these
[01:15:06] production level applications,
[01:15:08] definitely check out the spec driven
[01:15:10] agentic development course. It's not out
[01:15:12] yet as it's going to be super detailed
[01:15:14] and it's going to follow the best
[01:15:15] practices from the strongest developer
[01:15:17] teams out there. But yeah, it'll be out
[01:15:19] soon, but I'm still super glad that
[01:15:21] while I'm developing that, you can still
[01:15:24] learn how I develop these applications
[01:15:26] with the agentic ways with this new
[01:15:28] video that you're watching right now.
[01:15:30] And you can let me know down in the
[01:15:32] comments how you like this new type of
[01:15:34] video. I get that it's completely
[01:15:36] different from manual coding, but I
[01:15:38] still think there's so much to learn and
[01:15:41] we can have a predictable development
[01:15:44] workflow even with AI doing the writing
[01:15:47] for us. So, let's see whether this
[01:15:49] actually fixes it. And the build passes.
[01:15:51] The after sign out URL prop was removed
[01:15:54] from the user button as it belongs in
[01:15:56] clerk options and is set via environment
[01:15:58] variables. So, we'll soon be able to
[01:16:00] verify whether that actually fixes it.
[01:16:03] But before, I want to open up my
[01:16:05] terminal,
[01:16:06] stop it from running and then rerun it
[01:16:08] again on localhost 3000 because we
[01:16:10] changed the ENVs, so we want to make
[01:16:12] sure that they're read by the browser.
[01:16:14] So now, heading back over to localhost
[01:16:16] 3000, maybe you're signed in already,
[01:16:18] which is fine. You can simply sign out
[01:16:20] now and that brings us to another error,
[01:16:23] which is the same one we've had before.
[01:16:25] And another thing you can do is head
[01:16:27] over to inspect element, switch over to
[01:16:29] the application tab, and then clear all
[01:16:32] the cookies. So, find the cookies for
[01:16:34] localhost 3000, clear them, and then
[01:16:36] reload the page.
[01:16:38] You'll be redirected back to the home
[01:16:40] page and now we can retry with a clean
[01:16:42] slate.
[01:16:43] So, I'll sign in using GitHub the same
[01:16:46] way I did before. That works. I
[01:16:48] automatically get redirected over to the
[01:16:50] editor, which is great. And now, I'll
[01:16:52] sign out, and that worked. So, now head
[01:16:55] back over within your terminal,
[01:16:57] run git add dot, git commit {dash} m,
[01:17:01] implement auth, and then git push. This
[01:17:04] is going to push all the changes to
[01:17:06] origin development, allowing us to open
[01:17:08] up a pull request over to the main
[01:17:10] branch. Then, you can open up a PR, and
[01:17:14] let's wait for CodeRabbit to review it.
[01:17:16] This time, we had many changes, but not
[01:17:19] many of them are directly related to
[01:17:21] what we did in the code. We just added
[01:17:23] these agent skills so that everybody
[01:17:25] else's agents working on this code base
[01:17:28] also, well, become smart in the
[01:17:30] technologies that we're using for the
[01:17:32] project. And then, yeah, of course, we
[01:17:34] implemented a couple of different files
[01:17:36] that CodeRabbit will verify. But,
[01:17:38] primarily, what we've done is right here
[01:17:41] within app, sign in and sign up pages,
[01:17:45] we have added some features that would
[01:17:46] display on the left side. And then, the
[01:17:48] sign-in page, where on the right side,
[01:17:51] we just render the sign-in component
[01:17:54] coming from Clerk.
[01:17:56] Similar thing happens over to the
[01:17:58] sign-up page. So, right here, we're just
[01:18:01] rendering the sign-up UI.
[01:18:03] Then,
[01:18:04] over in the layout, we are wrapping
[01:18:07] everything with a Clerk provider,
[01:18:09] setting the theme to dark, and setting
[01:18:11] some custom variables. That's it.
[01:18:14] Everything else remains the same. And
[01:18:15] then, within the editor page, we are
[01:18:18] simply showing the nav bar and the
[01:18:20] sidebar, as well as the rest of the
[01:18:22] content.
[01:18:23] In the nav bar, we display the Clerk
[01:18:26] user button, allowing us to see more
[01:18:27] info about the user, and allowing us to
[01:18:30] log us out. Pretty straightforward so
[01:18:32] far. As our components and features get
[01:18:34] more detailed, we're going to do deeper
[01:18:36] dives into the code base, but so far so
[01:18:39] good. Let's wait for the review. And
[01:18:41] quickly we're back with a full
[01:18:43] walk-through. This pull request
[01:18:45] integrates Clerk auth into a Next.js
[01:18:47] application and establishes
[01:18:49] comprehensive agent skills for Clerk
[01:18:52] integration across multiple frameworks.
[01:18:54] It also adds auth middleware, sign-in
[01:18:57] and sign-up pages, Clerk provider setup,
[01:18:59] and introduces five new skill
[01:19:01] definitions for supporting scripts,
[01:19:03] documentation, and so on. So, obviously
[01:19:06] a lot of the checks right here from
[01:19:08] CodeRabbit are going to be about the
[01:19:09] skills that we set up, but we can skip
[01:19:12] those for now and focus on the ones
[01:19:14] about the actual files we implemented.
[01:19:17] In this case, it looks like there's one
[01:19:19] critical issue, and that is within the
[01:19:21] context current issues.md.
[01:19:24] Well, you never want to publish current
[01:19:26] issues to GitHub anyways, because you
[01:19:28] want people to see your code and not
[01:19:30] your mistakes. Um what we're doing here
[01:19:33] is even worse. We're exposing the
[01:19:36] handshake or the JWT token from the
[01:19:38] track docs. So, this is a real security
[01:19:42] issue. So, what we need to do is delete
[01:19:44] this file. Obviously, this won't delete
[01:19:46] it from the Git history, but that's fine
[01:19:49] for us because this JWT is no longer in
[01:19:51] use.
[01:19:53] So, right here over to getignore, I'm
[01:19:54] going to add our {forward-slash} context
[01:19:58] {forward-slash}, and that's going to be
[01:20:00] the current issues
[01:20:03] .md file.
[01:20:05] And I'll also remove everything that is
[01:20:07] within it.
[01:20:09] Not that it matters right now, because
[01:20:10] we're adding it to getignore anyway. So,
[01:20:13] let's go ahead and push those changes by
[01:20:14] saying get add {dot} get commit update
[01:20:18] {dot} getignore.
[01:20:20] And get push. Immediately the changes
[01:20:23] will be recognized, which means that we
[01:20:24] can merge this over to the main branch.
[01:20:27] And while we're here, we can also head
[01:20:29] over into context on the main branch and
[01:20:32] remove the current issues file right
[01:20:34] here from GitHub by simply deleting the
[01:20:36] file.
[01:20:38] And committing the changes.
[01:20:40] We can also do the same thing on the
[01:20:41] development branch by heading over to
[01:20:43] context
[01:20:45] and heading over to current issues, and
[01:20:48] just removing the file
[01:20:50] so that it's no longer here, and it's
[01:20:51] not going to be pushed to GitHub any
[01:20:53] longer because we added it to get
[01:20:55] ignore.
[01:20:56] Perfect. With that in mind, we've
[01:20:58] successfully implemented the full UI and
[01:21:01] functionality for the authentication
[01:21:03] within our application.


## Chapter 08: Project Dialogues (01:21:05)

[01:21:07] Now that our authentication is done, and
[01:21:09] we can actually sign into our
[01:21:11] application, let's make the sidebar
[01:21:14] actually do something. As right now, it
[01:21:16] is just static. Before we hook up any
[01:21:19] real data, we need the UI in place.
[01:21:22] The create, rename, and delete
[01:21:25] dialogues, plus the editor home state.
[01:21:27] So, we're keeping this prompt focused on
[01:21:29] UI only with no API calls yet. Head over
[01:21:33] into context, feature specs, and add a
[01:21:36] new file called 04 project dialogues.
[01:21:40] Within it, we can specify that the goal
[01:21:43] is to build the editor home screen and
[01:21:45] add the project dialogues and sidebar
[01:21:47] actions with no API calls yet. So, what
[01:21:51] does this specifically mean?
[01:21:52] Well, it means that on the home page, we
[01:21:54] want to reuse the existing editor layout
[01:21:58] without modifying the navbar or sidebar
[01:22:00] behavior, but in the center of the page,
[01:22:02] we want to add a heading, create a
[01:22:04] project, or open up an existing one, and
[01:22:07] a description. Start a new architecture
[01:22:09] workspace or choose a project from the
[01:22:11] sidebar, and a new project button with a
[01:22:14] plus icon. Keeping the layout minimal
[01:22:16] without wrapping this content in cards.
[01:22:19] And then clicking new project should
[01:22:21] open up the create project dialogue.
[01:22:23] Let me actually show you what I mean by
[01:22:26] all of this by heading over to the
[01:22:27] finished version of the application, and
[01:22:30] quickly signing in. Notice how right
[01:22:32] here in the middle we have some text to
[01:22:34] greeting us, even though the canvas is
[01:22:36] empty, allowing us to create a new
[01:22:38] project, which then opens up this
[01:22:39] dialogue. That's exactly what we want to
[01:22:42] achieve.
[01:22:43] So, we'll have a dialogue for creating a
[01:22:45] new project, as well as for editing one,
[01:22:48] and deleting it. So, let's specify these
[01:22:51] three dialogues below.
[01:22:53] We're going to have one for creating a
[01:22:54] project that takes in the project name
[01:22:57] input, the live slug preview based on
[01:23:00] the name, and preview updates as the
[01:23:02] user types. Then, the one for the rename
[01:23:05] with pre-filled project name input, and
[01:23:08] the one for delete. Finally, on the
[01:23:10] sidebar, we want to add the following
[01:23:13] project item actions, rename and delete,
[01:23:16] show actions only for the projects that
[01:23:18] we own, and hide actions for the shared
[01:23:21] or projects belonging to collaborators,
[01:23:23] and on mobile, tapping outside the
[01:23:25] sidebar closes it, and want to add some
[01:23:27] kind of a backdrop scrim. Finally, let's
[01:23:29] specify the implementation right here by
[01:23:32] telling it to create a dedicated hook to
[01:23:35] manage the dialogue state, the form
[01:23:37] state, and the loading state, that way
[01:23:39] we can reuse the functionality.
[01:23:41] And then we want to wire the editor home
[01:23:44] new project to create dialogue, the
[01:23:47] sidebar create button to create dialogue
[01:23:49] as well, sidebar rename to rename
[01:23:52] dialogue, and sidebar delete to delete
[01:23:54] dialogue. For now, we only want to use
[01:23:56] mock project data with no API calls.
[01:24:00] And to check when it is done, we need to
[01:24:03] check that sidebar actions are wired,
[01:24:05] that slug preview works, that no
[01:24:07] TypeScript errors exist, and there's
[01:24:09] also no linting errors.
[01:24:11] So, let's open up Claude Code or your AI
[01:24:14] agent of choice,
[01:24:16] and then we can tell it to read this
[01:24:19] file, update the progress-tracker.md
[01:24:22] to mark this as in progress and then
[01:24:24] implement it exactly as specified. And
[01:24:28] let's run it.
[01:24:29] And in about a minute or so, feature
[01:24:31] four is done.
[01:24:33] Here's what's built. New file hooks use
[01:24:36] project dialogues, which centralizes the
[01:24:38] dialogue type, form, including the name
[01:24:41] and the slug, the loading state and mock
[01:24:44] data, which exposes these different
[01:24:46] functions to deal with the dialogues.
[01:24:48] Then there's the dialogue component, as
[01:24:50] well as within the project sidebar, we
[01:24:53] also call the dialogues when needed.
[01:24:56] So, let's quickly check this hooks file
[01:24:58] that it implemented. You can see that it
[01:25:00] is strictly typed right here with the
[01:25:02] project interface, the dialogue type, to
[01:25:05] slug, which takes in the name and turns
[01:25:07] it into a human readable ID,
[01:25:09] and it even created some mock three
[01:25:11] projects that we can verify.
[01:25:13] It came up with a lot of different use
[01:25:15] states, keeping track of all the
[01:25:17] projects, the dialogue type, the
[01:25:20] selected project, the name, slug, and
[01:25:22] loading.
[01:25:23] And all of these are going to be used
[01:25:25] within the dialogues themselves. Then it
[01:25:27] returns the data, so we can actually use
[01:25:29] them. Let's check where the dialogue is
[01:25:31] being used. Most often, it is right here
[01:25:33] within project dialogues,
[01:25:35] where we have the actual code for how
[01:25:37] the dialogue looks like. If the dialogue
[01:25:40] is of a type create, then we show this
[01:25:42] one. If it's of a type rename, we show
[01:25:44] this one. And if it's delete, we show
[01:25:47] the one below. Before we test it out,
[01:25:49] let's check out the progress tracker
[01:25:51] that says that the current phase is the
[01:25:53] feature four dialogues.
[01:25:55] It has the goal to do it. And it has
[01:25:58] actually completed the project dialogues
[01:26:00] with all of these different components.
[01:26:02] So, now if you come back to the editor,
[01:26:04] this is going to look much better. It's
[01:26:06] no longer just a blank screen, but
[01:26:08] rather in the middle, it says create a
[01:26:10] project or open up an existing one,
[01:26:12] start a new architectural workspace, or
[01:26:14] choose is project from the sidebar. And
[01:26:16] if you click create project, it actually
[01:26:19] opens up a new project dialogue where
[01:26:22] you can type something like my project.
[01:26:26] It automatically creates a slug at the
[01:26:28] bottom as well. And if you click create,
[01:26:30] you saw that creating loading.
[01:26:33] And of course, the data is currently
[01:26:35] static, but you can see how it's going
[01:26:37] to look once it actually picks the data
[01:26:39] from the database.
[01:26:41] So, we have Ghost AI Core, which you can
[01:26:44] select
[01:26:45] to edit its name
[01:26:47] as well as to delete it. This means that
[01:26:50] the UI for all of the dialogue
[01:26:52] functionalities has now been implemented
[01:26:54] alongside this centerpiece of the
[01:26:56] application, which means that now that
[01:26:58] the majority of the UI is done, in the
[01:27:00] next lesson, we can start focusing on
[01:27:03] implementing real data with a real
[01:27:05] database to make our app come to life.
[01:27:08] But before we dive into the database,
[01:27:10] let's make sure that our current code is
[01:27:12] good. And I want to show you another
[01:27:14] Code Rabbit feature allowing you to
[01:27:16] review your code directly within your VS
[01:27:18] Code, which means that you don't even
[01:27:20] have to create a PR and you can be that
[01:27:22] much faster. You can install the Code
[01:27:24] Rabbit extension, authenticate to your
[01:27:26] account.
[01:27:28] It'll notice the changes that you have
[01:27:29] right now, so you can just click review
[01:27:32] all changes. And the review will start
[01:27:34] directly within your editor.
[01:27:37] So, let's give it a minute. We'll check
[01:27:39] the changes and if they're good, push
[01:27:41] them. If not, we're going to fix them.
[01:27:43] And within a minute, the review is in
[01:27:45] and Code Rabbit left the comments
[01:27:47] directly on our code base. So, you can
[01:27:49] expand all the files and click on them
[01:27:52] to see exactly what's happening.
[01:27:55] For example, right here, specific
[01:27:57] confirmation message and project name
[01:27:58] display, the delete project dialogue
[01:28:01] lacks key detail. What text should be
[01:28:03] shown to the user? Should the dialogue
[01:28:05] show which project is being deleted? And
[01:28:08] should we show the cancel button as
[01:28:09] well? These are some important
[01:28:11] questions. And it's good because in this
[01:28:13] case Code Rabbit is telling us that we
[01:28:15] can be even more precise with our
[01:28:17] feature specifications. But, let's see
[01:28:19] if it has any comments within our code
[01:28:21] base. It says right here that the
[01:28:22] project item that is this one right here
[01:28:25] appears clickable, but it lacks
[01:28:27] interaction handling. It has a cursor
[01:28:29] pointer, that is this one right here in
[01:28:31] the sidebar, but when I click on it, it
[01:28:34] doesn't do anything. That's fine for now
[01:28:36] because later on we're going to make it
[01:28:37] open the actual canvas of that project.
[01:28:40] Since that is not implemented yet,
[01:28:42] that's totally fine. Then, another
[01:28:44] inconsistency, feature four is being
[01:28:46] marked as both in the current phase as
[01:28:49] well as finished right here at the
[01:28:50] bottom. So, we need to modify the
[01:28:52] progress tracker to say that the feature
[01:28:54] five is to be done. And then, and then
[01:28:57] modify the current goal to be determined
[01:29:00] for feature five. Next up, feature five.
[01:29:03] This is good. And finally, in the use
[01:29:05] project dialog hooks, we have a couple
[01:29:08] of comments as well.
[01:29:09] First, we have missing validation for
[01:29:12] empty slug edge case.
[01:29:14] If the user enters a name containing
[01:29:16] only special characters, it passes the
[01:29:18] truthy check, but returns an empty
[01:29:20] string, resulting in a project with an
[01:29:22] empty slug. So, if I head back right
[01:29:25] here and try to create something, take a
[01:29:27] look. It's true.
[01:29:29] I can actually create a new project, but
[01:29:31] nothing gets added to the slug because
[01:29:33] these are not valid slug characters. So,
[01:29:36] we definitely have to fix this.
[01:29:37] Thankfully, what we need to do is add
[01:29:40] slug validation.
[01:29:42] So, I'll just press accept right here
[01:29:45] and it'll update the code for me. That's
[01:29:47] another perk of using Code Rabbit within
[01:29:49] VS Code. And I think there is one other
[01:29:51] comment right here in this dialog, which
[01:29:54] is the same issue right here.
[01:29:56] Same as before, the rename operation has
[01:29:58] the edge case where the slug could end
[01:30:00] up empty. So, we definitely want to fix
[01:30:02] the validation there as well.
[01:30:05] Now, we can push the changes by saying
[01:30:07] get add dot, get commit {dash} m
[01:30:11] implement dialogues
[01:30:14] and then get pull to pull the latest
[01:30:16] changes and then run get push {dash}
[01:30:19] {dash} force to push the latest changes.
[01:30:22] Because remember, we deleted that file
[01:30:24] directly on GitHub, but still we want to
[01:30:25] push the local changes as well. So now
[01:30:28] if you want to, you can manually open up
[01:30:30] a PR by heading over to new pull request
[01:30:33] from the development branch
[01:30:34] over to the main branch
[01:30:37] and we can immediately merge it because
[01:30:39] we've already reviewed all the changes
[01:30:41] with Code Rabbit with their VS Code
[01:30:43] extension. So back within the
[01:30:45] application, you can run get pull
[01:30:48] and you can also check out to main and
[01:30:50] run get pull there as well
[01:30:53] to be up to date. But make sure to
[01:30:55] switch back to the development branch
[01:30:56] because that is where we're actively
[01:30:58] developing new features.


## Chapter 09: Prisma Setup (01:31:00)

[01:31:02] Now that our project management UI is
[01:31:04] wired up, we need the actual database
[01:31:06] behind it. And for that, we're going to
[01:31:08] use Prisma with Postgres.
[01:31:11] If you prefer a different database, the
[01:31:13] process is the same. Just swap the
[01:31:15] provider in the schema.
[01:31:17] Prisma supports Postgres, MySQL, SQLite,
[01:31:20] and more. So let's start with a manual
[01:31:23] installation right here within the
[01:31:24] terminal. Stop the app from running and
[01:31:27] then run npm install Prisma tsx {at}
[01:31:31] types {forward-slash} pg {dash} {dash}
[01:31:33] save {dash} dev. These are the dev
[01:31:35] dependencies so that we have a nice
[01:31:37] development workflow. After that is
[01:31:39] done, you can install all the necessary
[01:31:41] packages needed for us to set up our
[01:31:43] database such as {at} Prisma
[01:31:45] {forward-slash} client, Prisma adapter
[01:31:48] pg, {dot} env, and pg itself. And press
[01:31:52] enter. After that is done, initialize
[01:31:54] Prisma with the correct output path for
[01:31:57] the Next.js router.
[01:31:59] You can do that by running npx Prisma
[01:32:01] init dash dash output, data slash app
[01:32:04] generated Prisma. This creates a new
[01:32:07] Prisma folder with the schema.prisma
[01:32:10] file and an ENV file at the root. So,
[01:32:13] head over to the Prisma dashboard. I'll
[01:32:15] leave the link down in the description
[01:32:17] and create a new account. You can sign
[01:32:19] in with GitHub or Google. And once
[01:32:22] you're in, you can create a new project.
[01:32:25] I'll call it Ghost AI and they'll give
[01:32:28] you a one command setup, but in this
[01:32:30] case we can proceed with the connection
[01:32:32] string.
[01:32:33] So, you can just copy it and then head
[01:32:35] over into your .env and override the
[01:32:38] current database URL with the new one
[01:32:40] that you just got from the dashboard. As
[01:32:42] a matter of fact, we can take this
[01:32:43] database URL and put it within the
[01:32:45] .env.local as that's what we're using
[01:32:47] for our environment variables. Then,
[01:32:49] open up your prisma.config.ts
[01:32:53] and update the path to the schema. It's
[01:32:55] just going to be prisma forward slash.
[01:32:57] We want to remove this schema.prisma
[01:33:00] because we'll make a separate Prisma
[01:33:02] model.
[01:33:03] So, just use prisma forward slash. Now,
[01:33:06] before we run our spec, let's also
[01:33:08] install Prisma Agent Skill. We did the
[01:33:11] same thing with Clerk, so the same idea
[01:33:13] applies. Just for a different library.
[01:33:16] Open up your terminal and run MPX skills
[01:33:19] add Prisma skills.
[01:33:22] It'll ask you which ones you
[01:33:24] specifically want to install and in this
[01:33:26] case you can select all of them. CLI,
[01:33:28] client API, database setup, Postgres,
[01:33:31] Postgres setup, and upgrade V7 and press
[01:33:33] enter.
[01:33:35] You can install them for cloud code
[01:33:37] within this project with simlink.
[01:33:40] And we can proceed with the
[01:33:41] installation. And now we are ready to
[01:33:43] generate our schemas. So, let's create a
[01:33:46] new file right here within our context
[01:33:49] feature specs
[01:33:51] 05-prisma.md.
[01:33:54] And one sentence update is that Prisma
[01:33:56] is already installed, but we needed to
[01:33:59] add the project data models, Prisma
[01:34:01] client singleton, and the first
[01:34:03] migration. So, then we have to start
[01:34:05] specifying the models that we want to
[01:34:07] install.
[01:34:09] That we want to set up.
[01:34:11] First, we're going to have the project
[01:34:13] model.
[01:34:14] So, we'll ask it to add project that has
[01:34:19] to have an owner ID mapped to the Clerk
[01:34:21] user, a name, an optional description, a
[01:34:25] status enum, either draft or archived, a
[01:34:28] canvas JSON path for future canvas blob
[01:34:31] storage, timestamps, and indexes on
[01:34:34] owner ID and creation date. So, we can
[01:34:36] actually search through them. The second
[01:34:38] model we want to have is going to be the
[01:34:40] project collaborator, which is a project
[01:34:43] relation with cascading delete. It
[01:34:46] includes collaborator email, timestamp,
[01:34:49] and some constraints on the project and
[01:34:51] email, and indexes, so we can actually
[01:34:54] map over it. Do not add any extra fields
[01:34:56] unless required by Prisma. Finally, to
[01:34:59] be able to use these models, we have to
[01:35:01] set up Prisma client.
[01:35:03] So, create a lib prisma.ts file as a
[01:35:07] cached singleton,
[01:35:08] branch by database URL. If it starts
[01:35:11] with Prisma plus Postgres, then use
[01:35:13] accelerate, else direct to add Prisma
[01:35:16] adapter PG. In our case, it's going to
[01:35:19] start with Postgres forward slash, which
[01:35:22] means that it is actually hosted
[01:35:24] somewhere. Finally, we want to ask it to
[01:35:27] run the migrations and to generate that
[01:35:29] Prisma client, and want to verify
[01:35:31] whether it has installed all the
[01:35:32] dependencies,
[01:35:34] such as Prisma, Prisma client, Prisma
[01:35:36] adapter PG, and PG itself, and some
[01:35:39] checks are whether schema has both
[01:35:41] models with correct relations and
[01:35:43] indexes, the lib Prisma file exports one
[01:35:46] cached Prisma instance,
[01:35:48] the migration runs successfully, and the
[01:35:50] NPM run build passes. So, let's open up
[01:35:54] Claude Code, give it this file, and tell
[01:35:56] it to read this file, update the
[01:35:59] progress tracker, and implement it
[01:36:01] exactly as specified. I think you get
[01:36:04] the idea with these prompts.
[01:36:06] The actual spec file is doing the heavy
[01:36:08] lifting.
[01:36:09] So, let's see how it approaches it.
[01:36:11] It'll first read the Prisma spec,
[01:36:14] the progress tracker, the architecture
[01:36:16] context, and only then will it start
[01:36:18] implementing it.
[01:36:20] It'll first verify we have all the
[01:36:22] necessary packages, and it might even
[01:36:24] consult the Prisma skill. So, the agent
[01:36:27] does a better way implementing the best
[01:36:29] practices. So, let's give it some time,
[01:36:31] and I'll be right back. Now, it's in the
[01:36:33] process of creating the Prisma models
[01:36:36] for the project and the project
[01:36:37] collaborator.
[01:36:39] Then, creating the Prisma singleton, so
[01:36:41] we can actually have the client and run
[01:36:43] it. It's asking us whether we can
[01:36:45] actually run Prisma migrate. So, I'll
[01:36:47] allow it to run it.
[01:36:50] And then, it'll verify everything is
[01:36:51] done, and we'll be able to check it all
[01:36:53] out.
[01:36:54] You can see that we have many files
[01:36:56] changed, but once again, the majority of
[01:36:58] these are coming from the agents that we
[01:37:00] installed or the agent skills. The
[01:37:02] actual generated files that we care
[01:37:04] about are going to be within just a
[01:37:06] couple of files, such as this Prisma
[01:37:08] model right here,
[01:37:10] and this Prisma client. That's it. But
[01:37:13] okay, let's let it do its thing, and the
[01:37:15] feature five is done. Here's what's
[01:37:18] created, just two files that we need to
[01:37:20] take a look at.
[01:37:21] The first one is the project model, and
[01:37:24] the second one is the Prisma client. So,
[01:37:27] let's go ahead and check them out. I'll
[01:37:28] first open up the model that is going to
[01:37:31] be within models, project.prisma, and it
[01:37:34] looks like I'm missing the Prisma syntax
[01:37:37] highlighting. So, I'll head over into
[01:37:39] extensions and install Prisma, which
[01:37:42] would add the syntax highlighting,
[01:37:43] formatting, auto completion, and more.
[01:37:46] There we go. This now looks better. But
[01:37:48] yeah, essentially we have created a new
[01:37:50] model for the project with the ID, owner
[01:37:53] ID, name, description, status, the
[01:37:56] canvas, which is going to be attached to
[01:37:57] a project very soon, and a potential
[01:38:00] list of collaborators. And we also made
[01:38:02] it indexable so we can search for these
[01:38:04] projects.
[01:38:05] Same thing happens with the project
[01:38:07] collaborator. That's going to be a clerk
[01:38:09] ID connected to it. And it's going to
[01:38:12] have access to one or more projects.
[01:38:15] Then, if we take a look at the actual
[01:38:17] Prisma client, that's going to be within
[01:38:20] lib Prisma,
[01:38:22] we're just using the Prisma PG adapter
[01:38:24] to create a new Prisma client and
[01:38:27] connect it to it.
[01:38:29] Then, we export this global Prisma
[01:38:31] instance that we can use to make any
[01:38:33] kind of database calls. We can't really
[01:38:36] test a lot of stuff right here because
[01:38:38] we've just built a database.
[01:38:39] But in the next lesson, we can build a
[01:38:41] couple of API routes that'll bring us
[01:38:43] one step closer to actually making use
[01:38:45] of this data.
[01:38:47] So, for time being, let's just run git
[01:38:49] add dot, git commit {dash} m, implement
[01:38:54] Prisma,
[01:38:55] and then git push.


## Chapter 10: Project CRUD APIs (01:38:58)

[01:38:59] Now that our schema is ready, we're
[01:39:02] ready to build the API routes that sit
[01:39:05] on top of it.
[01:39:06] This is back end only.
[01:39:08] We're not yet wiring the UI. That'll
[01:39:11] come next. But right now, we need to
[01:39:13] focus on one single thing.
[01:39:15] A clean, secure set of routes for
[01:39:18] creating, listing, renaming, and
[01:39:21] deleting projects.
[01:39:23] So, create a new spec right here under
[01:39:26] context feature specs 06
[01:39:30] project APIs.md.
[01:39:33] And within it, we want to tell it that
[01:39:35] the database schema is ready. So, we
[01:39:38] need to build the back end project API
[01:39:41] routes. The routes are as follows: the
[01:39:44] REST endpoints for get API project,
[01:39:46] which is going to list the current
[01:39:48] user's projects, the post for API
[01:39:51] projects, which creates a project, we
[01:39:54] have the patch for renaming, and delete
[01:39:57] for, obviously, deleting.
[01:39:59] We can also give it a couple of rules,
[01:40:02] such as use the authenticated clerk user
[01:40:05] ID as an owner ID.
[01:40:07] And when creating, default missing
[01:40:10] project to untitled project and use the
[01:40:12] schema's existing ID strategy without
[01:40:15] adding sequential IDs. We also want to
[01:40:18] tighten up the security a bit by telling
[01:40:20] it that the unauthenticated requests
[01:40:22] return 401, and only the project owner
[01:40:26] can rename or delete. Non-owners
[01:40:28] mutations return 403. Which means that
[01:40:31] we're making our app secure not only on
[01:40:33] the client side, but the server-side API
[01:40:36] calls are also going to return invalid
[01:40:38] responses if somebody tries to break
[01:40:41] them. And again, we're not yet wiring
[01:40:43] any UI.
[01:40:44] And finally, to verify, we need to check
[01:40:46] whether the routes exist, whether the
[01:40:49] owner's checks are enforced, whether 401
[01:40:52] and 403 responses are handled correctly,
[01:40:54] and that the npm run dev build passes.
[01:40:57] You know the drill. Open up Claude code,
[01:40:59] tell it to read the file, and execute.
[01:41:03] Read this file, update the progress
[01:41:05] tracker, and implement it exactly as
[01:41:07] specified. Let's see how it does.
[01:41:10] The process of actually creating four
[01:41:13] REST API routes would take us some time,
[01:41:16] and you most likely already know how to
[01:41:17] do that. But our agent is just going to
[01:41:19] do it much more quickly for us. And then
[01:41:22] when you take a look at it, you can
[01:41:23] fully understand the structure, and
[01:41:25] you'll be able to add any other
[01:41:26] additional routes very easily, because
[01:41:28] it's mostly boilerplate. So, let's give
[01:41:30] it some time, and I'll be right back.
[01:41:32] There we go. That was quick. Four routes
[01:41:35] have been created, and the build is
[01:41:37] clean.
[01:41:38] All of them are right here within
[01:41:40] project routes or project project ID
[01:41:43] route. So, these are the general ones
[01:41:46] and these are the ones for update and
[01:41:48] delete.
[01:41:49] Let's go ahead and check them out. They
[01:41:51] are right here under app API route.ts
[01:41:56] for general project routes where we have
[01:41:59] a asynchronous get function where we
[01:42:01] first get the user ID from auth
[01:42:03] belonging to clerk.
[01:42:06] We check whether the user ID doesn't
[01:42:07] exist. In that case, we return a 401.
[01:42:10] But, if it does exist, we try to find
[01:42:13] all the projects that match with that
[01:42:15] user and then we return them.
[01:42:17] Similarly, if the user is trying to
[01:42:19] create a post, we get all the data from
[01:42:23] request.json. We take the name and
[01:42:26] finally create it. Then, if we want to
[01:42:28] update or delete them, you can head over
[01:42:30] to the project ID route where we can
[01:42:33] patch it based on the project ID. So, we
[01:42:36] first check whether the user has access.
[01:42:39] If they do, we take a look at the
[01:42:40] context params,
[01:42:42] find the project, parse the data,
[01:42:45] update the project data, and then return
[01:42:47] it.
[01:42:48] And the same thing goes with the delete.
[01:42:50] It's going to be even simpler. We find
[01:42:52] it, we delete it, and we call it a day.
[01:42:55] It's even returning a proper 204 status,
[01:42:58] which means deleted. But now, in the
[01:43:00] same lesson, I want to actually create
[01:43:02] an additional feature spec, which is
[01:43:04] going to be 07
[01:43:06] wireeditorhome.md.
[01:43:10] Where we want to wire the editor home
[01:43:13] sidebar and dialogues to the real
[01:43:16] project APIs we just created.
[01:43:19] So, first, we got to deal with data
[01:43:21] fetching because the editor home page is
[01:43:24] a server component. So, we need to fetch
[01:43:27] owned and shared projects server-side
[01:43:30] using the existing project data helper
[01:43:33] and pass both lists to the sidebar. And
[01:43:35] I don't want to see any client-side
[01:43:37] fetching for the initial load. Now, we
[01:43:39] can do that by using the project
[01:43:42] actions. So, I want to create a new hook
[01:43:45] in the hooks folder that manages dialog
[01:43:48] state and project mutation.
[01:43:51] That's going to look something like
[01:43:52] this.
[01:43:53] Create manage create dialog state,
[01:43:56] manage project name input, generate a
[01:43:59] short unique suffix, slugify the name,
[01:44:02] call the post API projects, and then
[01:44:05] navigate over to the new workspace.
[01:44:07] The project ID and Liveblocks room ID
[01:44:09] should stay aligned, and we can do a
[01:44:12] similar thing for rename and delete. The
[01:44:15] rename simply has to store the target
[01:44:17] project ID plus current name, and then
[01:44:20] patch the name, and delete has to store
[01:44:22] the target project ID, and then patch
[01:44:24] it. Finally, we are ready to wire it all
[01:44:27] together by connecting the hook to the
[01:44:30] sidebar and dialogs. Create dialog will
[01:44:32] show a room ID preview.
[01:44:35] Rename dialog will prefill the current
[01:44:37] name, and delete dialog will show the
[01:44:39] project name. As usual, we want to run
[01:44:42] some checks when we are done, and that
[01:44:43] is to see whether the sidebar uses real
[01:44:46] project data, not the fake dummy data it
[01:44:48] uses right now, whether the create
[01:44:50] actually navigates to the workspace,
[01:44:52] whether the rename updates correctly,
[01:44:55] and whether delete refreshes or
[01:44:57] redirects correctly.
[01:44:58] Finally, the build has to pass. So, this
[01:45:01] is the moment that our sidebar goes from
[01:45:03] mock data to real data.
[01:45:06] So, let's open up our agent,
[01:45:09] tell it to read the file,
[01:45:12] update the progress tracker, and
[01:45:14] implement it exactly as specified. So,
[01:45:16] let's let it do its thing, and once it's
[01:45:19] done, we can test it out in the browser.
[01:45:21] And after some time, we are back. The
[01:45:23] build passes clean, and it created a
[01:45:26] couple of new files. The lib projects is
[01:45:29] used for fetching the own projects and
[01:45:31] shared projects. We can quickly check
[01:45:33] that out right here under lib projects.
[01:45:38] And you can see that this file simply
[01:45:40] exports one function called get projects
[01:45:43] for user, which calls all the projects
[01:45:45] where the owner ID is the user ID that
[01:45:48] is currently signed in, and then it
[01:45:50] returns all the owned and shared
[01:45:52] projects. It also created a hook that
[01:45:54] deals with all the project actions.
[01:45:57] And it modified some additional files
[01:45:59] such as the editor, the projects route,
[01:46:02] and some more types and props updates
[01:46:04] over the sidebar and the dialogues. So,
[01:46:06] don't forget to rerun your application
[01:46:08] by running npm run dev. And then back on
[01:46:11] localhost:3000, we are ready to test it
[01:46:14] out by creating a new project. I'll give
[01:46:17] it a name such as my system design.
[01:46:22] And you can see that it's going to give
[01:46:24] it an additional slug right here, and we
[01:46:26] can click create project.
[01:46:29] It's creating it, and we get redirected
[01:46:31] to editor my system design. So, the
[01:46:34] redirect is actually working, but
[01:46:36] there's no route under that page. But,
[01:46:39] that's to be expected because so far, we
[01:46:41] just wanted to test whether we can wire
[01:46:43] the database functions with the API
[01:46:45] routes. So, if I head back over to the
[01:46:47] editor and then open up the sidebar,
[01:46:49] you'll see that there's a new my system
[01:46:51] design project. And you can also rename
[01:46:55] it to something like Ghost AI system
[01:46:59] architecture, and you can see that it
[01:47:01] updated it in real time. Or, you can
[01:47:03] also just delete it. Let's test it out.
[01:47:06] Yep, that works and it updates in real
[01:47:08] time. So, this means that we have not
[01:47:10] only implemented the dialogues to create
[01:47:13] all of this, but also implemented the
[01:47:16] API routes that handle the
[01:47:17] functionality.
[01:47:19] And if you're wondering why we didn't do
[01:47:20] all of this in a single prompt? Well,
[01:47:23] the API routes touch the back-end layer
[01:47:26] and the UI wiring touches the front-end
[01:47:28] and server components.
[01:47:30] Combining them gives the agent too much
[01:47:32] surface area to make assumptions across.
[01:47:35] Instead, we had two focused prompts,
[01:47:38] which means that we got back two clean
[01:47:40] results without messing up stuff on
[01:47:42] front-end and the back-end. So, before
[01:47:44] we go ahead and review these changes,
[01:47:46] head over to GitHub and merge the
[01:47:48] previous PR, which contained
[01:47:50] implementing Prisma and even more
[01:47:52] importantly adding all of those
[01:47:54] additional files for agent skills. So,
[01:47:57] I'll just go ahead and merge it. So, now
[01:48:00] when we push this over to GitHub, we'll
[01:48:01] be able to review just those changes.
[01:48:04] So, run git add dot,
[01:48:06] git commit {dash} m, wire up Prisma
[01:48:11] UI and REST APIs,
[01:48:14] and run git push. You can head over to
[01:48:16] your repo, open up a new pull request,
[01:48:19] and do it specifically from the
[01:48:20] development branch. This one will be
[01:48:22] fairly quick as there's only 11 files
[01:48:24] changed. So, let's give the Dr. Code
[01:48:27] Rabbit some time to review it. In this
[01:48:29] PR, we've finally introduced the REST
[01:48:32] APIs and CRUD functionalities, making
[01:48:35] our app, well, full stack. We've done
[01:48:37] that across all the different files and
[01:48:39] I always like when Code Rabbit thinks
[01:48:42] the functionality is so detailed that it
[01:48:44] actually gives us a diagram that we can
[01:48:46] review. So, as the user clicks the new
[01:48:49] project, the action that open create
[01:48:51] dialog runs.
[01:48:53] Then we initialize the dialog and
[01:48:55] generate the room ID with a suffix.
[01:48:58] We ask the user to enter the project
[01:49:00] name and submit. After they submit, we
[01:49:03] set the loading and we then make a post
[01:49:05] request to our API projects, which is
[01:49:08] our CRUD REST API route, which then
[01:49:11] calls Prisma project create.
[01:49:13] As soon as the project is created in the
[01:49:15] database, we return the project data,
[01:49:18] set the loading to false, and bring it
[01:49:20] back and then navigate over to the new
[01:49:22] project. It looks like we have one issue
[01:49:25] where we need to import the use project
[01:49:27] actions as a value and not as a type.
[01:49:30] So, return type of requires the hook in
[01:49:32] a value space, but import type is a type
[01:49:35] only import that TypeScript erases from
[01:49:38] the value namespace. So, what we can do
[01:49:40] is just copy this import right here,
[01:49:43] find where we're already importing a
[01:49:45] type, specifically the use project
[01:49:48] actions. That's going to be right here.
[01:49:50] And instead of it, we can just import
[01:49:52] the use project actions without the type
[01:49:55] at the start.
[01:49:57] That way, when it's referred right here,
[01:49:59] we can say type of use project actions,
[01:50:02] which is a function that TypeScript can
[01:50:04] now actually understand. This is a
[01:50:05] pretty nice save. And there's another
[01:50:07] issue in the use project actions where
[01:50:10] we need to handle the failed mutations
[01:50:12] before closing or redirecting. So,
[01:50:15] rename and delete always close the
[01:50:17] dialogue and refresh push even if the
[01:50:20] API calls fail. So, a server or off
[01:50:23] error can look like a success. We need
[01:50:25] to gate those transitions on res.ok and
[01:50:28] keep the dialogue open on failure.
[01:50:30] Thankfully, there's a quick fix right
[01:50:31] here or we can copy just this part,
[01:50:33] which is going to be the submit
[01:50:35] function. So, copy the submit,
[01:50:37] head over into the project actions or
[01:50:41] use project actions.
[01:50:44] And again, the these changes might be
[01:50:46] different for you as they are for me.
[01:50:48] So, if you have some other issues to
[01:50:49] fix, you can definitely do that.
[01:50:52] I'll remove the submit,
[01:50:55] bring in the correct one, push the
[01:50:57] changes by running git add dot, git
[01:50:59] commit {dash} m, implement
[01:51:03] CodeRabbit suggested
[01:51:06] fixes
[01:51:07] and run git push.
[01:51:10] The changes will automatically be
[01:51:12] recognized right here. So, we can go
[01:51:14] ahead and merge it and we are ready to
[01:51:16] continue.


## Chapter 11: Editor: Access Sharing (01:51:18)

[01:51:19] Before we build the canvas, let me
[01:51:21] quickly explain how Liveblocks works.
[01:51:24] Because once you understand it, the
[01:51:26] build order will make complete sense.
[01:51:29] Liveblocks gives every project a shared
[01:51:32] real-time room.
[01:51:33] Think of it like a live session.
[01:51:36] Everyone who opens the same project
[01:51:38] connects to that room over web sockets.
[01:51:41] And any change one person makes
[01:51:43] instantly appears on everyone else's.
[01:51:46] That canvas state, multiple users'
[01:51:48] cursors, the AI drawing nodes, all of it
[01:51:52] lives in that shared room and syncs in
[01:51:54] real time. Liveblocks rooms are open by
[01:51:57] default. So, technically, anyone could
[01:51:59] connect if we let them.
[01:52:01] But since Ghost AI is a project-based
[01:52:04] app where only owners and collaborators
[01:52:06] should have access, we need to control
[01:52:09] who gets in with a sharing mechanism.
[01:52:12] So, before Liveblocks connects a user to
[01:52:14] a room, it has to call authentication
[01:52:16] endpoints first.
[01:52:18] And when we check whether that user
[01:52:20] belongs to a specific project, only if
[01:52:22] they do, we issue a token to let them
[01:52:25] in.
[01:52:26] That token endpoint is what we're
[01:52:28] building in this chapter. And for it to
[01:52:30] work, the access control and the
[01:52:32] collaborator model have to exist. So,
[01:52:34] we're doing it in this order. Workspace
[01:52:37] access first, so each project has a
[01:52:39] secure route only authorized users can
[01:52:42] enter. And then we'll focus on the
[01:52:44] collaborator model second, so the system
[01:52:46] knows exactly who those authorized users
[01:52:49] are.
[01:52:50] Then Liveblocks and then the canvas.
[01:52:53] So, head over into context, feature
[01:52:55] specs, and create a new file called 08
[01:52:59] editor-workspace-shell.md.
[01:53:03] And within it, we'll explain exactly
[01:53:05] what has to happen next. So, let's go
[01:53:07] through it together. The goal of this
[01:53:09] prompt is to build the editor room ID
[01:53:12] workspace.
[01:53:13] Remember, that's that page that we got
[01:53:15] redirected to and we saw a 404. So, if I
[01:53:19] create a new spec right here and we
[01:53:22] navigate over to it, we get a 404. So,
[01:53:25] this is the page we're building. Before
[01:53:27] rendering, the unauthenticated users
[01:53:29] will be redirected to sign in. The users
[01:53:32] without project access will see the
[01:53:34] access denied and non-existent projects
[01:53:37] will also show access denied.
[01:53:40] Then, we need to create that access
[01:53:42] denied component with a centered layout,
[01:53:44] lock icon, short message, and a link
[01:53:47] back to the editor.
[01:53:48] And we can also create some helpers that
[01:53:50] are going to make it simpler for us to
[01:53:52] reuse the access functionality
[01:53:54] such as getting access to Clerk's
[01:53:56] identity and checking whether they can
[01:53:58] access a specific project.
[01:54:01] When it comes to the layout, we want to
[01:54:02] build a full viewport workspace layout
[01:54:05] with a top bar showing the project name,
[01:54:07] navbar actions at the top right, the
[01:54:10] existing projects hyper on the left, the
[01:54:13] current room highlighted in the sidebar,
[01:54:16] central canvas placeholder with a dark
[01:54:18] background and a centered message, and
[01:54:19] the right sidebar placeholder for future
[01:54:21] AI chat. This is exactly how the final
[01:54:24] version of the application looks like.
[01:54:26] We have the left sidebar with the
[01:54:27] currently open project highlighted, the
[01:54:30] top bar with the icons on the right, and
[01:54:32] then we have the AI chat, which is going
[01:54:34] to be coming soon. The canvas area, of
[01:54:36] course, should fill the remaining space.
[01:54:39] And in this case, we want to tell it to
[01:54:41] not add any real canvas logic, live
[01:54:44] blocks, AI chat, or sharing behavior
[01:54:47] yet. That's the keyword right here.
[01:54:50] When it's done, it should perform the
[01:54:51] following checks. So, let's open it up
[01:54:54] within our agent
[01:54:55] and tell it to read the current file,
[01:54:58] update the progress, and execute it
[01:55:01] exactly as specified. Of course, make
[01:55:03] sure that it knows what file you're
[01:55:05] talking about. Let's run it and give it
[01:55:07] some time to process it. And after a
[01:55:10] couple of minutes, it is done. I
[01:55:12] actually took Codex for a spin to see
[01:55:14] how well it can handle it. And yeah, it
[01:55:16] said that it implemented feature eight
[01:55:18] as specified. The guarded workspace
[01:55:20] route now lives under this page, stays
[01:55:23] server-side, and the redirects
[01:55:25] unauthenticated users to sign in. The
[01:55:27] workspace shell component is right here,
[01:55:30] and it includes a project aware top
[01:55:32] navbar with buttons to share. Okay, so
[01:55:35] let's go ahead and test it. Oh, this is
[01:55:38] looking nice. It is a bit different from
[01:55:39] the final design, but I actually love
[01:55:42] it. You can see how the sidebar
[01:55:44] collapses and then the central part
[01:55:46] actually expands. Later on, we can play
[01:55:48] a bit more with the design, but so far,
[01:55:50] I love it. So, right now we are looking
[01:55:52] the details of the new spec project
[01:55:55] because you can see that we're on that
[01:55:56] specific URL. And if you just head over
[01:55:58] to the editor, you'll be able to see
[01:56:00] something like this. You can expand the
[01:56:02] sidebar and then navigate over to the
[01:56:04] details page.
[01:56:06] If the redirect isn't working for
[01:56:07] whatever reason, send a small corrective
[01:56:10] prompt describing exactly what's
[01:56:12] happening, and it'll fix it. Now, let's
[01:56:15] test access control.
[01:56:17] Open up an incognito tab and then head
[01:56:19] over to the same URL. You'll
[01:56:21] automatically be redirected back to sign
[01:56:23] in, which is the first good sign. Go
[01:56:25] ahead and create a new account. I'll try
[01:56:28] to use the email and password this time.
[01:56:31] Let's go with contact js mastery pro and
[01:56:34] a password. And it's good to see that
[01:56:36] Clerk is trying to keep us safe, so it's
[01:56:38] suggesting a stronger password. So, let
[01:56:40] me do that. There we go. And for the
[01:56:44] email, I'll use a secondary email that I
[01:56:47] have because the first one is already
[01:56:49] tied with GitHub. There we go. And we're
[01:56:51] going to even have the email
[01:56:53] verification. So, you're going to get an
[01:56:55] email that looks something like this. Go
[01:56:56] ahead and copy the verification code.
[01:56:59] Then, paste it right here and you'll be
[01:57:01] logged in and redirected to the editor.
[01:57:04] So, if once again, you try to go to that
[01:57:06] same project URL,
[01:57:09] you should hit the access denied screen.
[01:57:11] You don't have access to this workspace.
[01:57:13] Hit back to your editor home to open up
[01:57:15] a project you actually can access.
[01:57:17] That's great. So, now, let's allow this
[01:57:19] user to actually invite that
[01:57:21] collaborator. To do that, I'll head over
[01:57:24] within our context, feature specs, and
[01:57:27] create a new file called 09 share
[01:57:31] dialog.md.
[01:57:33] Let's go through it together. In this
[01:57:34] case, we're basically working on the
[01:57:36] share button.
[01:57:37] It's going to be within the editor
[01:57:39] navbar and it's going to open up the
[01:57:41] share dialog, allowing owners to invite
[01:57:44] collaborators by email, view current
[01:57:47] collaborators, remove collaborators, and
[01:57:49] copy the project link with the temporary
[01:57:52] copy feedback.
[01:57:53] Collaborators can view the collaborator
[01:57:55] list only and not invite, remove, or
[01:57:59] manage access. It's also important that
[01:58:01] we're going to use Clerk data for the
[01:58:03] collaborator sharing system. So, they're
[01:58:05] going to be stored by email in the
[01:58:07] database and we'll use Clerk's backend
[01:58:09] API to enrich the collaborator email
[01:58:12] with display name and avatar image.
[01:58:16] And if a Clerk user is not found for an
[01:58:18] email, then we can fall back to showing
[01:58:20] the email only. We want to add the
[01:58:22] required API logic for listing,
[01:58:24] inviting, and removing collaborators,
[01:58:27] and we want to enforce ownership
[01:58:28] server-side, not client-side, for
[01:58:31] inviting and removing actions. Finally,
[01:58:34] we have a couple of checks to see
[01:58:35] whether everything's been done properly.
[01:58:37] So, once again, let's open up Codex or
[01:58:40] whichever agent you're using and tell it
[01:58:42] to read the 09 share dialog,
[01:58:47] update the progress tracker,
[01:58:49] and implement it exactly as specified.
[01:58:52] We can do it within the same chat
[01:58:55] because this is somewhat related to the
[01:58:56] functionality we just worked on. Let's
[01:58:58] give it some time and I'll be right
[01:59:00] back. And in about 5 minutes, feature
[01:59:02] number nine got implemented exactly
[01:59:05] within the specs scope. The workspace
[01:59:08] navbar share button now opens a new
[01:59:10] dialogue.
[01:59:12] So, what do you say that we actually
[01:59:13] test it out? Back within the browser,
[01:59:15] but not the anonymous one, which doesn't
[01:59:17] have the access. We have to go to the
[01:59:19] one that is the owner of this workspace.
[01:59:22] We can now click this share button,
[01:59:24] which allows us to copy the workspace
[01:59:25] link or invite them via email. And I
[01:59:28] love this share interface. So, I'll
[01:59:30] enter the email of my second account
[01:59:34] and click invite. You can see that the
[01:59:36] user has been invited as the
[01:59:37] collaborator, and since we signed up via
[01:59:40] email, this user doesn't have a profile
[01:59:42] photo. So, now if you head back and
[01:59:44] reload,
[01:59:46] check this out.
[01:59:48] The user now has access. And for this
[01:59:50] user, it's not under my projects, but
[01:59:52] under shared projects. And this user
[01:59:55] doesn't have the permissions to update,
[01:59:57] rename, or delete. Whereas for this
[02:00:00] user, you can see that it's under my
[02:00:01] projects and we have full permissions.
[02:00:04] That's the full collaborator flow
[02:00:06] working end-to-end.
[02:00:08] Owner invites, collaborator receives the
[02:00:10] invites, and nobody else can access it.
[02:00:13] And before we push the changes, let's
[02:00:15] review them with Code Rabbit. This time,
[02:00:17] I'll do it directly within VS Code
[02:00:19] through the Code Rabbit extension. And
[02:00:21] as soon as the comments are in, we can
[02:00:23] go ahead and check them out. Within the
[02:00:25] use project share.ts file, that is the
[02:00:28] hook that the share button borrows the
[02:00:31] functionality from.
[02:00:32] And right here, where we have the copy
[02:00:35] link button, this does nothing else than
[02:00:37] basically copy the URL to clipboard.
[02:00:40] But currently, the copy link doesn't
[02:00:42] handle the clipboard API failures, and
[02:00:44] the timer lacks cleanup. So, if the
[02:00:46] clipboard fails due to permissions or
[02:00:48] something else, the set timeout will
[02:00:51] still fire letting the user know that it
[02:00:53] has been copied, whereas that's not
[02:00:55] really true.
[02:00:56] So, we have to set the error in case
[02:00:58] something goes wrong. We can very easily
[02:01:00] do that. I'll just copy this part right
[02:01:04] here with a try and catch block, and we
[02:01:06] have to replace everything from await
[02:01:09] navigator. So, right here, await
[02:01:11] navigator,
[02:01:12] replace it with this part right here.
[02:01:15] And we have to remove these plus signs
[02:01:17] right here at the start. Okay, great.
[02:01:20] So, this one has been fixed, and I
[02:01:22] believe there's another one right here
[02:01:24] where we have the reload functionality.
[02:01:26] Reload silently swallows errors, which
[02:01:29] may cause stale UI state. If the reload
[02:01:32] function fails due to a network error,
[02:01:34] the error is not captured, and the UI
[02:01:36] may show outdated collaborator data
[02:01:39] after a successful invite or remove,
[02:01:41] which means that here we also have to
[02:01:43] check for errors and display them if
[02:01:45] there are any. So, once again, I'll copy
[02:01:48] this part and replace the old one.
[02:01:51] And don't forget to remove the plus
[02:01:53] signs just to make sure it works.
[02:01:55] Wonderful. So, two comments in this file
[02:01:57] resolved. We have one more in the
[02:01:59] project share dialogue. This is the
[02:02:02] actual dialogue where we have a key
[02:02:04] collision when collaborators share the
[02:02:06] same email or display name. Well, that's
[02:02:09] not really going to happen, right?
[02:02:11] Because each one of the collaborators is
[02:02:12] unique. So, this isn't unlikely, but
[02:02:15] it's impossible. So, yeah, this one is
[02:02:17] good. And finally, there is one more
[02:02:19] under project collaborators where it
[02:02:22] says batch emails in chunks of 500 to
[02:02:25] respect Clerk's API limit. Well, yeah,
[02:02:28] here where we're getting the users, uh
[02:02:30] we definitely don't want to fetch more
[02:02:31] than 500 users. This is great regardless
[02:02:34] of Clerk's limit, but I'm glad that it
[02:02:36] caught it because you never want to
[02:02:38] fetch so many emails at the same time.
[02:02:41] So, in this case, it's not just a copy
[02:02:43] and paste that couple of lines of code.
[02:02:45] What we can do here is use our agent to
[02:02:48] fix it. So, if you click that button,
[02:02:50] it's going to copy a little prompt and
[02:02:53] put it into the chat that's going to
[02:02:54] know exactly which part it has to fix.
[02:02:56] So, let's give it a second to read it
[02:02:58] and fix it. And it's done. The get clerk
[02:03:01] email now batches emails into chunks of
[02:03:03] 500 so that it doesn't go over the
[02:03:05] limit. But, instead of doing that, what
[02:03:08] I actually want to do is never fetch
[02:03:10] more than 500. I mean, that's too much.
[02:03:13] So, I'll tell it
[02:03:14] instead of chunking the emails, maybe we
[02:03:17] just don't have to fetch so many. We can
[02:03:19] just fetch fewer emails. So, let's see
[02:03:21] how it handles a bit more vague
[02:03:23] response. I mean, so far it has been
[02:03:25] implementing everything so perfectly
[02:03:28] because our prompts, or our specs,
[02:03:31] should I say, were so precise. So, it
[02:03:33] never had any issues.
[02:03:35] But, yeah, in this case, it simplified
[02:03:37] it. It's going to call fewer emails.
[02:03:39] Good. So, we're going to keep this. And
[02:03:41] now that all the issues have been fixed,
[02:03:43] we actually fixed these two manually, we
[02:03:45] can just go ahead and push all of these
[02:03:47] changes by opening up our terminal and
[02:03:50] running get add dot get commit {dash} m
[02:03:54] implement share functionality.
[02:03:58] And get push.
[02:04:00] Perfect. Great job.


## Chapter 12: Editor: Liveblocks Canvas (02:04:02)

[02:04:03] Now that the access control is done and
[02:04:06] collaborators and sharing is enabled,
[02:04:10] we are ready to finally build the
[02:04:12] canvas. First, click the link down in
[02:04:14] the description and head over to
[02:04:16] Liveblocks.
[02:04:18] If you haven't already, create a new
[02:04:20] account, create a new project, call it
[02:04:23] Ghost AI, and choose a region that is
[02:04:25] closest to you. And the environment can
[02:04:27] be set to development for now. Once the
[02:04:29] project is created, select personalized
[02:04:32] setup
[02:04:33] and multiplayer. Then, select canvases
[02:04:36] as we want to focus on workflow
[02:04:38] diagrams, whiteboards, design tools, or
[02:04:40] in this case, code architecture. And
[02:04:43] then for the guide, you can select React
[02:04:45] Flow with Next.js. That's exactly what
[02:04:48] we're using. Then, copy the first
[02:04:49] command that you can see right here, and
[02:04:51] paste it within your terminal. You can
[02:04:53] press enter, and here we're installing a
[02:04:55] couple of things.
[02:04:56] The Liveblocks client is the core client
[02:04:59] that manages the WebSocket connection to
[02:05:02] Liveblocks.
[02:05:03] Then, there's the Liveblocks React,
[02:05:05] which contains the React hooks for
[02:05:07] accessing shared room state, presence,
[02:05:10] and storage.
[02:05:11] There's also the Liveblocks React UI,
[02:05:13] containing the pre-built UI components.
[02:05:16] There's also Liveblocks React Flow,
[02:05:19] which is the bridge between Liveblocks
[02:05:21] and React Flow, so canvases are synced
[02:05:24] in real time across all the connected
[02:05:26] users.
[02:05:27] And finally, the XY Flow is the React
[02:05:30] Flow itself, which handles the canvas,
[02:05:32] nodes, edges, and interaction. Once that
[02:05:35] is done, we can initialize the
[02:05:37] Liveblocks config file. So, go ahead and
[02:05:39] copy this command, and paste it into the
[02:05:42] terminal,
[02:05:43] and press enter.
[02:05:45] This will generate a Liveblocks
[02:05:47] config.ts file at the root of our
[02:05:49] directory.
[02:05:50] This is where we define the TypeScript
[02:05:52] types for the shared room, what the
[02:05:54] presence will look like, what user data
[02:05:56] we want to attach to each connected
[02:05:58] session. You can think of it as the
[02:06:00] contract that describes everything
[02:06:02] shared between users in real time.
[02:06:05] And we'll configure it with AI. But
[02:06:07] before we do, let's install Liveblocks
[02:06:10] agent skills. Same pattern as with Clerk
[02:06:13] and Prisma. We want to allow our agent
[02:06:15] to be fluent in how Liveblocks works.
[02:06:19] So, go ahead and copy this command, or
[02:06:21] follow along with me,
[02:06:23] and just run
[02:06:26] npx skills add Liveblocks skills.
[02:06:30] Say Y to update it, and then select
[02:06:33] Liveblocks best practices, and we don't
[02:06:35] need the second part. Press enter.
[02:06:38] Select Claude or whichever agent you're
[02:06:40] using,
[02:06:41] and install it for the project and using
[02:06:43] Simulink.
[02:06:45] Perfect. This was quick. Now, I want to
[02:06:47] split this specific feature
[02:06:49] implementation into three separate spec
[02:06:52] files. So, let's take it step by step,
[02:06:55] and I'll walk you through everything.
[02:06:56] First, let's dive into feature number
[02:06:58] 10, Liveblocks setup. Here, we want to
[02:07:01] tell it to set up the real-time
[02:07:03] collaboration infrastructure using
[02:07:06] Liveblocks. This file will wire up the
[02:07:09] entire collaboration infrastructure. The
[02:07:11] config file will get the presence and
[02:07:13] user metadata types, and then we'll
[02:07:15] create a Liveblocks client. Finally,
[02:07:18] we'll build the off endpoints like API
[02:07:21] Liveblocks off, so we can verify that
[02:07:23] people can actually access the room. So,
[02:07:25] go ahead and open it with either Codex
[02:07:28] or Claude Code. Tell it to read this
[02:07:31] file,
[02:07:32] update the progress,
[02:07:34] and execute everything as specified, and
[02:07:37] press enter. Let's give it some time to
[02:07:39] do all the hard work for us while we
[02:07:42] remain the architect and monitor exactly
[02:07:45] what it is doing. And very soon, feature
[02:07:47] 10 is complete. It implemented just
[02:07:50] three separate files. The Liveblocks
[02:07:52] config, now with types for the presence
[02:07:55] and user metadata, the lib Liveblocks
[02:07:58] file, which allows us to fetch the
[02:08:00] cached Liveblocks node client, so we can
[02:08:03] use its instance, and we also have the
[02:08:06] function that maps out a specific user
[02:08:08] color. Most importantly, we have the
[02:08:10] post endpoint that verifies whether the
[02:08:12] user has been authenticated and whether
[02:08:15] it has access to the project. If it
[02:08:17] does, it returns all the data, and we're
[02:08:20] one step closer to testing it out. But,
[02:08:22] all of these were just some
[02:08:23] functionalities that we need to use
[02:08:25] within our code, but we're not using
[02:08:27] them yet. So, instead of testing at this
[02:08:29] point, what I want to do is head over to
[02:08:32] feature number 11.
[02:08:34] That's going to be the base canvas.md.
[02:08:38] So, right here in lesson 11, we want to
[02:08:41] replace the canvas placeholder with a
[02:08:44] real LiveBlocks backed ReactFlow canvas.
[02:08:48] Allowing multiple users to connect to a
[02:08:51] LiveBlocks room and share the same
[02:08:53] canvas state. That means that the nodes
[02:08:56] and edges will sync in real time. And
[02:08:59] after that, we can basically say that we
[02:09:01] have a full collaborative canvas
[02:09:03] application.
[02:09:04] Not yet polished, but real. We don't
[02:09:08] want to add any controls yet or custom
[02:09:10] nodes or edges. We just want to create
[02:09:12] that canvas.
[02:09:14] So, let's open this up in a new chat. As
[02:09:17] usual, I'll tell it to read the file,
[02:09:21] update the progress,
[02:09:23] and execute as specified. And I've just
[02:09:27] went to grab a coffee, and feature 11 is
[02:09:30] done. So, let's review it. It built out
[02:09:32] the canvas types, so that our
[02:09:34] application remains heavily typed.
[02:09:37] Then, it added the storage part over to
[02:09:40] the LiveBlocks config.
[02:09:41] This matters right here because it knows
[02:09:43] that we're going to be keeping track of
[02:09:45] the presence of the cursors and whether
[02:09:47] they're thinking,
[02:09:48] but also the storage of different nodes
[02:09:50] and edges and users on the screens.
[02:09:52] Later on, we're going to fill up these
[02:09:54] two.
[02:09:55] using LiveBlocks provider and the room
[02:09:57] provider, it created the canvas room.
[02:10:00] And most importantly, the canvas
[02:10:02] placeholder got replaced with that room.
[02:10:05] So, what do you say that we go ahead and
[02:10:07] test it out?
[02:10:08] Back on localhost:3000, we got
[02:10:10] connecting to a room, but there's one
[02:10:13] issue. It says LiveBlocks authentication
[02:10:16] failed, reason not provided. Maybe
[02:10:18] because this project was created before
[02:10:20] our whole LiveBlocks setup. So, what
[02:10:22] I'll do is delete it, reload the page,
[02:10:25] and create a new project.
[02:10:27] I'll call it live blocks live room and
[02:10:31] create. Unfortunately, we still get the
[02:10:34] same issue. Thankfully, the error in the
[02:10:36] terminal gives us a bit more info. It
[02:10:39] looks like we're missing the live blocks
[02:10:40] keys. So, if you head over to your
[02:10:42] project under API keys,
[02:10:44] you'll be able to see your public key
[02:10:46] and the secret key. So, go ahead and
[02:10:48] copy them and add them to your
[02:10:50] .env.local
[02:10:52] where we can first specify the live
[02:10:54] blocks public key as well as the live
[02:10:58] blocks secret key.
[02:11:00] With these two keys in place, head back
[02:11:02] over to your application and reload. And
[02:11:05] after connecting to room, you'll be able
[02:11:07] to see the actual canvas. This is the
[02:11:10] React Flow canvas underneath that you
[02:11:12] can move through. And there's even a
[02:11:14] little window that you'll be able to
[02:11:16] scroll through to very quickly access
[02:11:18] specific parts of the workspace. This is
[02:11:20] looking absolutely amazing. We can even
[02:11:23] expand it by collapsing the left
[02:11:24] sidebar. Oh, and the right sidebar is
[02:11:27] collapsible, too. So, now we have a real
[02:11:30] fully functional React Flow canvas. But,
[02:11:34] of course, what is the canvas for if we
[02:11:36] can't add any elements on top of it? So,
[02:11:38] let's create a little bottom navigation
[02:11:41] that allows us to add some shapes that
[02:11:43] are going to act as specific parts of
[02:11:45] the diagrams within our application.
[02:11:47] We'll do that by creating a new feature
[02:11:50] spec called 12 shape panel.md.
[02:11:55] You can add it right here. This one will
[02:11:56] be simple.
[02:11:58] And what this does is it adds a floating
[02:12:01] toolbar at the bottom of the canvas
[02:12:03] where users can drag shapes onto the
[02:12:06] canvas to create notes. Rectangle,
[02:12:09] diamond shapes, circles, pills,
[02:12:11] cylinders, and hexagons for databases.
[02:12:14] And after this, users will actually be
[02:12:17] able to start creating the architectural
[02:12:20] diagrams. We want to allow the users to
[02:12:22] drag a shape, including the shape name
[02:12:24] and the default size. Then, they can
[02:12:27] also drag and drop it.
[02:12:29] And on drop, we need to read the dragged
[02:12:31] shape payload, convert it to the screen
[02:12:34] position, create a new node at that
[02:12:36] position, use an empty label, and the
[02:12:39] default color. We then want to give each
[02:12:41] one of these shapes a node ID with their
[02:12:44] shape name, timestamp, and a counter.
[02:12:47] And we want to render it.
[02:12:49] So, this is an exciting one. So, let's
[02:12:51] get it built. Read the file, update the
[02:12:54] progress, and execute it exactly as
[02:12:56] specified. I'm sure there's an easier
[02:12:58] way for me to just to read the file and
[02:13:01] not have to repeat this sentence every
[02:13:03] now and then. I mean, I could have put
[02:13:05] it at the top of the file and just share
[02:13:06] the file itself. That would have worked.
[02:13:09] Uh but yeah, I don't mind it. It's the
[02:13:11] actual work that you put before that
[02:13:14] saves you so much time later down the
[02:13:16] line. This one took a bit longer, but
[02:13:18] feature 12 is done. It created the
[02:13:21] canvas node renderer and a floating pill
[02:13:23] toolbar at the bottom with six draggable
[02:13:26] shapes. So, if you head back over to
[02:13:28] your room,
[02:13:30] take a look at the bottom.
[02:13:31] You have the rectangle, which you can
[02:13:33] drag and drop. Hopefully, nope. As I
[02:13:37] dropped it, it didn't appear on the
[02:13:39] screen.
[02:13:40] Let's try with a second one.
[02:13:42] It looks like I can drag and drop them,
[02:13:44] but they're not actually showing up on
[02:13:46] the screen, which makes it a great
[02:13:47] opportunity to debug it the proper way
[02:13:50] by specifying in detail the current
[02:13:52] issue that we're experiencing. So, I
[02:13:55] took a second to write all of the issues
[02:13:57] that I believe we currently have with
[02:13:59] the application. At least that I have on
[02:14:01] my version of the app. Your agent might
[02:14:04] have done something different. So, let's
[02:14:05] go through everything together first,
[02:14:07] and then you'll be able to tell your
[02:14:09] agent to fix some issues that you see on
[02:14:11] your end as well. Let's think of this as
[02:14:13] a little corrective prompt.
[02:14:15] So, review the editor canvas
[02:14:16] implementation and fix the visual
[02:14:18] issues. The canvas currently looks like
[02:14:21] it's floating above the background
[02:14:23] inside a border box. Instead of feeling
[02:14:25] like a real design canvas. And I want to
[02:14:28] teach you how we can also add images to
[02:14:29] the context. So, right here within the
[02:14:32] context, you can create a new folder
[02:14:34] called screenshots.
[02:14:36] And then you can screenshot the entire
[02:14:37] design and simply drag and drop it in.
[02:14:42] Of course, I'll rename it to image as I
[02:14:44] specified right here within the
[02:14:46] document. That way you can also give
[02:14:48] your agent some visual feedback.
[02:14:51] Also, read the current canvas component
[02:14:53] code in the components editor. And here
[02:14:55] are a couple of issues to look for.
[02:14:57] Obviously and first of all, the drag and
[02:15:00] drop issues, right? The canvas nodes
[02:15:02] from the node panel cannot be dragged
[02:15:05] and dropped onto the canvas. We need to
[02:15:06] investigate the full drag and drop
[02:15:09] pipeline. We need to confirm that the
[02:15:11] draggable nodes in the node panel have
[02:15:13] the correct draggable attribute, that
[02:15:15] the canvas has the on drag over handler
[02:15:19] and on drop allowing us to drop them.
[02:15:21] That the drop handler reads the node
[02:15:23] type from data transfer, calculates the
[02:15:26] coordinates, and then actually creates a
[02:15:28] new node at the drop position.
[02:15:30] And while we're fixing the drag and drop
[02:15:32] issues, I also thought we can fix some
[02:15:34] visual inconsistencies such as the way
[02:15:37] that the canvas and the left and the
[02:15:39] right sidebar are positioned. So, the
[02:15:41] left and the right sidebar should float
[02:15:42] over the canvas, not push or shrink it.
[02:15:45] Sidebars must use the fixed position or
[02:15:48] absolute with a higher Z index and so
[02:15:50] on. So, after documenting all issues, we
[02:15:53] want to fix all of the above so that it
[02:15:55] basically corrects what we specified.
[02:15:58] So, let's actually open this up right
[02:16:00] here. We can tell it to read this file
[02:16:03] and fix all of the listed issues and
[02:16:06] then run it.
[02:16:08] So, we've done three things. First, we
[02:16:11] gave Claude code some file references up
[02:16:14] front and the screenshots right here.
[02:16:16] This stops it from wandering around the
[02:16:18] entire project trying to figure out
[02:16:20] where things live.
[02:16:21] We're pointing it exactly where to look.
[02:16:23] We're listing every issue one by one and
[02:16:26] mixing some technical hints alongside
[02:16:28] them.
[02:16:29] These technical details act as
[02:16:31] shortcuts. They give the AI the stronger
[02:16:34] starting point so it can find and fix
[02:16:36] the root cause faster instead of
[02:16:38] guessing. And third, at the bottom, we
[02:16:40] describe exactly what success looks
[02:16:42] like. The AI now knows not just what's
[02:16:45] broken, but what done looks like. So,
[02:16:48] let's see if we can manage to correct
[02:16:50] itself and fix it. Quickly after reading
[02:16:52] through some of these files, it has a
[02:16:54] full picture of all the issues, so it's
[02:16:57] going to use the to-do right to track
[02:16:59] the fixes and then implement them. Fix
[02:17:02] the canvas layout was the first thing,
[02:17:04] removing the card styling and making it
[02:17:06] a fill full viewport, fixing the left
[02:17:09] sidebar not fully hiding when closed,
[02:17:11] fixing the dotted canvas background
[02:17:13] visibility, and finally and most
[02:17:14] importantly, verifying the drag-and-drop
[02:17:17] pipeline. And see how well we did. Uh
[02:17:20] it's even thanking us,
[02:17:21] uh specifying that the core issue is
[02:17:23] clear from the screenshot of the code.
[02:17:26] The canvas is boxed inside a padded main
[02:17:29] with card styling and the layout shrinks
[02:17:32] the canvas to accommodate sidebars
[02:17:34] instead of floating over them. So, it's
[02:17:36] going to fix it very easily.
[02:17:38] Perfect. Hopefully, this video is
[02:17:40] teaching you how you can approach
[02:17:42] developing apps with AI. You are the
[02:17:45] architect and agent is just a coder. And
[02:17:49] there we go. All four files have been
[02:17:51] updated, so let's test it out.
[02:17:54] Back into the browser, I will reload.
[02:17:57] You can see that now the canvas spans
[02:17:59] across left and right and the left and
[02:18:02] right sidebar appear to be floating on
[02:18:04] top of it. So, if you want to hide it,
[02:18:06] it just gets completely hidden away,
[02:18:08] which is great. And the right sidebar
[02:18:11] also gets completely hidden away, so we
[02:18:14] have a complete canvas. This is a big
[02:18:16] difference from what we had before,
[02:18:18] because now if you hide the sidebars,
[02:18:20] you have so much more space to work
[02:18:22] with. And what happens if we try to drag
[02:18:24] and drop an element?
[02:18:26] It looks like that functionality is
[02:18:28] still not working properly. And I think
[02:18:30] that's because Claude focused mostly on
[02:18:32] cosmetic changes and the layout. I don't
[02:18:35] see too many mentions of the drag and
[02:18:38] drop functionality being fixed. So, what
[02:18:40] we can do now is head over into the
[02:18:42] current issues and specify that we want
[02:18:45] to fix the drag and drop functionality.
[02:18:50] So, we're going to remove everything
[02:18:52] else besides the drag and drop and keep
[02:18:55] the last part saying nodes can be
[02:18:57] dragged from the node panel and dropped
[02:18:59] onto the canvas as correctly. So, now we
[02:19:01] can say read the current issues file
[02:19:04] again and fix the remaining issue and
[02:19:07] press enter.
[02:19:09] This time, it's all about the drag and
[02:19:11] drop. And after some thinking, it looks
[02:19:14] like it found the root cause. The React
[02:19:17] Flow viewport has pointer events none,
[02:19:20] and React Flow internally uses D3 zoom
[02:19:23] or native pointer listeners that call
[02:19:25] prevent default on pointer down. So,
[02:19:27] when the shape panel is rendered inside
[02:19:30] of the React Flow as a panel, those
[02:19:32] pointer handlers interfere with the
[02:19:34] browser's drag gesture recognition
[02:19:36] before Dragster can fire. The standard
[02:19:39] React Flow drag and drop pattern puts
[02:19:41] drag sources outside of the React Flow
[02:19:44] and puts on drop or on drag over on a
[02:19:46] wrapper div, not on the React Flow
[02:19:48] component. So, it's going to fix this
[02:19:50] issue for both the canvas editor and the
[02:19:52] shape panel. That's it. Note that there
[02:19:55] is the fix is clean. We specified what
[02:19:57] was wrong, and the fix was to move the
[02:20:00] on drag over and on drop from the React
[02:20:03] Flow component to the outer wrapper. And
[02:20:05] also to replace the panel position from
[02:20:07] bottom center, which is React internal
[02:20:09] panel, with a plain absolutely
[02:20:11] positioned div.
[02:20:12] So, let's test it out. Back on localhost
[02:20:15] 3000 within a specific project, I'll
[02:20:17] drag and drop this rectangle, and it
[02:20:20] still doesn't do it. So, what I'm
[02:20:22] thinking is maybe we can make use of
[02:20:25] that Liveblocks agent skills that we
[02:20:27] installed earlier.
[02:20:28] I mean, this is the exact situation
[02:20:30] they're built for. So, in the same
[02:20:31] context window, let's simply tell the
[02:20:34] agent to check the Liveblocks best
[02:20:37] practices and fix the drag and drop
[02:20:39] flow. Dragging shapes from the shape
[02:20:41] panel should create new nodes on the
[02:20:43] canvas. But, it's still not working.
[02:20:46] Nodes should be draggable from the panel
[02:20:49] and dropped onto the canvas correctly.
[02:20:51] So, by telling it to check the
[02:20:52] Liveblocks best practices, I'm hoping
[02:20:54] that it's going to consult the
[02:20:56] Liveblocks agent skill. So, let's give
[02:20:58] it a shot, and you can see that that is
[02:20:59] the first thing that it did. Liveblocks
[02:21:01] best practices. After analyzing it, it
[02:21:04] came back with the complete picture with
[02:21:06] three things that are wrong.
[02:21:08] The storage type declares top-level
[02:21:10] nodes and edges, but use Liveblocks flow
[02:21:13] actually stores everything under a
[02:21:15] nested flow key. Within the canvas room,
[02:21:17] the initial storage creates top-level
[02:21:19] nodes and edges, once again, wrong
[02:21:21] schema. And then the canvas editor add
[02:21:23] node mutation calls storage. get nodes,
[02:21:27] which writes to the wrong storage path.
[02:21:30] Instead, it should use on nodes change
[02:21:32] with a type of add and then the item
[02:21:34] we're adding.
[02:21:35] So, let's wait until it fixes all three,
[02:21:38] and it says clean. So, let's actually
[02:21:40] test it out. Back within the browser,
[02:21:42] I'll reload the page, and I'll try drag
[02:21:45] and dropping a node once again.
[02:21:47] And you can see that this time we
[02:21:49] actually get a a
[02:21:50] Now, if you try drag and dropping
[02:21:52] another shape, you'll see that it'll
[02:21:54] just give you another rectangle. And yet
[02:21:56] another rectangle of a different size.
[02:21:59] You're only getting rectangles, and
[02:22:01] that's okay for now. Because in the next
[02:22:04] lessons, we're going to turn these
[02:22:05] rectangles into different shapes. We'll
[02:22:08] basically make it like a real
[02:22:09] architecture canvas where you can
[02:22:11] connect different nodes and give them
[02:22:13] titles and make them make sense. But
[02:22:16] thankfully, we fixed this shape drag and
[02:22:18] dropping feature, which is one of the
[02:22:19] bigger features in the app. And while
[02:22:21] fixing it, I wanted to keep the full
[02:22:23] process of me doing that. So, you're not
[02:22:25] just watching me copy and paste from the
[02:22:27] other screen.
[02:22:28] We're actually debugging this together.
[02:22:31] And in this case, the solution was to
[02:22:33] invoke an agent skill. So, whenever
[02:22:35] you're working with specific tools,
[02:22:37] always verify that they also have their
[02:22:39] agent skills, install them, and ask your
[02:22:42] agent to use them.
[02:22:44] Okay, great. So, let's actually get
[02:22:46] these changes pushed by saying get add
[02:22:48] dot, get commit {dash} m,
[02:22:50] implement drag and drop canvas
[02:22:54] functionality,
[02:22:55] and then run get push. And I'll actually
[02:22:57] open up a PR for this and get it merged
[02:23:00] so that in the next lesson, we can focus
[02:23:02] on adding more canvas features. For
[02:23:05] these, we already reviewed most of the
[02:23:07] changes before.
[02:23:08] So, I won't be reviewing them again. And
[02:23:11] we have to resolve the conflicts right
[02:23:13] here within our current issues. And
[02:23:15] there's a fix with Copilot thing right
[02:23:16] here, resolve the merge conflicts in
[02:23:18] this pull request by clearing the
[02:23:22] current issues.md file.
[02:23:25] We basically want to make it empty as we
[02:23:27] said. We don't need to push whatever is
[02:23:29] in the current issues file. This is also
[02:23:31] a new feature by GitHub where the
[02:23:33] Copilot can automatically fix it on our
[02:23:35] behalf.
[02:23:37] And once it does, we'll be able to merge
[02:23:39] it back to the main branch and continue
[02:23:41] developing. And there we go. It
[02:23:42] basically cleared out the file, and
[02:23:44] we're good to merge it. So now, back
[02:23:46] within the editor, you can just run git
[02:23:48] pull to pull the latest changes and
[02:23:50] we're ready to continue with the next
[02:23:52] feature.


## Chapter 13: Editor: Canvas Features (02:23:54)

[02:23:55] In this lesson, the goal is to make the
[02:23:57] canvas feel like a real product. So,
[02:24:01] open up your feature specs and go ahead
[02:24:04] and create another one that's going to
[02:24:06] be 13 node shape.md.
[02:24:09] In this lesson, we're going to actually
[02:24:11] polish and add six features. Each one
[02:24:14] will have a distinct layer of
[02:24:16] interaction. So, that by the end, the
[02:24:18] canvas will have proper shape rendering,
[02:24:21] node colors, edge behavior, and keyboard
[02:24:23] shortcuts. Everything that makes a
[02:24:25] difference between a working prototype
[02:24:27] and something that genuinely feels
[02:24:29] polished to use. So, starting with the
[02:24:32] first one, it's going to be the node
[02:24:34] shape. It's a fairly simple one where we
[02:24:36] just want to replace the placeholder
[02:24:38] node renderer with proper shape
[02:24:40] rendering and a drag preview.
[02:24:43] So, instead of a placeholder node shape,
[02:24:45] which is just a rectangle, we want to
[02:24:47] render all of these different types of
[02:24:48] shapes through SVGs.
[02:24:51] They should scale with the node size and
[02:24:53] we want to keep the border subtle. We
[02:24:54] also want to add a shape drag preview
[02:24:57] while we're dragging.
[02:24:59] We want to keep the node rendering
[02:25:00] connected to the existing collaborative
[02:25:02] canvas state.
[02:25:03] We don't want to rebuild anything.
[02:25:06] And when we're done, we want to check
[02:25:08] that the node renderer renders the
[02:25:10] correct shape variant for each type.
[02:25:13] So, you know the drill. Open up your
[02:25:15] agent and let's ask it to read this
[02:25:18] file, update the progress, and implement
[02:25:20] it as specified. Let's give it some time
[02:25:23] and I'll be right back. And a couple of
[02:25:25] minutes after, feature 13 is done. It
[02:25:28] replaced the single style placeholder
[02:25:30] with a shape aware rendering and also
[02:25:33] added the cursor tracking ghost preview.
[02:25:35] I'll show you what that means quickly.
[02:25:38] But, basically now, you can see that our
[02:25:40] array of rectangles that we created
[02:25:42] before is now a bunch of different
[02:25:45] shapes. And we can actually move across
[02:25:47] the canvas and drag and drop different
[02:25:49] shapes. There's a mini map at the bottom
[02:25:50] as well, which we can later on remove as
[02:25:53] we don't need it as we'll be mostly
[02:25:54] working within a single centralized
[02:25:56] place. But yeah, we now have the shapes
[02:25:59] and you can actually connect the shapes
[02:26:01] together. But we still can't change the
[02:26:03] size of the nodes, right?
[02:26:05] They are always of the same size and we
[02:26:07] can't edit their labels. Like currently
[02:26:09] these are just shapes. They don't have
[02:26:11] any data associated with them.
[02:26:14] So what we can do is create another file
[02:26:17] right here, another feature
[02:26:19] 14 node editing.md.
[02:26:23] And within it, we essentially want to
[02:26:25] add resizing and inline label editing to
[02:26:28] the canvas. So that when we select a
[02:26:30] specific node, we can resize it and
[02:26:32] scale them however we need to. And if we
[02:26:34] double click it, we'll be able to edit
[02:26:37] its label. So this is the next feature
[02:26:39] that we're going to develop. I'll tell
[02:26:40] it to read the file, update the
[02:26:43] progress,
[02:26:45] and implement it exactly as specified.
[02:26:49] And you know what? I will actually copy
[02:26:51] this part right here. So in the future I
[02:26:53] can just paste it into the prompt.
[02:26:56] Okay, and after some wearing and
[02:26:59] cogitating and thinking, let's see what
[02:27:02] it'll actually come up with. And as it's
[02:27:04] close to being done after running a
[02:27:06] couple of minutes, um near the end, uh
[02:27:09] when it tries to build and check for
[02:27:11] errors, it almost always finds some type
[02:27:15] issues. Like right here, it was
[02:27:17] complaining about the canvas node. So it
[02:27:20] expanded the types and made it a bit
[02:27:22] more type safe. And only once that is
[02:27:24] done, it actually updates the progress
[02:27:26] tracker and then finishes with the
[02:27:28] feature. So it's always great to ask it
[02:27:30] to test the application and test the
[02:27:32] output.
[02:27:33] Okay, great. So the The
[02:27:35] from XY flow now renders when a node is
[02:27:38] selected and we can resize dimension
[02:27:40] changes through live boxes on node
[02:27:42] change automatically. Also,
[02:27:44] double-clicking any node opens up a text
[02:27:47] area.
[02:27:48] So, let's go ahead and test it out. We
[02:27:50] now have these labels, which is perfect.
[02:27:53] But first, let's test the resizing. If I
[02:27:56] now pull it at any of the borders
[02:27:59] or even at any of the edges, you can see
[02:28:02] that this is very precise and would take
[02:28:05] us some time to implement properly. You
[02:28:06] can now resize it both horizontally and
[02:28:09] vertically or if you want to keep the
[02:28:11] aspect ratio, you can resize it by the
[02:28:13] edges. This is absolutely amazing.
[02:28:17] And let's also test changing the label
[02:28:19] by double-clicking right here and typing
[02:28:21] something like start
[02:28:23] of the app
[02:28:25] and leaving it and you can see that it
[02:28:27] looks good. It quickly brings the text
[02:28:29] up in case you want to type more stuff
[02:28:31] into it.
[02:28:32] But
[02:28:33] but we can fix that later on because the
[02:28:35] text will mostly always stay centered.
[02:28:38] So, if we pull some kind of a label, we
[02:28:40] can now mark this as a post grass DB,
[02:28:43] for example, and it's going to fall down
[02:28:46] right here and we can now connect the
[02:28:48] application that way. Perfect. Let's
[02:28:50] just quickly tell it that even though
[02:28:52] while we're typing into the field, we
[02:28:54] want the text to stay in the middle.
[02:28:56] Right now, it jumps to the start. So,
[02:28:59] I'll take a quick screenshot while I am
[02:29:01] typing
[02:29:03] and drag and drop it into the chat and
[02:29:05] tell it while the label editing is
[02:29:07] focused, the text appears at the top of
[02:29:10] the element instead of in the middle
[02:29:12] where it falls back to when not focused
[02:29:15] any longer.
[02:29:16] Make it so that when we're typing, we're
[02:29:18] also typing within the middle of the
[02:29:20] element. Hopefully, this should be clear
[02:29:22] enough for a little quick corrective fix
[02:29:25] and very quickly, the build passes. It
[02:29:27] just swapped the text area for the
[02:29:29] content editable div. So, now if we head
[02:29:32] back right here and start typing, you
[02:29:34] can see that it remains in the middle
[02:29:36] and you can say start, here we can say
[02:29:40] label and as soon as we start typing, it
[02:29:43] basically centers itself right in the
[02:29:46] middle.
[02:29:47] Wonderful. So, now that we can actually
[02:29:49] type within these inputs, what do you
[02:29:51] say that we implement the functionality
[02:29:53] to also be able to differentiate them by
[02:29:56] color? So, create a new feature spec
[02:29:58] called 15 nodes color toolbar.md
[02:30:03] and here we want to add a floating color
[02:30:05] toolbar that appears when a node is
[02:30:08] selected. We then want to allow the user
[02:30:10] to pick a color and both the node
[02:30:13] background and text color will update
[02:30:15] instantly synced across all
[02:30:17] collaborators in real-time. So, it'll
[02:30:20] check our UI context for the node color
[02:30:22] palette, include a background color as
[02:30:25] well as a matching text color so that
[02:30:27] the contrast is nice
[02:30:28] and we want to reuse existing colors if
[02:30:31] they exist in globals, otherwise it can
[02:30:33] keep the palette in the canvas types.
[02:30:35] Then we want to add a toolbar
[02:30:38] above the selected node that'll only
[02:30:40] show when the node is selected.
[02:30:43] And when a color is selected, we want to
[02:30:45] update the node background color and
[02:30:47] text color. I think this is pretty
[02:30:49] understandable.
[02:30:51] So, let's actually build it by telling
[02:30:53] it our usual secret sentence which is
[02:30:56] super simple, but again, the spec file
[02:30:58] does the heavy lifting. This one for
[02:31:00] some reason was super quick. It added
[02:31:03] the text color, and the ability to
[02:31:05] choose between a predefined set of
[02:31:07] colors and also the color background.
[02:31:10] So, if we head back over here and select
[02:31:12] an element, would you look at that? I
[02:31:14] mean, this is really starting to come
[02:31:15] into life and I'm not sure how much time
[02:31:18] this would take me to manually code it
[02:31:20] out. But this way, we just have to think
[02:31:23] of an idea, write a fairly simple yet
[02:31:26] descriptive uh spec file, and then it
[02:31:29] does it instantly. And
[02:31:32] take a look.
[02:31:33] You can actually select the colors of
[02:31:35] each one of the nodes
[02:31:38] separately.
[02:31:39] So, if I make this one purple, the
[02:31:41] database, for example, can be green.
[02:31:44] Uh yep, for example, this one can be
[02:31:46] MongoDB in its classic green color.
[02:31:49] Then, we can have some kind of an
[02:31:50] algorithm right here going on, which can
[02:31:53] be orange. And yeah, it is all working
[02:31:56] wonderfully. So, on top of the colors,
[02:31:59] what else is there to implement?
[02:32:00] Currently, there's these custom edges
[02:32:02] from all four sides. But no matter which
[02:32:05] you select, it's always going to start
[02:32:06] making a connection from the bottom, as
[02:32:08] you can see right here.
[02:32:09] And it'll connect it to the bottom or
[02:32:11] the top as well. So, we want to fix that
[02:32:13] edge behavior.
[02:32:15] So, I'll create a new spec just for
[02:32:17] that, and you can see how I'm being very
[02:32:19] specific with the specs, only focusing
[02:32:22] on the smallest thing possible. So, 16
[02:32:26] edge behavior
[02:32:28] .md. And the goal of this spec is to
[02:32:31] just replace the default canvas edges
[02:32:33] with custom edges that feel easier to
[02:32:36] follow, easier to click, and support
[02:32:39] inline labels. So, we want to add
[02:32:41] connection handles to every node at the
[02:32:43] top, right, bottom, and left sides, and
[02:32:45] user should be able to connect from any
[02:32:47] handle to any other handle. Oh, and
[02:32:50] another thing you can notice is that
[02:32:52] we're opening up a new chat for every
[02:32:55] single one of these specs. This helps us
[02:32:57] with lowering the overall context window
[02:33:00] and the amount of tokens that we're
[02:33:02] spending for each transaction, and it
[02:33:04] also makes the agent that much more
[02:33:06] focused on the task at hand. And all
[02:33:09] these little things together, like the
[02:33:11] separate feature spec.md files instead
[02:33:13] of just regular messages,
[02:33:15] or the current issues file, where we can
[02:33:17] specify what's wrong, and these six
[02:33:20] files that altogether make the system
[02:33:22] work, just makes it a breeze to work
[02:33:24] with an AI, which is typically not the
[02:33:26] case because it starts imagining things
[02:33:29] and creating stuff that we don't want or
[02:33:30] breaking other things. But this way, it
[02:33:33] is super predictable. And if you take a
[02:33:35] look at the progress tracker, which we
[02:33:38] haven't looked at in a long time now,
[02:33:40] you'll see that everything we've done so
[02:33:42] far is written right here. But what I
[02:33:45] care more about is that it even kept
[02:33:48] some additional architectural decision
[02:33:50] so that it knows what we're doing. And
[02:33:52] the session notes for specifically what
[02:33:54] it thought is very important. Like the
[02:33:56] specific versions of different tools
[02:33:58] that we're using, the fact that the
[02:33:59] Prisma config uses Prisma forward slash
[02:34:02] and not some other path, and that it
[02:34:04] reads the database URL from the .env.
[02:34:07] It kept everything it needs and
[02:34:09] everything that future sessions with AI
[02:34:11] or other developers continuing to
[02:34:13] develop this project need to do it in a
[02:34:16] sane and happy way. And another build
[02:34:19] passes.
[02:34:20] It implemented the canvas edge data
[02:34:22] pieces, allowing us to connect the
[02:34:24] source and the end.
[02:34:27] So if you head back over here, you would
[02:34:29] see that we have plenty of different
[02:34:30] lines happening. But now, if you select
[02:34:32] it from the left side, you can see how
[02:34:34] it creates a bit of a different kind of
[02:34:36] connection, and you can now connect it
[02:34:38] to another element. This line looks a
[02:34:40] bit different from other more
[02:34:42] organic-looking lines. Oh, and right
[02:34:44] now, we cannot even delete the elements.
[02:34:46] So we have plenty of elements on the
[02:34:48] screen.
[02:34:49] But I'll create a new one right here and
[02:34:51] another database on the right.
[02:34:54] Drag [snorts] the canvas so we can see
[02:34:56] them right here. Now the mini map starts
[02:34:58] making a bit more sense, as you can see.
[02:35:00] But if you try to connect it, you can
[02:35:02] now do that in a bit of a more
[02:35:04] consistent and better way.
[02:35:06] Now that the canvas is looking so good,
[02:35:08] I guess we can focus on little
[02:35:10] quality-of-life fixes.
[02:35:12] Like under feature specs, we're going to
[02:35:14] do 17 canvas ergonomics.md.
[02:35:18] And within it we can focus on adding a
[02:35:20] little floating control bar for zooming
[02:35:23] in and out and undoing or redoing and
[02:35:26] then wiring those actions to keyboard as
[02:35:28] well. So if you press plus or equal it's
[02:35:30] going to zoom in minus to zoom out
[02:35:33] command or control Z or Y to undo and
[02:35:36] redo and I also don't like that mini map
[02:35:39] at the bottom right. I don't think our
[02:35:41] app will need it. So simply say remove
[02:35:44] the mini map at the bottom right.
[02:35:47] It's just a personal preference. But
[02:35:49] yeah, this is that finishing layer that
[02:35:51] makes the canvas feel like a tool that
[02:35:53] somebody would actually use every day.
[02:35:54] So let's implement this one as well and
[02:35:57] very quickly feature 17 is done as well.
[02:36:00] We now have a new pill shaped floating
[02:36:02] bar at the bottom left for zooming in
[02:36:05] and out or fitting within the view. So
[02:36:07] if we collapse the sidebars, you'll be
[02:36:09] able to see it right here at the bottom.
[02:36:11] Ooh, it it actually looks very nice and
[02:36:14] if I move some things around, you can
[02:36:16] see that the left arrow or the undo
[02:36:19] actually starts shining and you can undo
[02:36:22] previous actions or redo them. You can
[02:36:25] also use command or control Z or Y to
[02:36:28] actually go back and forth, which is
[02:36:30] absolutely amazing. There's this fit in
[02:36:32] view, which is going to fit all the
[02:36:34] elements within the view. So if you're
[02:36:36] working on something that is a bit
[02:36:37] closer together, it's going to actually
[02:36:39] increase the view, which is always nice.
[02:36:41] And you can zoom in or you can zoom out,
[02:36:43] but that's hidden by the next JS logo,
[02:36:46] but that's only in development.
[02:36:48] So these little things really do make a
[02:36:50] big difference. And finally, I had an
[02:36:52] idea that isn't even necessary, but I
[02:36:55] want to make it work.
[02:36:57] So let's create a new feature spec 18
[02:37:00] starter template.md.
[02:37:03] The goal of this one is to create a
[02:37:05] template library that lets users start
[02:37:08] from a pre-built diagram instead of
[02:37:11] blank canvases. So we can start with
[02:37:13] some ideas, like let's say microservices
[02:37:17] or a CICD pipeline or an event-driven
[02:37:19] system. Each one will load directly into
[02:37:22] the shared canvas. That's going to make
[02:37:24] it easier for users to figure out how to
[02:37:26] actually use the app and what are the
[02:37:28] different use cases. Because maybe
[02:37:30] somebody's not going to even get the
[02:37:31] idea of what they can use this app for.
[02:37:34] So, the templates should give them a
[02:37:35] pretty good idea. This one took a bit
[02:37:37] longer, but feature 18 is done. We now
[02:37:40] have the starter templates file.
[02:37:43] So, if you head over here and collapse
[02:37:46] everything, maybe we should start with a
[02:37:48] blank canvas, but we can keep doing it
[02:37:51] within our mess right here. Uh at the
[02:37:53] top right, there's the templates button.
[02:37:56] And if you click it, you'll see a couple
[02:37:58] of different starter templates, which
[02:38:00] aren't looking that good right now. They
[02:38:02] look a bit too vertical, but yeah, as
[02:38:05] soon as you click import, it'll actually
[02:38:07] import a lot of stuff pre-labeled. Uh
[02:38:10] but it may be better to do that within a
[02:38:12] new project, so we can see it a bit
[02:38:13] better. So, I'll call it CICD
[02:38:16] and create a new project.
[02:38:19] And then we'll start from a template by
[02:38:21] going with maybe the CICD pipeline or
[02:38:24] let's go with microservices.
[02:38:27] And you can take a look that that
[02:38:29] immediately tells you a bit about how we
[02:38:31] can start structuring the application
[02:38:33] infrastructure. But yeah, this right now
[02:38:35] is looking a bit too vertical. The
[02:38:38] design is not actually being displayed.
[02:38:40] So, we want to take this screenshot and
[02:38:42] we want to feed it into the chat by
[02:38:44] holding the shift key and then drag and
[02:38:46] dropping. And then we want to compare
[02:38:47] that with how it looks like on the
[02:38:49] finished product.
[02:38:50] Where we can clearly see the full
[02:38:53] template before we drag and drop it. So,
[02:38:55] I'll also put that here.
[02:38:57] And I'll say
[02:38:59] I'll pass in the screenshot of how the
[02:39:02] templates look right now. They look a
[02:39:04] bit too vertical and the actual elements
[02:39:07] are not clearly visible. Whereas, on
[02:39:10] another screenshot, which is the
[02:39:11] finished product, you can see how each
[02:39:13] card gets its own space, and they show
[02:39:16] the entire diagram or the entire
[02:39:18] template that's going to be entered in
[02:39:20] once clicked. Make it look more similar
[02:39:22] to that. So, once again, this is a
[02:39:24] little corrective prompt with two
[02:39:26] different screenshots, one before and
[02:39:28] one after. Let's see how well it does.
[02:39:31] So, currently, it looks like this. So,
[02:39:33] I'm going to snap my fingers, and we
[02:39:35] come down to something that looks like
[02:39:37] this.
[02:39:38] Definitely not good.
[02:39:40] Even though now it's a bit better, as
[02:39:42] it's showing the full template that's
[02:39:43] going to be inserted in, but I'm not
[02:39:46] quite sure why it cannot get the widths
[02:39:49] right. So, we could be a bit more
[02:39:50] specific and tell it to increase the
[02:39:52] width of the whole import template card,
[02:39:54] and then to increase the width of the
[02:39:56] cards within it, so that they are the
[02:39:58] same as this.
[02:40:00] And that's what I'll tell it for the
[02:40:01] second time
[02:40:03] by saying, "Increase the width of the
[02:40:05] entire import template overlay, and then
[02:40:08] increase the width of the card within it
[02:40:10] as well, so it looks the same as on the
[02:40:12] final screenshot." And I'm purposefully
[02:40:15] being not as descriptive right here as
[02:40:17] we are within our spec files, because I
[02:40:19] want to show you how
[02:40:21] it can cost you a lot by not being
[02:40:23] specific from the start. A lot of
[02:40:25] back-and-forth messages, conversations,
[02:40:27] and corrective fixes. And very soon, the
[02:40:30] fix is in, and now it actually looks
[02:40:32] amazing. It increased the width, and
[02:40:34] it's much clearer what it's actually
[02:40:36] going to insert in. So, that means that
[02:40:37] we now also officially have the
[02:40:40] templates. So, we implemented a lot of
[02:40:43] stuff across these five separate feature
[02:40:45] specs, 18 files changed in total, which
[02:40:48] means a lot of stuff to review. This
[02:40:49] actually deserves its own pull request.
[02:40:51] So, let's go ahead and push the changes
[02:40:53] either via terminal or via the source
[02:40:55] control right here. It's going to
[02:40:57] auto-craft a nice message, such as
[02:40:59] improve node shape, added resizing and
[02:41:01] inline labels, and adding color
[02:41:04] toolbars.
[02:41:05] Then, once you commit and sync, back on
[02:41:08] GitHub, you'll see that the development
[02:41:09] branch had recent pushes 7 seconds ago.
[02:41:13] So, let's just open up a new pull
[02:41:15] request, and let's wait Code Rabbit to
[02:41:17] provide us with a review. I think this
[02:41:19] walkthrough will be particularly useful,
[02:41:21] as we've covered many different
[02:41:22] features.
[02:41:24] So, this PR implements a comprehensive
[02:41:26] canvas editing feature set, including
[02:41:28] custom edge rendering with inline
[02:41:30] labels, node resizing with color
[02:41:33] toolbars, keyboard shortcuts for zooming
[02:41:35] and undoing and redoing, a canvas
[02:41:37] control bar, and a starter template
[02:41:40] system with a modal dialogue and
[02:41:42] SVG-based previews. We've made changes
[02:41:45] across 19 different files, and here is
[02:41:48] the sequence diagram. The user clicks
[02:41:50] the templates button. It opens the
[02:41:52] editor navbar, and then we open up the
[02:41:54] templates. We display the templates with
[02:41:57] card previews. The user imports them,
[02:42:00] and then once they do, we pass the
[02:42:02] pending template prop. Then, we forward
[02:42:05] that pending template to the canvas
[02:42:07] editor. Live Blocks clears the existing
[02:42:09] nodes or edges, adds the templates,
[02:42:12] syncs this new graph to the canvas,
[02:42:14] triggers the fit view automatically, and
[02:42:17] then once it's imported, we bring it
[02:42:19] back to the user.
[02:42:20] This is a nice diagram on the starter
[02:42:22] templates feature. This was a complex
[02:42:24] PR, so I'm assuming there's going to be
[02:42:27] a lot of different things we can fix.
[02:42:29] The first one points out to exposing an
[02:42:31] accessible name on these icon-only
[02:42:34] buttons.
[02:42:35] Because title is not a dependable
[02:42:37] accessible label. It's telling us to add
[02:42:40] the area label title for the zoom, fit,
[02:42:43] undo, redo buttons for people who are
[02:42:46] using some assistive technologies. So,
[02:42:47] if I head back over here and hover over
[02:42:50] them, it will tell me that this is an
[02:42:52] undo. But, for people with screen
[02:42:54] readers, this is not going to do it, and
[02:42:56] they will have no idea what these
[02:42:58] buttons are all about. I mean, it's rare
[02:43:01] that these types of people would be
[02:43:02] using this kind of an application
[02:43:04] anyway, but it's always great to
[02:43:06] implement anything you're doing with
[02:43:08] best practices in mind. So, in this
[02:43:09] case, CodeRabbit provided me with a
[02:43:11] prompt for AI agents to use, so we can
[02:43:14] add those area labels. After that,
[02:43:15] there's a major potential issue on
[02:43:17] avoiding double committing the edge
[02:43:20] label on enter or escape. So, when
[02:43:22] pressing enter or escape, it'll call the
[02:43:25] commit edit immediately, then the
[02:43:27] input's on blur handler will call it
[02:43:29] again when the element loses focus. This
[02:43:31] sends two mutations through live blocks,
[02:43:33] creating duplicate undo retries for a
[02:43:36] single edit. That's interesting. So, the
[02:43:38] fix is simply to call the prevent
[02:43:40] default and prevent blur instead of
[02:43:43] commit edit. So, let's find that. I'll
[02:43:45] find where this commit edit is getting
[02:43:47] called.
[02:43:48] It is right here in canvas edge
[02:43:50] component. Specifically, we're looking
[02:43:52] at it on the enter key or the escape
[02:43:55] key. So, right here, and instead of
[02:43:58] that, we want to apply those two lines,
[02:44:01] prevent blur and
[02:44:03] prevent default.
[02:44:05] And we also want to remove the commit
[02:44:07] edit from the dependency array. After
[02:44:09] that, there's a minor issue to move ref
[02:44:12] updates into a sync effect to comply
[02:44:14] with React 19 ref values. So, basically,
[02:44:17] it's telling us to put it within a use
[02:44:19] effect. That's super simple. Let's just
[02:44:21] find where in the code this is.
[02:44:23] And after that, you can see that even
[02:44:25] it's complaining right here about the
[02:44:26] code, but we didn't take a look at it
[02:44:28] because we weren't looking at the actual
[02:44:30] code.
[02:44:31] It's always good to use the best
[02:44:33] practices. So, we just need a use effect
[02:44:36] right here below that's going to put all
[02:44:38] of these node refs into edges and nodes
[02:44:41] like this.
[02:44:42] And everybody's happy. After that, we're
[02:44:45] missing the enter key for handling the
[02:44:46] label commit. So, if it says save the
[02:44:49] label on blur, enter, or escape, but on
[02:44:53] handle key down, we only add escape. So,
[02:44:55] right here, we also have to add the
[02:44:58] enter key. I think we searched for this
[02:45:00] across the code base just before. That
[02:45:02] was right here in the canvas edge.
[02:45:05] But, not this instance, the instance
[02:45:07] where we just had the escape. So, I'll
[02:45:09] search for escape.
[02:45:11] And it's right here. We have to replace
[02:45:13] it with if key is escape or if is key is
[02:45:16] enter. And once again, for you, these
[02:45:19] suggestions might be completely
[02:45:20] different from mine. And that's normal
[02:45:22] because agentic development is not
[02:45:24] predictable. So, for me, it's adding
[02:45:26] some accessibility names or guarding
[02:45:28] some colors. For you, it's going to be
[02:45:30] something else. But, I always love
[02:45:32] learning about everything that Code
[02:45:34] Rabbit throws at me because the next
[02:45:35] time, I can immediately do it better. Or
[02:45:37] in this case, we can make our feature
[02:45:39] specs more specific so that our agents
[02:45:42] don't make these mistakes in the first
[02:45:44] place. Oh, and this one is interesting.
[02:45:46] When trying to undo or redo, it's
[02:45:48] currently looking only at a lower letter
[02:45:50] Z, but in case somebody has caps lock
[02:45:52] turned on, we also want it to take a
[02:45:54] look at the upper case Z.
[02:45:56] This is interesting. So, let's go ahead
[02:45:58] and push those Code Rabbit suggested
[02:46:00] fixes.
[02:46:02] All of them were within the canvas.
[02:46:06] And then, once they're up, we can simply
[02:46:09] go ahead and merge this PR.
[02:46:12] Amazing job on adding all of these
[02:46:14] little improvements that make our canvas
[02:46:17] that much more interactive.


## Chapter 14: Avatar Feature, Chat Sidebar UI & Auto Save (02:46:19)

[02:46:21] In this chapter, we'll add the
[02:46:23] collaborators avatar. So, when somebody
[02:46:25] else is moving something on the screen,
[02:46:27] you can see who is messing with you.
[02:46:29] We'll also complete the chat sidebar UI
[02:46:32] and implement a canvas auto save, which
[02:46:35] will save our canvas data to a Vercel
[02:46:37] blob. So, when you create something, you
[02:46:40] don't lose it. And I'll break down all
[02:46:42] of these within three separate feature
[02:46:45] spec files. Each one is independent, but
[02:46:47] together they complete the collaborative
[02:46:50] experience before AI generation enters
[02:46:53] the picture. So, back within our
[02:46:54] application, create a new 19 presence
[02:46:59] avatars cursors.md
[02:47:02] chat. The goal of this spec is to
[02:47:04] implement presence avatars and cursors.
[02:47:08] Because right now, multiple users can
[02:47:10] edit the same canvas, but they can't see
[02:47:13] each other.
[02:47:14] And after this, every connected
[02:47:16] collaborator will appear as a live
[02:47:19] cursor directly on the canvas with their
[02:47:22] name and color. So, we want to render
[02:47:25] those collaborator avatars and add those
[02:47:27] cursors to the canvas. And also, on the
[02:47:30] top right, we can show a stacked group
[02:47:33] of avatars where we can see everyone in
[02:47:35] the room at one place. So, you know the
[02:47:38] drill. Let's get it implemented. And the
[02:47:40] presence feature has now been
[02:47:42] implemented. There's a new component
[02:47:44] rendered inside of the canvas wrapper
[02:47:46] called the presence cursor as well as
[02:47:49] the collaborators avatars. So, if you
[02:47:51] head back over to a specific project, we
[02:47:53] can stay within the CICD, open up this
[02:47:56] project within a second tab. And check
[02:47:58] this out. Right here on top, you should
[02:48:00] see that Adrian is also within this
[02:48:02] canvas. But in this case, both of us are
[02:48:04] Adrians. So, you can see another
[02:48:06] person's cursor. And if I put these tabs
[02:48:09] side by side, take a look at this.
[02:48:12] Using LiveBlocks, while one user is
[02:48:15] doing something, all the other users in
[02:48:17] the room can see exactly what they're
[02:48:19] doing. So, this is a great first step
[02:48:22] toward interactivity, but we can do
[02:48:24] more.
[02:48:25] Head over and create a new feature spec,
[02:48:28] or just get it from the zip, called 20
[02:48:30] AI sidebar.md.
[02:48:34] The goal of this one is to create a
[02:48:37] sidebar placeholder that'll later on get
[02:48:39] replaced with a proper UI.
[02:48:42] Two tabs, the AI architect and the
[02:48:45] specs. The AI architect tab will have a
[02:48:48] scrollable chat area, starter prompt
[02:48:50] chips, message bubbles, and a composer
[02:48:53] input. While the specs tab will have a
[02:48:56] generate button and a placeholder spec
[02:48:58] card.
[02:49:00] No back-end logic yet, just the UI that
[02:49:02] everything else will connect to.
[02:49:04] So, let's run it and let's see how it
[02:49:07] does. And after a couple of minutes, it
[02:49:09] is done. In this case, it touched only
[02:49:12] the AI sidebar, which is a new
[02:49:14] standalone component, as well as the
[02:49:16] editor workspace client, where it
[02:49:18] replaced the old aside with this new AI
[02:49:21] sidebar. So, now we got a new sidebar
[02:49:24] that looks something like this. You can
[02:49:26] see it on the right side. There's the AI
[02:49:29] architect, which soon enough will allow
[02:49:31] you to design full workflows and systems
[02:49:34] within the canvas, which looks like a
[02:49:36] chat because you're speaking with an
[02:49:38] agent. And then there's a specs tab,
[02:49:41] which allows you to generate a specific
[02:49:43] specification and then later on download
[02:49:45] it. This is just the UI for now, but
[02:49:47] soon enough this will become real. You
[02:49:49] can also type multiple messages by
[02:49:51] pressing shift and then enter, which is
[02:49:54] useful for those longer prompt. Oh, and
[02:49:56] before we run the next spec, which is
[02:49:58] all about auto-saving what we're
[02:50:00] currently working on,
[02:50:01] we need to set up Vercel blob storage.
[02:50:04] Vercel blob is basically an object
[02:50:06] storage service. Think of it like a
[02:50:09] cloud drive for your app. So, instead of
[02:50:11] storing large files directly in your
[02:50:13] database, you upload them to the blob
[02:50:16] and store only the URL reference in
[02:50:18] Prisma.
[02:50:19] We're using it for two different things
[02:50:21] in Ghost AI.
[02:50:22] Canvas snapshots as saved JSON and
[02:50:25] generated specs that will be available
[02:50:27] for download later on through markdown.
[02:50:30] It's completely free to get started
[02:50:32] with. You can just head over to
[02:50:33] vercel.com. Then on the left side, click
[02:50:36] storage and create a new database.
[02:50:38] Choose blob for store name, enter
[02:50:41] something like ghost AI, and we'll set
[02:50:43] it to private because private storage
[02:50:45] means that your blob URLs require a
[02:50:48] token to access.
[02:50:49] Without this, anyone who gets a hold of
[02:50:52] your blob URL can read the file
[02:50:53] directly, which means the canvas data
[02:50:56] and generated specs would be publicly
[02:50:58] readable. But private storage keeps
[02:51:00] everything scoped to your application
[02:51:02] only.
[02:51:04] So, create it. And once it is created,
[02:51:07] click on it, and then right here you'll
[02:51:09] be able to find your .env.local, where
[02:51:11] you can just copy the snippet. Then
[02:51:13] within your .env.local,
[02:51:15] you can simply add this new .env, blob
[02:51:18] read write token, and we are ready to
[02:51:21] execute our next feature spec
[02:51:23] by adding a file called
[02:51:25] 21_canvas_autosave.md.
[02:51:30] Before we add that AI generation, canvas
[02:51:33] state needs to persist.
[02:51:35] So, after this, every change to the
[02:51:37] canvas is automatically saved to Vercel
[02:51:39] blob, which we just set up. And then
[02:51:41] we'll save the blob URL, store it in
[02:51:43] Prisma, and our canvas data will be
[02:51:46] saved securely. So, this spec is all
[02:51:48] about saving the current canvas state.
[02:51:51] It should be pretty simple for our agent
[02:51:53] to implement, given that we gave it all
[02:51:55] the information about the Vercel blob
[02:51:57] and about the environment variable that
[02:51:59] it can use to save data. And after a
[02:52:01] couple of minutes, it is done. A Vercel
[02:52:04] blob is installed, and blob read write
[02:52:07] token is already present in the
[02:52:09] .env.local.
[02:52:10] But if we get back to the editor, at
[02:52:12] least on my end, there seems to be a
[02:52:14] bug. So, let me show you how I would
[02:52:16] approach fixing it. To fix this issue,
[02:52:19] you can just copy it, head back over to
[02:52:21] our application,
[02:52:23] specifically into the current issues.md,
[02:52:27] and specify that this is the current
[02:52:31] error that I'm seeing on the screen. And
[02:52:35] you can paste it right here. It's going
[02:52:36] to give it all the necessary
[02:52:37] information, and you can say
[02:52:40] fix it.
[02:52:42] So, make sure that it has access to the
[02:52:44] current issues, and say
[02:52:46] fix it. Or you could have just pasted
[02:52:48] that into the chat itself.
[02:52:50] For just a singular issue like this, it
[02:52:52] should be totally okay. And as it's
[02:52:54] working through it, I can already see
[02:52:55] what was the issue. Even though we ran
[02:52:57] MPX Prisma generate and migrate, the
[02:53:00] generated client is correct, but there's
[02:53:03] a stale .next cache bundling the old
[02:53:06] schema. So, it's going to clear the old
[02:53:08] cache and then delete it, which forces
[02:53:10] Turbopack to recompile from a freshly
[02:53:13] generated Prisma client, which already
[02:53:15] has the canvas blob URL. Then, we just
[02:53:17] have to restart our server, and the
[02:53:19] error will be gone. So, open up your
[02:53:21] terminal and just to rerun it by saying
[02:53:23] npm run dev. And then back on
[02:53:25] localhost:3000, if you reload, the error
[02:53:28] will be gone. So, now we are ready to
[02:53:30] test that final feature we implemented.
[02:53:33] Head over to one of the active projects,
[02:53:35] add a couple of nodes right here,
[02:53:37] refresh the page, and make sure it
[02:53:39] remains at the exact space where you
[02:53:40] left it at.
[02:53:41] So, I'll try to change its name and move
[02:53:44] it below the auth service, and just make
[02:53:46] sure that it actually remains there,
[02:53:47] which would mean that the auto save is
[02:53:49] working.
[02:53:51] Perfect. But even though it saved it, it
[02:53:53] wasn't saved through a blob, because if
[02:53:55] you head over to the Ghost AI blob
[02:53:57] storage, you'll see that there is
[02:53:59] absolutely nothing there. So, let's fix
[02:54:01] this issue and uh couple others.
[02:54:04] I went through the application, tested
[02:54:06] it deeply, and came up with a couple of
[02:54:08] different issues that I added in the
[02:54:10] current issues.md file. You should
[02:54:13] already have a file like this in your
[02:54:15] zip, which you can just refer to. But
[02:54:17] again, it's possible that for you,
[02:54:19] you'll have to go through the app
[02:54:20] yourself, try to find some specific
[02:54:22] issues within your app, and then write
[02:54:24] the prompt to fix them.
[02:54:26] But yeah, in this case, let's go over
[02:54:28] the most important one, which is the
[02:54:30] saving button in the workspace navbar.
[02:54:33] Uh the workspace navbar is missing a
[02:54:35] save button. The auto save hook exists,
[02:54:38] but we need to wire the button to it. It
[02:54:41] should default to save. While saving, it
[02:54:43] should switch over to saving. After
[02:54:45] successful save, it should switch over
[02:54:47] to save. And that's it. The most
[02:54:50] important thing that I noticed right
[02:54:51] here is in this canvas route.ts
[02:54:55] file. If you take a look at the blob
[02:54:58] storage, the access is set to public.
[02:55:01] And remember what I said before, it has
[02:55:03] to be set to private because we don't
[02:55:05] want other people to be able to view the
[02:55:07] changes we make within the canvas. So,
[02:55:09] we need to set it to private. And we're
[02:55:11] not asking it to change anything else
[02:55:13] for now. For now, I just want to focus
[02:55:15] on issue one and then later on go
[02:55:17] through all of the other issues. So,
[02:55:19] yeah, let's ask it to fix the save
[02:55:21] button first. I'll open up a new chat
[02:55:24] and tell it to read the current issue.md
[02:55:27] file, check the issue one and fix it.
[02:55:29] After fixing it, mark it as pending to
[02:55:31] test. Let's run it and see how well it
[02:55:34] does. And very quickly, issue one is
[02:55:36] fully implemented and marked as pending
[02:55:39] for tests. So, let's go ahead and test
[02:55:41] it out. You can see the save button
[02:55:43] right here. And as you move something on
[02:55:45] the screen and change its color and
[02:55:47] click save, you can see that the saving
[02:55:50] indicator is not really changing. So,
[02:55:52] you can quickly head over to the code
[02:55:53] base, see there's no errors in the
[02:55:55] terminal, but it's still not doing its
[02:55:57] thing. So, let's send it one quick
[02:55:59] corrective prompt by telling it that
[02:56:02] issue one still hasn't been fully fixed.
[02:56:05] The saving status indicator is not being
[02:56:07] changed, and when I click the save
[02:56:09] button, nothing is changing either.
[02:56:11] Analyze the issue further and fix it.
[02:56:14] And we can send it out. And it was doing
[02:56:16] a bit of thinking, but it came back with
[02:56:18] the response that the root cause was
[02:56:20] React strict mode, Enabled by default in
[02:56:23] next js app router. It double invokes
[02:56:26] effects in development. So on initial
[02:56:28] mount, the cleanup is intentionally
[02:56:30] fired by the strict mode before remount,
[02:56:33] and then remount effect only registers
[02:56:35] the cleanup again, but it never resets.
[02:56:38] So that means that the is mounted is
[02:56:40] permanently set to false in development.
[02:56:42] So the save exited every time. This fix
[02:56:45] removes the is mounted ref entirely. Uh
[02:56:48] because react 18 made this guard
[02:56:50] unnecessary. Perfect. So if we head back
[02:56:52] right here and reload, and if you move
[02:56:55] something around, and then press save at
[02:56:58] the top right,
[02:57:00] you can see that it says saving, and
[02:57:02] then we get an error. Save failed.
[02:57:05] If I move it again a couple of times and
[02:57:07] click save again,
[02:57:08] it says save failed.
[02:57:11] It's funny because when I tested it
[02:57:12] initially, it actually said saving and
[02:57:15] then saved. So back in the blob storage,
[02:57:18] you can see that I have this new canvas,
[02:57:20] and it actually stored the JSON data.
[02:57:22] But then when I tried doing it again, it
[02:57:25] failed. So if you open up the terminal,
[02:57:27] you'll see that we have an error with
[02:57:29] the vercel blob saying that the blob
[02:57:31] already exists, so we should add allow
[02:57:34] override is set to true if we want to
[02:57:37] override it. So what we can do is simply
[02:57:39] find this file. That's the canvas root.
[02:57:42] So you can go over to canvas root, and
[02:57:46] just add an additional prop of allow
[02:57:49] override is set to true. This single
[02:57:51] line should immediately allow us to save
[02:57:55] every other time,
[02:57:57] not just the first time. You can see it
[02:58:00] says saved, and back when I did the
[02:58:01] blob, you can see that it got modified
[02:58:04] less than a minute ago, which means that
[02:58:06] it is consistently saving data. And
[02:58:08] right now the size of this JSON file is
[02:58:11] 6.11 kilobytes, but if we head back and
[02:58:13] add a couple more labels and models and
[02:58:17] shapes and some pieces of text within
[02:58:19] them and then save again and then head
[02:58:22] to the blob. You can see that now the
[02:58:24] size increased, which means that it is
[02:58:26] properly saving all the data. So, now
[02:58:29] that our issue one has been fixed right
[02:58:31] here,
[02:58:32] uh we can ask it to continue fixing the
[02:58:34] other issues.
[02:58:35] Uh specifically, some issues that are
[02:58:37] found are about deleting nodes and
[02:58:40] edges. Uh so, right now we don't have a
[02:58:43] way to delete anything. So, if I try
[02:58:46] pressing backspace or the delete keys or
[02:58:48] anything, I can't do it. So, the
[02:58:51] solution is simple. We just need to add
[02:58:53] a key down event listener to the canvas
[02:58:56] that listens for the delete and
[02:58:57] backspace keys, doesn't fire when the
[02:59:00] event target is an input or text area,
[02:59:02] but just gets fired when we're selecting
[02:59:05] specific nodes, and then it deletes
[02:59:07] them.
[02:59:08] As the third issue, uh currently, we can
[02:59:10] also just connect from top to the top of
[02:59:15] the handle. You can see, even if I drag
[02:59:17] from the right handle, it connects from
[02:59:19] top to top. We want to be able to drag
[02:59:22] and drop from any side of the element to
[02:59:25] any other side. That will allow us to
[02:59:27] make these graphics so much more
[02:59:29] customizable.
[02:59:30] So, we just want to allow it to be
[02:59:32] connected from top, right, bottom, and
[02:59:35] left.
[02:59:36] Then, as the fourth issue, I noticed
[02:59:38] that when I drag and drop specific
[02:59:40] elements, they drop a bit lower than
[02:59:43] where they're supposed to. So, I just
[02:59:45] wanted to fix that offset.
[02:59:48] And notice when I dragged and dropped
[02:59:50] it, it actually said saving at the
[02:59:52] bottom left right here and then saved,
[02:59:54] which means that the auto save
[02:59:55] functionality is working. And then, the
[02:59:58] fifth issue is the auto zoom on first
[03:00:01] node. We want to read the Liveblocks
[03:00:03] agent skills before implementing it, and
[03:00:05] then as soon as we drop it, we want to
[03:00:06] zoom it in. And for six and seven, we
[03:00:09] want to check the clerk skills, um and
[03:00:11] we have some issues with the
[03:00:12] collaborator avatar images. If the image
[03:00:15] is coming from Clerk, we want to add it
[03:00:17] to next config, so it gets properly
[03:00:19] shown. And also, currently, we have two
[03:00:23] different Clerk buttons. We just want to
[03:00:25] keep the one and remove the other one.
[03:00:27] So, let's ask it to fix the errors from
[03:00:30] two all the way to seven. Okay, now that
[03:00:33] the issue one in the current issues.md
[03:00:36] file has been fixed, uh analyze and fix
[03:00:39] issues from two to seven. Press enter.
[03:00:43] And let's see how well it does. Okay, it
[03:00:45] looks like all the remaining issues have
[03:00:48] been implemented, and uh it marked them
[03:00:51] for pending test, uh which is a good
[03:00:53] thing for us to test right now. We have
[03:00:55] to test deleting the nodes and edges,
[03:00:58] um handling uh the positions or the
[03:01:01] lines in between the elements, drop
[03:01:04] position offset, auto zooming, and then
[03:01:06] Clerk images.
[03:01:08] So, if I head back right here and reload
[03:01:11] the page, let's first test the drag and
[03:01:13] drop. So, if I try to drag and drop it
[03:01:15] here, you can see that it gets placed at
[03:01:17] the exact position. This is pretty
[03:01:19] crazy.
[03:01:21] Take a look at once again. I'll try to
[03:01:22] place it right here,
[03:01:24] and it worked. Of course, it's going to
[03:01:26] depend on the zoom position. I think if
[03:01:28] we're at a normal regular zoom, and you
[03:01:30] once again drag and drop it to a
[03:01:32] specific position, that's exactly where
[03:01:34] it places it. So, that has been fixed.
[03:01:37] Also, now there's just one Clerk icon
[03:01:39] right here, where you can see your
[03:01:40] account.
[03:01:42] Uh what else did we fix? The edges
[03:01:45] connections. So, for example, let's try
[03:01:47] to drag and drop the bottom of this edge
[03:01:49] right here to the left side of the test
[03:01:52] suite, and take a look at how well it
[03:01:55] connects. It even places the arrow from
[03:01:57] here to here. Or maybe when I go into
[03:01:59] the package, that works as well, and the
[03:02:02] arrows move. This makes our application
[03:02:04] so much more usable, because now, for
[03:02:06] example, we can connect the auth service
[03:02:09] horizontally with the database
[03:02:12] and then take the database output and do
[03:02:14] something with it.
[03:02:16] Again, this canvas is becoming a mess
[03:02:18] right now because there's so much stuff
[03:02:20] happening. So, it would make sense to
[03:02:22] test out the delete. Select a couple of
[03:02:24] elements and try to press the backspace
[03:02:27] or the delete key and see whether it's
[03:02:30] going to remove them. Because for me, it
[03:02:33] doesn't. So, it looks like that's the
[03:02:35] last issue that's still pending. So,
[03:02:37] let's just tell it that issue two
[03:02:40] remains unfixed. When I select an
[03:02:42] element and press the backspace or the
[03:02:44] delete key, the element is still there
[03:02:47] and isn't being deleted from the canvas.
[03:02:49] Analyze it and fix it. So, let's see if
[03:02:52] we can just narrow it down to one issue,
[03:02:54] whether it can finish that last one. And
[03:02:57] again, this just shows you that whenever
[03:02:58] you give it more stuff to fix,
[03:03:01] it's easy for some of these to fall
[03:03:04] through because it maybe didn't analyze
[03:03:06] them as deeply in isolation.
[03:03:09] So, you can see why these feature specs
[03:03:11] worked so well so far because they were
[03:03:14] super detailed and well-documented. But
[03:03:17] as soon as you go deeper into the
[03:03:18] conversation, the agent can easily get
[03:03:20] lost.
[03:03:22] So, this is its last chance. Let's see
[03:03:24] how well it does.
[03:03:27] It looks like it was able to find a root
[03:03:29] cause in about 30 seconds. In apply no
[03:03:32] changes inside of the live blocks react
[03:03:35] flow source, we had a case of remove
[03:03:38] which was not doing anything.
[03:03:40] So, it was silently ignoring the remove
[03:03:43] type changes, whereas live blocks
[03:03:46] exposes a dedicated on delete function
[03:03:49] that correctly deletes from the live
[03:03:51] map. So, it fixed it and let's see how
[03:03:54] well it does right now.
[03:03:55] I'll reload the page and then I'll
[03:03:58] select a couple of elements and press
[03:04:00] the backspace key and now it deletes
[03:04:02] them properly. Now, if you don't want to
[03:04:04] delete them one by one, you can also
[03:04:06] hold the shift key, and then drag and
[03:04:09] drop over multiple, and remove them that
[03:04:11] way.
[03:04:12] Also, another thing that I didn't tell
[03:04:13] you so far is that you can also add uh
[03:04:16] text to the lines connecting different
[03:04:19] elements. Like, we want to build and
[03:04:23] then
[03:04:24] run
[03:04:25] the test suite. So, this way kind of it
[03:04:28] makes more sense with the connection.
[03:04:30] But, you can also use the text on the
[03:04:31] lines for significantly more detailed
[03:04:34] instructions when it comes to connecting
[03:04:36] different elements. But, yeah, now that
[03:04:38] all of these issues are fixed, we can go
[03:04:40] ahead and push them. So, say get add
[03:04:43] dot, get commit {dash} m, and this
[03:04:45] lesson was all about canvas interaction.
[03:04:48] So, say implement improved canvas
[03:04:51] interaction.
[03:04:53] And then run get push. Now, in the next
[03:04:55] lesson, we'll focus on the AI
[03:04:58] collaborative side of the application.


## Chapter 15: Trigger.dev Setup (03:05:01)

[03:05:02] And now that we have the full canvas
[03:05:05] right here, where we can drag and drop
[03:05:07] elements, move things around, and create
[03:05:10] our own architectural systems,
[03:05:13] we're ready to help our users a bit by
[03:05:16] implementing the AI workspace, where we
[03:05:19] can allow our users to collaborate with
[03:05:22] our AI agent within the application,
[03:05:25] that I'll teach you how to implement
[03:05:26] right now.
[03:05:28] But, I want you to think about it a bit.
[03:05:30] Like, before we start building the AI
[03:05:32] generation features,
[03:05:34] um you need to understand why these
[03:05:36] can't run inside a normal API route.
[03:05:40] See, when a user sends a prompt to Ghost
[03:05:42] AI, something like this, to design an
[03:05:45] e-commerce back end, the agent doesn't
[03:05:48] just make one call. It analyzes the
[03:05:50] request, runs multiple AI steps,
[03:05:53] generates nodes and edges, and syncs
[03:05:56] everything back to the canvas all
[03:05:58] keeping the user updated. And that can
[03:06:00] easily take 30 to 60 seconds, maybe even
[03:06:04] a couple of minutes. And I mean, you've
[03:06:05] already seen this pattern. When you
[03:06:07] generate an image with ChatGPT or
[03:06:09] Gemini, it doesn't happen instantly. The
[03:06:12] work runs in the background, and you
[03:06:14] keep receiving the updates until the
[03:06:16] response is ready. And the API routes
[03:06:18] within our application are not designed
[03:06:20] for that. They have execution limits,
[03:06:23] which means that long-running requests
[03:06:24] can time out. And even if they didn't,
[03:06:27] keeping a request open for that long
[03:06:29] isn't how production systems are built.
[03:06:31] That's what I'll teach you how to
[03:06:33] implement Trigger.dev to solve this
[03:06:35] problem.
[03:06:36] In the final version of the application,
[03:06:38] if you give it a detailed prompt and
[03:06:40] send it, you'll be able to see direct
[03:06:43] updates as it is working on the thing.
[03:06:46] It'll first start with analyzing your
[03:06:48] architecture request, and all of these
[03:06:51] functions will run as durable background
[03:06:54] tasks outside of the request life cycle,
[03:06:57] which means that the work is running in
[03:06:59] the background, and you'll be updated on
[03:07:02] the process. So, the work of the API
[03:07:04] route is to just trigger the task and
[03:07:06] then return, while the heavy work
[03:07:08] continues in the background. And that's
[03:07:10] why both the AI design generation and
[03:07:13] the spec generation in Ghost AI run
[03:07:16] through Trigger.dev instead of directly
[03:07:18] in API routes. And even before we used
[03:07:20] Trigger on Ghost AI, I was already using
[03:07:24] it within jsmastey.com platform, where
[03:07:27] every time that users go through
[03:07:28] different lessons, check out the
[03:07:30] overviews, contents, or transcripts, we
[03:07:32] can perform some actions on the back end
[03:07:35] without slowing down or freezing what
[03:07:37] the user can see on the front end, which
[03:07:39] is super helpful for quizzes or sharing
[03:07:41] the status of the AI interviewer that we
[03:07:44] worked on. So, yeah, let me show you how
[03:07:46] we can set up Trigger.dev in your
[03:07:48] project.
[03:07:49] First, click the link down in the
[03:07:51] description to be able to follow along
[03:07:53] and see exactly what I'm seeing.
[03:07:55] And then create a new account. Once
[03:07:58] you're in, you should be able to see
[03:07:59] your dashboard that looks something like
[03:08:01] this.
[03:08:02] So, go ahead and create a new project.
[03:08:04] I'll call it Ghost AI.
[03:08:08] We are working on an AI agent, and under
[03:08:11] technologies, I thought that Gemini
[03:08:13] works the best. So, you can proceed with
[03:08:15] Google Gemini. And what we're trying to
[03:08:17] do with Trigger? Well, we're still
[03:08:19] learning how Trigger works, as well as
[03:08:21] potentially shipping a production
[03:08:23] workflow. So, let's create it. Then,
[03:08:25] once it is created, you can run this CLI
[03:08:28] command to initialize it in the existing
[03:08:31] project. So, just copy it.
[03:08:33] Head back. Open up the terminal.
[03:08:36] You can do it under a new tab.
[03:08:39] And
[03:08:40] just run NPX trigger.dev@latest
[03:08:43] in it, and then pass your specific
[03:08:45] project ID.
[03:08:46] Say yes to install the Trigger.dev CLI.
[03:08:49] And this will now install the
[03:08:51] Trigger.dev SDK and initialize the
[03:08:54] config file. But, it'll first ask you a
[03:08:56] couple of questions, such as choose how
[03:08:59] you want to initialize your project. In
[03:09:01] this case, we'll proceed with the
[03:09:02] Trigger.dev MCP, which allows you to
[03:09:05] vibe your way to a new project. Well, in
[03:09:08] this case, write detailed project
[03:09:10] specifications to come up with a new
[03:09:12] scalable project. It's going to ask you
[03:09:14] whether you want to restrict the MCP
[03:09:16] server to the dev environment only. I'll
[03:09:18] say no.
[03:09:19] And then, you'll be able to choose one
[03:09:21] or more clients to install the MCP
[03:09:23] server into. You can choose all the ones
[03:09:26] that you're using, such as Claude Code,
[03:09:28] VS Code, OpenAI Codex, or really
[03:09:31] anything else that you want.
[03:09:33] And then, press enter.
[03:09:35] Where should the MCP server for Claude
[03:09:37] Code be installed? I'll go over with the
[03:09:40] project.
[03:09:41] Same thing for all the other ones.
[03:09:45] And that's it. We don't need to
[03:09:47] our MCP clients. In your client, look
[03:09:50] for a server named trigger, and then get
[03:09:52] started with trigger dev by asking it to
[03:09:55] add trigger to our project. So, let's do
[03:09:58] just that. I'll open up our Claude code,
[03:10:01] and that's going to be on a new chat
[03:10:03] window, and I'll simply tell it to add
[03:10:05] trigger dev to my project. And we can
[03:10:07] now run it, but just before I do, I want
[03:10:10] to share another thing with you, and
[03:10:11] that is that trigger also supports agent
[03:10:15] skills to teach any AI coding assistant
[03:10:17] best practices for writing tasks,
[03:10:20] agents, and workflows. So, we can
[03:10:22] install it as we did for all the other
[03:10:24] dev tools by opening up the terminal and
[03:10:27] running MPX skills add trigger.dev
[03:10:31] skills.
[03:10:32] We can choose uh trigger agents, config,
[03:10:36] and maybe setup. I think that's going to
[03:10:38] be all we need for now, but you can just
[03:10:40] go ahead and add all of them as well.
[03:10:43] Choose your specific agents you want to
[03:10:45] add it for.
[03:10:47] Do it within the projects through
[03:10:49] symlink, and then quickly install it.
[03:10:52] Now, let's go ahead and ask it to add
[03:10:54] trigger dev to my project. Then, let's
[03:10:57] run it. It's going to explore the
[03:10:58] project structure,
[03:11:00] find all the relevant files, and the
[03:11:02] architecture context, which matters a
[03:11:03] lot, it's going to get the full picture,
[03:11:06] and it'll start with configuring the
[03:11:08] trigger config.ts,
[03:11:10] creating a trigger directory with
[03:11:12] example tasks, adding the trigger.dev
[03:11:15] route handler, and finally updating the
[03:11:17] progress tracker. And there we go, after
[03:11:19] a couple of minutes, the trigger dev is
[03:11:21] now set up. So, it first added the
[03:11:24] trigger config.js.
[03:11:27] So, let's quickly go over into it.
[03:11:30] That's going to be within our
[03:11:33] trigger.config.ts
[03:11:34] in the root of the application,
[03:11:36] and it looks something like this.
[03:11:39] It is coming from trigger dev SDK.
[03:11:41] We define a specific configuration, and
[03:11:44] then we need to connect it to a project
[03:11:46] reference.
[03:11:48] This is coming from our environment
[03:11:49] variables. So, very soon we'll have to
[03:11:51] find it in our Trigger Dev dashboard,
[03:11:53] and then add it to our .env's. Then,
[03:11:56] below the project, we can add a runtime
[03:11:59] and set the environment to node. When it
[03:12:02] comes to directories, ./trigger is going
[03:12:05] to be fine, or in this case, I think we
[03:12:07] can just leave it to trigger. Now, max
[03:12:09] duration stands for the max compute
[03:12:12] seconds a task is allowed to run.
[03:12:15] If the tasks exceed this duration, it'll
[03:12:17] be stopped. And by default, we can set
[03:12:20] it to something like 3600,
[03:12:23] so that any task can run up to an hour
[03:12:25] before it's stopped.
[03:12:27] But again, that's not needed because
[03:12:28] most of our AI tasks will be done in a
[03:12:30] couple of minutes.
[03:12:32] And then for the retries, if something
[03:12:34] fails, Trigger Dev will retry it up to
[03:12:37] three times with increasing delays
[03:12:39] between each attempt. So, having that
[03:12:41] built right in to make sure that if
[03:12:43] something does go wrong, which it often
[03:12:44] does with AI generation,
[03:12:47] it retries it. So, when your user comes
[03:12:49] back to your app, whatever they were
[03:12:50] waiting for from an AI agent is waiting
[03:12:52] for them there. Okay, so let's get those
[03:12:54] keys.
[03:12:55] I'll head back over to Trigger Dev,
[03:12:57] specifically scroll down to API keys,
[03:13:01] and right here you'll be able to find
[03:13:02] your secret key. So, simply copy it.
[03:13:05] Then, head over into your .env.local,
[03:13:09] and here we can add, as it specifies,
[03:13:13] the Trigger project ref,
[03:13:16] as well as the Trigger secret key. So,
[03:13:19] the secret key is the one we just
[03:13:20] copied, and the project key you can find
[03:13:22] right here by going over to the tasks
[03:13:25] and copying it right here from the end
[03:13:28] part of the CLI init command.
[03:13:31] And then just paste it over here. And
[03:13:33] the next part is to start your local dev
[03:13:36] workflow. And I think this is the exact
[03:13:39] second step from our 3-minute setup. NPX
[03:13:42] trigger dev at latest dev. So, you can
[03:13:45] open up your terminal, make sure that
[03:13:47] it's not the one running your
[03:13:48] application.
[03:13:49] And before we run this, let me actually
[03:13:51] explain what it does.
[03:13:53] This is specific to local development.
[03:13:55] Trigger dev background tasks don't run
[03:13:58] on your machine automatically. They need
[03:14:00] a local worker process running alongside
[03:14:03] your Next.js dev server.
[03:14:05] So, just to run this command, would you
[03:14:07] like to install the Trigger dev code
[03:14:09] agent rules? Well, yeah, go ahead.
[03:14:11] We can select it for Claude code or
[03:14:14] whichever other agent you're using.
[03:14:16] And choose the rules you want to
[03:14:17] install. Let's go with basic, advanced.
[03:14:21] You know what? Let me go with all of
[03:14:22] them.
[03:14:24] Now, it's going to wait for you to log
[03:14:26] in to your Trigger dev account, which
[03:14:28] you can do by simply heading over to
[03:14:30] this URL and then authenticating your
[03:14:32] account. Once you're successfully
[03:14:34] authenticated, you can head back and
[03:14:36] you'll be able to see a screen that
[03:14:38] looks something like this.
[03:14:40] Logged in successfully, Trigger dev is
[03:14:42] running, and the local worker is ready.
[03:14:46] So, keep this running whenever you're
[03:14:47] developing locally, because without it,
[03:14:49] any task you trigger will queue, but
[03:14:52] never execute.
[03:14:53] And in production on Vercel, this isn't
[03:14:55] needed because Trigger dev will handle
[03:14:58] the worker infrastructure for you. So,
[03:15:00] if you now head back over to your
[03:15:01] dashboard, you'll be able to see two
[03:15:03] different tasks generate design and
[03:15:05] generate spec, which is absolutely
[03:15:07] amazing. This was going to be one of my
[03:15:10] upcoming project specifications to add,
[03:15:12] but it looks like the MCP already
[03:15:14] figured out exactly what we want, and it
[03:15:17] created those tasks right here. So, soon
[03:15:19] enough, you'll be able to see how those
[03:15:21] tasks actually run and then see more
[03:15:24] information about it. So, that was it
[03:15:26] for the setup. And then in the next
[03:15:28] lesson, let's build the AI generation
[03:15:30] logic.


## Chapter 16: AI Architecture Design Generation Flow (03:15:32)

[03:15:33] Okay, Trigger.dev and the agent together
[03:15:36] already created for us the task
[03:15:38] skeletons. But in this lesson, we'll
[03:15:41] build the full AI generation flow. Now,
[03:15:44] before we make our system design agent
[03:15:46] logic, we'll have to install a couple
[03:15:48] more packages. So, open up your
[03:15:50] terminal. We'll have to go with the
[03:15:52] third one right here.
[03:15:54] And run npm install
[03:15:56] @trigger.dev/react-hooks,
[03:16:00] which lets the front-end subscribe to a
[03:16:02] live Trigger.dev background run without
[03:16:05] manually polling. So, think of it like
[03:16:07] instead of asking is the job done yet
[03:16:10] every few seconds, the hook will stream
[03:16:12] in real-time status updates directly to
[03:16:15] the UI as the task progresses.
[03:16:18] Then, there's the @ai-sdk/google,
[03:16:21] which is the Google provider for the
[03:16:22] Vercel AI SDK. And in this case, we'll
[03:16:25] be using Gemini for both design
[03:16:27] generation and spec generation. But of
[03:16:29] course, feel free to use any other agent
[03:16:31] you prefer. And finally, AI is the core
[03:16:34] Vercel AI SDK, which is going to give us
[03:16:37] utilities for generating text or
[03:16:39] generating different objects by working
[03:16:41] consistently with any kind of AI
[03:16:43] provider. So, go ahead and install these
[03:16:46] three. And while they're getting
[03:16:47] installed, head over to AI
[03:16:49] Studio.google.com,
[03:16:51] which we're going to connect with
[03:16:53] Trigger.dev to infuse it with all sorts
[03:16:55] of different functionalities. So, click
[03:16:57] get started. Make sure to authenticate
[03:16:59] with your account.
[03:17:01] And Google AI Studio will give you free
[03:17:03] credits in most regions, which is going
[03:17:05] to be enough to test out the generation
[03:17:07] flow throughout this build.
[03:17:09] So, click get API key, then create a new
[03:17:13] API key. You can call it something like
[03:17:15] Ghost AI.
[03:17:18] And then, you'll be given all your API
[03:17:20] key details. So, first, copy the actual
[03:17:22] API key
[03:17:24] and paste it into your .env.local.
[03:17:28] Specifically, that's going to be under
[03:17:31] google_ai_api_key,
[03:17:35] and it's going to be set to this key you
[03:17:37] just copied. Or, if you want to get a
[03:17:40] completely free alternative to Google
[03:17:43] Gemini, OpenRouter has a pretty good
[03:17:45] selection of free models. I recommend
[03:17:47] this Nvidia Neumotron 3 Nano Omni.
[03:17:51] That's a mouthful. Which is a free model
[03:17:54] that has a 256,000 context window, and
[03:17:58] it handles the architecture generation
[03:18:00] pretty well. Just keep in mind that the
[03:18:01] free tier models always have usage
[03:18:03] limits. So, if you go that route, simply
[03:18:06] swap that AI SDK Google thing for the
[03:18:09] OpenRouter SDK in the generation task.
[03:18:12] For this video, I'll personally use
[03:18:13] Google AI Studio, but again, as with the
[03:18:16] AI agents, follow along with whichever
[03:18:18] one works for you. So, now with the
[03:18:20] setup ready, we are ready to start
[03:18:22] adding the Trigger.dev task spec files.
[03:18:26] So, head over into our context feature
[03:18:29] specs,
[03:18:30] and find or create a new one called
[03:18:33] 22_design_agent_api.md.
[03:18:38] The goal of this feature is to set up
[03:18:40] the back-end flow for design generation
[03:18:43] using Trigger.dev.
[03:18:44] And keep in mind that when we're
[03:18:45] referring to design here, we're
[03:18:47] referring to the systems or architecture
[03:18:49] design of our applications. So, we're
[03:18:52] setting up this design agent API for the
[03:18:54] back-end wiring. Starting with the
[03:18:57] trigger route, where we need to create a
[03:18:59] specific post route that should accept
[03:19:01] the design prompt and some context, and
[03:19:04] then trigger the design task through
[03:19:06] Trigger.dev. Because, as I said, these
[03:19:09] tasks and these AI prompts can take some
[03:19:11] time to process. Then, we'll add task
[03:19:14] tracking. This is going to be a special
[03:19:16] model in Prisma to track Trigger.dev
[03:19:19] runs and verify ownership.
[03:19:21] Who created the run, when, and what is
[03:19:24] it all about?
[03:19:25] We should add the token route to verify
[03:19:27] ownership, and then finally create the
[03:19:30] actual design task. We want to check the
[03:19:33] existing Trigger.dev setup and installed
[03:19:35] agent features, reuse the existing
[03:19:37] setup, export a minimal design task, and
[03:19:40] for now not add any design logic yet.
[03:19:44] Just the infrastructure that makes the
[03:19:45] next spec possible.
[03:19:47] You learned that already. Spec by spec,
[03:19:50] we're getting closer to the final
[03:19:51] solution.
[03:19:53] So, let's go ahead and run it. As usual,
[03:19:56] you can just tell it to read the current
[03:19:58] file, update the context progress
[03:20:00] tracker, and implement it exactly as
[03:20:03] specified. And after some work, feature
[03:20:06] 22, the design agent API, has now been
[03:20:09] completed. It created a new Prisma model
[03:20:13] called task run with run ID, project ID,
[03:20:16] user ID, so we know which projects are
[03:20:18] being run over on Trigger.dev. Then,
[03:20:20] there's the design agent itself, which
[03:20:23] is a minimal task accepting a prompt and
[03:20:25] a room ID, which logs and echoes the
[03:20:28] inputs.
[03:20:29] So, if you open it up, you'll see that
[03:20:31] it looks like this. Currently, there's
[03:20:34] no logic and functionality, but we'll
[03:20:36] add it very soon.
[03:20:38] Then, there's the post API AI design,
[03:20:41] which requires authentication. And what
[03:20:43] this one does is it basically figures
[03:20:45] out whether the user is authenticated,
[03:20:47] takes in the body, and finally creates a
[03:20:50] new task run in the database.
[03:20:53] But of course, before it hands it over
[03:20:55] to Trigger.dev. But now, the actual task
[03:20:58] is pretty empty. It's just console
[03:21:00] logging design agent triggered, and it's
[03:21:02] not doing anything else.
[03:21:04] So, our next task is to implement the
[03:21:07] full AI design agent logic, so a user
[03:21:10] prompt results in real-time updates on
[03:21:13] the canvas. To do that, head over into
[03:21:15] our feature specs, and let's focus on
[03:21:18] adding the 23rd spec, which is design
[03:21:21] agent
[03:21:23] logic.md.
[03:21:25] And as I said, the goal here is to
[03:21:27] implement the full AI design agent
[03:21:29] logic.
[03:21:31] So, first we need to update the file
[03:21:32] which was just created.
[03:21:34] Before, when I check the product
[03:21:36] behavior of the system, check the live
[03:21:38] blocks and trigger agent skills. This is
[03:21:40] very important. Sometimes you have to
[03:21:41] explicitly tell it to check the skills.
[03:21:44] Follow the trigger dev setup and agent
[03:21:46] patterns already set up. Reuse the
[03:21:48] existing live blocks flow and presence
[03:21:50] patterns instead of creating new ones,
[03:21:52] and then implement use Gemini logic to
[03:21:56] interpret the user prompt, update the
[03:21:59] canvas using the collaborative flow
[03:22:01] utilities, supporting actions like
[03:22:03] adding nodes, moving them, resizing
[03:22:05] them, updating them, deleting them.
[03:22:07] Basically, everything that our
[03:22:09] application is already doing.
[03:22:11] Then, want to publish that AI activity
[03:22:13] to the shared status feed, so all users
[03:22:15] can see the progress.
[03:22:17] Update the AI presence through cursors
[03:22:19] and thinking state, and push clear
[03:22:21] status messages at key steps. If you
[03:22:24] think about it, this is a very important
[03:22:28] and big feature spec. Maybe the biggest
[03:22:31] one in our application so far, because
[03:22:33] now we're essentially telling our AI
[03:22:35] agent and trigger
[03:22:37] to figure out the entirety of our
[03:22:40] application
[03:22:42] and to replicate its functionality on
[03:22:44] its own while following the user prompt.
[03:22:47] Like, the user is telling it to create
[03:22:50] something on the canvas, and it should
[03:22:52] create it.
[03:22:53] So, let's go ahead and see how well it
[03:22:55] does by opening up a new Claude code
[03:22:57] window, giving it access to the file,
[03:22:59] and asking it to read the spec file,
[03:23:04] update the progress document, and
[03:23:07] implement it exactly as specified. This
[03:23:09] is a big one, so I'm super excited to
[03:23:12] see how well it actually does it. And
[03:23:14] feature 23 is now complete. This one
[03:23:17] took a bit longer because it's a it's a
[03:23:19] huge one. And we now have a full AI
[03:23:23] agent built within our application
[03:23:25] powered by trigger.dev.
[03:23:27] It uses Gemini 2.0 flash via create
[03:23:31] Google generative AI plus generate text
[03:23:34] with output object to produce a typed
[03:23:37] list of canvas actions for adding,
[03:23:40] moving, resizing, updating, and deleting
[03:23:42] nodes and edges. It sets the AI presence
[03:23:46] by thinking is set to true. So, all
[03:23:48] collaborators can see the AI cursor. It
[03:23:51] broadcasts three different statuses:
[03:23:53] start, thinking, and complete. And it
[03:23:56] applies all mutations atomically in a
[03:23:59] single mutate storage call.
[03:24:01] Perfect. This is exactly what we wanted.
[03:24:03] So, while we can't see it on the screen
[03:24:06] just yet,
[03:24:07] what we can do is head over to our
[03:24:09] trigger.dev dashboard under tasks.
[03:24:12] Currently, we have three separate tasks.
[03:24:14] That's because our initial setup task
[03:24:17] created the skeletons for generate
[03:24:19] design and generate spec, but the new
[03:24:21] one is right here under design agent.
[03:24:23] So, what we can do is maybe we can clean
[03:24:26] up the other two just so they're not
[03:24:28] confusing us. So, under trigger, we can
[03:24:30] remove the generate design and generate
[03:24:32] spec, which are just empty placeholders.
[03:24:36] And instead, we can just leave the
[03:24:37] design agent right here. So, that's the
[03:24:39] only one that remains.
[03:24:41] Now, open it up
[03:24:43] and perform a test run.
[03:24:46] It's going to ask you to pass the data
[03:24:48] as a regular user would through the
[03:24:49] application.
[03:24:50] And we can write something like room ID,
[03:24:53] and you'll have to get this room ID
[03:24:55] directly from one of your canvases.
[03:24:57] So, head over here and create a new
[03:24:59] project. Let's call it something like um
[03:25:03] system design.
[03:25:06] Created. And you can copy the project ID
[03:25:08] directly from the URL right here at the
[03:25:11] top.
[03:25:13] Then, if you head back, you can update
[03:25:15] it over here. And we can ask it to
[03:25:17] architect a real-time chat application.
[03:25:20] I need a web socket server for live
[03:25:23] messaging, a presence service to track
[03:25:25] online users, and a relational database
[03:25:27] for message history. Connect the
[03:25:29] services using a pub sub system like
[03:25:31] Redis, so it can scale horizontally, and
[03:25:33] include an S3 bucket for media
[03:25:36] attachments.
[03:25:37] I'll give you a prompt like this in the
[03:25:39] video kit link down in the description,
[03:25:41] so you can copy it and paste it.
[03:25:43] But make sure to update the room ID. And
[03:25:46] now, let's go ahead and run the test.
[03:25:48] Oh, but before, make sure that your dev
[03:25:51] server is connected right here. If it's
[03:25:53] not, connect it, and then we'll be able
[03:25:55] to run the test.
[03:25:57] As you run it, you'll be able to see all
[03:26:00] the information about this specific task
[03:26:02] run. When it was triggered, when it was
[03:26:05] queued, and when it has started. Now,
[03:26:07] immediately, it'll fail after three
[03:26:10] attempts, saying that we exceeded our
[03:26:12] current quota, and we need to check our
[03:26:14] Google billing plan. So, it's super
[03:26:16] convenient to be able to test the runs
[03:26:18] directly within the Trigger dashboard.
[03:26:20] So, once you top it up or change your
[03:26:22] providers, uh you can just reload your
[03:26:24] Trigger dev server, and then replay the
[03:26:26] run.
[03:26:28] Hopefully, this time, it continues
[03:26:30] running after just a couple of seconds.
[03:26:32] And we get another little API error,
[03:26:35] saying that models Gemini 2.0 Flash is
[03:26:37] no longer available.
[03:26:39] Um I wish they made those backwards
[03:26:41] compatible, but it is what it is. We got
[03:26:44] to find one that actually is compatible.
[03:26:46] So, instead of using 2.0 Flash, I'll
[03:26:49] head over into this design agent file,
[03:26:52] that's going to be right here,
[03:26:54] and I'll switch it over to 2.5
[03:26:58] Flash. I believe that is the latest
[03:27:00] running model. Then, when you change it,
[03:27:03] don't forget to rerun your server.
[03:27:06] Again, the Trigger.dev server by running
[03:27:08] MPX Trigger.dev at latest dev. Then,
[03:27:11] after it creates the local worker, go
[03:27:13] ahead and replay the run. Third times
[03:27:15] the charm. Or, apparently not, because
[03:27:18] after about 20 seconds, we got a little
[03:27:20] error saying, "No object generated.
[03:27:23] Response did not match the schema."
[03:27:27] So, open up a new chat, and let's tell
[03:27:30] it something like this.
[03:27:32] While implementing
[03:27:35] at 23, that's going to be the 23rd
[03:27:39] design spec
[03:27:41] that we tried to do, the agent logic. Or
[03:27:44] rather, we can say after implementing, I
[03:27:46] tried to run a test. And then, I give it
[03:27:49] some more information that we used for
[03:27:51] the test itself, and then pasted the
[03:27:53] error that we got, which you can get
[03:27:54] from the web.
[03:27:56] Finally, we can tell it something like
[03:27:57] analyze trigger.dev and Liveblocks best
[03:28:00] practices. Analyze this doc, and I
[03:28:03] shared it a link to the doc of the
[03:28:06] generating structured data part, because
[03:28:08] so far, it generated it just as text.
[03:28:11] But, what we need to do instead is have
[03:28:14] some kind of a schema that we can
[03:28:16] validate against. So, currently, it is
[03:28:18] using this output, but what we can do is
[03:28:21] use a so-called tool calling approach
[03:28:24] with generate text with a tools object.
[03:28:28] So, I'll tell it analyze this docs page
[03:28:31] and the error, and then, I'll pass some
[03:28:33] additional info which I think is the
[03:28:35] reason for why it's failing.
[03:28:37] So, that design agent is failing because
[03:28:39] generate text is being used with output
[03:28:42] object for structured output. That
[03:28:45] experimental API is causing the runtime
[03:28:47] error.
[03:28:48] So, instead, replace it with a tool
[03:28:50] calling approach using generate text
[03:28:52] with a tools object. Each canvas action
[03:28:55] should be its own tool. So, we have the
[03:28:57] add node, move node, and so on. And this
[03:29:00] way it's going to follow the schema
[03:29:02] precisely. So, have a message that looks
[03:29:04] like this and send it out.
[03:29:08] This is also a useful approach to share
[03:29:10] it a link to a specific documentation
[03:29:13] page so that it can do a web fetch and
[03:29:16] figure out how it works. Or
[03:29:17] alternatively, there's also this context
[03:29:20] seven, which is a library of the latest
[03:29:22] documentations that you can directly
[03:29:24] fuse with cursor, Claude, or other LLMs.
[03:29:28] For example, it has the latest docs for
[03:29:29] Next.js updated 9 hours ago. Same thing
[03:29:32] for React and most likely for AI agents
[03:29:36] as well. There we go. AI SDK. This is
[03:29:39] what we're using. So, if we hook this up
[03:29:41] with our agent, and you can do that very
[03:29:43] easily just by copy and pasting this
[03:29:45] thing right here, it would have all the
[03:29:47] latest docs. But let's see what it can
[03:29:49] do with just the URL. And very quickly,
[03:29:51] the build passes. Here's what changed.
[03:29:54] The output object in generate text
[03:29:56] relies on the model emitting a single
[03:29:59] structured JSON blob. But Gemini 2.5
[03:30:02] Flash returned a response that didn't
[03:30:04] match the schema, triggering the AI no
[03:30:06] object generated. So, in this case,
[03:30:08] we're replacing the output with a tool
[03:30:11] approach where each canvas action is its
[03:30:13] own named tool, like add node, move
[03:30:16] node, and so on. So, after generation,
[03:30:18] all tool calls are collected and then we
[03:30:20] get the final canvas.
[03:30:22] Okay, so let's go ahead and test it out.
[03:30:25] Back on Trigger.dev, we can just replay
[03:30:27] the run. And in about 15 seconds, it
[03:30:30] finished. We got a successful output
[03:30:32] with 11 actions applied and a summary of
[03:30:36] what happened. Now, let's make it even
[03:30:38] better by adding another feature spec
[03:30:42] right here. That's going to be 24 AI
[03:30:45] presence state.md.
[03:30:48] And the goal of this one is to add a
[03:30:51] shared activity indicator so that when
[03:30:54] AI is generating, everyone in the room
[03:30:56] will see it. A status indicator in the
[03:30:59] sidebar, as well as a thinking spinner
[03:31:02] cursor, and the input will be disabled
[03:31:04] while generation is active. So, let's go
[03:31:06] ahead and run it with the usual message.
[03:31:11] And let's give it a minute. And I sped
[03:31:13] up the process for you, but this one
[03:31:15] definitely took some time, but
[03:31:17] thankfully the build passes cleanly.
[03:31:20] We added some new types for the
[03:31:23] tasks.ts,
[03:31:24] modified the liveblocks.config, and
[03:31:27] added the presence cursors. But before
[03:31:29] we actually go ahead and test this out,
[03:31:31] I want to finish the implementation of
[03:31:33] the sidebar so we can test everything
[03:31:35] we've been working on together.
[03:31:37] So, go ahead and open up a 25 sidebar
[03:31:42] chat feed.md
[03:31:44] file.
[03:31:45] And within this one, the goal is to wire
[03:31:49] up the AI chat liveblocks feed into the
[03:31:52] sidebar.
[03:31:53] See, liveblocks feeds are real-time
[03:31:56] message channels. Think of them like a
[03:31:59] group chat that is tied to a specific
[03:32:01] project room. Anyone in that room can
[03:32:04] send a message, and everyone else can
[03:32:06] instantly see it. In this case, we're
[03:32:08] using two separate feeds, the AI chat
[03:32:11] feed and the AI status feed. The AI
[03:32:14] status feed is simply for some kind of
[03:32:17] progress signals, and AI chat is for the
[03:32:20] actual conversation. This spec handles
[03:32:22] the chat side where users can send
[03:32:25] messages and make them appear across
[03:32:27] every connected client. So, let's go
[03:32:29] ahead and run it, and I'll speed it up
[03:32:32] for you. And feature 25 is done. Here's
[03:32:35] what was changed across three files.
[03:32:37] First, added some additional types.
[03:32:40] Then, in the config, we extended the
[03:32:42] feed message data with optional chat
[03:32:45] fields. So, now it also supports the
[03:32:47] sender, role, content, and timestamp
[03:32:50] alongside the existing AI status fields,
[03:32:53] so they both coexist under the same
[03:32:55] type. The key addition right here was
[03:32:57] the chat feed ID constant. So, now we
[03:33:01] support the chat alongside these status
[03:33:03] updates as well. And finally, just one
[03:33:06] more thing before we test it, we have to
[03:33:09] wire everything together. So far, this
[03:33:11] is just the UI. In the last couple of
[03:33:13] prompts, we implemented the UI side of
[03:33:15] things and Liveblocks side of
[03:33:17] functionality. Just before that, we
[03:33:19] implemented background tasks through
[03:33:22] trigger.dev, but now we have to wire it
[03:33:25] all together.
[03:33:26] So, go ahead and open up 26
[03:33:30] design agent
[03:33:33] the goal here
[03:33:36] is really to connect everything
[03:33:38] together.
[03:33:39] We are submitting a prompt from the AI
[03:33:42] sidebar, then we're tracking the status
[03:33:45] live through the use real-time run
[03:33:48] function. We're also showing a status
[03:33:51] strip while the task runs,
[03:33:54] and we're letting Liveblocks handle the
[03:33:56] updates of the canvas automatically.
[03:33:59] So, let's go ahead and run it. And as
[03:34:01] soon as it is finished, we're going to
[03:34:03] test everything together.
[03:34:05] And in a couple of minutes, definitely
[03:34:07] much faster than it would take me to do
[03:34:09] all of this, feature 26 is done. Again,
[03:34:13] just modify some of the types,
[03:34:16] modify the config to widen it just a
[03:34:18] bit, and then most importantly, the
[03:34:20] major rework happened within the AI
[03:34:22] sidebar, where the handle send now
[03:34:25] actually pushes the user message to AI
[03:34:28] chat, calls our API endpoint to get the
[03:34:32] run ID, and then the token as well to
[03:34:34] get the public token, and then stores
[03:34:36] both in state.
[03:34:39] Finally, trigger.dev hooks run. We track
[03:34:42] the run and once it reaches a final
[03:34:44] status, it pushes the final AI message
[03:34:46] to the AI chat, resetting the loading
[03:34:48] state and clearing the presence. So,
[03:34:51] what do you say that we head back over
[03:34:53] to localhost:3000,
[03:34:54] reload the page, and you'll see a
[03:34:56] missing access token in trigger context
[03:34:59] auth or use API client options. We can
[03:35:02] quickly head back over to just a
[03:35:04] localhost:3000 and editor. It is
[03:35:07] possible that that's because of this
[03:35:08] specific project. So, I'll create a new
[03:35:11] project now.
[03:35:12] I'll call it
[03:35:14] testing
[03:35:15] AI designs
[03:35:18] and create it.
[03:35:20] And once again, we immediately get the
[03:35:22] missing access token in trigger auth
[03:35:25] context or use API client options.
[03:35:28] So, there's this handy little copy error
[03:35:31] info click that you can copy, and then
[03:35:33] you can directly paste the full error
[03:35:35] right here. When I try to open a
[03:35:37] specific canvas, this is the error that
[03:35:40] I get. And then we can just display that
[03:35:42] error.
[03:35:43] Tell it to analyze it by following the
[03:35:47] best practices from both Liveblocks and
[03:35:50] Trigger.dev, and provide me your
[03:35:53] reasoning and idea of what is wrong and
[03:35:56] how to fix it. So, something like this
[03:35:58] does. I noticed when you don't ask it to
[03:36:00] fix it immediately, but rather you first
[03:36:03] ask it to analyze it and give you the
[03:36:05] idea of what it would do, that's not
[03:36:07] cluttering the context as much, and it
[03:36:10] gives you the ability to say whether you
[03:36:13] would like it to execute what it
[03:36:15] suggests or not. So, let's see what it
[03:36:17] comes up with, and then we can
[03:36:18] potentially execute it. And very
[03:36:20] quickly, it was able to figure out the
[03:36:22] reasoning, and I believe it actually
[03:36:24] applied it because it was just a couple
[03:36:26] of lines of code. The root cause was
[03:36:28] that the use real-time run performs an
[03:36:30] eager validation check for access token
[03:36:33] on every render, and it doesn't wait for
[03:36:36] a connection attempt. So, if we pass
[03:36:38] empty string, it's the same as if we
[03:36:40] don't pass it at all, so it immediately
[03:36:42] throws the error on the first render.
[03:36:44] But rather, we need to wait, and only
[03:36:47] when there's an active run, then we need
[03:36:49] to check for the token. So, now if we
[03:36:50] head back, you can see that we can open
[03:36:53] up a design, the new one as well as the
[03:36:57] old one. So, now let's go within the new
[03:36:59] project we created,
[03:37:01] and we are ready to describe a new
[03:37:03] system to AI.
[03:37:06] In this case, you can really go ahead
[03:37:07] and type anything. I'll write something
[03:37:09] like this. You can also pause your
[03:37:11] screen and write it with me. But the
[03:37:13] goal here is to design a high-scale
[03:37:16] e-commerce back-end architecture,
[03:37:18] including an API gateway, a user service
[03:37:21] with auth, a product catalog service
[03:37:24] using a no SQL database,
[03:37:26] and an order processing system that
[03:37:28] communicates via a message queue. Also,
[03:37:31] don't forget to add a Redis cache for
[03:37:33] the catalog to handle high traffic.
[03:37:36] And now, we can go ahead and click send.
[03:37:39] You can see that Ghost AI is analyzing
[03:37:42] your request in real time right now.
[03:37:46] I'm going to zoom it in. So, this is the
[03:37:48] first status that we're seeing. It says
[03:37:50] working right here.
[03:37:51] And then immediately after, we were able
[03:37:54] to see a completed product. So, in this
[03:37:57] case, we get the API gateway,
[03:38:00] the user accessing it, browsing
[03:38:03] different products, placing an order
[03:38:05] through the product catalog service, and
[03:38:07] that goes into the message queue, and
[03:38:09] then the order is actually processed.
[03:38:11] So, this is a great and pretty detailed
[03:38:14] system architecture diagram, and we were
[03:38:16] able to generate it using AI very
[03:38:19] quickly. Because we already had the
[03:38:21] underlying system for creating different
[03:38:23] nodes and adding labels within the
[03:38:25] elements and the edges.
[03:38:28] And then we just created a system that
[03:38:30] works in the background through
[03:38:31] trigger.dev that makes use of all of
[03:38:34] those functionalities within the app,
[03:38:37] generates that JSON, and then we just
[03:38:39] slap it onto the canvas. So, now that
[03:38:41] everything is working so well, the last
[03:38:43] missing piece of the puzzle is to
[03:38:46] generate the specs. We need to take
[03:38:49] everything that is on the canvas and
[03:38:51] generate a markdown document that we can
[03:38:53] then actually feed into a thinking or
[03:38:57] planning AI agent, which is going to
[03:38:58] make it the strongest possible starting
[03:39:00] point for starting to develop any kind
[03:39:03] of an application for real. But, the
[03:39:06] first step is now done. It's all about
[03:39:08] approaching the architecture from a
[03:39:10] planning and very detailed way, like you
[03:39:13] are an architect really, designing a
[03:39:15] specification document. So, in the next
[03:39:17] lesson, let's focus on generating that
[03:39:20] spec.


## Chapter 17: AI Spec Generation (03:39:21)

[03:39:22] The flow for generating the spec is
[03:39:25] almost the same pattern as for
[03:39:27] generating the design. A trigger route,
[03:39:30] a background task, and a token route for
[03:39:33] ownership tracking. Then, persistence to
[03:39:36] Vercel blob, and finally, a piece of UI
[03:39:39] to then view and download the result.
[03:39:42] Because we've already built this pattern
[03:39:44] once, these specs will move faster. So,
[03:39:48] let's go ahead and build it one by one
[03:39:50] by creating a feature spec number 27
[03:39:53] called spec generation flow.md.
[03:39:58] And yeah, as I told you, the goal of
[03:40:01] this one is to build the full backend,
[03:40:04] the trigger route, and the trigger.dev
[03:40:06] task that calls Gemini and then
[03:40:09] generates a markdown spec, but most
[03:40:11] importantly, it generates it from the
[03:40:14] canvas state and the chat history. You
[03:40:18] can see that right here, spec generation
[03:40:20] based on the project ID, room ID, chat
[03:40:24] history, nodes, and edges. No backend
[03:40:27] yet, We just wanted to execute that
[03:40:29] task. So, let's go ahead and run it. 27
[03:40:32] spec already. I'm not sure how to feel
[03:40:35] about it. Is it too high or too low of a
[03:40:37] number? I mean, considering what we've
[03:40:39] implemented and what we've done so far,
[03:40:42] like a full stack, full canvas
[03:40:45] AI-powered application with templates
[03:40:48] and everything else we've done. I mean,
[03:40:50] I think this would take us months to
[03:40:53] develop manually. And yeah, now that I
[03:40:56] think about it, I'm sure. 27 spec files
[03:41:00] is definitely not a lot for this
[03:41:02] production-ready application we've
[03:41:04] developed so far. We're very close, so I
[03:41:07] believe we'll be able to get it done in
[03:41:08] under 30. Let's make it run.
[03:41:11] In this case, it looks like it's
[03:41:13] actually running all three files in
[03:41:15] parallel. This one was actually pretty
[03:41:17] quick. Feature 27 is complete, and the
[03:41:20] only thing we need to check from this
[03:41:21] one is the trigger task called generate
[03:41:24] spec. So, let's head over into that
[03:41:26] file, and you'll notice that it's quite
[03:41:29] similar to design agent. It takes all
[03:41:31] the schemas, it builds the context,
[03:41:34] returns it all, and here's a system
[03:41:36] prompt saying that we are a ghost AI
[03:41:39] senior technical architect whose job is
[03:41:42] to generate a comprehensive markdown
[03:41:44] technical specification document based
[03:41:46] on the provider architecture canvas and
[03:41:49] the conversation context. And we then
[03:41:51] give it some information on how to
[03:41:52] structure the spec. Finally, we call the
[03:41:55] schema task coming from trigger, give it
[03:41:58] an ID, the schema of what it needs to
[03:42:01] do, the ability to retry it after
[03:42:03] specific options, and then what is it
[03:42:06] actually running? In this case, we're
[03:42:07] calling the Google generative AI and
[03:42:10] asking it to generate the spec, build
[03:42:13] the context, generate it in text. Again,
[03:42:16] we have to use 2.5 flash. 2.0 is no
[03:42:20] longer there. And then finally, it gets
[03:42:22] the spec and returns it. Before we go
[03:42:25] ahead and test it, we have to first
[03:42:27] implement a couple of functionalities
[03:42:29] and then wire it to the sidebar. So, go
[03:42:32] ahead and open feature specs and create
[03:42:35] a unit 28 spec persistence
[03:42:39] download.md.
[03:42:41] The goal of this one is to save the
[03:42:44] generated spec file to Vercel blob,
[03:42:47] store the URL in project spec Prisma
[03:42:49] model, and then add a secure download
[03:42:52] route. Basically, same Prisma metadata
[03:42:55] plus the blob content pattern that we
[03:42:57] use for the canvas auto save. That's how
[03:42:59] we want to save it.
[03:43:00] And then finally, we want to ensure that
[03:43:02] it's downloadable through this specific
[03:43:05] API route. It should authenticate the
[03:43:08] user, verify the access, verify the spec
[03:43:11] belongs to that project, and then fetch
[03:43:13] the file and return it as a downloadable
[03:43:16] markdown file.
[03:43:18] Go ahead and open this with your AI
[03:43:20] agent. As usual, we'll tell it to read
[03:43:23] the file, update our progress tracker,
[03:43:25] and then implement it exactly as
[03:43:27] specified.
[03:43:29] And while it's doing its job, let's
[03:43:31] quickly check how the progress tracker
[03:43:33] is coming along. I mean, we've
[03:43:34] implemented so many features so far, and
[03:43:37] all of it is here for future developers
[03:43:40] within your team or future agents
[03:43:42] working on the project to check out and
[03:43:44] then continue developing new features on
[03:43:47] top of. All the architecture decisions,
[03:43:49] session notes, and more.
[03:43:52] So, yeah. Let's see how it approaches
[03:43:54] this one. And feature 28 is done. A
[03:43:57] summary right here is that it added a
[03:43:59] project spec Prisma model with the ID,
[03:44:03] project ID, file path, and created at.
[03:44:05] And it's attached to a project. So, if
[03:44:08] we delete it, it's going to be deleted
[03:44:09] as well. Migrations have already been
[03:44:11] applied for us. I love agents for doing
[03:44:14] that automatically, so we don't have to
[03:44:16] run Prisma generate and migrate on our
[03:44:18] own. And finally, it updated the
[03:44:20] generate spec so that after the markdown
[03:44:23] is generated, it uploads it to a Vercel
[03:44:25] blob so that we can download it later
[03:44:28] on. And this route is responsible for
[03:44:30] that. So now, just before we tested we
[03:44:34] need to wire everything together. You
[03:44:36] know how I like to make sure that these
[03:44:38] spec files are really only handling one
[03:44:40] thing at a time. So in 27, we handled
[03:44:43] the spec generation flow. Then we made
[03:44:46] it persist by storing it into Vercel
[03:44:48] blob and creating a download route. And
[03:44:51] now finally, in 29, spec UI
[03:44:55] integration.md,
[03:44:57] we are going to wire everything together
[03:44:59] into the specs tab in the AI sidebar
[03:45:03] through a list of generated specs. We
[03:45:05] could have multiple, a preview model
[03:45:07] that renders the markdown in case you
[03:45:09] want to preview it in the browser, and
[03:45:11] finally a download action to download it
[03:45:14] on your device. So, go ahead and run it.
[03:45:17] And let's give it some time to implement
[03:45:18] it. And let's let it do its thing.
[03:45:21] And now that feature 29 is fully
[03:45:23] implemented and the build passes, which
[03:45:25] is important, we'll soon be ready to
[03:45:27] test it out. So, there's two new backend
[03:45:30] routes. The first one gets access to all
[03:45:33] the project specifications for a
[03:45:34] specific project, and then the second
[03:45:37] one actually creates a downloadable
[03:45:39] markdown text. And the AI sidebar got
[03:45:42] updated so we can test it all out. Back
[03:45:45] within the browser, if you now head over
[03:45:47] to specs and click generate spec, you'll
[03:45:50] notice that, at least on my end,
[03:45:52] nothing's happening.
[03:45:54] On your end, it might be working. Maybe
[03:45:56] your agent did a bit of a better job,
[03:45:58] but at least here, it's not budging. But
[03:46:01] thankfully, we are getting some errors
[03:46:03] right here within the terminal.
[03:46:05] So, I'll go ahead and copy these errors
[03:46:08] and tell it when I click the generate
[03:46:11] spec button, it doesn't do anything. And
[03:46:14] this is what I see in the terminal. I
[03:46:15] pasted it and then I'll say analyze it
[03:46:19] and provide a solution.
[03:46:21] Refer to trigger.dev and liveblocks
[03:46:25] skills if needed and press enter.
[03:46:28] I find it that sometimes it's great to
[03:46:30] explicitly mention that it can refer to
[03:46:32] specific skills if you think it's going
[03:46:34] to be useful. Yeah, this definitely took
[03:46:36] some time. But yeah, it says right here
[03:46:39] just to restart your server. It did some
[03:46:43] additional changes, but I think after
[03:46:45] all the changes, it's necessary to just
[03:46:47] reload it. So that's what I'm going to
[03:46:49] do. Back on localhost 3000, it's going
[03:46:51] to be active.
[03:46:53] Make sure to reload the page and then
[03:46:55] head over to specs.
[03:46:58] Click generate spec
[03:47:00] and it is generating. While it is
[03:47:02] actually generating, you can head over
[03:47:05] to trigger.dev under runs and you can
[03:47:08] see generate spec is being executed as
[03:47:10] we speak. So here you can see a bit more
[03:47:13] information on exactly what is
[03:47:14] happening. This is the payload that we
[03:47:16] sent into it, all the different nodes,
[03:47:19] all the information about the
[03:47:20] architecture and more. And it looks like
[03:47:23] it generated it and returned it. So now
[03:47:25] if you head back, you'll be able to see
[03:47:27] a new markdown file that when you click
[03:47:30] on it, it'll be opened within a markdown
[03:47:32] previewer right here in the browser.
[03:47:36] There we go. It's a bit tiny. We can
[03:47:38] definitely increase its width.
[03:47:40] But yeah, I mean, take a look at this.
[03:47:42] This architecture diagram, it was able
[03:47:45] to generate a pretty hefty technical
[03:47:47] specification document that outlines
[03:47:50] this huge system that we can send over
[03:47:52] to our planning agent and start
[03:47:54] developing it. Let's test the download
[03:47:56] functionality as well. I clicked the
[03:47:58] button and it opened it up. It's a long
[03:48:01] file, but if you've been following along
[03:48:04] with this course, you know that
[03:48:05] specifications have to be long,
[03:48:08] especially if you're creating one spec
[03:48:10] for the entire system. So, that's it.
[03:48:13] That's the full Ghost AI feature set
[03:48:15] working end to end. So, what do you say
[03:48:18] that we test out the functionalities one
[03:48:20] more time on two separate screens? At
[03:48:22] least right now, I'm on two separate
[03:48:24] tabs, so still logged in with the same
[03:48:26] account, but that should be okay.
[03:48:28] So, I'll say final test and create a new
[03:48:32] project.
[03:48:34] That project will immediately show up
[03:48:36] right here as well after reloading the
[03:48:39] page.
[03:48:40] And now we are viewing it from both
[03:48:42] sides.
[03:48:44] Both of us are in the same room, and you
[03:48:45] can see my name
[03:48:48] and cursor pointing different locations.
[03:48:51] Of course, if it were some other people
[03:48:53] right here, you'll be able to see their
[03:48:55] profiles as well.
[03:48:57] And as soon as I drag and drop
[03:48:58] something, you can see that it appears
[03:49:01] immediately. It also auto zoomed in
[03:49:03] right here, and we can continue creating
[03:49:06] the diagram. You can see it happens in
[03:49:09] real time. And that's the beauty of
[03:49:11] Liveblocks. What we can do next is test
[03:49:14] the AI functionalities. So, I'll open up
[03:49:17] the AI window right here,
[03:49:20] and let's go with something simple and
[03:49:22] default like design an e-commerce
[03:49:24] backend.
[03:49:26] I'll first select all of these by
[03:49:27] holding the shift key and then remove
[03:49:29] them.
[03:49:31] And design that e-commerce backend
[03:49:33] by sending a new AI chat message. It'll
[03:49:37] start working on it,
[03:49:39] and very quickly it'll generate the full
[03:49:42] UI right here. And that UI got generated
[03:49:46] for the other user as well. Finally, we
[03:49:48] can generate some specs out of it. And
[03:49:50] of course, this is happening in the
[03:49:52] background as a task that is being run
[03:49:55] on the trigger.dev side of things. Or
[03:49:58] specifically, we are running an agent,
[03:50:00] in this case Gemini, to process
[03:50:02] something. But, of course, you can run
[03:50:04] all sorts of different AI agents, media
[03:50:06] processing, media generation. Like,
[03:50:08] there's tons of different use cases for
[03:50:10] how Trigger can be used, and we can
[03:50:12] definitely explore some more of it in
[03:50:14] one of the upcoming videos.
[03:50:16] But, yeah, the spec is here. We can
[03:50:18] preview it, download it, and that's it.
[03:50:22] That is the entire app. So, in the next
[03:50:25] lesson, let's get it deployed.


## Chapter 18: Deployment (03:50:28)

[03:50:30] Okay. Now that the app is complete,
[03:50:32] before we deploy, we need to switch a
[03:50:35] few services from development to
[03:50:37] production.
[03:50:39] Dev keys are rate-limited and aren't
[03:50:41] meant for real traffic. So, we have to
[03:50:44] update Liveblocks, Trigger.dev, and make
[03:50:46] sure that every environment variable is
[03:50:49] set correctly in Vercel. Let's start
[03:50:51] with Liveblocks.
[03:50:52] Create a new project and call it Ghost
[03:50:56] AI production or something like that.
[03:50:59] And set the environment to production.
[03:51:02] Then, from the API key section, simply
[03:51:05] copy the public key,
[03:51:07] head over into your .env.local,
[03:51:10] and paste it right here.
[03:51:12] Liveblocks public key, you can override
[03:51:15] the development one, or in case you want
[03:51:17] to keep it, you can just comment it out.
[03:51:19] But, again, make sure to add new
[03:51:22] production ones right here. Or at least
[03:51:24] when we're deploying the project on
[03:51:25] Vercel, you'll have to put these new
[03:51:27] updated ones.
[03:51:29] So, yeah, let's go ahead and update it.
[03:51:32] Uh the Liveblocks public key is going to
[03:51:34] be this new prod key right here.
[03:51:37] And also, let's generate a secret key,
[03:51:40] which you can copy,
[03:51:42] and then also override right here.
[03:51:45] Step two is get the Trigger.dev
[03:51:47] production API keys by heading over to
[03:51:50] the dashboard, and then in the top
[03:51:52] selector right here, where it says
[03:51:55] environment, switch it over from
[03:51:57] development to production. Then, from
[03:52:01] the project settings right here under
[03:52:03] API keys,
[03:52:04] go ahead and copy the secret key and
[03:52:07] replace the existing one right here
[03:52:09] under ENV local.
[03:52:11] Once again, I will comment out the
[03:52:12] previous one and just update this one
[03:52:15] that's going to have prod right here in
[03:52:17] the middle. And below the API keys, you
[03:52:19] can head over to general project
[03:52:21] settings and copy the project ref, which
[03:52:24] I believe should be the same. So, if you
[03:52:27] duplicate it
[03:52:29] and override it here, you'll see that
[03:52:31] one is actually the same, so we can
[03:52:33] leave it as it is. Now, go ahead and
[03:52:35] copy all of your ENVs
[03:52:38] and we have to push our changes.
[03:52:40] So, run git add dot, git commit {dash}
[03:52:44] m,
[03:52:45] finalize the app and prepare it for
[03:52:48] deployment, and then run git push.
[03:52:51] Then, head over to Vercel, click add a
[03:52:54] new project, and just import it from
[03:52:56] git. Once pushed, it should have changes
[03:52:59] a couple of seconds ago, not a couple of
[03:53:01] hours ago. But, the reason it says 5
[03:53:03] hours here is because we've pushed the
[03:53:05] changes to our dev branch. So, for them
[03:53:09] to show up on Vercel, we first have to
[03:53:10] push them over to the main branch by
[03:53:13] creating a new PR.
[03:53:16] And in this case, there were so many
[03:53:17] changes that we've done, most of which
[03:53:19] are actually agent skills that we
[03:53:22] installed. So, there's going to be 1.7
[03:53:24] million lines of code to review. In this
[03:53:27] case, what I'm going to do just to get
[03:53:29] it deployed is I will first fix the
[03:53:32] conflict we have with Copilot. I'll just
[03:53:35] tell it to completely remove the current
[03:53:38] issues.md file,
[03:53:41] which should fix the conflict,
[03:53:42] obviously.
[03:53:44] That's because we're hoping not to have
[03:53:46] any more issues. It's going to look into
[03:53:48] it and start implementing it right away.
[03:53:51] And as soon as it has been removed, we
[03:53:53] are ready to merge the PR,
[03:53:55] which means that the latest changes
[03:53:57] under the Ghost AI project should be
[03:53:59] reflected momentarily. And after a
[03:54:02] reload, they say just now. So, we can go
[03:54:05] ahead and import it.
[03:54:07] And immediately add the environment
[03:54:10] variables by pasting all of them into
[03:54:12] this first key and value pair, and it'll
[03:54:14] automatically populate all of them. So,
[03:54:17] go ahead and scroll down and click
[03:54:19] deploy.
[03:54:20] Now, we've implemented so many
[03:54:22] individual features within this
[03:54:24] application,
[03:54:25] integrated and wired up so many services
[03:54:28] across front-end and back-end and Prisma
[03:54:30] databases.
[03:54:32] It would be a miracle if it worked first
[03:54:34] try. So, just as I said that, in about 8
[03:54:37] seconds, the initial build failed saying
[03:54:40] that we can find a full log right here.
[03:54:43] So, I'll go ahead and inspect the
[03:54:44] deployment, and it looks like it just
[03:54:47] failed on running npm install.
[03:54:50] So, typically when we face an error this
[03:54:52] early with the npm install, most likely
[03:54:55] culprit is going to be the
[03:54:57] package-lock.json.
[03:54:59] So, what I like to do in this situation
[03:55:01] is just make sure that we are on the
[03:55:04] main branch, and we are, and want to
[03:55:07] delete the package-lock.json entirely,
[03:55:10] and then push to the main without it by
[03:55:12] running git add dot, git commit {dash} m
[03:55:15] remove package-lock.json,
[03:55:19] and want to get push.
[03:55:21] This is going to push it straight over
[03:55:22] to main, which means that it should
[03:55:24] automatically re-trigger another
[03:55:26] deployment. And this time, it is
[03:55:28] building past second eight, successfully
[03:55:32] installing the dependencies. So, this
[03:55:33] time we've gotten a bit further, but it
[03:55:36] still breaks right here on Prisma.
[03:55:39] Uh this is a typical procedure. Whenever
[03:55:41] you're publishing a Next.js project on
[03:55:44] Vercel with Prisma, you also have to add
[03:55:47] an additional script to the
[03:55:49] package.json.
[03:55:50] That's going to be right here.
[03:55:52] Right after lint, go ahead and add a
[03:55:55] post
[03:55:56] install script where you can run Prisma
[03:56:00] generate. So, once again, you can make
[03:56:03] that change
[03:56:04] and push it over to the main branch.
[03:56:08] As I told you, it's going to be unlikely
[03:56:10] that the build is going to succeed from
[03:56:12] the first try. As we've been developing
[03:56:14] this project for so long locally and in
[03:56:17] development version, and now we want to
[03:56:19] run it in production.
[03:56:21] But, don't worry, we're going to get
[03:56:22] there. And third time's the charm
[03:56:25] because the status is now ready and we
[03:56:27] are live. So, go to the project overview
[03:56:31] and visit your URL, which brings us back
[03:56:34] to our auth and home page at the same
[03:56:36] time, where after you sign in, you are
[03:56:39] redirected to an empty project screen or
[03:56:42] since we already logged in with the same
[03:56:44] account, you can find all of your
[03:56:45] previous projects. This means that
[03:56:48] everything is working exactly as it's
[03:56:50] supposed to, even on the deployed
[03:56:52] version of the application. So,
[03:56:54] congrats.
[03:56:55] This was a long build and quite a
[03:56:58] different one from the typical ones
[03:57:00] where we manually code everything out.
[03:57:02] So, I want to hear from you.
[03:57:04] How did you like this new approach?
[03:57:06] Would you like to dive even deeper
[03:57:08] within the Agenty course that I'm
[03:57:10] working on?
[03:57:11] If so, you can join the waitlist. And if
[03:57:13] you haven't already, also go ahead and
[03:57:15] download that six-file contact system
[03:57:17] for Agenty development that I prepared
[03:57:19] for you alongside this video. That way,
[03:57:22] you can use the same system we followed
[03:57:24] along with this build and implement it
[03:57:27] with your future builds. And yeah, huge
[03:57:29] thanks to Trigger for amazing background
[03:57:32] tasks and AI agent functionalities that
[03:57:35] they allow you to add to your app. Also,
[03:57:37] huge thanks to Liveblocks for allowing
[03:57:39] us to make our applications interactive.
[03:57:42] And finally, to Clerk for simplifying
[03:57:44] authentication and user management.
[03:57:47] Thank you not only for sponsoring this
[03:57:49] video, but for developing such amazing
[03:57:51] developer tools that I get to share with
[03:57:54] you guys watching this video.
[03:57:56] That was it for this one. I'll see you
[03:57:58] within jsmastey.com
[03:58:00] or if not there, within one of the
[03:58:03] upcoming videos on the YouTube channel.
[03:58:05] Once again, thank you for watching and
[03:58:08] have a wonderful day.
