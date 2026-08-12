<script setup>
import '../styles/message-bubble.css'

const props = defineProps({
  role: { type: String, required: true }, // 'user' | 'assistant' | 'error'
  text: { type: String, required: true },
  mode: { type: String, default: null },
  sources: { type: Array, default: () => [] },
  fileName: { type: String, default: null },
  time: { type: String, default: '' }
})

function formatText(value) {
  if (!value) return ''

  return value
    .replace(/\n{3,}/g, '<br><br>')
    .replace(/\n/g, '<br>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/`(.+?)`/g, '<code>$1</code>')
    .replace(/^(#{1,6})\s+(.*)$/gm, '<h$1>$2</h$1>')
    .replace(/^\s*[-*]\s+(.*)$/gm, '<li>$1</li>')
    .replace(/(<li>.*<\/li>)/gs, '<ul>$1</ul>')
    .replace(/^(\d+\.\s+.*)$/gm, '<div class="numbered-item">$1</div>')
    .replace(/\|/g, '<span class="pipe">|</span>')
}
</script>

<template>
  <div class="row" :class="role">
    <div class="bubble">
      <div v-if="fileName" class="attachment">
        <span class="pin"></span>
        <span class="attachment-name">{{ fileName }}</span>
      </div>

      <div class="text" v-html="formatText(text)"></div>

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

