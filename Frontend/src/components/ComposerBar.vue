<script setup>
import { ref } from 'vue'

const props = defineProps({
  disabled: { type: Boolean, default: false }
})
const emit = defineEmits(['send'])

const text = ref('')
const file = ref(null)
const fileInput = ref(null)

function pickFile() {
  fileInput.value?.click()
}

function onFileChange(e) {
  file.value = e.target.files?.[0] || null
}

function clearFile() {
  file.value = null
  if (fileInput.value) fileInput.value.value = ''
}

function submit() {
  const trimmed = text.value.trim()
  if (!trimmed || props.disabled) return
  emit('send', { message: trimmed, file: file.value })
  text.value = ''
  clearFile()
}

function onKeydown(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault()
    submit()
  }
}
</script>

<template>
  <div class="composer">
    <div v-if="file" class="staged">
      <span class="pin"></span>
      <span class="staged-name">{{ file.name }}</span>
      <button type="button" class="staged-remove" @click="clearFile" aria-label="Remove attached file">
        ×
      </button>
    </div>

    <div class="input-row">
      <button
        type="button"
        class="attach-btn"
        @click="pickFile"
        :disabled="disabled"
        title="Attach a document"
        aria-label="Attach a document"
      >
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
          <path d="M21 11.5V7a2 2 0 0 0-2-2H8.5L4 9.5V19a2 2 0 0 0 2 2h6" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M4 9.5H8.5V5" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M15 15v4M13 17h4" stroke-linecap="round"/>
        </svg>
      </button>
      <input
        ref="fileInput"
        type="file"
        class="hidden-input"
        accept=".pdf,.docx,.txt,.png,.jpg,.jpeg"
        @change="onFileChange"
      />

      <textarea
        v-model="text"
        rows="1"
        class="text-input"
        placeholder="Ask a question, or attach a document first…"
        :disabled="disabled"
        @keydown="onKeydown"
      ></textarea>

      <button type="button" class="send-btn" :disabled="disabled || !text.trim()" @click="submit">
        {{ disabled ? 'Sending…' : 'Send' }}
      </button>
    </div>
    <p class="hint">Enter to send · Shift+Enter for a new line</p>
  </div>
</template>

<style scoped>
.composer {
  border-top: 1px solid var(--ink-line);
  background: var(--ink-raised);
  padding: 12px 20px 14px;
}

.staged {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  background: var(--ink);
  border: 1px solid var(--ink-line);
  border-radius: 2px;
  padding: 5px 8px;
  margin-bottom: 8px;
  color: var(--paper-dim);
}
.pin {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--amber);
  flex: none;
}
.staged-remove {
  background: none;
  border: none;
  color: var(--muted);
  cursor: pointer;
  font-size: 0.9rem;
  line-height: 1;
  padding: 0 2px;
}
.staged-remove:hover {
  color: var(--danger);
}

.input-row {
  display: flex;
  align-items: flex-end;
  gap: 8px;
}

.hidden-input {
  display: none;
}

.attach-btn {
  flex: none;
  width: 38px;
  height: 38px;
  border-radius: 2px;
  border: 1px solid var(--ink-line);
  background: var(--ink);
  color: var(--paper-dim);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
.attach-btn:hover:not(:disabled) {
  border-color: var(--amber);
  color: var(--amber);
}
.attach-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.text-input {
  flex: 1;
  resize: none;
  background: var(--ink);
  border: 1px solid var(--ink-line);
  border-radius: 2px;
  color: var(--paper);
  font-family: var(--font-body);
  font-size: 0.92rem;
  padding: 9px 12px;
  max-height: 160px;
  line-height: 1.4;
}
.text-input:focus {
  border-color: var(--amber);
}
.text-input::placeholder {
  color: var(--muted);
}

.send-btn {
  flex: none;
  background: var(--amber);
  color: #1c1300;
  border: none;
  border-radius: 2px;
  padding: 10px 16px;
  font-weight: 600;
  font-size: 0.85rem;
  cursor: pointer;
}
.send-btn:hover:not(:disabled) {
  background: #dd9c37;
}
.send-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.hint {
  margin: 8px 2px 0;
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: var(--muted);
}
</style>
