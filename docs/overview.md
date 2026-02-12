# AGICE Overview (Public‑Safe)

> **Patent Pending (USPTO Provisional)** — Application No. **63/978,753** — Filed **2026-02-09**.  
> This repository and linked artifacts are provided for research/verification and do not imply a granted patent.

AGICE (Aleph General Intelligence Convergence Engine) is an evidence‑native reasoning system that couples a generator (LLM) with task verifiers in an iterative closed loop.

## Core loop (conceptual)
1) **Generate** a bounded incremental *RoundOutput* under an output contract (progress in verifiable chunks).  
2) **Verify** using a pack of one or more oracles (unit tests, simulators, feasibility checks, scorers).  
3) **Arbitrate** across multiple oracles (hard‑constraint veto + soft objective aggregation).  
4) **Converge** using verifier‑driven strategies (best‑of selection, robust aggregation, bounded repair).  
5) **Emit evidence**: an audit‑grade bundle including candidates, verifier outputs, arbitration decisions, and replay metadata.

## Evidence‑native generalization
AGICE is designed for **novel / low‑pattern‑overlap tasks**, shifting trust from “model assertions” to **machine‑checkable evidence**. A central goal is to estimate performance on **post‑cutoff problems** using benchmarks with **release dates** (e.g., LiveCodeBench’s time‑windowed problems).

## Geometric projection branching (GMDT / MA −i)
In **A3**, AGICE enables an optional bounded projection exploration mechanism referred to as **Geometrical Multi‑Dimensional Transformation (GMDT)** / **Multi‑Axis (MA −i)** branching.

Intuition:
- When an update appears anti‑aligned with verifier feedback, AGICE may explore bounded “projection variants” of the update.
- One practical realization is a 4‑cycle over projections:
  - `base`
  - `minus_i` (−i)
  - `neg_base` (−1)
  - `neg_minus_i` (+i)

These projections are evaluated by the same verifier pack and selected/arbitrated under the same evidence protocol.

## Experimental modes (A0–A3)
AGICE reports results using an ablation ladder:
- **A0**: baseline model, one‑shot
- **A1**: baseline model with retries
- **A2**: AGICE with GMDT (MA −i) **OFF**
- **A3**: AGICE with GMDT (MA −i) **ON**

Concrete mappings for the two evidence tracks are summarized in the repository README.
