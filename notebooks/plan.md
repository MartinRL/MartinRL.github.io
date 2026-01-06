# Workshop Plan: Demystifying Agents, MCP, and Skills

## Meta
- **Format**: Polyglot Notebook (.dib) serving as slides + hands-on workshop
- **Duration**: 3.5 hours (210 minutes)
- **Audience**: .NET developers
- **Language**: C#
- **Domain**: EV charging
- **Tooling**: GitHub Copilot (supports MCP + Skills), VS Code, .NET 8+

## Learning Outcomes
Participants will:
1. Understand the architecture of agentic software engineering (2026 paradigm)
2. Build a working MCP server in C#
3. Create a reusable skill (works in Copilot + Claude Code)
4. Construct an "LLM in a loop with tools" agent
5. Connect all three components into a functioning system

---

## Workshop Structure

### Warm-up: Polyglot Notebooks 101 (10 min)
- What is a polyglot notebook? (.dib format, .NET Interactive kernel)
- Cell types: `#!markdown`, `#!csharp`, `#!meta`
- Running cells: Shift+Enter, cell output, state persistence
- **Mini-exercise**: Run a "Hello EV World" cell, declare a variable, reference it in next cell

---

### Opening (15 min)
**Theory**: The Agentic SWE Landscape
- From autocomplete to agents: the 2024-2026 evolution
- The convergence: code as universal interface
- Architecture overview: Agent Loop + Runtime + MCP + Skills
- Key insight from Anthropic: "Stop building agents, start building skills"

---

### Module 1: MCP Servers (50 min)

**Theory (15 min)**: Model Context Protocol
- What MCP solves: standardized tool/data connectivity for LLMs
- Protocol basics: JSON-RPC 2.0, stdio/SSE transport
- MCP server anatomy: Tools, Resources, Prompts
- C# SDK: `ModelContextProtocol` NuGet package

**Exercise 1 (35 min)**: Build an EV Charger Status Server
- Create minimal MCP server with one tool: `GetChargerStatus(chargerId)`
- Returns: availability, power output, current session info
- Boilerplate provided, participant implements tool logic
- Test with MCP Inspector

```csharp
// Skeleton provided:
[McpServerToolType]
public static class ChargerTools
{
    [McpServerTool, Description("Get real-time status of an EV charger")]
    public static ChargerStatus GetChargerStatus(string chargerId)
    {
        // TODO: Participant implements
    }
}
```

---

### Module 2: Skills (45 min)

**Theory (10 min)**: Agent Skills
- Skills = organized folders with procedural knowledge
- Progressive disclosure: metadata first, details on demand
- SKILL.md structure: YAML frontmatter + instructions
- Cross-platform: works in GitHub Copilot AND Claude Code
- Scripts as tools: Python/Bash/C# scripts the agent can execute

**Exercise 2 (35 min)**: Create an EV Charging Advisor Skill
- Build skill folder structure: `ev-charging-advisor/SKILL.md`
- Write YAML metadata with clear trigger description
- Add instructions for optimal charging recommendations
- Include reference script for tariff calculation
- Install and test in Copilot/Claude Code

```
ev-charging-advisor/
├── SKILL.md           # Core instructions
├── scripts/
│   └── calculate-cost.csx  # C# script for cost calculation
└── references/
    └── tariff-guide.md     # Loaded when needed
```

---

### Break (15 min)

---

### Module 3: Building an Agent (55 min)

**Theory (15 min)**: The Agentic Loop
- "LLM in a loop with tools" - demystified
- Tool use protocol: function calling → execution → result injection
- The loop: Prompt → LLM → Tool Call? → Execute → Append → Repeat
- When to stop: no more tool calls or max iterations
- Anthropic.SDK: `ToolCall`, `ToolResult`, conversation management

**Exercise 3 (40 min)**: Build an EV Charging Assistant Agent
- Implement agentic loop using Anthropic.SDK
- Define tools: `SearchChargers`, `GetChargerStatus`, `CalculateCost`
- Handle multi-turn tool execution
- Boilerplate provided, participant completes the loop logic

```csharp
// Core loop skeleton:
while (!done && iterations < maxIterations)
{
    var response = await client.Messages.CreateAsync(/* ... */);

    if (response.StopReason == "tool_use")
    {
        // TODO: Participant implements tool execution
        // 1. Extract tool calls from response
        // 2. Execute each tool
        // 3. Append tool results to conversation
    }
    else
    {
        done = true;
    }
}
```

---

### Module 4: Integration (30 min)

**Theory (5 min)**: Connecting the Pieces
- MCP provides connectivity (tools/data)
- Skills provide expertise (how to use tools well)
- Agent orchestrates everything
- The 2026 pattern: thin agent core + rich skill library + MCP ecosystem

**Exercise 4 (25 min)**: Wire It All Together
- Connect MCP server as tool provider to the agent
- Equip agent with the charging advisor skill's instructions
- Run end-to-end: user asks → agent reasons → calls MCP tools → applies skill knowledge → responds

---

### Closing (10 min)
- Recap: MCP = connectivity, Skills = expertise, Agent = orchestration
- What's next: skill marketplaces, MCP Apps, parallel agents
- Resources and community links

---

## Technical Requirements

### Packages
```xml
<PackageReference Include="Anthropic.SDK" Version="3.*" />
<PackageReference Include="ModelContextProtocol" Version="0.*" />
```

### Pre-built Assets Needed
1. Mock EV charger data (JSON with 5-10 chargers)
2. Tariff rate structure (peak/off-peak pricing)
3. MCP server boilerplate with hosting code
4. Agent loop skeleton with Anthropic client setup

---

## Notebook Cell Structure

Each module follows:
1. **Markdown**: Theory/concept explanation with diagrams
2. **Markdown**: Exercise instructions
3. **Code cell**: Boilerplate with TODO comments
4. **Code cell**: Solution (hidden/collapsed, for reference)
5. **Markdown**: Checkpoint - what you should see

---

## EV Charging Domain Context

**Scenario**: ChargeSmart - a fictional EV charging network
- 10 charging stations across a city
- Mix of slow (7kW), fast (50kW), ultra-fast (150kW) chargers
- Dynamic pricing based on time-of-day and demand
- Real-time availability tracking

**Tools the agent will have**:
- `SearchChargers(location, minPower)` - Find nearby chargers
- `GetChargerStatus(chargerId)` - Real-time availability
- `CalculateChargingCost(chargerId, kWhNeeded, startTime)` - Cost estimation
- `GetTariffSchedule(chargerId)` - Pricing tiers

---

## Design Decisions

1. **Cumulative exercises**: Each exercise builds on the previous. The MCP server from Exercise 1 is used in Exercise 4's integration.
2. **Single notebook**: All content in one `agentic-swe-workshop.dib` for easy distribution.
3. **Warm-up included**: 10-minute intro to polyglot notebooks before Module 1.

---

## Revised Time Allocation

| Section | Duration |
|---------|----------|
| Warm-up: Polyglot Notebooks 101 | 10 min |
| Opening: Agentic SWE Landscape | 15 min |
| Module 1: MCP Servers | 50 min |
| Module 2: Skills | 45 min |
| Break | 15 min |
| Module 3: Building an Agent | 55 min |
| Module 4: Integration | 25 min |
| Closing | 5 min |
| **Total** | **220 min (3h 40min)** |

*Buffer: exercises may run faster, leaving time for Q&A*

---

## File to Create
`C:\code\GitHub\MartinRL.github.io\notebooks\agentic-swe-workshop.dib`
