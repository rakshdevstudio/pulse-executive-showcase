# CSS Design System for PULSE Executive Showcase

CSS_CONTENT = """
    :root {
      --midnight: #101923;
      --slate: #182631;
      --slate-card: #1C2D3B;
      --slate-card-hover: #223747;
      --slate-border: rgba(147, 163, 174, 0.22);
      --slate-border-light: rgba(147, 163, 174, 0.35);
      --gold: #C6A675;
      --gold-light: #DFCAAB;
      --gold-dim: rgba(198, 166, 117, 0.16);
      --gold-border: rgba(198, 166, 117, 0.38);
      --porcelain: #F7F6F2;
      --steel: #93A3AE;
      --steel-dim: rgba(147, 163, 174, 0.6);
      --white: #FFFFFF;
      --emerald: #468B77;
      --emerald-dim: rgba(70, 139, 119, 0.18);
      --amber: #C48C49;
      --amber-dim: rgba(196, 140, 73, 0.18);
      --crimson: #D9534F;
      --crimson-dim: rgba(217, 83, 79, 0.18);

      --font-serif: 'Cinzel', 'Playfair Display', 'Bodoni MT', 'Baskerville', 'Georgia', serif;
      --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'SF Pro Text', Roboto, Helvetica, Arial, sans-serif;
      --font-mono: 'SF Mono', 'Roboto Mono', 'Fira Code', 'Courier New', monospace;

      --transition-smooth: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      --transition-scene: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--midnight);
      color: var(--porcelain);
      font-family: var(--font-sans);
      font-size: 14px;
      line-height: 1.5;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    /* Scrollbars */
    ::-webkit-scrollbar { width: 7px; height: 7px; }
    ::-webkit-scrollbar-track { background: var(--midnight); }
    ::-webkit-scrollbar-thumb { background: rgba(147, 163, 174, 0.3); border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--gold); }

    /* DSM Logo Brand Styling */
    .dsm-logo {
      height: 28px;
      width: auto;
      object-fit: contain;
      filter: brightness(1.05) contrast(1.05);
      vertical-align: middle;
    }
    .dsm-logo-lg {
      height: 38px;
      width: auto;
      object-fit: contain;
      filter: drop-shadow(0 2px 8px rgba(0,0,0,0.4));
    }

    /* Common Typography */
    h1, h2, h3, h4 {
      font-family: var(--font-serif);
      font-weight: 500;
      letter-spacing: 0.04em;
    }

    .pulse-dot {
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background-color: var(--gold);
      box-shadow: 0 0 10px var(--gold);
      animation: pulseGlow 2.4s infinite ease-in-out;
    }

    @keyframes pulseGlow {
      0%, 100% { transform: scale(1); opacity: 0.8; box-shadow: 0 0 6px var(--gold); }
      50% { transform: scale(1.3); opacity: 1; box-shadow: 0 0 14px var(--gold); }
    }

    /* =========================================================================
       STORY MODE PRESENTATION STYLES
       ========================================================================= */
    #story-mode-container {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: radial-gradient(circle at 50% 30%, #15222E 0%, var(--midnight) 75%);
      display: flex;
      flex-direction: column;
      z-index: 100;
      overflow: hidden;
    }

    #story-mode-container.hidden {
      display: none !important;
    }

    .story-header {
      height: 64px;
      padding: 0 36px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--slate-border);
      background: rgba(16, 25, 35, 0.85);
      backdrop-filter: blur(12px);
      z-index: 10;
    }

    .brand-mark {
      display: flex;
      align-items: center;
      gap: 12px;
      font-family: var(--font-serif);
      font-size: 18px;
      letter-spacing: 0.22em;
      color: var(--white);
      text-transform: uppercase;
    }

    .brand-subtext {
      font-family: var(--font-mono);
      font-size: 11px;
      letter-spacing: 0.14em;
      color: var(--steel);
      text-transform: uppercase;
      padding-left: 10px;
      border-left: 1px solid var(--slate-border);
    }

    .presenter-pill {
      font-family: var(--font-sans);
      font-size: 11px;
      font-weight: 500;
      color: var(--gold);
      background: var(--gold-dim);
      border: 1px solid var(--gold-border);
      padding: 3px 10px;
      border-radius: 12px;
      letter-spacing: 0.04em;
      margin-left: 8px;
    }

    .story-controls {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .scene-counter {
      font-family: var(--font-mono);
      font-size: 12px;
      letter-spacing: 0.18em;
      color: var(--steel);
    }

    .btn-header {
      background: transparent;
      border: 1px solid var(--slate-border);
      color: var(--porcelain);
      padding: 7px 14px;
      font-size: 12px;
      border-radius: 4px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: var(--transition-smooth);
      font-family: var(--font-sans);
    }
    .btn-header:hover {
      border-color: var(--gold);
      color: var(--gold);
      background: var(--gold-dim);
    }
    .btn-header.primary-action {
      background: var(--gold-dim);
      border-color: var(--gold);
      color: var(--gold-light);
      font-weight: 500;
    }
    .btn-header.primary-action:hover {
      background: var(--gold);
      color: var(--midnight);
    }

    .story-progress-bar {
      height: 3px;
      background: rgba(147, 163, 174, 0.15);
      width: 100%;
      position: relative;
    }
    .story-progress-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--gold), #E8D5B5);
      width: 11.11%;
      transition: width 0.4s ease;
    }

    .story-viewport {
      flex: 1;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 40px 60px;
      overflow-y: auto;
    }

    .scene-slide {
      position: absolute;
      width: 100%;
      max-width: 1280px;
      padding: 0 40px;
      display: none;
      opacity: 0;
      transform: translateY(12px);
      transition: opacity 0.28s ease, transform 0.28s ease;
    }
    .scene-slide.active {
      display: block;
      opacity: 1;
      transform: translateY(0);
      position: relative;
    }

    .story-footer {
      height: 64px;
      padding: 0 40px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--slate-border);
      background: rgba(16, 25, 35, 0.85);
      backdrop-filter: blur(12px);
      z-index: 10;
    }

    .keyboard-hints {
      display: flex;
      align-items: center;
      gap: 16px;
      font-size: 11px;
      color: var(--steel-dim);
      font-family: var(--font-mono);
    }
    .kbd-key {
      padding: 2px 7px;
      background: var(--slate);
      border: 1px solid var(--slate-border);
      border-radius: 3px;
      color: var(--steel);
      margin-right: 4px;
    }

    .story-pagination-dots {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .story-dot {
      width: 28px;
      height: 3px;
      background: rgba(147, 163, 174, 0.25);
      cursor: pointer;
      border-radius: 2px;
      transition: var(--transition-smooth);
    }
    .story-dot.active {
      background: var(--gold);
      width: 44px;
    }

    .nav-arrow-group {
      display: flex;
      gap: 8px;
    }
    .btn-nav-arrow {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: var(--slate);
      border: 1px solid var(--slate-border);
      color: var(--porcelain);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: var(--transition-smooth);
    }
    .btn-nav-arrow:hover {
      border-color: var(--gold);
      color: var(--gold);
      background: var(--gold-dim);
    }
    .btn-nav-arrow:disabled {
      opacity: 0.3;
      cursor: not-allowed;
      border-color: var(--slate-border);
      color: var(--steel);
    }

    /* Scene 1: Opening */
    .scene-1-container {
      max-width: 960px;
      text-align: center;
      position: relative;
      margin: 0 auto;
    }
    .scene-1-pulse-svg {
      width: 100%;
      height: 110px;
      margin-bottom: 24px;
    }
    .pulse-path {
      stroke: var(--gold);
      stroke-width: 2.2;
      fill: none;
      stroke-dasharray: 1000;
      stroke-dashoffset: 1000;
      animation: drawPulse 3.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      filter: drop-shadow(0 0 10px rgba(198, 166, 117, 0.55));
    }
    @keyframes drawPulse {
      0% { stroke-dashoffset: 1000; opacity: 0; }
      20% { opacity: 1; }
      100% { stroke-dashoffset: 0; opacity: 1; }
    }
    .headline-line-1 {
      font-size: 54px;
      line-height: 1.15;
      color: var(--porcelain);
      text-transform: uppercase;
      letter-spacing: 0.12em;
      margin-bottom: 18px;
      opacity: 0;
      transform: translateY(18px);
      animation: fadeUpMask 0.7s 0.1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    .headline-line-2 {
      font-size: 54px;
      line-height: 1.15;
      color: var(--gold);
      text-transform: uppercase;
      letter-spacing: 0.12em;
      margin-bottom: 28px;
      opacity: 0;
      transform: translateY(18px);
      animation: fadeUpMask 0.7s 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    .scene-1-subtext {
      font-size: 19px;
      color: var(--steel);
      max-width: 720px;
      margin: 0 auto 36px;
      line-height: 1.6;
      opacity: 0;
      transform: translateY(14px);
      animation: fadeUpMask 0.7s 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    .scene-1-cta {
      opacity: 0;
      transform: translateY(12px);
      animation: fadeUpMask 0.6s 0.85s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    @keyframes fadeUpMask {
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    /* Scene Specific Hero Styling */
    .scene-title-badge {
      font-family: var(--font-mono);
      font-size: 12px;
      letter-spacing: 0.2em;
      color: var(--gold);
      text-transform: uppercase;
      margin-bottom: 16px;
      display: inline-flex;
      align-items: center;
      gap: 10px;
    }
    .scene-title-badge::before {
      content: '';
      width: 14px;
      height: 1px;
      background: var(--gold);
    }

    .scene-headline {
      font-size: 44px;
      line-height: 1.15;
      margin-bottom: 24px;
      color: var(--white);
      max-width: 980px;
    }
    .scene-headline span.gold-highlight {
      color: var(--gold);
    }

    .scene-narrative {
      font-size: 18px;
      line-height: 1.6;
      color: var(--steel);
      max-width: 840px;
      margin-bottom: 36px;
      font-weight: 300;
    }

    /* =========================================================================
       EXPLORE PRODUCT MODE APP SHELL
       ========================================================================= */
    #product-mode-container {
      display: flex;
      flex-direction: column;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      background: var(--midnight);
    }
    #product-mode-container.hidden {
      display: none !important;
    }

    .app-topbar {
      height: 58px;
      background: #121C26;
      border-bottom: 1px solid var(--slate-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      z-index: 20;
    }

    .topbar-left {
      display: flex;
      align-items: center;
      gap: 18px;
    }

    .topbar-clocks {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 5px 14px;
      background: rgba(24, 38, 49, 0.6);
      border: 1px solid var(--slate-border);
      border-radius: 20px;
      font-family: var(--font-mono);
      font-size: 11px;
    }
    .clock-item {
      display: flex;
      align-items: center;
      gap: 6px;
      color: var(--steel);
    }
    .clock-item strong {
      color: var(--porcelain);
    }

    .topbar-right {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .role-badge-container {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 5px 12px;
      background: var(--slate);
      border: 1px solid var(--slate-border);
      border-radius: 6px;
    }
    .role-label {
      font-size: 11px;
      color: var(--steel);
      text-transform: uppercase;
      font-family: var(--font-mono);
    }
    .role-select {
      background: transparent;
      border: none;
      color: var(--gold-light);
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      outline: none;
    }
    .role-select option {
      background: var(--slate);
      color: var(--porcelain);
    }

    .user-pill {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 4px 10px;
      border-radius: 20px;
      background: rgba(24, 38, 49, 0.4);
      border: 1px solid var(--slate-border);
    }
    .user-avatar {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: var(--gold-dim);
      border: 1px solid var(--gold-border);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--gold);
      font-weight: bold;
    }
    .user-meta {
      display: flex;
      flex-direction: column;
    }
    .user-name {
      font-size: 12px;
      font-weight: 500;
      color: var(--porcelain);
    }
    .user-role-title {
      font-size: 10px;
      color: var(--steel-dim);
      font-family: var(--font-mono);
    }

    .app-workspace {
      display: flex;
      flex: 1;
      height: calc(100vh - 58px);
      overflow: hidden;
    }

    /* Sidebar Navigation */
    .app-sidebar {
      width: 256px;
      background: #131E27;
      border-right: 1px solid var(--slate-border);
      display: flex;
      flex-direction: column;
      padding: 16px 0;
      overflow-y: auto;
      flex-shrink: 0;
    }

    .nav-section-title {
      padding: 10px 20px 4px;
      font-family: var(--font-mono);
      font-size: 10px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--steel-dim);
    }

    .sidebar-menu {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 1px;
    }

    .menu-item {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 9px 20px;
      color: var(--steel);
      cursor: pointer;
      font-size: 13px;
      transition: var(--transition-smooth);
      position: relative;
    }
    .menu-item:hover {
      color: var(--porcelain);
      background: rgba(24, 38, 49, 0.4);
    }
    .menu-item.active {
      color: var(--gold);
      background: rgba(198, 166, 117, 0.08);
      font-weight: 500;
    }
    .menu-item.active::before {
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      width: 3px;
      background: var(--gold);
    }

    .menu-badge {
      margin-left: auto;
      font-family: var(--font-mono);
      font-size: 10px;
      padding: 2px 7px;
      border-radius: 10px;
      background: var(--slate);
      border: 1px solid var(--slate-border);
      color: var(--steel);
    }
    .menu-badge.alert {
      background: var(--crimson-dim);
      border-color: var(--crimson);
      color: #FFA5A2;
    }
    .menu-badge.gold {
      background: var(--gold-dim);
      border-color: var(--gold-border);
      color: var(--gold);
    }

    /* Content Area */
    .app-main {
      flex: 1;
      overflow-y: auto;
      background: var(--midnight);
      position: relative;
    }

    .view-panel {
      display: none;
      padding: 28px 36px 60px;
      max-width: 1480px;
      margin: 0 auto;
    }
    .view-panel.active {
      display: block;
      animation: fadeIn 0.25s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* View Header */
    .view-header {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      margin-bottom: 24px;
      padding-bottom: 18px;
      border-bottom: 1px solid var(--slate-border);
    }
    .view-header-title {
      font-size: 24px;
      color: var(--white);
      margin-bottom: 4px;
    }
    .view-header-subtitle {
      font-size: 13px;
      color: var(--steel);
      max-width: 760px;
    }

    /* Global Cards and Grids */
    .card {
      background: var(--slate-card);
      border: 1px solid var(--slate-border);
      border-radius: 8px;
      padding: 22px;
      transition: var(--transition-smooth);
    }
    .card:hover {
      border-color: var(--slate-border-light);
    }
    .card-title {
      font-size: 15px;
      color: var(--white);
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    /* Metric Card */
    .metric-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }
    .metric-card {
      background: var(--slate-card);
      border: 1px solid var(--slate-border);
      border-radius: 8px;
      padding: 18px;
      position: relative;
    }
    .metric-label {
      font-size: 11px;
      color: var(--steel);
      text-transform: uppercase;
      letter-spacing: 0.1em;
      font-family: var(--font-mono);
      margin-bottom: 6px;
    }
    .metric-value {
      font-size: 30px;
      font-weight: 600;
      color: var(--white);
      font-family: var(--font-serif);
      margin-bottom: 4px;
    }
    .metric-context {
      font-size: 11px;
      color: var(--steel-dim);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Tables */
    .data-table-container {
      background: var(--slate-card);
      border: 1px solid var(--slate-border);
      border-radius: 8px;
      overflow-x: auto;
      margin-bottom: 24px;
    }
    .data-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      text-align: left;
    }
    .data-table th {
      background: #14212C;
      padding: 12px 16px;
      font-family: var(--font-mono);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--steel);
      border-bottom: 1px solid var(--slate-border);
      white-space: nowrap;
    }
    .data-table td {
      padding: 12px 16px;
      border-bottom: 1px solid rgba(147, 163, 174, 0.12);
      color: var(--porcelain);
      vertical-align: middle;
    }
    .data-table tr:hover td {
      background: rgba(24, 38, 49, 0.45);
    }

    /* Status Badges */
    .status-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 3px 10px;
      border-radius: 12px;
      font-size: 11px;
      font-family: var(--font-mono);
      white-space: nowrap;
    }
    .status-badge.verified {
      background: var(--emerald-dim);
      border: 1px solid var(--emerald);
      color: #79D2B7;
    }
    .status-badge.in {
      background: rgba(70, 139, 119, 0.2);
      border: 1px solid var(--emerald);
      color: #8DE0C8;
    }
    .status-badge.out {
      background: rgba(217, 83, 79, 0.2);
      border: 1px solid var(--crimson);
      color: #FF9E9B;
    }
    .status-badge.break {
      background: rgba(196, 140, 73, 0.2);
      border: 1px solid var(--amber);
      color: #FFC98B;
    }
    .status-badge.exception {
      background: rgba(155, 89, 182, 0.2);
      border: 1px solid #9B59B6;
      color: #D2B4DE;
    }
    .status-badge.warning {
      background: var(--amber-dim);
      border: 1px solid var(--amber);
      color: var(--amber);
    }
    .status-badge.alert {
      background: var(--crimson-dim);
      border: 1px solid var(--crimson);
      color: #FF7B76;
    }

    /* Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 8px 16px;
      font-size: 13px;
      border-radius: 4px;
      cursor: pointer;
      font-family: var(--font-sans);
      font-weight: 500;
      transition: var(--transition-smooth);
      border: 1px solid transparent;
      text-decoration: none;
    }
    .btn-gold {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      padding: 12px 28px;
      font-size: 14px;
      font-family: var(--font-sans);
      font-weight: 600;
      border-radius: 4px;
      border: 1px solid var(--gold);
      cursor: pointer;
      transition: var(--transition-smooth);
      background: var(--gold);
      color: var(--midnight);
    }
    .btn-gold:hover {
      background: #D4B688;
      box-shadow: 0 0 16px var(--gold-dim);
    }
    .btn-outline {
      background: transparent;
      border-color: var(--slate-border);
      color: var(--porcelain);
    }
    .btn-outline:hover {
      border-color: var(--gold);
      color: var(--gold);
      background: var(--gold-dim);
    }
    .btn-sm {
      padding: 5px 10px;
      font-size: 11px;
    }

    /* Modal System */
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(16, 25, 35, 0.85);
      backdrop-filter: blur(8px);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease;
    }
    .modal-backdrop.open {
      opacity: 1;
      pointer-events: auto;
    }
    .modal-box {
      width: 90%;
      max-width: 620px;
      background: #182631;
      border: 1px solid var(--slate-border-light);
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 16px 40px rgba(0,0,0,0.5);
      transform: translateY(14px);
      transition: transform 0.25s ease;
    }
    .modal-backdrop.open .modal-box {
      transform: translateY(0);
    }
    .modal-header {
      padding: 16px 22px;
      border-bottom: 1px solid var(--slate-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #131E27;
    }
    .modal-title {
      font-size: 16px;
      color: var(--white);
    }
    .modal-close {
      background: transparent;
      border: none;
      color: var(--steel);
      cursor: pointer;
      font-size: 18px;
    }
    .modal-close:hover { color: var(--porcelain); }
    .modal-body {
      padding: 22px;
      max-height: 70vh;
      overflow-y: auto;
    }
    .modal-footer {
      padding: 14px 22px;
      background: #131E27;
      border-top: 1px solid var(--slate-border);
      display: flex;
      justify-content: flex-end;
      gap: 12px;
    }

    /* Form Styles */
    .form-group {
      margin-bottom: 16px;
    }
    .form-label {
      display: block;
      font-size: 11px;
      font-family: var(--font-mono);
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--steel);
      margin-bottom: 6px;
    }
    .form-input, .form-select, .form-textarea {
      width: 100%;
      padding: 9px 12px;
      background: var(--midnight);
      border: 1px solid var(--slate-border);
      border-radius: 4px;
      color: var(--porcelain);
      font-size: 13px;
      font-family: var(--font-sans);
      outline: none;
      transition: border-color 0.2s;
    }
    .form-input:focus, .form-select:focus, .form-textarea:focus {
      border-color: var(--gold);
    }

    /* Toast */
    #toast-container {
      position: fixed;
      bottom: 24px;
      right: 24px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      z-index: 2000;
      pointer-events: none;
    }
    .toast-msg {
      background: #1B2B38;
      border: 1px solid var(--gold);
      color: var(--porcelain);
      padding: 12px 18px;
      border-radius: 6px;
      font-size: 13px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.4);
      display: flex;
      align-items: center;
      gap: 12px;
      animation: toastIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      pointer-events: auto;
      max-width: 420px;
    }
    @keyframes toastIn {
      from { transform: translateY(20px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
    @keyframes toastOut {
      from { transform: translateY(0); opacity: 1; }
      to { transform: translateY(20px); opacity: 0; }
    }

    /* Print Stylesheet for Shift Report */
    @media print {
      body {
        background: #FFFFFF !important;
        color: #111111 !important;
      }
      #story-mode-container, .app-topbar, .app-sidebar, .btn, .no-print {
        display: none !important;
      }
      #product-mode-container {
        display: block !important;
        height: auto !important;
        overflow: visible !important;
      }
      .app-workspace {
        display: block !important;
        height: auto !important;
      }
      .app-main {
        display: block !important;
        overflow: visible !important;
      }
      .view-panel {
        display: none !important;
      }
      #view-shift-report {
        display: block !important;
        padding: 0 !important;
        max-width: 100% !important;
      }
      .card, .data-table-container {
        background: #FFFFFF !important;
        border: 1px solid #CCCCCC !important;
        color: #111111 !important;
        box-shadow: none !important;
      }
      .data-table th {
        background: #F0F0F0 !important;
        color: #333333 !important;
        border-bottom: 2px solid #999999 !important;
      }
      .data-table td {
        color: #222222 !important;
        border-bottom: 1px solid #DDDDDD !important;
      }
      .metric-value {
        color: #000000 !important;
      }
      .metric-card {
        background: #F9F9F9 !important;
        border: 1px solid #CCCCCC !important;
      }
    }
"""
print("parts_css.py created successfully.")
