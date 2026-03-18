# Ayako Discord Bot — Comprehensive Product & Market Analysis Report

## Executive Summary

Ayako is an enterprise-grade, open-source Discord bot built with TypeScript and discord.js v14, designed to serve as an all-in-one server management and community engagement platform. The bot currently operates across thousands of Discord servers through a hybrid sharding architecture backed by PostgreSQL and Redis. Despite its technical sophistication and extensive feature set (34+ slash commands, 71+ RP actions, 250+ event handlers, 46+ database tables), Ayako faces the universal challenge of Discord bot adoption: standing out in an oversaturated market where users can choose from Dyno, MEE6, Carl-bot, YAGPDB, Arcane, and hundreds of alternatives.

This report examines Ayako's feature landscape, competitive positioning, technical architecture, and community reception to inform strategic decisions about feature investment, marketing, and growth.

---

## Part 1: Feature Inventory

### 1.1 Core Moderation Suite
Ayako's moderation system is its most fully-developed pillar. It includes:

- **Punishment Types**: Ban, unban, kick, mute (temp/permanent), soft-ban, temp-ban, warn, soft-warn, strike, channel ban, temp channel ban, voice mute/deafen
- **Pardon System**: Revoke specific punishments, pardon by date range, pardon by executor, bulk pardons
- **Appeals Workflow**: Custom appeal forms with configurable questions, accept/reject with tracking
- **Punishment History**: Fully searchable and editable audit trail
- **Message Clearing**: Bulk delete with advanced filters (by user, content type, media, links, mentions, bots)
- **Slowmode Management**: Per-channel configuration
- **Permissions Control**: Fine-grained moderation command visibility

Compared to competitors: Ayako's pardon system and appeals workflow are more sophisticated than most competitors. MEE6 and Dyno offer basic moderation but lack Ayako's pardon-by-executor and configurable appeal forms. Carl-bot is the closest competitor in moderation depth.

### 1.2 Security & Anti-Abuse
- **Anti-Spam**: Configurable message frequency detection
- **Anti-Raid**: Mass-join attack detection and prevention
- **Anti-Virus**: Malicious link detection via FishFish API + Sinking Yachts phishing database
- **Invite Filtering**: Block unauthorized Discord server invites
- **Word Censor**: Rule-based content filtering with denylist
- **Newline Limiter**: Prevent visual spam via excessive newlines
- **Verification**: Captcha-based member verification with role assignment
- **Auto-Punish**: Consistent automatic punishment rules

### 1.3 Leveling & Progression
- **Multiple XP Formulas**: Polynomial, exponential, logarithmic, quadratic, cubic, linear
- **Activity Tracking**: Separate message XP and voice channel XP
- **Per-Channel and Per-Role Multipliers**: Different XP rates by channel or role
- **Level Rewards**: Auto-grant roles at milestones
- **Leaderboards**: Server, global, channel-specific, and nitro booster rankings
- **Visual Rank Cards**: Image-based rank display via Canvas rendering

### 1.4 Role Management
- **Auto-Roles**: Automatic assignment on member join
- **Self-Roles**: User-selectable via command
- **Reaction-Roles**: Role assignment via Discord reactions
- **Button-Roles**: Role assignment via Discord buttons
- **Custom Roles**: User-created roles with color (solid/gradient/holographic), icons, and sharing
- **Sticky Roles**: Persist roles across leave/rejoin cycles
- **Sticky Permissions**: Preserve channel permissions across rejoin
- **Role Separators**: Visual category organization in role lists
- **Nitro Rewards**: Booster-specific roles
- **Shop System**: Currency-based role purchasing

### 1.5 Logging & Audit Trail
Comprehensive event logging covering: moderation actions, message edits/deletes, member joins/leaves, role changes, channel modifications, voice events, and server-level updates. All delivered via webhook to designated log channels.

### 1.6 Ticketing / Support System
Ayako has a full-featured ticketing system for server support workflows:
- **Ticket Types**: DM-to-thread, DM-to-channel, thread-based, and channel-based tickets
- **Ticket Lifecycle**: Create, claim (staff assignment), close, delete
- **DM Tickets**: Users can open tickets via DM — messages are relayed to a staff-visible thread/channel
- **Blacklisting**: Block specific users or roles from creating tickets
- **Logging**: All ticket actions (create, claim, close) logged to designated channels
- **Archive Management**: Closed tickets can be moved to an archive category
- **Auto-Close**: Inactive tickets automatically closed by the bot
- **User Info Embed**: Staff see a user info card when a ticket is opened
- **Message Prefixes**: Configurable reply prefixes for staff responses
- **Duplicate Prevention**: Users can only have one open ticket at a time

This puts Ayako on par with dedicated ticketing bots like Ticket Tool, and ahead of MEE6/Dyno which lack ticketing entirely.

### 1.7 Community Engagement
- **Welcome System**: Customizable messages with dynamic variables, images, and animated GIFs
- **Giveaway Management**: Timed giveaways with role requirements, fair selection, reroll, claim timeout
- **Suggestion System**: User submission, community voting, moderator approval workflow
- **Vote-Punish**: Community-driven moderation voting
- **AFK System**: Auto-response when mentioned while away
- **Reminder System**: User-set reminders with flexible timing
- **Currency & Economy**: Per-guild currency with balance tracking and shop integration
- **Disboard Integration**: Bump reminders and streak tracking

### 1.8 Fun & Social
- **Anime Images**: 12+ categories (neko, waifu, husbando, kitsune, shinobu, megumin, etc.)
- **Roleplay Actions**: 71+ interactive button-based actions (hug, pat, kiss, slap, cuddle, dance, etc.)
- **Block System**: Users can block RP interactions from specific users
- **Seasonal Events**: Snowball collection, throwing, leaderboards

### 1.9 Utility
- **Info Commands**: User, server, role, channel, emoji, sticker, bot, invite details
- **Embed Builder**: Visual embed creation with templates
- **Sticky Messages**: Auto-reposting pinned messages
- **Voice Hubs**: Dynamic voice channel creation and management
- **View Raw**: Display raw message/embed content

---

## Part 2: Technical Architecture

### Infrastructure
- **Language**: TypeScript compiled with SWC
- **Framework**: discord.js v14.25.1
- **Scaling**: discord-hybrid-sharding v3.0.1
- **Database**: PostgreSQL with Prisma ORM v6.18
- **Cache**: Redis via ioredis
- **Image Generation**: Canvas v3.2.1
- **Monitoring**: Prometheus metrics
- **Deployment**: Docker + Nirn Proxy for HTTP routing
- **Runtime**: Node.js v24+

### Monorepo Structure
The project is organized as a monorepo with 8+ packages:
- Bot (main application)
- API (REST endpoints)
- Database (Prisma schema)
- Gateway (Discord gateway handler)
- Service (core service plugins)
- Utility (shared functions)
- CDN (content delivery)
- Website (web dashboard)

---

## Part 3: Competitive Landscape

### Top Competitors by Feature Overlap

| Feature Area | MEE6 | Dyno | Carl-bot | YAGPDB | Arcane | Ayako |
|---|---|---|---|---|---|---|
| Moderation | Good | Good | Excellent | Excellent | Basic | Excellent |
| Leveling | Good (paid) | Good (paid) | None | Basic | Excellent | Good |
| Auto-Roles | Good | Good | Excellent | Good | Good | Excellent |
| Custom Roles | None | None | None | None | None | Excellent |
| Logging | Basic | Good | Excellent | Good | Basic | Good |
| Fun/RP | None | None | None | None | None | Excellent |
| Giveaways | Good | Good | None | Basic (CC) | None | Good |
| Ticketing | None | Good (paid) | None | None | None | Excellent |
| Anti-Raid | Basic | Basic | Good | Good | Basic | Good |
| Dashboard | Excellent | Excellent | Good | Good | Good | In Development |
| Pricing | Freemium ($12/mo) | Freemium ($5/mo) | Freemium ($8/mo) | Free | Freemium | Free |

*Note: "(paid)" = feature exists but requires premium subscription. "(CC)" = available via custom commands, not built-in.*

### Key Competitive Advantages of Ayako
1. **Completely free** — no premium tier, no paywalled features
2. **Custom roles with gradients and holographic effects** — unique in market
3. **Most extensive RP/action system** — 71+ actions, popular in anime/social communities
4. **Appeals workflow** — rare among competitors
5. **Multiple leveling formulas** — unprecedented flexibility

### Key Competitive Disadvantages
1. **No web dashboard** (website package exists but appears early-stage) — every major competitor has one; this is the single biggest UX gap
2. **Lower brand recognition** than MEE6/Dyno/Carl-bot
3. **Documentation may be limited** for non-technical server owners
4. **No music features** — a common reason servers invite bots
5. **Setup complexity** — 34+ commands with deep configuration trees may overwhelm new admins; no setup wizard or onboarding flow

---

## Part 4: Bot Discovery Ecosystem

### How Server Admins Find Bots
1. **Bot listing sites**: top.gg (dominant), discord.bots.gg, discordbotlist.com, discords.com
2. **Word of mouth**: Staff from other servers recommending bots
3. **Discord server directories**: Template servers pre-configured with bots
4. **YouTube/TikTok tutorials**: "Best Discord Bots 2025" videos drive massive adoption
5. **Reddit communities**: r/discordapp, r/Discord_Bots, specific community subreddits
6. **Twitter/X**: Bot announcements, feature showcases
7. **Organic discovery**: Seeing bot features in other servers and asking "what bot is that?"

### Ayako's Current Listing Presence
Registered on 6 bot listing platforms: top.gg, discord.bots.gg, discordbotlist.com, discords.com, infinitybots.gg, botlist.me. Has vote tracking and rewards integration with top.gg.

---

## Part 5: Real User Sentiment — Evidence from Community Sources (2024-2026)

*Sources: Reddit (r/discordapp, r/Discord_Bots), Discord Support community posts, top.gg/Trustpilot reviews, Latenode Community forums, Dark Gaming forums, GitHub discussions, DEV Community. Industry marketing blogs deliberately excluded.*

### What Makes Users UNINVITE a Bot (Ordered by Severity)

**1. Paywalling previously free features** (THE #1 complaint across all sources)
MEE6 is the case study. XP role rewards, reaction roles, and custom commands were moved behind $11.99/mo. Users describe discovering they "have to pay for half the functions after already setting up the entire thing." A former MEE6 volunteer (ZRunner) published a GitHub doc describing how the support team spent two years explaining paywalled XP features to angry users. An entire website (alternativestomee6.com) and a GitHub repo (DodoGames7/stop-using-mee6) exist solely to catalog reasons not to use it. MEE6's $150 NFT "Genesis Pass" promotion caused mass departures — users called it "predating on oblivious people, especially teens." MEE6 was subsequently hacked via its NFT infrastructure, compromising multiple servers.

**2. Unsolicited DMs and spam behavior** (Widespread)
Bots sending DM advertisements is a major uninvite trigger. Server owners with ~3,000 users report DM spam bots hitting members daily despite countermeasures. Large servers report banning ~50 bot accounts in a single day. Server owners have requested "server-side DM settings" for years with no Discord response.

**3. Bot reliability failures** (Common)
The Groovy/Rythm music bot shutdowns (2021) left lasting trauma — users now worry about any bot suddenly disappearing. Tickets bot was discontinued March 2025, forcing emergency migration. Bots hosted on free tiers suffer sleep/restart issues. Once servers exceed ~1,000 users, rate limits and crashes become frequent.

**4. Security compromise** (Growing concern)
A documented case (NITRONOMICS 2025) shows a 5,000+ member server destroyed by a single compromised bot token with outdated permissions. When bots are kicked, their managed roles remain and cannot be deleted — a persistent UX frustration.

### What Makes Users INVITE a Bot (Ordered by Frequency in Discussions)

1. **Moderation automation** — keyword blocking, spam filtering, raid protection (Dyno for ease, YAGPDB for depth)
2. **Role management** — reaction roles, auto-roles (Carl-bot overwhelmingly wins; YAGPDB recommended most on Reddit)
3. **Entertainment and engagement** — games, economy, character collection, RP
4. **Welcome/onboarding automation**
5. **XP/leveling without paywalls** — Arcane and free alternatives gain traction specifically as "not MEE6"
6. **Music playback** — split between Hydra, Jockie Music, FredBoat post-Groovy era
7. **Ticketing/support** — but users want simple setup, not enterprise-grade complexity

### The Top Frustrations Users Actually Report

**1. Permission system complexity** (Universal)
"The most confusing part of server management." Multi-layer permissions (server > category > channel) stack in confusing ways. The most common advice is "just give admin" — which creates security risks. Bots fail silently when their role is below what they're trying to manage.

**2. Slash command problems** (Widespread)
Commands not appearing due to permission inconsistencies. 50-command limit per bot is insufficient for multi-purpose bots. Servers with ~30 bots create an unusable command list. Users describe slash commands as "slow and confusing" compared to old prefix commands.

**3. Reaction role breakage** (Common)
99% of failures come from role hierarchy positioning, but error messaging is poor. Discord updates break reaction roles — bots lose permissions, emojis vanish if deleted from source servers. The 250-role server limit causes silent failures.

**4. Automod false positives** (Common)
Wildcard matching catches innocent content. Bots "aren't great at understanding context or intent." Users report being permanently banned from their own servers for posting memes. Human review is still needed but bots auto-punish before review happens.

**5. Onboarding/verification conflicts** (Common)
Discord's native onboarding conflicts with verification bots (requires 5 channels with @everyone write access, breaking security). Wall-of-text welcome messages cause new members to leave. DM-based verification fails for users with DMs disabled. 92% of users reportedly dislike being redirected to external websites for verification.

**6. Bot bloat** (Growing — directly relevant to Ayako's positioning)
Too many bots cause command conflicts and cluttered UX. "A good moderation bot does one thing exceptionally well: keeps your server safe. Everything else is feature bloat." BUT the counter-trend is also real: users want one bot to replace several, reducing total bot count. This tension favors comprehensive bots like Ayako IF the UX is clean.

### What Features Users Actually ASK FOR (vs. What Tech Blogs Push)

**What tech blogs push:** AI chatbots, AI moderation, AI image generation, AI everything.

**What users in community discussions actually request:**
1. Better spam/raid protection that doesn't require external sites or complex setup
2. Reaction roles that reliably work without hierarchy headaches
3. XP/leveling without paywalls
4. Ticket systems that don't require enterprise-level setup for small servers
5. Giveaway bots they can trust (rigging concerns and scam bots erode trust)
6. Server-side DM controls (prevent bots from DMing members)
7. Bot-managed role cleanup after kicking bots
8. One bot to replace several — reducing total bot count per server
9. Proxying/identity-switching natively (Tupperbox/PluralKit functionality for RP and plural communities)

### What Anime/RP/Social Community Owners Specifically Want

**Character collection bots are near-mandatory for anime servers:**
- Mudae (140,000 character database) and Karuta are described as "almost mandatory." WaifuGame is growing with monthly events.

**Roleplay identity tools are essential:**
- Tupperbox and PluralKit allow sending messages as different characters with separate avatars/names. Users call Tupperbox "extremely unique and unlike anything else." Both communities have requested Discord build proxying as a native feature.

**Social engagement expectations:**
- Quest systems that encourage "meaningful engagement" rather than message spam for XP
- Economy bots: UnbelievaBoat for "peaceful" communities, Dank Memer for chaotic/meme servers. Key warning: "gambling and stealing mechanics can cause drama"
- No single bot combines character collection + RP identity switching + social engagement well

### How Users Feel About Pricing

**The consensus is clear:**
- Free is expected for testing and small servers
- $2-5/mo is acceptable for well-maintained bots in production
- $12/mo (MEE6) is considered predatory, especially when features were previously free
- Users respect bots that offer everything free with optional cosmetic/convenience premiums
- "Nitro + server boosts + bot subscriptions + external storage often approaches the price of dedicated business communication tools"
- Ayako's completely-free model is a genuine competitive advantage that should be marketed aggressively

### The AI Question — Evidence-Based Assessment

**The tech industry narrative frames AI as an inevitable "entry ticket." Real Discord community evidence contradicts this:**

- Discord's own AI bot (Clyde) shut down after 8 months — jailbreaking, inappropriate responses, widespread backlash. Many users were relieved.
- Discord banned 100,000+ AI bots from Shapes.inc in 2025 for policy violations
- Anthropic's Claude bot was restricted to a single channel by community vote after dominating conversations
- AI agents on Discord were found to leak private information and take "unintended destructive actions"
- Users organized petitions against Discord pushing AI features without consent
- Dyno and Carl-bot thrive in 2026 without any AI features
- Ayako's core audience (anime/RP/creative communities) skews anti-AI

**Where AI has narrow real value:** Behind-the-scenes spam detection and moderation automation for very large servers. NOT user-facing chatbot features.

**For Ayako specifically:** Pushing AI integration could alienate the core user base. The web dashboard, setup wizard, and reliability improvements are far more justified investments.

### Discord Platform Trust Context (2026)

Discord's broader trust environment affects all bots:
- February 2026 age verification announcement triggered mass Nitro cancellations
- 70,000 government ID images from Discord's third-party vendor (Persona) were found publicly accessible
- Discord delayed global age verification rollout to late 2026 after backlash
- Users describe Discord as having "became a soulless greedy cash grab" post-2023
- This general distrust makes users MORE skeptical of bots, MORE sensitive to permission requests, and MORE likely to prefer bots with transparent, free, open-source models — which benefits Ayako

---

## Part 6: Growth Metrics & Challenges

### Current Growth Channels
- Bot listing site votes (top.gg integration active)
- Disboard bump reminders (indirect — helps servers grow, which increases Ayako's visibility)
- Organic discovery via RP commands (users see fun interactions and ask about the bot)

### Bot Discovery Ecosystem — Real User Experience
The bot discovery experience is fragmented and trust-challenged:
- **top.gg dominates** but has major problems: 6-7 outages/month, lost votes, extremely slow bot review process (~1,000 bots in queue, some waiting 4+ months). Trustpilot reviews reflect frustration.
- **No official Discord bot store** exists — users must navigate third-party listing sites, creating trust concerns.
- **YouTube/TikTok "Best Bots" videos** drive massive adoption — bots featured in top-10 videos see significant server spikes.
- **Word of mouth** remains the most trusted channel — staff from other servers recommending bots.
- **Organic discovery** — seeing a bot's features in another server and asking "what bot is that?" — is how many small server admins find bots.

### Growth Bottlenecks
1. **No web dashboard**: Every major competitor has one. This is the single biggest UX gap. Users expect web-based configuration — typing commands to configure a bot feels outdated to most admins.
2. **Setup friction**: Permission configuration is the #1 stumbling block for new bot users across the ecosystem. Multi-layer permissions fail silently. No setup wizard or guided onboarding exists for Ayako.
3. **No viral mechanic**: Unlike bots with shareable features (custom welcome images posted publicly, rank cards shared in chat), Ayako's best features are admin-facing and invisible to regular users.
4. **Lower brand recognition**: MEE6 (21.3M servers), Dyno, and Carl-bot have name recognition. Ayako does not.
5. **Bot listing site bottleneck**: top.gg's slow review process and outages limit discoverability. Ayako is on 6 platforms but may not rank well on any.
6. **No referral or recommendation mechanic**: No incentive for admins who love Ayako to recommend it to other admins.
7. **The "all-in-one" paradox**: Users want fewer bots, but also fear feature bloat. Ayako must solve the UX problem of being comprehensive without feeling overwhelming.

---

## Part 7: Community Archetypes — Based on Real User Discussions

### Who Uses Discord Bots and What Do They Actually Do?

**Discord now has ~259M monthly active users (2025), 30M+ servers, 1.1B daily messages. 54% of Discord users are now non-gamers.** This fundamentally changes the bot market — bots can no longer assume a gaming-only audience.

1. **Small Server Admins (10-100 members)**: Teenagers or young adults running friend groups, gaming guilds, or study groups. Want simple setup — "anyone can make a Discord server in minutes; few know how to set it up professionally." Give up easily when bots fail silently due to permissions. Default to giving bots Administrator permission because granular setup is too hard. Price-sensitive: $0 is the expected price point. Most likely to discover bots via YouTube "best bots" videos.

2. **Medium Server Admins (100-5,000 members)**: Community managers for content creators, game communities, or hobby groups. Willing to invest time in configuration but frustrated by poor documentation. This is where bot consolidation pressure peaks — they want one bot to replace 3-4 specialized ones but fear losing reliability. Most likely to switch bots after a bad experience (paywall, outage, security incident).

3. **Large Server Admins (5,000-100,000+ members)**: Dedicated moderation teams. Need enterprise-grade reliability and advanced anti-raid. A single compromised bot token has been documented destroying a 5,000+ member server. Require at least two staff members trained on bot management. DM spam is a "HUGE problem that hurts Discord server owners in a real and impactful way" at this scale — ~50 bot accounts banned daily in large servers. Most likely to pay for premium features.

4. **Anime/Social Community Leaders** (Ayako's core demographic): Character collection (Mudae/Karuta) is near-mandatory. RP identity switching (Tupperbox/PluralKit) is essential. Economy bots wanted but "gambling and stealing mechanics can cause drama." Custom roles with visual flair (colors, gradients, icons) are a status symbol. Quest systems that reward meaningful engagement > spam for XP. Tend to skew anti-AI. Want bots that understand their community's culture.

5. **Gaming Community Leaders**: Want leveling, giveaways, voice channel management. Post-Groovy/Rythm, music is a persistent need with no dominant solution. Competitive communities want leaderboards and seasonal events.

6. **Content Creator Managers**: Need welcome messages, role management, member tracking. Fan communities are the fastest-growing Discord segment. Subscription/tier management (linking Patreon/YouTube membership to Discord roles) is increasingly requested.

7. **Moderators** (distinct from admins): Struggle with automod false positives — "bots aren't great at understanding context or intent." Burn out from scale — "same questions repeatedly." Level-up spam disrupts chats and users can't opt out. Need better tools for contextual moderation, not just keyword matching. When a bot is discontinued (like Tickets in March 2025), emergency migration falls entirely on them.

7. **Casual Users (Non-Admins)**: Interact with bot commands in servers. Care about fun features, responsiveness, and visual quality. Their enthusiasm drives organic recommendation.
