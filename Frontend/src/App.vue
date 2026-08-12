<script setup>
import { ref, computed, nextTick } from 'vue'
import Sidebar from './components/Sidebar.vue'
import MessageBubble from './components/MessageBubble.vue'
import ComposerBar from './components/ComposerBar.vue'
import { sendChatMessage } from './api.js'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000'

const messages = ref([])
const sending = ref(false)
const connected = ref(true)
const activeDocument = ref(null)
const currentMode = ref(null)
const threadEl = ref(null)

const messageCount = computed(() => messages.value.length)

function timestamp() {
  return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
}

async function scrollToEnd() {
  await nextTick()
  threadEl.value?.scrollTo({ top: threadEl.value.scrollHeight, behavior: 'smooth' })
}

async function handleSend({ message, file }) {
  messages.value.push({
    role: 'user',
    text: message,
    fileName: file ? file.name : null,
    time: timestamp()
  })
  scrollToEnd()

  sending.value = true
  try {
    const data = await sendChatMessage(message, file)
    connected.value = true
    currentMode.value = data.mode || null
    if (file) activeDocument.value = file.name

    messages.value.push({
      role: 'assistant',
      text: data.response ?? '(no response returned)',
      mode: data.mode,
      sources: data.sources || [],
      time: timestamp()
    })
  } catch (err) {
    connected.value = false
    messages.value.push({
      role: 'error',
      text: `Something went wrong reaching the backend: ${err.message}`,
      time: timestamp()
    })
  } finally {
    sending.value = false
    scrollToEnd()
  }
}
</script>

<template>
  <div class="shell">
    <Sidebar
      :active-document="activeDocument"
      :message-count="messageCount"
      :current-mode="currentMode"
      :connected="connected"
      :api-base="API_BASE_URL"
    />

    <main class="thread-col">
      <div class="thread" ref="threadEl">
        <div v-if="messages.length === 0" class="empty">
          <div class="empty-mark">§</div>
          <h2>Start a conversation</h2>
          <p>
            Ask a general question, or attach a document to have answers
            grounded in it, with sources cited beneath each reply.
          </p>
        </div>

        <MessageBubble
          v-for="(m, i) in messages"
          :key="i"
          :role="m.role"
          :text="m.text"
          :mode="m.mode"
          :sources="m.sources"
          :file-name="m.fileName"
          :time="m.time"
        />

        <div v-if="sending" class="row assistant thinking">
          <div class="bubble">
            <span class="dot-flash"></span>
            <span class="dot-flash"></span>
            <span class="dot-flash"></span>
          </div>
        </div>
      </div>

      <ComposerBar :disabled="sending" @send="handleSend" />
    </main>
  </div>
</template>

<style scoped>
.shell {
  display: flex;
  height: 100vh;
}

.thread-col {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.thread {
  flex: 1;
  overflow-y: auto;
  padding: 28px 24px 8px;
  max-width: 880px;
  width: 100%;
  margin: 0 auto;
}

.empty {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: var(--paper-dim);
  padding: 40px;
}
.empty-mark {
  font-family: var(--font-display);
  font-size: 2.4rem;
  color: var(--amber);
  margin-bottom: 8px;
}
.empty h2 {
  font-family: var(--font-display);
  font-weight: 500;
  margin: 0 0 8px;
  color: var(--paper);
}
.empty p {
  max-width: 380px;
  font-size: 0.88rem;
  line-height: 1.6;
  margin: 0;
}

.row.assistant.thinking .bubble {
  background: var(--ink-raised);
  border: 1px solid var(--ink-line);
  display: flex;
  gap: 5px;
  padding: 14px 16px;
}
.dot-flash {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--muted);
  animation: flash 1.1s infinite ease-in-out;
}
.dot-flash:nth-child(2) {
  animation-delay: 0.15s;
}
.dot-flash:nth-child(3) {
  animation-delay: 0.3s;
}
@keyframes flash {
  0%, 80%, 100% {
    opacity: 0.25;
  }
  40% {
    opacity: 1;
  }
}

@media (max-width: 720px) {
  .shell {
    flex-direction: column;
  }
}
</style>
