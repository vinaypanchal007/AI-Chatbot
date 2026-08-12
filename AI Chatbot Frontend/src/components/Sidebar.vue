<script setup>
defineProps({
  activeDocument: { type: String, default: null },
  messageCount: { type: Number, default: 0 },
  currentMode: { type: String, default: null },
  connected: { type: Boolean, default: true },
  apiBase: { type: String, required: true }
})
</script>

<template>
  <aside class="sidebar">
    <div class="brand">
      <span class="brand-mark">A&amp;A</span>
      <div>
        <h1>Archive &amp; Answer</h1>
        <p>Document-aware chat</p>
      </div>
    </div>

    <div class="ledger">
      <div class="ledger-title">Session ledger</div>

      <dl>
        <div class="row">
          <dt>Status</dt>
          <dd>
            <span class="dot" :class="connected ? 'ok' : 'bad'"></span>
            {{ connected ? 'Ready' : 'Unreachable' }}
          </dd>
        </div>
        <div class="row">
          <dt>Mode</dt>
          <dd>{{ currentMode || '—' }}</dd>
        </div>
        <div class="row">
          <dt>Document</dt>
          <dd class="doc" :title="activeDocument || ''">{{ activeDocument || 'none attached' }}</dd>
        </div>
        <div class="row">
          <dt>Messages</dt>
          <dd>{{ messageCount }}</dd>
        </div>
      </dl>
    </div>

    <div class="how">
      <div class="ledger-title">How it works</div>
      <ol>
        <li>Ask a question directly for general chat.</li>
        <li>Attach a PDF, DOCX, TXT, or image to ground answers in that document.</li>
        <li>Cited excerpts appear beneath grounded answers.</li>
      </ol>
    </div>

    <div class="endpoint">
      <span class="ledger-title">Backend</span>
      <code>{{ apiBase }}</code>
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 260px;
  flex: none;
  background: var(--ink-raised);
  border-right: 1px solid var(--ink-line);
  padding: 22px 20px;
  display: flex;
  flex-direction: column;
  gap: 26px;
  height: 100%;
  overflow-y: auto;
}

.brand {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}
.brand-mark {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  letter-spacing: 0.06em;
  border: 1px solid var(--amber);
  color: var(--amber);
  padding: 4px 6px;
  border-radius: 2px;
  flex: none;
}
.brand h1 {
  font-family: var(--font-display);
  font-weight: 500;
  font-size: 1.15rem;
  margin: 0 0 2px;
  color: var(--paper);
}
.brand p {
  margin: 0;
  font-size: 0.72rem;
  color: var(--muted);
}

.ledger-title {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--verdigris);
  margin-bottom: 10px;
}

dl {
  margin: 0;
  border-top: 1px dashed var(--ink-line);
}
.row {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  padding: 8px 0;
  border-bottom: 1px dashed var(--ink-line);
  font-size: 0.8rem;
}
dt {
  color: var(--muted);
}
dd {
  margin: 0;
  color: var(--paper);
  text-align: right;
  display: flex;
  align-items: center;
  gap: 6px;
  max-width: 150px;
}
.doc {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  flex: none;
}
.dot.ok {
  background: var(--verdigris);
}
.dot.bad {
  background: var(--danger);
}

.how ol {
  margin: 0;
  padding-left: 18px;
  color: var(--paper-dim);
  font-size: 0.78rem;
  line-height: 1.6;
}

.endpoint {
  margin-top: auto;
  padding-top: 16px;
  border-top: 1px dashed var(--ink-line);
}
.endpoint code {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  color: var(--paper-dim);
  word-break: break-all;
}

@media (max-width: 720px) {
  .sidebar {
    width: 100%;
    height: auto;
    max-height: 40vh;
    border-right: none;
    border-bottom: 1px solid var(--ink-line);
  }
}
</style>
