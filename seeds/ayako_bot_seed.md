# Ayako Discord Bot — Comprehensive Product & Market Analysis Report

## Executive Summary

Ayako is an enterprise-grade, open-source Discord bot built with TypeScript and discord.js v14, designed to serve as an all-in-one server management and community engagement platform. The bot currently operates across 8,026 servers reaching 2,470,970 users through a hybrid sharding architecture backed by PostgreSQL (73 tables) and Redis. It is maintained by a single developer (Larsundso) based in Germany. Despite its technical sophistication and extensive feature set (34+ slash commands, 71+ RP actions, 250+ event handlers, 55+ settings commands), Ayako faces the universal challenge of Discord bot adoption: standing out in an oversaturated market where users can choose from Dyno, MEE6, Carl-bot, YAGPDB, Arcane, and hundreds of alternatives.

Ayako's strongest differentiator is that it is **completely free** — no premium tier, no paywalled features — in a market where the dominant bot (MEE6) is widely hated for predatory monetization. It also has several features no competitor offers: white-label custom client, vote punishment, ping reporter, 6 XP formulas with visual graphs, 14-metric leveling analytics, and a community art gallery.

This report examines Ayako's feature landscape, competitive positioning, real user sentiment, technical architecture, online presence, and growth challenges to inform strategic decisions.

---

## Part 1: Feature Inventory

### 1.1 Core Moderation Suite
Ayako's moderation system is its most fully-developed pillar. It includes:

- **Punishment Types**: Ban, unban, kick, mute (temp/permanent), soft-ban, temp-ban, warn, soft-warn, strike, channel ban, temp channel ban, voice mute/deafen
- **Pardon System**: Revoke specific punishments, pardon by date range, pardon by executor, bulk pardons
- **Appeals Workflow**: Custom appeal forms with configurable questions (6 question types: paragraph, short text, number, boolean, single-choice, multi-choice), reviewer voting, full web-based workflow at ayakobot.com
- **Punishment History**: Fully searchable and editable audit trail
- **Message Clearing**: Bulk delete with advanced filters (by user, content type, media, links, mentions, bots)
- **Slowmode Management**: Per-channel configuration
- **Permissions Control**: Fine-grained moderation command visibility
- **Auto-Punish**: Strike system with configurable escalation and punishment expiry

Compared to competitors: Ayako's pardon system, dynamic appeals, and vote punishment are more sophisticated than any competitor. Carl-bot is the closest in moderation depth but lacks appeals and community voting.

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
- **6 XP Formulas**: Polynomial, exponential, logarithmic, quadratic, cubic, linear — with ECharts Canvas-generated comparison charts (800x500px, dark theme)
- **Activity Tracking**: Separate message XP and voice channel XP
- **14-Metric Per-Channel Analytics**: Tracks character count, word count, attachment count, user/channel/role mention counts, link count, emote usage. Allows conditional XP rules ("Only count messages with 10+ words in #general")
- **Per-Channel and Per-Role Multipliers**: Different XP rates by channel or role
- **Level Rewards**: Auto-grant roles at milestones
- **Leaderboards**: Server, global, channel-specific, and nitro booster rankings
- **Visual Rank Cards**: Image-based rank display via Canvas rendering
- **Duplicate Message Detection**: Uses string-similarity library to deny XP for repeated/similar messages
- **Less Intrusive Level-Ups**: Configurable notification modes (silent, message, reaction)

### 1.4 Role Management
- **Auto-Roles**: Automatic assignment on member join (separate for bots vs users)
- **Self-Roles**: User-selectable via command
- **Reaction-Roles**: Role assignment via Discord reactions
- **Button-Roles**: Role assignment via Discord buttons
- **Custom Roles**: User-created roles with color (solid/gradient/holographic), icons, and sharing — **unique in market, valued as status symbols**
- **Sticky Roles**: Persist roles across leave/rejoin cycles
- **Sticky Permissions**: Preserve channel permissions across rejoin
- **Role Separators**: Visual category organization in role lists
- **Nitro Rewards**: Booster-specific roles and leaderboard
- **Role Rewards**: Grant currency/XP multiplier when user gets role
- **Shop System**: Currency-based role purchasing
- **Ping Reporter**: Detects role mentions and notifies members who weren't pinged — **unique feature**
- **Linked Roles**: Discord verified credentials integration

### 1.5 Logging & Audit Trail
Comprehensive event logging covering 17+ categories: moderation actions, message edits/deletes, member joins/leaves, role changes, channel modifications, voice events, server-level updates, applications, auto-mod, scheduled events, invites, stages, stickers, typing, webhooks, reactions. All delivered via webhook to designated log channels. Hierarchical descriptions with block quotes showing who did what, before/after change tracking, color-coded by action type.

### 1.6 Ticketing / Support System
Full-featured ticketing system with 4 modes (most competitors offer 1-2):
- **DM-to-Thread**: Users open tickets via DM, relayed to a staff-visible thread
- **DM-to-Channel**: Users open tickets via DM, relayed to a dedicated channel
- **Thread-based**: Tickets created as private threads
- **Channel-based**: Tickets created as channels with permission overrides
- **Ticket Lifecycle**: Create, claim (staff assignment), close, delete
- **Blacklisting**: Block specific users or roles from creating tickets
- **Logging**: All ticket actions logged to designated channels
- **Archive Management**: Closed tickets moved to archive category
- **Auto-Close**: Inactive tickets automatically closed
- **User Info Embed**: Staff see user info card when ticket opens
- **Message Prefixes**: Configurable reply prefixes for staff responses
- **Duplicate Prevention**: One open ticket per user

### 1.7 Community Engagement
- **Welcome System**: Customizable messages with dynamic variables, images, and animated GIFs
- **Giveaway Management**: Timed giveaways with role requirements, fair selection, reroll, claim timeout, auto-payout, auto-reroll if unclaimed
- **Suggestion System**: User submission, community voting, moderator approval workflow
- **Vote-Punish**: Community-driven moderation — members nominate problematic users, voting phase runs (requiring X votes from specific roles), automatic punishment executes. **No major competitor has this.**
- **AFK System**: Auto-response when mentioned while away
- **Reminder System**: User-set reminders with flexible timing
- **Currency & Economy**: Per-guild currency with balance tracking and shop integration
- **Disboard Integration**: Bump reminders and streak tracking
- **Vote Rewards**: top.gg voting integration with reward system
- **Seasonal Events**: Snowball collection, throwing, leaderboards

### 1.8 Fun & Social
- **Anime Images**: 12+ categories (neko, waifu, husbando, kitsune, shinobu, megumin, etc.)
- **Roleplay Actions**: 71+ interactive button-based actions (hug, pat, kiss, slap, cuddle, dance, bonk, comfort, etc.) — displayed as embeds with anime GIFs, dynamic text based on targets, interactive reply buttons, footer shows source anime name
- **Block System**: Users can block RP interactions from specific users
- **Seasonal Events**: Snowball collection, throwing, leaderboards

### 1.9 Utility
- **Info Commands**: User, server, role, channel, emoji, sticker, bot, invite details — "Information even Discord doesn't show you"
- **Embed Builder**: Visual embed creation with templates, save/load
- **Sticky Messages**: Auto-reposting pinned messages
- **Voice Hubs**: Dynamic voice channel creation and management with member/manager roles
- **View Raw**: Display raw message/embed content

### 1.10 Custom Client / White-Label System
**Extremely unique — no major competitor offers this:**
Server admins can create their own Discord Application, provide the token to Ayako via `/settings custom-client`, and run a fully branded copy of Ayako under their own bot name. Ayako validates the token, registers all commands, and the custom bot runs with the full Ayako feature set. Enables communities to have "their own bot" without forking code. Enterprise-grade white-labeling.

---

## Part 2: Technical Architecture

### Infrastructure
- **Language**: TypeScript compiled with SWC
- **Framework**: discord.js v14.25.1
- **Scaling**: discord-hybrid-sharding v3.0.1
- **Database**: PostgreSQL with Prisma ORM v6.18 — **73 tables**
- **Cache**: Redis via ioredis
- **Image Generation**: Canvas v3.2.1, ECharts for XP formula charts
- **Monitoring**: Prometheus metrics
- **Deployment**: Docker + Nirn Proxy for HTTP routing
- **Runtime**: Node.js v24+
- **Event Handlers**: 84+ covering nearly every Discord event

### Monorepo Structure (16 repos)
- Bot (main application), API (Discord.js wrapper), Database (Prisma schema), Gateway (Discord gateway), Service (v3 microservices rewrite — in progress March 2026), Utility (shared functions), CDN (asset storage), Website (SvelteKit frontend), Server (SvelteKit API backend)

### Performance Optimizations
- String similarity check on messages (prevents XP spam)
- Cooldown layers: guild-wide, channel-specific, per-user
- Batch command registration
- Custom rate limit management per feature
- Scheduled jobs via node-schedule

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
| Dashboard | Excellent | Excellent | Good | Good | Good | Partial* |
| White-Label | None | None | None | None | None | Excellent |
| Vote Punishment | None | None | None | None | None | Unique |
| Pricing | Freemium ($12/mo) | Freemium ($5/mo) | Freemium ($8/mo) | Free | Freemium | Free |

*Note: "(paid)" = feature requires premium. "(CC)" = via custom commands. Ayako's website has leaderboards, appeals, art gallery, and login — but no web-based settings configuration dashboard.*

### Key Competitive Advantages of Ayako
1. **Completely free** — no premium tier, no paywalled features
2. **Custom roles with gradients and holographic effects** — unique in market, valued as status symbols
3. **Most extensive RP/action system** — 71+ actions, popular in anime/social communities
4. **White-label custom client** — enterprise-grade, no competitor offers this
5. **Vote punishment** — community-driven moderation, unique
6. **Dynamic appeals workflow** — 6 question types, reviewer voting, rare among competitors
7. **6 XP formulas with visual graphs** — unprecedented flexibility
8. **14-metric leveling analytics** — conditional XP rules no competitor matches
9. **4-mode ticketing** — most complete ticketing in a general-purpose bot

### Key Competitive Disadvantages
1. **No web-based settings dashboard** — the website exists for leaderboards/appeals/art, but server configuration requires slash commands. Every competitor has a settings dashboard. This is the #1 UX gap.
2. **Lower brand recognition** than MEE6 (21.3M servers), Dyno, Carl-bot
3. **No setup wizard or guided onboarding** — 55+ settings commands across 10 categories is powerful but overwhelming for new admins
4. **No music features** — a common reason servers invite bots
5. **Only 2 languages** (English, German) — limits international growth
6. **Solo developer** — limits development speed and support bandwidth

---

## Part 4: Bot Discovery Ecosystem

### How Server Admins Find Bots (ranked by trust)
1. **Word of mouth**: Staff from other servers recommending bots (most trusted)
2. **Organic discovery**: Seeing bot features in another server and asking "what bot is that?"
3. **YouTube/TikTok tutorials**: "Best Discord Bots 2025/2026" videos drive massive adoption spikes
4. **Bot listing sites**: top.gg (dominant but unreliable), discord.bots.gg, discordbotlist.com, others
5. **Reddit communities**: r/discordapp, r/Discord_Bots — skeptical, comparison-minded
6. **Discord server directories**: Template servers pre-configured with bots

### Bot Discovery Ecosystem — Real Problems
- **top.gg dominates** but has 6-7 outages/month, lost votes, extremely slow review process (~1,000 bots in queue, some waiting 4+ months). Trustpilot reviews reflect frustration.
- **No official Discord bot store** — trust concerns with third-party sites
- Admins respond by cross-referencing multiple listing sites before trusting a bot
- The discovery process is labor-intensive and fragmented

### Ayako's Current Listing Presence
Listed on **8 platforms**: Top.GG, Bots.gg, Discord Bot List, Wumpus Store, Discords.com, Rovelstars, Infinity Bots, Botlist.me. Has vote tracking and rewards integration with top.gg. **229 total votes, 14 reviews (all 5/5), 0 upvotes in current month — voting momentum has stalled.**

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

### What Makes Users INVITE a Bot (Ordered by Frequency)

1. **Moderation automation** — keyword blocking, spam filtering, raid protection
2. **Role management** — reaction roles, auto-roles (Carl-bot wins, YAGPDB recommended on Reddit)
3. **Entertainment and engagement** — games, economy, character collection, RP
4. **Welcome/onboarding automation**
5. **XP/leveling without paywalls** — Arcane and free alternatives gain traction as "not MEE6"
6. **Music playback** — split between Hydra, Jockie Music, FredBoat post-Groovy
7. **Ticketing/support** — users want simple setup, not enterprise complexity

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
Too many bots cause command conflicts and cluttered UX. "A good moderation bot does one thing exceptionally well." BUT the counter-trend is also real: users want one bot to replace several, reducing total bot count. This tension favors comprehensive bots like Ayako IF the UX is clean.

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
9. Proxying/identity-switching natively (Tupperbox/PluralKit for RP and plural communities)

### What Anime/RP/Social Community Owners Specifically Want

**Character collection bots are near-mandatory for anime servers:**
Mudae (140,000 character database) and Karuta are described as "almost mandatory." WaifuGame is growing with monthly events.

**Roleplay identity tools are essential:**
Tupperbox and PluralKit allow sending messages as different characters with separate avatars/names. Users call Tupperbox "extremely unique and unlike anything else." Both communities have requested Discord build proxying as a native feature.

**Social engagement expectations:**
- Quest systems that encourage "meaningful engagement" rather than message spam for XP
- Economy bots: UnbelievaBoat for "peaceful" communities, Dank Memer for chaotic/meme servers. Key warning: "gambling and stealing mechanics can cause drama"
- Custom visual roles (colors, gradients, icons) are status symbols
- No single bot combines character collection + RP identity switching + social engagement well

### How Users Feel About Pricing

- Free is expected for testing and small servers
- $2-5/mo is acceptable for well-maintained bots in production
- $12/mo (MEE6) is considered predatory, especially when features were previously free
- Users respect bots that offer everything free with optional cosmetic/convenience premiums
- "Nitro + server boosts + bot subscriptions + external storage often approaches the price of dedicated business communication tools"
- **Ayako's completely-free model is a genuine competitive advantage that should be marketed aggressively**

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
- This general distrust makes users MORE skeptical of bots, MORE sensitive to permission requests, and MORE likely to prefer bots with transparent, free, open-source models — **which directly benefits Ayako**
- Discord stats: ~259M monthly active users, 30M+ servers, 1.1B daily messages, 54% non-gamers

### What Moderators Specifically Struggle With

1. **Automod tuning** — balancing false positives vs missed violations, context/sarcasm beyond bot capability
2. **DM spam uncontrollable** — "HUGE problem that hurts server owners," ~50 bot accounts banned daily in large servers
3. **Compromised bot recovery** — single token compromise can destroy entire server, need 2+ staff trained on bots
4. **Scale burnout** — same questions repeatedly, manual handling doesn't scale
5. **Bot coordination overhead** — multiple bots with overlapping commands, no unified dashboard
6. **Bot discontinuation emergency** — Tickets bot died March 2025, migration fell on mods
7. **Level-up spam** disrupts chats, users can't opt out, XP systems incentivize shallow spam

---

## Part 6: Growth Metrics & Challenges

### Current Growth Channels
- Bot listing site votes (top.gg integration active, but 0 votes this month)
- Disboard bump reminders (indirect — helps servers grow, increasing Ayako's visibility)
- Organic discovery via RP commands and custom roles (users see features and ask about the bot)

### Growth Bottlenecks
1. **No web-based settings dashboard**: Every competitor has one. The website has leaderboards/appeals/art but not settings configuration. This is the single biggest UX gap.
2. **Setup friction**: Permission configuration is the #1 stumbling block across the ecosystem. No setup wizard or guided onboarding. 55+ settings commands across 10 categories is powerful but overwhelming.
3. **No viral mechanic beyond organic**: Custom roles and RP actions are passive advertisements, but there's no active referral or sharing system.
4. **Low brand recognition**: 8,026 servers vs MEE6's 21.3M. Solo developer can't match marketing spend.
5. **YouTube channel is empty**: Zero significant content on the single biggest discovery channel for medium server admins.
6. **Stalled voting momentum**: 0 upvotes this month on top.gg despite 229 total. No active campaign.
7. **The "all-in-one" paradox**: Users want fewer bots but fear feature bloat. Ayako must be comprehensive without feeling overwhelming.
8. **top.gg platform issues**: 6-7 outages/month, 4+ month review queues limit discoverability.

---

## Part 7: Community Archetypes — Based on Real User Discussions

**Discord now has ~259M monthly active users (2025), 30M+ servers, 1.1B daily messages. 54% of Discord users are now non-gamers.**

1. **Small Server Admins (10-100 members)**: Teenagers or young adults running friend groups, gaming guilds, or study groups. Want simple setup. Give up easily when bots fail silently. Default to giving bots Administrator permission because granular setup is too hard. Price-sensitive: $0 expected. Discover bots via YouTube videos.

2. **Medium Server Admins (100-5,000 members)**: Community managers for content creators, game communities, hobby groups. Want to consolidate bots (1 replacing 3-4). Frustrated by poor documentation. Most likely to switch bots after bad experience.

3. **Large Server Admins (5,000-100,000+ members)**: Dedicated moderation teams. Need enterprise reliability. Single compromised bot token can destroy a server. DM spam is daily (~50 bot accounts banned). Most likely to pay for premium features.

4. **Anime/Social Community Leaders** (Ayako's core demographic): Character collection (Mudae/Karuta) is near-mandatory. RP identity switching (Tupperbox/PluralKit) is essential. Custom visual roles are status symbols. Quest systems > spam-for-XP. Anti-AI sentiment. Want bots that understand their culture.

5. **Gaming Community Leaders**: Want leveling, giveaways, voice management. Post-Groovy/Rythm, music is a persistent need. Competitive communities want leaderboards and seasonal events.

6. **Content Creator Managers**: Need welcome messages, role management, member tracking. Fan communities are the fastest-growing Discord segment. Subscription/tier management increasingly requested.

7. **Moderators** (distinct from admins): Struggle with automod false positives. Burn out from scale. Level-up spam disrupts chats. Fear bot discontinuation. When a bot dies (Tickets, March 2025), migration falls on them.

8. **Casual Users (Non-Admins)**: Interact with bot commands in servers. Care about fun features, responsiveness, visual quality. Their enthusiasm drives organic recommendation.

---

## Part 8: Ayako's Online Presence & Brand

### Website (ayakobot.com)
Built with **SvelteKit 5 + Three.js + GSAP** — production-quality, not a stub. Features:
- **Interactive 3D home page** ("GardenExperience") with Three.js scene and GSAP animations
- **Tagline**: "A Discord bot that keeps communities cared for"
- **Meta description**: "Ayako is an all-in-one Discord bot for moderation, leveling, roles, events, and the day-to-day care of your server."
- **Stats displayed**: 8,026 guilds, 2,470,970 users, 5.0 rating from reviews
- **Navigation**: Invite, Support, Premium, Appeals, Art, Leaderboards, Creators, Animekos, API Docs, Log-In
- **40+ community server logos** with member counts (10k-259k) as social proof
- **User testimonial cards** with avatars
- **Design language**: Nature/garden theme — "Return to the garden" navigation, floating dandelion seed ambient animations, CSS variables named `--soil`, `--bark`, `--fog`, `--mist`, `--glow`, `--bloom`, `--water`. Dark theme with organic feel.
- **Donate page**: Patreon + PayPal + vote links to 8 bot listing sites. Copy: "Ayako is free and always will be."
- **Reference page**: Full character reference sheets — anime mascot with 6 variants (Kimono, Casual, Thoughtful, Cheerful, Stylish, Sleepy) with downloadable art
- **Artwork gallery**: Community-submitted fan art with type filtering (Full Art, Icons, Emojis) and search
- **Appeals system**: Full web-based appeals workflow — users log in, see punishments, submit custom forms
- **Leaderboards**: Per-server with visual podium for top 3
- **Legal pages**: Terms, Privacy, Credits

### Character/Mascot Identity
Ayako has a fully developed anime mascot character — not just a logo. Professional reference sheets with multiple outfits and expressions. Community art submissions mean users are emotionally invested in the character. This is a unique brand asset that resonates with the anime community target audience.

### Bot Listing Marketing Copy
On discordbotlist.com: "🤖 Ayako: Your Server's Best Friend 🤖 — Looking to make your server less boring, less manual, more unified, or add customization?" Features organized with emoji headers across 7 sections. Key differentiators highlighted: "Less intrusive Level-Ups", "Conditional XP Multipliers", "Logs about everything… literally" (17 categories).

### Top.gg Reviews (14 reviews, 5.0/5.0)
Notable quotes:
- "An amazing bot that deserves way more support, it keeps growing and the developer is very open to suggestions"
- "Ayako makes monke brain rush dopamine, seriously tho it's very versatile and easily configurable if you want a bot to fulfill all your needs in your server free of any charges"
- "Useful bot, cute waifu, hardworking dev, what more can you ask for?"
- Long-term user since February 2020 praising all-in-one capabilities
- Multiple reviews explicitly compare favorably to MEE6

**Common review themes**: Versatility, free pricing, responsive developer, comprehensive features. Setup difficulty noted but forgiven.

### GitHub Organization (github.com/orgs/AyakoBot)
- **16 repositories**, 1 member (Larsundso — solo developer, Germany)
- **Main repo**: 14 stars, 2 forks, 2,301 commits, TypeScript 99.6%
- **v3 microservices rewrite** in progress (March 2026)
- Contact: dev@ayakobot.com

### YouTube Channel (@AyakoBot)
Listed but has no significant content. **This is the single biggest missed growth opportunity** — YouTube "Best Discord Bots" videos are one of the top discovery mechanisms for bots.

---

## Part 9: Bot Visual Identity & UX

### Color System
- **Base**: `#b0ff00` (Lime Green) — default embed color for general messages
- **Danger**: `#ff0000` (Red) — bans, kicks, warns, destructive actions
- **Success**: `#00ff00` (Green) — unbans, unmutes, positive actions
- **Loading**: `#ffff00` (Yellow) — processing states
- **Ephemeral**: `#2b2d31` (Dark Gray) — system messages
- 150+ named colors available for customization (blurple, coral, darknavy, etc.)

### Embed Design Patterns
Consistent format: author+icon header, color-coded by action type, hierarchical descriptions using block quotes. Max 26 fields per embed with automatic pagination. Zero-width space characters for spacing. Footer guides users to support resources. Moderation actions include clickable appeal button linking to ayakobot.com.

### Error Handling UX
- Author: "Error" text with warning emote icon
- Color: Red (#ff0000)
- Always ephemeral (hidden from other users)
- Clean, simple presentation

### RP Action Display (71+ commands)
- Embed with anime GIF/image
- Dynamic text based on action and targets (solo: "@User bonks themself", multi: "@User bonks @Target1, @Target2")
- Interactive reply buttons below (Secondary style)
- Footer shows source anime name
- Users can block specific people from using RP on them

### Giveaway UX
- Author with custom love emote
- Title: participant count
- Prize description with winner count + end time
- Host footer with avatar
- Primary "Participate 🎁" button during giveaway
- "Claim Prize" button after end with timeout

### Language/Tone
Friendly and casual in social contexts ("monke brain rush dopamine"), playful in RP ("bonks themself, at least I didn't have to do it"), professional in moderation. Supports English and German (1000+ localization strings).

### Canvas-Generated Visuals
- XP formula comparison charts (ECharts, 800x500px, dark theme, 10-color palette, tooltips)
- Rank cards via Canvas rendering

---

## Part 10: Strategic Assessment

### Ayako's Actual Position
Ayako is a **technically superior, feature-rich, completely free** Discord bot that suffers from a **discovery and brand recognition problem**, not a feature problem. It has features no competitor offers, a professional website with 3D graphics, a beloved anime mascot with community fan art, and 100% positive reviews from everyone who finds it.

### The Core Tension
Built by a **solo developer** maintaining 16 repos, 73 database tables, 84 event handlers, and 8,000+ servers. The v3 microservices rewrite suggests awareness of scaling needs. The question isn't "what features to build" — it's "how to get discovered by the 99.99% of Discord server admins who've never heard of Ayako."

### What a Simulation Should Reveal
1. Which unique features (white-label, vote punishment, art gallery, 6 XP formulas, custom roles) have the most viral potential if marketed correctly
2. Whether "completely free" positioning alone can overcome MEE6/Dyno/Carl-bot brand recognition
3. What content (YouTube, social media, listing optimization) most efficiently reaches new admins
4. Whether the anime mascot identity helps or limits audience expansion beyond anime communities
5. How the solo developer constraint should shape prioritization — features vs. marketing vs. UX polish
6. Is the solo developer model sustainable at 50K+ servers, and what breaks first
