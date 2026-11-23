# Complete JavaScript Operational Engine for PULSE Executive Showcase

JS_CONTENT = r"""
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
    let currentEmpTab = 'overview';
    let parsedImportRows = [];

    let lastVisitedScene = 1;
    if (typeof window !== 'undefined') {
      window.appState = appState;
      window.currentRole = currentRole;
      window.selected360EmpId = selected360EmpId;
    }

    // Scene Meta for Overview
    const SCENES_META = [
      { id: 1, title: 'Strategic Imperative', desc: 'Opening Hook: Every Shift Tells a Story' },
      { id: 2, title: 'Current Operations', desc: 'Our Teams Work Hard. Our Reports Work Separately.' },
      { id: 3, title: 'Introducing PULSE', desc: 'One Place for Everything That Matters' },
      { id: 4, title: 'Attendance Records', desc: 'Know Who\'s Here. When They Arrived. And When They Leave.' },
      { id: 5, title: 'Daily Work Output', desc: 'Every Order. Every Flashing. Every Contribution.' },
      { id: 6, title: 'Shift Continuity', desc: 'When One Shift Ends, The Next Starts Informed.' },
      { id: 7, title: 'Employee Development', desc: 'Understand Performance. Recognize Progress.' },
      { id: 8, title: 'Executive View', desc: 'Your Entire Operation. One Clear View.' },
      { id: 9, title: 'Internship Proposal', desc: 'Proposed MCA 4th-Semester Internship Project' }
    ];

    /* ==========================================================================
       INITIALIZATION
       ========================================================================== */
    function initApp() {
      initDualClocks();
      initStoryMode();
      populateDropdowns();
      renderAllViews();

      // Check URL parameters & hash for direct deep-linking
      try {
        const params = new URLSearchParams(window.location.search);
        const scParam = params.get('scene');
        const viewParam = params.get('view');
        if (scParam) {
          const scNum = parseInt(scParam, 10);
          if (!isNaN(scNum)) goToScene(scNum);
        } else if (viewParam) {
          switchToProductMode();
          switchView(viewParam);
        } else if (window.location.hash) {
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
      } catch (err) {}
    }

    if (document.readyState === 'loading') {
      window.addEventListener('DOMContentLoaded', initApp);
    } else {
      initApp();
    }

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
       ========================================================================== */
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
      if (storyContainer && storyContainer.classList.contains('hidden')) return;

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
      for (let i = 1; i <= TOTAL_SCENES; i++) {
        const sc = document.getElementById(`scene-${i}`);
        if (sc) sc.classList.remove('active');
      }

      const activeSc = document.getElementById(`scene-${currentScene}`);
      if (activeSc) activeSc.classList.add('active');

      const indicator = document.getElementById('scene-counter-display');
      if (indicator) indicator.textContent = `SCENE 0${currentScene} / 0${TOTAL_SCENES}`;

      const dots = document.querySelectorAll('.story-dot');
      dots.forEach((dot, idx) => {
        if (idx === currentScene - 1) {
          dot.classList.add('active');
        } else {
          dot.classList.remove('active');
        }
      });

      // Update scene progression bar
      const prog = document.getElementById('story-progress-fill');
      if (prog) {
        prog.style.width = `${(currentScene / TOTAL_SCENES) * 100}%`;
      }

      // Update URL hash without scroll
      history.replaceState(null, null, `#scene-${currentScene}`);
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
        lastVisitedScene = sceneNum;
        updateSceneDisplay();
        const storyCont = document.getElementById('story-mode-container');
        const prodCont = document.getElementById('product-mode-container');
        if (storyCont && prodCont) {
          prodCont.classList.add('hidden');
          storyCont.classList.remove('hidden');
        }
      }
    }

    function toggleConsolidateSheets() {
      const stage = document.getElementById('sheets-stage-container');
      if (!stage) return;
      stage.classList.toggle('sheets-consolidated');
      if (typeof showToast === 'function') {
        showToast(stage.classList.contains('sheets-consolidated') ? 
          'Information unified into single operational hub' : 
          'Demonstrating fragmented reporting silos');
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

    /* ==========================================================================
       VIEW & MODE SWITCHING
       ========================================================================== */
    function exploreFeature(viewName) {
      lastVisitedScene = currentScene;
      switchToProductMode();
      switchView(viewName);
    }

    function switchToProductMode() {
      lastVisitedScene = currentScene;
      const storyCont = document.getElementById('story-mode-container');
      const prodCont = document.getElementById('product-mode-container');
      if (storyCont && prodCont) {
        storyCont.classList.add('hidden');
        prodCont.classList.remove('hidden');
        history.replaceState(null, null, '#product');
      }
    }

    function switchToStoryMode() {
      const storyCont = document.getElementById('story-mode-container');
      const prodCont = document.getElementById('product-mode-container');
      if (storyCont && prodCont) {
        prodCont.classList.add('hidden');
        storyCont.classList.remove('hidden');
        goToScene(lastVisitedScene || 1);
      }
    }

    function switchView(viewName) {
      const menuItems = document.querySelectorAll('.app-sidebar .menu-item');
      menuItems.forEach(item => item.classList.remove('active'));

      // Highlight clicked sidebar item
      const clicked = window.event ? window.event.currentTarget : null;
      if (clicked && clicked.classList && clicked.classList.contains('menu-item')) {
        clicked.classList.add('active');
      } else {
        menuItems.forEach(item => {
          const oc = item.getAttribute('onclick') || '';
          if (oc.includes(`'${viewName}'`) || oc.includes(`"${viewName}"`)) {
            item.classList.add('active');
          }
        });
      }

      const panels = document.querySelectorAll('.view-panel');
      panels.forEach(p => p.classList.remove('active'));

      const target = document.getElementById(`view-${viewName}`);
      if (target) {
        target.classList.add('active');
        const main = document.querySelector('.app-main');
        if (main) main.scrollTop = 0;
      }
    }

    /* ==========================================================================
       ROLE PROFILES & PERMISSIONS
       ========================================================================== */
    function onRoleChange(role) {
      currentRole = role;
      if (typeof window !== 'undefined') window.currentRole = role;
      const profiles = {
        'PRESENTER': { name: 'Rakshith', title: 'Operational Strategist', avatar: 'RK' },
        'MANAGEMENT': { name: 'David Harrison', title: 'Managing Director', avatar: 'DH' },
        'TEAM_LEADER': { name: 'Priya Nair', title: 'Shift A Team Leader', avatar: 'PN' },
        'EMPLOYEE': { name: 'Rohan Sharma', title: 'Senior Keying Specialist', avatar: 'RS' },
        'SUPER_ADMIN': { name: 'Alex Vance', title: 'Super Administrator', avatar: 'AV' }
      };

      const p = profiles[role] || profiles['PRESENTER'];
      const elName = document.getElementById('user-name-display');
      const elRole = document.getElementById('user-role-display');
      const elAvatar = document.getElementById('user-avatar-badge');
      if (elName) elName.textContent = p.name;
      if (elRole) elRole.textContent = p.title;
      if (elAvatar) elAvatar.textContent = p.avatar;

      const selRole = document.getElementById('role-select');
      if (selRole && selRole.value !== role) selRole.value = role;

      // Re-render views to reflect dynamic confidentiality & role permissions
      renderAllViews();
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
          <option value="${e.id}">${e.name} (${e.id}) — ${e.designation || e.role || 'Specialist'}</option>
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
      const elAlerts = document.getElementById('badge-alert-count');
      if (elAlerts) elAlerts.textContent = `${openAlerts} open`;

      const leaves = appState.leaveRequests || [];
      const pendingLeaves = leaves.filter(l => l.status === 'Pending').length;
      const elLeaves = document.getElementById('badge-leave-count');
      if (elLeaves) elLeaves.textContent = `${pendingLeaves} pending`;

      const quality = appState.qualityCases || [];
      const activeQ = quality.filter(q => q.status !== 'Closed' && q.status !== 'Resolved').length;
      const elQ = document.getElementById('badge-quality-active');
      if (elQ) elQ.textContent = `${activeQ} active`;
    }

    /* ==========================================================================
       1. TODAY'S OPERATIONS RENDERER
       ========================================================================== */
    function renderCommandCentre() {
      const emps = appState.employees || [];
      const presentEmps = emps.filter(e => e.status === 'Present');
      const leaveEmps = emps.filter(e => e.status === 'On Leave');
      const absentEmps = emps.filter(e => e.status === 'Absent');
      const lateEmps = emps.filter(e => (e.lateMinutes || 0) > 0 || e.isLate);

      const elPresent = document.getElementById('cc-emp-present-count');
      if (elPresent) elPresent.textContent = presentEmps.length;
      const elLeave = document.getElementById('cc-emp-leave-count');
      if (elLeave) elLeave.textContent = `${leaveEmps.length} employees`;
      const elAbsent = document.getElementById('cc-emp-absent-count');
      if (elAbsent) elAbsent.textContent = `${absentEmps.length} employee`;
      const elLate = document.getElementById('cc-emp-late-count');
      if (elLate) elLate.textContent = `${lateEmps.length || 2} (compensated)`;

      const prods = appState.productionRecords || [];
      const totalOrders = prods.reduce((sum, p) => sum + (parseInt(p.orders, 10) || 0), 0);
      const totalFlashings = prods.reduce((sum, p) => sum + (parseInt(p.flashings, 10) || 0), 0);
      const totalBits = prods.reduce((sum, p) => sum + (parseInt(p.bits, 10) || 0), 0);
      const totalChecks = prods.reduce((sum, p) => sum + (parseInt(p.doubleChecks, 10) || 0), 0);

      const elOrders = document.getElementById('cc-orders-count');
      if (elOrders) elOrders.textContent = totalOrders;
      const elFlashings = document.getElementById('cc-flashings-count');
      if (elFlashings) elFlashings.textContent = `${Math.round(totalFlashings * 1.87)} linear metres`;
      const elBits = document.getElementById('cc-bits-count');
      if (elBits) elBits.textContent = `${Math.round(totalBits * 18.4)} individual parts`;
      const elChecks = document.getElementById('cc-checks-count');
      if (elChecks) elChecks.textContent = `${totalChecks} verified (${totalOrders > 0 ? ((totalChecks / totalOrders) * 100).toFixed(1) : '97.2'}%)`;

      const quality = appState.qualityCases || [];
      const openCases = quality.filter(q => q.status !== 'Closed' && q.status !== 'Resolved');
      const closedCases = quality.filter(q => q.status === 'Closed' || q.status === 'Resolved');

      const elOpenQ = document.getElementById('cc-open-cases-count');
      if (elOpenQ) elOpenQ.textContent = `${openCases.length} under review`;
      const elResolvedQ = document.getElementById('cc-resolved-count');
      if (elResolvedQ) elResolvedQ.textContent = `${closedCases.length} case closed`;
      const elQualityPct = document.getElementById('cc-quality-pct');
      if (elQualityPct) {
        elQualityPct.textContent = openCases.length === 0 ? '99.4%' : openCases.length === 1 ? '99.0%' : '98.6%';
      }
    }

    /* ==========================================================================
       2. ENTRY, EXIT & BREAKS (BIOMETRIC ATTENDANCE) RENDERER
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
        punches = punches.filter(p => (p.type || '').includes('Break'));
      } else if (activePunchFilter === 'EXCEPTION') {
        punches = punches.filter(p => (p.type || '').includes('Manual') || (p.type || '').includes('Adjustment'));
      }

      tbody.innerHTML = punches.map(p => {
        let badgeClass = 'verified';
        const pType = p.type || 'Office IN';
        if (pType === 'Office IN') badgeClass = 'in';
        else if (pType === 'Office OUT') badgeClass = 'out';
        else if (pType.includes('Break')) badgeClass = 'break';
        else badgeClass = 'exception';

        const punchId = p.punchId || p.id || 'PUN-1001';
        const empId = p.empId || 'EMP-101';
        const empName = p.empName || 'Employee';
        const timeStr = p.timeIST || p.timestamp || '06:00 AM IST';
        const device = p.device || 'Terminal 01 (Gate)';
        const method = p.source || p.method || 'Biometric Scanner';
        const status = p.status || 'Verified';

        return `
          <tr>
            <td><strong style="color: var(--steel); font-family: var(--font-mono);">${punchId}</strong></td>
            <td><span style="font-family: var(--font-mono); color: var(--gold);">${empId}</span></td>
            <td><strong>${empName}</strong></td>
            <td><span style="font-family: var(--font-mono); color: var(--white);">${timeStr}</span></td>
            <td><span class="status-badge ${badgeClass}">${pType}</span></td>
            <td>${device}</td>
            <td><span style="color: var(--steel); font-size: 12px;">${method}</span></td>
            <td><span class="status-badge verified">${status}</span></td>
          </tr>
        `;
      }).join('');
    }

    function renderBiometricTimeline(empId) {
      const summaryContainer = document.getElementById('timeline-summary-container');
      const visualContainer = document.getElementById('timeline-visual-container');
      if (!visualContainer) return;

      const emp = (appState.employees || []).find(e => e.id === empId) || (appState.employees && appState.employees[0]) || { name: 'Rohan Sharma', id: 'EMP-101' };
      const timelineData = (appState.employeeAttendanceTimelines && appState.employeeAttendanceTimelines[empId]) || {
        empId: empId,
        firstEntry: '05:58 AM',
        lastExit: 'In Progress (Shift A)',
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

      if (summaryContainer) {
        summaryContainer.innerHTML = `
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; background: var(--midnight); padding: 16px; border: 1px solid var(--slate-border); border-radius: 6px;">
            <div>
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">First Entry Punch</div>
              <div style="font-size: 18px; font-weight: 600; color: #79D2B7; font-family: var(--font-mono);">${timelineData.firstEntry || '05:58 AM'}</div>
              <div style="font-size: 11px; color: var(--steel-dim);">Expected: ${timelineData.expectedStart || '06:00 AM'}</div>
            </div>
            <div>
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Time on Premises</div>
              <div style="font-size: 18px; font-weight: 600; color: var(--white); font-family: var(--font-mono);">${timelineData.timeOnPremises || '7h 12m'}</div>
              <div style="font-size: 11px; color: var(--steel-dim);">Gate Entry to Current</div>
            </div>
            <div>
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Recorded Breaks</div>
              <div style="font-size: 18px; font-weight: 600; color: var(--amber); font-family: var(--font-mono);">${timelineData.recordedBreakDuration || '45m'}</div>
              <div style="font-size: 11px; color: var(--steel-dim);">Tea (15m) + Lunch (30m)</div>
            </div>
            <div>
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Net Attended Duration</div>
              <div style="font-size: 18px; font-weight: 600; color: var(--gold); font-family: var(--font-mono);">${timelineData.netAttendedDuration || '6h 27m'}</div>
              <div style="font-size: 11px; color: #79D2B7;">Status: ${timelineData.regularizationStatus || 'Compliant'}</div>
            </div>
          </div>
        `;
      }

      visualContainer.innerHTML = `
        <div style="display: flex; flex-direction: column; gap: 12px; position: relative; padding-left: 30px;">
          <div style="position: absolute; left: 11px; top: 12px; bottom: 12px; width: 2px; background: rgba(147, 163, 174, 0.25);"></div>
          ${(timelineData.events || []).map(ev => {
            let dotColor = 'var(--emerald)';
            if ((ev.type || '').includes('OUT')) dotColor = 'var(--crimson)';
            else if ((ev.type || '').includes('Break')) dotColor = 'var(--amber)';

            return `
              <div style="display: flex; align-items: center; justify-content: space-between; padding: 10px 14px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px; position: relative;">
                <div style="position: absolute; left: -25px; width: 12px; height: 12px; border-radius: 50%; background: ${dotColor}; border: 2px solid var(--midnight);"></div>
                <div style="display: flex; align-items: center; gap: 14px;">
                  <strong style="font-family: var(--font-mono); color: var(--white); font-size: 13px;">${ev.time} IST</strong>
                  <span class="status-badge ${(ev.type || '').includes('IN') ? 'in' : (ev.type || '').includes('OUT') ? 'out' : 'break'}">${ev.type}</span>
                  <span style="color: var(--porcelain); font-size: 13px;">${ev.label}</span>
                </div>
                <span class="status-badge verified">${ev.status || 'Verified'}</span>
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

      const emp = (appState.employees || []).find(e => e.id === empId);
      const newPunch = {
        id: `PUN-${Math.floor(1000 + Math.random() * 9000)}`,
        punchId: `PUN-${Math.floor(1000 + Math.random() * 9000)}`,
        empId: empId,
        empName: emp ? emp.name : 'Unknown',
        timestamp: `Today ${time} IST`,
        timeIST: `${time} IST`,
        timeAEST: '10:45 AEDT',
        type: type,
        device: 'Manual Regularization Interface',
        source: 'Manager Approved Override',
        method: 'Manager Approved Override',
        status: 'Regularized'
      };

      appState.biometricPunches.unshift(newPunch);
      closeModal('modal-biometric-punch');
      renderPunchTable();
      showToast(`Biometric punch regularized for ${emp ? emp.name : empId} (${type} at ${time} IST).`);
    }

    /* ==========================================================================
       3. EMPLOYEE PERFORMANCE (5 CLEAR TABS)
       ========================================================================== */
    function switchEmpTab(tabName) {
      currentEmpTab = tabName;
      renderEmployee360(selected360EmpId);
    }

    function renderEmployee360(empId) {
      selected360EmpId = empId;
      const container = document.getElementById('emp360-content-container');
      if (!container) return;

      const emp = (appState.employees || []).find(e => e.id === empId) || (appState.employees && appState.employees[0]) || {
        id: 'EMP-101',
        name: 'Rohan Sharma',
        role: 'Senior Detailing Specialist',
        designation: 'Senior Detailing Specialist',
        team: 'Team Alpha',
        shift: 'Shift A (Day)',
        manager: 'Priya Nair',
        status: 'Present',
        hours: 7.5,
        accuracy: '99.2%',
        accuracyText: '99.2%',
        dailyTarget: { orders: 16, flashings: 210, bits: 480 }
      };

      const isRestrictedRole = (currentRole === 'EMPLOYEE');
      const initials = (emp.name || 'RS').split(' ').map(n => n[0]).join('');
      const empRole = emp.designation || emp.role || 'Sheetmetal Specialist';
      const empHours = emp.hours != null ? emp.hours : 7.5;
      const empAcc = emp.accuracyText || emp.accuracy || '99.2%';
      const dailyOrders = (emp.dailyTarget && emp.dailyTarget.orders) ? emp.dailyTarget.orders : 16;
      const dailyFlashings = (emp.dailyTarget && emp.dailyTarget.flashings) ? emp.dailyTarget.flashings : 210;
      const dailyBits = (emp.dailyTarget && emp.dailyTarget.bits) ? emp.dailyTarget.bits : 480;

      // Clean skills list
      let skillList = [];
      if (Array.isArray(emp.skills)) {
        skillList = emp.skills;
      } else if (emp.skills && typeof emp.skills === 'object') {
        skillList = Object.entries(emp.skills).map(([k, v]) => `${k.replace(/([A-Z])/g, ' $1').toUpperCase()}: ${v}`);
      } else {
        skillList = ['Order Keying (L4)', 'Flashing Detailing (L4)', 'Quality Review (L3)'];
      }

      // Tab navigation HTML
      const tabs = [
        { id: 'overview', label: '1. Overview' },
        { id: 'attendance', label: '2. Attendance' },
        { id: 'work', label: '3. Work Completed' },
        { id: 'quality', label: '4. Quality Record' },
        { id: 'growth', label: '5. Growth & Mentorship' }
      ];

      const tabNavHtml = `
        <div style="display: flex; gap: 8px; border-bottom: 1px solid var(--slate-border); margin-bottom: 20px;">
          ${tabs.map(t => `
            <button onclick="switchEmpTab('${t.id}')" style="background: none; border: none; padding: 10px 18px; font-size: 13px; font-weight: 500; cursor: pointer; color: ${currentEmpTab === t.id ? 'var(--gold)' : 'var(--steel)'}; border-bottom: 2px solid ${currentEmpTab === t.id ? 'var(--gold)' : 'transparent'}; transition: all 0.2s ease;">
              ${t.label}
            </button>
          `).join('')}
        </div>
      `;

      // Header Card (Common across all tabs)
      const headerCard = `
        <div class="card" style="margin-bottom: 20px; background: rgba(24, 38, 49, 0.7); border: 1px solid var(--gold-border);">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px;">
            <div style="display: flex; gap: 16px; align-items: center;">
              <div style="width: 54px; height: 54px; border-radius: 50%; background: var(--gold-dim); border: 2px solid var(--gold); display: flex; align-items: center; justify-content: center; font-family: var(--font-mono); font-size: 18px; color: var(--gold); font-weight: bold;">
                ${initials}
              </div>
              <div>
                <div style="display: flex; align-items: center; gap: 10px;">
                  <h2 style="font-size: 20px; color: var(--white);">${emp.name}</h2>
                  <span class="status-badge ${emp.status === 'Present' ? 'verified' : emp.status === 'On Leave' ? 'warning' : 'out'}">${emp.status}</span>
                  <span style="font-family: var(--font-mono); font-size: 12px; color: var(--gold);">${emp.id}</span>
                </div>
                <div style="font-size: 13px; color: var(--steel); margin-top: 4px;">
                  ${empRole} • ${emp.team} • Reports to <strong>${emp.manager || 'Priya Nair'}</strong>
                </div>
              </div>
            </div>
            <div style="text-align: right; font-family: var(--font-mono); font-size: 12px;">
              <div style="color: var(--steel-dim);">Assigned Shift</div>
              <div style="color: var(--gold); font-weight: 600;">${emp.shift}</div>
              <div style="color: var(--steel); margin-top: 2px;">Monday, 23 November 2026</div>
            </div>
          </div>
        </div>
      `;

      // Dynamic Tab Body Content
      let tabBodyContent = '';

      if (currentEmpTab === 'overview') {
        tabBodyContent = `
          <!-- 4 Core Overview Cards -->
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 20px;">
            <div class="card" style="padding: 16px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Today's Attendance</div>
              <div style="font-size: 22px; font-weight: 600; color: #79D2B7; font-family: var(--font-serif); margin: 4px 0;">${empHours}h</div>
              <div style="font-size: 11px; color: var(--steel-dim);">Clocked in at 05:54 AM</div>
            </div>
            <div class="card" style="padding: 16px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Orders Completed</div>
              <div style="font-size: 22px; font-weight: 600; color: var(--gold); font-family: var(--font-serif); margin: 4px 0;">${dailyOrders} Orders</div>
              <div style="font-size: 11px; color: var(--steel-dim);">${dailyFlashings}m Flashings • ${dailyBits} Parts</div>
            </div>
            <div class="card" style="padding: 16px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Quality Accuracy</div>
              <div style="font-size: 22px; font-weight: 600; color: #79D2B7; font-family: var(--font-serif); margin: 4px 0;">${empAcc}</div>
              <div style="font-size: 11px; color: var(--steel-dim);">First-Pass Verification</div>
            </div>
            <div class="card" style="padding: 16px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Double-Check Results</div>
              <div style="font-size: 22px; font-weight: 600; color: var(--white); font-family: var(--font-serif); margin: 4px 0;">100%</div>
              <div style="font-size: 11px; color: var(--steel-dim);">All orders peer verified</div>
            </div>
          </div>

          <!-- Skills Badges Card -->
          <div class="card" style="margin-bottom: 20px;">
            <div class="card-title">Sheetmetal Core Skills</div>
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
              ${skillList.map(s => `
                <span style="padding: 6px 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px; font-size: 12px; color: var(--porcelain); font-family: var(--font-mono);">
                  ${s}
                </span>
              `).join('')}
            </div>
          </div>

          <!-- Summary Insight Card -->
          <div class="card" style="border-left: 4px solid var(--gold);">
            <div style="font-family: var(--font-mono); font-size: 11px; color: var(--gold); margin-bottom: 6px;">PERFORMANCE NOTE</div>
            <p style="font-size: 13px; color: var(--porcelain); line-height: 1.6; margin: 0;">
              <strong>${emp.name}</strong> is a high-accuracy operator in <strong>${emp.team}</strong>. Consistently meets daily production targets while maintaining exceptional double-check rigor and clean drawings for Australian site assembly.
            </p>
          </div>
        `;
      } else if (currentEmpTab === 'attendance') {
        tabBodyContent = `
          <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
            <div class="card">
              <div class="card-title">Biometric Entry & Exit Details</div>
              <div style="display: flex; flex-direction: column; gap: 12px; font-size: 13px;">
                <div style="display: flex; justify-content: space-between; padding-bottom: 8px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--steel);">First Gate Entry:</span>
                  <strong style="color: #79D2B7; font-family: var(--font-mono);">05:54 AM IST</strong>
                </div>
                <div style="display: flex; justify-content: space-between; padding-bottom: 8px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--steel);">Assigned Shift Hours:</span>
                  <strong style="color: var(--white); font-family: var(--font-mono);">06:00 AM — 14:30 PM IST</strong>
                </div>
                <div style="display: flex; justify-content: space-between; padding-bottom: 8px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--steel);">Arrival Status:</span>
                  <strong style="color: #79D2B7;">On-Time (6m early)</strong>
                </div>
                <div style="display: flex; justify-content: space-between; padding-bottom: 8px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--steel);">Total Time on Premises:</span>
                  <strong style="color: var(--white); font-family: var(--font-mono);">8h 32m</strong>
                </div>
                <div style="display: flex; justify-content: space-between; padding-bottom: 8px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--steel);">Total Break Duration:</span>
                  <strong style="color: var(--amber); font-family: var(--font-mono);">45 minutes (Compliant)</strong>
                </div>
                <div style="display: flex; justify-content: space-between;">
                  <span style="color: var(--steel);">Net Attended Duration:</span>
                  <strong style="color: var(--gold); font-family: var(--font-mono);">${empHours} hours</strong>
                </div>
              </div>
            </div>

            <div class="card">
              <div class="card-title">Monthly Attendance Summary (November 2026)</div>
              <div style="display: flex; flex-direction: column; gap: 12px; font-size: 13px;">
                <div style="display: flex; justify-content: space-between; padding-bottom: 8px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--steel);">Working Days:</span>
                  <strong style="color: var(--white);">23 Days Scheduled</strong>
                </div>
                <div style="display: flex; justify-content: space-between; padding-bottom: 8px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--steel);">Days Present:</span>
                  <strong style="color: #79D2B7;">22 Days Present</strong>
                </div>
                <div style="display: flex; justify-content: space-between; padding-bottom: 8px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--steel);">Approved Leave:</span>
                  <strong style="color: var(--porcelain);">1 Day (Annual Leave)</strong>
                </div>
                <div style="display: flex; justify-content: space-between; padding-bottom: 8px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--steel);">Late Arrivals:</span>
                  <strong style="color: var(--porcelain);">0 Late (100% Punctual)</strong>
                </div>
                <div style="display: flex; justify-content: space-between;">
                  <span style="color: var(--steel);">Reliability Score:</span>
                  <strong style="color: var(--gold);">99.1%</strong>
                </div>
              </div>
            </div>
          </div>
        `;
      } else if (currentEmpTab === 'work') {
        tabBodyContent = `
          <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
            <div class="card">
              <div class="card-title">Daily Work Completed (Shift A)</div>
              <div style="display: flex; flex-direction: column; gap: 12px; font-size: 13px;">
                <div style="display: flex; justify-content: space-between; padding-bottom: 8px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--steel);">Orders Keyed:</span>
                  <strong style="color: var(--gold); font-size: 15px;">${dailyOrders} Orders</strong>
                </div>
                <div style="display: flex; justify-content: space-between; padding-bottom: 8px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--steel);">Flashings Detailed:</span>
                  <strong style="color: var(--white);">${dailyFlashings} linear metres</strong>
                </div>
                <div style="display: flex; justify-content: space-between; padding-bottom: 8px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--steel);">Bits & Accessories:</span>
                  <strong style="color: var(--white);">${dailyBits} individual parts</strong>
                </div>
                <div style="display: flex; justify-content: space-between;">
                  <span style="color: var(--steel);">Shift Target Achievement:</span>
                  <strong style="color: #79D2B7;">106% of Daily Target</strong>
                </div>
              </div>
            </div>

            <div class="card">
              <div class="card-title">Double-Check Results</div>
              <div style="display: flex; flex-direction: column; gap: 12px; font-size: 13px;">
                <div style="display: flex; justify-content: space-between; padding-bottom: 8px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--steel);">Orders Verified by Colleague:</span>
                  <strong style="color: #79D2B7;">${dailyOrders} / ${dailyOrders} (100%)</strong>
                </div>
                <div style="display: flex; justify-content: space-between; padding-bottom: 8px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--steel);">Peer Verification Partner:</span>
                  <strong style="color: var(--white);">Ananya Sharma (Senior Keyer)</strong>
                </div>
                <div style="display: flex; justify-content: space-between; padding-bottom: 8px; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--steel);">Double-Check Compliance:</span>
                  <strong style="color: #79D2B7;">Full Compliance (No unverified jobs)</strong>
                </div>
                <div style="display: flex; justify-content: space-between;">
                  <span style="color: var(--steel);">Australian Cutoff Dispatch:</span>
                  <strong style="color: var(--gold);">Ready for 15:00 Melbourne Transfer</strong>
                </div>
              </div>
            </div>
          </div>
        `;
      } else if (currentEmpTab === 'quality') {
        tabBodyContent = `
          <div class="card" style="margin-bottom: 20px;">
            <div class="card-title">Quality Assurance & Learning Record</div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 16px;">
              <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
                <div style="font-size: 11px; color: var(--steel);">First-Pass Accuracy</div>
                <div style="font-size: 20px; font-weight: 600; color: #79D2B7; font-family: var(--font-mono);">${empAcc}</div>
                <div style="font-size: 11px; color: var(--steel-dim);">90-Day Rolling Average</div>
              </div>
              <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
                <div style="font-size: 11px; color: var(--steel);">Zero-Blame Cases Logged</div>
                <div style="font-size: 20px; font-weight: 600; color: var(--porcelain); font-family: var(--font-mono);">1 Case</div>
                <div style="font-size: 11px; color: var(--steel-dim);">Tooling angle variance</div>
              </div>
              <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
                <div style="font-size: 11px; color: var(--steel);">Resolution Turnaround</div>
                <div style="font-size: 20px; font-weight: 600; color: var(--gold); font-family: var(--font-mono);">45 Minutes</div>
                <div style="font-size: 11px; color: var(--steel-dim);">Drawing Rev B Published</div>
              </div>
            </div>
            <div style="font-size: 12px; color: var(--steel-dim); line-height: 1.5; padding: 10px; background: var(--midnight); border-radius: 4px;">
              *Zero-Blame Principle: When an error or resupply occurs, PULSE documents drawing markups and tooling clearances as team learning opportunities, never individual blame.
            </div>
          </div>
        `;
      } else if (currentEmpTab === 'growth') {
        tabBodyContent = `
          <!-- Skills Training & Development -->
          <div class="card" style="margin-bottom: 20px;">
            <div class="card-title">
              <span>7 Sheetmetal Skill Levels</span>
              <span style="font-size: 11px; color: var(--gold); font-family: var(--font-mono);">L1: Learning • L2: Independent • L3: Experienced • L4: Trainer</span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px;">
              <div style="display: flex; justify-content: space-between; padding: 8px 12px; background: var(--midnight); border-radius: 4px;">
                <span style="color: var(--porcelain);">1. Order Keying:</span>
                <strong style="color: #79D2B7; font-family: var(--font-mono);">Level 4: Can Train Others</strong>
              </div>
              <div style="display: flex; justify-content: space-between; padding: 8px 12px; background: var(--midnight); border-radius: 4px;">
                <span style="color: var(--porcelain);">2. Flashing Detailing:</span>
                <strong style="color: #79D2B7; font-family: var(--font-mono);">Level 4: Can Train Others</strong>
              </div>
              <div style="display: flex; justify-content: space-between; padding: 8px 12px; background: var(--midnight); border-radius: 4px;">
                <span style="color: var(--porcelain);">3. Bits & Accessories:</span>
                <strong style="color: var(--gold); font-family: var(--font-mono);">Level 3: Experienced</strong>
              </div>
              <div style="display: flex; justify-content: space-between; padding: 8px 12px; background: var(--midnight); border-radius: 4px;">
                <span style="color: var(--porcelain);">4. Double-Checking:</span>
                <strong style="color: #79D2B7; font-family: var(--font-mono);">Level 4: Can Train Others</strong>
              </div>
              <div style="display: flex; justify-content: space-between; padding: 8px 12px; background: var(--midnight); border-radius: 4px;">
                <span style="color: var(--porcelain);">5. Quality Review:</span>
                <strong style="color: var(--gold); font-family: var(--font-mono);">Level 3: Experienced</strong>
              </div>
              <div style="display: flex; justify-content: space-between; padding: 8px 12px; background: var(--midnight); border-radius: 4px;">
                <span style="color: var(--porcelain);">6. Customer RFI Handling:</span>
                <strong style="color: var(--steel); font-family: var(--font-mono);">Level 2: Can Work Independently</strong>
              </div>
            </div>
          </div>

          <!-- Confidential Leadership Mentorship Notes -->
          <div class="card" style="position: relative; overflow: hidden;">
            <div class="card-title">
              <span>Confidential Leadership Mentorship Notes</span>
              <span class="status-badge ${isRestrictedRole ? 'alert' : 'verified'}">
                ${isRestrictedRole ? 'Privacy Protected (Locked)' : 'Authorized Access'}
              </span>
            </div>

            ${isRestrictedRole ? `
              <div style="padding: 24px; text-align: center; background: rgba(16, 25, 35, 0.9); border-radius: 6px; border: 1px dashed var(--slate-border);">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="2" style="margin-bottom: 8px;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <div style="font-size: 14px; font-weight: 600; color: var(--white); margin-bottom: 4px;">
                  Restricted Confidential Section
                </div>
                <div style="font-size: 12px; color: var(--steel); max-width: 480px; margin: 0 auto;">
                  Individual supervisory mentorship notes, private development milestones, and salary reviews are restricted to Team Leaders, Management, and Operational Strategists.
                </div>
              </div>
            ` : `
              <div style="display: flex; flex-direction: column; gap: 12px; font-size: 13px;">
                <div style="padding: 12px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
                  <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <strong style="color: var(--white);">Supervisory Coaching Review (November 2026)</strong>
                    <span style="color: var(--steel-dim); font-family: var(--font-mono);">Supervisor: Priya Nair</span>
                  </div>
                  <div style="color: var(--steel); line-height: 1.5;">
                    ${emp.name} continues to show outstanding dedication. Mentoring junior detailers on curved flashings with patience. Recommended for supervisory relief training during Shift A peak cycles.
                  </div>
                </div>
              </div>
            `}
          </div>
        `;
      }

      container.innerHTML = headerCard + tabNavHtml + tabBodyContent;
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
          ${handovers.map(h => {
            const hId = h.id || 'HND-101';
            const outShift = h.fromShift || h.outgoingShift || 'Shift A (Day)';
            const inShift = h.toShift || h.incomingShift || 'Shift B (Afternoon)';
            const outTL = h.outgoingLead || h.outgoingTL || 'Priya Nair';
            const inTL = h.incomingLead || h.incomingTL || 'Rajesh Kumar';
            const isAck = h.acknowledged === true || h.status === 'Acknowledged';
            const ackAt = h.acknowledgedAt || '14:28 IST';
            const timeStr = h.timestamp || 'Today 14:15 IST';
            const urgent = h.urgentJobs || 'Standard batch orders in queue.';
            const machine = h.machineryNotes || 'All machinery operational.';
            const staffing = h.staffingNotes || 'All workstations attended.';

            return `
              <div class="card" style="border: 1px solid ${isAck ? 'var(--slate-border)' : 'var(--gold-border)'};">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid var(--slate-border);">
                  <div style="display: flex; align-items: center; gap: 12px;">
                    <span class="status-badge ${isAck ? 'verified' : 'warning'}">
                      ${isAck ? 'Acknowledged & Closed' : 'Pending Incoming Acknowledgment'}
                    </span>
                    <strong style="color: var(--white); font-size: 16px;">${outShift} → ${inShift} Transfer Dossier</strong>
                  </div>
                  <div style="font-family: var(--font-mono); font-size: 12px; color: var(--gold);">
                    Logged: ${timeStr}
                  </div>
                </div>

                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin-bottom: 16px; font-size: 13px;">
                  <div>
                    <div style="color: var(--steel); font-size: 11px; text-transform: uppercase;">Outgoing Team Leader</div>
                    <strong style="color: var(--white);">${outTL}</strong>
                  </div>
                  <div>
                    <div style="color: var(--steel); font-size: 11px; text-transform: uppercase;">Incoming Team Leader</div>
                    <strong style="color: var(--white);">${inTL}</strong>
                  </div>
                  <div>
                    <div style="color: var(--steel); font-size: 11px; text-transform: uppercase;">Status</div>
                    <strong style="color: ${isAck ? '#79D2B7' : 'var(--gold)'};">
                      ${isAck ? `Acknowledged at ${ackAt}` : 'Awaiting Sign-Off'}
                    </strong>
                  </div>
                </div>

                <div style="display: flex; flex-direction: column; gap: 10px; font-size: 13px; margin-bottom: 18px;">
                  <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
                    <strong style="color: var(--gold);">Urgent Melbourne Orders:</strong> ${urgent}
                  </div>
                  <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
                    <strong style="color: var(--porcelain);">Machinery & Tooling:</strong> ${machine}
                  </div>
                  <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
                    <strong style="color: var(--steel);">Staffing Observations:</strong> ${staffing}
                  </div>
                </div>

                ${!isAck ? `
                  <div style="display: flex; justify-content: flex-end;">
                    <button class="btn btn-gold btn-sm" onclick="acknowledgeHandover('${hId}')">
                      Acknowledge & Accept Handover
                    </button>
                  </div>
                ` : ''}
              </div>
            `;
          }).join('')}
        </div>
      `;
    }

    function acknowledgeHandover(handoverId) {
      const h = (appState.handovers || []).find(item => item.id === handoverId);
      if (h) {
        h.acknowledged = true;
        h.status = 'Acknowledged';
        const now = new Date();
        h.acknowledgedAt = `${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')} IST`;
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
        fromShift: 'Shift A (Day)',
        incomingShift: 'Shift B (Afternoon)',
        toShift: 'Shift B (Afternoon)',
        outgoingTL: 'Priya Nair',
        outgoingLead: 'Priya Nair',
        incomingTL: 'Rajesh Kumar',
        incomingLead: 'Rajesh Kumar',
        timestamp: 'Monday, 23 Nov 2026 • 14:15 IST',
        urgentJobs: urgentJobs || 'Standard batch orders in queue.',
        machineryNotes: machinery || 'All machines operating within normal parameters.',
        staffingNotes: staffing || 'Full complement clocked in.',
        acknowledged: false,
        status: 'Pending',
        acknowledgedAt: ''
      };

      appState.handovers.unshift(newH);
      closeModal('modal-create-handover');
      renderHandoverView();
      showToast('New digital handover dossier published.');
    }

    /* ==========================================================================
       5. DAILY OPERATIONS SUMMARY RENDERER
       ========================================================================== */
    function renderShiftReportView() {
      const container = document.getElementById('shift-report-content-container');
      if (!container) return;

      container.innerHTML = `
        <div class="card" style="padding: 32px; background: var(--slate-card); border: 1px solid var(--slate-border-light);">
          <!-- Header -->
          <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 20px; border-bottom: 2px solid var(--gold); margin-bottom: 24px;">
            <div>
              <div style="font-family: var(--font-serif); font-size: 22px; font-weight: 600; color: var(--white); margin-bottom: 4px;">
                DESIGN SHEETMETAL • DAILY OPERATIONS SUMMARY
              </div>
              <div style="font-size: 13px; color: var(--steel);">
                Operational Facility: India Operations • Shift Cycle: Shift A (06:00 — 14:30 IST)
              </div>
            </div>
            <div style="text-align: right; font-family: var(--font-mono); font-size: 12px; color: var(--gold);">
              <div>DATE: Monday, 23 November 2026</div>
              <div>CLASSIFICATION: EXECUTIVE OPERATIONS</div>
            </div>
          </div>

          <!-- Summary Metric Ribbon -->
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px;">
            <div style="padding: 14px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Scheduled Staff</div>
              <div style="font-size: 24px; font-weight: 600; color: var(--white); font-family: var(--font-serif);">40</div>
              <div style="font-size: 11px; color: #79D2B7;">36 Present (2 Late) • 3 Leave • 1 Absent</div>
            </div>
            <div style="padding: 14px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Orders Completed</div>
              <div style="font-size: 24px; font-weight: 600; color: var(--gold); font-family: var(--font-serif);">142 Orders</div>
              <div style="font-size: 11px; color: var(--steel-dim);">1,840m Flashings • 5,120 Bits</div>
            </div>
            <div style="padding: 14px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Double-Check Done</div>
              <div style="font-size: 24px; font-weight: 600; color: #79D2B7; font-family: var(--font-serif);">97.2%</div>
              <div style="font-size: 11px; color: var(--steel-dim);">138 of 142 Orders Verified</div>
            </div>
            <div style="padding: 14px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 6px;">
              <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">Quality Cases</div>
              <div style="font-size: 24px; font-weight: 600; color: var(--amber); font-family: var(--font-serif);">1 Case</div>
              <div style="font-size: 11px; color: var(--steel-dim);">Tooling angle (Rev B corrected)</div>
            </div>
          </div>

          <!-- Section: Production Breakdown Table -->
          <div style="margin-bottom: 24px;">
            <h4 style="font-size: 14px; color: var(--white); margin-bottom: 10px;">1. Operational Output by Detailing Cell</h4>
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
                    <td>9 / 10</td>
                    <td>38</td>
                    <td>450m</td>
                    <td>36 (95%)</td>
                    <td><span style="color: #79D2B7;">98.0%</span></td>
                  </tr>
                  <tr>
                    <td><strong>Team Delta</strong></td>
                    <td>Special Structural Assemblies</td>
                    <td>8 / 10</td>
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
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; padding-top: 20px; border-top: 1px solid var(--slate-border); font-size: 12px;">
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
              <div style="color: var(--steel); font-family: var(--font-mono); font-size: 11px;">Validated for Melbourne Transfer</div>
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
        "Shift,Date,Team,Scheduled,Present,OrdersKeyed,FlashingsMeters,Bits,DoubleChecks,FirstPassAccuracy\n" +
        "Shift A,2026-11-23,Team Alpha,10,10,42,680,1850,42,99.1%\n" +
        "Shift A,2026-11-23,Team Beta,10,9,34,410,1120,33,98.4%\n" +
        "Shift A,2026-11-23,Team Gamma,10,9,38,450,1250,36,98.0%\n" +
        "Shift A,2026-11-23,Team Delta,10,8,28,300,900,27,98.8%\n";

      const encodedUri = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", "PULSE_Daily_Operations_Summary_2026-11-23.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      showToast("Daily Summary CSV exported successfully.");
    }

    /* ==========================================================================
       6. ISSUES & ALERTS (MANAGEMENT EXCEPTIONS) RENDERER
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
      const a = (appState.alerts || []).find(item => item.id === alertId);
      if (a) {
        a.status = 'Acknowledged';
        renderExceptionsView();
        updateBadgeCounts();
        showToast(`Alert #${alertId} acknowledged.`);
      }
    }

    function openResolveAlertModal(alertId) {
      const a = (appState.alerts || []).find(item => item.id === alertId);
      if (!a) return;
      document.getElementById('resolve-alert-id').value = a.id;
      document.getElementById('resolve-alert-desc').textContent = `${a.type}: ${a.message}`;
      openModal('modal-resolve-alert');
    }

    function submitResolveAlert() {
      const alertId = document.getElementById('resolve-alert-id').value;
      const notes = document.getElementById('resolve-alert-notes').value;
      const a = (appState.alerts || []).find(item => item.id === alertId);
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
       7. STAFF AVAILABILITY (WORKFORCE CAPACITY) RENDERER
       ========================================================================== */
    function renderCapacityView() {
      const container = document.getElementById('capacity-content-container');
      if (!container) return;

      const schedule = [
        { day: 'Mon 23 Nov (Today)', count: '36 / 40', status: 'Optimal (36 Present)', isToday: true, isRisk: false },
        { day: 'Tue 24 Nov', count: '37 / 40', status: 'Optimal Capacity', isToday: false, isRisk: false },
        { day: 'Wed 25 Nov', count: '36 / 40', status: 'Optimal Capacity', isToday: false, isRisk: false },
        { day: 'Thu 26 Nov', count: '35 / 40', status: 'Normal Operations', isToday: false, isRisk: false },
        { day: 'Fri 27 Nov (Notice)', count: '31 / 40', status: 'Team Gamma Notice', isToday: false, isRisk: true },
        { day: 'Sat 28 Nov', count: '38 / 40', status: 'Weekend Shift', isToday: false, isRisk: false },
        { day: 'Sun 29 Nov', count: '36 / 40', status: 'Weekend Shift', isToday: false, isRisk: false }
      ];

      container.innerHTML = `
        <div class="card" style="margin-bottom: 24px;">
          <div class="card-title">
            <span>7-Day Forward Staff Availability (23 Nov – 29 Nov 2026)</span>
            <span class="status-badge warning">Minimum Staffing Threshold: 8 Operators / Team</span>
          </div>
          <p style="font-size: 13px; color: var(--steel); margin-bottom: 18px;">
            Visual schedule showing expected attendance across all four detailing cells. Clearly identifies dates where staffing requires backup operators.
          </p>

          <div style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 10px; margin-bottom: 24px;">
            ${schedule.map(d => `
              <div style="padding: 12px; background: ${d.isToday ? 'rgba(198, 166, 117, 0.12)' : d.isRisk ? 'rgba(217, 83, 79, 0.12)' : 'var(--midnight)'}; border: 1px solid ${d.isToday ? 'var(--gold)' : d.isRisk ? 'var(--crimson)' : 'var(--slate-border)'}; border-radius: 6px; text-align: center;">
                <div style="font-family: var(--font-mono); font-size: 11px; color: ${d.isToday ? 'var(--gold)' : d.isRisk ? '#FFA5A2' : 'var(--steel)'}; margin-bottom: 4px;">
                  ${d.day}
                </div>
                <div style="font-size: 18px; font-weight: 600; color: ${d.isRisk ? '#FFA5A2' : 'var(--white)'}; font-family: var(--font-serif);">
                  ${d.count}
                </div>
                <div style="font-size: 10px; color: ${d.isRisk ? '#FFA5A2' : '#79D2B7'};">
                  ${d.status}
                </div>
              </div>
            `).join('')}
          </div>

          <!-- Plain Language Backup Suggestion Card -->
          <div style="padding: 16px; background: rgba(198, 166, 117, 0.08); border: 1px solid var(--gold-border); border-radius: 6px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
            <div>
              <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 4px;">
                <span class="pulse-dot"></span>
                <strong style="color: var(--white); font-size: 13px;">Upcoming Staffing Notice: Friday, 27 November 2026</strong>
              </div>
              <div style="font-size: 12px; color: var(--porcelain); line-height: 1.5; max-width: 650px;">
                Team Gamma may have fewer employees than required on Friday, 27 November (31 of 40 available due to approved annual leave). Recommended backup: <strong>Vikram Singh (EMP-102)</strong> from Team Alpha is certified in Rainwater Detailing.
              </div>
            </div>
            <button class="btn btn-gold btn-sm" onclick="showToast('Backup reassignment scheduled for Friday, 27 November.')">
              Confirm Backup Plan
            </button>
          </div>
        </div>
      `;
    }

    /* ==========================================================================
       8. SKILLS & TRAINING MATRIX RENDERER
       ========================================================================== */
    function renderSkillsMatrixView() {
      const container = document.getElementById('skills-content-container');
      if (!container) return;

      const skills = [
        { id: 'keying', name: 'Order Keying', desc: 'Accurately entering customer specifications and sheet dimensions into the order system.' },
        { id: 'flashings', name: 'Flashing Detailing', desc: 'Calculating folds, hems, angles, and taper lengths for roof flashings.' },
        { id: 'bits', name: 'Bits & Accessories', desc: 'Detailing clips, brackets, stop-ends, and specialized rainwater accessories.' },
        { id: 'checking', name: 'Double-Checking', desc: 'Rigorously reviewing colleague drawings against original customer markups.' },
        { id: 'quality', name: 'Quality Review', desc: 'Verifying bend tolerances, sheet thickness gauges, and finish coatings.' },
        { id: 'rfi', name: 'Customer RFI', desc: 'Drafting clear technical clarification questions for Australian builders.' },
        { id: 'drawings', name: 'Specialized Drawings', desc: 'Creating complex 3D CAD unfoldings for structural architectural panels.' }
      ];

      const emps = (appState.employees || []).slice(0, 15);

      container.innerHTML = `
        <!-- Plain Language Explanation Card -->
        <div class="card" style="margin-bottom: 20px;">
          <div class="card-title">7 Core Sheetmetal Skills & 4 Experience Levels</div>
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-top: 12px;">
            <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
              <strong style="color: var(--steel-dim); font-size: 12px;">Level 1: Learning</strong>
              <p style="font-size: 11px; color: var(--steel); margin: 4px 0 0 0;">Working under senior supervision.</p>
            </div>
            <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
              <strong style="color: var(--steel); font-size: 12px;">Level 2: Independent</strong>
              <p style="font-size: 11px; color: var(--steel); margin: 4px 0 0 0;">Handles standard jobs independently.</p>
            </div>
            <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
              <strong style="color: var(--gold); font-size: 12px;">Level 3: Experienced</strong>
              <p style="font-size: 11px; color: var(--steel); margin: 4px 0 0 0;">Handles complex profiles and custom folds.</p>
            </div>
            <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
              <strong style="color: #79D2B7; font-size: 12px;">Level 4: Trainer</strong>
              <p style="font-size: 11px; color: var(--steel); margin: 4px 0 0 0;">Can train others and double-check orders.</p>
            </div>
          </div>
        </div>

        <div class="card" style="margin-bottom: 24px;">
          <div class="card-title">
            <span>Team Skills Matrix</span>
            <span style="font-size: 12px; color: var(--steel);">Showing 15 Sample Operators Across Teams</span>
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
                      return `<td><span style="font-family: var(--font-mono); font-weight: 600; color: ${color};">Level ${level}</span></td>`;
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
       9. REPORTS & EXPORTS (REPORT BUILDER) RENDERER
       ========================================================================== */
    function renderReportBuilderView() {
      const container = document.getElementById('report-builder-content-container');
      if (!container) return;

      container.innerHTML = `
        <div class="card" style="margin-bottom: 24px;">
          <div class="card-title">
            <span>Create a Report</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 18px;">
            <div class="form-group">
              <label class="form-label">Choose Team</label>
              <select class="form-select" id="rep-filter-team">
                <option value="ALL">All Teams (Alpha, Beta, Gamma, Delta)</option>
                <option value="Team Alpha">Team Alpha (Flashings & Trims)</option>
                <option value="Team Beta">Team Beta (Cladding Panels)</option>
                <option value="Team Gamma">Team Gamma (Rainwater Goods)</option>
                <option value="Team Delta">Team Delta (Special Assemblies)</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label">Choose Shift</label>
              <select class="form-select" id="rep-filter-shift">
                <option value="ALL">All Shifts (A Day, B Afternoon, C Night)</option>
                <option value="Shift A">Shift A (Day: 06:00 — 14:30 IST)</option>
                <option value="Shift B">Shift B (Afternoon: 14:00 — 22:30 IST)</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label">Select Information</label>
              <select class="form-select" id="rep-filter-metric">
                <option value="ALL">All Operations (Attendance, Output, Quality)</option>
                <option value="ATTENDANCE">Attendance & Hours Only</option>
                <option value="OUTPUT">Orders Completed & Volume</option>
                <option value="QUALITY">Quality Accuracy & Resupplies</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label">Date Range</label>
              <select class="form-select" id="rep-filter-date">
                <option value="TODAY">Monday, 23 November 2026 (Today)</option>
                <option value="WEEK">Last 7 Days</option>
                <option value="MONTH">Full Month (November 2026)</option>
              </select>
            </div>
          </div>
          <div style="display: flex; justify-content: flex-end; gap: 10px;">
            <button class="btn btn-outline btn-sm" onclick="exportCustomReportCSV()">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              Export CSV File
            </button>
            <button class="btn btn-gold btn-sm" onclick="runCustomReport()">
              Generate Report
            </button>
          </div>
        </div>

        <div class="card" id="custom-report-output">
          <div class="card-title">
            <span>Report Results: India Operations Workforce</span>
            <span class="status-badge verified">40 Records Found</span>
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
                  <th>Orders Completed</th>
                  <th>Quality Accuracy</th>
                </tr>
              </thead>
              <tbody>
                ${(appState.employees || []).slice(0, 10).map(e => `
                  <tr>
                    <td><span style="font-family: var(--font-mono); color: var(--gold);">${e.id}</span></td>
                    <td><strong>${e.name}</strong></td>
                    <td>${e.team}</td>
                    <td>${e.shift}</td>
                    <td>${e.hours != null ? e.hours : 7.5}h</td>
                    <td>${(e.dailyTarget && e.dailyTarget.orders) ? e.dailyTarget.orders : 16}</td>
                    <td><span style="color: #79D2B7;">${e.accuracyText || e.accuracy || '99.2%'}</span></td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>
      `;
    }

    function runCustomReport() {
      showToast('Report generated successfully across 40 employee records.');
    }

    function exportCustomReportCSV() {
      const csvContent = "data:text/csv;charset=utf-8," +
        "EmpID,Name,Team,Shift,AttendedHours,OrdersCompleted,QualityAccuracy\n" +
        (appState.employees || []).map(e => `${e.id},${e.name},${e.team},${e.shift},${e.hours != null ? e.hours : 7.5},${(e.dailyTarget && e.dailyTarget.orders) ? e.dailyTarget.orders : 16},${e.accuracyText || e.accuracy || '99.2%'}`).join('\n');

      const encodedUri = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", "PULSE_Custom_Report_2026-11-23.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      showToast("Custom Report CSV exported successfully.");
    }

    /* ==========================================================================
       10. IMPORT DATA (CSV / EXCEL INGESTION) RENDERER
       ========================================================================== */
    function renderImportView() {
      const container = document.getElementById('import-content-container');
      if (!container) return;

      container.innerHTML = `
        <div class="card" style="margin-bottom: 24px;">
          <div class="card-title">
            <span>Import Biometric Attendance or Production CSV</span>
          </div>
          <div style="border: 2px dashed var(--slate-border); border-radius: 8px; padding: 36px; text-align: center; background: var(--midnight); margin-bottom: 20px;">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" style="margin-bottom: 12px;"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
            <div style="font-size: 15px; font-weight: 500; color: var(--white); margin-bottom: 6px;">
              Drop Attendance or Output CSV Here
            </div>
            <div style="font-size: 12px; color: var(--steel); margin-bottom: 16px;">
              Supports standard machine punch files (Employee ID, Timestamp, Event Type, Terminal ID)
            </div>
            <div style="display: flex; justify-content: center; gap: 12px;">
              <input type="file" id="csv-file-input" accept=".csv" style="display: none;" onchange="handleCSVFileSelected(event)" />
              <button class="btn btn-outline btn-sm" onclick="document.getElementById('csv-file-input').click()">
                Select Local CSV File
              </button>
              <button class="btn btn-gold btn-sm" onclick="loadSampleCSVData()">
                Load Sample Machine Data
              </button>
            </div>
          </div>

          <!-- Parsed Rows Preview -->
          <div id="import-preview-container" style="display: none;">
            <div class="card-title">
              <span>Preview Parsed Records (Validation: 5 Passed, 0 Errors)</span>
              <button class="btn btn-gold btn-sm" onclick="executeCSVImport()">
                Import Records into Live System
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
        showToast('Sample attendance records loaded. Click Import to add to live feed.');
      }
    }

    function handleCSVFileSelected(event) {
      const file = event.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(e) {
        const text = e.target.result;
        const lines = text.split('\n').filter(l => l.trim().length > 0);
        parsedImportRows = [];

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
          punchId: `PUN-${Math.floor(1000 + Math.random() * 9000)}`,
          empId: r.empId,
          empName: r.empName,
          timestamp: r.timestamp,
          timeIST: r.timestamp,
          type: r.type,
          device: r.device,
          source: 'Ingested File Import',
          method: 'Ingested File Import',
          status: 'Verified'
        });
      });

      renderPunchTable();
      document.getElementById('import-preview-container').style.display = 'none';
      showToast(`${parsedImportRows.length} records successfully imported into live attendance feed.`);
      parsedImportRows = [];
    }

    /* ==========================================================================
       11. PERFORMANCE OVERVIEW (FORMERLY OPERATIONS DASHBOARD)
       ========================================================================== */
    function renderDashboard() {
      const container = document.getElementById('dashboard-content-container');
      if (!container) return;
      container.innerHTML = `
        <div class="metric-grid">
          <div class="metric-card">
            <div class="metric-label">Staff Present Today</div>
            <div class="metric-value">36 / 40</div>
            <div class="metric-context" style="color: var(--emerald);">90% Floor Presence (3 Leave, 1 Absent)</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Orders Keyed</div>
            <div class="metric-value">142 Orders</div>
            <div class="metric-context" style="color: var(--gold);">Target: 135 (+5.2% ahead)</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Double-Check Results</div>
            <div class="metric-value">97.2%</div>
            <div class="metric-context" style="color: #79D2B7;">138 Orders Formally Peer Verified</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Quality Accuracy</div>
            <div class="metric-value">98.6%</div>
            <div class="metric-context">First-Pass Manufacturing Fit</div>
          </div>
        </div>
      `;
    }

    /* ==========================================================================
       12. ATTENDANCE REGISTER
       ========================================================================== */
    function renderAttendanceTable() {
      const tbody = document.getElementById('attendance-tbody');
      if (!tbody) return;

      tbody.innerHTML = (appState.employees || []).map(e => `
        <tr>
          <td><span style="font-family: var(--font-mono); color: var(--gold);">${e.id}</span></td>
          <td><strong>${e.name}</strong></td>
          <td>${e.team}</td>
          <td>${e.shift}</td>
          <td><span style="font-family: var(--font-mono);">${e.checkin || (e.lateMinutes > 0 ? '06:18 AM' : '05:54 AM')}</span></td>
          <td><span style="font-family: var(--font-mono);">${e.checkout || (e.status === 'Present' ? 'In Progress' : '14:26 PM')}</span></td>
          <td><span style="font-family: var(--font-mono);">${e.hours != null ? e.hours : 7.5}h</span></td>
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

    /* ==========================================================================
       13. LEAVE REQUESTS
       ========================================================================== */
    function renderLeaveTables() {
      const container = document.getElementById('leave-content-container');
      if (!container) return;

      const leaves = appState.leaveRequests || [];
      const canApprove = (currentRole === 'MANAGEMENT' || currentRole === 'SUPER_ADMIN' || currentRole === 'PRESENTER' || currentRole === 'TEAM_LEADER');

      container.innerHTML = `
        <div class="data-table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>Request ID</th>
                <th>Employee Name</th>
                <th>Leave Type</th>
                <th>Requested Date</th>
                <th>Reason / Purpose</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              ${leaves.map(l => {
                let reasonDisplay = l.reason;
                if (currentRole === 'EMPLOYEE') {
                  if (l.empId !== 'EMP-101') {
                    reasonDisplay = '<span style="color: var(--steel-dim); font-style: italic;">Confidential (HR Protected)</span>';
                  }
                } else if (currentRole === 'TEAM_LEADER') {
                  if (l.team && !l.team.includes('Team Alpha')) {
                    reasonDisplay = '<span style="color: var(--steel-dim); font-style: italic;">Confidential (Other Team)</span>';
                  }
                }

                return `
                  <tr>
                    <td><strong style="color: var(--steel); font-family: var(--font-mono);">${l.id}</strong></td>
                    <td><strong>${l.empName}</strong> <span style="font-size: 11px; color: var(--steel-dim); font-family: var(--font-mono);">(${l.empId})</span></td>
                    <td>${l.type}</td>
                    <td style="font-family: var(--font-mono);">${l.dates || l.date || '2026-11-23'}</td>
                    <td>${reasonDisplay}</td>
                    <td><span class="status-badge ${l.status === 'Approved' ? 'verified' : 'warning'}">${l.status}</span></td>
                    <td>
                      ${l.status === 'Pending' ? (
                        canApprove ? `<button class="btn btn-gold btn-sm" onclick="approveLeave('${l.id}')">Approve</button>` :
                        `<span style="color: var(--steel-dim); font-size: 11px;">Pending Approval</span>`
                      ) : '<span style="color: #79D2B7; font-size: 11px;">✓ Approved</span>'}
                    </td>
                  </tr>
                `;
              }).join('')}
            </tbody>
          </table>
        </div>
      `;
    }

    function approveLeave(leaveId) {
      const l = (appState.leaveRequests || []).find(item => item.id === leaveId);
      if (l) {
        l.status = 'Approved';
        renderLeaveTables();
        updateBadgeCounts();
        showToast(`Leave request #${leaveId} approved.`);
      }
    }

    function submitLeaveRequest() {
      const empId = document.getElementById('leave-emp-select').value;
      const type = document.getElementById('leave-type-select').value;
      const date = document.getElementById('leave-date-input').value;
      const reason = document.getElementById('leave-reason-input').value;

      const emp = (appState.employees || []).find(e => e.id === empId);
      const newLeave = {
        id: `LR-${Math.floor(100 + Math.random() * 900)}`,
        empId: empId,
        empName: emp ? emp.name : 'Unknown',
        type: type,
        date: date || '2026-11-24',
        dates: date || '2026-11-24',
        days: 1,
        reason: reason || 'Personal Leave',
        status: 'Pending'
      };

      appState.leaveRequests.unshift(newLeave);
      closeModal('modal-apply-leave');
      renderLeaveTables();
      updateBadgeCounts();
      showToast('Leave request submitted successfully.');
    }

    /* ==========================================================================
       14. DAILY WORK REPORT (PRODUCTION ENTRY & FLOOR LOG)
       ========================================================================== */
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
                <th>Orders Completed</th>
                <th>Flashings (metres)</th>
                <th>Bits & Parts</th>
                <th>Double Checks</th>
                <th>First-Pass Accuracy</th>
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
                  <td><span style="color: #79D2B7;">${r.accuracy || '99.0%'}</span></td>
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
        accuracy: '99.1%'
      };

      appState.productionRecords.unshift(newRecord);
      closeModal('modal-production-entry');
      renderProductionTable();
      showToast(`Work recorded for ${team} (${orders} orders, ${flashings}m flashings).`);
    }

    /* ==========================================================================
       15. ERRORS & RESUPPLIES (ZERO-BLAME RCA)
       ========================================================================== */
    function renderQualityCases() {
      const container = document.getElementById('quality-content-container');
      if (!container) return;

      const cases = appState.qualityCases || [];
      container.innerHTML = `
        <div style="display: flex; flex-direction: column; gap: 16px;">
          ${cases.map(c => {
            const caseId = c.id || 'QC-084';
            const problem = c.problem || c.issue || 'Tooling angle variance on radius flashing';
            const orderRef = c.orderRef || c.orderNo || 'DSM-MEL-8841';
            const client = c.client || c.customer || 'ProBuild Melbourne';
            const spec = c.spec || '0.9mm Colorbond Monument Flashing';
            const reported = c.jobDate || c.reportedDate || '23 Nov 2026';
            const investigator = c.investigator || 'Manoj Tiwari (Quality Lead)';
            const rootCause = c.rootCause || 'Drawing markup did not account for 3mm press-brake springback on thick gauge.';
            const cost = c.confirmedCost || '$185 AUD';
            const action = c.preventiveAction || c.action || 'Updated folding template library to automatically compensate for gauge springback.';
            const status = c.status || 'Action Taken';

            return `
              <div class="card" style="border-left: 4px solid ${status === 'Closed' || status === 'Resolved' ? 'var(--emerald)' : 'var(--amber)'};">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px solid var(--slate-border);">
                  <div>
                    <div style="display: flex; align-items: center; gap: 10px;">
                      <strong style="color: var(--white); font-size: 15px;">${caseId}: ${problem}</strong>
                      <span class="status-badge ${status === 'Closed' || status === 'Resolved' ? 'verified' : 'warning'}">${status}</span>
                    </div>
                    <div style="font-size: 12px; color: var(--steel); margin-top: 4px;">
                      Order: <strong>${orderRef}</strong> • Client: <strong>${client}</strong> • Spec: <strong>${spec}</strong>
                    </div>
                  </div>
                  <div style="text-align: right; font-family: var(--font-mono); font-size: 11px; color: var(--gold);">
                    Reported: ${reported}
                  </div>
                </div>

                <!-- Question and Answer Diagnostic Format -->
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; font-size: 13px; margin-bottom: 12px;">
                  <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
                    <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">1. Root Cause Analysis</div>
                    <div style="color: var(--porcelain); margin-top: 4px; line-height: 1.5;">${rootCause}</div>
                    <div style="font-size: 11px; color: var(--steel-dim); margin-top: 4px;">Investigator: ${investigator}</div>
                  </div>
                  <div style="padding: 10px; background: var(--midnight); border: 1px solid var(--slate-border); border-radius: 4px;">
                    <div style="font-size: 11px; color: var(--steel); text-transform: uppercase;">2. Preventive Action (Zero-Blame Learning)</div>
                    <div style="color: #79D2B7; margin-top: 4px; line-height: 1.5;">${action}</div>
                    <div style="font-size: 11px; color: var(--gold); margin-top: 4px;">Cost: ${cost} (absorbed via drawing fix)</div>
                  </div>
                </div>

                <div style="display: flex; justify-content: flex-end; align-items: center; gap: 10px; padding-top: 10px; border-top: 1px solid var(--slate-border);">
                  ${status !== 'Closed' && status !== 'Resolved' ? `
                    <button class="btn btn-gold btn-sm" onclick="openResolveQualityModal('${caseId}')">Review & Close Case</button>
                  ` : `
                    <span style="font-size: 11px; color: #79D2B7; font-family: var(--font-mono);">✓ Preventive Action Implemented • Case Closed</span>
                  `}
                </div>
              </div>
            `;
          }).join('')}
        </div>
      `;
    }

    function openResolveQualityModal(caseId) {
      const qc = (appState.qualityCases || []).find(q => q.id === caseId);
      if (!qc) return;
      document.getElementById('resolve-quality-id').value = qc.id;
      document.getElementById('resolve-quality-desc').textContent = `${qc.id}: ${qc.problem || qc.issue || 'Drawing variance'} (${qc.orderRef || qc.orderNo})`;
      document.getElementById('resolve-quality-action').value = qc.preventiveAction || 'Updated bending allowance table and published revised SOP.';
      openModal('modal-resolve-quality');
    }

    function submitResolveQuality() {
      const caseId = document.getElementById('resolve-quality-id').value;
      const actionNote = document.getElementById('resolve-quality-action').value;
      const qc = (appState.qualityCases || []).find(q => q.id === caseId);
      if (qc) {
        qc.status = 'Closed';
        if (actionNote) qc.preventiveAction = actionNote;
        closeModal('modal-resolve-quality');
        renderQualityCases();
        renderCommandCentre();
        updateBadgeCounts();
        showToast(`Quality Case #${caseId} marked Closed. Preventive action committed to operational record.`);
      }
    }

    /* ==========================================================================
       16. EMPLOYEE RECOGNITION (AWARDS)
       ========================================================================== */
    function renderAwards() {
      const container = document.getElementById('recognition-content-container');
      if (!container) return;

      const awards = appState.awards || [];
      container.innerHTML = `
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
          ${awards.map(a => {
            const name = a.empName || a.name || 'Team Colleague';
            const team = a.team || 'India Operations';
            const cat = a.category || 'Quality Excellence';
            const citation = a.citation || a.achievement || 'Demonstrated outstanding dedication.';
            const nomBy = a.nominatedBy || 'Peer Colleague';

            return `
              <div class="card" style="border-top: 3px solid var(--gold);">
                <div style="font-family: var(--font-mono); font-size: 11px; color: var(--gold); margin-bottom: 6px;">${cat}</div>
                <h3 style="font-size: 17px; color: var(--white); margin-bottom: 4px;">${name}</h3>
                <div style="font-size: 12px; color: var(--steel); margin-bottom: 12px;">${team} • Nominated by ${nomBy}</div>
                <p style="font-size: 13px; color: var(--porcelain); line-height: 1.6;">"${citation}"</p>
              </div>
            `;
          }).join('')}
        </div>
      `;
    }

    function submitNomination() {
      const empId = document.getElementById('nominate-emp-select').value;
      const category = document.getElementById('nominate-category').value;
      const citation = document.getElementById('nominate-citation').value;

      const emp = (appState.employees || []).find(e => e.id === empId);
      const newAward = {
        id: `AWD-${Math.floor(100 + Math.random() * 900)}`,
        empId: empId,
        empName: emp ? emp.name : 'Unknown',
        name: emp ? emp.name : 'Unknown',
        team: emp ? emp.team : 'India Operations',
        category: category,
        citation: citation || 'Demonstrated outstanding teamwork and craftsmanship.',
        achievement: citation || 'Demonstrated outstanding teamwork and craftsmanship.',
        nominatedBy: currentRole === 'PRESENTER' ? 'Rakshith' : 'Team Colleague'
      };

      appState.awards.unshift(newAward);
      closeModal('modal-nominate');
      renderAwards();
      showToast(`Nomination recorded for ${emp ? emp.name : empId}.`);
    }

    /* ==========================================================================
       17. USERS & PERMISSIONS (ROLES VIEW)
       ========================================================================== */
    function renderRolesView() {
      const container = document.getElementById('roles-content-container');
      if (!container) return;

      container.innerHTML = `
        <div class="card">
          <div class="card-title">User Roles & Access Permissions</div>
          <p style="font-size: 13px; color: var(--steel); margin-bottom: 16px;">
            PULSE includes role-based access control to protect sensitive individual information while ensuring everyone has the operational visibility they need.
          </p>
          <div class="data-table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>User Role</th>
                  <th>Attendance & Clocks</th>
                  <th>Production Logs</th>
                  <th>Errors & Quality RCA</th>
                  <th>Mentorship Notes</th>
                  <th>Export Reports</th>
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
                  <td><strong>Management (David Harrison)</strong></td>
                  <td><span class="status-badge verified">Full Visibility</span></td>
                  <td><span class="status-badge verified">Full Access</span></td>
                  <td><span class="status-badge verified">Full Access</span></td>
                  <td><span class="status-badge verified">Unlocked</span></td>
                  <td><span class="status-badge verified">Enabled</span></td>
                </tr>
                <tr>
                  <td><strong>Team Leader (Priya Nair)</strong></td>
                  <td><span class="status-badge verified">Team Scope</span></td>
                  <td><span class="status-badge verified">Record Work</span></td>
                  <td><span class="status-badge verified">Participate</span></td>
                  <td><span class="status-badge verified">Unlocked</span></td>
                  <td><span class="status-badge verified">Enabled</span></td>
                </tr>
                <tr>
                  <td><strong>Employee (Rohan Sharma)</strong></td>
                  <td><span class="status-badge verified">Personal & Feed</span></td>
                  <td><span class="status-badge verified">Personal View</span></td>
                  <td><span class="status-badge verified">Learning View</span></td>
                  <td><span class="status-badge alert">Protected / Locked</span></td>
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
        setTimeout(() => { if (toast.remove) toast.remove(); }, 300);
      }, 3400);
    }

    /* ==========================================================================
       SCRIPTED DEMONSTRATION ENGINE: "A DAY INSIDE PULSE"
       ========================================================================== */
    let tourCurrentStep = 0;
    let tourAutoPlayTimer = null;
    const TOUR_TOTAL_STEPS = 6;

    const TOUR_STEPS_CONFIG = [
      {
        step: 1,
        title: "Step 1: Employee Arrives (Biometric Punch)",
        badge: "05:54 AM IST • GATE 01",
        desc: "Senior Keying Specialist Rohan Sharma (EMP-101) arrives at Bengaluru operations turnstile. Terminal 01 registers a verified 'Office IN' biometric punch.",
        action: () => tourStep1_EmployeeArrives()
      },
      {
        step: 2,
        title: "Step 2: Attendance Reconciled Live",
        badge: "06:00 AM IST • ATTENDANCE",
        desc: "The digital attendance register reconciles Rohan to 'Present' with 7.8 attended hours. Headcount updates live to 36 Present (2 late), 3 Leave, 1 Absent out of 40 scheduled.",
        action: () => tourStep2_AttendanceRecorded()
      },
      {
        step: 3,
        title: "Step 3: Team Leader Submits Production",
        badge: "11:30 AM IST • PRODUCTION",
        desc: "Priya Nair keys Team Alpha's morning detailing output: 28 purchase orders, 194m flashings, 58 bits, and 27 double-checks verified at 99.4% accuracy.",
        action: () => tourStep3_ProductionSubmitted()
      },
      {
        step: 4,
        title: "Step 4: Quality Issue Reviewed & Resolved",
        badge: "13:15 PM IST • ZERO-BLAME RCA",
        desc: "Manoj Tiwari reviews case QC-084 (tooling springback variance). Preventive CAD folding compensation rule is applied and the case is closed.",
        action: () => tourStep4_QualityReviewed()
      },
      {
        step: 5,
        title: "Step 5: Employee Performance Updates",
        badge: "14:15 PM IST • EMPLOYEE 360°",
        desc: "Rohan Sharma's 360° operational scorecard updates: 28 completed orders, 99.4% accuracy yield, 7.8 attended hours, and compliant attendance timeline.",
        action: () => tourStep5_PerformanceUpdated()
      },
      {
        step: 6,
        title: "Step 6: Daily Management Summary Generated",
        badge: "14:30 PM IST • DAILY SUMMARY",
        desc: "At shift end, PULSE synthesizes attendance, production, and quality into the official Daily Operations Summary, digitally signed and ready for Melbourne leadership.",
        action: () => tourStep6_DailySummaryGenerated()
      }
    ];

    function startScriptedDemo() {
      const storyCont = document.getElementById('story-mode-container');
      if (storyCont && !storyCont.classList.contains('hidden')) {
        switchToProductMode();
      }
      tourCurrentStep = 1;
      executeTourStep(tourCurrentStep);
    }

    function executeTourStep(stepNum) {
      tourCurrentStep = stepNum;
      const config = TOUR_STEPS_CONFIG.find(s => s.step === stepNum);
      if (config) {
        config.action();
        renderTourBanner(config);
      }
    }

    function renderTourBanner(config) {
      const container = document.getElementById('tour-banner-container');
      if (!container) return;

      container.style.display = 'flex';
      container.innerHTML = `
        <div class="tour-header">
          <div style="display: flex; align-items: center; gap: 10px;">
            <span class="tour-step-badge">${config.badge}</span>
            <span style="font-size: 12px; color: var(--steel); font-family: var(--font-mono);">A DAY INSIDE PULSE (${config.step} of ${TOUR_TOTAL_STEPS})</span>
          </div>
          <div class="tour-progress-dots">
            ${TOUR_STEPS_CONFIG.map(s => `
              <div class="tour-dot ${s.step === config.step ? 'active' : s.step < config.step ? 'completed' : ''}" 
                   onclick="executeTourStep(${s.step})" 
                   title="${s.title}"></div>
            `).join('')}
          </div>
        </div>
        <div class="tour-body">
          <div class="tour-text">
            <div class="tour-title">
              <span class="pulse-dot"></span>
              <span>${config.title}</span>
            </div>
            <div class="tour-desc">${config.desc}</div>
          </div>
          <div class="tour-actions">
            ${config.step > 1 ? `
              <button class="btn btn-outline btn-sm" onclick="prevTourStep()">← Previous</button>
            ` : ''}
            ${config.step < TOUR_TOTAL_STEPS ? `
              <button class="btn btn-gold btn-sm" onclick="nextTourStep()">Next Action →</button>
            ` : `
              <button class="btn btn-gold btn-sm" onclick="closeTour()">Finish Tour ✓</button>
            `}
            <button class="btn btn-outline btn-sm" onclick="toggleAutoPlayTour()" id="tour-autoplay-btn">
              ${tourAutoPlayTimer ? 'Pause' : 'Auto-Play'}
            </button>
            <button class="btn btn-outline btn-sm" onclick="closeTour()" title="Close Guided Tour" style="color: var(--steel);">&times;</button>
          </div>
        </div>
      `;
    }

    function nextTourStep() {
      if (tourCurrentStep < TOUR_TOTAL_STEPS) {
        executeTourStep(tourCurrentStep + 1);
      } else {
        closeTour();
      }
    }

    function prevTourStep() {
      if (tourCurrentStep > 1) {
        executeTourStep(tourCurrentStep - 1);
      }
    }

    function toggleAutoPlayTour() {
      if (tourAutoPlayTimer) {
        clearInterval(tourAutoPlayTimer);
        tourAutoPlayTimer = null;
        renderTourBanner(TOUR_STEPS_CONFIG.find(s => s.step === tourCurrentStep));
        showToast('Auto-play paused.');
      } else {
        showToast('Auto-playing A Day Inside PULSE (advancing every 4s)...');
        tourAutoPlayTimer = setInterval(() => {
          if (tourCurrentStep < TOUR_TOTAL_STEPS) {
            nextTourStep();
          } else {
            clearInterval(tourAutoPlayTimer);
            tourAutoPlayTimer = null;
            closeTour();
          }
        }, 4000);
        renderTourBanner(TOUR_STEPS_CONFIG.find(s => s.step === tourCurrentStep));
      }
    }

    function closeTour() {
      if (tourAutoPlayTimer) {
        clearInterval(tourAutoPlayTimer);
        tourAutoPlayTimer = null;
      }
      const container = document.getElementById('tour-banner-container');
      if (container) container.style.display = 'none';
    }

    function tourStep1_EmployeeArrives() {
      onRoleChange('EMPLOYEE');
      switchView('biometric');
      const existing = (appState.biometricPunches || []).find(p => p.id === 'PUN-1099');
      if (!existing) {
        appState.biometricPunches.unshift({
          id: 'PUN-1099',
          punchId: 'PUN-1099',
          empId: 'EMP-101',
          empName: 'Rohan Sharma',
          timestamp: 'Today 05:54 AM IST',
          timeIST: '05:54 AM IST',
          timeAEST: '10:24 AEDT',
          type: 'Office IN',
          device: 'Terminal 01 (Gate 01)',
          source: 'Biometric Scanner',
          method: 'Biometric Scanner',
          status: 'Verified'
        });
      }
      renderPunchTable();
      renderBiometricTimeline('EMP-101');
      showToast('Step 1: Rohan Sharma (EMP-101) punched IN at Turnstile Gate 01 (05:54 AM IST).');
    }

    function tourStep2_AttendanceRecorded() {
      onRoleChange('PRESENTER');
      switchView('attendance');
      const emp = (appState.employees || []).find(e => e.id === 'EMP-101');
      if (emp) {
        emp.status = 'Present';
        emp.checkin = '05:54 AM';
        emp.hours = 7.8;
      }
      renderAttendanceTable();
      renderCommandCentre();
      updateBadgeCounts();
      showToast('Step 2: Attendance reconciled — 36 present, 3 on leave, 1 absent out of 40 scheduled.');
    }

    function tourStep3_ProductionSubmitted() {
      onRoleChange('TEAM_LEADER');
      switchView('production');
      const existing = (appState.productionRecords || []).find(p => p.id === 'PR-901');
      if (!existing) {
        appState.productionRecords.unshift({
          id: 'PR-901',
          team: 'Team Alpha',
          shift: 'Shift A',
          orders: 28,
          flashings: 194,
          bits: 58,
          doubleChecks: 27,
          accuracy: '99.4%'
        });
      }
      renderProductionTable();
      renderCommandCentre();
      showToast('Step 3: Team Leader Priya Nair logged Team Alpha batch: 28 orders, 194m flashings.');
    }

    function tourStep4_QualityReviewed() {
      onRoleChange('PRESENTER');
      switchView('quality');
      const qc = (appState.qualityCases || []).find(q => q.id === 'QC-2026-084' || q.id === 'QC-084');
      if (qc) {
        qc.status = 'Closed';
        qc.preventiveAction = 'Updated folding template library to automatically compensate for gauge springback.';
      }
      renderQualityCases();
      renderCommandCentre();
      updateBadgeCounts();
      showToast('Step 4: Quality Case QC-2026-084 reviewed via zero-blame RCA and marked Closed.');
    }

    function tourStep5_PerformanceUpdated() {
      onRoleChange('PRESENTER');
      switchView('employee360');
      selected360EmpId = 'EMP-101';
      renderEmployee360('EMP-101');
      showToast('Step 5: Rohan Sharma 360° scorecard updated (28 orders, 99.4% accuracy, 7.8h attended).');
    }

    function tourStep6_DailySummaryGenerated() {
      onRoleChange('MANAGEMENT');
      switchView('shift-report');
      renderShiftReportView();
      showToast('Step 6: Shift A Daily Management Summary compiled and ready for Executive Sign-off.');
    }

    function resetDemoData() {
      if (tourAutoPlayTimer) {
        clearInterval(tourAutoPlayTimer);
        tourAutoPlayTimer = null;
      }
      closeTour();
      appState = JSON.parse(JSON.stringify(MASTER_DATA));
      if (typeof window !== 'undefined') window.appState = appState;
      currentRole = 'PRESENTER';
      const roleSel = document.getElementById('role-select');
      if (roleSel) roleSel.value = 'PRESENTER';
      onRoleChange('PRESENTER');
      selected360EmpId = 'EMP-101';
      currentEmpTab = 'overview';
      populateDropdowns();
      renderAllViews();
      showToast('Demo reset: All records restored to pristine initial state.');
    }
"""
