<script setup>
defineProps({
  role: { type: String, required: true }, // 'user' | 'assistant' | 'error'
  text: { type: String, required: true },
  mode: { type: String, default: null },
  sources: { type: Array, default: () => [] },
  fileName: { type: String, default: null },
  time: { type: String, default: '' }
})
</script>

<template>
  <div class="row" :class="role">
    <div class="bubble">
      <div v-if="fileName" class="attachment">
        <span class="pin"></span>
        <span class="attachment-name">{{ fileName }}</span>
      </div>

      <p class="text">{{ text }}</p>

      <div class="meta">
        <span v-if="mode" class="tag" :class="mode === 'RAG' ? 'tag-rag' : 'tag-general'">{{ mode }}</span>
        <span class="time">{{ time }}</span>
      </div>

      <div v-if="sources && sources.length" class="sources">
        <div class="sources-label">Sources</div>
        <div class="cards">
          <details v-for="(src, i) in sources" :key="i" class="card">
            <summary>
              <span class="card-index">{{ String(i + 1).padStart(2, '0') }}</span>
              <span class="card-hint">excerpt</span>
            </summary>
            <pre class="card-body">{{ typeof src === 'string' ? src : JSON.stringify(src, null, 2) }}</pre>
          </details>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.row {
  display: flex;
  margin: 0 0 18px;
}
.row.user {
  justify-content: flex-end;
}
.row.assistant,
.row.error {
  justify-content: flex-start;
}

.bubble {
  max-width: min(640px, 82%);
  padding: 14px 16px;
  border-radius: 3px;
  position: relative;
  line-height: 1.55;
}

.row.user .bubble {
  background: var(--vellum);
  color: #1c1a13;
  border-top-right-radius: 2px;
}

.row.assistant .bubble {
  background: var(--ink-raised);
  border: 1px solid var(--ink-line);
  color: var(--paper);
  border-top-left-radius: 2px;
}

.row.error .bubble {
  background: rgba(185, 88, 63, 0.12);
  border: 1px solid var(--danger);
  color: var(--paper);
}

.text {
  margin: 0;
  font-size: 0.96rem;
  white-space: pre-wrap;
  word-break: break-word;
}

.attachment {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.02em;
  margin-bottom: 8px;
  padding-bottom: 8px;
  border-bottom: 1px dashed rgba(0, 0, 0, 0.2);
  opacity: 0.85;
}
.row.assistant .attachment {
  border-bottom-color: var(--ink-line);
}
.pin {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--amber);
  flex: none;
}

.meta {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 8px;
}
.tag {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 2px 6px;
  border-radius: 2px;
}
.tag-rag {
  background: rgba(92, 143, 129, 0.18);
  color: var(--verdigris);
}
.tag-general {
  background: rgba(201, 138, 44, 0.16);
  color: var(--amber);
}
.time {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  color: var(--muted);
}
.row.user .time {
  color: #6b6552;
}

.sources {
  margin-top: 12px;
  padding-top: 10px;
  border-top: 1px dashed var(--ink-line);
}
.sources-label {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--verdigris);
  margin-bottom: 6px;
}
.cards {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.card {
  background: var(--ink);
  border: 1px solid var(--ink-line);
  border-radius: 2px;
}
.card summary {
  cursor: pointer;
  list-style: none;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 7px 10px;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--paper-dim);
}
.card summary::-webkit-details-marker {
  display: none;
}
.card-index {
  color: var(--amber);
}
.card-hint {
  color: var(--muted);
}
.card-body {
  margin: 0;
  padding: 0 10px 10px;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  line-height: 1.5;
  color: var(--paper-dim);
  white-space: pre-wrap;
  word-break: break-word;
}
</style>
