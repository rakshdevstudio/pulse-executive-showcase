# Generate refined, executive, human-centered story mode scenes for PULSE showcase

story_code = r'''# Story Mode HTML (Cinematic Executive Presentation)

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

      <!-- SCENE 1: OPENING HOOK (RESTORED EXACT APPROVED EXECUTIVE DESIGN) -->
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
          <p class="scene-1-subtext">A proposal to bring together employee attendance, order keying, quality, and daily operational reports across Design Sheetmetal's India operations.</p>
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

      <!-- SCENE 2: THE CURRENT CHALLENGE -->
      <section class="scene-slide" id="scene-2">
        <div class="scene-title-badge">Current Operational Reality</div>
        <h2 class="scene-headline">Our Teams Work Hard. <span class="gold-highlight">Our Reports Work Separately.</span></h2>
        <p class="scene-narrative">
          Every day, our team leaders track attendance, order keying, flashings, double-checking, leave and quality issues. Much of this information is maintained through separate manual reports.
        </p>

        <!-- Floating Disconnected Sheets & Interactive Transformation Stage -->
        <div class="sheets-stage" id="sheets-stage-container">
          <!-- Sheet 1: Attendance -->
          <div class="floating-sheet" style="top: 8px; left: 30px; transform: rotate(-3deg);">
            <div class="sheet-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
            </div>
            <div class="sheet-name">Attendance Register</div>
            <div class="sheet-desc">Manual physical sign-in & disconnected spreadsheet logs.</div>
            <span class="sheet-status">Manual Entry</span>
          </div>

          <!-- Sheet 2: Daily Orders Keyed -->
          <div class="floating-sheet" style="top: 5px; left: 380px; transform: rotate(2deg);">
            <div class="sheet-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
            </div>
            <div class="sheet-name">Daily Orders Keyed</div>
            <div class="sheet-desc">Shift emails and nightly handovers sent to Melbourne.</div>
            <span class="sheet-status">Email Chain</span>
          </div>

          <!-- Sheet 3: Flashings & Bits Log -->
          <div class="floating-sheet" style="top: 10px; right: 30px; transform: rotate(-2deg);">
            <div class="sheet-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/></svg>
            </div>
            <div class="sheet-name">Flashings & Bits Log</div>
            <div class="sheet-desc">Separate shared folder workbook tracking units & meters.</div>
            <span class="sheet-status">Excel Workbook</span>
          </div>

          <!-- Sheet 4: Double-Check Records -->
          <div class="floating-sheet" style="bottom: 8px; left: 60px; transform: rotate(3deg);">
            <div class="sheet-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
            </div>
            <div class="sheet-name">Double-Check Records</div>
            <div class="sheet-desc">Auditor notes on physical printouts and CAD sign-offs.</div>
            <span class="sheet-status">Paper Checklists</span>
          </div>

          <!-- Sheet 5: Resupply & Errors Log -->
          <div class="floating-sheet" style="bottom: 5px; left: 400px; transform: rotate(-1deg);">
            <div class="sheet-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            </div>
            <div class="sheet-name">Resupply & Errors Log</div>
            <div class="sheet-desc">Urgent WhatsApp alerts when Melbourne installation halts.</div>
            <span class="sheet-status">Ad-Hoc Messaging</span>
          </div>

          <!-- Sheet 6: Leaves & Holidays -->
          <div class="floating-sheet" style="bottom: 8px; right: 50px; transform: rotate(2deg);">
            <div class="sheet-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            </div>
            <div class="sheet-name">Leaves & Holidays</div>
            <div class="sheet-desc">Separate email threads, paper slips and calendar notices.</div>
            <span class="sheet-status">Unlinked Records</span>
          </div>

          <!-- Central Hub Transformation Card (Unified Operational Core) -->
          <div class="central-hub-reveal" id="central-hub-reveal">
            <div class="pulse-dot" style="margin: 0 auto 10px;"></div>
            <h3 style="font-size: 20px; color: var(--gold); margin-bottom: 6px; font-weight: 700; letter-spacing: 0.05em;">ONE CONSOLIDATED OPERATIONAL CORE</h3>
            <p style="font-size: 13px; color: var(--porcelain); margin-bottom: 14px; line-height: 1.45;">
              One real-time data pipeline replacing disconnected spreadsheets, email handovers, and paper sign-offs with universal operational visibility.
            </p>
            <span class="status-badge verified">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              All Operational Channels Unified
            </span>
          </div>
        </div>

        <!-- Interactive Consolidation Toggle -->
        <div style="display: flex; justify-content: center; margin-bottom: 14px;">
          <button class="btn btn-gold btn-sm" onclick="toggleConsolidateSheets()" style="gap: 8px; box-shadow: 0 0 20px rgba(198, 166, 117, 0.25); cursor: pointer;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 14 10 14 10 20"/><polyline points="20 10 14 10 14 4"/><line x1="14" y1="10" x2="21" y2="3"/><line x1="3" y1="21" x2="10" y2="14"/></svg>
            <span>Toggle Consolidation Animation</span>
          </button>
        </div>

        <!-- 5 Friction Callout Cards -->
        <div class="friction-grid">
          <div class="friction-card">
            <div class="friction-tag">Friction 01</div>
            <div class="friction-title">Information Scattered</div>
            <div class="friction-body">Data lives across 6+ unconnected formats, Excel workbooks, and folders.</div>
          </div>
          <div class="friction-card">
            <div class="friction-tag">Friction 02</div>
            <div class="friction-title">Manual Consolidation</div>
            <div class="friction-body">Team leaders spend 1.5+ hours nightly copying rows and rekeying tallies.</div>
          </div>
          <div class="friction-card">
            <div class="friction-tag">Friction 03</div>
            <div class="friction-title">Limited Visibility</div>
            <div class="friction-body">Historical performance comparisons require manual searches across past logs.</div>
          </div>
          <div class="friction-card">
            <div class="friction-tag">Friction 04</div>
            <div class="friction-title">Administrative Burden</div>
            <div class="friction-body">Repeated data entry creates fatigue, burnout, and transcription errors.</div>
          </div>
          <div class="friction-card">
            <div class="friction-tag">Friction 05</div>
            <div class="friction-title">Delayed Action</div>
            <div class="friction-body">Leadership sees operational problems and resupply trends 24–48 hours late.</div>
          </div>
        </div>

        <!-- Closing Opportunity Message Banner -->
        <div style="padding: 16px 24px; background: rgba(198, 166, 117, 0.08); border: 1px solid var(--gold-border); border-radius: 8px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
          <div>
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 4px;">
              <span class="pulse-dot"></span>
              <strong style="color: var(--white); font-size: 15px;">The information exists. The opportunity is to bring it together.</strong>
            </div>
            <div style="font-size: 13px; color: var(--steel); line-height: 1.5;">
              This proposal originated directly from our floor manager's request to digitize manually prepared reports into one reliable operational system.
            </div>
          </div>
          <button class="btn btn-gold btn-sm" onclick="nextScene()">
            See the Solution →
          </button>
        </div>
      </section>

      <!-- SCENE 3: THE PRODUCT REVEAL -->
      <section class="scene-slide" id="scene-3">
        <div class="scene-title-badge">Proposed Solution</div>
        <h2 class="scene-headline">Introducing PULSE. <span class="gold-highlight">One Place for Everything That Matters.</span></h2>
        <p class="scene-narrative">
          A proposed digital workplace for managing employee attendance, daily work, quality, leave and operational reporting.
        </p>

        <!-- 4 Core Pillars Grid -->
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin-bottom: 24px;">
          <div class="card" style="padding: 20px; border-top: 3px solid var(--emerald); background: rgba(24, 38, 49, 0.7);">
            <div style="width: 38px; height: 38px; border-radius: 6px; background: var(--emerald-dim); border: 1px solid var(--emerald); display: flex; align-items: center; justify-content: center; color: var(--emerald); font-weight: bold; font-family: var(--font-mono); margin-bottom: 12px;">01</div>
            <h3 style="font-size: 17px; color: var(--white); margin-bottom: 8px;">Our People</h3>
            <p style="font-size: 13px; color: var(--steel); line-height: 1.6;">
              Attendance, approved leave, assigned shifts, and team availability across all detailing cells.
            </p>
          </div>

          <div class="card" style="padding: 20px; border-top: 3px solid var(--gold); background: rgba(24, 38, 49, 0.7);">
            <div style="width: 38px; height: 38px; border-radius: 6px; background: var(--gold-dim); border: 1px solid var(--gold); display: flex; align-items: center; justify-content: center; color: var(--gold); font-weight: bold; font-family: var(--font-mono); margin-bottom: 12px;">02</div>
            <h3 style="font-size: 17px; color: var(--white); margin-bottom: 8px;">Our Work</h3>
            <p style="font-size: 13px; color: var(--steel); line-height: 1.6;">
              Customer purchase orders keyed, flashing linear metres, accessory bits, and peer double-checks.
            </p>
          </div>

          <div class="card" style="padding: 20px; border-top: 3px solid var(--amber); background: rgba(24, 38, 49, 0.7);">
            <div style="width: 38px; height: 38px; border-radius: 6px; background: var(--amber-dim); border: 1px solid var(--amber); display: flex; align-items: center; justify-content: center; color: var(--amber); font-weight: bold; font-family: var(--font-mono); margin-bottom: 12px;">03</div>
            <h3 style="font-size: 17px; color: var(--white); margin-bottom: 8px;">Our Quality</h3>
            <p style="font-size: 13px; color: var(--steel); line-height: 1.6;">
              Order errors, resupply reviews, verified root causes, and zero-blame improvement actions.
            </p>
          </div>

          <div class="card" style="padding: 20px; border-top: 3px solid #9B59B6; background: rgba(24, 38, 49, 0.7);">
            <div style="width: 38px; height: 38px; border-radius: 6px; background: rgba(155, 89, 182, 0.2); border: 1px solid #9B59B6; display: flex; align-items: center; justify-content: center; color: #D2B4DE; font-weight: bold; font-family: var(--font-mono); margin-bottom: 12px;">04</div>
            <h3 style="font-size: 17px; color: var(--white); margin-bottom: 8px;">Our Management</h3>
            <p style="font-size: 13px; color: var(--steel); line-height: 1.6;">
              Clear operational summaries, shift handover dossiers, and pending items requiring attention.
            </p>
          </div>
        </div>

        <!-- Teaser Preview Ribbon -->
        <div style="padding: 18px 24px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 8px; display: flex; justify-content: space-between; align-items: center;">
          <div style="font-size: 13px; color: var(--porcelain);">
            <strong style="color: var(--gold);">Simulated Architecture:</strong> Designed specifically for Design Sheetmetal India Operations without third-party subscriptions or vendor lock-in.
          </div>
          <button class="btn btn-outline btn-sm" onclick="switchToProductMode()">
            Preview Prototype Interface →
          </button>
        </div>
      </section>

      <!-- SCENE 4: ATTENDANCE & BIOMETRICS -->
      <section class="scene-slide" id="scene-4">
        <div class="scene-title-badge">Pillar 01 • Attendance Records</div>
        <h2 class="scene-headline">Know Who's Here. When They Arrived. <span class="gold-highlight">And When They Leave.</span></h2>
        <p class="scene-narrative">
          PULSE is designed to connect with the company's existing attendance system, making entry, exit, breaks and working-time records easier to review.
        </p>

        <!-- 3 Feature Cards -->
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin-bottom: 22px;">
          <div class="card" style="padding: 16px;">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--emerald); margin-bottom: 6px;">01 — ENTRY & EXIT</div>
            <h4 style="color: var(--white); margin-bottom: 6px;">Verified Timestamps</h4>
            <p style="font-size: 12px; color: var(--steel); line-height: 1.6;">
              See each employee's recorded arrival and departure times clearly across shifts.
            </p>
          </div>
          <div class="card" style="padding: 16px;">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--gold); margin-bottom: 6px;">02 — BREAK TRACKING</div>
            <h4 style="color: var(--white); margin-bottom: 6px;">Tea & Lunch Duration</h4>
            <p style="font-size: 12px; color: var(--steel); line-height: 1.6;">
              Review lunch and morning tea breaks where the attendance device supports recorded events.
            </p>
          </div>
          <div class="card" style="padding: 16px;">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--amber); margin-bottom: 6px;">03 — CORRECTIONS</div>
            <h4 style="color: var(--white); margin-bottom: 6px;">Transparent Regularization</h4>
            <p style="font-size: 12px; color: var(--steel); line-height: 1.6;">
              Handle missing punches, discrepancies and supervisor-approved changes with a clear audit history.
            </p>
          </div>
        </div>

        <!-- Animated Employee Attendance Timeline -->
        <div class="card" style="background: rgba(24, 38, 49, 0.7); border: 1px solid var(--gold-border); margin-bottom: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
            <strong style="color: var(--white); font-size: 14px;">Sample Timeline: Rohan Sharma (Senior Detailing Specialist • Shift A)</strong>
            <span class="status-badge verified">Verified Compliant</span>
          </div>

          <!-- Step-by-Step Flow Line -->
          <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; margin-bottom: 14px; text-align: center;">
            <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--emerald); border-radius: 6px;">
              <div style="font-size: 10px; color: var(--steel); text-transform: uppercase;">1. Office Entry</div>
              <strong style="font-size: 14px; color: #79D2B7; font-family: var(--font-mono);">05:58 AM</strong>
              <div style="font-size: 10px; color: var(--steel-dim);">On-Time (2m early)</div>
            </div>
            <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 10px; color: var(--steel); text-transform: uppercase;">2. Morning Tea</div>
              <strong style="font-size: 14px; color: var(--amber); font-family: var(--font-mono);">09:15 AM</strong>
              <div style="font-size: 10px; color: var(--steel-dim);">Break Start</div>
            </div>
            <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 10px; color: var(--steel); text-transform: uppercase;">3. Tea Return</div>
              <strong style="font-size: 14px; color: #79D2B7; font-family: var(--font-mono);">09:30 AM</strong>
              <div style="font-size: 10px; color: var(--steel-dim);">15m Elapsed</div>
            </div>
            <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 10px; color: var(--steel); text-transform: uppercase;">4. Lunch Break</div>
              <strong style="font-size: 14px; color: var(--amber); font-family: var(--font-mono);">12:10 PM</strong>
              <div style="font-size: 10px; color: var(--steel-dim);">Break Start</div>
            </div>
            <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 10px; color: var(--steel); text-transform: uppercase;">5. Lunch Return</div>
              <strong style="font-size: 14px; color: #79D2B7; font-family: var(--font-mono);">12:40 PM</strong>
              <div style="font-size: 10px; color: var(--steel-dim);">30m Elapsed</div>
            </div>
            <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--gold); border-radius: 6px;">
              <div style="font-size: 10px; color: var(--steel); text-transform: uppercase;">6. Shift Handover</div>
              <strong style="font-size: 14px; color: var(--gold); font-family: var(--font-mono);">14:30 PM</strong>
              <div style="font-size: 10px; color: var(--steel-dim);">Net: 7h 47m</div>
            </div>
          </div>

          <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 10px; border-top: 1px solid var(--slate-border); font-size: 12px; color: var(--steel);">
            <div>
              Time on Premises: <strong style="color: var(--white);">8h 32m</strong> • Recorded Breaks: <strong style="color: var(--amber);">45m</strong> • Net Attended: <strong style="color: var(--gold);">7h 47m</strong>
            </div>
            <div style="color: var(--gold); font-style: italic;">
              *Biometric integration is proposed and subject to existing device capabilities. Illustrative demonstration.
            </div>
          </div>
        </div>

        <div style="display: flex; justify-content: flex-end; gap: 12px;">
          <button class="btn btn-gold btn-sm" onclick="exploreFeature('biometric')">
            Explore Attendance in Prototype →
          </button>
        </div>
      </section>

      <!-- SCENE 5: DAILY WORK & PRODUCTIVITY -->
      <section class="scene-slide" id="scene-5">
        <div class="scene-title-badge">Pillar 02 • Daily Work Output</div>
        <h2 class="scene-headline">Every Order. Every Flashing. <span class="gold-highlight">Every Contribution.</span></h2>
        <p class="scene-narrative">
          A simpler way to record and understand the work completed across our teams.
        </p>

        <!-- 4 Sample Metric Cards -->
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 22px;">
          <div class="metric-card" style="padding: 18px;">
            <div class="metric-label">Orders Keyed</div>
            <div class="metric-value">142</div>
            <div class="metric-context" style="color: var(--gold);">Customer Orders Processed</div>
          </div>
          <div class="metric-card" style="padding: 18px;">
            <div class="metric-label">Flashing Lengths Recorded</div>
            <div class="metric-value">1,840m</div>
            <div class="metric-context" style="color: var(--emerald);">Linear Metres Detailed</div>
          </div>
          <div class="metric-card" style="padding: 18px;">
            <div class="metric-label">Bits Processed</div>
            <div class="metric-value">5,120</div>
            <div class="metric-context" style="color: var(--porcelain);">Accessories & Brackets</div>
          </div>
          <div class="metric-card" style="padding: 18px;">
            <div class="metric-label">Double-Checks Completed</div>
            <div class="metric-value">138</div>
            <div class="metric-context" style="color: #79D2B7;">Peer Quality Verifications (97.2%)</div>
          </div>
        </div>

        <!-- Team Comparison Table -->
        <div class="card" style="background: rgba(24, 38, 49, 0.7); margin-bottom: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <strong style="color: var(--white); font-size: 14px;">Work Completed Across Detailing Cells (Sample Reporting Day)</strong>
            <span style="font-size: 11px; color: var(--gold); font-family: var(--font-mono);">Illustrative Sample Figures</span>
          </div>
          <div class="data-table-container">
            <table class="data-table" style="font-size: 12px;">
              <thead>
                <tr>
                  <th>Detailing Cell</th>
                  <th>Product Focus</th>
                  <th>Orders Keyed</th>
                  <th>Flashings Detailed</th>
                  <th>Accessories / Bits</th>
                  <th>Double-Checks Completed</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Team Alpha</strong></td>
                  <td>Parapet Flashings & Roof Trims</td>
                  <td><strong style="color: var(--gold);">42</strong></td>
                  <td>680 metres</td>
                  <td>1,850 parts</td>
                  <td><span style="color: #79D2B7;">42 of 42 (100%)</span></td>
                </tr>
                <tr>
                  <td><strong>Team Beta</strong></td>
                  <td>Architectural Cladding Panels</td>
                  <td><strong style="color: var(--gold);">34</strong></td>
                  <td>410 metres</td>
                  <td>1,120 parts</td>
                  <td><span style="color: #79D2B7;">33 of 34 (97.1%)</span></td>
                </tr>
                <tr>
                  <td><strong>Team Gamma</strong></td>
                  <td>Rainwater Goods & Downpipes</td>
                  <td><strong style="color: var(--gold);">38</strong></td>
                  <td>450 metres</td>
                  <td>1,250 parts</td>
                  <td><span style="color: #79D2B7;">36 of 38 (94.7%)</span></td>
                </tr>
                <tr>
                  <td><strong>Team Delta</strong></td>
                  <td>Special Structural Assemblies</td>
                  <td><strong style="color: var(--gold);">28</strong></td>
                  <td>300 metres</td>
                  <td>900 parts</td>
                  <td><span style="color: #79D2B7;">27 of 28 (96.4%)</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center;">
          <div style="font-size: 12px; color: var(--steel);">
            Team leaders enter daily work in under 60 seconds • Management sees instantly updated totals.
          </div>
          <button class="btn btn-gold btn-sm" onclick="exploreFeature('production')">
            Explore Daily Work Report in Prototype →
          </button>
        </div>
      </section>

      <!-- SCENE 6: SHIFT HANDOVER -->
      <section class="scene-slide" id="scene-6">
        <div class="scene-title-badge">Pillar 03 • Shift Continuity</div>
        <h2 class="scene-headline">When One Shift Ends, <span class="gold-highlight">The Next Starts Informed.</span></h2>
        <p class="scene-narrative">
          Important work, pending checks, customer clarifications and team updates can be passed to the next shift in one organized handover.
        </p>

        <!-- Step-by-Step Handover Workflow -->
        <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-bottom: 20px; align-items: center;">
          <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px; text-align: center;">
            <div style="font-size: 10px; color: var(--gold); text-transform: uppercase; font-family: var(--font-mono);">Step 1</div>
            <strong style="font-size: 12px; color: var(--white);">Outgoing TL</strong>
            <div style="font-size: 11px; color: var(--steel);">Prepares handover</div>
          </div>
          <div style="text-align: center; color: var(--gold); font-size: 18px;">→</div>
          <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px; text-align: center;">
            <div style="font-size: 10px; color: var(--gold); text-transform: uppercase; font-family: var(--font-mono);">Step 2</div>
            <strong style="font-size: 12px; color: var(--white);">Records Items</strong>
            <div style="font-size: 11px; color: var(--steel);">Pending checks & RFIs</div>
          </div>
          <div style="text-align: center; color: var(--gold); font-size: 18px;">→</div>
          <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--emerald); border-radius: 6px; text-align: center;">
            <div style="font-size: 10px; color: var(--emerald); text-transform: uppercase; font-family: var(--font-mono);">Step 3</div>
            <strong style="font-size: 12px; color: #79D2B7;">Incoming TL</strong>
            <div style="font-size: 11px; color: var(--steel);">Acknowledges & Continues</div>
          </div>
        </div>

        <!-- Sample Handover Card -->
        <div class="card" style="background: rgba(24, 38, 49, 0.7); border: 1px solid var(--gold-border); margin-bottom: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; padding-bottom: 10px; border-bottom: 1px solid var(--slate-border);">
            <div style="display: flex; align-items: center; gap: 12px;">
              <span class="status-badge warning">Awaiting Acknowledgment</span>
              <strong style="color: var(--white); font-size: 15px;">Shift A → Shift B Handover Note</strong>
            </div>
            <div style="font-family: var(--font-mono); font-size: 12px; color: var(--gold);">
              Monday, 23 Nov 2026 • 14:15 IST
            </div>
          </div>

          <div style="display: grid; grid-template-columns: 1fr 1.5fr; gap: 20px; font-size: 13px;">
            <div style="display: flex; flex-direction: column; gap: 10px;">
              <div>
                <span style="color: var(--steel); font-size: 11px; text-transform: uppercase;">From Outgoing Leader:</span>
                <div style="color: var(--white); font-weight: 500;">Priya Nair (Shift A Lead)</div>
              </div>
              <div>
                <span style="color: var(--steel); font-size: 11px; text-transform: uppercase;">To Incoming Leader:</span>
                <div style="color: var(--white); font-weight: 500;">Rajesh Kumar (Shift B Lead)</div>
              </div>
              <div style="padding: 8px 12px; background: var(--midnight); border-radius: 4px; font-size: 12px; color: #79D2B7;">
                ✓ All 36 operators logged & attendance closed.
              </div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 8px;">
              <span style="color: var(--steel); font-size: 11px; text-transform: uppercase;">Pending Work Items to Transfer:</span>
              <ul style="list-style: none; display: flex; flex-direction: column; gap: 6px; font-size: 12px; color: var(--porcelain);">
                <li style="padding: 6px 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
                  • <strong>4 orders awaiting double-check:</strong> Orders #8841, #8842, #8845, #8849.
                </li>
                <li style="padding: 6px 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
                  • <strong>2 customer clarifications:</strong> Builder RFI response expected on roof pitch angle.
                </li>
                <li style="padding: 6px 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
                  • <strong>1 urgent follow-up:</strong> Bayside Commercial flashing batch priority queue.
                </li>
                <li style="padding: 6px 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
                  • <strong>1 resupply investigation:</strong> Tooling clearance check on 0.9mm Colorbond.
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div style="display: flex; justify-content: flex-end;">
          <button class="btn btn-gold btn-sm" onclick="exploreFeature('handover')">
            Explore Shift Handover in Prototype →
          </button>
        </div>
      </section>

      <!-- SCENE 7: EMPLOYEE PERFORMANCE -->
      <section class="scene-slide" id="scene-7">
        <div class="scene-title-badge">Pillar 04 • Employee Development</div>
        <h2 class="scene-headline">Understand Performance. <span class="gold-highlight">Recognize Progress.</span></h2>
        <p class="scene-narrative">
          Give employees and management a clearer view of attendance, work completed, quality and professional development.
        </p>

        <!-- 4 Visual Cards -->
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 20px;">
          <div class="card" style="padding: 16px; border-top: 3px solid var(--emerald);">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--emerald); margin-bottom: 4px;">01 — ATTENDANCE</div>
            <h4 style="color: var(--white); margin-bottom: 6px; font-size: 14px;">Reliability & Presence</h4>
            <p style="font-size: 12px; color: var(--steel); line-height: 1.5;">
              Entry and exit records, approved leave history, and monthly attendance trends.
            </p>
          </div>
          <div class="card" style="padding: 16px; border-top: 3px solid var(--gold);">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--gold); margin-bottom: 4px;">02 — WORK COMPLETED</div>
            <h4 style="color: var(--white); margin-bottom: 6px; font-size: 14px;">Orders & Output</h4>
            <p style="font-size: 12px; color: var(--steel); line-height: 1.5;">
              Orders keyed, flashings detailed, bits processed, and peer double-check completion.
            </p>
          </div>
          <div class="card" style="padding: 16px; border-top: 3px solid #79D2B7;">
            <div style="font-family: var(--font-mono); font-size: 11px; color: #79D2B7; margin-bottom: 4px;">03 — QUALITY</div>
            <h4 style="color: var(--white); margin-bottom: 6px; font-size: 14px;">Errors & Learnings</h4>
            <p style="font-size: 12px; color: var(--steel); line-height: 1.5;">
              Verified drawing corrections, resupply investigations, and constructive learnings.
            </p>
          </div>
          <div class="card" style="padding: 16px; border-top: 3px solid #9B59B6;">
            <div style="font-family: var(--font-mono); font-size: 11px; color: #D2B4DE; margin-bottom: 4px;">04 — DEVELOPMENT</div>
            <h4 style="color: var(--white); margin-bottom: 6px; font-size: 14px;">Skills & Training</h4>
            <p style="font-size: 12px; color: var(--steel); line-height: 1.5;">
              Core sheetmetal skills, peer recognition awards, and supervisory coaching notes.
            </p>
          </div>
        </div>

        <!-- Fictional Employee Profile Showcase -->
        <div class="card" style="background: rgba(24, 38, 49, 0.7); border: 1px solid var(--slate-border); margin-bottom: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <div style="display: flex; align-items: center; gap: 12px;">
              <div style="width: 42px; height: 42px; border-radius: 50%; background: var(--gold-dim); border: 2px solid var(--gold); display: flex; align-items: center; justify-content: center; color: var(--gold); font-weight: bold;">RS</div>
              <div>
                <strong style="color: var(--white); font-size: 15px;">Rohan Sharma</strong>
                <span style="font-size: 12px; color: var(--steel);"> • Senior Detailing Specialist • Team Alpha</span>
              </div>
            </div>
            <span class="status-badge verified">Demonstration Profile</span>
          </div>

          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; font-size: 12px; margin-bottom: 10px;">
            <div style="padding: 10px; background: var(--midnight); border-radius: 4px;">
              <div style="color: var(--steel);">Monthly Attendance</div>
              <strong style="color: #79D2B7; font-size: 14px;">22 / 23 Days</strong>
              <div style="color: var(--steel-dim); font-size: 10px;">1 Day Approved Annual Leave</div>
            </div>
            <div style="padding: 10px; background: var(--midnight); border-radius: 4px;">
              <div style="color: var(--steel);">Daily Output Average</div>
              <strong style="color: var(--gold); font-size: 14px;">16 Orders / Shift</strong>
              <div style="color: var(--steel-dim); font-size: 10px;">210m Flashings Detailed</div>
            </div>
            <div style="padding: 10px; background: var(--midnight); border-radius: 4px;">
              <div style="color: var(--steel);">Quality Accuracy</div>
              <strong style="color: #79D2B7; font-size: 14px;">99.4% First-Pass</strong>
              <div style="color: var(--steel-dim); font-size: 10px;">Zero-Blame Learning Action</div>
            </div>
            <div style="padding: 10px; background: var(--midnight); border-radius: 4px;">
              <div style="color: var(--steel);">Double-Check Rigor</div>
              <strong style="color: var(--white); font-size: 14px;">100% Peer Verified</strong>
              <div style="color: var(--steel-dim); font-size: 10px;">All jobs formally checked</div>
            </div>
          </div>

          <div style="font-size: 11px; color: var(--steel-dim); line-height: 1.4; padding-top: 6px;">
            *Privacy Protected: Confidential supervisory coaching notes are accessible only to team leaders and management, protecting individual employee privacy.
          </div>
        </div>

        <div style="display: flex; justify-content: flex-end;">
          <button class="btn btn-gold btn-sm" onclick="exploreFeature('employee360')">
            Explore Employee Performance in Prototype →
          </button>
        </div>
      </section>

      <!-- SCENE 8: MANAGEMENT OVERVIEW -->
      <section class="scene-slide" id="scene-8">
        <div class="scene-title-badge">Executive View</div>
        <h2 class="scene-headline">Your Entire Operation. <span class="gold-highlight">One Clear View.</span></h2>
        <p class="scene-narrative">
          See attendance, daily work, pending approvals and quality issues in one management dashboard.
        </p>

        <!-- Mini Dashboard Preview -->
        <div class="card" style="background: rgba(24, 38, 49, 0.85); border: 1px solid var(--gold-border); margin-bottom: 20px; padding: 22px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px; padding-bottom: 12px; border-bottom: 1px solid var(--slate-border);">
            <div>
              <strong style="color: var(--white); font-size: 16px;">Management Summary Dashboard</strong>
              <div style="font-size: 12px; color: var(--steel);">Monday, 23 November 2026 • Shift A Operations</div>
            </div>
            <span style="font-family: var(--font-mono); font-size: 11px; color: var(--gold);">Management visibility based on latest approved records</span>
          </div>

          <!-- Numbers at the Top -->
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 18px;">
            <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Employees Present</div>
              <div style="font-size: 22px; font-weight: 600; color: #79D2B7; font-family: var(--font-serif); margin: 2px 0;">36 / 40</div>
              <div style="font-size: 10px; color: var(--steel-dim);">3 Leave • 1 Absent • 2 Late (ok)</div>
            </div>
            <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Orders Keyed</div>
              <div style="font-size: 22px; font-weight: 600; color: var(--gold); font-family: var(--font-serif); margin: 2px 0;">142 Orders</div>
              <div style="font-size: 10px; color: var(--steel-dim);">1,840m Flashings • 5,120 Bits</div>
            </div>
            <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Double-Checks Done</div>
              <div style="font-size: 22px; font-weight: 600; color: var(--white); font-family: var(--font-serif); margin: 2px 0;">138 (97.2%)</div>
              <div style="font-size: 10px; color: var(--steel-dim);">Peer quality verifications</div>
            </div>
            <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Items For Attention</div>
              <div style="font-size: 22px; font-weight: 600; color: var(--amber); font-family: var(--font-serif); margin: 2px 0;">2 Items</div>
              <div style="font-size: 10px; color: var(--steel-dim);">1 Punch Fix • 1 Leave Request</div>
            </div>
          </div>

          <!-- Two Practical Alerts -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
            <div style="padding: 10px 14px; background: rgba(196, 140, 73, 0.12); border: 1px solid var(--amber); border-radius: 6px; font-size: 12px;">
              <strong style="color: var(--amber);">Notice:</strong> One attendance record needs supervisor correction (EMP-114 missing exit punch).
            </div>
            <div style="padding: 10px 14px; background: rgba(70, 139, 119, 0.12); border: 1px solid var(--emerald); border-radius: 6px; font-size: 12px;">
              <strong style="color: #79D2B7;">Reporting:</strong> Four daily work reports from Shift A await final management approval.
            </div>
          </div>
        </div>

        <!-- Big Primary Action Button -->
        <div style="text-align: center; margin-top: 10px;">
          <button class="btn btn-gold" onclick="exploreFeature('command-centre')" style="padding: 14px 36px; font-size: 15px; font-weight: 600;">
            EXPLORE MANAGEMENT DASHBOARD
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </button>
        </div>
      </section>

      <!-- SCENE 9: PROPOSED MCA INTERNSHIP PROJECT & APPROVAL REQUEST -->
      <section class="scene-slide" id="scene-9">
        <div class="scene-title-badge">Internship Project Approval Request</div>
        <h2 class="scene-headline">Proposed MCA Fourth-Semester <span class="gold-highlight">Internship Project</span></h2>
        <p class="scene-narrative">
          Presented by <strong>Rakshith</strong> (Operational Strategist & MCA Final-Semester Candidate) to the Managing Director and Operational Leadership of Design Sheetmetal.
        </p>

        <!-- Project Origin Note -->
        <div class="card" style="margin-bottom: 20px; background: rgba(24, 38, 49, 0.7); border-left: 4px solid var(--gold);">
          <div style="font-family: var(--font-mono); font-size: 11px; color: var(--gold); margin-bottom: 4px;">PROJECT ORIGIN & PURPOSE</div>
          <p style="font-size: 13px; color: var(--porcelain); line-height: 1.6; margin: 0;">
            This project proposal originated directly from our floor manager's request to digitize manually prepared attendance, daily work, and shift handover reports into one reliable operational system for our India operations.
          </p>
        </div>

        <!-- 6 Clear Asks Grid -->
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-bottom: 24px;">
          <div class="card" style="padding: 14px; border-top: 2px solid var(--gold);">
            <div style="font-family: var(--font-mono); font-size: 10px; color: var(--gold); margin-bottom: 4px;">01 • AUTHORIZATION</div>
            <h4 style="font-size: 13px; color: var(--white); margin-bottom: 4px;">Project Sponsorship</h4>
            <p style="font-size: 11px; color: var(--steel); line-height: 1.5;">
              Formal approval to develop PULSE as the official MCA 4th-semester final project.
            </p>
          </div>
          <div class="card" style="padding: 14px; border-top: 2px solid var(--emerald);">
            <div style="font-family: var(--font-mono); font-size: 10px; color: var(--emerald); margin-bottom: 4px;">02 • MENTORSHIP</div>
            <h4 style="font-size: 13px; color: var(--white); margin-bottom: 4px;">Company Supervisor</h4>
            <p style="font-size: 11px; color: var(--steel); line-height: 1.5;">
              Appointment of an internal operations lead to review technical milestones and project progress.
            </p>
          </div>
          <div class="card" style="padding: 14px; border-top: 2px solid var(--amber);">
            <div style="font-family: var(--font-mono); font-size: 10px; color: var(--amber); margin-bottom: 4px;">03 • REQUIREMENTS</div>
            <h4 style="font-size: 13px; color: var(--white); margin-bottom: 4px;">Access to Formats</h4>
            <p style="font-size: 11px; color: var(--steel); line-height: 1.5;">
              Permission to study current manual report sheets, spreadsheets, and shift handover formats.
            </p>
          </div>
          <div class="card" style="padding: 14px; border-top: 2px solid #79D2B7;">
            <div style="font-family: var(--font-mono); font-size: 10px; color: #79D2B7; margin-bottom: 4px;">04 • COLLABORATION</div>
            <h4 style="font-size: 13px; color: var(--white); margin-bottom: 4px;">Floor Validation</h4>
            <p style="font-size: 11px; color: var(--steel); line-height: 1.5;">
              Working sessions with floor management and team leaders to validate workflow usability.
            </p>
          </div>
          <div class="card" style="padding: 14px; border-top: 2px solid #9B59B6;">
            <div style="font-family: var(--font-mono); font-size: 10px; color: #D2B4DE; margin-bottom: 4px;">05 • PILOT</div>
            <h4 style="font-size: 13px; color: var(--white); margin-bottom: 4px;">Supervised Trial</h4>
            <p style="font-size: 11px; color: var(--steel); line-height: 1.5;">
              Permission to pilot the prototype with a single detailing cell under operational supervision.
            </p>
          </div>
          <div class="card" style="padding: 14px; border-top: 2px solid var(--gold);">
            <div style="font-family: var(--font-mono); font-size: 10px; color: var(--gold); margin-bottom: 4px;">06 • DOCUMENTATION</div>
            <h4 style="font-size: 13px; color: var(--white); margin-bottom: 4px;">Confirmation Letter</h4>
            <p style="font-size: 11px; color: var(--steel); line-height: 1.5;">
              Issuance of the institutional internship confirmation letter for college academic records.
            </p>
          </div>
        </div>

        <!-- Big Launch Prototype Button -->
        <div style="text-align: center;">
          <button class="btn btn-gold" onclick="switchToProductMode()" style="padding: 14px 38px; font-size: 15px; font-weight: 600;">
            Launch Interactive Working Prototype
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
'''

with open("/Users/raksh/.gemini/antigravity/scratch/pulse-showcase/parts_story.py", "w") as f:
    f.write(story_code)

print("parts_story.py successfully generated!")
