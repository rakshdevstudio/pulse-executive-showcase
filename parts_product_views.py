# Explore Product Mode Application Views and Modals

def get_product_views_html(dsm_logo_b64):
    return f"""
  <!-- =========================================================================
       2. EXPLORE PRODUCT MODE (INTERACTIVE WORKFORCE OPERATIONS PLATFORM)
       ========================================================================= -->
  <div id="product-mode-container" class="hidden">
    <!-- Application Top Bar -->
    <header class="app-topbar">
      <div class="topbar-left">
        <img src="data:image/png;base64,{dsm_logo_b64}" alt="Design Sheetmetal" class="dsm-logo" />
        <span style="display: inline-block; width: 1px; height: 20px; background: rgba(147, 163, 174, 0.25); margin: 0 2px;"></span>
        <div style="display: flex; align-items: center; gap: 8px;">
          <span class="pulse-dot"></span>
          <span style="font-family: var(--font-serif); font-size: 16px; letter-spacing: 0.16em; font-weight: 600; color: var(--white);">PULSE</span>
          <span class="presenter-pill">Presented by Rakshith</span>
        </div>
        <div class="topbar-clocks">
          <div class="clock-item">
            <span>MELBOURNE:</span>
            <strong id="clock-melbourne">--:--:-- AEDT</strong>
          </div>
          <span style="color: var(--slate-border);">|</span>
          <div class="clock-item">
            <span>INDIA:</span>
            <strong id="clock-india">--:--:-- IST</strong>
          </div>
        </div>
      </div>

      <div class="topbar-right">
        <div class="role-badge-container">
          <span class="role-label">Active Role:</span>
          <select class="role-select" id="role-select" onchange="onRoleChange(this.value)">
            <option value="PRESENTER" selected>Presenter (Rakshith, Systems Architect)</option>
            <option value="MANAGEMENT">Management (David Harrison, MD)</option>
            <option value="TEAM_LEADER">Team Leader (Priya Nair, Shift A)</option>
            <option value="EMPLOYEE">Employee (Rohan Sharma, Keying Specialist)</option>
            <option value="SUPER_ADMIN">System Admin (Alex Vance)</option>
          </select>
        </div>

        <div class="user-pill">
          <div class="user-avatar" id="user-avatar-badge">RK</div>
          <div class="user-meta">
            <span class="user-name" id="user-name-display">Rakshith</span>
            <span class="user-role-title" id="user-role-display">Lead Systems Architect & Operational Strategist</span>
          </div>
        </div>

        <button class="btn btn-outline btn-sm" onclick="resetDemoData()" title="Reset all demo data to pristine state">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M3 21v-5h5"/></svg>
          Reset Demo
        </button>

        <button class="btn btn-gold btn-sm" onclick="switchToStoryMode()">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>
          Story Mode
        </button>
      </div>
    </header>

    <!-- Workspace Layout -->
    <div class="app-workspace">
      <!-- Sidebar Navigation -->
      <aside class="app-sidebar">
        <div class="nav-section-title">Executive Command</div>
        <ul class="sidebar-menu">
          <li class="menu-item active" onclick="switchView('command-centre')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="12 6 12 12 16 14"/></svg>
            <span>Live Command Centre</span>
            <span class="menu-badge gold">LIVE</span>
          </li>
          <li class="menu-item" onclick="switchView('dashboard')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="9"/><rect x="14" y="3" width="7" height="5"/><rect x="14" y="12" width="7" height="9"/><rect x="3" y="16" width="7" height="5"/></svg>
            <span>Operations Dashboard</span>
          </li>
          <li class="menu-item" onclick="switchView('exceptions')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
            <span>Exceptions & Alerts</span>
            <span class="menu-badge alert" id="badge-alerts-count">5</span>
          </li>
        </ul>

        <div class="nav-section-title">Biometrics & Workforce</div>
        <ul class="sidebar-menu">
          <li class="menu-item" onclick="switchView('biometric')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 0 0-10 10c0 4.42 2.87 8.17 6.84 9.5.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34-.46-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.87 1.52 2.34 1.07 2.91.83.09-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.92 0-1.11.38-2 1.03-2.71-.1-.25-.45-1.29.1-2.64 0 0 .84-.27 2.75 1.02.79-.22 1.65-.33 2.5-.33.85 0 1.71.11 2.5.33 1.91-1.29 2.75-1.02 2.75-1.02.55 1.35.2 2.39.1 2.64.65.71 1.03 1.6 1.03 2.71 0 3.82-2.34 4.66-4.57 4.91.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2z"/></svg>
            <span>Biometric & Breaks</span>
            <span class="menu-badge">SIM</span>
          </li>
          <li class="menu-item" onclick="switchView('employee360')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="7" r="4"/><path d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2"/></svg>
            <span>Employee 360° Profile</span>
            <span class="menu-badge gold">360°</span>
          </li>
          <li class="menu-item" onclick="switchView('attendance')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            <span>Attendance Registry</span>
            <span class="menu-badge" id="badge-present-count">34</span>
          </li>
          <li class="menu-item" onclick="switchView('leave')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            <span>Leave Management</span>
            <span class="menu-badge alert" id="badge-leave-pending">2 pending</span>
          </li>
          <li class="menu-item" onclick="switchView('capacity')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
            <span>Capacity & Coverage</span>
          </li>
        </ul>

        <div class="nav-section-title">Manufacturing & Quality</div>
        <ul class="sidebar-menu">
          <li class="menu-item" onclick="switchView('production')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
            <span>Daily Production Log</span>
          </li>
          <li class="menu-item" onclick="switchView('quality')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span>Quality & Resupply</span>
            <span class="menu-badge alert" id="badge-quality-active">2 active</span>
          </li>
          <li class="menu-item" onclick="switchView('handover')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>
            <span>Shift Handover</span>
          </li>
          <li class="menu-item" onclick="switchView('shift-report')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
            <span>End-of-Shift Report</span>
            <span class="menu-badge">PDF</span>
          </li>
        </ul>

        <div class="nav-section-title">Capability & Analytics</div>
        <ul class="sidebar-menu">
          <li class="menu-item" onclick="switchView('skills')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            <span>Skills Matrix (7-Point)</span>
          </li>
          <li class="menu-item" onclick="switchView('report-builder')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
            <span>Custom Report Builder</span>
          </li>
          <li class="menu-item" onclick="switchView('import')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
            <span>CSV / Excel Import</span>
          </li>
          <li class="menu-item" onclick="switchView('recognition')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>
            <span>Recognition & Merit</span>
          </li>
          <li class="menu-item" onclick="switchView('roles')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            <span>Role Permissions</span>
          </li>
        </ul>
      </aside>

      <!-- Main Application Content Area -->
      <main class="app-main">

        <!-- 1. LIVE SHIFT COMMAND CENTRE -->
        <div class="view-panel active" id="view-command-centre">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Live Shift Command Centre</h1>
              <div class="view-header-subtitle">
                Real-time operational nerve centre synchronizing India manufacturing shifts with Melbourne delivery schedules.
              </div>
            </div>
            <div style="display: flex; gap: 10px;">
              <button class="btn btn-outline btn-sm" onclick="switchView('shift-report')">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
                Shift Dossier
              </button>
              <button class="btn btn-gold btn-sm" onclick="switchView('handover')">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/></svg>
                Initiate Handover
              </button>
            </div>
          </div>

          <!-- Live Shift Status Strip -->
          <div class="card" style="margin-bottom: 24px; background: rgba(24, 38, 49, 0.7); border: 1px solid var(--gold-border);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
              <div style="display: flex; align-items: center; gap: 12px;">
                <span class="pulse-dot"></span>
                <strong style="color: var(--white); font-size: 15px;">ACTIVE SHIFT: SHIFT A (DAY SHIFT)</strong>
                <span class="status-badge in">06:00 — 14:30 IST</span>
              </div>
              <div style="font-family: var(--font-mono); font-size: 12px; color: var(--gold);">
                Shift Progress: 82% (6h 58m elapsed)
              </div>
            </div>
            <div style="height: 6px; background: rgba(147, 163, 174, 0.15); border-radius: 3px; overflow: hidden; margin-bottom: 12px;">
              <div style="width: 82%; height: 100%; background: linear-gradient(90deg, var(--gold), #79D2B7); border-radius: 3px;"></div>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; color: var(--steel-dim); font-family: var(--font-mono);">
              <span>06:00 IST Shift Commenced</span>
              <span>12:10 — 12:40 Lunch Window Completed</span>
              <span style="color: var(--gold);">14:30 IST Scheduled Handover to Shift B</span>
            </div>
          </div>

          <!-- Staffing Health Metrics Grid -->
          <div class="metric-grid">
            <div class="metric-card">
              <div class="metric-label">Scheduled Workforce</div>
              <div class="metric-value">40</div>
              <div class="metric-context">Full India Complement</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">Clocked In (Present)</div>
              <div class="metric-value" style="color: #79D2B7;">34</div>
              <div class="metric-context" style="color: var(--emerald);">Active on Shopfloor</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">Approved Leave</div>
              <div class="metric-value">3</div>
              <div class="metric-context">Planned & Covered</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">Unplanned Absence</div>
              <div class="metric-value" style="color: #FFA5A2;">1</div>
              <div class="metric-context" style="color: var(--crimson);">Team Beta (Backup Assigned)</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">Late Arrivals</div>
              <div class="metric-value" style="color: var(--amber);">2</div>
              <div class="metric-context">Transit Regularized</div>
            </div>
          </div>

          <!-- Operational Keying & Quality Ticker -->
          <div class="metric-grid">
            <div class="metric-card">
              <div class="metric-label">Orders Processed Today</div>
              <div class="metric-value">142</div>
              <div class="metric-context" style="color: var(--emerald);">Target: 135 (+5.2%)</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">Total Flashings Detailed</div>
              <div class="metric-value">1,840</div>
              <div class="metric-context">Linear Metres Processed</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">Bits & Accessories</div>
              <div class="metric-value">5,120</div>
              <div class="metric-context">Brackets, End Caps, Clips</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">Double-Check Rate</div>
              <div class="metric-value" style="color: #79D2B7;">97.2%</div>
              <div class="metric-context">138 Orders Formally Verified</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">First-Pass Quality</div>
              <div class="metric-value" style="color: var(--gold);">98.6%</div>
              <div class="metric-context">Australian Tolerance Spec</div>
            </div>
          </div>

          <!-- Dual Column: Urgent Melbourne Orders & Quality Radar -->
          <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 24px; margin-bottom: 24px;">
            <!-- Urgent Melbourne Orders -->
            <div class="card">
              <div class="card-title">
                <span>Critical Melbourne Dispatch Orders (Cutoff Risk)</span>
                <span class="status-badge warning">3 High Priority</span>
              </div>
              <div class="data-table-container" style="margin-bottom: 0;">
                <table class="data-table">
                  <thead>
                    <tr>
                      <th>Job Order #</th>
                      <th>Project / Client</th>
                      <th>Items</th>
                      <th>Current Stage</th>
                      <th>Cutoff Target</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong style="color: var(--gold);">DSM-MEL-8841</strong></td>
                      <td>Bayside Commercial Office</td>
                      <td>280 Flashings</td>
                      <td><span class="status-badge in">Bending (Brake #2)</span></td>
                      <td><span style="color: #FFA5A2; font-family: var(--font-mono);">15:30 AEDT</span></td>
                    </tr>
                    <tr>
                      <td><strong style="color: var(--gold);">DSM-MEL-8849</strong></td>
                      <td>Docklands High-Rise Facade</td>
                      <td>42 Wall Panels</td>
                      <td><span class="status-badge warning">Double-Check Pending</span></td>
                      <td><span style="color: #FFA5A2; font-family: var(--font-mono);">16:00 AEDT</span></td>
                    </tr>
                    <tr>
                      <td><strong style="color: var(--gold);">DSM-MEL-8854</strong></td>
                      <td>Monash Health Specialty Ward</td>
                      <td>120 Parapet Cappings</td>
                      <td><span class="status-badge verified">Verified Ready</span></td>
                      <td><span style="color: #79D2B7; font-family: var(--font-mono);">17:30 AEDT</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Quality Radar & Live Incidents -->
            <div class="card">
              <div class="card-title">
                <span>Active Quality & Resupply Cases</span>
                <span class="status-badge alert" id="cmd-quality-count">2 Active</span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 12px;">
                <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
                  <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <strong style="color: var(--white); font-size: 13px;">#QC-2027-084: Angle Clearance Variance</strong>
                    <span class="status-badge alert">Under Review</span>
                  </div>
                  <div style="font-size: 12px; color: var(--steel); margin-bottom: 6px;">
                    Melbourne Tullamarine dry-fit observed 93° vs 90° specification on radius parapet flashing.
                  </div>
                  <div style="font-size: 11px; color: var(--gold); font-family: var(--font-mono);">
                    Assigned: Team Alpha • Corrective revision B validated
                  </div>
                </div>

                <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
                  <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <strong style="color: var(--white); font-size: 13px;">#QC-2027-081: Notch Corner Interference</strong>
                    <span class="status-badge verified">Corrected</span>
                  </div>
                  <div style="font-size: 12px; color: var(--steel); margin-bottom: 6px;">
                    Corner notching clearance on cladding cassette panel adjusted for 2.0mm aluminum bend radius.
                  </div>
                  <div style="font-size: 11px; color: var(--steel-dim); font-family: var(--font-mono);">
                    Assigned: Team Gamma • Drawing template updated
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 2. BIOMETRIC ATTENDANCE & BREAK MANAGEMENT -->
        <div class="view-panel" id="view-biometric">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Biometric Attendance & Break Management</h1>
              <div class="view-header-subtitle">
                Simulated biometric hardware punch feed, tea/lunch break duration tracking, and policy-driven regularization workflows.
              </div>
            </div>
            <div style="display: flex; gap: 10px;">
              <button class="btn btn-outline btn-sm" onclick="openModal('modal-biometric-punch')">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
                Log Manual Regularization
              </button>
            </div>
          </div>

          <!-- Hardware Diagnostics Banner -->
          <div class="card" style="margin-bottom: 24px; background: rgba(24, 38, 49, 0.6); border: 1px solid var(--slate-border-light);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
              <div style="display: flex; align-items: center; gap: 12px;">
                <span class="status-badge verified">Hardware Online</span>
                <strong style="color: var(--white); font-size: 14px;">Terminal 01: DSM-BIO-BLR-MAIN (Main Entry Turnstile)</strong>
              </div>
              <div style="font-family: var(--font-mono); font-size: 11px; color: var(--gold);">
                Demo Mode — Simulated Biometric Event Feed
              </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 16px; font-family: var(--font-mono); font-size: 12px; color: var(--steel);">
              <div>IP: <strong style="color: var(--porcelain);">192.168.10.45</strong></div>
              <div>Firmware: <strong style="color: var(--porcelain);">v4.8.2-DSM</strong></div>
              <div>Heartbeat: <strong style="color: #79D2B7;">2m ago (OK)</strong></div>
              <div>Clock Drift: <strong style="color: var(--porcelain);">+0.4s</strong></div>
              <div>Sync Protocol: <strong style="color: var(--porcelain);">Push SDK / Webhook</strong></div>
            </div>
          </div>

          <!-- Employee Visual Attendance Timeline & Break Analyzer -->
          <div class="card" style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
              <div>
                <span style="font-size: 15px; font-weight: 600; color: var(--white);">Employee Visual Attendance Timeline</span>
                <span style="font-size: 12px; color: var(--steel); margin-left: 8px;">Select employee to inspect punch events & break intervals:</span>
              </div>
              <select class="form-select" id="timeline-emp-select" style="width: 280px;" onchange="renderBiometricTimeline(this.value)">
                <!-- Injected via JS -->
              </select>
            </div>

            <!-- Day Summary Card -->
            <div id="timeline-summary-container" style="margin-bottom: 20px;">
              <!-- Injected via JS -->
            </div>

            <!-- Disclaimer Banner -->
            <div style="padding: 10px 16px; background: rgba(16, 25, 35, 0.7); border: 1px solid var(--slate-border); border-radius: 6px; font-size: 12px; color: var(--steel); margin-bottom: 20px;">
              <strong style="color: var(--gold);">Fairness & Policy Note:</strong> Biometric timestamps establish physical entry and exit records. Recorded presence does not automatically equate to productive hours or payable time. Overtime eligibility and payable hours strictly follow configured enterprise award rules and supervisor sign-off.
            </div>

            <!-- Visual SVG/CSS Timeline -->
            <div id="timeline-visual-container">
              <!-- Injected via JS -->
            </div>
          </div>

          <!-- Raw Biometric Punch Stream -->
          <div class="card">
            <div class="card-title">
              <span>Live Ingested Biometric Punch Event Feed</span>
              <div style="display: flex; gap: 8px;">
                <button class="btn btn-outline btn-sm" onclick="filterPunchFeed('ALL')">All Events</button>
                <button class="btn btn-outline btn-sm" onclick="filterPunchFeed('IN')">Office IN</button>
                <button class="btn btn-outline btn-sm" onclick="filterPunchFeed('OUT')">Office OUT</button>
                <button class="btn btn-outline btn-sm" onclick="filterPunchFeed('BREAK')">Breaks</button>
                <button class="btn btn-outline btn-sm" onclick="filterPunchFeed('EXCEPTION')">Exceptions</button>
              </div>
            </div>
            <div class="data-table-container">
              <table class="data-table" id="biometric-punches-table">
                <thead>
                  <tr>
                    <th>Punch ID</th>
                    <th>Employee ID</th>
                    <th>Name</th>
                    <th>Timestamp (IST)</th>
                    <th>Event Type</th>
                    <th>Terminal / Device</th>
                    <th>Auth Method</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody id="biometric-punches-tbody">
                  <!-- Injected via JS -->
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- 3. EMPLOYEE 360-DEGREE DASHBOARD -->
        <div class="view-panel" id="view-employee360">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Employee 360° Intelligence Profile</h1>
              <div class="view-header-subtitle">
                Holistic capability, attendance regularity, shopfloor output velocity, and confidential development reviews.
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 12px;">
              <span class="form-label" style="margin-bottom: 0;">Select Profile:</span>
              <select class="form-select" id="emp360-selector" style="width: 320px;" onchange="renderEmployee360(this.value)">
                <!-- Injected via JS -->
              </select>
            </div>
          </div>

          <!-- Flagship 360 Content Container -->
          <div id="emp360-content-container">
            <!-- Injected via JS -->
          </div>
        </div>

        <!-- 4. OPERATIONS DASHBOARD (EXISTING) -->
        <div class="view-panel" id="view-dashboard">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Operations Performance Dashboard</h1>
              <div class="view-header-subtitle">
                Aggregate team metrics across Flashings, Architectural Panels, Rainwater Goods, and Special Assemblies.
              </div>
            </div>
          </div>
          <!-- Injected via JS -->
          <div id="dashboard-content-container"></div>
        </div>

        <!-- 5. ATTENDANCE REGISTRY (40 EMPLOYEES) -->
        <div class="view-panel" id="view-attendance">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Attendance & Shift Registry</h1>
              <div class="view-header-subtitle">
                Comprehensive 40-employee roster tracking shift allocations, punch regularity, and attendance status.
              </div>
            </div>
            <div style="display: flex; gap: 10px;">
              <input type="text" id="attendance-search" class="form-input" style="width: 220px;" placeholder="Search employee..." onkeyup="filterAttendanceTable()" />
              <select id="attendance-filter-team" class="form-select" style="width: 180px;" onchange="filterAttendanceTable()">
                <option value="ALL">All Teams</option>
                <option value="Team Alpha">Team Alpha</option>
                <option value="Team Beta">Team Beta</option>
                <option value="Team Gamma">Team Gamma</option>
                <option value="Team Delta">Team Delta</option>
              </select>
            </div>
          </div>
          <div class="data-table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Emp ID</th>
                  <th>Employee Name</th>
                  <th>Team & Department</th>
                  <th>Assigned Shift</th>
                  <th>Entry Punch</th>
                  <th>Exit Punch</th>
                  <th>Attended Hours</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody id="attendance-tbody">
                <!-- Injected via JS -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- 6. LEAVE MANAGEMENT -->
        <div class="view-panel" id="view-leave">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Leave Management & Regularization</h1>
              <div class="view-header-subtitle">
                Structured approvals, team coverage impact checks, and leave ledger records.
              </div>
            </div>
            <button class="btn btn-gold btn-sm" onclick="openApplyLeaveModal()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
              Apply Leave Request
            </button>
          </div>
          <div id="leave-content-container"></div>
        </div>

        <!-- 7. CAPACITY & COVERAGE PLANNER -->
        <div class="view-panel" id="view-capacity">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Workforce Capacity & Coverage Planner</h1>
              <div class="view-header-subtitle">
                14-day forward schedule heatmap, minimum staffing threshold guards, and cross-trained backup recommendations.
              </div>
            </div>
          </div>
          <div id="capacity-content-container"></div>
        </div>

        <!-- 8. DAILY PRODUCTION ENTRY -->
        <div class="view-panel" id="view-production">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Daily Production Entry & Floor Log</h1>
              <div class="view-header-subtitle">
                Shopfloor keying volume, linear meters of flashings, bits detailed, and double-check records.
              </div>
            </div>
            <button class="btn btn-gold btn-sm" onclick="openProductionModal()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
              Log Daily Output
            </button>
          </div>
          <div id="production-content-container"></div>
        </div>

        <!-- 9. QUALITY & RESUPPLY CASES -->
        <div class="view-panel" id="view-quality">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Quality Assurance & Zero-Blame Resupply RCA</h1>
              <div class="view-header-subtitle">
                Connecting Australian field variances to root-cause drawings for continuous operational learning.
              </div>
            </div>
          </div>
          <div id="quality-content-container"></div>
        </div>

        <!-- 10. SHIFT HANDOVER MODULE -->
        <div class="view-panel" id="view-handover">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Shift Handover Experience</h1>
              <div class="view-header-subtitle">
                Structured digital handover dossiers transferring WIP jobs, Melbourne order priorities, and equipment status.
              </div>
            </div>
            <button class="btn btn-gold btn-sm" onclick="openModal('modal-create-handover')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
              Create Handover Dossier
            </button>
          </div>
          <div id="handover-content-container"></div>
        </div>

        <!-- 11. END-OF-SHIFT REPORT -->
        <div class="view-panel" id="view-shift-report">
          <div class="view-header no-print">
            <div>
              <h1 class="view-header-title">End-of-Shift Intelligence Report</h1>
              <div class="view-header-subtitle">
                Formatted executive summary report for shift performance, attendance reconciliation, and printable archiving.
              </div>
            </div>
            <div style="display: flex; gap: 10px;">
              <button class="btn btn-outline btn-sm" onclick="exportShiftReportCSV()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                Export CSV
              </button>
              <button class="btn btn-gold btn-sm" onclick="printShiftReport()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
                Print / Save PDF
              </button>
            </div>
          </div>
          <div id="shift-report-content-container"></div>
        </div>

        <!-- 12. MANAGEMENT EXCEPTIONS & ALERTS -->
        <div class="view-panel" id="view-exceptions">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Management Exceptions & Alerts Inbox</h1>
              <div class="view-header-subtitle">
                Triage missing punches, late arrivals, quality discrepancies, and staffing threshold risks.
              </div>
            </div>
          </div>
          <div id="exceptions-content-container"></div>
        </div>

        <!-- 13. SKILLS & TRAINING MATRIX -->
        <div class="view-panel" id="view-skills">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Employee Skills & Training Matrix</h1>
              <div class="view-header-subtitle">
                7-point sheet-metal operational proficiency matrix tracking operator mastery from Trainee to Master Trainer.
              </div>
            </div>
          </div>
          <div id="skills-content-container"></div>
        </div>

        <!-- 14. CUSTOM REPORT BUILDER -->
        <div class="view-panel" id="view-report-builder">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Custom Report Builder & Data Query</h1>
              <div class="view-header-subtitle">
                Filter by team, shift, date range, and operational metrics with on-the-fly table generation and CSV export.
              </div>
            </div>
          </div>
          <div id="report-builder-content-container"></div>
        </div>

        <!-- 15. CSV / EXCEL IMPORT CENTRE -->
        <div class="view-panel" id="view-import">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Excel & CSV Data Import Centre</h1>
              <div class="view-header-subtitle">
                Upload raw punch logs or shopfloor rosters, preview parsed rows, map fields, and execute live state updates.
              </div>
            </div>
          </div>
          <div id="import-content-container"></div>
        </div>

        <!-- 16. RECOGNITION & ROLES -->
        <div class="view-panel" id="view-recognition">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Merit, Recognition & Peer Awards</h1>
              <div class="view-header-subtitle">
                Monthly craftsmanship awards, safety badges, and peer commendations.
              </div>
            </div>
            <button class="btn btn-gold btn-sm" onclick="openNominationModal()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
              Nominate Colleague
            </button>
          </div>
          <div id="recognition-content-container"></div>
        </div>

        <div class="view-panel" id="view-roles">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Role & Security Permissions Matrix</h1>
              <div class="view-header-subtitle">
                Granular access control ensuring operational visibility while strictly protecting confidential development notes.
              </div>
            </div>
          </div>
          <div id="roles-content-container"></div>
        </div>

      </main>
    </div>
  </div>

  <!-- =========================================================================
       MODALS
       ========================================================================= -->
  <!-- 1. Biometric Regularization Modal -->
  <div class="modal-backdrop" id="modal-biometric-punch">
    <div class="modal-box">
      <div class="modal-header">
        <h3 class="modal-title">Log Biometric Regularization / Manual Punch</h3>
        <button class="modal-close" onclick="closeModal('modal-biometric-punch')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label">Employee</label>
          <select class="form-select" id="manual-punch-emp">
            <!-- Injected via JS -->
          </select>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
          <div class="form-group">
            <label class="form-label">Punch Event Type</label>
            <select class="form-select" id="manual-punch-type">
              <option value="Office IN">Office IN (Shift Entry)</option>
              <option value="Office OUT">Office OUT (Shift Departure)</option>
              <option value="Break START">Break START (Tea / Lunch)</option>
              <option value="Break END">Break END (Break Return)</option>
              <option value="Manual Regularization">Manual Regularization / Drift Correction</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">Time (IST)</label>
            <input type="time" class="form-input" id="manual-punch-time" value="06:00" />
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Reason for Manual Entry</label>
          <select class="form-select" id="manual-punch-reason">
            <option value="Hardware Reader Time Drift">Hardware Reader Time Drift</option>
            <option value="Sensor Missed Scan">Sensor Missed Scan</option>
            <option value="Approved Off-Site Transit">Approved Off-Site Transit</option>
            <option value="Emergency Shift Overtime">Emergency Shift Overtime</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Manager Verification Note</label>
          <textarea class="form-textarea" id="manual-punch-note" rows="2" placeholder="e.g. Verified by Team Leader Priya Nair via turnstile gate log."></textarea>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-outline btn-sm" onclick="closeModal('modal-biometric-punch')">Cancel</button>
        <button class="btn btn-gold btn-sm" onclick="submitManualBiometricPunch()">Commit Regularization</button>
      </div>
    </div>
  </div>

  <!-- 2. Create Handover Modal -->
  <div class="modal-backdrop" id="modal-create-handover">
    <div class="modal-box">
      <div class="modal-header">
        <h3 class="modal-title">Create Shift Handover Dossier</h3>
        <button class="modal-close" onclick="closeModal('modal-create-handover')">&times;</button>
      </div>
      <div class="modal-body">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
          <div class="form-group">
            <label class="form-label">Outgoing Shift</label>
            <input type="text" class="form-input" id="handover-out-shift" value="Shift A (Day)" readonly />
          </div>
          <div class="form-group">
            <label class="form-label">Incoming Shift</label>
            <input type="text" class="form-input" id="handover-in-shift" value="Shift B (Afternoon)" readonly />
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Critical Melbourne Orders Transferred</label>
          <input type="text" class="form-input" id="handover-urgent-jobs" value="DSM-MEL-8841 (Bayside Commercial, 280 pcs)" />
        </div>
        <div class="form-group">
          <label class="form-label">Shopfloor Machinery & Maintenance Notes</label>
          <textarea class="form-textarea" id="handover-machinery-notes" rows="2" placeholder="e.g. Brake Press #2 hydraulic check completed; Guillotine #1 blade alignment verified."></textarea>
        </div>
        <div class="form-group">
          <label class="form-label">Staffing & Skill Handover Observations</label>
          <textarea class="form-textarea" id="handover-staffing-notes" rows="2" placeholder="e.g. Night shift requires 1 backup keyer for custom radii flashings."></textarea>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-outline btn-sm" onclick="closeModal('modal-create-handover')">Cancel</button>
        <button class="btn btn-gold btn-sm" onclick="submitNewHandover()">Publish Handover</button>
      </div>
    </div>
  </div>

  <!-- 3. Resolve Exception Modal -->
  <div class="modal-backdrop" id="modal-resolve-alert">
    <div class="modal-box">
      <div class="modal-header">
        <h3 class="modal-title">Resolve Management Exception</h3>
        <button class="modal-close" onclick="closeModal('modal-resolve-alert')">&times;</button>
      </div>
      <div class="modal-body">
        <input type="hidden" id="resolve-alert-id" />
        <div class="form-group">
          <label class="form-label">Exception Details</label>
          <div id="resolve-alert-desc" style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px; font-size: 13px; color: var(--porcelain);"></div>
        </div>
        <div class="form-group">
          <label class="form-label">Resolution Action & Leadership Notes</label>
          <textarea class="form-textarea" id="resolve-alert-notes" rows="3" placeholder="Describe corrective action taken..."></textarea>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-outline btn-sm" onclick="closeModal('modal-resolve-alert')">Cancel</button>
        <button class="btn btn-gold btn-sm" onclick="submitResolveAlert()">Mark as Resolved</button>
      </div>
    </div>
  </div>

  <!-- 4. Apply Leave Modal -->
  <div class="modal-backdrop" id="modal-apply-leave">
    <div class="modal-box">
      <div class="modal-header">
        <h3 class="modal-title">Apply Leave Request</h3>
        <button class="modal-close" onclick="closeModal('modal-apply-leave')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label">Employee</label>
          <select class="form-select" id="leave-emp-select">
            <!-- Injected via JS -->
          </select>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
          <div class="form-group">
            <label class="form-label">Leave Type</label>
            <select class="form-select" id="leave-type-select">
              <option value="Annual Leave">Annual Leave</option>
              <option value="Sick Leave">Sick / Medical Leave</option>
              <option value="Casual Leave">Casual Leave</option>
              <option value="Compensatory Off">Compensatory Off</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">Date</label>
            <input type="date" class="form-input" id="leave-date-input" value="2027-03-26" />
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Reason (Confidential HR Protected)</label>
          <input type="text" class="form-input" id="leave-reason-input" placeholder="e.g. Scheduled medical appointment" />
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-outline btn-sm" onclick="closeModal('modal-apply-leave')">Cancel</button>
        <button class="btn btn-gold btn-sm" onclick="submitLeaveRequest()">Submit Request</button>
      </div>
    </div>
  </div>

  <!-- 5. Production Entry Modal -->
  <div class="modal-backdrop" id="modal-production-entry">
    <div class="modal-box">
      <div class="modal-header">
        <h3 class="modal-title">Log Daily Production Output</h3>
        <button class="modal-close" onclick="closeModal('modal-production-entry')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label">Team & Shift</label>
          <select class="form-select" id="prod-team-select">
            <option value="Team Alpha">Team Alpha — Shift A</option>
            <option value="Team Beta">Team Beta — Shift A</option>
            <option value="Team Gamma">Team Gamma — Shift B</option>
            <option value="Team Delta">Team Delta — Shift C (Night)</option>
          </select>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
          <div class="form-group">
            <label class="form-label">Orders Processed</label>
            <input type="number" class="form-input" id="prod-orders-input" value="24" />
          </div>
          <div class="form-group">
            <label class="form-label">Flashings Detailed (m)</label>
            <input type="number" class="form-input" id="prod-flashings-input" value="380" />
          </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
          <div class="form-group">
            <label class="form-label">Bits & Accessories</label>
            <input type="number" class="form-input" id="prod-bits-input" value="950" />
          </div>
          <div class="form-group">
            <label class="form-label">Double-Checks Done</label>
            <input type="number" class="form-input" id="prod-checks-input" value="23" />
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-outline btn-sm" onclick="closeModal('modal-production-entry')">Cancel</button>
        <button class="btn btn-gold btn-sm" onclick="submitProductionEntry()">Record Output</button>
      </div>
    </div>
  </div>

  <!-- 6. Nominate Award Modal -->
  <div class="modal-backdrop" id="modal-nominate">
    <div class="modal-box">
      <div class="modal-header">
        <h3 class="modal-title">Nominate for Craftsmanship & Merit</h3>
        <button class="modal-close" onclick="closeModal('modal-nominate')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label">Colleague to Nominate</label>
          <select class="form-select" id="nominate-emp-select">
            <!-- Injected via JS -->
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Category</label>
          <select class="form-select" id="nominate-category">
            <option value="Precision Craftsmanship">Precision Craftsmanship (Zero-Defect Detailing)</option>
            <option value="Shopfloor Safety Guardian">Shopfloor Safety Guardian</option>
            <option value="Cross-Border Collaboration">Cross-Border Collaboration Excellence</option>
            <option value="Technical Mentorship">Technical Mentorship & Peer Growth</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Citation & Justification</label>
          <textarea class="form-textarea" id="nominate-citation" rows="3" placeholder="Describe the specific contribution..."></textarea>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-outline btn-sm" onclick="closeModal('modal-nominate')">Cancel</button>
        <button class="btn btn-gold btn-sm" onclick="submitNomination()">Submit Nomination</button>
      </div>
    </div>
  </div>

  <!-- 7. Scene Navigation Overview Modal -->
  <div class="modal-backdrop" id="modal-scene-overview">
    <div class="modal-box" style="max-width: 780px;">
      <div class="modal-header">
        <h3 class="modal-title">Executive Presentation Outline</h3>
        <button class="modal-close" onclick="closeModal('modal-scene-overview')">&times;</button>
      </div>
      <div class="modal-body" style="padding: 16px;">
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;" id="scene-overview-grid">
          <!-- Injected via JS -->
        </div>
      </div>
    </div>
  </div>

  <!-- Toast Notification Container -->
  <div id="toast-container"></div>
"""

print("parts_product_views.py created successfully.")
