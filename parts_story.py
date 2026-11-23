# Story Mode HTML (Cinematic Executive Presentation)

def get_story_html(dsm_logo_b64):
    return f"""
  <!-- =========================================================================
       1. STORY MODE (CINEMATIC EXECUTIVE PRESENTATION)
       ========================================================================= -->
  <div id="story-mode-container">
    <!-- Top Bar -->
    <header class="story-header">
      <div class="brand-mark">
        <img src="data:image/png;base64,{dsm_logo_b64}" alt="Design Sheetmetal" class="dsm-logo" />
        <span style="display: inline-block; width: 1px; height: 22px; background: rgba(147, 163, 174, 0.35); margin: 0 4px;"></span>
        <span class="pulse-dot"></span>
        <span>PULSE</span>
        <span class="brand-subtext">Strategic Executive Proposal</span>
        <span class="presenter-pill">Presented by Rakshith</span>
      </div>
      <div class="story-controls">
        <span class="scene-counter" id="scene-counter-display">SCENE 01 / 09</span>
        <button class="btn-header" onclick="openSceneModal()" title="View Scene Menu">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
          Overview
        </button>
        <button class="btn-header" onclick="toggleFullscreen()" title="Toggle Fullscreen">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>
          Fullscreen
        </button>
        <button class="btn-header primary-action" onclick="switchToProductMode()">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          Explore Prototype
        </button>
      </div>
    </header>

    <!-- Progress Fill Line -->
    <div class="story-progress-bar">
      <div class="story-progress-fill" id="story-progress-fill"></div>
    </div>

    <!-- Presentation Viewport -->
    <main class="story-viewport" id="story-viewport">

      <!-- SCENE 1: OPENING HOOK -->
      <section class="scene-slide active" id="scene-1">
        <div class="scene-1-container">
          <div style="display: flex; justify-content: center; margin-bottom: 14px;">
            <img src="data:image/png;base64,{dsm_logo_b64}" alt="Design Sheetmetal" class="dsm-logo-lg" />
          </div>
          <div style="font-family: var(--font-mono); font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--gold); margin-bottom: 12px;">
            Design Sheetmetal • Strategic Operations & Technology Proposal
          </div>
          <!-- Animated SVG Pulse Line -->
          <svg class="scene-1-pulse-svg" viewBox="0 0 900 120" preserveAspectRatio="none">
            <path class="pulse-path" d="M 0 60 L 280 60 L 310 60 L 330 20 L 350 100 L 370 10 L 390 110 L 410 40 L 430 80 L 450 60 L 900 60" />
          </svg>
          <h1 class="headline-line-1">Every Shift Tells a Story.</h1>
          <h2 class="headline-line-2">But are we seeing the whole picture?</h2>
          <p class="scene-1-subtext">A strategic operational proposal to unify workforce operations, keying velocity, and quality intelligence across Design Sheetmetal's India operations.</p>
          <div style="display: inline-flex; align-items: center; gap: 10px; padding: 7px 18px; background: rgba(24, 38, 49, 0.7); border: 1px solid var(--gold-border); border-radius: 20px; font-size: 13px; color: var(--porcelain); margin-bottom: 24px;">
            <span style="color: var(--gold);">Presented by</span>
            <strong>Rakshith</strong>
            <span style="color: var(--steel);">| Operational Strategist</span>
          </div>
          <div class="scene-1-cta">
            <button class="btn btn-gold" onclick="nextScene()">
              Begin Executive Proposal
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
          </div>
        </div>
      </section>

      <!-- SCENE 2: THE OPERATIONAL CHALLENGE -->
      <section class="scene-slide" id="scene-2">
        <div class="scene-title-badge">Operational Diagnosis</div>
        <h2 class="scene-headline">The Reality of Cross-Border <span class="gold-highlight">Sheet-Metal Manufacturing</span></h2>
        <p class="scene-narrative">
          Operating high-precision sheet-metal detailing and order keying across three Indian shifts to serve Australian construction schedules creates three fundamental friction points:
        </p>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-bottom: 30px;">
          <div class="card" style="border-top: 3px solid var(--amber);">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--amber); margin-bottom: 8px;">01. ISOLATED ATTENDANCE</div>
            <h3 style="font-size: 17px; margin-bottom: 10px; color: var(--white);">Biometric Clock Disconnect</h3>
            <p style="font-size: 13px; color: var(--steel); line-height: 1.6;">
              Punch clocks record physical presence at turnstiles, but management has zero real-time visibility into shift keying velocity or whether staff are allocated to high-priority Melbourne jobs.
            </p>
          </div>
          <div class="card" style="border-top: 3px solid var(--crimson);">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--crimson); margin-bottom: 8px;">02. SHIFT BLIND SPOTS</div>
            <h3 style="font-size: 17px; margin-bottom: 10px; color: var(--white);">Fragmented TL Handovers</h3>
            <p style="font-size: 13px; color: var(--steel); line-height: 1.6;">
              When Shift A departs at 14:30 and Shift B arrives, pending Melbourne delivery cutoffs and machine maintenance statuses are lost in informal messaging channels.
            </p>
          </div>
          <div class="card" style="border-top: 3px solid var(--gold);">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--gold); margin-bottom: 8px;">03. QUALITY SILOS</div>
            <h3 style="font-size: 17px; margin-bottom: 10px; color: var(--white);">Delayed Resupply Feedback</h3>
            <p style="font-size: 13px; color: var(--steel); line-height: 1.6;">
              Fabrication variances identified during site dry-fit in Melbourne often take days to trace back to shopfloor drawing revisions in India, preventing rapid root-cause learning.
            </p>
          </div>
        </div>
      </section>

      <!-- SCENE 3: THE PULSE ARCHITECTURE -->
      <section class="scene-slide" id="scene-3">
        <div class="scene-title-badge">System Architecture</div>
        <h2 class="scene-headline">Introducing <span class="gold-highlight">PULSE</span>: The Operational Nervous System</h2>
        <p class="scene-narrative">
          A single glass pane uniting time & attendance hardware, daily shopfloor production logs, zero-blame quality control, and cross-border management intelligence.
        </p>
        <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 32px; align-items: center;">
          <div class="card" style="background: rgba(24, 38, 49, 0.6);">
            <div style="display: flex; flex-direction: column; gap: 14px;">
              <div style="display: flex; align-items: center; gap: 16px; padding: 12px 16px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
                <div style="width: 36px; height: 36px; border-radius: 6px; background: var(--emerald-dim); border: 1px solid var(--emerald); display: flex; align-items: center; justify-content: center; color: var(--emerald); font-weight: bold;">01</div>
                <div>
                  <div style="font-weight: 600; color: var(--white);">Biometric & Break Intelligence</div>
                  <div style="font-size: 12px; color: var(--steel);">Simulated punch ingestion, tea/lunch duration tracking, net attended duration vs award policy.</div>
                </div>
              </div>
              <div style="display: flex; align-items: center; gap: 16px; padding: 12px 16px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
                <div style="width: 36px; height: 36px; border-radius: 6px; background: var(--gold-dim); border: 1px solid var(--gold); display: flex; align-items: center; justify-content: center; color: var(--gold); font-weight: bold;">02</div>
                <div>
                  <div style="font-weight: 600; color: var(--white);">Live Shopfloor Keying & Output</div>
                  <div style="font-size: 12px; color: var(--steel);">Real-time tracking of orders keyed, flashing meters, accessories, and double-check verifications.</div>
                </div>
              </div>
              <div style="display: flex; align-items: center; gap: 16px; padding: 12px 16px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
                <div style="width: 36px; height: 36px; border-radius: 6px; background: var(--amber-dim); border: 1px solid var(--amber); display: flex; align-items: center; justify-content: center; color: var(--amber); font-weight: bold;">03</div>
                <div>
                  <div style="font-weight: 600; color: var(--white);">Zero-Blame Quality & Resupply RCA</div>
                  <div style="font-size: 12px; color: var(--steel);">Constructive case investigations connecting Australian field resupplies directly to drawing revisions.</div>
                </div>
              </div>
              <div style="display: flex; align-items: center; gap: 16px; padding: 12px 16px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
                <div style="width: 36px; height: 36px; border-radius: 6px; background: rgba(155, 89, 182, 0.2); border: 1px solid #9B59B6; display: flex; align-items: center; justify-content: center; color: #D2B4DE; font-weight: bold;">04</div>
                <div>
                  <div style="font-weight: 600; color: var(--white);">Cross-Border Command Centre</div>
                  <div style="font-size: 12px; color: var(--steel);">Dual-clock real-time dashboard synchronizing India shift teams with Melbourne delivery deadlines.</div>
                </div>
              </div>
            </div>
          </div>
          <div style="padding: 24px; border: 1px solid var(--gold-border); border-radius: 8px; background: rgba(198, 166, 117, 0.04);">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--gold); margin-bottom: 8px;">STRATEGIC PRINCIPLE</div>
            <h3 style="font-size: 20px; color: var(--white); margin-bottom: 14px;">Operational Clarity Over Punitive Surveillance</h3>
            <p style="font-size: 13px; color: var(--steel); line-height: 1.7; margin-bottom: 18px;">
              PULSE is engineered to empower operators and team leaders with instant self-awareness, seamless handovers, and transparent operational data — not fear-driven rankings.
            </p>
            <div style="font-size: 12px; color: var(--gold); font-family: var(--font-mono);">Design Sheetmetal India • 2027 Strategic Roadmap</div>
          </div>
        </div>
      </section>

      <!-- SCENE 4: BIOMETRIC PRECISION -->
      <section class="scene-slide" id="scene-4">
        <div class="scene-title-badge">Chapter 01 • Shift Inception</div>
        <h2 class="scene-headline">From the First Turnstile Punch: <span class="gold-highlight">Biometric Precision</span></h2>
        <p class="scene-narrative">
          Every shift begins with biometric verification at our facility gates. PULSE ingests raw hardware punch feeds while maintaining clear boundaries between physical presence and payable hours.
        </p>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;">
          <div class="card">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--emerald); margin-bottom: 6px;">HARDWARE AGNOSTIC</div>
            <h4 style="color: var(--white); margin-bottom: 8px;">Universal Gateway Adapter</h4>
            <p style="font-size: 12px; color: var(--steel); line-height: 1.6;">
              Engineered to support any TCP/IP biometric terminal via webhook, push SDK, or scheduled CSV export without vendor lock-in.
            </p>
          </div>
          <div class="card">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--gold); margin-bottom: 6px;">TIMELINE VISUALIZATION</div>
            <h4 style="color: var(--white); margin-bottom: 8px;">Break & Tea Cycle Tracking</h4>
            <p style="font-size: 12px; color: var(--steel); line-height: 1.6;">
              Differentiates Office IN/OUT from tea and lunch pauses. Calculates exact net attended duration and flags missing return punches.
            </p>
          </div>
          <div class="card">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--amber); margin-bottom: 6px;">AWARD COMPLIANCE</div>
            <h4 style="color: var(--white); margin-bottom: 8px;">Policy-Driven Regularization</h4>
            <p style="font-size: 12px; color: var(--steel); line-height: 1.6;">
              Time on premises is never falsely equated with payable hours. Structured exception approvals protect both employees and company policy.
            </p>
          </div>
        </div>
      </section>

      <!-- SCENE 5: IN-FLIGHT PRODUCTION -->
      <section class="scene-slide" id="scene-5">
        <div class="scene-title-badge">Chapter 02 • Operational Execution</div>
        <h2 class="scene-headline">In-Flight Production Velocity & <span class="gold-highlight">Quality Assurance</span></h2>
        <p class="scene-narrative">
          As sheet-metal detailers key orders, PULSE monitors throughput, flashing complexity, and double-check verifications in real-time, catching discrepancies before metal is cut in Tullamarine.
        </p>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px;">
          <div class="metric-card">
            <div class="metric-label">Daily Orders Keyed</div>
            <div class="metric-value">142</div>
            <div class="metric-context" style="color: var(--emerald);">+8.4% vs Shift Baseline</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Flashings & Trims</div>
            <div class="metric-value">1,840</div>
            <div class="metric-context">Linear Metres Detailed</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Double-Check Rate</div>
            <div class="metric-value">97.2%</div>
            <div class="metric-context" style="color: var(--emerald);">138 of 142 Orders Verified</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">First-Pass Accuracy</div>
            <div class="metric-value">98.6%</div>
            <div class="metric-context">Australian Dry-Fit Benchmark</div>
          </div>
        </div>
      </section>

      <!-- SCENE 6: SEAMLESS HANDOVERS -->
      <section class="scene-slide" id="scene-6">
        <div class="scene-title-badge">Chapter 03 • Shift Continuity</div>
        <h2 class="scene-headline">Unbroken Momentum: <span class="gold-highlight">Structured Handovers</span></h2>
        <p class="scene-narrative">
          Shift transitions are no longer informal handshakes. PULSE mandates a digital handover dossier capturing urgent Melbourne dispatch orders, machine statuses, and upcoming staffing gaps.
        </p>
        <div class="card" style="background: rgba(24, 38, 49, 0.7); border: 1px solid var(--slate-border-light); margin-bottom: 20px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid var(--slate-border);">
            <div style="display: flex; align-items: center; gap: 12px;">
              <span class="status-badge verified">Digital Handover Active</span>
              <strong style="color: var(--white); font-size: 15px;">Shift A (Day) → Shift B (Afternoon) Transfer Dossier</strong>
            </div>
            <div style="font-family: var(--font-mono); font-size: 12px; color: var(--gold);">Cutoff Target: 16:00 AEDT Melbourne Express</div>
          </div>
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; font-size: 13px;">
            <div>
              <div style="color: var(--steel); font-size: 11px; text-transform: uppercase; margin-bottom: 4px;">Outgoing Team Leader</div>
              <div style="color: var(--white); font-weight: 500;">Priya Nair (Shift A Lead)</div>
              <div style="color: var(--steel-dim); font-size: 11px;">Signed & Staged: 14:28 IST</div>
            </div>
            <div>
              <div style="color: var(--steel); font-size: 11px; text-transform: uppercase; margin-bottom: 4px;">Incoming Team Leader</div>
              <div style="color: var(--white); font-weight: 500;">Rajesh Kumar (Shift B Lead)</div>
              <div style="color: var(--emerald); font-size: 11px;">Acknowledged in System: 14:32 IST</div>
            </div>
            <div>
              <div style="color: var(--steel); font-size: 11px; text-transform: uppercase; margin-bottom: 4px;">Urgent Jobs Handed Over</div>
              <div style="color: var(--gold); font-weight: 500;">DSM-MEL-8841 (Bayside Commercial)</div>
              <div style="color: var(--steel-dim); font-size: 11px;">280 flashings cut; bending in progress</div>
            </div>
          </div>
        </div>
      </section>

      <!-- SCENE 7: EMPLOYEE 360 & MERIT -->
      <section class="scene-slide" id="scene-7">
        <div class="scene-title-badge">Chapter 04 • Human Capital</div>
        <h2 class="scene-headline">Employee 360° & <span class="gold-highlight">Sheet-Metal Craftsmanship</span></h2>
        <p class="scene-narrative">
          Building operational capability rather than punitive rankings. Individual 360° dossiers synthesize attendance regularity, output velocity, zero-blame quality learning, and technical sheet-metal certifications.
        </p>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;">
          <div class="card">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--gold); margin-bottom: 6px;">SKILLS & MASTERY</div>
            <h4 style="color: var(--white); margin-bottom: 8px;">7-Point Technical Matrix</h4>
            <p style="font-size: 12px; color: var(--steel); line-height: 1.6;">
              Tracks verified proficiencies across slitting, CNC turret punching, press brake bending, corner notching, TIG/MIG welding, and powder coating.
            </p>
          </div>
          <div class="card">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--emerald); margin-bottom: 6px;">ZERO-BLAME RCA</div>
            <h4 style="color: var(--white); margin-bottom: 8px;">Resupply Learning Ingestion</h4>
            <p style="font-size: 12px; color: var(--steel); line-height: 1.6;">
              Australian site feedback loops are translated into constructive drawing tips and mentorship notes, fostering craftsmanship and ownership.
            </p>
          </div>
          <div class="card">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--steel); margin-bottom: 6px;">ROLE PRIVACY</div>
            <h4 style="color: var(--white); margin-bottom: 8px;">Confidential Mentorship</h4>
            <p style="font-size: 12px; color: var(--steel); line-height: 1.6;">
              Private coaching records and developmental reviews remain securely masked from general staff views, visible only to authorized leadership.
            </p>
          </div>
        </div>
      </section>

      <!-- SCENE 8: EXECUTIVE COMMAND CENTRE -->
      <section class="scene-slide" id="scene-8">
        <div class="scene-title-badge">Chapter 05 • Executive Control</div>
        <h2 class="scene-headline">The Managing Director's <span class="gold-highlight">Command Centre</span></h2>
        <p class="scene-narrative">
          A real-time command dashboard giving the India Managing Director and operations executives instant cross-border visibility into attendance health, floor velocity, and unresolved alerts.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; align-items: center;">
          <div class="card" style="border: 1px solid var(--gold-border);">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--gold); margin-bottom: 10px;">EXECUTIVE CONTROLS AT A GLANCE</div>
            <ul style="list-style: none; display: flex; flex-direction: column; gap: 10px; font-size: 13px; color: var(--porcelain);">
              <li style="display: flex; align-items: center; gap: 10px;">
                <span class="pulse-dot"></span>
                <span><strong>Dual Timezone Synchrony:</strong> Melbourne AEDT and India IST running simultaneously.</span>
              </li>
              <li style="display: flex; align-items: center; gap: 10px;">
                <span class="pulse-dot"></span>
                <span><strong>Instant Attendance Tally:</strong> Scheduled (40) vs Present (34) vs Leave (3) vs Late (2).</span>
              </li>
              <li style="display: flex; align-items: center; gap: 10px;">
                <span class="pulse-dot"></span>
                <span><strong>High-Priority Melbourne Orders:</strong> Direct visibility into critical construction jobs.</span>
              </li>
              <li style="display: flex; align-items: center; gap: 10px;">
                <span class="pulse-dot"></span>
                <span><strong>Exceptions Inbox:</strong> One-click acknowledgment and resolution of operational alerts.</span>
              </li>
            </ul>
          </div>
          <div style="text-align: center; padding: 24px;">
            <div style="font-size: 48px; color: var(--gold); font-family: var(--font-serif); margin-bottom: 10px;">100%</div>
            <div style="font-size: 16px; color: var(--white); margin-bottom: 8px;">Operational Transparency</div>
            <div style="font-size: 12px; color: var(--steel); max-width: 340px; margin: 0 auto 20px;">
              Zero guesswork. Complete alignment between Bengaluru shopfloor execution and Australian customer commitments.
            </div>
            <button class="btn btn-gold" onclick="switchToProductMode()">
              Launch Live Command Centre
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            </button>
          </div>
        </div>
      </section>

      <!-- SCENE 9: PROPOSAL & INVESTMENT ASKS -->
      <section class="scene-slide" id="scene-9">
        <div class="scene-title-badge">Leadership Decision</div>
        <h2 class="scene-headline">Strategic Proposal & <span class="gold-highlight">Implementation Directives</span></h2>
        <p class="scene-narrative">
          Presented by <strong>Rakshith</strong> (Operational Strategist) to the Managing Director and Executive Leadership of Design Sheetmetal.
        </p>
        <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 14px; margin-bottom: 28px;">
          <div class="card" style="padding: 16px; border-top: 3px solid var(--gold);">
            <div style="font-family: var(--font-mono); font-size: 10px; color: var(--gold); margin-bottom: 6px;">ASK 01 • PILOT</div>
            <h4 style="font-size: 14px; color: var(--white); margin-bottom: 6px;">60-Day Shopfloor Pilot</h4>
            <p style="font-size: 11px; color: var(--steel); line-height: 1.5;">
              Deploy PULSE Phase 1 with Team Alpha across Shift A & B to validate keying telemetry.
            </p>
          </div>
          <div class="card" style="padding: 16px; border-top: 3px solid var(--emerald);">
            <div style="font-family: var(--font-mono); font-size: 10px; color: var(--emerald); margin-bottom: 6px;">ASK 02 • BIOMETRICS</div>
            <h4 style="font-size: 14px; color: var(--white); margin-bottom: 6px;">Hardware Connector</h4>
            <p style="font-size: 11px; color: var(--steel); line-height: 1.5;">
              Commission local biometric gateway bridge to ingest turnstile punches in real-time.
            </p>
          </div>
          <div class="card" style="padding: 16px; border-top: 3px solid var(--amber);">
            <div style="font-family: var(--font-mono); font-size: 10px; color: var(--amber); margin-bottom: 6px;">ASK 03 • HARDWARE</div>
            <h4 style="font-size: 14px; color: var(--white); margin-bottom: 6px;">Shopfloor Tablets</h4>
            <p style="font-size: 11px; color: var(--steel); line-height: 1.5;">
              Provision 4 ruggedized tablets at folding stations for instant digital shift handovers.
            </p>
          </div>
          <div class="card" style="padding: 16px; border-top: 3px solid var(--gold);">
            <div style="font-family: var(--font-mono); font-size: 10px; color: var(--gold); margin-bottom: 6px;">ASK 04 • DATA FEED</div>
            <h4 style="font-size: 14px; color: var(--white); margin-bottom: 6px;">Melbourne RCA Link</h4>
            <p style="font-size: 11px; color: var(--steel); line-height: 1.5;">
              Formalize weekly Australian dry-fit resupply logging into the zero-blame learning feed.
            </p>
          </div>
          <div class="card" style="padding: 16px; border-top: 3px solid #9B59B6;">
            <div style="font-family: var(--font-mono); font-size: 10px; color: #D2B4DE; margin-bottom: 6px;">ASK 05 • COUNCIL</div>
            <h4 style="font-size: 14px; color: var(--white); margin-bottom: 6px;">Steering Council</h4>
            <p style="font-size: 11px; color: var(--steel); line-height: 1.5;">
              Bi-weekly executive steering sessions to review velocity, quality gains, and operator feedback.
            </p>
          </div>
        </div>
        <div style="text-align: center;">
          <button class="btn btn-gold" onclick="switchToProductMode()" style="padding: 12px 32px; font-size: 14px;">
            Proceed to Interactive Working Prototype
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </button>
        </div>
      </section>

    </main>

    <!-- Footer Controls -->
    <footer class="story-footer">
      <div class="keyboard-hints">
        <span><span class="kbd-key">←</span><span class="kbd-key">→</span> Navigate</span>
        <span><span class="kbd-key">SPACE</span> Next</span>
        <span><span class="kbd-key">ESC</span> Overview</span>
      </div>
      <div class="story-pagination-dots" id="story-pagination-dots">
        <!-- Injected via JS -->
      </div>
      <div class="nav-arrow-group">
        <button class="btn-nav-arrow" id="btn-prev-scene" onclick="prevScene()" title="Previous Scene">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>
        </button>
        <button class="btn-nav-arrow" id="btn-next-scene" onclick="nextScene()" title="Next Scene">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>
        </button>
      </div>
    </footer>
  </div>
"""

print("parts_story.py created successfully.")
