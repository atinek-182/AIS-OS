---
name: mattpocock-teach
description: Socratic teaching and mental model builder for TypeScript and web development. Breaks down complex types, frameworks, and patterns into clear analogies, code snippets, and interactive missions. Triggered via /mattpocock-teach or naturally when asking for explanation of complex code.
argument-hint: '[topic_or_concept]'
---

# Matt Pocock Socratic Teaching Engine (`/mattpocock-teach`)

## ⚡ Overview & Tri-Mode Routing

Adapted from TypeScript educator Matt Pocock's signature teaching methodology. Teaches complex TypeScript, React, Next.js, and web engineering concepts through clear mental models, zero fluff, and interactive exercises.

Invokable via:
- **Slash Command**: `/mattpocock-teach [concept]`
- **Dynamic Intent**: Triggered naturally when asking "explain this pattern", "how does TS type inference work here?", or asking for a deep breakdown of web concepts.
- **Inter-Skill Calling**: Invoked by `/grill-me`, `/mattpocock-domain-modeling`, and `/jsmastery-architect`.

---

## 🎓 The 4-Step Teaching Structure

### 1. The Core Mental Model (The "Aha!" Moment)
Start with a high-leverage 2-sentence analogy or physical mental model. Avoid jargon dumps.

### 2. Concrete Code Comparison
Show a **Before (Naive / Broken)** vs **After (Idiomatic / Professional)** code block.

```typescript
// ❌ Naive Approach: Bloated interface with impossible state combinations
interface State {
  isLoading: boolean;
  isError: boolean;
  error?: Error;
  data?: User;
}

// ✅ Matt Pocock Discriminated Union: Impossible states made type-level impossible
type State =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: User }
  | { status: 'error'; error: Error };
```

### 3. Interactive Mission (Test Your Knowledge)
Provide a 3-line coding challenge or question for the user to solve, reinforcing active recall.

### 4. Production Gotchas & Pitfalls
Highlight 1-2 real-world edge cases to watch out for when using this pattern in production.

---

## 🔗 Inter-Skill Connections & Handoff Pipeline
- **Concept Explanation**: Used during Phase 0 discovery by **`/grill-me`** whenever introducing unfamiliar concepts before asking questions.
- **Domain Training**: Connects with **`/mattpocock-domain-modeling`**.
