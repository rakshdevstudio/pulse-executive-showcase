# Explore Product Mode Application Views and Modals
# Human-Centered Plain-Language Design for Design Sheetmetal India Operations

def get_product_views_html(dsm_logo_b64):
    return f"""
  <!-- =========================================================================
       2. EXPLORE PRODUCT MODE (WORKFORCE OPERATIONS PLATFORM)
       ========================================================================= -->
  <div id="product-mode-container" class="hidden">
    <!-- Application Top Bar -->
    <header class="app-topbar">
      <div class="topbar-left">
        <img src="data:image/png;base64,{dsm_logo_b64}" alt="Design Sheetmetal" class="dsm-logo" />
        <span style="display: inline-block; width: 1px; height: 20px; background: rgba(147, 163, 174, 0.25); margin: 0 4px;"></span>
        <div style="display: flex; align-items: center; gap: 8px;">
          <span class="pulse-dot"></span>
          <span style="font-family: var(--font-serif); font-size: 16px; letter-spacing: 0.16em; font-weight: 600; color: var(--white);">PULSE</span>
          <span class="presenter-pill">Presented by Rakshith</span>
        </div>
        
        <div style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: rgba(198, 166, 117, 0.1); border: 1px solid var(--gold-border); border-radius: 14px; font-size: 11px; color: var(--gold); font-family: var(--font-mono);">
          <span>Demo Shift:</span>
          <strong>Monday, 23 Nov 2026</strong>
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
            <option value="PRESENTER" selected>Presenter (Rakshith, Operational Strategist)</option>
            <option value="MANAGEMENT">Managing Director (David Harrison)</option>
            <option value="TEAM_LEADER">Team Leader (Priya Nair, Shift A)</option>
            <option value="EMPLOYEE">Employee (Rohan Sharma, Keying Specialist)</option>
            <option value="SUPER_ADMIN">System Admin (Alex Vance)</option>
          </select>
        </div>

        <div class="user-pill">
          <div class="user-avatar" id="user-avatar-badge">RK</div>
          <div class="user-meta">
            <span class="user-name" id="user-name-display">Rakshith</span>
            <span class="user-role-title" id="user-role-display">Operational Strategist</span>
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
      <!-- Sidebar Navigation with Human-Centered Names -->
      <aside class="app-sidebar">
        <div class="nav-section-title">Management</div>
        <ul class="sidebar-menu">
          <li class="menu-item active" onclick="switchView('command-centre')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="12 6 12 12 16 14"/></svg>
            <span>Today's Operations</span>
            <span class="menu-badge gold">LIVE</span>
          </li>
          <li class="menu-item" onclick="switchView('dashboard')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="9"/><rect x="14" y="3" width="7" height="5"/><rect x="14" y="12" width="7" height="9"/><rect x="3" y="16" width="7" height="5"/></svg>
            <span>Performance Overview</span>
          </li>
          <li class="menu-item" onclick="switchView('exceptions')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
            <span>Issues & Alerts</span>
            <span class="menu-badge alert" id="badge-alerts-count">5</span>
          </li>
        </ul>

        <div class="nav-section-title">Workforce & Attendance</div>
        <ul class="sidebar-menu">
          <li class="menu-item" onclick="switchView('biometric')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 0 0-10 10c0 4.42 2.87 8.17 6.84 9.5.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34-.46-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.87 1.52 2.34 1.07 2.91.83.09-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.92 0-1.11.38-2 1.03-2.71-.1-.25-.45-1.29.1-2.64 0 0 .84-.27 2.75 1.02.79-.22 1.65-.33 2.5-.33.85 0 1.71.11 2.5.33 1.91-1.29 2.75-1.02 2.75-1.02.55 1.35.2 2.39.1 2.64.65.71 1.03 1.6 1.03 2.71 0 3.82-2.34 4.66-4.57 4.91.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2z"/></svg>
            <span>Entry, Exit & Breaks</span>
            <span class="menu-badge">SIM</span>
          </li>
          <li class="menu-item" onclick="switchView('employee360')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="7" r="4"/><path d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2"/></svg>
            <span>Employee Performance</span>
            <span class="menu-badge gold">360°</span>
          </li>
          <li class="menu-item" onclick="switchView('attendance')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            <span>Attendance Register</span>
            <span class="menu-badge" id="badge-present-count">36</span>
          </li>
          <li class="menu-item" onclick="switchView('leave')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            <span>Leave Management</span>
            <span class="menu-badge alert" id="badge-leave-pending">1 pending</span>
          </li>
          <li class="menu-item" onclick="switchView('capacity')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
            <span>Staff Availability</span>
          </li>
        </ul>

        <div class="nav-section-title">Daily Work & Quality</div>
        <ul class="sidebar-menu">
          <li class="menu-item" onclick="switchView('production')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
            <span>Daily Work Report</span>
          </li>
          <li class="menu-item" onclick="switchView('quality')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span>Errors & Resupplies</span>
            <span class="menu-badge alert" id="badge-quality-active">2 open</span>
          </li>
          <li class="menu-item" onclick="switchView('handover')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>
            <span>Shift Handover</span>
          </li>
          <li class="menu-item" onclick="switchView('shift-report')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
            <span>Daily Summary</span>
            <span class="menu-badge">PDF</span>
          </li>
        </ul>

        <div class="nav-section-title">Skills & Tools</div>
        <ul class="sidebar-menu">
          <li class="menu-item" onclick="switchView('skills')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            <span>Skills & Training</span>
          </li>
          <li class="menu-item" onclick="switchView('report-builder')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
            <span>Reports & Exports</span>
          </li>
          <li class="menu-item" onclick="switchView('import')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
            <span>Import Data</span>
          </li>
          <li class="menu-item" onclick="switchView('recognition')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>
            <span>Employee Recognition</span>
          </li>
          <li class="menu-item" onclick="switchView('roles')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            <span>Users & Permissions</span>
          </li>
        </ul>
      </aside>

      <!-- Main Application Content Area -->
      <main class="app-main">

        <!-- 1. TODAY'S OPERATIONS (FORMERLY COMMAND CENTRE) -->
        <div class="view-panel active" id="view-command-centre">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Today's Operations</h1>
              <div class="view-header-subtitle">
                Monday, 23 November 2026 • Shift A (Day Shift: 06:00 – 14:30 IST) • Real-time overview of attendance, completed work, and items needing attention.
              </div>
            </div>
            <div style="display: flex; gap: 10px;">
              <button class="btn btn-outline btn-sm" onclick="switchView('shift-report')">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
                Daily Summary (PDF)
              </button>
              <button class="btn btn-gold btn-sm" onclick="switchView('handover')">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/></svg>
                Shift Handover
              </button>
            </div>
          </div>

          <!-- Active Shift Ribbon -->
          <div class="card" style="margin-bottom: 24px; background: rgba(24, 38, 49, 0.7); border: 1px solid var(--gold-border);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
              <div style="display: flex; align-items: center; gap: 12px;">
                <span class="pulse-dot"></span>
                <strong style="color: var(--white); font-size: 15px;">Shift A (Day Shift: 06:00 — 14:30 IST)</strong>
                <span class="status-badge in">Active on Shopfloor</span>
              </div>
              <div style="font-family: var(--font-mono); font-size: 12px; color: var(--gold);">
                Shift Progress: 82% completed • Handover to Shift B at 14:30 IST
              </div>
            </div>
            <div style="height: 6px; background: rgba(147, 163, 174, 0.15); border-radius: 3px; overflow: hidden; margin-bottom: 10px;">
              <div style="width: 82%; height: 100%; background: linear-gradient(90deg, var(--gold), #79D2B7); border-radius: 3px;"></div>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 11px; color: var(--steel-dim); font-family: var(--font-mono);">
              <span>06:00 IST Shift Started</span>
              <span>12:10 — 12:40 Lunch Window Completed</span>
              <span style="color: var(--gold);">14:30 IST Next Shift Starts</span>
            </div>
          </div>

          <!-- 4 Core Executive Summary Sections -->
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px;">
            <!-- Group 1: EMPLOYEES -->
            <div class="card" style="padding: 16px;">
              <div style="font-size: 11px; font-family: var(--font-mono); color: var(--gold); text-transform: uppercase; margin-bottom: 8px;">
                1. EMPLOYEES TODAY
              </div>
              <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
                <span style="font-size: 28px; font-weight: 600; color: var(--white); font-family: var(--font-serif);">36</span>
                <span style="font-size: 12px; color: #79D2B7;">Present / Clocked In</span>
              </div>
              <div style="font-size: 11px; color: var(--steel); display: flex; flex-direction: column; gap: 3px; padding-top: 8px; border-top: 1px solid rgba(147, 163, 174, 0.12);">
                <div>Scheduled: <strong>40 total employees</strong></div>
                <div>On Approved Leave: <strong style="color: var(--amber);">3 employees</strong></div>
                <div>Unplanned Absent: <strong style="color: #FFA5A2;">1 employee</strong></div>
                <div>Late Arrivals: <strong style="color: var(--steel);">2 (compensated)</strong></div>
              </div>
            </div>

            <!-- Group 2: WORK COMPLETED -->
            <div class="card" style="padding: 16px;">
              <div style="font-size: 11px; font-family: var(--font-mono); color: var(--gold); text-transform: uppercase; margin-bottom: 8px;">
                2. WORK COMPLETED
              </div>
              <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
                <span style="font-size: 28px; font-weight: 600; color: var(--gold); font-family: var(--font-serif);">142</span>
                <span style="font-size: 12px; color: var(--emerald);">Orders Keyed</span>
              </div>
              <div style="font-size: 11px; color: var(--steel); display: flex; flex-direction: column; gap: 3px; padding-top: 8px; border-top: 1px solid rgba(147, 163, 174, 0.12);">
                <div>Flashings Detailed: <strong>1,840 linear metres</strong></div>
                <div>Accessories & Bits: <strong>5,120 individual parts</strong></div>
                <div>Double-Checks Done: <strong style="color: #79D2B7;">138 verified (97.2%)</strong></div>
                <div>Shift Target: <strong>135 orders (+5.2%)</strong></div>
              </div>
            </div>

            <!-- Group 3: QUALITY -->
            <div class="card" style="padding: 16px;">
              <div style="font-size: 11px; font-family: var(--font-mono); color: var(--gold); text-transform: uppercase; margin-bottom: 8px;">
                3. QUALITY & ACCURACY
              </div>
              <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
                <span style="font-size: 28px; font-weight: 600; color: #79D2B7; font-family: var(--font-serif);">98.6%</span>
                <span style="font-size: 12px; color: #79D2B7;">First-Pass Accuracy</span>
              </div>
              <div style="font-size: 11px; color: var(--steel); display: flex; flex-direction: column; gap: 3px; padding-top: 8px; border-top: 1px solid rgba(147, 163, 174, 0.12);">
                <div>Open Error Cases: <strong style="color: var(--amber);">2 under review</strong></div>
                <div>Resupplies Being Checked: <strong>1 Melbourne order</strong></div>
                <div>Scrap Rework Cost: <strong>$280 AUD confirmed</strong></div>
                <div>Resolved Today: <strong style="color: #79D2B7;">1 case closed</strong></div>
              </div>
            </div>

            <!-- Group 4: NEEDS ATTENTION -->
            <div class="card" style="padding: 16px; border: 1px solid var(--gold-border);">
              <div style="font-size: 11px; font-family: var(--font-mono); color: var(--amber); text-transform: uppercase; margin-bottom: 8px;">
                4. NEEDS ATTENTION
              </div>
              <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
                <span style="font-size: 28px; font-weight: 600; color: var(--amber); font-family: var(--font-serif);">4</span>
                <span style="font-size: 12px; color: var(--amber);">Pending Items</span>
              </div>
              <div style="font-size: 11px; color: var(--porcelain); display: flex; flex-direction: column; gap: 3px; padding-top: 8px; border-top: 1px solid rgba(147, 163, 174, 0.12);">
                <div>• Missing Exit Punch: <strong style="color: var(--gold);">1 employee</strong></div>
                <div>• Leave Request: <strong style="color: var(--gold);">1 pending review</strong></div>
                <div>• Urgent Melbourne Cutoff: <strong style="color: #FFA5A2;">Order #8841 (16:00)</strong></div>
                <div>• Quality Case Review: <strong>QC-2026-084</strong></div>
              </div>
            </div>
          </div>

          <!-- Urgent Melbourne Orders and Open Issues -->
          <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 24px; margin-bottom: 24px;">
            <!-- Urgent Melbourne Orders -->
            <div class="card">
              <div class="card-title">
                <span>Orders Requiring Melbourne Dispatch Approval Today</span>
                <span class="status-badge warning">Deadline: 16:00 AEDT</span>
              </div>
              <div class="data-table-container" style="margin-bottom: 0;">
                <table class="data-table">
                  <thead>
                    <tr>
                      <th>Order #</th>
                      <th>Project / Client</th>
                      <th>Work Required</th>
                      <th>Current Stage</th>
                      <th>Cutoff Time</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong style="color: var(--gold);">DSM-MEL-8841</strong></td>
                      <td>St. Vincent Hospital Roof Cappings</td>
                      <td>280 Flashings</td>
                      <td><span class="status-badge in">Bending on Press #2</span></td>
                      <td><span style="color: #FFA5A2; font-family: var(--font-mono);">16:00 AEDT</span></td>
                    </tr>
                    <tr>
                      <td><strong style="color: var(--gold);">DSM-MEL-8849</strong></td>
                      <td>Docklands High-Rise Facade</td>
                      <td>42 Wall Panels</td>
                      <td><span class="status-badge warning">Double-Check in Progress</span></td>
                      <td><span style="color: #FFA5A2; font-family: var(--font-mono);">16:30 AEDT</span></td>
                    </tr>
                    <tr>
                      <td><strong style="color: var(--gold);">DSM-MEL-8854</strong></td>
                      <td>Monash Health Specialty Ward</td>
                      <td>120 Parapet Cappings</td>
                      <td><span class="status-badge verified">Verified & Ready</span></td>
                      <td><span style="color: #79D2B7; font-family: var(--font-mono);">17:30 AEDT</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Active Quality & Resupply Cases -->
            <div class="card">
              <div class="card-title">
                <span>Errors & Resupplies Requiring Action</span>
                <span class="status-badge alert">2 Open Cases</span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 12px;">
                <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
                  <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <strong style="color: var(--white); font-size: 13px;">QC-2026-084: Flashing Angle Variance (+3°)</strong>
                    <span class="status-badge alert">Cause Confirmed</span>
                  </div>
                  <div style="font-size: 12px; color: var(--steel); margin-bottom: 6px;">
                    Melbourne warehouse observed 93° angle instead of 90° specification on bend 3. Conflicting customer markup identified.
                  </div>
                  <div style="font-size: 11px; color: var(--gold); font-family: var(--font-mono);">
                    Investigator: Manoj Tiwari • Corrective action prompt active
                  </div>
                </div>

                <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
                  <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <strong style="color: var(--white); font-size: 13px;">QC-2026-081: Corner Notch Gap Discrepancy</strong>
                    <span class="status-badge verified">Action Taken</span>
                  </div>
                  <div style="font-size: 12px; color: var(--steel); margin-bottom: 6px;">
                    Corner notch gap was 1.5mm instead of 2.5mm required for bend radius. Standard CAD library updated.
                  </div>
                  <div style="font-size: 11px; color: var(--steel-dim); font-family: var(--font-mono);">
                    Investigator: Priya Nair • Closed for production
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 2. ENTRY, EXIT & BREAKS (FORMERLY BIOMETRIC ATTENDANCE) -->
        <div class="view-panel" id="view-biometric">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Entry, Exit & Breaks</h1>
              <div class="view-header-subtitle">
                Review employee turnstile check-ins, tea breaks, lunch breaks, and verified attendance times.
              </div>
            </div>
            <div style="display: flex; gap: 10px;">
              <button class="btn btn-outline btn-sm" onclick="openModal('modal-biometric-punch')">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
                Log Manual Punch Correction
              </button>
            </div>
          </div>

          <!-- Employee Attendance Timeline (SHOWN FIRST) -->
          <div class="card" style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
              <div>
                <span style="font-size: 15px; font-weight: 600; color: var(--white);">Employee Daily Attendance Timeline</span>
                <span style="font-size: 12px; color: var(--steel); margin-left: 8px;">Select an employee to see their recorded check-ins and breaks:</span>
              </div>
              <select class="form-select" id="timeline-emp-select" style="width: 300px;" onchange="renderBiometricTimeline(this.value)">
                <!-- Injected via JS -->
              </select>
            </div>

            <!-- Day Summary Card -->
            <div id="timeline-summary-container" style="margin-bottom: 20px;">
              <!-- Injected via JS -->
            </div>

            <!-- Plain-Language Policy Note -->
            <div style="padding: 10px 16px; background: rgba(16, 25, 35, 0.7); border: 1px solid var(--slate-border); border-radius: 6px; font-size: 12px; color: var(--steel); margin-bottom: 20px;">
              <strong style="color: var(--gold);">Attendance Policy Note:</strong> Turnstile timestamps record when employees enter and leave the office. Time spent on premises does not automatically equate to productive hours or payable overtime, which follows standard company approval rules.
            </div>

            <!-- Visual Timeline -->
            <div id="timeline-visual-container">
              <!-- Injected via JS -->
            </div>

            <!-- Technical Diagnostics under Expandable Details (Section 8) -->
            <details style="margin-top: 20px; padding: 12px 16px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px; cursor: pointer;">
              <summary style="font-family: var(--font-mono); font-size: 12px; color: var(--steel); outline: none;">
                Advanced: Device Information & Technical Diagnostics
              </summary>
              <div style="margin-top: 14px; padding-top: 12px; border-top: 1px solid rgba(147, 163, 174, 0.15); display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; font-size: 12px; font-family: var(--font-mono); color: var(--steel);">
                <div>Terminal: <strong style="color: var(--white);">DSM-BIO-BLR-01 (Main Turnstile)</strong></div>
                <div>IP Address: <strong style="color: var(--porcelain);">192.168.10.45</strong></div>
                <div>Firmware: <strong style="color: var(--porcelain);">v4.8.2-DSM</strong></div>
                <div>Sync Protocol: <strong style="color: var(--porcelain);">Push SDK / Webhook</strong></div>
                <div>Status: <strong style="color: #79D2B7;">Online (Latency: 18ms)</strong></div>
                <div>Heartbeat: <strong style="color: var(--porcelain);">2 minutes ago</strong></div>
                <div>Clock Drift: <strong style="color: var(--porcelain);">+0.4 seconds</strong></div>
                <div>Integration Mode: <strong style="color: var(--gold);">Simulated Hardware Feed</strong></div>
              </div>
            </details>
          </div>

          <!-- Raw Punch Events Stream -->
          <div class="card">
            <div class="card-title">
              <span>Today's Recorded Biometric Check-ins & Breaks</span>
              <div style="display: flex; gap: 8px;">
                <button class="btn btn-outline btn-sm" onclick="filterPunchFeed('ALL')">All Events</button>
                <button class="btn btn-outline btn-sm" onclick="filterPunchFeed('IN')">Office IN</button>
                <button class="btn btn-outline btn-sm" onclick="filterPunchFeed('OUT')">Office OUT</button>
                <button class="btn btn-outline btn-sm" onclick="filterPunchFeed('BREAK')">Breaks</button>
                <button class="btn btn-outline btn-sm" onclick="filterPunchFeed('EXCEPTION')">Corrections</button>
              </div>
            </div>
            <div class="data-table-container">
              <table class="data-table" id="biometric-punches-table">
                <thead>
                  <tr>
                    <th>Record ID</th>
                    <th>Employee ID</th>
                    <th>Employee Name</th>
                    <th>Time (IST)</th>
                    <th>Event Type</th>
                    <th>Location / Gate</th>
                    <th>Verification Method</th>
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

        <!-- 3. EMPLOYEE PERFORMANCE (FORMERLY EMPLOYEE 360°) -->
        <div class="view-panel" id="view-employee360">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Employee Performance</h1>
              <div class="view-header-subtitle">
                Work completed, attendance history, quality records, and skill training for each team member.
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 12px;">
              <span class="form-label" style="margin-bottom: 0;">Choose Employee:</span>
              <select class="form-select" id="emp360-selector" style="width: 320px;" onchange="renderEmployee360(this.value)">
                <!-- Injected via JS -->
              </select>
            </div>
          </div>

          <!-- 360 Content Container -->
          <div id="emp360-content-container">
            <!-- Injected via JS -->
          </div>
        </div>

        <!-- 4. PERFORMANCE OVERVIEW (FORMERLY OPERATIONS DASHBOARD) -->
        <div class="view-panel" id="view-dashboard">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Performance Overview</h1>
              <div class="view-header-subtitle">
                Weekly team performance trends across Flashings, Architectural Panels, Rainwater Goods, and Special Assemblies.
              </div>
            </div>
          </div>
          <div id="dashboard-content-container"></div>
        </div>

        <!-- 5. ATTENDANCE REGISTER (FORMERLY ATTENDANCE REGISTRY) -->
        <div class="view-panel" id="view-attendance">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Attendance Register</h1>
              <div class="view-header-subtitle">
                Complete list of all 40 employees showing scheduled shift, arrival time, departure time, and today's status.
              </div>
            </div>
            <div style="display: flex; gap: 10px;">
              <input type="text" id="attendance-search" class="form-input" style="width: 220px;" placeholder="Search by name or ID..." onkeyup="filterAttendanceTable()" />
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
                  <th>Employee ID</th>
                  <th>Employee Name</th>
                  <th>Team & Role</th>
                  <th>Assigned Shift</th>
                  <th>Entry Time</th>
                  <th>Exit Time</th>
                  <th>Hours Worked</th>
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
              <h1 class="view-header-title">Leave Management</h1>
              <div class="view-header-subtitle">
                Review and approve employee leave requests while maintaining required shift coverage.
              </div>
            </div>
            <button class="btn btn-gold btn-sm" onclick="openApplyLeaveModal()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
              Apply for Leave
            </button>
          </div>
          <div id="leave-content-container"></div>
        </div>

        <!-- 7. STAFF AVAILABILITY (FORMERLY CAPACITY & COVERAGE) -->
        <div class="view-panel" id="view-capacity">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Staff Availability</h1>
              <div class="view-header-subtitle">
                Weekly team staffing calendar with shortage warnings and recommended certified backup operators.
              </div>
            </div>
          </div>
          <div id="capacity-content-container"></div>
        </div>

        <!-- 8. DAILY WORK REPORT (FORMERLY PRODUCTION ENTRY) -->
        <div class="view-panel" id="view-production">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Daily Work Report</h1>
              <div class="view-header-subtitle">
                Record and review daily sheetmetal orders keyed, linear metres of flashings, and double-checks completed.
              </div>
            </div>
            <button class="btn btn-gold btn-sm" onclick="openProductionModal()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
              Record Today's Work
            </button>
          </div>
          <div id="production-content-container"></div>
        </div>

        <!-- 9. ERRORS & RESUPPLIES (FORMERLY QUALITY ASSURANCE & RCA) -->
        <div class="view-panel" id="view-quality">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Errors & Resupplies</h1>
              <div class="view-header-subtitle">
                Plain-language tracking of drawing variances, customer reported issues, and preventive actions.
              </div>
            </div>
          </div>
          <div id="quality-content-container"></div>
        </div>

        <!-- 10. SHIFT HANDOVER -->
        <div class="view-panel" id="view-handover">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Shift Handover</h1>
              <div class="view-header-subtitle">
                Seamless transition between shifts: Transfer urgent Melbourne orders, in-progress jobs, and machine maintenance notes.
              </div>
            </div>
            <button class="btn btn-gold btn-sm" onclick="openModal('modal-create-handover')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
              Create Handover
            </button>
          </div>
          <div id="handover-content-container"></div>
        </div>

        <!-- 11. DAILY SUMMARY (FORMERLY END-OF-SHIFT REPORT) -->
        <div class="view-panel" id="view-shift-report">
          <div class="view-header no-print">
            <div>
              <h1 class="view-header-title">Daily Operations Summary</h1>
              <div class="view-header-subtitle">
                End-of-shift operational overview ready for management review, CSV download, and printing.
              </div>
            </div>
            <div style="display: flex; gap: 10px;">
              <button class="btn btn-outline btn-sm" onclick="exportShiftReportCSV()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                Download CSV
              </button>
              <button class="btn btn-gold btn-sm" onclick="printShiftReport()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
                Print / Save PDF
              </button>
            </div>
          </div>
          <div id="shift-report-content-container"></div>
        </div>

        <!-- 12. ISSUES & ALERTS (FORMERLY MANAGEMENT EXCEPTIONS) -->
        <div class="view-panel" id="view-exceptions">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Issues & Alerts</h1>
              <div class="view-header-subtitle">
                Review and resolve missing punches, delayed jobs, quality checks, and staffing alerts.
              </div>
            </div>
          </div>
          <div id="exceptions-content-container"></div>
        </div>

        <!-- 13. SKILLS & TRAINING (FORMERLY SKILLS MATRIX) -->
        <div class="view-panel" id="view-skills">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Skills & Training</h1>
              <div class="view-header-subtitle">
                Design Sheetmetal tracks 7 core sheetmetal manufacturing skills across 4 recognized proficiency levels.
              </div>
            </div>
          </div>
          <div id="skills-content-container"></div>
        </div>

        <!-- 14. REPORTS & EXPORTS (FORMERLY CUSTOM REPORT BUILDER) -->
        <div class="view-panel" id="view-report-builder">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Reports & Exports</h1>
              <div class="view-header-subtitle">
                Create simple custom reports by selecting your team, date range, and information type.
              </div>
            </div>
          </div>
          <div id="report-builder-content-container"></div>
        </div>

        <!-- 15. IMPORT DATA (FORMERLY CSV / EXCEL IMPORT) -->
        <div class="view-panel" id="view-import">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Import Data</h1>
              <div class="view-header-subtitle">
                Upload CSV spreadsheets from biometric turnstiles or shift rosters to update records.
              </div>
            </div>
          </div>
          <div id="import-content-container"></div>
        </div>

        <!-- 16. EMPLOYEE RECOGNITION & PERMISSIONS -->
        <div class="view-panel" id="view-recognition">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Employee Recognition</h1>
              <div class="view-header-subtitle">
                Monthly peer commendations, craftsmanship stars, and safety milestones.
              </div>
            </div>
            <button class="btn btn-gold btn-sm" onclick="openNominationModal()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
              Nominate a Colleague
            </button>
          </div>
          <div id="recognition-content-container"></div>
        </div>

        <div class="view-panel" id="view-roles">
          <div class="view-header">
            <div>
              <h1 class="view-header-title">Users & Permissions</h1>
              <div class="view-header-subtitle">
                Role-based privacy controls ensuring employees only see appropriate information while leaders access supervisory tools.
              </div>
            </div>
          </div>
          <div id="roles-content-container"></div>
        </div>

      </main>
    </div>
  </div>

  <!-- =========================================================================
       MODALS (Plain Language, Practical Form Labels)
       ========================================================================= -->
  <!-- 1. Biometric Regularization Modal -->
  <div class="modal-backdrop" id="modal-biometric-punch">
    <div class="modal-box">
      <div class="modal-header">
        <h3 class="modal-title">Record Manual Punch Correction</h3>
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
            <label class="form-label">Punch Type</label>
            <select class="form-select" id="manual-punch-type">
              <option value="Office IN">Office IN (Shift Entry)</option>
              <option value="Office OUT">Office OUT (Shift Departure)</option>
              <option value="Break START">Break START (Tea / Lunch)</option>
              <option value="Break END">Break END (Break Return)</option>
              <option value="Manual Correction">Manual Correction</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">Time (IST)</label>
            <input type="time" class="form-input" id="manual-punch-time" value="06:00" />
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Reason for Correction</label>
          <select class="form-select" id="manual-punch-reason">
            <option value="Turnstile Sensor Missed Scan">Turnstile Sensor Missed Scan</option>
            <option value="Approved Transit Between Plants">Approved Transit Between Plants</option>
            <option value="Authorized Overtime Extension">Authorized Overtime Extension</option>
            <option value="Card Reader Offline">Card Reader Offline</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Supervisor Approval Note</label>
          <textarea class="form-textarea" id="manual-punch-note" rows="2" placeholder="e.g. Verified by Team Leader Priya Nair via security log."></textarea>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-outline btn-sm" onclick="closeModal('modal-biometric-punch')">Cancel</button>
        <button class="btn btn-gold btn-sm" onclick="submitManualBiometricPunch()">Save Correction</button>
      </div>
    </div>
  </div>

  <!-- 2. Create Handover Modal -->
  <div class="modal-backdrop" id="modal-create-handover">
    <div class="modal-box">
      <div class="modal-header">
        <h3 class="modal-title">Create Shift Handover</h3>
        <button class="modal-close" onclick="closeModal('modal-create-handover')">&times;</button>
      </div>
      <div class="modal-body">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
          <div class="form-group">
            <label class="form-label">From Shift</label>
            <input type="text" class="form-input" id="handover-out-shift" value="Shift A (Day: 06:00 — 14:30)" readonly />
          </div>
          <div class="form-group">
            <label class="form-label">To Shift</label>
            <input type="text" class="form-input" id="handover-in-shift" value="Shift B (Afternoon: 14:00 — 22:30)" readonly />
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Urgent Melbourne Orders</label>
          <input type="text" class="form-input" id="handover-urgent-jobs" value="DSM-MEL-8841 (St. Vincent Hospital Roof Cappings, 280 pcs)" />
        </div>
        <div class="form-group">
          <label class="form-label">Machinery & Tooling Notes</label>
          <textarea class="form-textarea" id="handover-machinery-notes" rows="2" placeholder="e.g. Brake Press #2 hydraulic check completed; slitter ready for next run."></textarea>
        </div>
        <div class="form-group">
          <label class="form-label">Staffing & Shift Observations</label>
          <textarea class="form-textarea" id="handover-staffing-notes" rows="2" placeholder="e.g. Night shift requires 1 backup detailer for custom curved profiles."></textarea>
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
        <h3 class="modal-title">Resolve Issue</h3>
        <button class="modal-close" onclick="closeModal('modal-resolve-alert')">&times;</button>
      </div>
      <div class="modal-body">
        <input type="hidden" id="resolve-alert-id" />
        <div class="form-group">
          <label class="form-label">Issue Summary</label>
          <div id="resolve-alert-desc" style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px; font-size: 13px; color: var(--porcelain);"></div>
        </div>
        <div class="form-group">
          <label class="form-label">Action Taken & Leadership Notes</label>
          <textarea class="form-textarea" id="resolve-alert-notes" rows="3" placeholder="Describe the corrective action taken to close this issue..."></textarea>
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
        <h3 class="modal-title">Apply for Leave</h3>
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
            <label class="form-label">Leave Date</label>
            <input type="date" class="form-input" id="leave-date-input" value="2026-11-27" />
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Reason (Confidential HR Protected)</label>
          <input type="text" class="form-input" id="leave-reason-input" placeholder="e.g. Scheduled personal appointment" />
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-outline btn-sm" onclick="closeModal('modal-apply-leave')">Cancel</button>
        <button class="btn btn-gold btn-sm" onclick="submitLeaveRequest()">Submit Leave Request</button>
      </div>
    </div>
  </div>

  <!-- 5. Production Entry Modal -->
  <div class="modal-backdrop" id="modal-production-entry">
    <div class="modal-box">
      <div class="modal-header">
        <h3 class="modal-title">Record Today's Work</h3>
        <button class="modal-close" onclick="closeModal('modal-production-entry')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label">Team & Shift</label>
          <select class="form-select" id="prod-team-select">
            <option value="Team Alpha">Team Alpha (Flashings & Trims) — Shift A</option>
            <option value="Team Beta">Team Beta (Architectural Panels) — Shift A</option>
            <option value="Team Gamma">Team Gamma (Rainwater Goods) — Shift B</option>
            <option value="Team Delta">Team Delta (Structural Trims) — Shift C</option>
          </select>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
          <div class="form-group">
            <label class="form-label">Orders Keyed (Total Orders)</label>
            <input type="number" class="form-input" id="prod-orders-input" value="26" />
          </div>
          <div class="form-group">
            <label class="form-label">Flashings Detailed (Linear Metres)</label>
            <input type="number" class="form-input" id="prod-flashings-input" value="380" />
          </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
          <div class="form-group">
            <label class="form-label">Accessories & Bits (Individual Parts)</label>
            <input type="number" class="form-input" id="prod-bits-input" value="950" />
          </div>
          <div class="form-group">
            <label class="form-label">Double-Checks Completed</label>
            <input type="number" class="form-input" id="prod-checks-input" value="25" />
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-outline btn-sm" onclick="closeModal('modal-production-entry')">Save Draft</button>
        <button class="btn btn-gold btn-sm" onclick="submitProductionEntry()">Submit Report</button>
      </div>
    </div>
  </div>

  <!-- 6. Nominate Award Modal -->
  <div class="modal-backdrop" id="modal-nominate">
    <div class="modal-box">
      <div class="modal-header">
        <h3 class="modal-title">Nominate a Colleague for Recognition</h3>
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
          <label class="form-label">Recognition Category</label>
          <select class="form-select" id="nominate-category">
            <option value="Precision Craftsmanship">Precision Craftsmanship (Zero-Defect Detailing)</option>
            <option value="Shopfloor Safety Guardian">Shopfloor Safety Guardian</option>
            <option value="Team Support & Mentorship">Team Support & Mentorship</option>
            <option value="On-Time Attendance Star">On-Time Attendance Star</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Why are you nominating them?</label>
          <textarea class="form-textarea" id="nominate-citation" rows="3" placeholder="Describe the specific work, teamwork, or milestone they achieved..."></textarea>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-outline btn-sm" onclick="closeModal('modal-nominate')">Cancel</button>
        <button class="btn btn-gold btn-sm" onclick="submitNomination()">Submit Nomination</button>
      </div>
    </div>
  </div>

  <!-- 7. Presentation Overview Modal -->
  <div class="modal-backdrop" id="modal-scene-overview">
    <div class="modal-box" style="max-width: 780px;">
      <div class="modal-header">
        <h3 class="modal-title">Presentation Overview</h3>
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
