# Complete JavaScript Operational Engine for PULSE Executive Showcase

JS_CONTENT = """
    /* ==========================================================================
       PULSE OPERATIONAL ENGINE & STATE MANAGEMENT
       ========================================================================== */
    const MASTER_DATA = __INITIAL_DATA_PLACEHOLDER__;
    let appState = JSON.parse(JSON.stringify(MASTER_DATA));

    let currentRole = 'PRESENTER';
    let currentScene = 1;
    const TOTAL_SCENES = 9;
    let activePunchFilter = 'ALL';
    let selected360EmpId = 'EMP-101';
    let parsedImportRows = [];

    // Scene Meta for Overview
    const SCENES_META = [
      { id: 1, title: 'Strategic Imperative', desc: 'Opening Hook: Every Shift Tells a Story' },
      { id: 2, title: 'Operational Diagnosis', desc: 'Cross-Border Realities in Sheet Metal' },
      { id: 3, title: 'PULSE Architecture', desc: 'The Operational Nervous System' },
      { id: 4, title: 'Biometric Precision', desc: 'Shift Inception, Breaks & Award Policy' },
      { id: 5, title: 'In-Flight Production', desc: 'Real-time Floor Velocity & Double Checks' },
      { id: 6, title: 'Unbroken Momentum', desc: 'Structured Shift Handovers & Cutoff Safety' },
      { id: 7, title: 'Employee 360° Profile', desc: '7-Point Skills Matrix & Zero-Blame RCA' },
      { id: 8, title: 'Executive Command Centre', desc: 'Managing Director Real-Time Control' },
      { id: 9, title: 'Implementation Asks', desc: 'Rakshith: 5 Strategic Directives' }
    ];

    /* ==========================================================================
       INITIALIZATION
       ========================================================================== */
    window.addEventListener('DOMContentLoaded', () => {
      initDualClocks();
      initStoryMode();
      populateDropdowns();
      renderAllViews();

      // Check URL hash for direct deep-linking
      if (window.location.hash) {
        const hash = window.location.hash.replace('#', '');
        if (hash.startsWith('view-')) {
          switchToProductMode();
          switchView(hash.replace('view-', ''));
        } else if (hash === 'product' || hash === 'prototype') {
          switchToProductMode();
        } else if (hash.startsWith('scene-')) {
          const scNum = parseInt(hash.replace('scene-', ''), 10);
          if (!isNaN(scNum)) goToScene(scNum);
        }
      }
    });

    /* ==========================================================================
       DUAL TIMEZONE ENGINE (MELBOURNE & INDIA)
       ========================================================================== */
    function initDualClocks() {
      updateClocks();
      setInterval(updateClocks, 1000);
    }

    function updateClocks() {
      const now = new Date();
      const melbourneTime = now.toLocaleTimeString('en-AU', {
        timeZone: 'Australia/Melbourne',
        hour12: false,
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      });
      const indiaTime = now.toLocaleTimeString('en-IN', {
        timeZone: 'Asia/Kolkata',
        hour12: false,
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      });

      const elMel = document.getElementById('clock-melbourne');
      const elInd = document.getElementById('clock-india');
      if (elMel) elMel.textContent = `${melbourneTime} AEDT`;
      if (elInd) elInd.textContent = `${indiaTime} IST`;
    }

    /* ==========================================================================
       PRESENTATION STORY MODE ENGINE
       ========================================================================= */
    function initStoryMode() {
      const dotsContainer = document.getElementById('story-pagination-dots');
      if (dotsContainer) {
        dotsContainer.innerHTML = '';
        for (let i = 1; i <= TOTAL_SCENES; i++) {
          const dot = document.createElement('div');
          dot.className = `story-dot ${i === 1 ? 'active' : ''}`;
          dot.onclick = () => goToScene(i);
          dotsContainer.appendChild(dot);
        }
      }

      // Populate Overview Modal
      const overviewGrid = document.getElementById('scene-overview-grid');
      if (overviewGrid) {
        overviewGrid.innerHTML = SCENES_META.map(s => `
          <div class="card" style="cursor: pointer; padding: 14px; border: 1px solid var(--slate-border);" onclick="goToScene(${s.id}); closeModal('modal-scene-overview');">
            <div style="font-family: var(--font-mono); font-size: 10px; color: var(--gold); margin-bottom: 4px;">SCENE 0${s.id}</div>
            <div style="font-weight: 600; color: var(--white); font-size: 13px; margin-bottom: 4px;">${s.title}</div>
            <div style="font-size: 11px; color: var(--steel); line-height: 1.4;">${s.desc}</div>
          </div>
        `).join('');
      }

      document.addEventListener('keydown', handlePresentationKeydown);
    }

    function handlePresentationKeydown(e) {
      const storyContainer = document.getElementById('story-mode-container');
      if (storyContainer.classList.contains('hidden')) return;

      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
        e.preventDefault();
        nextScene();
      } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        e.preventDefault();
        prevScene();
      } else if (e.key === 'Escape') {
        openSceneModal();
      }
    }

    function updateSceneDisplay() {
      // Hide all scenes
      for (let i = 1; i <= TOTAL_SCENES; i++) {
        const sc = document.getElementById(`scene-${i}`);
        if (sc) sc.classList.remove('active');
      }
      // Show active scene
      const activeSc = document.getElementById(`scene-${currentScene}`);
      if (activeSc) activeSc.classList.add('active');

      // Update counter & progress fill
      const counter = document.getElementById('scene-counter-display');
      if (counter) counter.textContent = `SCENE 0${currentScene} / 0${TOTAL_SCENES}`;

      const progressFill = document.getElementById('story-progress-fill');
      if (progressFill) {
        const pct = (currentScene / TOTAL_SCENES) * 100;
        progressFill.style.width = `${pct}%`;
      }

      // Update dots
      const dots = document.querySelectorAll('.story-dot');
      dots.forEach((d, idx) => {
        if (idx + 1 === currentScene) d.classList.add('active');
        else d.classList.remove('active');
      });

      // Update nav arrows
      const btnPrev = document.getElementById('btn-prev-scene');
      const btnNext = document.getElementById('btn-next-scene');
      if (btnPrev) btnPrev.disabled = (currentScene === 1);
      if (btnNext) btnNext.disabled = (currentScene === TOTAL_SCENES);
    }

    function nextScene() {
      if (currentScene < TOTAL_SCENES) {
        currentScene++;
        updateSceneDisplay();
      } else {
        switchToProductMode();
      }
    }

    function prevScene() {
      if (currentScene > 1) {
        currentScene--;
        updateSceneDisplay();
      }
    }

    function goToScene(sceneNum) {
      if (sceneNum >= 1 && sceneNum <= TOTAL_SCENES) {
        currentScene = sceneNum;
        updateSceneDisplay();
      }
    }

    function openSceneModal() {
      openModal('modal-scene-overview');
    }

    function toggleFullscreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        if (document.exitFullscreen) document.exitFullscreen();
      }
    }

    function switchToProductMode() {
      document.getElementById('story-mode-container').classList.add('hidden');
      document.getElementById('product-mode-container').classList.remove('hidden');
      window.scrollTo(0, 0);
      showToast('Switched to Interactive Prototype Mode. Full live operations active.');
    }

    function switchToStoryMode() {
      document.getElementById('product-mode-container').classList.add('hidden');
      document.getElementById('story-mode-container').classList.remove('hidden');
      window.scrollTo(0, 0);
    }

    /* ==========================================================================
       VIEW SWITCHER & SIDEBAR
       ========================================================================== */
    function switchView(viewName) {
      const menuItems = document.querySelectorAll('.app-sidebar .menu-item');
      menuItems.forEach(item => item.classList.remove('active'));

      // Highlight clicked sidebar item
      const clicked = event ? event.currentTarget : null;
      if (clicked && clicked.classList.contains('menu-item')) {
        clicked.classList.add('active');
      } else {
        // Fallback: match by onclick attribute
        menuItems.forEach(item => {
          if (item.getAttribute('onclick') && item.getAttribute('onclick').includes(viewName)) {
            item.classList.add('active');
          }
        });
      }

      const panels = document.querySelectorAll('.view-panel');
      panels.forEach(p => p.classList.remove('active'));

      const target = document.getElementById(`view-${viewName}`);
      if (target) {
        target.classList.add('active');
        document.querySelector('.app-main').scrollTop = 0;
      }
    }

    /* ==========================================================================
       ROLE PROFILES & PERMISSIONS
       ========================================================================== */
    function onRoleChange(role) {
      currentRole = role;
      const profiles = {
        'PRESENTER': { name: 'Rakshith', title: 'Lead Systems Architect & Operational Strategist', avatar: 'RK' },
        'MANAGEMENT': { name: 'David Harrison', title: 'Managing Director', avatar: 'DH' },
        'TEAM_LEADER': { name: 'Priya Nair', title: 'Shift A Team Leader', avatar: 'PN' },
        'EMPLOYEE': { name: 'Rohan Sharma', title: 'Senior Keying Specialist', avatar: 'RS' },
        'SUPER_ADMIN': { name: 'Alex Vance', title: 'Super Administrator', avatar: 'AV' }
      };

      const p = profiles[role] || profiles['PRESENTER'];
      document.getElementById('user-name-display').textContent = p.name;
      document.getElementById('user-role-display').textContent = p.title;
      document.getElementById('user-avatar-badge').textContent = p.avatar;

      // Re-render Employee 360 to reflect dynamic confidentiality lock
      renderEmployee360(selected360EmpId);
      showToast(`Active Perspective: ${p.name} (${p.title})`);
    }

    /* ==========================================================================
       DROPDOWNS & SELECTORS POPULATION
       ========================================================================== */
    function populateDropdowns() {
      const emps = appState.employees || [];

      // 1. Timeline employee select
      const timelineSelect = document.getElementById('timeline-emp-select');
      if (timelineSelect) {
        timelineSelect.innerHTML = emps.map(e => `
          <option value="${e.id}">${e.name} (${e.id}) — ${e.team}</option>
        `).join('');
      }

      // 2. Employee 360 select
      const emp360Select = document.getElementById('emp360-selector');
      if (emp360Select) {
        emp360Select.innerHTML = emps.map(e => `
          <option value="${e.id}">${e.name} (${e.id}) — ${e.designation}</option>
        `).join('');
      }

      // 3. Modal employee selectors
      ['manual-punch-emp', 'leave-emp-select', 'nominate-emp-select'].forEach(id => {
        const sel = document.getElementById(id);
        if (sel) {
          sel.innerHTML = emps.map(e => `<option value="${e.id}">${e.name} (${e.id}) — ${e.team}</option>`).join('');
        }
      });
    }

    /* ==========================================================================
       RENDER MASTER DISPATCHER
       ========================================================================== */
    function renderAllViews() {
      renderCommandCentre();
      renderBiometricView();
      renderEmployee360(selected360EmpId);
      renderDashboard();
      renderAttendanceTable();
      renderLeaveTables();
      renderCapacityView();
      renderProductionTable();
      renderQualityCases();
      renderHandoverView();
      renderShiftReportView();
      renderExceptionsView();
      renderSkillsMatrixView();
      renderReportBuilderView();
      renderImportView();
      renderAwards();
      renderRolesView();
      updateBadgeCounts();
    }

    function updateBadgeCounts() {
      const emps = appState.employees || [];
      const presentCount = emps.filter(e => e.status === 'Present').length;
      const elPresent = document.getElementById('badge-present-count');
      if (elPresent) elPresent.textContent = presentCount;

      const alerts = appState.alerts || [];
      const openAlerts = alerts.filter(a => a.status !== 'Resolved').length;
      const elAlerts = document.getElementById('badge-alerts-count');
      if (elAlerts) elAlerts.textContent = openAlerts;

      const quality = appState.qualityCases || [];
      const activeQ = quality.filter(q => q.status !== 'Resolved').length;
      const elQ = document.getElementById('badge-quality-active');
      if (elQ) elQ.textContent = `${activeQ} active`;
    }

    /* ==========================================================================
       1. LIVE SHIFT COMMAND CENTRE RENDERER
       ========================================================================== */
    function renderCommandCentre() {
      // Dynamic updates for Command Centre metrics are reflected via appState
    }

    /* ==========================================================================
       2. BIOMETRIC ATTENDANCE & BREAKS RENDERER
       ========================================================================== */
    function renderBiometricView() {
      renderPunchTable();
      renderBiometricTimeline(selected360EmpId);
    }

    function filterPunchFeed(filterType) {
      activePunchFilter = filterType;
      renderPunchTable();
    }

    function renderPunchTable() {
      const tbody = document.getElementById('biometric-punches-tbody');
      if (!tbody) return;

      let punches = appState.biometricPunches || [];

      if (activePunchFilter === 'IN') {
        punches = punches.filter(p => p.type === 'Office IN');
      } else if (activePunchFilter === 'OUT') {
        punches = punches.filter(p => p.type === 'Office OUT');
      } else if (activePunchFilter === 'BREAK') {
        punches = punches.filter(p => p.type.includes('Break'));
      } else if (activePunchFilter === 'EXCEPTION') {
        punches = punches.filter(p => p.type.includes('Manual') || p.type.includes('Adjustment'));
      }

      tbody.innerHTML = punches.map(p => {
        let badgeClass = 'verified';
        if (p.type === 'Office IN') badgeClass = 'in';
        else if (p.type === 'Office OUT') badgeClass = 'out';
        else if (p.type.includes('Break')) badgeClass = 'break';
        else badgeClass = 'exception';

        return `
          <tr>
            <td><strong style="color: var(--steel); font-family: var(--font-mono);">${p.id}</strong></td>
            <td><span style="font-family: var(--font-mono); color: var(--gold);">${p.empId}</span></td>
            <td><strong>${p.empName}</strong></td>
            <td><span style="font-family: var(--font-mono); color: var(--white);">${p.timestamp}</span></td>
            <td><span class="status-badge ${badgeClass}">${p.type}</span></td>
            <td>${p.device}</td>
            <td><span style="color: var(--steel); font-size: 12px;">${p.method}</span></td>
            <td><span class="status-badge verified">${p.status}</span></td>
          </tr>
        `;
      }).join('');
    }

    function renderBiometricTimeline(empId) {
      const summaryContainer = document.getElementById('timeline-summary-container');
      const visualContainer = document.getElementById('timeline-visual-container');
      if (!visualContainer) return;

      const timelineData = (appState.employeeAttendanceTimelines && appState.employeeAttendanceTimelines[empId]) || {
        empId: empId,
        firstEntry: '05:58 AM',
        lastExit: 'In Progress (Active Shift)',
        expectedStart: '06:00 AM',
        expectedEnd: '14:30 PM',
        timeOnPremises: '7h 12m',
        recordedBreakDuration: '45m',
        netAttendedDuration: '6h 27m',
        regularizationStatus: 'Verified Compliant',
        events: [
          { time: '05:58', type: 'Office IN', label: 'Office Entry Turnstile', status: 'Verified' },
          { time: '09:15', type: 'Break START', label: 'Morning Tea Break', status: 'Verified' },
          { time: '09:30', type: 'Break END', label: 'Tea Return (15m elapsed)', status: 'Verified' },
          { time: '12:10', type: 'Break START', label: 'Lunch Break', status: 'Verified' },
          { time: '12:40', type: 'Break END', label: 'Lunch Return (30m elapsed)', status: 'Verified' }
        ]
      };

      summaryContainer.innerHTML = `
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; background: var(--midnight); padding: 16px; border: 1px solid var(--slate-border); border-radius: 6px;">
          <div>
            <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">First Entry Punch</div>
            <div style="font-size: 16px; font-weight: 600; color: #79D2B7; font-family: var(--font-mono);">${timelineData.firstEntry}</div>
            <div style="font-size: 10px; color: var(--steel-dim);">Assigned: ${timelineData.expectedStart}</div>
          </div>
          <div>
            <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Time on Premises</div>
            <div style="font-size: 16px; font-weight: 600; color: var(--white); font-family: var(--font-mono);">${timelineData.timeOnPremises}</div>
            <div style="font-size: 10px; color: var(--steel-dim);">Gross Gate Time</div>
          </div>
          <div>
            <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Recorded Breaks</div>
            <div style="font-size: 16px; font-weight: 600; color: var(--amber); font-family: var(--font-mono);">${timelineData.recordedBreakDuration}</div>
            <div style="font-size: 10px; color: var(--steel-dim);">Morning Tea + Lunch</div>
          </div>
          <div>
            <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Net Attended Duration</div>
            <div style="font-size: 16px; font-weight: 600; color: var(--gold); font-family: var(--font-mono);">${timelineData.netAttendedDuration}</div>
            <div style="font-size: 10px; color: #79D2B7;">Status: ${timelineData.regularizationStatus}</div>
          </div>
        </div>
      `;

      visualContainer.innerHTML = `
        <div style="display: flex; flex-direction: column; gap: 12px; position: relative; padding-left: 30px;">
          <div style="position: absolute; left: 11px; top: 12px; bottom: 12px; width: 2px; background: rgba(147, 163, 174, 0.25);"></div>
          ${timelineData.events.map(ev => {
            let dotColor = 'var(--emerald)';
            if (ev.type.includes('OUT')) dotColor = 'var(--crimson)';
            else if (ev.type.includes('Break')) dotColor = 'var(--amber)';

            return `
              <div style="display: flex; align-items: center; justify-content: space-between; padding: 10px 14px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px; position: relative;">
                <div style="position: absolute; left: -25px; width: 12px; height: 12px; border-radius: 50%; background: ${dotColor}; border: 2px solid var(--midnight);"></div>
                <div style="display: flex; align-items: center; gap: 14px;">
                  <strong style="font-family: var(--font-mono); color: var(--white); font-size: 13px;">${ev.time} IST</strong>
                  <span class="status-badge ${ev.type.includes('IN') ? 'in' : ev.type.includes('OUT') ? 'out' : 'break'}">${ev.type}</span>
                  <span style="color: var(--porcelain); font-size: 13px;">${ev.label}</span>
                </div>
                <span class="status-badge verified">${ev.status}</span>
              </div>
            `;
          }).join('')}
        </div>
      `;
    }

    function submitManualBiometricPunch() {
      const empId = document.getElementById('manual-punch-emp').value;
      const type = document.getElementById('manual-punch-type').value;
      const time = document.getElementById('manual-punch-time').value;
      const reason = document.getElementById('manual-punch-reason').value;

      const emp = appState.employees.find(e => e.id === empId);
      const newPunch = {
        id: `PUN-${Math.floor(1000 + Math.random() * 9000)}`,
        empId: empId,
        empName: emp ? emp.name : 'Unknown',
        timestamp: `Today ${time} IST`,
        type: type,
        device: 'Manual Regularization Interface',
        method: 'Manager Approved Override',
        status: 'Regularized'
      };

      appState.biometricPunches.unshift(newPunch);
      closeModal('modal-biometric-punch');
      renderPunchTable();
      showToast(`Biometric punch regularized for ${emp ? emp.name : empId} (${type} at ${time} IST).`);
    }

    /* ==========================================================================
       3. EMPLOYEE 360-DEGREE DASHBOARD RENDERER
       ========================================================================== */
    function renderEmployee360(empId) {
      selected360EmpId = empId;
      const container = document.getElementById('emp360-content-container');
      if (!container) return;

      const emp = appState.employees.find(e => e.id === empId) || appState.employees[0];
      const isRestrictedRole = (currentRole === 'EMPLOYEE');

      const skillBadges = Array.isArray(emp.skills) 
        ? emp.skills 
        : Object.entries(emp.skills || {}).map(([k, v]) => `${k.replace(/([A-Z])/g, ' $1').toUpperCase()}: ${v}`);

      container.innerHTML = `
        <!-- Section A: Overview Header -->
        <div class="card" style="margin-bottom: 24px; background: rgba(24, 38, 49, 0.7); border: 1px solid var(--gold-border);">
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="display: flex; gap: 18px; align-items: center;">
              <div style="width: 58px; height: 58px; border-radius: 50%; background: var(--gold-dim); border: 2px solid var(--gold); display: flex; align-items: center; justify-content: center; font-family: var(--font-mono); font-size: 20px; color: var(--gold); font-weight: bold;">
                ${emp.name.split(' ').map(n => n[0]).join('')}
              </div>
              <div>
                <div style="display: flex; align-items: center; gap: 10px;">
                  <h2 style="font-size: 22px; color: var(--white);">${emp.name}</h2>
                  <span class="status-badge verified">${emp.status}</span>
                  <span style="font-family: var(--font-mono); font-size: 12px; color: var(--gold);">${emp.id}</span>
                </div>
                <div style="font-size: 13px; color: var(--steel); margin-top: 4px;">
                  ${emp.designation} • ${emp.team} • Reports to <strong>${emp.manager}</strong>
                </div>
              </div>
            </div>
            <div style="text-align: right; font-family: var(--font-mono); font-size: 12px;">
              <div style="color: var(--steel-dim);">Assigned Shift</div>
              <div style="color: var(--gold); font-weight: 600;">${emp.shift}</div>
            </div>
          </div>
          <!-- Skills Badges -->
          <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 18px; padding-top: 14px; border-top: 1px solid var(--slate-border);">
            ${skillBadges.map(s => `
              <span style="padding: 4px 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 12px; font-size: 11px; color: var(--porcelain); font-family: var(--font-mono);">
                ${s}
              </span>
            `).join('')}
          </div>
        </div>

        <!-- 3-Column Diagnostic Grid -->
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 24px;">
          <!-- Section B: Attendance Intelligence -->
          <div class="card">
            <div class="card-title">
              <span>Attendance & Reliability</span>
              <span class="status-badge verified">98.2% Score</span>
            </div>
            <div style="display: flex; flex-direction: column; gap: 10px; font-size: 13px;">
              <div style="display: flex; justify-content: space-between; padding-bottom: 6px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                <span style="color: var(--steel);">Present Days</span>
                <strong style="color: var(--white);">22 / 23 Days</strong>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 6px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                <span style="color: var(--steel);">Approved Leave</span>
                <strong style="color: var(--porcelain);">1 Day (Annual)</strong>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 6px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                <span style="color: var(--steel);">Late Arrivals</span>
                <strong style="color: var(--amber);">${emp.lateMinutes > 0 ? '1 (18m transit)' : '0 (On-Time)'}</strong>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 6px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                <span style="color: var(--steel);">Net Attended Hours</span>
                <strong style="color: var(--gold); font-family: var(--font-mono);">${emp.hours}h (Month)</strong>
              </div>
            </div>
          </div>

          <!-- Section C: Daily Production Output -->
          <div class="card">
            <div class="card-title">
              <span>Production Velocity</span>
              <span class="status-badge in">104% Target</span>
            </div>
            <div style="display: flex; flex-direction: column; gap: 10px; font-size: 13px;">
              <div style="display: flex; justify-content: space-between; padding-bottom: 6px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                <span style="color: var(--steel);">Average Orders / Shift</span>
                <strong style="color: var(--white);">${emp.dailyTarget ? emp.dailyTarget.orders : 14} Orders</strong>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 6px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                <span style="color: var(--steel);">Flashings Detailed</span>
                <strong style="color: var(--white);">${emp.dailyTarget ? emp.dailyTarget.flashings : 180} Metres</strong>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 6px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                <span style="color: var(--steel);">Bits & Accessories</span>
                <strong style="color: var(--white);">${emp.dailyTarget ? emp.dailyTarget.bits : 450} Units</strong>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 6px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                <span style="color: var(--steel);">Double-Check Rigor</span>
                <strong style="color: #79D2B7;">99.1% Compliance</strong>
              </div>
            </div>
          </div>

          <!-- Section D: Quality & Zero-Blame RCA -->
          <div class="card">
            <div class="card-title">
              <span>Quality Assurance & RCA</span>
              <span class="status-badge verified">Zero-Defect Merit</span>
            </div>
            <div style="display: flex; flex-direction: column; gap: 10px; font-size: 13px;">
              <div style="display: flex; justify-content: space-between; padding-bottom: 6px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                <span style="color: var(--steel);">Resupply Involvement</span>
                <strong style="color: var(--porcelain);">1 Case (Learning Logged)</strong>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 6px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                <span style="color: var(--steel);">First-Pass Accuracy</span>
                <strong style="color: var(--gold); font-family: var(--font-mono);">99.2%</strong>
              </div>
              <div style="display: flex; justify-content: space-between; padding-bottom: 6px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                <span style="color: var(--steel);">Resolution Turnaround</span>
                <strong style="color: #79D2B7;">45m (Drawing Rev B)</strong>
              </div>
              <div style="font-size: 11px; color: var(--steel-dim); line-height: 1.4; padding-top: 4px;">
                *Zero-blame ethos: Resupply analysis focuses on tooling clearance & drawing markups, not individual fault.
              </div>
            </div>
          </div>
        </div>

        <!-- Section E: Performance Insight Narrative -->
        <div class="card" style="margin-bottom: 24px; border-left: 4px solid var(--gold);">
          <div style="font-family: var(--font-mono); font-size: 11px; color: var(--gold); margin-bottom: 6px;">AI PERFORMANCE INSIGHT ENGINE</div>
          <p style="font-size: 14px; color: var(--porcelain); line-height: 1.6; margin-bottom: 8px;">
            <strong>${emp.name}</strong> demonstrates exceptional proficiency in complex radius flashings and architectural capping profiles, maintaining a 99.2% first-pass accuracy rating over the last 90 operational days. Production throughput surged by 12% following recent CAD cross-training on 3D folding geometries.
          </p>
          <div style="font-size: 12px; color: var(--steel-dim); font-family: var(--font-mono);">
            Recommended Milestone: Ready for Senior Operator Certification in NC Press Brake Folding.
          </div>
        </div>

        <!-- Section G: Confidential Development & Mentorship (Role-Restricted) -->
        <div class="card" style="position: relative; overflow: hidden;">
          <div class="card-title">
            <span>Confidential Leadership Mentorship & Development Reviews</span>
            <span class="status-badge ${isRestrictedRole ? 'alert' : 'verified'}">
              ${isRestrictedRole ? 'Privacy Protected (Locked)' : 'Authorized Access'}
            </span>
          </div>

          ${isRestrictedRole ? `
            <div style="padding: 30px; text-align: center; background: rgba(16, 25, 35, 0.9); border-radius: 6px; border: 1px dashed var(--slate-border);">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="2" style="margin-bottom: 10px;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
              <div style="font-size: 14px; font-weight: 600; color: var(--white); margin-bottom: 6px;">
                Restricted Confidential Section
              </div>
              <div style="font-size: 12px; color: var(--steel); max-width: 480px; margin: 0 auto;">
                Individual supervisory mentorship notes, private development milestones, and salary reviews are restricted to Team Leaders, Management, and Systems Architects.
              </div>
            </div>
          ` : `
            <div style="display: flex; flex-direction: column; gap: 14px; font-size: 13px;">
              <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                  <strong style="color: var(--white);">Quarterly Operational Review (Q1 2027)</strong>
                  <span style="color: var(--steel-dim); font-family: var(--font-mono);">Reviewer: Priya Nair (TL)</span>
                </div>
                <div style="color: var(--steel); line-height: 1.5;">
                  Rohan continues to be a cornerstone of Team Alpha. Showed great patience coaching junior keyers on tapering corner flashings. Recommended for supervisory relief training during Shift A peak cycles.
                </div>
              </div>
            </div>
          `}
        </div>
      `;
    }

    /* ==========================================================================
       4. SHIFT HANDOVER MODULE RENDERER
       ========================================================================== */
    function renderHandoverView() {
      const container = document.getElementById('handover-content-container');
      if (!container) return;

      const handovers = appState.handovers || [];

      container.innerHTML = `
        <div style="display: flex; flex-direction: column; gap: 20px;">
          ${handovers.map(h => `
            <div class="card" style="border: 1px solid ${h.acknowledged ? 'var(--slate-border)' : 'var(--gold-border)'};">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid var(--slate-border);">
                <div style="display: flex; align-items: center; gap: 12px;">
                  <span class="status-badge ${h.acknowledged ? 'verified' : 'warning'}">
                    ${h.acknowledged ? 'Acknowledged & Closed' : 'Pending Incoming Acknowledgment'}
                  </span>
                  <strong style="color: var(--white); font-size: 16px;">${h.outgoingShift} → ${h.incomingShift} Transfer Dossier</strong>
                </div>
                <div style="font-family: var(--font-mono); font-size: 12px; color: var(--gold);">
                  Logged: ${h.timestamp}
                </div>
              </div>

              <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin-bottom: 16px; font-size: 13px;">
                <div>
                  <div style="color: var(--steel); font-size: 11px; text-transform: uppercase;">Outgoing TL</div>
                  <strong style="color: var(--white);">${h.outgoingTL}</strong>
                </div>
                <div>
                  <div style="color: var(--steel); font-size: 11px; text-transform: uppercase;">Incoming TL</div>
                  <strong style="color: var(--white);">${h.incomingTL}</strong>
                </div>
                <div>
                  <div style="color: var(--steel); font-size: 11px; text-transform: uppercase;">Status</div>
                  <strong style="color: ${h.acknowledged ? '#79D2B7' : 'var(--gold)'};">
                    ${h.acknowledged ? `Acknowledged at ${h.acknowledgedAt}` : 'Awaiting Sign-Off'}
                  </strong>
                </div>
              </div>

              <div style="display: flex; flex-direction: column; gap: 10px; font-size: 13px; margin-bottom: 18px;">
                <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
                  <strong style="color: var(--gold);">Urgent Melbourne Orders:</strong> ${h.urgentJobs}
                </div>
                <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
                  <strong style="color: var(--porcelain);">Machinery & Tooling:</strong> ${h.machineryNotes}
                </div>
                <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
                  <strong style="color: var(--steel);">Staffing Observations:</strong> ${h.staffingNotes}
                </div>
              </div>

              ${!h.acknowledged ? `
                <div style="display: flex; justify-content: flex-end;">
                  <button class="btn btn-gold btn-sm" onclick="acknowledgeHandover('${h.id}')">
                    Acknowledge & Accept Handover
                  </button>
                </div>
              ` : ''}
            </div>
          `).join('')}
        </div>
      `;
    }

    function acknowledgeHandover(handoverId) {
      const h = appState.handovers.find(item => item.id === handoverId);
      if (h) {
        h.acknowledged = true;
        const now = new Date();
        h.acknowledgedAt = `${now.getHours()}:${String(now.getMinutes()).padStart(2, '0')} IST`;
        renderHandoverView();
        showToast(`Shift Handover #${handoverId} acknowledged by incoming Team Leader.`);
      }
    }

    function submitNewHandover() {
      const urgentJobs = document.getElementById('handover-urgent-jobs').value;
      const machinery = document.getElementById('handover-machinery-notes').value;
      const staffing = document.getElementById('handover-staffing-notes').value;

      const newH = {
        id: `HND-${Math.floor(100 + Math.random() * 900)}`,
        outgoingShift: 'Shift A (Day)',
        incomingShift: 'Shift B (Afternoon)',
        outgoingTL: 'Priya Nair',
        incomingTL: 'Rajesh Kumar',
        timestamp: 'Just Now',
        urgentJobs: urgentJobs || 'Standard batch orders in queue.',
        machineryNotes: machinery || 'All machines operating within normal parameters.',
        staffingNotes: staffing || 'Full complement clocked in.',
        acknowledged: false,
        acknowledgedAt: ''
      };

      appState.handovers.unshift(newH);
      closeModal('modal-create-handover');
      renderHandoverView();
      showToast('New digital handover dossier published.');
    }

    /* ==========================================================================
       5. END-OF-SHIFT REPORT RENDERER
       ========================================================================== */
    function renderShiftReportView() {
      const container = document.getElementById('shift-report-content-container');
      if (!container) return;

      container.innerHTML = `
        <div class="card" style="padding: 36px; background: var(--slate-card); border: 1px solid var(--slate-border-light);">
          <!-- Header -->
          <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 24px; border-bottom: 2px solid var(--gold); margin-bottom: 24px;">
            <div>
              <div style="font-family: var(--font-serif); font-size: 24px; font-weight: 600; color: var(--white); margin-bottom: 4px;">
                DESIGN SHEETMETAL • EXECUTIVE SHIFT RECONCILIATION DOSSIER
              </div>
              <div style="font-size: 13px; color: var(--steel);">
                Operational Facility: Bengaluru det-01 • Shift Cycle: Shift A (06:00 — 14:30 IST)
              </div>
            </div>
            <div style="text-align: right; font-family: var(--font-mono); font-size: 12px; color: var(--gold);">
              <div>DATE: 2027-03-24</div>
              <div>CLASSIFICATION: EXECUTIVE OPERATIONS</div>
            </div>
          </div>

          <!-- Summary Metric Ribbon -->
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin-bottom: 28px;">
            <div style="padding: 16px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Scheduled Operators</div>
              <div style="font-size: 24px; font-weight: 600; color: var(--white); font-family: var(--font-serif);">40</div>
              <div style="font-size: 11px; color: #79D2B7;">34 Clocked In • 3 Leave • 1 Absent</div>
            </div>
            <div style="padding: 16px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Total Output Volume</div>
              <div style="font-size: 24px; font-weight: 600; color: var(--gold); font-family: var(--font-serif);">142 Orders</div>
              <div style="font-size: 11px; color: var(--steel-dim);">1,840m Flashings • 5,120 Bits</div>
            </div>
            <div style="padding: 16px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Double-Check Completion</div>
              <div style="font-size: 24px; font-weight: 600; color: #79D2B7; font-family: var(--font-serif);">97.2%</div>
              <div style="font-size: 11px; color: var(--steel-dim);">138 of 142 Formally Verified</div>
            </div>
            <div style="padding: 16px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Quality Variance Count</div>
              <div style="font-size: 24px; font-weight: 600; color: #FFA5A2; font-family: var(--font-serif);">1 Case</div>
              <div style="font-size: 11px; color: var(--steel-dim);">Tooling Angle (Rev B Corrected)</div>
            </div>
          </div>

          <!-- Section: Production Breakdown Table -->
          <div style="margin-bottom: 28px;">
            <h4 style="font-size: 15px; color: var(--white); margin-bottom: 12px;">1. Operational Output by Detailing Cell</h4>
            <div class="data-table-container">
              <table class="data-table">
                <thead>
                  <tr>
                    <th>Cell / Team</th>
                    <th>Detailing Focus</th>
                    <th>Staff Present</th>
                    <th>Orders Completed</th>
                    <th>Meters Detailed</th>
                    <th>Double-Checks</th>
                    <th>First-Pass %</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Team Alpha</strong></td>
                    <td>Parapet Flashings & Roof Trims</td>
                    <td>10 / 10</td>
                    <td>42</td>
                    <td>680m</td>
                    <td>42 (100%)</td>
                    <td><span style="color: #79D2B7;">99.1%</span></td>
                  </tr>
                  <tr>
                    <td><strong>Team Beta</strong></td>
                    <td>Architectural Cladding Panels</td>
                    <td>9 / 10</td>
                    <td>34</td>
                    <td>410m</td>
                    <td>33 (97%)</td>
                    <td><span style="color: #79D2B7;">98.4%</span></td>
                  </tr>
                  <tr>
                    <td><strong>Team Gamma</strong></td>
                    <td>Rainwater Goods & Downpipes</td>
                    <td>8 / 10</td>
                    <td>38</td>
                    <td>450m</td>
                    <td>36 (95%)</td>
                    <td><span style="color: #79D2B7;">98.0%</span></td>
                  </tr>
                  <tr>
                    <td><strong>Team Delta</strong></td>
                    <td>Special Structural Assemblies</td>
                    <td>7 / 10</td>
                    <td>28</td>
                    <td>300m</td>
                    <td>27 (96%)</td>
                    <td><span style="color: #79D2B7;">98.8%</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Executive Sign-Off Signatures -->
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; padding-top: 24px; border-top: 1px solid var(--slate-border); font-size: 12px;">
            <div>
              <div style="color: var(--steel-dim); margin-bottom: 4px;">Outgoing Shift Supervisor:</div>
              <div style="color: var(--white); font-weight: 600; font-family: var(--font-serif); font-size: 14px;">Priya Nair</div>
              <div style="color: var(--gold); font-family: var(--font-mono); font-size: 11px;">Digitally Signed 14:28 IST</div>
            </div>
            <div>
              <div style="color: var(--steel-dim); margin-bottom: 4px;">Incoming Shift Supervisor:</div>
              <div style="color: var(--white); font-weight: 600; font-family: var(--font-serif); font-size: 14px;">Rajesh Kumar</div>
              <div style="color: #79D2B7; font-family: var(--font-mono); font-size: 11px;">Digitally Acknowledged 14:32 IST</div>
            </div>
            <div>
              <div style="color: var(--steel-dim); margin-bottom: 4px;">Operations Director Sign-Off:</div>
              <div style="color: var(--white); font-weight: 600; font-family: var(--font-serif); font-size: 14px;">David Harrison</div>
              <div style="color: var(--steel); font-family: var(--font-mono); font-size: 11px;">Status: Validated for Melbourne Release</div>
            </div>
          </div>
        </div>
      `;
    }

    function printShiftReport() {
      window.print();
    }

    function exportShiftReportCSV() {
      const csvContent = "data:text/csv;charset=utf-8," +
        "Shift,Date,Team,Scheduled,Present,OrdersKeyed,FlashingsMeters,Bits,DoubleChecks,FirstPassAccuracy\\n" +
        "Shift A,2027-03-24,Team Alpha,10,10,42,680,1850,42,99.1%\\n" +
        "Shift A,2027-03-24,Team Beta,10,9,34,410,1120,33,98.4%\\n" +
        "Shift A,2027-03-24,Team Gamma,10,8,38,450,1250,36,98.0%\\n" +
        "Shift A,2027-03-24,Team Delta,10,7,28,300,900,27,98.8%\\n";

      const encodedUri = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", "PULSE_ShiftA_Executive_Report.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      showToast("Shift Dossier CSV exported successfully.");
    }

    /* ==========================================================================
       6. MANAGEMENT EXCEPTIONS & ALERTS INBOX RENDERER
       ========================================================================== */
    function renderExceptionsView() {
      const container = document.getElementById('exceptions-content-container');
      if (!container) return;

      const alerts = appState.alerts || [];

      container.innerHTML = `
        <div style="display: flex; flex-direction: column; gap: 14px;">
          ${alerts.map(a => {
            let priorityBadge = 'in';
            if (a.priority === 'High') priorityBadge = 'alert';
            else if (a.priority === 'Medium') priorityBadge = 'warning';

            return `
              <div class="card" style="border-left: 4px solid ${a.status === 'Resolved' ? 'var(--emerald)' : a.priority === 'High' ? 'var(--crimson)' : 'var(--amber)'};">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                  <div style="display: flex; align-items: center; gap: 10px;">
                    <span class="status-badge ${priorityBadge}">${a.priority} Priority</span>
                    <strong style="font-size: 14px; color: var(--white);">${a.type}: ${a.empName} (${a.empId})</strong>
                    <span style="font-size: 11px; color: var(--steel-dim); font-family: var(--font-mono);">${a.id}</span>
                  </div>
                  <span class="status-badge ${a.status === 'Resolved' ? 'verified' : a.status === 'In Progress' ? 'warning' : 'out'}">
                    ${a.status}
                  </span>
                </div>
                <div style="font-size: 13px; color: var(--porcelain); margin-bottom: 8px; line-height: 1.5;">
                  ${a.message}
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; font-size: 11px; color: var(--steel); font-family: var(--font-mono);">
                  <div>Team: ${a.team} • Assigned To: <strong>${a.assignedTo}</strong></div>
                  <div>Created: ${a.created}</div>
                </div>
                ${a.status !== 'Resolved' ? `
                  <div style="display: flex; justify-content: flex-end; gap: 10px; margin-top: 12px; padding-top: 10px; border-top: 1px solid var(--slate-border);">
                    <button class="btn btn-outline btn-sm" onclick="acknowledgeAlert('${a.id}')">Acknowledge</button>
                    <button class="btn btn-gold btn-sm" onclick="openResolveAlertModal('${a.id}')">Resolve with Notes</button>
                  </div>
                ` : `
                  <div style="margin-top: 10px; padding: 8px 12px; background: rgba(70, 139, 119, 0.15); border: 1px solid var(--emerald); border-radius: 4px; font-size: 12px; color: #79D2B7;">
                    <strong>Resolution Note:</strong> ${a.resolution || 'Resolved by operational lead.'}
                  </div>
                `}
              </div>
            `;
          }).join('')}
        </div>
      `;
    }

    function acknowledgeAlert(alertId) {
      const a = appState.alerts.find(item => item.id === alertId);
      if (a) {
        a.status = 'Acknowledged';
        renderExceptionsView();
        updateBadgeCounts();
        showToast(`Alert #${alertId} acknowledged.`);
      }
    }

    function openResolveAlertModal(alertId) {
      const a = appState.alerts.find(item => item.id === alertId);
      if (!a) return;
      document.getElementById('resolve-alert-id').value = a.id;
      document.getElementById('resolve-alert-desc').textContent = `${a.type}: ${a.message}`;
      openModal('modal-resolve-alert');
    }

    function submitResolveAlert() {
      const alertId = document.getElementById('resolve-alert-id').value;
      const notes = document.getElementById('resolve-alert-notes').value;
      const a = appState.alerts.find(item => item.id === alertId);
      if (a) {
        a.status = 'Resolved';
        a.resolution = notes || 'Confirmed resolved by operational supervisor.';
        closeModal('modal-resolve-alert');
        renderExceptionsView();
        updateBadgeCounts();
        showToast(`Exception #${alertId} marked as Resolved.`);
      }
    }

    /* ==========================================================================
       7. WORKFORCE CAPACITY & COVERAGE PLANNER RENDERER
       ========================================================================== */
    function renderCapacityView() {
      const container = document.getElementById('capacity-content-container');
      if (!container) return;

      container.innerHTML = `
        <div class="card" style="margin-bottom: 24px;">
          <div class="card-title">
            <span>14-Day Forward Workforce Capacity & Threshold Heatmap</span>
            <span class="status-badge warning">Min Staffing Threshold: 8 Operators / Team</span>
          </div>
          <p style="font-size: 13px; color: var(--steel); margin-bottom: 18px;">
            Visual staffing risk model. Highlights under-staffed dates and recommends certified backup operators across teams.
          </p>

          <div style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 10px; margin-bottom: 24px;">
            ${['Mon 22', 'Tue 23', 'Wed 24 (Today)', 'Thu 25', 'Fri 26 (Risk)', 'Sat 27', 'Sun 28'].map((day, idx) => {
              const isToday = idx === 2;
              const isRisk = idx === 4;
              return `
                <div style="padding: 12px; background: ${isToday ? 'rgba(198, 166, 117, 0.12)' : isRisk ? 'rgba(217, 83, 79, 0.12)' : 'var(--midnight)'}; border: 1px solid ${isToday ? 'var(--gold)' : isRisk ? 'var(--crimson)' : 'var(--slate-border)'}; border-radius: 6px; text-align: center;">
                  <div style="font-family: var(--font-mono); font-size: 11px; color: ${isToday ? 'var(--gold)' : isRisk ? '#FFA5A2' : 'var(--steel)'}; margin-bottom: 4px;">
                    ${day}
                  </div>
                  <div style="font-size: 18px; font-weight: 600; color: ${isRisk ? '#FFA5A2' : 'var(--white)'}; font-family: var(--font-serif);">
                    ${isRisk ? '31 / 40' : isToday ? '34 / 40' : '36 / 40'}
                  </div>
                  <div style="font-size: 10px; color: ${isRisk ? '#FFA5A2' : '#79D2B7'};">
                    ${isRisk ? 'Threshold Breach (Gamma)' : 'Optimal Capacity'}
                  </div>
                </div>
              `;
            }).join('')}
          </div>

          <!-- Cross-Training Backup Suggestion Card -->
          <div style="padding: 16px; background: rgba(198, 166, 117, 0.08); border: 1px solid var(--gold-border); border-radius: 6px;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
              <span class="pulse-dot"></span>
              <strong style="color: var(--white); font-size: 13px;">Automated Skill-Based Backup Recommender</strong>
            </div>
            <div style="font-size: 12px; color: var(--porcelain); line-height: 1.6;">
              On <strong>Friday March 26</strong>, Team Gamma faces a staffing dip due to medical leave. PULSE recommends temporarily reassigning <strong>Vikram Singh (EMP-107)</strong> from Team Alpha (certified in Downpipe Seaming & Press Brake Folding) to maintain minimum throughput.
            </div>
          </div>
        </div>
      `;
    }

    /* ==========================================================================
       8. SKILLS MATRIX RENDERER
       ========================================================================== */
    function renderSkillsMatrixView() {
      const container = document.getElementById('skills-content-container');
      if (!container) return;

      const skills = appState.skillsDefinitions || [];
      const emps = appState.employees.slice(0, 15); // showcase sample

      container.innerHTML = `
        <div class="card" style="margin-bottom: 24px;">
          <div class="card-title">
            <span>7-Point Sheet-Metal Operational Skills Matrix</span>
            <span style="font-size: 12px; color: var(--steel); font-family: var(--font-mono);">
              Legend: L1 Trainee • L2 Competent • L3 Senior Specialist • L4 Master Trainer
            </span>
          </div>
          <div class="data-table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Employee</th>
                  <th>Team</th>
                  ${skills.map(s => `<th>${s.name}</th>`).join('')}
                </tr>
              </thead>
              <tbody>
                ${emps.map(e => `
                  <tr>
                    <td><strong>${e.name}</strong><br/><span style="font-size: 11px; color: var(--gold); font-family: var(--font-mono);">${e.id}</span></td>
                    <td>${e.team}</td>
                    ${skills.map((s, idx) => {
                      const level = ((e.name.length + idx) % 4) + 1;
                      let color = 'var(--steel-dim)';
                      if (level === 2) color = 'var(--steel)';
                      else if (level === 3) color = 'var(--gold)';
                      else if (level === 4) color = '#79D2B7';
                      return `<td><span style="font-family: var(--font-mono); font-weight: 600; color: ${color};">L${level}</span></td>`;
                    }).join('')}
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>
      `;
    }

    /* ==========================================================================
       9. CUSTOM REPORT BUILDER RENDERER
       ========================================================================== */
    function renderReportBuilderView() {
      const container = document.getElementById('report-builder-content-container');
      if (!container) return;

      container.innerHTML = `
        <div class="card" style="margin-bottom: 24px;">
          <div class="card-title">
            <span>Operational Query & Dossier Parameters</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 18px;">
            <div class="form-group">
              <label class="form-label">Team Allocation</label>
              <select class="form-select" id="rep-filter-team">
                <option value="ALL">All Teams (Alpha, Beta, Gamma, Delta)</option>
                <option value="Team Alpha">Team Alpha (Flashings & Trims)</option>
                <option value="Team Beta">Team Beta (Cladding Panels)</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label">Shift Window</label>
              <select class="form-select" id="rep-filter-shift">
                <option value="ALL">All Shifts (A Day, B Afternoon, C Night)</option>
                <option value="Shift A">Shift A (Day: 06:00 — 14:30)</option>
                <option value="Shift B">Shift B (Afternoon: 14:00 — 22:30)</option>
                <option value="Shift C">Shift C (Night: 22:00 — 06:30)</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label">Metric Focus</label>
              <select class="form-select" id="rep-filter-metric">
                <option value="ALL">Comprehensive Operational Dossier</option>
                <option value="ATTENDANCE">Biometric Attendance Regularity</option>
                <option value="OUTPUT">Daily Production & Keying Volume</option>
                <option value="QUALITY">First-Pass Accuracy & Resupply Rates</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label">Date Range</label>
              <select class="form-select" id="rep-filter-date">
                <option value="TODAY">Current Shift Cycle (Today)</option>
                <option value="WEEK">Last 7 Operating Days</option>
                <option value="MONTH">Current Month to Date</option>
              </select>
            </div>
          </div>
          <div style="display: flex; justify-content: flex-end; gap: 10px;">
            <button class="btn btn-outline btn-sm" onclick="exportCustomReportCSV()">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              Export CSV Dossier
            </button>
            <button class="btn btn-gold btn-sm" onclick="runCustomReport()">
              Run Query & Generate Report
            </button>
          </div>
        </div>

        <div class="card" id="custom-report-output">
          <div class="card-title">
            <span>Query Results: Active India Workforce Operations</span>
            <span class="status-badge verified">40 Records Matched</span>
          </div>
          <div class="data-table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Employee ID</th>
                  <th>Name</th>
                  <th>Team</th>
                  <th>Shift</th>
                  <th>Attended Hours</th>
                  <th>Orders Keyed</th>
                  <th>Quality Accuracy</th>
                </tr>
              </thead>
              <tbody>
                ${appState.employees.slice(0, 8).map(e => `
                  <tr>
                    <td><span style="font-family: var(--font-mono); color: var(--gold);">${e.id}</span></td>
                    <td><strong>${e.name}</strong></td>
                    <td>${e.team}</td>
                    <td>${e.shift}</td>
                    <td>${e.hours}h</td>
                    <td>${e.dailyTarget ? e.dailyTarget.orders : 14}</td>
                    <td><span style="color: #79D2B7;">99.2%</span></td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>
      `;
    }

    function runCustomReport() {
      showToast('Query executed across 40 workforce records.');
    }

    function exportCustomReportCSV() {
      const csvContent = "data:text/csv;charset=utf-8," +
        "EmpID,Name,Team,Shift,AttendedHours,OrdersKeyed,QualityAccuracy\\n" +
        appState.employees.map(e => `${e.id},${e.name},${e.team},${e.shift},${e.hours},${e.dailyTarget ? e.dailyTarget.orders : 14},99.2%`).join('\\n');

      const encodedUri = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", "PULSE_Custom_Report.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      showToast("Custom Query CSV exported successfully.");
    }

    /* ==========================================================================
       10. CSV / EXCEL IMPORT CENTRE RENDERER
       ========================================================================== */
    function renderImportView() {
      const container = document.getElementById('import-content-container');
      if (!container) return;

      container.innerHTML = `
        <div class="card" style="margin-bottom: 24px;">
          <div class="card-title">
            <span>Biometric Hardware CSV / Excel Ingestion</span>
          </div>
          <div style="border: 2px dashed var(--slate-border); border-radius: 8px; padding: 36px; text-align: center; background: var(--midnight); margin-bottom: 20px;">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" style="margin-bottom: 12px;"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
            <div style="font-size: 15px; font-weight: 500; color: var(--white); margin-bottom: 6px;">
              Drop Biometric CSV Export File Here
            </div>
            <div style="font-size: 12px; color: var(--steel); margin-bottom: 16px;">
              Supports standard TCP/IP machine punch formats (Emp ID, Timestamp, Event Type, Device ID)
            </div>
            <div style="display: flex; justify-content: center; gap: 12px;">
              <input type="file" id="csv-file-input" accept=".csv" style="display: none;" onchange="handleCSVFileSelected(event)" />
              <button class="btn btn-outline btn-sm" onclick="document.getElementById('csv-file-input').click()">
                Select Local CSV File
              </button>
              <button class="btn btn-gold btn-sm" onclick="loadSampleCSVData()">
                Load Sample Turnstile Feed
              </button>
            </div>
          </div>

          <!-- Parsed Rows Preview -->
          <div id="import-preview-container" style="display: none;">
            <div class="card-title">
              <span>Parsed Punch Records (Validation: 5 Passed, 0 Errors)</span>
              <button class="btn btn-gold btn-sm" onclick="executeCSVImport()">
                Execute Ingestion into Live State
              </button>
            </div>
            <div class="data-table-container">
              <table class="data-table">
                <thead>
                  <tr>
                    <th>Emp ID</th>
                    <th>Name</th>
                    <th>Timestamp</th>
                    <th>Event Type</th>
                    <th>Device</th>
                  </tr>
                </thead>
                <tbody id="import-preview-tbody"></tbody>
              </table>
            </div>
          </div>
        </div>
      `;
    }

    function loadSampleCSVData() {
      parsedImportRows = [
        { empId: 'EMP-102', empName: 'Vikram Singh', timestamp: 'Today 05:52 IST', type: 'Office IN', device: 'Terminal 01 (Gate)' },
        { empId: 'EMP-103', empName: 'Ananya Sharma', timestamp: 'Today 05:55 IST', type: 'Office IN', device: 'Terminal 01 (Gate)' },
        { empId: 'EMP-108', empName: 'Pooja Gupta', timestamp: 'Today 09:15 IST', type: 'Break START', device: 'Terminal 02 (Canteen)' },
        { empId: 'EMP-108', empName: 'Pooja Gupta', timestamp: 'Today 09:30 IST', type: 'Break END', device: 'Terminal 02 (Canteen)' },
        { empId: 'EMP-114', empName: 'Kavita Patil', timestamp: 'Today 14:18 IST', type: 'Office IN', device: 'Terminal 01 (Gate)' }
      ];

      const previewContainer = document.getElementById('import-preview-container');
      const tbody = document.getElementById('import-preview-tbody');
      if (previewContainer && tbody) {
        tbody.innerHTML = parsedImportRows.map(r => `
          <tr>
            <td><strong style="color: var(--gold); font-family: var(--font-mono);">${r.empId}</strong></td>
            <td>${r.empName}</td>
            <td style="font-family: var(--font-mono);">${r.timestamp}</td>
            <td><span class="status-badge ${r.type.includes('IN') ? 'in' : r.type.includes('Break') ? 'break' : 'verified'}">${r.type}</span></td>
            <td>${r.device}</td>
          </tr>
        `).join('');
        previewContainer.style.display = 'block';
        showToast('Sample biometric records parsed. Click Execute Ingestion to commit.');
      }
    }

    function handleCSVFileSelected(event) {
      const file = event.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(e) {
        const text = e.target.result;
        const lines = text.split('\\n').filter(l => l.trim().length > 0);
        parsedImportRows = [];

        // Skip header if present
        const startIndex = lines[0].toLowerCase().includes('emp') ? 1 : 0;
        for (let i = startIndex; i < lines.length; i++) {
          const cols = lines[i].split(',').map(c => c.trim().replace(/"/g, ''));
          if (cols.length >= 4) {
            parsedImportRows.push({
              empId: cols[0],
              empName: cols[1] || 'Ingested Employee',
              timestamp: cols[2] || 'Today 06:00 IST',
              type: cols[3] || 'Office IN',
              device: cols[4] || 'Terminal 01'
            });
          }
        }

        const previewContainer = document.getElementById('import-preview-container');
        const tbody = document.getElementById('import-preview-tbody');
        if (previewContainer && tbody) {
          tbody.innerHTML = parsedImportRows.map(r => `
            <tr>
              <td><strong style="color: var(--gold); font-family: var(--font-mono);">${r.empId}</strong></td>
              <td>${r.empName}</td>
              <td style="font-family: var(--font-mono);">${r.timestamp}</td>
              <td><span class="status-badge ${r.type.includes('IN') ? 'in' : 'verified'}">${r.type}</span></td>
              <td>${r.device}</td>
            </tr>
          `).join('');
          previewContainer.style.display = 'block';
          showToast(`Successfully parsed ${parsedImportRows.length} rows from ${file.name}.`);
        }
      };
      reader.readAsText(file);
    }

    function executeCSVImport() {
      if (!parsedImportRows || parsedImportRows.length === 0) return;

      parsedImportRows.forEach(r => {
        appState.biometricPunches.unshift({
          id: `PUN-${Math.floor(1000 + Math.random() * 9000)}`,
          empId: r.empId,
          empName: r.empName,
          timestamp: r.timestamp,
          type: r.type,
          device: r.device,
          method: 'Ingested File Import',
          status: 'Verified'
        });
      });

      renderPunchTable();
      document.getElementById('import-preview-container').style.display = 'none';
      showToast(`${parsedImportRows.length} records successfully committed to live biometric feed.`);
      parsedImportRows = [];
    }

    /* ==========================================================================
       11. EXISTING VIEWS (DASHBOARD, ATTENDANCE, LEAVE, PRODUCTION, QUALITY, AWARDS)
       ========================================================================== */
    function renderDashboard() {
      const container = document.getElementById('dashboard-content-container');
      if (!container) return;
      container.innerHTML = `
        <div class="metric-grid">
          <div class="metric-card">
            <div class="metric-label">Active Attendance</div>
            <div class="metric-value">34 / 40</div>
            <div class="metric-context" style="color: var(--emerald);">85% Floor Presence</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Keying Output</div>
            <div class="metric-value">142 Orders</div>
            <div class="metric-context" style="color: var(--gold);">Target: 135</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Double-Check Rigor</div>
            <div class="metric-value">97.2%</div>
            <div class="metric-context" style="color: #79D2B7;">Verified Compliant</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Melbourne Dispatch SLA</div>
            <div class="metric-value">99.4%</div>
            <div class="metric-context">On-Time Transfer</div>
          </div>
        </div>
      `;
    }

    function renderAttendanceTable() {
      const tbody = document.getElementById('attendance-tbody');
      if (!tbody) return;

      tbody.innerHTML = appState.employees.map(e => `
        <tr>
          <td><span style="font-family: var(--font-mono); color: var(--gold);">${e.id}</span></td>
          <td><strong>${e.name}</strong></td>
          <td>${e.team}</td>
          <td>${e.shift}</td>
          <td><span style="font-family: var(--font-mono);">${e.lateMinutes > 0 ? '06:18 AM' : '05:54 AM'}</span></td>
          <td><span style="font-family: var(--font-mono);">${e.status === 'Present' ? 'In Progress' : '14:26 PM'}</span></td>
          <td><span style="font-family: var(--font-mono);">${e.hours}h</span></td>
          <td><span class="status-badge ${e.status === 'Present' ? 'verified' : e.status === 'On Leave' ? 'warning' : 'out'}">${e.status}</span></td>
        </tr>
      `).join('');
    }

    function filterAttendanceTable() {
      const search = (document.getElementById('attendance-search').value || '').toLowerCase();
      const team = document.getElementById('attendance-filter-team').value;

      const rows = document.querySelectorAll('#attendance-tbody tr');
      rows.forEach(r => {
        const text = r.textContent.toLowerCase();
        const matchesSearch = text.includes(search);
        const matchesTeam = (team === 'ALL') || text.includes(team.toLowerCase());
        r.style.display = (matchesSearch && matchesTeam) ? '' : 'none';
      });
    }

    function renderLeaveTables() {
      const container = document.getElementById('leave-content-container');
      if (!container) return;

      const leaves = appState.leaveRequests || [];
      container.innerHTML = `
        <div class="data-table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>Request ID</th>
                <th>Employee Name</th>
                <th>Leave Type</th>
                <th>Requested Date</th>
                <th>Reason (HR Protected)</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              ${leaves.map(l => `
                <tr>
                  <td><strong style="color: var(--steel); font-family: var(--font-mono);">${l.id}</strong></td>
                  <td><strong>${l.empName}</strong> (${l.empId})</td>
                  <td>${l.type}</td>
                  <td style="font-family: var(--font-mono);">${l.date}</td>
                  <td>${l.reason}</td>
                  <td><span class="status-badge ${l.status === 'Approved' ? 'verified' : 'warning'}">${l.status}</span></td>
                  <td>
                    ${l.status === 'Pending' ? `
                      <button class="btn btn-gold btn-sm" onclick="approveLeave('${l.id}')">Approve</button>
                    ` : '<span style="color: var(--steel-dim); font-size: 11px;">Completed</span>'}
                  </td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      `;
    }

    function approveLeave(leaveId) {
      const l = appState.leaveRequests.find(item => item.id === leaveId);
      if (l) {
        l.status = 'Approved';
        renderLeaveTables();
        showToast(`Leave request #${leaveId} approved.`);
      }
    }

    function submitLeaveRequest() {
      const empId = document.getElementById('leave-emp-select').value;
      const type = document.getElementById('leave-type-select').value;
      const date = document.getElementById('leave-date-input').value;
      const reason = document.getElementById('leave-reason-input').value;

      const emp = appState.employees.find(e => e.id === empId);
      const newLeave = {
        id: `LR-${Math.floor(100 + Math.random() * 900)}`,
        empId: empId,
        empName: emp ? emp.name : 'Unknown',
        type: type,
        date: date,
        reason: reason || 'Personal Leave',
        status: 'Pending'
      };

      appState.leaveRequests.unshift(newLeave);
      closeModal('modal-apply-leave');
      renderLeaveTables();
      showToast('Leave request submitted successfully.');
    }

    function renderProductionTable() {
      const container = document.getElementById('production-content-container');
      if (!container) return;

      const records = appState.productionRecords || [];
      container.innerHTML = `
        <div class="data-table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>Record ID</th>
                <th>Team / Cell</th>
                <th>Shift</th>
                <th>Orders Keyed</th>
                <th>Flashings (m)</th>
                <th>Bits & Parts</th>
                <th>Double Checks</th>
                <th>Accuracy</th>
              </tr>
            </thead>
            <tbody>
              ${records.map(r => `
                <tr>
                  <td><strong style="color: var(--steel); font-family: var(--font-mono);">${r.id}</strong></td>
                  <td><strong>${r.team}</strong></td>
                  <td>${r.shift}</td>
                  <td>${r.orders}</td>
                  <td>${r.flashings}m</td>
                  <td>${r.bits}</td>
                  <td>${r.doubleChecks}</td>
                  <td><span style="color: #79D2B7;">${r.accuracy}</span></td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      `;
    }

    function submitProductionEntry() {
      const team = document.getElementById('prod-team-select').value;
      const orders = parseInt(document.getElementById('prod-orders-input').value, 10) || 0;
      const flashings = parseInt(document.getElementById('prod-flashings-input').value, 10) || 0;
      const bits = parseInt(document.getElementById('prod-bits-input').value, 10) || 0;
      const checks = parseInt(document.getElementById('prod-checks-input').value, 10) || 0;

      const newRecord = {
        id: `PR-${Math.floor(1000 + Math.random() * 9000)}`,
        team: team,
        shift: 'Shift A',
        orders: orders,
        flashings: flashings,
        bits: bits,
        doubleChecks: checks,
        accuracy: '99.0%'
      };

      appState.productionRecords.unshift(newRecord);
      closeModal('modal-production-entry');
      renderProductionTable();
      showToast(`Recorded output for ${team} (${orders} orders, ${flashings}m flashings).`);
    }

    function renderQualityCases() {
      const container = document.getElementById('quality-content-container');
      if (!container) return;

      const cases = appState.qualityCases || [];
      container.innerHTML = `
        <div style="display: flex; flex-direction: column; gap: 14px;">
          ${cases.map(c => `
            <div class="card" style="border-left: 4px solid ${c.status === 'Resolved' ? 'var(--emerald)' : 'var(--amber)'};">
              <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                  <strong style="color: var(--white); font-size: 14px;">${c.id}: ${c.title}</strong>
                  <span class="status-badge ${c.status === 'Resolved' ? 'verified' : 'warning'}">${c.status}</span>
                </div>
                <span style="font-family: var(--font-mono); font-size: 11px; color: var(--gold);">Reported: Melbourne Dry-Fit</span>
              </div>
              <div style="font-size: 13px; color: var(--porcelain); margin-bottom: 8px; line-height: 1.5;">
                ${c.description}
              </div>
              <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px; font-size: 12px; color: var(--steel);">
                <strong style="color: var(--gold);">Zero-Blame Learning Action:</strong> ${c.action}
              </div>
            </div>
          `).join('')}
        </div>
      `;
    }

    function renderAwards() {
      const container = document.getElementById('recognition-content-container');
      if (!container) return;

      const awards = appState.awards || [];
      container.innerHTML = `
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
          ${awards.map(a => `
            <div class="card" style="border-top: 3px solid var(--gold);">
              <div style="font-family: var(--font-mono); font-size: 11px; color: var(--gold); margin-bottom: 6px;">${a.category}</div>
              <h3 style="font-size: 17px; color: var(--white); margin-bottom: 4px;">${a.empName}</h3>
              <div style="font-size: 12px; color: var(--steel); margin-bottom: 12px;">${a.team} • Nominated by ${a.nominatedBy}</div>
              <p style="font-size: 13px; color: var(--porcelain); line-height: 1.6;">"${a.citation}"</p>
            </div>
          `).join('')}
        </div>
      `;
    }

    function submitNomination() {
      const empId = document.getElementById('nominate-emp-select').value;
      const category = document.getElementById('nominate-category').value;
      const citation = document.getElementById('nominate-citation').value;

      const emp = appState.employees.find(e => e.id === empId);
      const newAward = {
        id: `AWD-${Math.floor(100 + Math.random() * 900)}`,
        empId: empId,
        empName: emp ? emp.name : 'Unknown',
        team: emp ? emp.team : 'India Operations',
        category: category,
        citation: citation || 'Demonstrated outstanding teamwork and craftsmanship.',
        nominatedBy: currentRole === 'PRESENTER' ? 'Rakshith' : 'Team Colleague'
      };

      appState.awards.unshift(newAward);
      closeModal('modal-nominate');
      renderAwards();
      showToast(`Nomination recorded for ${emp ? emp.name : empId}.`);
    }

    function renderRolesView() {
      const container = document.getElementById('roles-content-container');
      if (!container) return;

      container.innerHTML = `
        <div class="card">
          <div class="card-title">Role Permissions & Privacy Governance Matrix</div>
          <div class="data-table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Role</th>
                  <th>Attendance & Clocks</th>
                  <th>Production Logs</th>
                  <th>Quality RCA Cases</th>
                  <th>Confidential Mentorship</th>
                  <th>Export Controls</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Presenter (Rakshith)</strong></td>
                  <td><span class="status-badge verified">Full Visibility</span></td>
                  <td><span class="status-badge verified">Full Access</span></td>
                  <td><span class="status-badge verified">Full Access</span></td>
                  <td><span class="status-badge verified">Unlocked</span></td>
                  <td><span class="status-badge verified">Enabled</span></td>
                </tr>
                <tr>
                  <td><strong>Management (MD)</strong></td>
                  <td><span class="status-badge verified">Full Visibility</span></td>
                  <td><span class="status-badge verified">Full Access</span></td>
                  <td><span class="status-badge verified">Full Access</span></td>
                  <td><span class="status-badge verified">Unlocked</span></td>
                  <td><span class="status-badge verified">Enabled</span></td>
                </tr>
                <tr>
                  <td><strong>Team Leader</strong></td>
                  <td><span class="status-badge verified">Team Scope</span></td>
                  <td><span class="status-badge verified">Log Output</span></td>
                  <td><span class="status-badge verified">Participate</span></td>
                  <td><span class="status-badge verified">Unlocked</span></td>
                  <td><span class="status-badge verified">Enabled</span></td>
                </tr>
                <tr>
                  <td><strong>Employee</strong></td>
                  <td><span class="status-badge verified">Personal & Feed</span></td>
                  <td><span class="status-badge verified">Personal View</span></td>
                  <td><span class="status-badge verified">Learning View</span></td>
                  <td><span class="status-badge alert">Restricted / Locked</span></td>
                  <td><span class="status-badge warning">View Only</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      `;
    }

    /* ==========================================================================
       MODAL CONTROLLERS & NOTIFICATIONS
       ========================================================================== */
    function openModal(modalId) {
      const el = document.getElementById(modalId);
      if (el) el.classList.add('open');
    }

    function closeModal(modalId) {
      const el = document.getElementById(modalId);
      if (el) el.classList.remove('open');
    }

    function openApplyLeaveModal() { openModal('modal-apply-leave'); }
    function openProductionModal() { openModal('modal-production-entry'); }
    function openNominationModal() { openModal('modal-nominate'); }

    function showToast(message) {
      const container = document.getElementById('toast-container');
      if (!container) return;

      const toast = document.createElement('div');
      toast.className = 'toast-msg';
      toast.innerHTML = `
        <span class="pulse-dot"></span>
        <span>${message}</span>
      `;
      container.appendChild(toast);

      setTimeout(() => {
        toast.style.animation = 'toastOut 0.3s ease forwards';
        setTimeout(() => toast.remove(), 300);
      }, 3400);
    }

    function resetDemoData() {
      appState = JSON.parse(JSON.stringify(MASTER_DATA));
      renderAllViews();
      showToast('Master demo data reset: All simulated records restored to pristine showcase state.');
    }
"""

print("parts_js.py created successfully.")
