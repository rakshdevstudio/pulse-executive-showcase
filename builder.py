import json
import os

with open("/Users/raksh/.gemini/antigravity/scratch/pulse-showcase/initial_data.json", "r") as f:
    initial_data = json.load(f)

json_data_str = json.dumps(initial_data)

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PULSE — Workforce Operations & Performance Intelligence</title>
  <style>
    /* ==========================================================================
       PULSE EXECUTIVE SHOWCASE DESIGN SYSTEM
       Color Tokens:
       Midnight Navy: #101923
       Deep Slate: #182631
       Champagne Gold: #C6A675
       Warm Porcelain: #F7F6F2
       Steel Grey: #93A3AE
       White: #FFFFFF
       Muted Emerald: #468B77
       Subtle Amber: #C48C49
       ========================================================================== */
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
      --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      --font-mono: 'SF Mono', 'Cascadia Code', 'Fira Code', 'Consolas', monospace;

      --transition-smooth: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      --shadow-sm: 0 4px 12px rgba(0, 0, 0, 0.25);
      --shadow-md: 0 8px 28px rgba(0, 0, 0, 0.35);
      --shadow-lg: 0 16px 48px rgba(0, 0, 0, 0.45);
      --shadow-gold: 0 0 24px rgba(198, 166, 117, 0.22);
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html, body {
      width: 100%;
      height: 100%;
      background-color: var(--midnight);
      color: var(--porcelain);
      font-family: var(--font-sans);
      font-size: 15px;
      line-height: 1.5;
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    /* Accessibility / reduced motion */
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }

    /* Global Typography */
    h1, h2, h3, .serif-font {
      font-family: var(--font-serif);
      letter-spacing: 0.02em;
      font-weight: 400;
    }
    .mono-font {
      font-family: var(--font-mono);
    }
    .gold-text {
      color: var(--gold);
    }
    .steel-text {
      color: var(--steel);
    }

    /* Master Mode Containers */
    #story-mode-container, #product-mode-container {
      position: absolute;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
    }
    #story-mode-container.hidden, #product-mode-container.hidden {
      display: none !important;
      opacity: 0;
      pointer-events: none;
      z-index: 0;
    }
    #story-mode-container:not(.hidden), #product-mode-container:not(.hidden) {
      display: flex;
      opacity: 1;
      pointer-events: auto;
      z-index: 10;
    }

    /* ==========================================================================
       STORY MODE STYLES
       ========================================================================== */
    #story-mode-container {
      background: radial-gradient(circle at 50% 30%, #15222E 0%, #101923 70%, #0B1118 100%);
      display: flex;
      flex-direction: column;
    }

    /* Top presentation status bar */
    .story-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 18px 36px;
      height: 64px;
      border-bottom: 1px solid rgba(147, 163, 174, 0.12);
      background: rgba(16, 25, 35, 0.7);
      backdrop-filter: blur(12px);
      z-index: 20;
    }
    .brand-mark {
      display: flex;
      align-items: center;
      gap: 12px;
      font-family: var(--font-serif);
      font-size: 19px;
      letter-spacing: 0.24em;
      color: var(--white);
      text-transform: uppercase;
    }
    .pulse-dot {
      width: 9px;
      height: 9px;
      border-radius: 50%;
      background: var(--gold);
      box-shadow: 0 0 12px var(--gold);
      animation: pulseGlow 2.4s infinite ease-in-out;
    }
    @keyframes pulseGlow {
      0%, 100% { opacity: 0.4; transform: scale(0.85); box-shadow: 0 0 4px var(--gold); }
      50% { opacity: 1; transform: scale(1.15); box-shadow: 0 0 16px var(--gold); }
    }
    .brand-subtext {
      font-family: var(--font-sans);
      font-size: 11px;
      letter-spacing: 0.1em;
      color: var(--steel);
      text-transform: uppercase;
      padding-left: 12px;
      border-left: 1px solid rgba(147, 163, 174, 0.3);
    }
    .story-controls {
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .scene-counter {
      font-family: var(--font-mono);
      font-size: 12px;
      letter-spacing: 0.12em;
      color: var(--gold);
      background: var(--gold-dim);
      padding: 4px 12px;
      border-radius: 4px;
      border: 1px solid var(--gold-border);
    }
    .btn-header {
      background: rgba(24, 38, 49, 0.7);
      color: var(--porcelain);
      border: 1px solid var(--slate-border);
      padding: 6px 14px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 12px;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      transition: var(--transition-smooth);
    }
    .btn-header:hover {
      background: var(--slate-card-hover);
      border-color: var(--gold);
      color: var(--gold);
    }
    .btn-header.primary-action {
      background: var(--gold);
      color: var(--midnight);
      border-color: var(--gold);
      font-weight: 600;
    }
    .btn-header.primary-action:hover {
      background: var(--gold-light);
      box-shadow: var(--shadow-gold);
    }

    /* Scene Viewport */
    .scene-viewport {
      flex: 1;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .scene-slide {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 40px 80px;
    }
    .scene-slide.active {
      display: flex;
      animation: fadeInScene 0.25s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      z-index: 5;
    }
    @keyframes fadeInScene {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Progress bar */
    .story-progress-bar {
      position: absolute;
      top: 64px;
      left: 0;
      width: 100%;
      height: 3px;
      background: rgba(147, 163, 174, 0.15);
      z-index: 25;
    }
    .story-progress-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--gold), var(--gold-light));
      width: 12.5%;
      transition: width 0.4s ease;
      box-shadow: 0 0 8px var(--gold);
    }

    /* Bottom slide footer navigation */
    .story-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 16px 40px;
      height: 64px;
      background: rgba(16, 25, 35, 0.85);
      border-top: 1px solid rgba(147, 163, 174, 0.12);
      z-index: 20;
    }
    .nav-keyboard-hint {
      font-size: 12px;
      color: var(--steel-dim);
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .key-badge {
      display: inline-block;
      padding: 2px 7px;
      background: rgba(24, 38, 49, 0.9);
      border: 1px solid var(--slate-border);
      border-radius: 3px;
      font-family: var(--font-mono);
      font-size: 10px;
      color: var(--steel);
    }
    .slide-dots {
      display: flex;
      gap: 10px;
    }
    .slide-dot {
      width: 28px;
      height: 4px;
      background: rgba(147, 163, 174, 0.25);
      border-radius: 2px;
      cursor: pointer;
      transition: var(--transition-smooth);
    }
    .slide-dot.active {
      background: var(--gold);
      width: 44px;
      box-shadow: 0 0 8px var(--gold);
    }
    .slide-nav-btns {
      display: flex;
      gap: 12px;
    }
    .btn-nav {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: rgba(24, 38, 49, 0.8);
      border: 1px solid var(--slate-border);
      color: var(--porcelain);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: var(--transition-smooth);
    }
    .btn-nav:hover:not(:disabled) {
      background: var(--slate-card-hover);
      border-color: var(--gold);
      color: var(--gold);
      transform: scale(1.05);
    }
    .btn-nav:disabled {
      opacity: 0.3;
      cursor: not-allowed;
    }

    /* ==========================================================================
       INDIVIDUAL SCENES (1 to 8)
       ========================================================================== */
    /* Scene 1: Opening */
    .scene-1-container {
      max-width: 960px;
      text-align: center;
      position: relative;
    }
    .scene-1-pulse-svg {
      width: 100%;
      height: 110px;
      margin-bottom: 30px;
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
      max-width: 680px;
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

    /* Scene 2: The Existing Problem */
    .scene-2-container {
      width: 100%;
      max-width: 1140px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .scene-eyebrow {
      font-family: var(--font-mono);
      font-size: 11px;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 10px;
    }
    .scene-title {
      font-size: 38px;
      color: var(--porcelain);
      text-align: center;
      margin-bottom: 28px;
      line-height: 1.2;
    }
    .sheets-stage {
      position: relative;
      width: 100%;
      height: 330px;
      margin-bottom: 24px;
      perspective: 1000px;
    }
    .floating-sheet {
      position: absolute;
      width: 230px;
      padding: 16px;
      background: var(--slate-card);
      border: 1px solid var(--slate-border);
      border-radius: 8px;
      box-shadow: var(--shadow-md);
      transition: all 0.75s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: default;
    }
    .floating-sheet:hover {
      transform: translateY(-8px) scale(1.04) !important;
      border-color: var(--gold);
      box-shadow: var(--shadow-gold);
      z-index: 30 !important;
    }
    .sheet-icon {
      width: 28px;
      height: 28px;
      border-radius: 6px;
      background: var(--gold-dim);
      color: var(--gold);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 10px;
    }
    .sheet-name {
      font-size: 14px;
      font-weight: 600;
      color: var(--porcelain);
      margin-bottom: 4px;
    }
    .sheet-desc {
      font-size: 11px;
      color: var(--steel);
      line-height: 1.4;
    }
    .sheet-status {
      display: inline-block;
      margin-top: 8px;
      font-family: var(--font-mono);
      font-size: 9px;
      padding: 2px 6px;
      border-radius: 3px;
      background: rgba(217, 83, 79, 0.15);
      color: #E68280;
    }
    .sheets-consolidated .floating-sheet {
      left: 50% !important;
      top: 50% !important;
      transform: translate(-50%, -50%) scale(0.65) !important;
      opacity: 0.15 !important;
    }
    .central-hub-reveal {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) scale(0.6);
      width: 440px;
      padding: 28px;
      background: linear-gradient(145deg, #182631, #101923);
      border: 2px solid var(--gold);
      border-radius: 12px;
      text-align: center;
      box-shadow: 0 0 50px rgba(198, 166, 117, 0.35);
      opacity: 0;
      pointer-events: none;
      transition: all 0.75s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 25;
    }
    .sheets-consolidated .central-hub-reveal {
      opacity: 1;
      pointer-events: auto;
      transform: translate(-50%, -50%) scale(1);
    }
    .friction-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 16px;
      width: 100%;
      margin-top: 10px;
    }
    .friction-card {
      background: rgba(24, 38, 49, 0.5);
      border: 1px solid var(--slate-border);
      border-radius: 6px;
      padding: 12px 14px;
      text-align: left;
    }
    .friction-tag {
      font-family: var(--font-mono);
      font-size: 10px;
      color: var(--amber);
      margin-bottom: 4px;
    }
    .friction-title {
      font-size: 13px;
      font-weight: 600;
      color: var(--porcelain);
      margin-bottom: 4px;
    }
    .friction-body {
      font-size: 11px;
      color: var(--steel);
      line-height: 1.4;
    }

    /* Scene 3: The Product Reveal */
    .scene-3-container {
      max-width: 1080px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .reveal-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 16px;
      background: var(--gold-dim);
      border: 1px solid var(--gold-border);
      border-radius: 20px;
      color: var(--gold);
      font-family: var(--font-mono);
      font-size: 11px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      margin-bottom: 18px;
    }
    .product-hero-title {
      font-size: 68px;
      letter-spacing: 0.18em;
      color: var(--white);
      line-height: 1;
      margin-bottom: 12px;
      text-shadow: 0 4px 24px rgba(0,0,0,0.5);
    }
    .product-hero-sub {
      font-size: 20px;
      color: var(--gold);
      letter-spacing: 0.12em;
      text-transform: uppercase;
      margin-bottom: 8px;
    }
    .product-hero-tagline {
      font-size: 15px;
      color: var(--steel);
      letter-spacing: 0.08em;
      margin-bottom: 28px;
    }
    .preview-mockup-frame {
      position: relative;
      width: 860px;
      height: 340px;
      border-radius: 12px;
      background: var(--slate);
      border: 1px solid rgba(198, 166, 117, 0.4);
      box-shadow: 0 24px 64px rgba(0, 0, 0, 0.7), 0 0 40px rgba(198, 166, 117, 0.18);
      overflow: hidden;
      cursor: pointer;
      transition: var(--transition-smooth);
    }
    .preview-mockup-frame:hover {
      transform: translateY(-6px) scale(1.01);
      border-color: var(--gold);
      box-shadow: 0 30px 80px rgba(0, 0, 0, 0.8), 0 0 60px rgba(198, 166, 117, 0.3);
    }
    .mockup-inner-header {
      height: 38px;
      background: #14202B;
      border-bottom: 1px solid var(--slate-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
    }
    .mockup-dots {
      display: flex;
      gap: 6px;
    }
    .mockup-dot {
      width: 9px;
      height: 9px;
      border-radius: 50%;
      background: rgba(147, 163, 174, 0.3);
    }
    .mockup-content {
      padding: 20px;
      display: grid;
      grid-template-columns: 240px 1fr;
      gap: 18px;
      height: calc(100% - 38px);
      text-align: left;
    }
    .mockup-side {
      background: rgba(16, 25, 35, 0.6);
      border-radius: 8px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .mockup-main {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .mockup-kpis {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
    }
    .mock-kpi-card {
      background: rgba(28, 45, 59, 0.6);
      border: 1px solid var(--slate-border);
      border-radius: 6px;
      padding: 10px;
    }
    .mock-kpi-val {
      font-size: 22px;
      font-weight: 600;
      color: var(--gold);
      font-family: var(--font-mono);
    }
    .mock-chart-preview {
      flex: 1;
      background: rgba(28, 45, 59, 0.4);
      border: 1px solid var(--slate-border);
      border-radius: 6px;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .mockup-overlay-cta {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(16, 25, 35, 0.5);
      backdrop-filter: blur(2px);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 12px;
      transition: background 0.3s;
    }
    .preview-mockup-frame:hover .mockup-overlay-cta {
      background: rgba(16, 25, 35, 0.35);
    }

    /* Scene 4: Core Capabilities Overview */
    .scene-4-container {
      max-width: 1140px;
      width: 100%;
    }
    .pillars-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-top: 24px;
    }
    .pillar-card {
      background: var(--slate-card);
      border: 1px solid var(--slate-border);
      border-radius: 8px;
      padding: 24px 20px;
      display: flex;
      flex-direction: column;
      transition: var(--transition-smooth);
      position: relative;
      overflow: hidden;
    }
    .pillar-card:hover {
      border-color: var(--gold);
      transform: translateY(-6px);
      box-shadow: var(--shadow-gold);
    }
    .pillar-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: var(--gold);
      opacity: 0.6;
    }
    .pillar-num {
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--gold);
      margin-bottom: 12px;
    }
    .pillar-title {
      font-size: 18px;
      color: var(--porcelain);
      margin-bottom: 10px;
      line-height: 1.3;
    }
    .pillar-desc {
      font-size: 13px;
      color: var(--steel);
      line-height: 1.5;
      margin-bottom: 16px;
      flex: 1;
    }
    .pillar-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }
    .p-tag {
      font-size: 10px;
      font-family: var(--font-mono);
      padding: 2px 7px;
      background: rgba(147, 163, 174, 0.1);
      border-radius: 3px;
      color: var(--steel);
    }

    /* Scene 5: Before and After Experience */
    .scene-5-container {
      max-width: 1120px;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .split-compare-box {
      position: relative;
      width: 100%;
      height: 400px;
      border-radius: 10px;
      border: 1px solid var(--slate-border);
      overflow: hidden;
      margin-top: 20px;
      box-shadow: var(--shadow-lg);
    }
    .compare-side {
      position: absolute;
      top: 0;
      height: 100%;
      padding: 30px;
      display: flex;
      flex-direction: column;
    }
    .compare-side.before {
      left: 0;
      width: 50%;
      background: #141E28;
      border-right: 1px solid rgba(217, 83, 79, 0.3);
    }
    .compare-side.after {
      right: 0;
      width: 50%;
      background: #152533;
    }
    .compare-header {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 18px;
    }
    .badge-status-red {
      padding: 4px 10px;
      background: var(--crimson-dim);
      color: #FF8585;
      border: 1px solid rgba(217, 83, 79, 0.4);
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 600;
    }
    .badge-status-green {
      padding: 4px 10px;
      background: var(--emerald-dim);
      color: #79D1B8;
      border: 1px solid rgba(70, 139, 119, 0.4);
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 600;
    }
    .compare-points {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .compare-point {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      font-size: 14px;
      line-height: 1.4;
    }
    .point-icon {
      margin-top: 3px;
      flex-shrink: 0;
    }

    /* Scene 6: Role-Based Governance */
    .scene-6-container {
      max-width: 1120px;
      width: 100%;
    }
    .roles-story-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
      margin-top: 24px;
    }
    .role-story-card {
      background: var(--slate-card);
      border: 1px solid var(--slate-border);
      border-radius: 8px;
      padding: 22px 18px;
      position: relative;
    }
    .role-story-card.highlighted {
      border-color: var(--gold);
      box-shadow: var(--shadow-gold);
    }
    .role-badge {
      font-family: var(--font-mono);
      font-size: 11px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      padding: 3px 8px;
      border-radius: 4px;
      display: inline-block;
      margin-bottom: 12px;
    }
    .role-badge.emp { background: rgba(147, 163, 174, 0.15); color: var(--porcelain); }
    .role-badge.tl { background: var(--amber-dim); color: var(--amber); }
    .role-badge.mgmt { background: var(--gold-dim); color: var(--gold); border: 1px solid var(--gold-border); }
    .role-badge.admin { background: rgba(62, 123, 153, 0.2); color: #7EB8D6; }
    .role-story-title {
      font-size: 17px;
      color: var(--porcelain);
      margin-bottom: 12px;
    }
    .role-permission-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
      font-size: 12px;
      color: var(--steel);
    }
    .role-permission-list li {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .role-permission-list li.prohibited {
      color: #D98282;
      opacity: 0.8;
      text-decoration: line-through;
    }

    /* Scene 7: 6-Month Roadmap */
    .scene-7-container {
      max-width: 1140px;
      width: 100%;
    }
    .roadmap-timeline {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 12px;
      margin-top: 28px;
      position: relative;
    }
    .roadmap-timeline::before {
      content: '';
      position: absolute;
      top: 42px;
      left: 20px;
      right: 20px;
      height: 2px;
      background: linear-gradient(90deg, var(--gold) 0%, rgba(198, 166, 117, 0.2) 100%);
      z-index: 1;
    }
    .roadmap-month-card {
      background: var(--slate-card);
      border: 1px solid var(--slate-border);
      border-radius: 8px;
      padding: 16px 14px;
      position: relative;
      z-index: 2;
      transition: var(--transition-smooth);
    }
    .roadmap-month-card:hover {
      border-color: var(--gold);
      transform: translateY(-4px);
      box-shadow: var(--shadow-sm);
    }
    .month-node {
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: var(--slate);
      border: 2px solid var(--gold);
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-mono);
      font-size: 10px;
      color: var(--gold);
    }
    .month-label {
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--gold);
      margin-bottom: 4px;
    }
    .month-title {
      font-size: 13px;
      font-weight: 600;
      color: var(--porcelain);
      margin-bottom: 8px;
      line-height: 1.3;
    }
    .month-desc {
      font-size: 11px;
      color: var(--steel);
      line-height: 1.4;
    }

    /* Scene 8: Closing & Proposal */
    .scene-8-container {
      max-width: 900px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .closing-quote-1 {
      font-size: 44px;
      color: var(--porcelain);
      letter-spacing: 0.1em;
      margin-bottom: 6px;
    }
    .closing-quote-2 {
      font-size: 44px;
      color: var(--gold);
      letter-spacing: 0.1em;
      margin-bottom: 18px;
    }
    .closing-sub {
      font-size: 18px;
      color: var(--steel);
      margin-bottom: 28px;
    }
    .internship-banner {
      background: rgba(28, 45, 59, 0.7);
      border: 1px solid var(--gold-border);
      border-radius: 8px;
      padding: 16px 28px;
      margin-bottom: 28px;
      width: 100%;
    }
    .internship-banner-title {
      font-family: var(--font-mono);
      font-size: 12px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 6px;
    }
    .internship-banner-subtitle {
      font-size: 15px;
      color: var(--porcelain);
    }
    .proposal-asks-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 12px;
      margin-bottom: 32px;
      width: 100%;
      text-align: left;
    }
    .ask-box {
      background: rgba(24, 38, 49, 0.5);
      border: 1px solid var(--slate-border);
      border-radius: 6px;
      padding: 12px;
    }
    .ask-num {
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--gold);
      margin-bottom: 4px;
    }
    .ask-text {
      font-size: 11px;
      color: var(--porcelain);
      line-height: 1.4;
    }

    /* ==========================================================================
       EXPLORE PRODUCT MODE (ENTERPRISE APPLICATION SHELL)
       ========================================================================== */
    #product-mode-container {
      background: var(--midnight);
      display: flex;
      flex-direction: column;
    }

    /* Top application bar */
    .app-topbar {
      height: 58px;
      background: var(--slate);
      border-bottom: 1px solid var(--slate-border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 24px;
      z-index: 100;
    }
    .app-brand {
      display: flex;
      align-items: center;
      gap: 12px;
      font-family: var(--font-serif);
      font-size: 18px;
      letter-spacing: 0.2em;
      color: var(--white);
    }
    .app-topbar-center {
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .timezone-pill {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(16, 25, 35, 0.8);
      border: 1px solid var(--slate-border);
      padding: 4px 12px;
      border-radius: 20px;
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--steel);
      cursor: pointer;
      transition: var(--transition-smooth);
    }
    .timezone-pill:hover {
      border-color: var(--gold);
      color: var(--porcelain);
    }
    .role-switcher-wrap {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(16, 25, 35, 0.8);
      border: 1px solid var(--slate-border);
      padding: 3px 10px;
      border-radius: 6px;
    }
    .role-label {
      font-size: 11px;
      color: var(--steel);
      font-family: var(--font-mono);
      text-transform: uppercase;
    }
    .role-select {
      background: transparent;
      border: none;
      color: var(--gold);
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      outline: none;
    }
    .role-select option {
      background: var(--slate);
      color: var(--porcelain);
    }
    .app-topbar-right {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .user-pill {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(24, 38, 49, 0.6);
      padding: 4px 10px;
      border-radius: 6px;
      border: 1px solid var(--slate-border);
    }
    .user-avatar {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: var(--gold-dim);
      border: 1px solid var(--gold-border);
      color: var(--gold);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 600;
    }
    .user-meta {
      display: flex;
      flex-direction: column;
      text-align: left;
    }
    .user-name {
      font-size: 12px;
      font-weight: 600;
      color: var(--porcelain);
    }
    .user-role-title {
      font-size: 10px;
      color: var(--steel);
    }

    /* Main Application Body (Sidebar + Content Viewport) */
    .app-workspace {
      flex: 1;
      display: flex;
      overflow: hidden;
    }
    .app-sidebar {
      width: 250px;
      background: #131E27;
      border-right: 1px solid var(--slate-border);
      display: flex;
      flex-direction: column;
      padding: 16px 0;
    }
    .nav-section-title {
      padding: 8px 20px;
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
      gap: 2px;
    }
    .menu-item {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 10px 20px;
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
      background: var(--gold-dim);
      font-weight: 600;
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
      padding: 1px 6px;
      border-radius: 10px;
      background: rgba(147, 163, 174, 0.15);
      color: var(--steel);
    }
    .menu-badge.alert {
      background: var(--amber-dim);
      color: var(--amber);
    }

    /* Main Viewport */
    .app-viewport {
      flex: 1;
      background: var(--midnight);
      overflow-y: auto;
      padding: 24px 32px 60px;
      position: relative;
    }
    .view-panel {
      display: none;
      animation: fadeInView 0.3s ease forwards;
    }
    .view-panel.active {
      display: block;
    }
    @keyframes fadeInView {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .view-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 24px;
      border-bottom: 1px solid var(--slate-border);
      padding-bottom: 16px;
    }
    .view-title-group h2 {
      font-size: 26px;
      color: var(--porcelain);
      margin-bottom: 4px;
    }
    .view-subtitle {
      font-size: 13px;
      color: var(--steel);
    }
    .view-actions {
      display: flex;
      gap: 10px;
    }

    /* Common Card Styles */
    .kpi-row {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 14px;
      margin-bottom: 24px;
    }
    .kpi-card {
      background: var(--slate-card);
      border: 1px solid var(--slate-border);
      border-radius: 8px;
      padding: 16px;
      position: relative;
      transition: var(--transition-smooth);
    }
    .kpi-card:hover {
      border-color: var(--slate-border-light);
      transform: translateY(-2px);
    }
    .kpi-label {
      font-size: 11px;
      font-family: var(--font-mono);
      text-transform: uppercase;
      color: var(--steel);
      margin-bottom: 6px;
      letter-spacing: 0.05em;
    }
    .kpi-value {
      font-size: 28px;
      font-family: var(--font-mono);
      font-weight: 600;
      color: var(--porcelain);
      line-height: 1;
      margin-bottom: 4px;
    }
    .kpi-meta {
      font-size: 11px;
      color: var(--steel-dim);
    }
    .kpi-meta.trend-up { color: #79D1B8; }
    .kpi-meta.trend-down { color: #E68280; }

    /* Layout Grids */
    .grid-2col {
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 20px;
      margin-bottom: 24px;
    }
    .grid-1-1 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 24px;
    }
    .grid-3col {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-bottom: 24px;
    }
    .dashboard-card {
      background: var(--slate-card);
      border: 1px solid var(--slate-border);
      border-radius: 8px;
      padding: 20px;
      box-shadow: var(--shadow-sm);
    }
    .card-title-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }
    .card-title {
      font-size: 15px;
      font-weight: 600;
      color: var(--porcelain);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* Data Tables */
    .table-container {
      width: 100%;
      overflow-x: auto;
      border: 1px solid var(--slate-border);
      border-radius: 6px;
      background: var(--slate-card);
    }
    .pulse-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13px;
    }
    .pulse-table th {
      background: rgba(16, 25, 35, 0.7);
      padding: 12px 14px;
      font-family: var(--font-mono);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--steel);
      border-bottom: 1px solid var(--slate-border);
    }
    .pulse-table td {
      padding: 12px 14px;
      border-bottom: 1px solid rgba(147, 163, 174, 0.12);
      color: var(--porcelain);
    }
    .pulse-table tr:hover td {
      background: var(--slate-card-hover);
    }
    .status-badge {
      display: inline-block;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-family: var(--font-mono);
      font-weight: 500;
    }
    .status-badge.present { background: var(--emerald-dim); color: #79D1B8; border: 1px solid rgba(70, 139, 119, 0.3); }
    .status-badge.absent { background: var(--crimson-dim); color: #FF8585; border: 1px solid rgba(217, 83, 79, 0.3); }
    .status-badge.leave { background: var(--amber-dim); color: #E8A86B; border: 1px solid rgba(196, 140, 73, 0.3); }
    .status-badge.late { background: rgba(198, 166, 117, 0.2); color: var(--gold-light); border: 1px solid var(--gold-border); }

    /* Form Controls */
    .pulse-input, .pulse-select, .pulse-textarea {
      background: #14202B;
      border: 1px solid var(--slate-border);
      border-radius: 4px;
      padding: 8px 12px;
      color: var(--porcelain);
      font-size: 13px;
      width: 100%;
      outline: none;
      transition: border-color 0.2s;
    }
    .pulse-input:focus, .pulse-select:focus, .pulse-textarea:focus {
      border-color: var(--gold);
    }
    .form-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 14px;
    }
    .form-label {
      font-size: 12px;
      font-family: var(--font-mono);
      color: var(--steel);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .form-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }

    /* Buttons */
    .btn-gold {
      background: var(--gold);
      color: var(--midnight);
      border: 1px solid var(--gold);
      padding: 8px 16px;
      border-radius: 4px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: var(--transition-smooth);
    }
    .btn-gold:hover {
      background: var(--gold-light);
      box-shadow: var(--shadow-gold);
    }
    .btn-outline {
      background: transparent;
      color: var(--porcelain);
      border: 1px solid var(--slate-border);
      padding: 8px 16px;
      border-radius: 4px;
      font-size: 13px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: var(--transition-smooth);
    }
    .btn-outline:hover {
      background: var(--slate-card-hover);
      border-color: var(--steel);
    }
    .btn-sm {
      padding: 4px 10px;
      font-size: 11px;
    }

    /* Quality Workflow Stepper */
    .stepper-container {
      display: flex;
      justify-content: space-between;
      position: relative;
      margin: 24px 0 28px;
    }
    .stepper-line {
      position: absolute;
      top: 15px;
      left: 30px;
      right: 30px;
      height: 2px;
      background: rgba(147, 163, 174, 0.2);
      z-index: 1;
    }
    .stepper-line-fill {
      height: 100%;
      background: var(--gold);
      width: 25%;
      transition: width 0.4s ease;
    }
    .step-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      z-index: 2;
      cursor: pointer;
    }
    .step-circle {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: var(--slate);
      border: 2px solid var(--slate-border);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--steel);
      margin-bottom: 8px;
      transition: var(--transition-smooth);
    }
    .step-item.active .step-circle {
      border-color: var(--gold);
      background: var(--gold-dim);
      color: var(--gold);
      box-shadow: 0 0 12px rgba(198, 166, 117, 0.4);
    }
    .step-item.completed .step-circle {
      border-color: var(--emerald);
      background: var(--emerald-dim);
      color: #79D1B8;
    }
    .step-title {
      font-size: 11px;
      font-family: var(--font-mono);
      text-transform: uppercase;
      color: var(--steel);
    }
    .step-item.active .step-title {
      color: var(--gold);
      font-weight: 600;
    }

    /* Editorial Award Cards (Recognition) */
    .awards-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-bottom: 30px;
    }
    .award-card {
      background: var(--slate-card);
      border: 1px solid var(--slate-border);
      border-radius: 8px;
      padding: 24px 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      position: relative;
      overflow: hidden;
      transition: var(--transition-smooth);
    }
    .award-card:hover {
      border-color: var(--gold);
      transform: translateY(-4px);
      box-shadow: var(--shadow-gold);
    }
    .award-category-pill {
      font-family: var(--font-mono);
      font-size: 11px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 16px;
    }
    .award-avatar-ring {
      width: 72px;
      height: 72px;
      border-radius: 50%;
      border: 2px solid var(--gold);
      padding: 3px;
      margin-bottom: 14px;
      box-shadow: 0 0 16px rgba(198, 166, 117, 0.25);
    }
    .award-avatar {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background: var(--slate-card-hover);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      color: var(--gold);
      font-weight: 600;
    }
    .award-winner-name {
      font-size: 18px;
      font-weight: 600;
      color: var(--porcelain);
      margin-bottom: 4px;
    }
    .award-winner-role {
      font-size: 12px;
      color: var(--steel);
      margin-bottom: 14px;
    }
    .award-reason {
      font-size: 12px;
      color: var(--steel);
      line-height: 1.45;
      margin-bottom: 16px;
      flex: 1;
    }
    .award-metrics-table {
      width: 100%;
      border-top: 1px solid var(--slate-border);
      padding-top: 12px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      text-align: left;
    }
    .award-m-label {
      font-size: 10px;
      font-family: var(--font-mono);
      color: var(--steel-dim);
    }
    .award-m-val {
      font-size: 12px;
      font-family: var(--font-mono);
      color: var(--gold);
      font-weight: 600;
    }

    /* Calendar Grid */
    .calendar-container {
      background: var(--slate-card);
      border: 1px solid var(--slate-border);
      border-radius: 8px;
      padding: 20px;
    }
    .calendar-nav-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
    }
    .calendar-days-header {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      text-align: center;
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--steel);
      text-transform: uppercase;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--slate-border);
      margin-bottom: 10px;
    }
    .calendar-grid-cells {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 6px;
    }
    .cal-cell {
      min-height: 90px;
      background: rgba(16, 25, 35, 0.5);
      border: 1px solid rgba(147, 163, 174, 0.12);
      border-radius: 4px;
      padding: 8px;
      display: flex;
      flex-direction: column;
      position: relative;
    }
    .cal-cell.today {
      border-color: var(--gold);
      background: rgba(198, 166, 117, 0.05);
    }
    .cal-date {
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--steel);
      margin-bottom: 6px;
    }
    .cal-cell.today .cal-date {
      color: var(--gold);
      font-weight: 600;
    }
    .cal-event-tag {
      font-size: 10px;
      padding: 2px 6px;
      border-radius: 3px;
      margin-bottom: 4px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .cal-event-tag.holiday { background: rgba(217, 83, 79, 0.2); color: #FF9B99; border: 1px solid rgba(217, 83, 79, 0.3); }
    .cal-event-tag.leave { background: rgba(196, 140, 73, 0.2); color: #E8A86B; border: 1px solid rgba(196, 140, 73, 0.3); }
    .cal-event-tag.shift { background: rgba(70, 139, 119, 0.2); color: #79D1B8; border: 1px solid rgba(70, 139, 119, 0.3); }

    /* Modal System */
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(10, 16, 22, 0.85);
      backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 1000;
    }
    .modal-backdrop.active {
      display: flex;
    }
    .modal-box {
      width: 560px;
      max-width: 90vw;
      background: var(--slate);
      border: 1px solid var(--slate-border-light);
      border-radius: 10px;
      box-shadow: var(--shadow-lg);
      overflow: hidden;
      animation: modalPop 0.25s ease-out;
    }
    @keyframes modalPop {
      from { transform: scale(0.94); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }
    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 18px 24px;
      border-bottom: 1px solid var(--slate-border);
      background: #14212D;
    }
    .modal-title {
      font-size: 17px;
      font-weight: 600;
      color: var(--porcelain);
    }
    .modal-close {
      background: transparent;
      border: none;
      color: var(--steel);
      font-size: 18px;
      cursor: pointer;
    }
    .modal-close:hover {
      color: var(--white);
    }
    .modal-body {
      padding: 24px;
      max-height: 75vh;
      overflow-y: auto;
    }
    .modal-footer {
      padding: 16px 24px;
      border-top: 1px solid var(--slate-border);
      display: flex;
      justify-content: flex-end;
      gap: 12px;
      background: #14212D;
    }

    /* Toast System */
    .toast-container {
      position: fixed;
      bottom: 24px;
      right: 24px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      z-index: 2000;
    }
    .toast-msg {
      background: var(--slate);
      border: 1px solid var(--gold);
      border-left: 4px solid var(--gold);
      padding: 14px 18px;
      border-radius: 6px;
      color: var(--porcelain);
      font-size: 13px;
      box-shadow: var(--shadow-md);
      display: flex;
      align-items: center;
      gap: 12px;
      animation: toastIn 0.3s ease forwards;
    }
    @keyframes toastIn {
      from { transform: translateX(50px); opacity: 0; }
      to { transform: translateX(0); opacity: 1; }
    }
    @keyframes toastOut {
      from { transform: translateX(0); opacity: 1; }
      to { transform: translateX(50px); opacity: 0; }
    }

    /* Global watermark / illustrative data warning */
    
  </style>
</head>
<body>

  <!-- =========================================================================
       1. STORY MODE (CINEMATIC EXECUTIVE PRESENTATION)
       ========================================================================= -->
  <div id="story-mode-container">
    <!-- Top Bar -->
    <header class="story-header">
      <div class="brand-mark">
        <span class="pulse-dot"></span>
        <span>PULSE</span>
        <span class="brand-subtext">Executive Presentation</span>
        <span style="font-size: 10px; font-family: var(--font-mono); color: var(--gold); background: var(--gold-dim); border: 1px solid var(--gold-border); padding: 2px 8px; border-radius: 4px; margin-left: 12px; letter-spacing: 0.08em; text-transform: uppercase;">Illustrative Demonstration Data</span>
      </div>
      <div class="story-controls">
        <span class="scene-counter" id="scene-counter-display">SCENE 01 / 08</span>
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

    <!-- Scene Viewport (8 slides) -->
    <main class="scene-viewport">

      <!-- SCENE 1: OPENING -->
      <section class="scene-slide active" id="scene-slide-0">
        <div class="scene-1-container">
          <!-- Animated SVG Pulse Line -->
          <svg class="scene-1-pulse-svg" viewBox="0 0 900 120" preserveAspectRatio="none">
            <path class="pulse-path" d="M 0 60 L 280 60 L 310 60 L 330 20 L 350 100 L 370 10 L 390 110 L 410 40 L 430 80 L 450 60 L 900 60" />
          </svg>
          <h1 class="headline-line-1">Every Shift Tells a Story.</h1>
          <h2 class="headline-line-2">But are we seeing the whole picture?</h2>
          <p class="scene-1-subtext">An opportunity to transform how our workforce, productivity and operational quality are understood across our India manufacturing operations.</p>
          <div class="scene-1-cta">
            <button class="btn-gold" onclick="nextScene()">
              Begin Presentation
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
          </div>
        </div>
      </section>

      <!-- SCENE 2: THE EXISTING PROBLEM -->
      <section class="scene-slide" id="scene-slide-1">
        <div class="scene-2-container">
          <div class="scene-eyebrow">Current Operational Reality</div>
          <h2 class="scene-title">The work is happening. The information is scattered.</h2>
          
          <!-- Floating Disconnected Sheets -->
          <div class="sheets-stage" id="sheets-stage-container">
            <!-- Sheet 1 -->
            <div class="floating-sheet" style="top: 20px; left: 40px; transform: rotate(-3deg);">
              <div class="sheet-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div>
              <div class="sheet-name">Attendance Register</div>
              <div class="sheet-desc">Manual physical sign-in & disconnected spreadsheet logs.</div>
              <span class="sheet-status">Manual Entry</span>
            </div>
            <!-- Sheet 2 -->
            <div class="floating-sheet" style="top: 15px; left: 320px; transform: rotate(2deg);">
              <div class="sheet-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></div>
              <div class="sheet-name">Daily Orders Keyed</div>
              <div class="sheet-desc">Shift emails and nightly handovers sent to Melbourne.</div>
              <span class="sheet-status">Email Chain</span>
            </div>
            <!-- Sheet 3 -->
            <div class="floating-sheet" style="top: 30px; right: 40px; transform: rotate(-2deg);">
              <div class="sheet-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/></svg></div>
              <div class="sheet-name">Flashings & Bits Log</div>
              <div class="sheet-desc">Separate shared folder workbook tracking units & meters.</div>
              <span class="sheet-status">Excel Workbook</span>
            </div>
            <!-- Sheet 4 -->
            <div class="floating-sheet" style="bottom: 25px; left: 70px; transform: rotate(3deg);">
              <div class="sheet-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg></div>
              <div class="sheet-name">Double-Check Records</div>
              <div class="sheet-desc">Auditor notes on physical printouts and CAD sign-offs.</div>
              <span class="sheet-status">Paper Checklists</span>
            </div>
            <!-- Sheet 5 -->
            <div class="floating-sheet" style="bottom: 20px; left: 340px; transform: rotate(-1deg);">
              <div class="sheet-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg></div>
              <div class="sheet-name">Resupply & Errors Log</div>
              <div class="sheet-desc">Urgent WhatsApp alerts when Melbourne installation halts.</div>
              <span class="sheet-status">Ad-Hoc Messaging</span>
            </div>
            <!-- Sheet 6 -->
            <div class="floating-sheet" style="bottom: 25px; right: 60px; transform: rotate(2deg);">
              <div class="sheet-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div>
              <div class="sheet-name">Leaves & Holidays</div>
              <div class="sheet-desc">Separate email threads, paper slips and calendar notices.</div>
              <span class="sheet-status">Unlinked Records</span>
            </div>

            <!-- Central Hub Transformation Card -->
            <div class="central-hub-reveal" id="central-hub-reveal">
              <div class="pulse-dot" style="margin: 0 auto 12px;"></div>
              <h3 style="font-size: 20px; color: var(--gold); margin-bottom: 6px;">UNIFIED OPERATIONAL CORE</h3>
              <p style="font-size: 13px; color: var(--porcelain); margin-bottom: 14px;">One consolidated data pipeline replacing fragmented files with continuous visibility.</p>
              <span class="badge-status-green">All Channels Synchronized</span>
            </div>
          </div>

          <div style="margin-bottom: 18px;">
            <button class="btn-outline btn-sm" onclick="toggleConsolidateSheets()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 14 10 14 10 20"/><polyline points="20 10 14 10 14 4"/><line x1="14" y1="10" x2="21" y2="3"/><line x1="3" y1="21" x2="10" y2="14"/></svg>
              Toggle Consolidation Animation
            </button>
          </div>

          <!-- Friction Indicators -->
          <div class="friction-grid">
            <div class="friction-card">
              <div class="friction-tag">Friction 01</div>
              <div class="friction-title">Information Scattered</div>
              <div class="friction-body">Data lives across 6+ unconnected formats and folders.</div>
            </div>
            <div class="friction-card">
              <div class="friction-tag">Friction 02</div>
              <div class="friction-title">Manual Consolidation</div>
              <div class="friction-body">Team leaders spend 1.5+ hours nightly copying rows.</div>
            </div>
            <div class="friction-card">
              <div class="friction-tag">Friction 03</div>
              <div class="friction-title">Limited Visibility</div>
              <div class="friction-body">Historical performance comparisons require manual searches.</div>
            </div>
            <div class="friction-card">
              <div class="friction-tag">Friction 04</div>
              <div class="friction-title">Administrative Burden</div>
              <div class="friction-body">Repeated data entry creates fatigue and transcription errors.</div>
            </div>
            <div class="friction-card">
              <div class="friction-tag">Friction 05</div>
              <div class="friction-title">Delayed Action</div>
              <div class="friction-body">Leadership sees operational problems 24–48 hours late.</div>
            </div>
          </div>
        </div>
      </section>

      <!-- SCENE 3: THE PRODUCT REVEAL -->
      <section class="scene-slide" id="scene-slide-2">
        <div class="scene-3-container">
          <div class="reveal-badge">
            <span class="pulse-dot"></span>
            <span>Proposed Operational Intelligence Platform</span>
          </div>
          <h1 class="product-hero-title">PULSE.</h1>
          <h2 class="product-hero-sub">Workforce Operations & Performance Intelligence</h2>
          <p class="product-hero-tagline">Every Person. Every Order. One Clear Picture.</p>

          <!-- Interactive 3D Perspective Dashboard Preview -->
          <div class="preview-mockup-frame" onclick="switchToProductMode()">
            <div class="mockup-inner-header">
              <div class="mockup-dots">
                <div class="mockup-dot"></div>
                <div class="mockup-dot"></div>
                <div class="mockup-dot"></div>
              </div>
              <span style="font-family: var(--font-mono); font-size: 11px; color: var(--gold);">PULSE / EXECUTIVE OPERATIONS CONSOLE</span>
              <span style="font-size: 11px; color: var(--emerald);">● LIVE SYSTEM PROTOTYPE</span>
            </div>
            <div class="mockup-content">
              <div class="mockup-side">
                <div style="font-size: 12px; font-weight: 600; color: var(--gold);">SHIFT A IN PROGRESS</div>
                <div style="font-size: 11px; color: var(--steel);">Present: 21 / 24 Staff</div>
                <div style="font-size: 11px; color: var(--steel);">Keying SLA: 99.4%</div>
                <div style="font-size: 11px; color: var(--steel);">Melbourne Sync: Active</div>
                <div style="margin-top: auto; padding: 8px; background: rgba(0,0,0,0.3); border-radius: 4px; font-size: 10px; color: var(--gold);">
                  Click to launch interactive prototype
                </div>
              </div>
              <div class="mockup-main">
                <div class="mockup-kpis">
                  <div class="mock-kpi-card">
                    <div style="font-size: 10px; color: var(--steel);">ORDERS TODAY</div>
                    <div class="mock-kpi-val">184</div>
                  </div>
                  <div class="mock-kpi-card">
                    <div style="font-size: 10px; color: var(--steel);">FLASHINGS KEYED</div>
                    <div class="mock-kpi-val">1,248</div>
                  </div>
                  <div class="mock-kpi-card">
                    <div style="font-size: 10px; color: var(--steel);">DOUBLE-CHECKS</div>
                    <div class="mock-kpi-val">179</div>
                  </div>
                </div>
                <div class="mock-chart-preview">
                  <svg width="100%" height="100" viewBox="0 0 500 100" preserveAspectRatio="none">
                    <path d="M 0 80 Q 70 30, 150 45 T 300 25 T 420 50 T 500 15 L 500 100 L 0 100 Z" fill="rgba(198, 166, 117, 0.12)" />
                    <path d="M 0 80 Q 70 30, 150 45 T 300 25 T 420 50 T 500 15" stroke="#C6A675" stroke-width="2.5" fill="none" />
                  </svg>
                </div>
              </div>
            </div>
            <div class="mockup-overlay-cta">
              <button class="btn-gold" style="font-size: 15px; padding: 12px 28px;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
                EXPLORE THE EXPERIENCE
              </button>
              <span style="font-size: 12px; color: var(--steel);">Click anywhere on mockup to launch interactive demo</span>
            </div>
          </div>
        </div>
      </section>

      <!-- SCENE 4: CORE CAPABILITIES OVERVIEW -->
      <section class="scene-slide" id="scene-slide-3">
        <div class="scene-4-container">
          <div class="scene-eyebrow">Architectural Pillars</div>
          <h2 class="scene-title">Four Pillars of Operational Intelligence</h2>
          <div class="pillars-grid">
            <div class="pillar-card">
              <div class="pillar-num">PILLAR 01</div>
              <h3 class="pillar-title">Unified Attendance & Availability</h3>
              <p class="pillar-desc">Real-time shift rosters, leave tracking with privacy boundaries, automated late/absent logging, and seamless capacity planning.</p>
              <div class="pillar-tags">
                <span class="p-tag">Shift Roster</span>
                <span class="p-tag">Leave Workflow</span>
                <span class="p-tag">Privacy Masking</span>
              </div>
            </div>
            <div class="pillar-card">
              <div class="pillar-num">PILLAR 02</div>
              <h3 class="pillar-title">High-Velocity Production Reporting</h3>
              <p class="pillar-desc">Rapid entry for orders, flashings, custom bits, and double-checks with instant validation, draft states, and executive export.</p>
              <div class="pillar-tags">
                <span class="p-tag">Sheet-metal Specs</span>
                <span class="p-tag">Flashings / Bits</span>
                <span class="p-tag">CSV Export</span>
              </div>
            </div>
            <div class="pillar-card">
              <div class="pillar-num">PILLAR 03</div>
              <h3 class="pillar-title">Verified Root-Cause Quality</h3>
              <p class="pillar-desc">Transparent 5-stage resupply investigations that separate drafting ambiguities from machine tolerances with zero-blame ethics.</p>
              <div class="pillar-tags">
                <span class="p-tag">5-Stage Stepper</span>
                <span class="p-tag">Root Cause Analysis</span>
                <span class="p-tag">Cost Auditing</span>
              </div>
            </div>
            <div class="pillar-card">
              <div class="pillar-num">PILLAR 04</div>
              <h3 class="pillar-title">Dual-Timezone Synchronization</h3>
              <p class="pillar-desc">Complete harmony between India working shifts and Melbourne Victorian fabrication schedules, including midnight-crossing night shifts.</p>
              <div class="pillar-tags">
                <span class="p-tag">India IST</span>
                <span class="p-tag">Melbourne AEDT</span>
                <span class="p-tag">VIC Holidays</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SCENE 5: BEFORE AND AFTER SPLIT EXPERIENCE -->
      <section class="scene-slide" id="scene-slide-4">
        <div class="scene-5-container">
          <div class="scene-eyebrow">Operational Transformation</div>
          <h2 class="scene-title">The Evolution of Daily Operations</h2>
          
          <div class="split-compare-box">
            <!-- Left: Before -->
            <div class="compare-side before">
              <div class="compare-header">
                <span class="badge-status-red">BEFORE PULSE</span>
                <span style="font-size: 13px; color: var(--steel);">Fragmented Disconnection</span>
              </div>
              <ul class="compare-points">
                <li class="compare-point">
                  <span class="point-icon" style="color: #FF8585;">✕</span>
                  <span>Separate spreadsheets and physical logbooks requiring continuous reconciliation.</span>
                </li>
                <li class="compare-point">
                  <span class="point-icon" style="color: #FF8585;">✕</span>
                  <span>Team leaders spend 90+ minutes every evening consolidating orders keyed.</span>
                </li>
                <li class="compare-point">
                  <span class="point-icon" style="color: #FF8585;">✕</span>
                  <span>Quality errors trigger finger-pointing without structured root-cause investigation.</span>
                </li>
                <li class="compare-point">
                  <span class="point-icon" style="color: #FF8585;">✕</span>
                  <span>Executive management has delayed, retrospective visibility into shift productivity.</span>
                </li>
              </ul>
            </div>

            <!-- Right: After -->
            <div class="compare-side after">
              <div class="compare-header">
                <span class="badge-status-green">AFTER PULSE</span>
                <span style="font-size: 13px; color: var(--gold);">Unified Operational Intelligence</span>
              </div>
              <ul class="compare-points">
                <li class="compare-point">
                  <span class="point-icon" style="color: #79D1B8;">✓</span>
                  <span>Single centralized platform for attendance, production logs, quality cases and leave.</span>
                </li>
                <li class="compare-point">
                  <span class="point-icon" style="color: #79D1B8;">✓</span>
                  <span>Structured daily entry completed in under 4 minutes per shift with instant validation.</span>
                </li>
                <li class="compare-point">
                  <span class="point-icon" style="color: #79D1B8;">✓</span>
                  <span>Objective 5-stage resupply workflow verifying drawing, material, and system causes.</span>
                </li>
                <li class="compare-point">
                  <span class="point-icon" style="color: #79D1B8;">✓</span>
                  <span>Real-time executive dashboard linking India shifts with Melbourne delivery schedules.</span>
                </li>
              </ul>
            </div>
          </div>

          <div style="margin-top: 18px; font-size: 12px; color: var(--steel);">
            Demonstrating operational clarity without inflated claims or unverified statistics.
          </div>
        </div>
      </section>

      <!-- SCENE 6: ROLE-BASED GOVERNANCE & PRIVACY -->
      <section class="scene-slide" id="scene-slide-5">
        <div class="scene-6-container">
          <div class="scene-eyebrow">Enterprise Governance</div>
          <h2 class="scene-title">Role-Based Access with Strict Privacy Boundaries</h2>
          
          <div class="roles-story-grid">
            <div class="role-story-card">
              <span class="role-badge emp">Employee</span>
              <h3 class="role-story-title">Keying Specialist</h3>
              <ul class="role-permission-list">
                <li><span style="color: #79D1B8;">✓</span> View personal attendance & shifts</li>
                <li><span style="color: #79D1B8;">✓</span> Apply for confidential leave</li>
                <li><span style="color: #79D1B8;">✓</span> View public team availability</li>
                <li><span style="color: #79D1B8;">✓</span> Receive peer recognition</li>
                <li class="prohibited"><span>✕</span> Others' private medical reasons</li>
                <li class="prohibited"><span>✕</span> Resupply financial losses</li>
              </ul>
            </div>

            <div class="role-story-card">
              <span class="role-badge tl">Team Leader</span>
              <h3 class="role-story-title">Shift Supervisor</h3>
              <ul class="role-permission-list">
                <li><span style="color: #79D1B8;">✓</span> Submit daily shift production logs</li>
                <li><span style="color: #79D1B8;">✓</span> Approve/reject shift leave requests</li>
                <li><span style="color: #79D1B8;">✓</span> Log attendance corrections</li>
                <li><span style="color: #79D1B8;">✓</span> Initiate quality investigation cases</li>
                <li class="prohibited"><span>✕</span> System permissions & security</li>
                <li class="prohibited"><span>✕</span> Organization-wide financial loss</li>
              </ul>
            </div>

            <div class="role-story-card highlighted">
              <span class="role-badge mgmt">Management</span>
              <h3 class="role-story-title">Managing Director</h3>
              <ul class="role-permission-list">
                <li><span style="color: #79D1B8;">✓</span> Executive KPI dashboard</li>
                <li><span style="color: #79D1B8;">✓</span> Multi-shift cross-comparisons</li>
                <li><span style="color: #79D1B8;">✓</span> Resupply cost & freight analysis</li>
                <li><span style="color: #79D1B8;">✓</span> Export aggregated reports</li>
                <li><span style="color: #79D1B8;">✓</span> Final award laureate approvals</li>
                <li><span style="color: #79D1B8;">✓</span> India-Melbourne strategic planning</li>
              </ul>
            </div>

            <div class="role-story-card">
              <span class="role-badge admin">Super Admin</span>
              <h3 class="role-story-title">System Administrator</h3>
              <ul class="role-permission-list">
                <li><span style="color: #79D1B8;">✓</span> Manage employee credentials</li>
                <li><span style="color: #79D1B8;">✓</span> Configure teams & shifts</li>
                <li><span style="color: #79D1B8;">✓</span> Public holiday & calendar settings</li>
                <li><span style="color: #79D1B8;">✓</span> System audit log inspection</li>
                <li><span style="color: #79D1B8;">✓</span> Data backup & retention rules</li>
                <li class="prohibited"><span>✕</span> Medical details without HR consent</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <!-- SCENE 7: 6-MONTH ROADMAP -->
      <section class="scene-slide" id="scene-slide-6">
        <div class="scene-7-container">
          <div class="scene-eyebrow">Implementation Journey</div>
          <h2 class="scene-title">Proposed Six-Month Development Roadmap</h2>
          
          <div class="roadmap-timeline">
            <div class="roadmap-month-card">
              <div class="month-node">1</div>
              <div class="month-label">MONTH 01</div>
              <div class="month-title">Requirements & Process Mapping</div>
              <div class="month-desc">Catalog sheet-metal orders, flashing categories, CAD workflows, and report formats.</div>
            </div>
            <div class="roadmap-month-card">
              <div class="month-node">2</div>
              <div class="month-label">MONTH 02</div>
              <div class="month-title">Staffing & Attendance Core</div>
              <div class="month-desc">Build employee roster, shift schedules, attendance correction, and confidential leave engine.</div>
            </div>
            <div class="roadmap-month-card">
              <div class="month-node">3</div>
              <div class="month-label">MONTH 03</div>
              <div class="month-title">Production & Keying Modules</div>
              <div class="month-desc">Implement daily production entry, flashings/bits counters, double-checking, and CSV export.</div>
            </div>
            <div class="roadmap-month-card">
              <div class="month-node">4</div>
              <div class="month-label">MONTH 04</div>
              <div class="month-title">Quality & Resupply Intelligence</div>
              <div class="month-desc">Deploy 5-stage case investigation, root cause taxonomy, and restricted loss analytics.</div>
            </div>
            <div class="roadmap-month-card">
              <div class="month-node">5</div>
              <div class="month-label">MONTH 05</div>
              <div class="month-title">Merit & Dual Calendar</div>
              <div class="month-desc">Launch multi-criteria recognition, Melbourne/India holiday synchronization, and night shift logic.</div>
            </div>
            <div class="roadmap-month-card">
              <div class="month-node">6</div>
              <div class="month-label">MONTH 06</div>
              <div class="month-title">Supervised Pilot & Training</div>
              <div class="month-desc">Internal trial with Shift A team, feedback adjustments, user manuals, and executive sign-off.</div>
            </div>
          </div>

          <div style="margin-top: 24px; text-align: center; font-size: 13px; color: var(--gold);">
            Structured academic internship timeline with supervised milestones and zero production risk.
          </div>
        </div>
      </section>

      <!-- SCENE 8: CLOSING EXPERIENCE & PROPOSAL -->
      <section class="scene-slide" id="scene-slide-7">
        <div class="scene-8-container">
          <div class="pulse-dot" style="margin-bottom: 20px; width: 14px; height: 14px;"></div>
          <h1 class="closing-quote-1">BUILT FOR OUR PEOPLE.</h1>
          <h2 class="closing-quote-2">DESIGNED FOR OUR FUTURE.</h2>
          <p class="closing-sub">A clearer picture of every working day.</p>

          <div class="internship-banner">
            <div class="internship-banner-title">PROPOSED MCA FOURTH-SEMESTER INTERNSHIP PROJECT — 2027</div>
            <div class="internship-banner-subtitle">Workforce Operations & Performance Intelligence System</div>
          </div>

          <div class="proposal-asks-grid">
            <div class="ask-box">
              <div class="ask-num">REQUEST 01</div>
              <div class="ask-text">Approval to undertake the development project for official MCA graduation credits.</div>
            </div>
            <div class="ask-box">
              <div class="ask-num">REQUEST 02</div>
              <div class="ask-text">Appointment of a company industry mentor/supervisor for operational guidance.</div>
            </div>
            <div class="ask-box">
              <div class="ask-num">REQUEST 03</div>
              <div class="ask-text">Access to current report templates and anonymized historical operational data.</div>
            </div>
            <div class="ask-box">
              <div class="ask-num">REQUEST 04</div>
              <div class="ask-text">Official internship confirmation letter for college academic committee.</div>
            </div>
            <div class="ask-box">
              <div class="ask-num">REQUEST 05</div>
              <div class="ask-text">Permission to run a supervised, non-disruptive internal pilot in Month 6.</div>
            </div>
          </div>

          <div style="display: flex; gap: 16px;">
            <button class="btn-gold" style="font-size: 15px; padding: 12px 28px;" onclick="switchToProductMode()">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              Launch Interactive Prototype
            </button>
            <button class="btn-outline" style="font-size: 14px; padding: 12px 24px;" onclick="goToScene(0)">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
              Replay Presentation
            </button>
          </div>
        </div>
      </section>

    </main>

    <!-- Bottom Navigation Footer -->
    <footer class="story-footer">
      <div class="nav-keyboard-hint">
        <span><span class="key-badge">←</span> <span class="key-badge">→</span> Navigate</span>
        <span><span class="key-badge">SPACE</span> Next</span>
        <span><span class="key-badge">ESC</span> Overview</span>
      </div>
      <div class="slide-dots" id="slide-dots-container">
        <!-- Generated dynamically via JS -->
      </div>
      <div class="slide-nav-btns">
        <button class="btn-nav" id="btn-prev-scene" onclick="prevScene()" title="Previous Scene">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
        </button>
        <button class="btn-nav" id="btn-next-scene" onclick="nextScene()" title="Next Scene">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
        </button>
      </div>
    </footer>
  </div>


  <!-- =========================================================================
       2. EXPLORE PRODUCT MODE (INTERACTIVE PROTOTYPE APPLICATION)
       ========================================================================= -->
  <div id="product-mode-container" class="hidden">
    <!-- Topbar -->
    <header class="app-topbar">
      <div class="app-brand">
        <span class="pulse-dot"></span>
        <span>PULSE</span>
        <span style="font-size: 11px; font-family: var(--font-sans); color: var(--gold); border: 1px solid var(--gold-border); padding: 2px 8px; border-radius: 4px; margin-left: 8px;">AU-IN OPERATIONS</span>
        <span style="font-size: 10px; font-family: var(--font-mono); color: var(--steel); background: rgba(16, 25, 35, 0.8); border: 1px solid var(--slate-border); padding: 2px 8px; border-radius: 4px; margin-left: 8px; letter-spacing: 0.06em; text-transform: uppercase;">Demonstration Mode</span>
      </div>

      <div class="app-topbar-center">
        <!-- Timezone Switcher -->
        <div class="timezone-pill" onclick="toggleTimezone()" title="Click to toggle timezone display">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          <span id="active-tz-label">IST (India 06:17) / AEDT (Melbourne 11:47)</span>
        </div>

        <!-- Role Switcher -->
        <div class="role-switcher-wrap">
          <span class="role-label">Active Role:</span>
          <select class="role-select" id="role-select" onchange="onRoleChange(this.value)">
            <option value="MANAGEMENT">Management (David Harrison, MD)</option>
            <option value="TEAM_LEADER">Team Leader (Priya Nair, Shift A)</option>
            <option value="EMPLOYEE">Employee (Rohan Sharma, Keying)</option>
            <option value="SUPER_ADMIN">Super Admin (System Admin)</option>
          </select>
        </div>
      </div>

      <div class="app-topbar-right">
        <!-- Reset Demo Data -->
        <button class="btn-header" onclick="resetDemoData()" title="Reset all in-memory changes to initial state">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
          Reset Demo
        </button>

        <!-- User Profile Pill -->
        <div class="user-pill">
          <div class="user-avatar" id="user-avatar-badge">DH</div>
          <div class="user-meta">
            <span class="user-name" id="user-name-display">David Harrison</span>
            <span class="user-role-title" id="user-role-display">Managing Director</span>
          </div>
        </div>

        <!-- Return to Story Presentation -->
        <button class="btn-header primary-action" onclick="switchToStoryMode()">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          Return to Story
        </button>
      </div>
    </header>

    <!-- Workspace (Sidebar + Viewport) -->
    <div class="app-workspace">
      <!-- Navigation Sidebar -->
      <aside class="app-sidebar">
        <div class="nav-section-title">Core Operations</div>
        <ul class="sidebar-menu">
          <li class="menu-item active" onclick="switchView('dashboard')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="9"/><rect x="14" y="3" width="7" height="5"/><rect x="14" y="12" width="7" height="9"/><rect x="3" y="16" width="7" height="5"/></svg>
            <span>Operations Dashboard</span>
          </li>
          <li class="menu-item" onclick="switchView('attendance')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            <span>Attendance & Shifts</span>
            <span class="menu-badge" id="badge-present-count">21</span>
          </li>
          <li class="menu-item" onclick="switchView('leave')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            <span>Leave Management</span>
            <span class="menu-badge alert" id="badge-leave-pending">2 pending</span>
          </li>
          <li class="menu-item" onclick="switchView('production')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
            <span>Daily Production Entry</span>
          </li>
          <li class="menu-item" onclick="switchView('quality')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span>Quality & Resupply</span>
            <span class="menu-badge alert" id="badge-quality-active">2 active</span>
          </li>
        </ul>

        <div class="nav-section-title" style="margin-top: 18px;">Culture & Alignment</div>
        <ul class="sidebar-menu">
          <li class="menu-item" onclick="switchView('recognition')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>
            <span>Recognition & Merit</span>
          </li>
          <li class="menu-item" onclick="switchView('calendar')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            <span>Operations Calendar</span>
          </li>
          <li class="menu-item" onclick="switchView('roles')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8z"/><path d="M12 6a4 4 0 1 0 4 4 4 4 0 0 0-4-4z"/></svg>
            <span>Roles & Access Matrix</span>
          </li>
        </ul>

        <div style="margin-top: auto; padding: 16px 20px; border-top: 1px solid var(--slate-border); font-size: 11px; color: var(--steel-dim);">
          <div style="color: var(--gold); margin-bottom: 4px;">PULSE DEMONSTRATOR</div>
          <div>In-Memory Reactive State</div>
          <div style="margin-top: 2px;">Offline Capable Prototype</div>
        </div>
      </aside>

      <!-- Main Application Viewport -->
      <main class="app-viewport">

        <!-- VIEW 1: DASHBOARD -->
        <div class="view-panel active" id="view-dashboard">
          <div class="view-header">
            <div class="view-title-group">
              <h2>Operations Overview</h2>
              <div class="view-subtitle">Consolidated operational intelligence across India sheet-metal keying and Melbourne fabrication.</div>
            </div>
            <div class="view-actions">
              <select class="pulse-select" style="width: 170px;" onchange="filterDashboardShift(this.value)">
                <option value="ALL">All Shifts (A, B, C)</option>
                <option value="Shift A">Shift A (Day: 06:00–14:30)</option>
                <option value="Shift B">Shift B (Afternoon: 14:00–22:30)</option>
                <option value="Shift C">Shift C (Night: 22:00–06:30)</option>
              </select>
              <button class="btn-gold btn-sm" onclick="openProductionModal()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
                Record Shift Entry
              </button>
            </div>
          </div>

          <!-- Top KPI Metrics Row -->
          <div class="kpi-row">
            <div class="kpi-card">
              <div class="kpi-label">Total Workforce</div>
              <div class="kpi-value" id="kpi-total-emp">24</div>
              <div class="kpi-meta">3 Dedicated Keying Teams</div>
            </div>
            <div class="kpi-card">
              <div class="kpi-label">Present Today</div>
              <div class="kpi-value" style="color: #79D1B8;" id="kpi-present-count">21</div>
              <div class="kpi-meta trend-up">87.5% On Shift Roster</div>
            </div>
            <div class="kpi-card">
              <div class="kpi-label">Orders Keyed</div>
              <div class="kpi-value" id="kpi-orders-count">184</div>
              <div class="kpi-meta trend-up">↑ 6% vs Last Week</div>
            </div>
            <div class="kpi-card">
              <div class="kpi-label">Flashings & Bits</div>
              <div class="kpi-value" style="color: var(--gold);" id="kpi-flashings-count">1,630</div>
              <div class="kpi-meta">1,248 Flashings / 382 Bits</div>
            </div>
            <div class="kpi-card">
              <div class="kpi-label">Quality Accuracy</div>
              <div class="kpi-value" id="kpi-quality-rate">99.4%</div>
              <div class="kpi-meta">179 Double-Checks Logged</div>
            </div>
          </div>

          <!-- Production Trend Chart & Team Leaderboard -->
          <div class="grid-2col">
            <!-- Trend SVG Chart -->
            <div class="dashboard-card">
              <div class="card-title-bar">
                <span class="card-title">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
                  7-Day Production Velocity (Flashings & Trims Keyed)
                </span>
                <span style="font-family: var(--font-mono); font-size: 11px; color: var(--gold);">Average: 1,480 units/day</span>
              </div>
              <div style="height: 220px; width: 100%; position: relative;">
                <svg width="100%" height="100%" viewBox="0 0 600 200" preserveAspectRatio="none">
                  <defs>
                    <linearGradient id="chartGrad" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="0%" stop-color="#C6A675" stop-opacity="0.25"/>
                      <stop offset="100%" stop-color="#C6A675" stop-opacity="0.0"/>
                    </linearGradient>
                  </defs>
                  <!-- Horizontal Gridlines -->
                  <line x1="0" y1="40" x2="600" y2="40" stroke="rgba(147, 163, 174, 0.1)" stroke-width="1"/>
                  <line x1="0" y1="90" x2="600" y2="90" stroke="rgba(147, 163, 174, 0.1)" stroke-width="1"/>
                  <line x1="0" y1="140" x2="600" y2="140" stroke="rgba(147, 163, 174, 0.1)" stroke-width="1"/>
                  <!-- Area Fill -->
                  <path d="M 40 150 L 120 120 L 200 135 L 280 80 L 360 95 L 440 60 L 520 40 L 520 190 L 40 190 Z" fill="url(#chartGrad)" />
                  <!-- Line Stroke -->
                  <path d="M 40 150 L 120 120 L 200 135 L 280 80 L 360 95 L 440 60 L 520 40" stroke="#C6A675" stroke-width="3" fill="none" stroke-linecap="round"/>
                  <!-- Data Dots -->
                  <circle cx="40" cy="150" r="4" fill="#C6A675" />
                  <circle cx="120" cy="120" r="4" fill="#C6A675" />
                  <circle cx="200" cy="135" r="4" fill="#C6A675" />
                  <circle cx="280" cy="80" r="4" fill="#C6A675" />
                  <circle cx="360" cy="95" r="4" fill="#C6A675" />
                  <circle cx="440" cy="60" r="4" fill="#C6A675" />
                  <circle cx="520" cy="40" r="5" fill="#FFFFFF" stroke="#C6A675" stroke-width="2" />
                  <!-- Labels -->
                  <text x="35" y="185" fill="#93A3AE" font-size="10" font-family="monospace">Thu</text>
                  <text x="115" y="185" fill="#93A3AE" font-size="10" font-family="monospace">Fri</text>
                  <text x="195" y="185" fill="#93A3AE" font-size="10" font-family="monospace">Sat</text>
                  <text x="275" y="185" fill="#93A3AE" font-size="10" font-family="monospace">Mon</text>
                  <text x="355" y="185" fill="#93A3AE" font-size="10" font-family="monospace">Tue</text>
                  <text x="435" y="185" fill="#93A3AE" font-size="10" font-family="monospace">Wed</text>
                  <text x="510" y="185" fill="#C6A675" font-size="10" font-family="monospace" font-weight="bold">Today</text>
                </svg>
              </div>
            </div>

            <!-- Team Performance Leaderboard -->
            <div class="dashboard-card">
              <div class="card-title-bar">
                <span class="card-title">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
                  Keying Team Velocity
                </span>
                <span style="font-size: 11px; color: var(--steel);">Shift SLA: 99.5%</span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 14px;">
                <div style="background: rgba(16, 25, 35, 0.4); padding: 12px; border-radius: 6px; border: 1px solid var(--slate-border);">
                  <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-weight: 600; color: var(--porcelain);">Team Alpha (Flashings & Trims)</span>
                    <span style="color: var(--gold); font-family: var(--font-mono);">99.4% Acc</span>
                  </div>
                  <div style="font-size: 11px; color: var(--steel); margin-bottom: 6px;">Lead: Priya Nair | 10 Keyers | 82 Orders Keyed Today</div>
                  <div style="width: 100%; height: 6px; background: rgba(147, 163, 174, 0.15); border-radius: 3px;">
                    <div style="width: 92%; height: 100%; background: var(--gold); border-radius: 3px;"></div>
                  </div>
                </div>

                <div style="background: rgba(16, 25, 35, 0.4); padding: 12px; border-radius: 6px; border: 1px solid var(--slate-border);">
                  <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-weight: 600; color: var(--porcelain);">Team Beta (Architectural Panels)</span>
                    <span style="color: var(--gold); font-family: var(--font-mono);">99.1% Acc</span>
                  </div>
                  <div style="font-size: 11px; color: var(--steel); margin-bottom: 6px;">Lead: Pooja Gupta | 8 Detailers | 64 Orders Keyed Today</div>
                  <div style="width: 100%; height: 6px; background: rgba(147, 163, 174, 0.15); border-radius: 3px;">
                    <div style="width: 84%; height: 100%; background: var(--emerald); border-radius: 3px;"></div>
                  </div>
                </div>

                <div style="background: rgba(16, 25, 35, 0.4); padding: 12px; border-radius: 6px; border: 1px solid var(--slate-border);">
                  <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-weight: 600; color: var(--porcelain);">Team Gamma (Double-Check & Audit)</span>
                    <span style="color: #79D1B8; font-family: var(--font-mono);">99.9% Acc</span>
                  </div>
                  <div style="font-size: 11px; color: var(--steel); margin-bottom: 6px;">Lead: Manoj Tiwari | 6 Auditors | 179 Orders Double-Checked</div>
                  <div style="width: 100%; height: 6px; background: rgba(147, 163, 174, 0.15); border-radius: 3px;">
                    <div style="width: 97%; height: 100%; background: #79D1B8; border-radius: 3px;"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Bottom Row: Quality Alert & Live Feed -->
          <div class="grid-2col">
            <!-- Active Resupply Case Radar -->
            <div class="dashboard-card">
              <div class="card-title-bar">
                <span class="card-title">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
                  Operational Quality & Resupply Cases
                </span>
                <span class="badge-status-red" style="font-size: 10px;">2 Active Cases</span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 10px;" id="dashboard-quality-list">
                <!-- Dynamically rendered -->
              </div>
            </div>

            <!-- Recent Activity Feed -->
            <div class="dashboard-card">
              <div class="card-title-bar">
                <span class="card-title">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                  Recent Operations Feed
                </span>
                <span style="font-family: var(--font-mono); font-size: 11px; color: var(--steel);">Live Logs</span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 8px;" id="dashboard-feed-list">
                <div style="font-size: 12px; padding: 6px 0; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--gold); font-family: var(--font-mono);">06:02 AM</span> — Rajesh Kumar logged 24 orders (Team Alpha)
                </div>
                <div style="font-size: 12px; padding: 6px 0; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--gold); font-family: var(--font-mono);">05:58 AM</span> — Ananya Sen completed 27 double-checks for Melbourne facade job
                </div>
                <div style="font-size: 12px; padding: 6px 0; border-bottom: 1px solid rgba(147, 163, 174, 0.1);">
                  <span style="color: var(--gold); font-family: var(--font-mono);">05:48 AM</span> — Shift A morning briefing completed by Priya Nair
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- VIEW 2: ATTENDANCE & SHIFTS -->
        <div class="view-panel" id="view-attendance">
          <div class="view-header">
            <div class="view-title-group">
              <h2>Workforce Attendance Register</h2>
              <div class="view-subtitle">Live status tracking, shift assignments, and authorized attendance corrections.</div>
            </div>
            <div class="view-actions">
              <input type="text" class="pulse-input" placeholder="Search employee..." style="width: 200px;" id="attendance-search" oninput="renderAttendanceTable()">
              <select class="pulse-select" style="width: 160px;" id="attendance-filter-status" onchange="renderAttendanceTable()">
                <option value="ALL">All Statuses</option>
                <option value="Present">Present (21)</option>
                <option value="Approved Leave">On Leave (2)</option>
                <option value="Late">Late (1)</option>
                <option value="Absent">Absent (1)</option>
              </select>
              <button class="btn-outline btn-sm" onclick="openAttendanceCorrectionModal()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
                Log Correction
              </button>
            </div>
          </div>

          <div class="table-container">
            <table class="pulse-table">
              <thead>
                <tr>
                  <th>Employee</th>
                  <th>Team & Role</th>
                  <th>Assigned Shift</th>
                  <th>Check-In</th>
                  <th>Keying Accuracy</th>
                  <th>Status</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody id="attendance-tbody">
                <!-- Dynamically populated -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- VIEW 3: LEAVE MANAGEMENT -->
        <div class="view-panel" id="view-leave">
          <div class="view-header">
            <div class="view-title-group">
              <h2>Leave & Staffing Management</h2>
              <div class="view-subtitle">Confidential leave submissions, supervisory approvals, and public team availability.</div>
            </div>
            <div class="view-actions">
              <button class="btn-gold btn-sm" onclick="openApplyLeaveModal()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
                Apply for Leave
              </button>
            </div>
          </div>

          <!-- Pending Approvals Section (Team Leader & Management) -->
          <div class="dashboard-card" style="margin-bottom: 24px;" id="leave-pending-container">
            <div class="card-title-bar">
              <span class="card-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                Pending Shift Approvals (Supervisory Action Required)
              </span>
              <span class="badge-status-red" id="leave-pending-badge">2 Requests Pending</span>
            </div>
            <div class="table-container">
              <table class="pulse-table">
                <thead>
                  <tr>
                    <th>Request ID</th>
                    <th>Employee</th>
                    <th>Team</th>
                    <th>Leave Type</th>
                    <th>Dates</th>
                    <th>Days</th>
                    <th>Confidential Reason</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody id="leave-pending-tbody">
                  <!-- Rendered dynamically -->
                </tbody>
              </table>
            </div>
          </div>

          <!-- Public Team Availability Calendar -->
          <div class="dashboard-card">
            <div class="card-title-bar">
              <span class="card-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
                Public Team Availability Schedule (General Staff View)
              </span>
              <span style="font-size: 11px; color: var(--emerald);">Privacy Mask Active: Medical and Personal Details Redacted</span>
            </div>
            <div class="table-container">
              <table class="pulse-table">
                <thead>
                  <tr>
                    <th>Employee</th>
                    <th>Department</th>
                    <th>Dates Away</th>
                    <th>Coverage Status</th>
                    <th>Public Availability</th>
                  </tr>
                </thead>
                <tbody id="leave-approved-tbody">
                  <!-- Rendered dynamically -->
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- VIEW 4: DAILY PRODUCTION ENTRY -->
        <div class="view-panel" id="view-production">
          <div class="view-header">
            <div class="view-title-group">
              <h2>Daily Production Entry</h2>
              <div class="view-subtitle">High-velocity shift keying logs for flashings, custom bits, and double-checking audits.</div>
            </div>
            <div class="view-actions">
              <button class="btn-outline btn-sm" onclick="exportProductionCSV()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                Export CSV Report
              </button>
              <button class="btn-gold btn-sm" onclick="openProductionModal()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
                New Entry
              </button>
            </div>
          </div>

          <!-- Historical Production Table -->
          <div class="table-container">
            <table class="pulse-table">
              <thead>
                <tr>
                  <th>Record ID</th>
                  <th>Date</th>
                  <th>Keying Specialist</th>
                  <th>Team</th>
                  <th>Shift</th>
                  <th>Orders</th>
                  <th>Flashings</th>
                  <th>Bits</th>
                  <th>Double-Checks</th>
                  <th>Remarks</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody id="production-tbody">
                <!-- Dynamically rendered -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- VIEW 5: QUALITY & RESUPPLY INTELLIGENCE -->
        <div class="view-panel" id="view-quality">
          <div class="view-header">
            <div class="view-title-group">
              <h2>Quality & Resupply Intelligence</h2>
              <div class="view-subtitle">Objective 5-stage case investigation separating drafting ambiguities from manufacturing tolerances.</div>
            </div>
            <div class="view-actions">
              <span class="badge-status-green" style="font-size: 11px;">Zero-Blame Quality Policy Active</span>
            </div>
          </div>

          <!-- Quality Case Master-Detail Layout -->
          <div class="grid-2col">
            <!-- Case List -->
            <div class="dashboard-card">
              <div class="card-title-bar">
                <span class="card-title">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
                  Investigation Queue
                </span>
                <span style="font-size: 11px; color: var(--steel);">Select case to inspect</span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 10px;" id="quality-cases-list">
                <!-- Dynamically populated -->
              </div>
            </div>

            <!-- Case Detail & Stepper -->
            <div class="dashboard-card" id="quality-detail-pane">
              <div class="card-title-bar">
                <span class="card-title" id="qc-detail-id">Case #QC-2027-084</span>
                <span class="badge-status-red" id="qc-detail-category">Dimension Mismatch</span>
              </div>

              <!-- 5-Stage Stepper -->
              <div class="stepper-container">
                <div class="stepper-line">
                  <div class="stepper-line-fill" id="qc-stepper-fill" style="width: 25%;"></div>
                </div>
                <div class="step-item" id="qc-step-0" onclick="setQualityStage(0)">
                  <div class="step-circle">1</div>
                  <span class="step-title">Reported</span>
                </div>
                <div class="step-item active" id="qc-step-1" onclick="setQualityStage(1)">
                  <div class="step-circle">2</div>
                  <span class="step-title">Investigating</span>
                </div>
                <div class="step-item" id="qc-step-2" onclick="setQualityStage(2)">
                  <div class="step-circle">3</div>
                  <span class="step-title">Root Cause</span>
                </div>
                <div class="step-item" id="qc-step-3" onclick="setQualityStage(3)">
                  <div class="step-circle">4</div>
                  <span class="step-title">Action</span>
                </div>
                <div class="step-item" id="qc-step-4" onclick="setQualityStage(4)">
                  <div class="step-circle">5</div>
                  <span class="step-title">Closed</span>
                </div>
              </div>

              <!-- Case Specifications & Evidence -->
              <div style="background: rgba(16, 25, 35, 0.4); padding: 14px; border-radius: 6px; border: 1px solid var(--slate-border); margin-bottom: 14px;">
                <div style="font-size: 11px; font-family: var(--font-mono); color: var(--steel); margin-bottom: 2px;">ORDER & CLIENT SPECIFICATION</div>
                <div style="font-weight: 600; color: var(--porcelain); margin-bottom: 4px;" id="qc-detail-spec">Ridge Flashing 0.55mm Colorbond Monument (L: 3200mm, Girth: 450mm)</div>
                <div style="font-size: 12px; color: var(--steel);" id="qc-detail-client">Client: Melbourne Roofing & Facades Pty Ltd | Order: ORD-AU-89421</div>
              </div>

              <div style="margin-bottom: 14px;">
                <div style="font-size: 11px; font-family: var(--font-mono); color: var(--gold); margin-bottom: 4px;">REPORTED SITE ISSUE</div>
                <div style="font-size: 13px; color: var(--porcelain); line-height: 1.4;" id="qc-detail-problem">
                  Length variance (+35mm over length on bend 3) discovered during site dry-fit in Dandenong South.
                </div>
              </div>

              <!-- Root Cause Selector -->
              <div class="form-group" style="margin-bottom: 16px;">
                <label class="form-label">Verified Root Cause Category</label>
                <select class="pulse-select" id="qc-root-cause-select" onchange="onRootCauseChange(this.value)">
                  <option value="Unclear customer drawing">Unclear customer drawing (Markup clash)</option>
                  <option value="Keying oversight">Keying oversight (Digit transposition)</option>
                  <option value="Checking oversight">Checking oversight (Auditor variance)</option>
                  <option value="Customer spec change">Customer spec change (Site revision post-release)</option>
                  <option value="Machine calibration tolerance">Machine calibration tolerance (Brake press fold)</option>
                </select>
              </div>

              <!-- Financial Impact (Restricted to Management/Admin) -->
              <div id="qc-financial-impact-box" style="background: rgba(198, 166, 117, 0.08); border: 1px solid var(--gold-border); border-radius: 6px; padding: 12px; margin-bottom: 16px;">
                <div style="font-family: var(--font-mono); font-size: 11px; color: var(--gold); margin-bottom: 4px;">FINANCIAL LOSS IMPACT (MANAGEMENT CONFIDENTIAL)</div>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; font-size: 12px;">
                  <div>Material: <span style="font-weight: 600; color: var(--porcelain);" id="qc-loss-mat">$145 AUD</span></div>
                  <div>Labour: <span style="font-weight: 600; color: var(--porcelain);" id="qc-loss-lab">$60 AUD</span></div>
                  <div>Freight: <span style="font-weight: 600; color: var(--porcelain);" id="qc-loss-fre">$75 AUD</span></div>
                </div>
              </div>

              <div style="display: flex; justify-content: flex-end; gap: 10px;">
                <button class="btn-outline btn-sm" onclick="advanceQualityCaseStage()">
                  Advance Next Stage →
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- VIEW 6: RECOGNITION & MERIT -->
        <div class="view-panel" id="view-recognition">
          <div class="view-header">
            <div class="view-title-group">
              <h2>Recognition & Operational Merit</h2>
              <div class="view-subtitle">Balanced criteria celebrating quality, speed, complexity, and team collaboration.</div>
            </div>
            <div class="view-actions">
              <button class="btn-gold btn-sm" onclick="openNominationModal()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>
                Nominate Teammate
              </button>
            </div>
          </div>

          <!-- 4 Editorial Award Laureate Cards -->
          <div class="awards-grid" id="awards-grid-container">
            <!-- Dynamically populated -->
          </div>

          <!-- Merit Policy Explainer -->
          <div class="dashboard-card">
            <div class="card-title-bar">
              <span class="card-title">Recognition Framework & Transparency Standards</span>
              <span style="font-size: 11px; color: var(--gold);">Anti-Shaming & Anti-Gaming Policy</span>
            </div>
            <p style="font-size: 13px; color: var(--steel); line-height: 1.5;">
              Pulse evaluates performance comprehensively: raw volume alone never guarantees an award. Specialists tackling custom, low-tolerance complex architectural flashings are weighted equitably alongside high-volume standard profiles. Quality checks, double-checking diligence, and cross-team collaboration are primary scoring pillars.
            </p>
          </div>
        </div>

        <!-- VIEW 7: OPERATIONS CALENDAR -->
        <div class="view-panel" id="view-calendar">
          <div class="view-header">
            <div class="view-title-group">
              <h2>Cross-Border Operations Calendar</h2>
              <div class="view-subtitle">Synchronizing India shifts with Victoria (Melbourne) public holidays and fabrication delivery deadlines.</div>
            </div>
            <div class="view-actions">
              <button class="btn-outline btn-sm" onclick="toggleCalendarTimezone()">
                Switch Timezone (IST ⇄ Melbourne)
              </button>
            </div>
          </div>

          <div class="calendar-container">
            <div class="calendar-nav-bar">
              <h3 style="font-size: 18px; color: var(--porcelain);" id="cal-month-title">March 2027 — Shift & Delivery Schedule</h3>
              <div style="font-family: var(--font-mono); font-size: 12px; color: var(--gold);">
                Melbourne Fabrication: Victoria Active
              </div>
            </div>

            <div class="calendar-days-header">
              <span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Sat</span><span>Sun</span>
            </div>

            <div class="calendar-grid-cells" id="calendar-cells-grid">
              <!-- Dynamically populated 31 calendar day cells -->
            </div>
          </div>
        </div>

        <!-- VIEW 8: ROLES & ACCESS MATRIX -->
        <div class="view-panel" id="view-roles">
          <div class="view-header">
            <div class="view-title-group">
              <h2>Roles & Permission Architecture</h2>
              <div class="view-subtitle">Strict boundary matrices protecting employee confidentiality and operational accountability.</div>
            </div>
          </div>

          <div class="dashboard-card" style="margin-bottom: 24px;">
            <div class="table-container">
              <table class="pulse-table">
                <thead>
                  <tr>
                    <th>Operational Capability</th>
                    <th>Employee (Keying)</th>
                    <th>Team Leader (Supervisor)</th>
                    <th>Management (MD)</th>
                    <th>Super Admin</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>View Personal Shift Attendance</td>
                    <td><span style="color: #79D1B8;">Full Access</span></td>
                    <td><span style="color: #79D1B8;">Full Access</span></td>
                    <td><span style="color: #79D1B8;">Full Access</span></td>
                    <td><span style="color: #79D1B8;">Full Access</span></td>
                  </tr>
                  <tr>
                    <td>Submit Shift Daily Production Logs</td>
                    <td><span style="color: #E68280;">Prohibited</span></td>
                    <td><span style="color: #79D1B8;">Authorized (Assigned Shift)</span></td>
                    <td><span style="color: var(--steel);">Audit View</span></td>
                    <td><span style="color: var(--steel);">Technical View</span></td>
                  </tr>
                  <tr>
                    <td>Approve / Reject Leave Requests</td>
                    <td><span style="color: #E68280;">Prohibited</span></td>
                    <td><span style="color: #79D1B8;">Authorized (Team)</span></td>
                    <td><span style="color: #79D1B8;">Executive Override</span></td>
                    <td><span style="color: #E68280;">Prohibited</span></td>
                  </tr>
                  <tr>
                    <td>View Private Medical / Personal Leave Details</td>
                    <td><span style="color: #79D1B8;">Own Only</span></td>
                    <td><span style="color: #79D1B8;">Direct Reports</span></td>
                    <td><span style="color: #79D1B8;">Executive HR Access</span></td>
                    <td><span style="color: #E68280;">Redacted (Privacy Rule)</span></td>
                  </tr>
                  <tr>
                    <td>Inspect Resupply Financial Loss ($ AUD)</td>
                    <td><span style="color: #E68280;">Hidden</span></td>
                    <td><span style="color: #E68280;">Hidden</span></td>
                    <td><span style="color: #79D1B8;">Full Access</span></td>
                    <td><span style="color: #79D1B8;">Full Access</span></td>
                  </tr>
                  <tr>
                    <td>System Configuration & Role Assignment</td>
                    <td><span style="color: #E68280;">Prohibited</span></td>
                    <td><span style="color: #E68280;">Prohibited</span></td>
                    <td><span style="color: #E68280;">Prohibited</span></td>
                    <td><span style="color: #79D1B8;">Full Authority</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

      </main>
    </div>
  </div>


  <!-- =========================================================================
       MODALS & DIALOGS
       ========================================================================= -->

  <!-- Modal: Apply for Leave -->
  <div class="modal-backdrop" id="modal-apply-leave">
    <div class="modal-box">
      <div class="modal-header">
        <h3 class="modal-title">Apply for Leave</h3>
        <button class="modal-close" onclick="closeModal('modal-apply-leave')">✕</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label">Employee</label>
          <select class="pulse-select" id="leave-form-emp">
            <!-- Populated via JS -->
          </select>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label class="form-label">Leave Type</label>
            <select class="pulse-select" id="leave-form-type">
              <option value="Casual Leave">Casual Leave</option>
              <option value="Medical Leave">Medical Leave</option>
              <option value="Annual Leave">Annual Leave</option>
              <option value="Comp-Off">Compensatory Off</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">Duration (Days)</label>
            <input type="number" class="pulse-input" id="leave-form-days" min="1" max="14" value="1">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Date Range</label>
          <input type="text" class="pulse-input" id="leave-form-dates" placeholder="e.g. 2027-03-28 to 2027-03-29" value="2027-03-28">
        </div>
        <div class="form-group">
          <label class="form-label">Private Reason (Confidential to Approvers)</label>
          <textarea class="pulse-textarea" id="leave-form-reason" rows="3" placeholder="Enter reason for leave..."></textarea>
          <span style="font-size: 11px; color: var(--steel-dim); margin-top: 4px;">Protected by Pulse HR Privacy Engine: general peers will only see you marked as 'On Leave'.</span>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn-outline" onclick="closeModal('modal-apply-leave')">Cancel</button>
        <button class="btn-gold" onclick="submitLeaveApplication()">Submit Application</button>
      </div>
    </div>
  </div>

  <!-- Modal: Record Shift Daily Production -->
  <div class="modal-backdrop" id="modal-production-entry">
    <div class="modal-box">
      <div class="modal-header">
        <h3 class="modal-title">Log Daily Production Entry</h3>
        <button class="modal-close" onclick="closeModal('modal-production-entry')">✕</button>
      </div>
      <div class="modal-body">
        <div class="form-row">
          <div class="form-group">
            <label class="form-label">Keying Specialist</label>
            <select class="pulse-select" id="prod-form-emp">
              <!-- Populated via JS -->
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">Shift</label>
            <select class="pulse-select" id="prod-form-shift">
              <option value="Shift A">Shift A (Day: 06:00–14:30)</option>
              <option value="Shift B">Shift B (Afternoon: 14:00–22:30)</option>
              <option value="Shift C">Shift C (Night: 22:00–06:30)</option>
            </select>
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label class="form-label">Orders Keyed</label>
            <input type="number" class="pulse-input" id="prod-form-orders" value="25" min="1" max="100">
          </div>
          <div class="form-group">
            <label class="form-label">Flashings Keyed</label>
            <input type="number" class="pulse-input" id="prod-form-flashings" value="175" min="1" max="600">
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label class="form-label">Custom Bits Processed</label>
            <input type="number" class="pulse-input" id="prod-form-bits" value="48" min="0" max="200">
          </div>
          <div class="form-group">
            <label class="form-label">Double-Checks Completed</label>
            <input type="number" class="pulse-input" id="prod-form-doublechecks" value="24" min="0" max="100">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Technical Notes / Remarks</label>
          <input type="text" class="pulse-input" id="prod-form-remarks" placeholder="e.g. Completed Colorbond ridge flashings with 4 bends" value="Colorbond Monument ridge flashings keyed accurately">
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn-outline" onclick="closeModal('modal-production-entry')">Cancel</button>
        <button class="btn-gold" onclick="submitProductionReport()">Submit & Verify Log</button>
      </div>
    </div>
  </div>

  <!-- Modal: Attendance Correction -->
  <div class="modal-backdrop" id="modal-attendance-correction">
    <div class="modal-box">
      <div class="modal-header">
        <h3 class="modal-title">Authorized Attendance Correction</h3>
        <button class="modal-close" onclick="closeModal('modal-attendance-correction')">✕</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label">Employee</label>
          <select class="pulse-select" id="att-correct-emp">
            <!-- Populated via JS -->
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Updated Status</label>
          <select class="pulse-select" id="att-correct-status">
            <option value="Present">Present</option>
            <option value="Approved Leave">Approved Leave</option>
            <option value="Late">Late Arrival</option>
            <option value="Half-day">Half-day</option>
            <option value="Absent">Absent</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Reason for Administrative Correction</label>
          <input type="text" class="pulse-input" id="att-correct-reason" placeholder="e.g. Biometric reader sync delay" value="Authorized biometric delay adjustment">
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn-outline" onclick="closeModal('modal-attendance-correction')">Cancel</button>
        <button class="btn-gold" onclick="saveAttendanceCorrection()">Update Attendance</button>
      </div>
    </div>
  </div>

  <!-- Modal: Nominate Teammate for Recognition -->
  <div class="modal-backdrop" id="modal-nominate">
    <div class="modal-box">
      <div class="modal-header">
        <h3 class="modal-title">Nominate for Operational Recognition</h3>
        <button class="modal-close" onclick="closeModal('modal-nominate')">✕</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label">Nominee</label>
          <select class="pulse-select" id="nom-form-emp">
            <!-- Populated via JS -->
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Award Category</label>
          <select class="pulse-select" id="nom-form-category">
            <option value="Employee of the Day">Employee of the Day</option>
            <option value="Employee of the Week">Employee of the Week</option>
            <option value="Employee of the Month">Employee of the Month</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Operational Justification</label>
          <textarea class="pulse-textarea" id="nom-form-reason" rows="3" placeholder="Describe quality accuracy, complexity handled, or teamwork displayed..."></textarea>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn-outline" onclick="closeModal('modal-nominate')">Cancel</button>
        <button class="btn-gold" onclick="submitNomination()">Submit Nomination</button>
      </div>
    </div>
  </div>

  <!-- Modal: Presentation Scene Grid Menu -->
  <div class="modal-backdrop" id="modal-scene-menu">
    <div class="modal-box" style="width: 720px;">
      <div class="modal-header">
        <h3 class="modal-title">Presentation Scene Menu</h3>
        <button class="modal-close" onclick="closeModal('modal-scene-menu')">✕</button>
      </div>
      <div class="modal-body">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;" id="scene-menu-grid">
          <!-- Dynamically populated -->
        </div>
      </div>
    </div>
  </div>

  <!-- Toast Container -->
  <div class="toast-container" id="toast-container"></div>



  <!-- =========================================================================
       3. JAVASCRIPT STATE ENGINE & INTERACTION LOGIC
       ========================================================================= -->
  <script>
    // In-memory master state loaded from pre-compiled JSON
    const MASTER_DATA = __INITIAL_DATA_PLACEHOLDER__;
    let appState = JSON.parse(JSON.stringify(MASTER_DATA));

    // Runtime state variables
    let currentMode = 'STORY'; // 'STORY' | 'PRODUCT'
    let currentScene = 0;
    const TOTAL_SCENES = 8;
    const sceneTitles = [
      "Opening: Every Shift Tells a Story",
      "The Existing Problem: Scattered Information",
      "The Product Reveal: PULSE",
      "Core Capabilities: Four Operational Pillars",
      "Before & After: Operational Transformation",
      "Governance: Role-Based Privacy Boundaries",
      "Implementation Roadmap: Six-Month Journey",
      "Closing & Internship Proposal"
    ];

    let currentRole = 'MANAGEMENT'; // 'EMPLOYEE' | 'TEAM_LEADER' | 'MANAGEMENT' | 'SUPER_ADMIN'
    let currentTimezone = 'IST'; // 'IST' | 'AEDT'
    let activeQualityCaseId = 'QC-2027-084';

    // Initialize on page load
    window.addEventListener('DOMContentLoaded', () => {
      initStoryDots();
      populateDropdowns();
      renderAllViews();
      setupKeyboardNavigation();
    });

    /* ==========================================================================
       PRESENTATION NAVIGATION LOGIC (STORY MODE)
       ========================================================================== */
    function initStoryDots() {
      const container = document.getElementById('slide-dots-container');
      container.innerHTML = '';
      for (let i = 0; i < TOTAL_SCENES; i++) {
        const dot = document.createElement('div');
        dot.className = `slide-dot ${i === 0 ? 'active' : ''}`;
        dot.onclick = () => goToScene(i);
        container.appendChild(dot);
      }
    }

    function updateSceneDisplay() {
      // Update scene slides
      for (let i = 0; i < TOTAL_SCENES; i++) {
        const slide = document.getElementById(`scene-slide-${i}`);
        if (slide) {
          slide.classList.toggle('active', i === currentScene);
        }
      }

      // Update dots
      const dots = document.querySelectorAll('.slide-dot');
      dots.forEach((dot, index) => {
        dot.classList.toggle('active', index === currentScene);
      });

      // Update counter & progress bar
      const counter = document.getElementById('scene-counter-display');
      if (counter) {
        counter.textContent = `SCENE 0${currentScene + 1} / 0${TOTAL_SCENES}`;
      }
      const progressFill = document.getElementById('story-progress-fill');
      if (progressFill) {
        progressFill.style.width = `${((currentScene + 1) / TOTAL_SCENES) * 100}%`;
      }

      // Update nav buttons disabled state
      const btnPrev = document.getElementById('btn-prev-scene');
      const btnNext = document.getElementById('btn-next-scene');
      if (btnPrev) btnPrev.disabled = (currentScene === 0);
      if (btnNext) btnNext.disabled = (currentScene === TOTAL_SCENES - 1);
    }

    function goToScene(index) {
      if (index >= 0 && index < TOTAL_SCENES) {
        currentScene = index;
        updateSceneDisplay();
      }
    }

    function nextScene() {
      if (currentScene < TOTAL_SCENES - 1) {
        goToScene(currentScene + 1);
      }
    }

    function prevScene() {
      if (currentScene > 0) {
        goToScene(currentScene - 1);
      }
    }

    function toggleFullscreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => {
          showToast(`Fullscreen notice: ${err.message}`);
        });
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        }
      }
    }

    function openSceneModal() {
      const grid = document.getElementById('scene-menu-grid');
      grid.innerHTML = '';
      sceneTitles.forEach((title, idx) => {
        const item = document.createElement('div');
        item.style.cssText = `
          padding: 12px;
          background: ${idx === currentScene ? 'var(--gold-dim)' : 'rgba(24, 38, 49, 0.5)'};
          border: 1px solid ${idx === currentScene ? 'var(--gold)' : 'var(--slate-border)'};
          border-radius: 6px;
          cursor: pointer;
          transition: all 0.2s;
        `;
        item.innerHTML = `
          <div style="font-family: var(--font-mono); font-size: 10px; color: var(--gold); margin-bottom: 4px;">SCENE 0${idx + 1}</div>
          <div style="font-size: 13px; font-weight: 500; color: var(--porcelain);">${title}</div>
        `;
        item.onclick = () => {
          goToScene(idx);
          closeModal('modal-scene-menu');
        };
        grid.appendChild(item);
      });
      openModal('modal-scene-menu');
    }

    function toggleConsolidateSheets() {
      const stage = document.getElementById('sheets-stage-container');
      stage.classList.toggle('sheets-consolidated');
      showToast(stage.classList.contains('sheets-consolidated') ? 
        'Information unified into single operational hub' : 
        'Demonstrating fragmented reporting silos');
    }

    function setupKeyboardNavigation() {
      document.addEventListener('keydown', (e) => {
        // If typing in input or textarea, don't trigger slides
        if (['INPUT', 'TEXTAREA', 'SELECT'].includes(e.target.tagName)) return;

        if (currentMode === 'STORY') {
          if (e.key === 'ArrowRight' || e.key === ' ') {
            e.preventDefault();
            nextScene();
          } else if (e.key === 'ArrowLeft') {
            e.preventDefault();
            prevScene();
          } else if (e.key === 'Escape') {
            e.preventDefault();
            openSceneModal();
          }
        } else if (currentMode === 'PRODUCT') {
          if (e.key === 'Escape') {
            switchToStoryMode();
          }
        }
      });
    }

    /* ==========================================================================
       MODE SWITCHING (STORY ⇄ PRODUCT)
       ========================================================================== */
    function switchToProductMode() {
      currentMode = 'PRODUCT';
      document.getElementById('story-mode-container').classList.add('hidden');
      document.getElementById('product-mode-container').classList.remove('hidden');
      renderAllViews();
      showToast('Switched to Explore Product Mode: Live Interactive Prototype');
    }

    function switchToStoryMode() {
      currentMode = 'STORY';
      document.getElementById('product-mode-container').classList.add('hidden');
      document.getElementById('story-mode-container').classList.remove('hidden');
      updateSceneDisplay();
      showToast('Returned to Executive Story Presentation');
    }

    /* ==========================================================================
       PRODUCT VIEW NAVIGATION
       ========================================================================== */
    function switchView(viewName) {
      // Update sidebar active item
      const menuItems = document.querySelectorAll('.app-sidebar .menu-item');
      menuItems.forEach(item => item.classList.remove('active'));

      // Find matching item by text or call
      const clickedItem = event ? event.currentTarget : null;
      if (clickedItem) {
        clickedItem.classList.add('active');
      }

      // Switch view panel
      const panels = document.querySelectorAll('.view-panel');
      panels.forEach(p => p.classList.remove('active'));
      const activePanel = document.getElementById(`view-${viewName}`);
      if (activePanel) {
        activePanel.classList.add('active');
      }
    }

    /* ==========================================================================
       ROLE & TIMEZONE HANDLING
       ========================================================================== */
    function onRoleChange(role) {
      currentRole = role;
      const roleProfiles = {
        'MANAGEMENT': { name: 'David Harrison', title: 'Managing Director', avatar: 'DH' },
        'TEAM_LEADER': { name: 'Priya Nair', title: 'Shift A Team Leader', avatar: 'PN' },
        'EMPLOYEE': { name: 'Rohan Sharma', title: 'Senior Keying Specialist', avatar: 'RS' },
        'SUPER_ADMIN': { name: 'Alex Vance', title: 'Super Administrator', avatar: 'AV' }
      };

      const profile = roleProfiles[role] || roleProfiles['MANAGEMENT'];
      document.getElementById('user-name-display').textContent = profile.name;
      document.getElementById('user-role-display').textContent = profile.title;
      document.getElementById('user-avatar-badge').textContent = profile.avatar;

      // Apply role-based visibility rules
      applyRolePermissions();
      showToast(`Switched active perspective to: ${profile.name} (${profile.title})`);
    }

    function applyRolePermissions() {
      // Financial loss impact card in Quality
      const finBox = document.getElementById('qc-financial-impact-box');
      if (finBox) {
        finBox.style.display = (currentRole === 'MANAGEMENT' || currentRole === 'SUPER_ADMIN') ? 'block' : 'none';
      }

      // Leave pending approvals table
      const leavePending = document.getElementById('leave-pending-container');
      if (leavePending) {
        leavePending.style.display = (currentRole === 'TEAM_LEADER' || currentRole === 'MANAGEMENT' || currentRole === 'SUPER_ADMIN') ? 'block' : 'none';
      }

      // Re-render views with new privacy/action permissions
      renderAttendanceTable();
      renderLeaveTables();
      renderQualityDetail();
    }

    function toggleTimezone() {
      currentTimezone = (currentTimezone === 'IST') ? 'AEDT' : 'IST';
      const label = document.getElementById('active-tz-label');
      if (currentTimezone === 'IST') {
        label.textContent = 'IST (India 06:17) / AEDT (Melbourne 11:47)';
      } else {
        label.textContent = 'AEDT (Melbourne 11:47) / IST (India 06:17)';
      }
      showToast(`Operational Clock Context: Primary view set to ${currentTimezone}`);
      renderCalendar();
    }

    function toggleCalendarTimezone() {
      toggleTimezone();
    }

    /* ==========================================================================
       RENDER MASTER VIEWS
       ========================================================================== */
    function renderAllViews() {
      updateKPIs();
      renderAttendanceTable();
      renderLeaveTables();
      renderProductionTable();
      renderQualityCases();
      renderQualityDetail();
      renderAwards();
      renderCalendar();
      applyRolePermissions();
    }

    function updateKPIs() {
      const totalEmp = appState.employees.length;
      const presentCount = appState.employees.filter(e => e.status === 'Present' || e.status === 'Late').length;
      const totalOrders = appState.productionRecords.reduce((acc, r) => acc + r.orders, 0);
      const totalFlashings = appState.productionRecords.reduce((acc, r) => acc + r.flashings, 0);
      const totalBits = appState.productionRecords.reduce((acc, r) => acc + r.bits, 0);

      document.getElementById('kpi-total-emp').textContent = totalEmp;
      document.getElementById('kpi-present-count').textContent = presentCount;
      document.getElementById('badge-present-count').textContent = presentCount;
      document.getElementById('kpi-orders-count').textContent = totalOrders;
      document.getElementById('kpi-flashings-count').textContent = (totalFlashings + totalBits).toLocaleString();

      const pendingLeaveCount = appState.leaveRequests.filter(l => l.status === 'Pending').length;
      document.getElementById('badge-leave-pending').textContent = `${pendingLeaveCount} pending`;

      const activeQCount = appState.qualityCases.filter(q => q.stageIndex < 4).length;
      document.getElementById('badge-quality-active').textContent = `${activeQCount} active`;
    }

    function filterDashboardShift(shift) {
      showToast(`Filtered dashboard view to: ${shift}`);
    }

    /* ==========================================================================
       ATTENDANCE MODULE
       ========================================================================== */
    function renderAttendanceTable() {
      const tbody = document.getElementById('attendance-tbody');
      tbody.innerHTML = '';

      const query = (document.getElementById('attendance-search')?.value || '').toLowerCase();
      const statusFilter = document.getElementById('attendance-filter-status')?.value || 'ALL';

      appState.employees.forEach(emp => {
        if (query && !emp.name.toLowerCase().includes(query) && !emp.team.toLowerCase().includes(query)) return;
        if (statusFilter !== 'ALL' && emp.status !== statusFilter) return;

        let statusClass = 'present';
        if (emp.status === 'Absent') statusClass = 'absent';
        else if (emp.status === 'Approved Leave') statusClass = 'leave';
        else if (emp.status === 'Late') statusClass = 'late';

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span class="user-avatar" style="width: 24px; height: 24px; font-size: 10px;">${emp.avatar}</span>
              <span style="font-weight: 500;">${emp.name}</span>
            </div>
          </td>
          <td>
            <div style="font-size: 12px; color: var(--porcelain);">${emp.team}</div>
            <div style="font-size: 10px; color: var(--steel);">${emp.role}</div>
          </td>
          <td><span style="font-family: var(--font-mono); font-size: 11px;">${emp.shift}</span></td>
          <td><span style="font-family: var(--font-mono); font-size: 11px; color: var(--steel);">${emp.checkin}</span></td>
          <td><span style="font-family: var(--font-mono); color: var(--gold);">${emp.accuracy}%</span></td>
          <td><span class="status-badge ${statusClass}">${emp.status}</span></td>
          <td>
            ${(currentRole === 'TEAM_LEADER' || currentRole === 'SUPER_ADMIN') ? 
              `<button class="btn-outline btn-sm" onclick="quickEditAttendance('${emp.id}')">Edit</button>` : 
              `<span style="color: var(--steel-dim); font-size: 11px;">View only</span>`}
          </td>
        `;
        tbody.appendChild(tr);
      });
    }

    function quickEditAttendance(empId) {
      const emp = appState.employees.find(e => e.id === empId);
      if (emp) {
        document.getElementById('att-correct-emp').value = empId;
        openModal('modal-attendance-correction');
      }
    }

    function saveAttendanceCorrection() {
      const empId = document.getElementById('att-correct-emp').value;
      const newStatus = document.getElementById('att-correct-status').value;
      const reason = document.getElementById('att-correct-reason').value;

      const emp = appState.employees.find(e => e.id === empId);
      if (emp) {
        emp.status = newStatus;
        if (newStatus === 'Present') emp.checkin = '06:05 AM';
        else if (newStatus === 'Late') emp.checkin = '06:22 AM';
        else emp.checkin = '--';

        renderAttendanceTable();
        updateKPIs();
        closeModal('modal-attendance-correction');
        showToast(`Attendance updated for ${emp.name} to '${newStatus}' (${reason})`);
      }
    }

    /* ==========================================================================
       LEAVE MANAGEMENT MODULE
       ========================================================================== */
    function renderLeaveTables() {
      // 1. Pending Approvals
      const pendingTbody = document.getElementById('leave-pending-tbody');
      pendingTbody.innerHTML = '';
      const pendingRequests = appState.leaveRequests.filter(l => l.status === 'Pending');

      document.getElementById('leave-pending-badge').textContent = `${pendingRequests.length} Requests Pending`;

      if (pendingRequests.length === 0) {
        pendingTbody.innerHTML = `<tr><td colspan="8" style="text-align: center; color: var(--steel); padding: 18px;">No pending leave requests in this shift queue.</td></tr>`;
      } else {
        pendingRequests.forEach(req => {
          const isReasonMasked = (currentRole === 'EMPLOYEE');
          const displayedReason = isReasonMasked ? '🔒 Confidential HR Record' : req.reason;

          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td><span style="font-family: var(--font-mono); color: var(--gold);">${req.id}</span></td>
            <td><strong>${req.empName}</strong></td>
            <td>${req.team}</td>
            <td><span class="status-badge leave">${req.type}</span></td>
            <td>${req.dates}</td>
            <td>${req.days}d</td>
            <td style="color: ${isReasonMasked ? 'var(--steel-dim)' : 'var(--porcelain)'}; font-style: ${isReasonMasked ? 'italic' : 'normal'};">
              ${displayedReason}
            </td>
            <td>
              <div style="display: flex; gap: 6px;">
                <button class="btn-gold btn-sm" onclick="approveLeave('${req.id}')">Approve</button>
                <button class="btn-outline btn-sm" onclick="rejectLeave('${req.id}')">Reject</button>
              </div>
            </td>
          `;
          pendingTbody.appendChild(tr);
        });
      }

      // 2. Public Team Availability
      const publicTbody = document.getElementById('leave-approved-tbody');
      publicTbody.innerHTML = '';
      const approvedRequests = appState.leaveRequests.filter(l => l.status === 'Approved');

      approvedRequests.forEach(req => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td><strong>${req.empName}</strong></td>
          <td>${req.team}</td>
          <td><span style="font-family: var(--font-mono);">${req.dates}</span></td>
          <td><span style="color: #79D1B8;">Shift Handover Assigned</span></td>
          <td><span class="status-badge leave">On Approved Leave</span></td>
        `;
        publicTbody.appendChild(tr);
      });
    }

    function approveLeave(reqId) {
      const req = appState.leaveRequests.find(l => l.id === reqId);
      if (req) {
        req.status = 'Approved';
        // Update employee attendance status
        const emp = appState.employees.find(e => e.id === req.empId);
        if (emp) {
          emp.status = 'Approved Leave';
          emp.checkin = '--';
        }
        renderAllViews();
        showToast(`Leave approved for ${req.empName}. Public availability roster updated.`);
      }
    }

    function rejectLeave(reqId) {
      const req = appState.leaveRequests.find(l => l.id === reqId);
      if (req) {
        req.status = 'Rejected';
        renderLeaveTables();
        updateKPIs();
        showToast(`Leave request ${req.id} declined.`);
      }
    }

    function submitLeaveApplication() {
      const empId = document.getElementById('leave-form-emp').value;
      const type = document.getElementById('leave-form-type').value;
      const days = parseInt(document.getElementById('leave-form-days').value) || 1;
      const dates = document.getElementById('leave-form-dates').value || '2027-03-28';
      const reason = document.getElementById('leave-form-reason').value || 'Personal commitment';

      const emp = appState.employees.find(e => e.id === empId);
      if (emp) {
        const newReq = {
          id: `LR-${Math.floor(100 + Math.random() * 900)}`,
          empId: emp.id,
          empName: emp.name,
          team: emp.team,
          type: type,
          dates: dates,
          days: days,
          reason: reason,
          status: 'Pending',
          submittedAt: '2027-03-24'
        };
        appState.leaveRequests.unshift(newReq);
        renderLeaveTables();
        updateKPIs();
        closeModal('modal-apply-leave');
        showToast(`Leave application submitted for ${emp.name}. Routed to Team Leader for approval.`);
      }
    }

    /* ==========================================================================
       DAILY PRODUCTION REPORTS
       ========================================================================== */
    function renderProductionTable() {
      const tbody = document.getElementById('production-tbody');
      tbody.innerHTML = '';

      appState.productionRecords.forEach(rec => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td><span style="font-family: var(--font-mono); color: var(--gold);">${rec.id}</span></td>
          <td><span style="font-family: var(--font-mono);">${rec.date}</span></td>
          <td><strong>${rec.empName}</strong></td>
          <td>${rec.team}</td>
          <td><span class="status-badge" style="background: rgba(147, 163, 174, 0.1); color: var(--porcelain);">${rec.shift}</span></td>
          <td><span style="font-family: var(--font-mono); font-weight: 600;">${rec.orders}</span></td>
          <td><span style="font-family: var(--font-mono); color: var(--gold);">${rec.flashings}</span></td>
          <td><span style="font-family: var(--font-mono);">${rec.bits}</span></td>
          <td><span style="font-family: var(--font-mono); color: #79D1B8;">${rec.doubleChecks}</span></td>
          <td style="font-size: 12px; color: var(--steel); max-width: 200px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${rec.remarks}</td>
          <td><span class="status-badge present">${rec.status}</span></td>
        `;
        tbody.appendChild(tr);
      });
    }

    function submitProductionReport() {
      const empId = document.getElementById('prod-form-emp').value;
      const shift = document.getElementById('prod-form-shift').value;
      const orders = parseInt(document.getElementById('prod-form-orders').value) || 0;
      const flashings = parseInt(document.getElementById('prod-form-flashings').value) || 0;
      const bits = parseInt(document.getElementById('prod-form-bits').value) || 0;
      const doubleChecks = parseInt(document.getElementById('prod-form-doublechecks').value) || 0;
      const remarks = document.getElementById('prod-form-remarks').value || 'Standard production';

      const emp = appState.employees.find(e => e.id === empId);
      if (emp) {
        const newRec = {
          id: `PR-${Math.floor(1000 + Math.random() * 9000)}`,
          date: '2027-03-24',
          empId: emp.id,
          empName: emp.name,
          team: emp.team,
          shift: shift,
          orders: orders,
          flashings: flashings,
          bits: bits,
          doubleChecks: doubleChecks,
          status: 'Approved',
          remarks: remarks
        };
        appState.productionRecords.unshift(newRec);
        renderProductionTable();
        updateKPIs();
        closeModal('modal-production-entry');
        showToast(`Shift production verified: ${flashings} flashings keyed by ${emp.name}`);
      }
    }

    function exportProductionCSV() {
      let csv = 'Record ID,Date,Keying Specialist,Team,Shift,Orders,Flashings,Bits,Double-Checks,Remarks,Status\\n';
      appState.productionRecords.forEach(r => {
        csv += `"${r.id}","${r.date}","${r.empName}","${r.team}","${r.shift}",${r.orders},${r.flashings},${r.bits},${r.doubleChecks},"${r.remarks}","${r.status}"\\n`;
      });

      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', `PULSE_Daily_Production_${new Date().toISOString().slice(0,10)}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      showToast('Export generated: Production log CSV downloaded successfully.');
    }

    /* ==========================================================================
       QUALITY & RESUPPLY INTELLIGENCE
       ========================================================================== */
    function renderQualityCases() {
      const container = document.getElementById('quality-cases-list');
      container.innerHTML = '';

      const dashContainer = document.getElementById('dashboard-quality-list');
      if (dashContainer) dashContainer.innerHTML = '';

      const stageNames = ['Reported', 'Under Investigation', 'Root Cause Verified', 'Corrective Action', 'Closed'];

      appState.qualityCases.forEach(qc => {
        const isSelected = (qc.id === activeQualityCaseId);
        const card = document.createElement('div');
        card.style.cssText = `
          padding: 12px;
          background: ${isSelected ? 'rgba(198, 166, 117, 0.12)' : 'rgba(16, 25, 35, 0.4)'};
          border: 1px solid ${isSelected ? 'var(--gold)' : 'var(--slate-border)'};
          border-radius: 6px;
          cursor: pointer;
          transition: all 0.2s;
        `;
        card.onclick = () => {
          activeQualityCaseId = qc.id;
          renderQualityCases();
          renderQualityDetail();
        };

        card.innerHTML = `
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-family: var(--font-mono); font-size: 11px; color: var(--gold);">${qc.id}</span>
            <span class="status-badge" style="background: rgba(217, 83, 79, 0.2); color: #FF9B99; font-size: 10px;">${stageNames[qc.stageIndex]}</span>
          </div>
          <div style="font-size: 13px; font-weight: 500; color: var(--porcelain); margin-bottom: 2px;">${qc.issueCategory}: ${qc.spec.slice(0, 40)}...</div>
          <div style="font-size: 11px; color: var(--steel);">${qc.client} • ${qc.orderRef}</div>
        `;
        container.appendChild(card);

        // Also append summary to Dashboard
        if (dashContainer) {
          const dashCard = document.createElement('div');
          dashCard.style.cssText = card.style.cssText;
          dashCard.innerHTML = card.innerHTML;
          dashCard.onclick = () => {
            switchView('quality');
            activeQualityCaseId = qc.id;
            renderQualityCases();
            renderQualityDetail();
          };
          dashContainer.appendChild(dashCard);
        }
      });
    }

    function renderQualityDetail() {
      const qc = appState.qualityCases.find(q => q.id === activeQualityCaseId) || appState.qualityCases[0];
      if (!qc) return;

      document.getElementById('qc-detail-id').textContent = `Case #${qc.id} (${qc.orderRef})`;
      document.getElementById('qc-detail-category').textContent = qc.issueCategory;
      document.getElementById('qc-detail-spec').textContent = qc.spec;
      document.getElementById('qc-detail-client').textContent = `Client: ${qc.client} | Date: ${qc.jobDate}`;
      document.getElementById('qc-detail-problem').textContent = qc.problem;

      document.getElementById('qc-loss-mat').textContent = `$${qc.lossMaterial} AUD`;
      document.getElementById('qc-loss-lab').textContent = `$${qc.lossLabour} AUD`;
      document.getElementById('qc-loss-fre').textContent = `$${qc.lossFreight} AUD`;

      // Update stepper visuals
      const fillPercentage = (qc.stageIndex / 4) * 100;
      document.getElementById('qc-stepper-fill').style.width = `${fillPercentage}%`;

      for (let i = 0; i <= 4; i++) {
        const stepEl = document.getElementById(`qc-step-${i}`);
        if (stepEl) {
          stepEl.classList.remove('active', 'completed');
          if (i === qc.stageIndex) stepEl.classList.add('active');
          else if (i < qc.stageIndex) stepEl.classList.add('completed');
        }
      }

      // Set root cause select value
      const rcSelect = document.getElementById('qc-root-cause-select');
      if (rcSelect) rcSelect.value = qc.selectedCause;
    }

    function setQualityStage(stageIdx) {
      const qc = appState.qualityCases.find(q => q.id === activeQualityCaseId);
      if (qc) {
        qc.stageIndex = stageIdx;
        renderQualityCases();
        renderQualityDetail();
        updateKPIs();
        showToast(`Case #${qc.id} advanced to stage: ${['Reported', 'Under Investigation', 'Root Cause Verified', 'Corrective Action', 'Closed'][stageIdx]}`);
      }
    }

    function advanceQualityCaseStage() {
      const qc = appState.qualityCases.find(q => q.id === activeQualityCaseId);
      if (qc && qc.stageIndex < 4) {
        setQualityStage(qc.stageIndex + 1);
      }
    }

    function onRootCauseChange(cause) {
      const qc = appState.qualityCases.find(q => q.id === activeQualityCaseId);
      if (qc) {
        qc.selectedCause = cause;
        showToast(`Root cause attributed to: ${cause} (Zero-blame investigation logged)`);
      }
    }

    /* ==========================================================================
       RECOGNITION & OPERATIONAL MERIT
       ========================================================================== */
    function renderAwards() {
      const container = document.getElementById('awards-grid-container');
      container.innerHTML = '';

      appState.awards.forEach(aw => {
        const card = document.createElement('div');
        card.className = 'award-card';
        card.innerHTML = `
          <div class="award-category-pill">${aw.category}</div>
          <div class="award-avatar-ring">
            <div class="award-avatar">${aw.avatar}</div>
          </div>
          <h3 class="award-winner-name">${aw.name}</h3>
          <div class="award-winner-role">${aw.role}</div>
          <p class="award-reason">"${aw.achievement}"</p>
          <div class="award-metrics-table">
            <div>
              <div class="award-m-label">Quality Score</div>
              <div class="award-m-val">${aw.scores.Quality}</div>
            </div>
            <div>
              <div class="award-m-label">Productivity</div>
              <div class="award-m-val">${aw.scores.Productivity}</div>
            </div>
            <div>
              <div class="award-m-label">Complexity</div>
              <div class="award-m-val">${aw.scores.Complexity}</div>
            </div>
            <div>
              <div class="award-m-label">Reliability</div>
              <div class="award-m-val">${aw.scores.Reliability}</div>
            </div>
          </div>
        `;
        container.appendChild(card);
      });
    }

    function submitNomination() {
      const empId = document.getElementById('nom-form-emp').value;
      const category = document.getElementById('nom-form-category').value;
      const reason = document.getElementById('nom-form-reason').value || 'Exemplary double-checking diligence';

      const emp = appState.employees.find(e => e.id === empId);
      if (emp) {
        closeModal('modal-nominate');
        showToast(`Nomination submitted for ${emp.name} (${category}). Sent to Management for endorsement.`);
      }
    }

    /* ==========================================================================
       OPERATIONS CALENDAR (AUSTRALIA & INDIA)
       ========================================================================== */
    function renderCalendar() {
      const grid = document.getElementById('calendar-cells-grid');
      grid.innerHTML = '';

      const victoriaHolidays = {
        8: 'Labour Day (VIC Public Holiday)',
        26: 'Good Friday (Melbourne Closed)',
        29: 'Easter Monday (Melbourne Closed)'
      };

      const indiaHolidays = {
        23: 'Holi Festival (India Holiday)'
      };

      for (let day = 1; day <= 31; day++) {
        const cell = document.createElement('div');
        cell.className = `cal-cell ${day === 24 ? 'today' : ''}`;

        let eventsHtml = '';

        if (victoriaHolidays[day]) {
          eventsHtml += `<div class="cal-event-tag holiday" title="${victoriaHolidays[day]}">🇦🇺 ${victoriaHolidays[day]}</div>`;
        }
        if (indiaHolidays[day]) {
          eventsHtml += `<div class="cal-event-tag leave" title="${indiaHolidays[day]}">🇮🇳 ${indiaHolidays[day]}</div>`;
        }

        if (day >= 24 && day <= 26) {
          eventsHtml += `<div class="cal-event-tag shift">Shift A: 82 Orders</div>`;
        }

        cell.innerHTML = `
          <div class="cal-date">${day} ${day === 24 ? '• Today' : ''}</div>
          ${eventsHtml}
        `;
        grid.appendChild(cell);
      }
    }

    /* ==========================================================================
       UTILITY: DROPDOWNS, MODALS, TOASTS & RESET
       ========================================================================== */
    function populateDropdowns() {
      const leaveEmpSelect = document.getElementById('leave-form-emp');
      const prodEmpSelect = document.getElementById('prod-form-emp');
      const attEmpSelect = document.getElementById('att-correct-emp');
      const nomEmpSelect = document.getElementById('nom-form-emp');

      if (leaveEmpSelect) leaveEmpSelect.innerHTML = '';
      if (prodEmpSelect) prodEmpSelect.innerHTML = '';
      if (attEmpSelect) attEmpSelect.innerHTML = '';
      if (nomEmpSelect) nomEmpSelect.innerHTML = '';

      appState.employees.forEach(emp => {
        const opt = `<option value="${emp.id}">${emp.name} (${emp.team})</option>`;
        if (leaveEmpSelect) leaveEmpSelect.innerHTML += opt;
        if (prodEmpSelect) prodEmpSelect.innerHTML += opt;
        if (attEmpSelect) attEmpSelect.innerHTML += opt;
        if (nomEmpSelect) nomEmpSelect.innerHTML += opt;
      });
    }

    function openModal(modalId) {
      const modal = document.getElementById(modalId);
      if (modal) modal.classList.add('active');
    }

    function closeModal(modalId) {
      const modal = document.getElementById(modalId);
      if (modal) modal.classList.remove('active');
    }

    function openApplyLeaveModal() { openModal('modal-apply-leave'); }
    function openProductionModal() { openModal('modal-production-entry'); }
    function openAttendanceCorrectionModal() { openModal('modal-attendance-correction'); }
    function openNominationModal() { openModal('modal-nominate'); }

    function showToast(message) {
      const container = document.getElementById('toast-container');
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
  </script>
</body>
</html>
"""

final_html = html_template.replace("__INITIAL_DATA_PLACEHOLDER__", json_data_str)

OUTPUT_FILE = "/Users/raksh/.gemini/antigravity/scratch/pulse-showcase/pulse-executive-showcase.html"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(final_html)

print("SUCCESS: Standalone Pulse Executive Showcase HTML created!")
print(f"File: {OUTPUT_FILE}")
print(f"Size: {os.path.getsize(OUTPUT_FILE):,} bytes")
