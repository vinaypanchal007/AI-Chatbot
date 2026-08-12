<script setup>
import { ref, computed, nextTick } from 'vue'
import Sidebar from './components/Sidebar.vue'
import MessageBubble from './components/MessageBubble.vue'
import ComposerBar from './components/ComposerBar.vue'
import LimitationsView from './components/LimitationsView.vue'
import { sendChatMessage } from './api.js'
import './styles/app.css'

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
          <LimitationsView />
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

